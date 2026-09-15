#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vida_util_arrhenius.py — Vida util estimada desde un estudio acelerado: Arrhenius y regla Q10.

QUE CALCULA
  1) q10        : extrapola la vida util de una condicion acelerada a una condicion real usando la
                  regla Q10 (por cada 10 C de aumento, la velocidad de degradacion se multiplica por Q10).
  2) arrhenius  : lo mismo pero con la ecuacion de Arrhenius y una energia de activacion Ea.
  3) ea         : calcula la Ea a partir de DOS estudios a temperaturas distintas (esto es lo correcto:
                  medir Ea, no suponerla).
  4) desde-perdida : convierte "perdi X % del activo en N meses a T C" en una constante de degradacion
                  de primer orden y en el tiempo hasta el limite de especificacion; luego extrapola.
  5) q10-a-ea   : traduce un Q10 supuesto a la Ea equivalente entre dos temperaturas (y al reves),
                  para que veas si el Q10 que estas usando implica una Ea quimicamente creible.

FORMULAS
  Regla Q10 (empirica):
      t_real = t_acelerado x Q10^((T_acelerado - T_real)/10)          T en Celsius

  Arrhenius:
      k = A exp(-Ea/(R T))     ->   k_real/k_acel = exp( -Ea/R x (1/T_real - 1/T_acel) )
      t_real = t_acelerado x exp( Ea/R x (1/T_real - 1/T_acel) )       T en KELVIN
      (como T_real < T_acel, el exponente es positivo y la vida util se alarga)

  Ea desde dos estudios (t = vida util observada, que va como 1/k):
      t = (1/A) exp(Ea/(R T))  ->  ln(t2/t1) = Ea/R x (1/T2 - 1/T1)
      Ea = R x ln(t2/t1) / (1/T2 - 1/T1)      con t1 a T1 y t2 a T2, ambas en KELVIN

  Degradacion de primer orden:
      C(t) = C0 exp(-k t)  ->  k = -ln(C/C0)/t  ->  t_limite = -ln(C_limite/C0)/k

  Equivalencia Q10 <-> Ea (entre T1 y T2, en Kelvin):
      Ea = R ln(Q10) / (1/T1 - 1/T2)   evaluado con T2 = T1 + 10 K

DE DONDE SALE
  - ICH Q1A(R2) (estabilidad de nuevos productos) y ICH Q1E (evaluacion de datos de estabilidad):
    el marco de condiciones aceleradas (tipicamente 40 C / 75 % HR) y de extrapolacion.
  - La ecuacion de Arrhenius (1889) y la regla Q10, que es su simplificacion practica.

CUANDO **NO** APLICA (leelo antes de usar el numero)
  - Cuando el mecanismo de degradacion CAMBIA con la temperatura: fusion de una grasa, transicion
    vitrea, un excipiente que se funde, una reaccion nueva que solo arranca a 40 C. Ahi la extrapolacion
    miente y suele ser OPTIMISTA.
  - Cuando la degradacion NO es de primer orden (autocatalitica, orden cero, difusion limitante).
  - Cuando el problema NO es quimico sino fisico o microbiologico: separacion de fases, migracion de
    humedad por el envase, crecimiento de mohos, oxidacion por permeabilidad al oxigeno. Arrhenius no
    modela nada de eso.
  - Cuando lo limitante es la HUMEDAD y no la temperatura (tipico en polvos de hongos higroscopicos).
  - En productos con activos volatiles (terpenos): a 40 C se pierden por evaporacion, no por reaccion.

QUE **NO** HACE
  - No reemplaza el estudio en tiempo real. La extrapolacion sirve para PONER una fecha provisional y
    priorizar; la fecha definitiva la da el estudio a largo plazo (ICH Q1A: 12 meses minimo).
  - No calcula intervalos de confianza ni el limite inferior del 95 % que exige ICH Q1E.
  - No modela humedad relativa ni el efecto del envase.
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP

getcontext().prec = 34

R_GAS = Decimal("8.314462618")   # J/(mol K)
CERO_C = Decimal("273.15")


class ErrorDeEntrada(Exception):
    pass


def dec(texto):
    try:
        return Decimal(str(texto).strip().replace(" ", "").replace(",", "."))
    except (InvalidOperation, ValueError):
        raise argparse.ArgumentTypeError("'%s' no es un numero valido" % texto)


def exigir(condicion, mensaje):
    if not condicion:
        raise ErrorDeEntrada(mensaje)


def n(x, d=4):
    return str(Decimal(x).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP))


def kelvin(celsius):
    exigir(celsius > -CERO_C, "La temperatura no puede estar por debajo del cero absoluto (-273,15 C).")
    return celsius + CERO_C


# ----------------------------------------------------------------------------- calculo

def por_q10(t_acelerado, temp_acel_c, temp_real_c, q10):
    exigir(t_acelerado > 0, "El tiempo del estudio acelerado debe ser mayor que cero.")
    exigir(q10 > 1, "Q10 debe ser mayor que 1 (valores tipicos: 2 a 4). Un Q10 <= 1 diria que el "
                    "producto se degrada mas despacio al calentarlo.")
    exigir(q10 <= 10, "Q10 mayor que 10 no es creible para degradacion quimica: revisa el dato.")
    exigir(temp_acel_c > temp_real_c,
           "La temperatura acelerada (%s C) debe ser MAYOR que la real (%s C). Si no, no estas "
           "acelerando nada." % (temp_acel_c, temp_real_c))
    kelvin(temp_acel_c), kelvin(temp_real_c)
    exponente = (temp_acel_c - temp_real_c) / Decimal(10)
    factor = q10 ** exponente
    return {"factor": factor, "vida_util": t_acelerado * factor, "delta_t": temp_acel_c - temp_real_c}


def por_arrhenius(t_acelerado, temp_acel_c, temp_real_c, ea):
    exigir(t_acelerado > 0, "El tiempo del estudio acelerado debe ser mayor que cero.")
    exigir(ea > 0, "La energia de activacion debe ser mayor que cero.")
    exigir(ea < Decimal("500000"),
           "Ea mayor a 500 kJ/mol no es creible para degradacion en estado solido o solucion.")
    exigir(temp_acel_c > temp_real_c,
           "La temperatura acelerada debe ser MAYOR que la real.")
    ta = kelvin(temp_acel_c)
    tr = kelvin(temp_real_c)
    exponente = (ea / R_GAS) * ((Decimal(1) / tr) - (Decimal(1) / ta))
    factor = exponente.exp()
    return {"factor": factor, "vida_util": t_acelerado * factor, "exponente": exponente}


def ea_desde_dos_estudios(t1, temp1_c, t2, temp2_c):
    """t1 a temp1 y t2 a temp2 (vidas utiles observadas). Devuelve Ea en J/mol."""
    exigir(t1 > 0 and t2 > 0, "Los tiempos observados deben ser mayores que cero.")
    exigir(temp1_c != temp2_c, "Las dos temperaturas deben ser distintas.")
    k1 = kelvin(temp1_c)
    k2 = kelvin(temp2_c)
    # t = (1/A) exp(Ea/RT)  ->  ln(t2/t1) = Ea/R x (1/T2 - 1/T1)
    ea = R_GAS * (t2 / t1).ln() / ((Decimal(1) / k2) - (Decimal(1) / k1))
    exigir(ea > 0, "La Ea sale negativa: tus datos dicen que el producto dura MAS a mayor temperatura. "
                   "O hay un error de medicion, o el mecanismo no es el que crees.")
    return ea


def q10_a_ea(q10, temp_ref_c):
    exigir(q10 > 1, "Q10 debe ser mayor que 1.")
    t1 = kelvin(temp_ref_c)
    t2 = t1 + Decimal(10)
    return R_GAS * q10.ln() / ((Decimal(1) / t1) - (Decimal(1) / t2))


def ea_a_q10(ea, temp_ref_c):
    exigir(ea > 0, "La energia de activacion debe ser mayor que cero.")
    t1 = kelvin(temp_ref_c)
    t2 = t1 + Decimal(10)
    return ((ea / R_GAS) * ((Decimal(1) / t1) - (Decimal(1) / t2))).exp()


def desde_perdida(conc_inicial, conc_final, tiempo, limite_spec):
    """Primer orden: k desde una perdida observada, y tiempo hasta el limite de especificacion."""
    exigir(conc_inicial > 0, "La concentracion inicial debe ser mayor que cero.")
    exigir(conc_final > 0, "La concentracion final debe ser mayor que cero (si llego a 0 el modelo "
                           "exponencial no aplica).")
    exigir(conc_final < conc_inicial, "La concentracion final debe ser MENOR que la inicial: si no, "
                                      "no hay degradacion que modelar.")
    exigir(tiempo > 0, "El tiempo del estudio debe ser mayor que cero.")
    exigir(0 < limite_spec < conc_inicial,
           "El limite de especificacion debe estar entre 0 y la concentracion inicial.")
    k = -((conc_final / conc_inicial).ln()) / tiempo
    t_limite = -((limite_spec / conc_inicial).ln()) / k
    return {
        "k": k,
        "vida_media": Decimal(2).ln() / k,
        "t_limite": t_limite,
        "perdida_pct": (conc_inicial - conc_final) * Decimal(100) / conc_inicial,
    }


# ----------------------------------------------------------------------------- autotest

class _T:
    def __init__(self):
        self.fallos = []
        self.n = 0

    def cerca(self, nombre, obtenido, esperado, tol="1e-9"):
        self.n += 1
        o, e, t = Decimal(str(obtenido)), Decimal(str(esperado)), Decimal(str(tol))
        if abs(o - e) > t:
            self.fallos.append("FALLA %s: obtenido %s, esperado %s (tolerancia %s)" % (nombre, o, e, t))
        else:
            print("  ok  %-58s %s" % (nombre, o))

    def cierto(self, nombre, condicion, detalle=""):
        self.n += 1
        if condicion:
            print("  ok  %-58s %s" % (nombre, "cumple"))
        else:
            self.fallos.append("FALLA %s: %s" % (nombre, detalle))

    def resultado(self):
        if self.fallos:
            print("")
            for f in self.fallos:
                print("  " + f)
            print("")
            print("FALLARON %d de %d pruebas" % (len(self.fallos), self.n))
            return 1
        print("")
        print("OK - %d pruebas pasaron (vida_util_arrhenius.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST vida_util_arrhenius.py")

    # 1. Q10 = 2, de 40 C a 25 C, 3 meses de estudio acelerado
    q = por_q10(Decimal("3"), Decimal("40"), Decimal("25"), Decimal("2"))
    t.cerca("factor Q10=2 para 15 C de diferencia (2^1,5)", q["factor"], "2.8284271247461901", "1e-12")
    t.cerca("vida util extrapolada [meses]", q["vida_util"], "8.4852813742385702", "1e-12")
    # segunda via: 6 meses acelerados a 40 C equivalen a 2 anios a 25 C (regla de oro conocida)
    q2 = por_q10(Decimal("6"), Decimal("40"), Decimal("25"), Decimal("4"))
    t.cerca("regla clasica: 6 meses a 40 C con Q10=4 -> 24 meses", q2["vida_util"], "48", "1e-12")

    # 2. VERIFICACION POR SEGUNDA VIA: Q10 traducido a Ea debe dar el MISMO factor por Arrhenius
    ea_equiv = q10_a_ea(Decimal("2"), Decimal("25"))
    a = por_arrhenius(Decimal("3"), Decimal("40"), Decimal("25"), ea_equiv)
    t.cerca("Ea equivalente a Q10=2 a 25 C [kJ/mol]", ea_equiv / 1000, "52.9489", "1e-3")
    t.cierto("Arrhenius con esa Ea da un factor parecido al de Q10 (<2 % de diferencia)",
             abs(a["factor"] - q["factor"]) * 100 / q["factor"] < Decimal("2"),
             "factores: %s vs %s" % (a["factor"], q["factor"]))
    # inversa exacta: Ea -> Q10 -> Ea
    t.cerca("inversa: Ea -> Q10 devuelve 2", ea_a_q10(ea_equiv, Decimal("25")), "2", "1e-12")

    # 3. Arrhenius puro y su inversa
    a2 = por_arrhenius(Decimal("6"), Decimal("40"), Decimal("25"), Decimal("83000"))
    t.cierto("Ea 83 kJ/mol de 40 a 25 C multiplica la vida util por 4-6",
             Decimal("4") < a2["factor"] < Decimal("6"), "factor=%s" % a2["factor"])
    # INVERSA: recuperar Ea desde el par de vidas utiles
    ea_rec = ea_desde_dos_estudios(Decimal("6"), Decimal("40"), a2["vida_util"], Decimal("25"))
    t.cerca("inversa: Ea recuperada desde las dos vidas utiles", ea_rec, "83000", "1e-6")

    # 4. Monotonia fisica
    t.cierto("mas diferencia de temperatura -> mas vida util extrapolada",
             por_q10(Decimal("3"), Decimal("50"), Decimal("25"), Decimal("2"))["vida_util"] > q["vida_util"], "no")
    t.cierto("mayor Q10 -> mayor extrapolacion",
             por_q10(Decimal("3"), Decimal("40"), Decimal("25"), Decimal("3"))["vida_util"] > q["vida_util"], "no")
    t.cierto("mayor Ea -> mayor extrapolacion",
             por_arrhenius(Decimal("6"), Decimal("40"), Decimal("25"), Decimal("100000"))["factor"] > a2["factor"], "no")

    # 5. Degradacion de primer orden desde una perdida observada
    d = desde_perdida(Decimal("100"), Decimal("90"), Decimal("6"), Decimal("90"))
    t.cerca("perdida observada [%]", d["perdida_pct"], "10", "1e-12")
    t.cerca("t hasta el limite = el propio tiempo del estudio [meses]", d["t_limite"], "6", "1e-12")
    # segunda via: reconstruir la concentracion final con la k obtenida
    reconstruida = Decimal("100") * (-d["k"] * Decimal("6")).exp()
    t.cerca("segunda via: C reconstruida con k", reconstruida, "90", "1e-12")
    d2 = desde_perdida(Decimal("100"), Decimal("90"), Decimal("6"), Decimal("95"))
    t.cierto("con limite mas exigente (95 %) la vida util es MENOR",
             d2["t_limite"] < d["t_limite"], "%s >= %s" % (d2["t_limite"], d["t_limite"]))
    t.cerca("vida media coherente con k", d["vida_media"] * d["k"], Decimal(2).ln(), "1e-20")

    # 6. Cadena completa: perdida a 40 C -> t_limite -> extrapolar a 25 C
    cadena = por_q10(d["t_limite"], Decimal("40"), Decimal("25"), Decimal("2"))
    t.cerca("cadena completa: vida util a 25 C [meses]", cadena["vida_util"], "16.9705627484771404", "1e-10")

    # 7. Validaciones
    for descripcion, fn in [
        ("rechaza Q10 igual a 1", lambda: por_q10(Decimal("3"), Decimal("40"), Decimal("25"), Decimal("1"))),
        ("rechaza Q10 mayor a 10", lambda: por_q10(Decimal("3"), Decimal("40"), Decimal("25"), Decimal("15"))),
        ("rechaza T acelerada menor que la real",
         lambda: por_q10(Decimal("3"), Decimal("20"), Decimal("25"), Decimal("2"))),
        ("rechaza tiempo de estudio 0", lambda: por_q10(Decimal("0"), Decimal("40"), Decimal("25"), Decimal("2"))),
        ("rechaza Ea negativa", lambda: por_arrhenius(Decimal("3"), Decimal("40"), Decimal("25"), Decimal("-1"))),
        ("rechaza Ea absurda (> 500 kJ/mol)",
         lambda: por_arrhenius(Decimal("3"), Decimal("40"), Decimal("25"), Decimal("900000"))),
        ("rechaza T bajo cero absoluto", lambda: kelvin(Decimal("-300"))),
        ("rechaza dos estudios a la misma temperatura",
         lambda: ea_desde_dos_estudios(Decimal("3"), Decimal("40"), Decimal("6"), Decimal("40"))),
        ("rechaza Ea negativa implicita (dura mas al calentar)",
         lambda: ea_desde_dos_estudios(Decimal("12"), Decimal("40"), Decimal("6"), Decimal("25"))),
        ("rechaza concentracion final mayor que la inicial",
         lambda: desde_perdida(Decimal("90"), Decimal("100"), Decimal("6"), Decimal("80"))),
        ("rechaza limite de spec por encima del inicial",
         lambda: desde_perdida(Decimal("100"), Decimal("90"), Decimal("6"), Decimal("110"))),
    ]:
        try:
            fn()
            t.cierto(descripcion, False, "no lanzo ErrorDeEntrada")
        except ErrorDeEntrada:
            t.cierto(descripcion, True)

    return t.resultado()


# ----------------------------------------------------------------------------- CLI

ADVERTENCIA = """
  SUPUESTOS QUE ESTAS ACEPTANDO AL USAR ESTE NUMERO:
    1. El mecanismo de degradacion es EL MISMO a la temperatura acelerada y a la real.
    2. La degradacion sigue cinetica de primer orden.
    3. Lo limitante es la temperatura, no la humedad, ni el oxigeno, ni el envase, ni los microbios.
  SI ALGUNO NO SE CUMPLE, LA EXTRAPOLACION MIENTE — y casi siempre miente hacia el lado OPTIMISTA.
  Esta cifra sirve para poner una fecha PROVISIONAL y priorizar. La fecha definitiva la da el estudio
  en tiempo real (ICH Q1A(R2): minimo 12 meses en condicion de almacenamiento).
"""


def construir_parser():
    p = argparse.ArgumentParser(
        prog="vida_util_arrhenius.py",
        description="Vida util desde estudio acelerado por Arrhenius y por regla Q10, con sus supuestos.",
        epilog="Los tiempos salen en la MISMA unidad en que los metas (meses, dias, semanas): "
               "declarala con --unidad-tiempo.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    sub = p.add_subparsers(dest="modo")

    def tiempo_args(sp):
        sp.add_argument("--unidad-tiempo", default="meses", dest="ut",
                        help="etiqueta de la unidad de tiempo (def. meses)")

    q = sub.add_parser("q10", help="extrapolar con la regla Q10")
    q.add_argument("--tiempo-acelerado", type=dec, required=True, dest="ta",
                   help="vida util observada en la condicion acelerada")
    q.add_argument("--temp-acelerada", type=dec, required=True, dest="Ta", help="temperatura acelerada en C")
    q.add_argument("--temp-real", type=dec, required=True, dest="Tr", help="temperatura de almacenamiento real en C")
    q.add_argument("--q10", type=dec, default=Decimal("2"), help="valor de Q10 (def. 2; tipico 2 a 4)")
    tiempo_args(q)

    a = sub.add_parser("arrhenius", help="extrapolar con la ecuacion de Arrhenius")
    a.add_argument("--tiempo-acelerado", type=dec, required=True, dest="ta", help="vida util observada acelerada")
    a.add_argument("--temp-acelerada", type=dec, required=True, dest="Ta", help="temperatura acelerada en C")
    a.add_argument("--temp-real", type=dec, required=True, dest="Tr", help="temperatura real en C")
    a.add_argument("--ea", type=dec, required=True, help="energia de activacion en J/mol (ej. 83000)")
    tiempo_args(a)

    e = sub.add_parser("ea", help="calcular Ea desde DOS estudios a temperaturas distintas")
    e.add_argument("--t1", type=dec, required=True, help="vida util observada en el estudio 1")
    e.add_argument("--temp1", type=dec, required=True, help="temperatura del estudio 1 en C")
    e.add_argument("--t2", type=dec, required=True, help="vida util observada en el estudio 2")
    e.add_argument("--temp2", type=dec, required=True, help="temperatura del estudio 2 en C")
    tiempo_args(e)

    d = sub.add_parser("desde-perdida", help="de un %% de perdida observado a k y a la vida util")
    d.add_argument("--inicial", type=dec, required=True, help="valor del activo al tiempo 0 (%% o mg/g)")
    d.add_argument("--final", type=dec, required=True, help="valor del activo al final del estudio")
    d.add_argument("--tiempo", type=dec, required=True, help="duracion del estudio")
    d.add_argument("--limite-spec", type=dec, required=True, dest="lim",
                   help="valor minimo que exige tu especificacion")
    d.add_argument("--temp-estudio", type=dec, default=None, dest="Te", help="temperatura del estudio en C")
    d.add_argument("--temp-real", type=dec, default=None, dest="Tr",
                   help="temperatura real; si la das junto con --temp-estudio, se extrapola con Q10")
    d.add_argument("--q10", type=dec, default=Decimal("2"), help="Q10 para la extrapolacion (def. 2)")
    tiempo_args(d)

    c = sub.add_parser("q10-a-ea", help="traduce un Q10 supuesto a la Ea equivalente y al reves")
    c.add_argument("--q10", type=dec, default=None, help="Q10 a traducir a Ea")
    c.add_argument("--ea", type=dec, default=None, help="Ea en J/mol a traducir a Q10")
    c.add_argument("--temp-ref", type=dec, default=Decimal("25"), dest="Tref",
                   help="temperatura de referencia en C (def. 25)")
    return p


def main(argv):
    if "--test" in argv:
        return autotest()
    p = construir_parser()
    args = p.parse_args(argv)
    if not args.modo:
        p.print_help()
        return 0
    try:
        if args.modo == "q10":
            r = por_q10(args.ta, args.Ta, args.Tr, args.q10)
            print("VIDA UTIL POR REGLA Q10")
            print("  Estudio acelerado : %s %s a %s C" % (n(args.ta, 3), args.ut, n(args.Ta, 1)))
            print("  Condicion real    : %s C   (diferencia: %s C)" % (n(args.Tr, 1), n(r["delta_t"], 1)))
            print("  Q10 usado         : %s   (SUPUESTO, no medido)" % n(args.q10, 2))
            print("")
            print("  Factor de extrapolacion : %s x" % n(r["factor"], 4))
            print("  VIDA UTIL ESTIMADA      : %s %s a %s C" % (n(r["vida_util"], 2), args.ut, n(args.Tr, 1)))
            print("  Ea equivalente a ese Q10: %s kJ/mol (a %s C) — si no es creible para tu quimica,"
                  % (n(q10_a_ea(args.q10, args.Tr) / 1000, 1), n(args.Tr, 1)))
            print("  tu Q10 tampoco lo es.")
            print(ADVERTENCIA)

        elif args.modo == "arrhenius":
            r = por_arrhenius(args.ta, args.Ta, args.Tr, args.ea)
            print("VIDA UTIL POR ARRHENIUS")
            print("  Estudio acelerado : %s %s a %s C" % (n(args.ta, 3), args.ut, n(args.Ta, 1)))
            print("  Condicion real    : %s C" % n(args.Tr, 1))
            print("  Ea                : %s J/mol = %s kJ/mol" % (n(args.ea, 0), n(args.ea / 1000, 2)))
            print("")
            print("  Factor de extrapolacion : %s x" % n(r["factor"], 4))
            print("  VIDA UTIL ESTIMADA      : %s %s a %s C" % (n(r["vida_util"], 2), args.ut, n(args.Tr, 1)))
            print("  Q10 equivalente a esa Ea: %s (a %s C)" % (n(ea_a_q10(args.ea, args.Tr), 2), n(args.Tr, 1)))
            print(ADVERTENCIA)

        elif args.modo == "ea":
            ea = ea_desde_dos_estudios(args.t1, args.temp1, args.t2, args.temp2)
            print("ENERGIA DE ACTIVACION DESDE DOS ESTUDIOS (lo correcto: medirla, no suponerla)")
            print("  Estudio 1 : %s %s a %s C" % (n(args.t1, 3), args.ut, n(args.temp1, 1)))
            print("  Estudio 2 : %s %s a %s C" % (n(args.t2, 3), args.ut, n(args.temp2, 1)))
            print("")
            print("  Ea   : %s J/mol = %s kJ/mol" % (n(ea, 0), n(ea / 1000, 2)))
            print("  Q10 equivalente a 25 C : %s" % n(ea_a_q10(ea, Decimal("25")), 2))
            print("")
            if ea < Decimal("40000"):
                print("  ATENCION: Ea menor a 40 kJ/mol suele indicar que lo limitante NO es una reaccion")
                print("  quimica sino un proceso fisico (difusion, evaporacion, migracion de humedad).")
            elif ea > Decimal("200000"):
                print("  ATENCION: Ea mayor a 200 kJ/mol es rara. Revisa que las dos vidas utiles se hayan")
                print("  determinado con el MISMO criterio y el mismo metodo analitico.")
            print("  Dos puntos definen una recta, pero no la validan: con 3 temperaturas puedes ver si")
            print("  el grafico de Arrhenius (ln k vs 1/T) es realmente lineal.")
            print(ADVERTENCIA)

        elif args.modo == "desde-perdida":
            r = desde_perdida(args.inicial, args.final, args.tiempo, args.lim)
            print("DEGRADACION DE PRIMER ORDEN DESDE UNA PERDIDA OBSERVADA")
            print("  Inicial : %s   Final: %s   en %s %s" % (n(args.inicial, 4), n(args.final, 4),
                                                             n(args.tiempo, 3), args.ut))
            if args.Te is not None:
                print("  Temperatura del estudio : %s C" % n(args.Te, 1))
            print("  Perdida observada       : %s %%" % n(r["perdida_pct"], 2))
            print("")
            print("  k (constante de degradacion) : %s por %s" % (n(r["k"], 8), args.ut[:-1] if args.ut.endswith("s") else args.ut))
            print("  Vida media (50 %% de perdida) : %s %s" % (n(r["vida_media"], 2), args.ut))
            print("  Limite de especificacion     : %s" % n(args.lim, 4))
            print("  TIEMPO HASTA EL LIMITE       : %s %s (en la condicion del estudio)"
                  % (n(r["t_limite"], 2), args.ut))
            if args.Te is not None and args.Tr is not None:
                ex = por_q10(r["t_limite"], args.Te, args.Tr, args.q10)
                print("")
                print("  EXTRAPOLACION a %s C con Q10 = %s:" % (n(args.Tr, 1), n(args.q10, 2)))
                print("    Factor           : %s x" % n(ex["factor"], 4))
                print("    VIDA UTIL ESTIMADA: %s %s a %s C" % (n(ex["vida_util"], 2), args.ut, n(args.Tr, 1)))
            print(ADVERTENCIA)

        elif args.modo == "q10-a-ea":
            exigir(args.q10 is not None or args.ea is not None, "Da --q10 o --ea (uno de los dos).")
            exigir(not (args.q10 is not None and args.ea is not None),
                   "Da SOLO uno: --q10 o --ea. Este modo traduce de uno al otro.")
            print("EQUIVALENCIA Q10 <-> Ea  (temperatura de referencia: %s C)" % n(args.Tref, 1))
            if args.q10 is not None:
                ea = q10_a_ea(args.q10, args.Tref)
                print("  Q10 = %s  equivale a  Ea = %s kJ/mol" % (n(args.q10, 2), n(ea / 1000, 2)))
                print("  Comprobacion inversa: esa Ea devuelve Q10 = %s" % n(ea_a_q10(ea, args.Tref), 4))
            else:
                q = ea_a_q10(args.ea, args.Tref)
                print("  Ea = %s kJ/mol  equivale a  Q10 = %s" % (n(args.ea / 1000, 2), n(q, 3)))
                print("  Comprobacion inversa: ese Q10 devuelve Ea = %s kJ/mol" % n(q10_a_ea(q, args.Tref) / 1000, 2))
            print("")
            print("  Referencia util: en degradacion de principios activos se reportan Ea del orden de")
            print("  50 a 130 kJ/mol, que a 25 C corresponden a Q10 de ~2 a ~6. Si tu supuesto cae")
            print("  muy fuera de ahi, no es un supuesto: es un deseo.")
        return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))