#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
potencia_formula.py — Cuanto extracto poner por unidad para que la etiqueta se cumpla HASTA el final
de la vida util (sobredosificacion / overage).

QUE CALCULA
  1) formular : cuantos mg de extracto hay que poner por capsula/unidad para entregar X mg de activo
     al consumidor, considerando (a) la perdida en proceso y (b) la degradacion durante la vida util.
     Devuelve tambien el overage total en % y el contenido al tiempo cero.
  2) verificar : el camino inverso. Dado lo que ya estas poniendo, cuanto activo tendra el producto
     al inicio y al vencimiento, y si cumple la etiqueta.
  3) overage-desde-estabilidad : traduce una perdida observada en un estudio de estabilidad
     (por ejemplo "perdi 12 % en 24 meses") en el factor de degradacion que hay que usar arriba.

FORMULAS
      mg_extracto = objetivo_mg / [ (%activo/100) x (1 - perdida_proceso) x (1 - degradacion_vida_util) ]
      overage (%) = (mg_extracto_con_overage / mg_extracto_teorico - 1) x 100
      activo al tiempo 0        = mg_extracto x (%activo/100) x (1 - perdida_proceso)
      activo al vencimiento     = activo al tiempo 0 x (1 - degradacion_vida_util)

  Con humedad del extracto declarada, el %activo de base seca se corrige a polvo real:
      %activo_efectivo = %activo_base_seca x (1 - humedad/100)

  Degradacion de primer orden desde estabilidad:
      k = -ln(C_final/C_inicial)/t   ->  degradacion en el tiempo T = 1 - exp(-k T)

DE DONDE SALE
  La practica de OVERAGE esta reconocida en desarrollo farmaceutico: ICH Q8 (Pharmaceutical Development)
  la admite pero exige que este JUSTIFICADA (por perdida en fabricacion o por estabilidad), no que sea
  un colchon arbitrario. En suplementos, la regla practica es que el producto debe cumplir la etiqueta
  durante toda su vida util (cGMP 21 CFR 111 en EE.UU. exige especificaciones que se cumplan; en
  Colombia el rotulado debe corresponder al contenido declarado). Datos regulatorios fechados a
  AGOSTO DE 2026: verifica la norma vigente.

QUE **NO** HACE
  - No inventa la degradacion. Si no tienes estudio de estabilidad, el %% que metas en --degradacion es
    una SUPOSICION, y el script te lo dira en la salida. Mide.
  - No verifica que la capsula aguante fisicamente el volumen: valida el peso, no la densidad aparente.
  - No considera limites de seguridad ni maximos toxicologicos: un overage grande puede pasarse de un
    limite de ingesta. Eso lo evaluas aparte.
  - No aplica a activos con margen terapeutico estrecho: ahi el overage NO es aceptable.
  - No cubre la variabilidad lote a lote del extracto: si tu materia prima va de 25 a 35 %, hay que
    reformular por lote contra el COA, no fijar un solo numero.
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP

getcontext().prec = 34

FECHA_REGULATORIA = "agosto de 2026"


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


# ----------------------------------------------------------------------------- calculo

def pct_efectivo(activo_pct, base, humedad_pct):
    exigir(activo_pct > 0, "El % de activo del extracto debe ser mayor que cero.")
    exigir(activo_pct <= 100, "El % de activo no puede superar 100 %.")
    if base == "seca" and humedad_pct is not None:
        exigir(Decimal(0) <= humedad_pct < Decimal(100),
               "La humedad debe estar entre 0 y 100 % (100 % es imposible).")
        return activo_pct * (Decimal(1) - humedad_pct / Decimal(100)), True
    return activo_pct, False


def valida_perdida(valor, nombre):
    exigir(Decimal(0) <= valor < Decimal(100),
           "%s debe estar entre 0 y 100 %% (excluido el 100: una perdida total haria imposible "
           "cualquier formula)." % nombre)
    return Decimal(1) - valor / Decimal(100)


def formular(objetivo_mg, activo_pct, base, humedad_pct, perdida_proceso_pct, degradacion_pct):
    exigir(objetivo_mg > 0, "El objetivo de mg de activo por unidad debe ser mayor que cero.")
    f_act, corregido = pct_efectivo(activo_pct, base, humedad_pct)
    f_proc = valida_perdida(perdida_proceso_pct, "La perdida en proceso")
    f_deg = valida_perdida(degradacion_pct, "La degradacion en vida util")

    fraccion = f_act / Decimal(100)
    teorico = objetivo_mg / fraccion
    real = objetivo_mg / (fraccion * f_proc * f_deg)
    al_inicio = real * fraccion * f_proc
    al_final = al_inicio * f_deg
    return {
        "pct_efectivo": f_act,
        "corregido_por_humedad": corregido,
        "mg_extracto_teorico": teorico,
        "mg_extracto_real": real,
        "overage_pct": (real / teorico - Decimal(1)) * Decimal(100),
        "mg_activo_inicio": al_inicio,
        "mg_activo_final": al_final,
        "factor_proceso": f_proc,
        "factor_degradacion": f_deg,
    }


def verificar(mg_extracto, activo_pct, base, humedad_pct, perdida_proceso_pct, degradacion_pct,
              objetivo_mg):
    exigir(mg_extracto > 0, "Los mg de extracto por unidad deben ser mayores que cero.")
    exigir(objetivo_mg > 0, "El valor declarado en la etiqueta debe ser mayor que cero.")
    f_act, corregido = pct_efectivo(activo_pct, base, humedad_pct)
    f_proc = valida_perdida(perdida_proceso_pct, "La perdida en proceso")
    f_deg = valida_perdida(degradacion_pct, "La degradacion en vida util")
    inicio = mg_extracto * (f_act / Decimal(100)) * f_proc
    final = inicio * f_deg
    # Umbral con tolerancia relativa de 1e-12: evita que el ruido de la ultima cifra decimal
    # convierta un "justo en el limite" en un "no cumple". No es holgura real: es aritmetica.
    umbral = objetivo_mg * (Decimal(1) - Decimal("1e-12"))
    return {
        "pct_efectivo": f_act,
        "corregido_por_humedad": corregido,
        "mg_activo_inicio": inicio,
        "mg_activo_final": final,
        "cumple_inicio": inicio >= umbral,
        "cumple_final": final >= umbral,
        "margen_final_pct": (final - objetivo_mg) * Decimal(100) / objetivo_mg,
    }


def degradacion_desde_estabilidad(c_inicial, c_final, tiempo_estudio, vida_util):
    """Convierte una perdida observada en el % de degradacion esperado a la vida util declarada."""
    exigir(c_inicial > 0 and c_final > 0, "Las concentraciones deben ser mayores que cero.")
    exigir(c_final < c_inicial, "La concentracion final debe ser menor que la inicial: si no, no hay "
                                "degradacion que modelar.")
    exigir(tiempo_estudio > 0, "La duracion del estudio debe ser mayor que cero.")
    exigir(vida_util > 0, "La vida util declarada debe ser mayor que cero.")
    k = -((c_final / c_inicial).ln()) / tiempo_estudio
    restante = (-k * vida_util).exp()
    return {
        "k": k,
        "perdida_estudio_pct": (c_inicial - c_final) * Decimal(100) / c_inicial,
        "restante_fraccion": restante,
        "degradacion_pct": (Decimal(1) - restante) * Decimal(100),
        "extrapolado": vida_util > tiempo_estudio,
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
        print("OK - %d pruebas pasaron (potencia_formula.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST potencia_formula.py")

    # 1. Caso limpio: 100 mg de activo con un extracto al 25 %, sin perdidas
    f0 = formular(Decimal("100"), Decimal("25"), "seca", None, Decimal("0"), Decimal("0"))
    t.cerca("sin perdidas: mg de extracto por unidad", f0["mg_extracto_real"], "400", "1e-12")
    t.cerca("sin perdidas: overage", f0["overage_pct"], "0", "1e-12")
    t.cerca("sin perdidas: activo al vencimiento", f0["mg_activo_final"], "100", "1e-12")

    # 2. Con 5 % de perdida en proceso y 10 % de degradacion
    f = formular(Decimal("100"), Decimal("25"), "seca", None, Decimal("5"), Decimal("10"))
    t.cerca("con perdidas: mg de extracto por unidad", f["mg_extracto_real"], "467.8362573099415205", "1e-12")
    t.cerca("con perdidas: extracto teorico (sin overage)", f["mg_extracto_teorico"], "400", "1e-12")
    t.cerca("con perdidas: overage total [%]", f["overage_pct"], "16.9590643274853801", "1e-12")
    t.cerca("activo al tiempo 0 [mg]", f["mg_activo_inicio"], "111.1111111111111111", "1e-12")
    t.cerca("activo al vencimiento [mg] = objetivo", f["mg_activo_final"], "100", "1e-12")

    # 3. VERIFICACION POR SEGUNDA VIA: multiplicar de vuelta reconstruye el objetivo
    reconstruido = f["mg_extracto_real"] * Decimal("0.25") * Decimal("0.95") * Decimal("0.90")
    t.cerca("segunda via: mg_extracto x 0,25 x 0,95 x 0,90", reconstruido, "100", "1e-12")

    # 4. VERIFICACION CRUZADA con el modo verificar
    v = verificar(f["mg_extracto_real"], Decimal("25"), "seca", None, Decimal("5"), Decimal("10"),
                  Decimal("100"))
    t.cerca("verificar reproduce el activo al inicio", v["mg_activo_inicio"], f["mg_activo_inicio"], "1e-12")
    t.cerca("verificar reproduce el activo al final", v["mg_activo_final"], "100", "1e-12")
    t.cierto("verificar dice que CUMPLE al vencimiento", v["cumple_final"], "dice que no cumple")
    t.cerca("margen al vencimiento [%]", v["margen_final_pct"], "0", "1e-12")

    # 5. El caso que quiebra formulas: poner los 400 mg teoricos NO cumple la etiqueta
    mal = verificar(Decimal("400"), Decimal("25"), "seca", None, Decimal("5"), Decimal("10"), Decimal("100"))
    t.cerca("400 mg 'teoricos' -> activo al vencimiento", mal["mg_activo_final"], "85.5", "1e-12")
    t.cierto("...y por lo tanto NO cumple la etiqueta de 100 mg", not mal["cumple_final"], "dice que cumple")
    t.cerca("le falta [%] respecto de la etiqueta", mal["margen_final_pct"], "-14.5", "1e-12")

    # 6. Correccion por humedad del extracto
    fh = formular(Decimal("100"), Decimal("25"), "seca", Decimal("6"), Decimal("0"), Decimal("0"))
    t.cerca("con 6 % de humedad: % efectivo del polvo real", fh["pct_efectivo"], "23.5", "1e-12")
    t.cerca("con 6 % de humedad: mg de extracto", fh["mg_extracto_real"], "425.5319148936170213", "1e-12")
    t.cierto("corregir por humedad SIEMPRE exige poner mas extracto",
             fh["mg_extracto_real"] > f0["mg_extracto_real"], "no")
    # base humeda: el COA ya viene tal cual, no se corrige dos veces
    fhb = formular(Decimal("100"), Decimal("23.5"), "humeda", Decimal("6"), Decimal("0"), Decimal("0"))
    t.cerca("base humeda 23,5 % da lo mismo", fhb["mg_extracto_real"], fh["mg_extracto_real"], "1e-12")

    # 7. Degradacion desde estabilidad + su ida y vuelta
    d = degradacion_desde_estabilidad(Decimal("100"), Decimal("88"), Decimal("24"), Decimal("24"))
    t.cerca("perdida observada en el estudio [%]", d["perdida_estudio_pct"], "12", "1e-12")
    t.cerca("degradacion a 24 meses [%] (mismo plazo)", d["degradacion_pct"], "12", "1e-12")
    # extrapolar al doble de tiempo degrada mas (pero no el doble: es exponencial)
    d2 = degradacion_desde_estabilidad(Decimal("100"), Decimal("88"), Decimal("24"), Decimal("48"))
    t.cerca("degradacion a 48 meses [%]", d2["degradacion_pct"], "22.56", "1e-12")
    t.cierto("no es lineal: 48 meses degrada menos del doble que 24",
             d2["degradacion_pct"] < d["degradacion_pct"] * 2, "salio lineal")
    t.cierto("marca cuando esta extrapolando mas alla del estudio", d2["extrapolado"], "no marca")
    # cadena completa: usar esa degradacion para formular
    cadena = formular(Decimal("500"), Decimal("30"), "seca", None, Decimal("3"), d["degradacion_pct"])
    t.cerca("cadena completa: activo al vencimiento = objetivo", cadena["mg_activo_final"], "500", "1e-10")

    # 8. Monotonias
    t.cierto("mas degradacion -> mas extracto",
             formular(Decimal("100"), Decimal("25"), "seca", None, Decimal("5"), Decimal("20"))["mg_extracto_real"]
             > f["mg_extracto_real"], "no")
    t.cierto("mas % de activo -> menos extracto",
             formular(Decimal("100"), Decimal("50"), "seca", None, Decimal("5"), Decimal("10"))["mg_extracto_real"]
             < f["mg_extracto_real"], "no")

    # 9. Validaciones
    for descripcion, fn in [
        ("rechaza objetivo 0 mg", lambda: formular(Decimal("0"), Decimal("25"), "seca", None, Decimal("0"), Decimal("0"))),
        ("rechaza 0 % de activo", lambda: formular(Decimal("100"), Decimal("0"), "seca", None, Decimal("0"), Decimal("0"))),
        ("rechaza % de activo > 100", lambda: formular(Decimal("100"), Decimal("150"), "seca", None, Decimal("0"), Decimal("0"))),
        ("rechaza perdida en proceso de 100 %",
         lambda: formular(Decimal("100"), Decimal("25"), "seca", None, Decimal("100"), Decimal("0"))),
        ("rechaza degradacion negativa",
         lambda: formular(Decimal("100"), Decimal("25"), "seca", None, Decimal("0"), Decimal("-5"))),
        ("rechaza humedad de 100 %",
         lambda: formular(Decimal("100"), Decimal("25"), "seca", Decimal("100"), Decimal("0"), Decimal("0"))),
        ("rechaza 0 mg de extracto en verificar",
         lambda: verificar(Decimal("0"), Decimal("25"), "seca", None, Decimal("0"), Decimal("0"), Decimal("100"))),
        ("rechaza estabilidad que gana activo",
         lambda: degradacion_desde_estabilidad(Decimal("88"), Decimal("100"), Decimal("24"), Decimal("24"))),
        ("rechaza vida util 0 en estabilidad",
         lambda: degradacion_desde_estabilidad(Decimal("100"), Decimal("88"), Decimal("24"), Decimal("0"))),
    ]:
        try:
            fn()
            t.cierto(descripcion, False, "no lanzo ErrorDeEntrada")
        except ErrorDeEntrada:
            t.cierto(descripcion, True)

    return t.resultado()


# ----------------------------------------------------------------------------- CLI

def construir_parser():
    p = argparse.ArgumentParser(
        prog="potencia_formula.py",
        description="Cuanto extracto poner por unidad para entregar X mg de activo, con overage por "
                    "perdida en proceso y por degradacion en vida util.",
        epilog="Datos regulatorios fechados a %s. El overage debe estar JUSTIFICADO (ICH Q8): "
               "con datos de proceso y de estabilidad, no a ojo." % FECHA_REGULATORIA,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    sub = p.add_subparsers(dest="modo")

    def comunes(sp):
        sp.add_argument("--activo-pct", type=dec, required=True, dest="act",
                        help="%% del activo/marcador en el extracto, segun COA")
        sp.add_argument("--base", choices=["seca", "humeda"], required=True,
                        help="base del %% del COA (obligatorio declararla)")
        sp.add_argument("--humedad", type=dec, default=None,
                        help="humedad del extracto en %% p/p (corrige base seca a polvo real)")
        sp.add_argument("--perdida-proceso", type=dec, default=Decimal("0"), dest="perd",
                        help="%% de activo que se pierde en fabricacion (def. 0)")
        sp.add_argument("--degradacion", type=dec, default=Decimal("0"), dest="deg",
                        help="%% de activo que se degrada durante la vida util (def. 0)")
        sp.add_argument("--activo", default="activo", help="nombre del activo, solo para la salida")

    f = sub.add_parser("formular", help="cuanto extracto poner por unidad")
    f.add_argument("--objetivo-mg", type=dec, required=True, dest="obj",
                   help="mg de activo que quieres entregar por unidad al final de la vida util")
    comunes(f)

    v = sub.add_parser("verificar", help="que entrega la formula que ya tienes")
    v.add_argument("--mg-extracto", type=dec, required=True, dest="mg",
                   help="mg de extracto que estas poniendo por unidad")
    v.add_argument("--etiqueta-mg", type=dec, required=True, dest="obj",
                   help="mg de activo declarados en la etiqueta")
    comunes(v)

    e = sub.add_parser("overage-desde-estabilidad",
                       help="convierte una perdida observada en el %% de degradacion a usar")
    e.add_argument("--inicial", type=dec, required=True, help="valor del activo al tiempo 0")
    e.add_argument("--final", type=dec, required=True, help="valor del activo al final del estudio")
    e.add_argument("--tiempo-estudio", type=dec, required=True, dest="te", help="duracion del estudio")
    e.add_argument("--vida-util", type=dec, required=True, dest="vu", help="vida util que quieres declarar")
    e.add_argument("--unidad-tiempo", default="meses", dest="ut", help="unidad de tiempo (def. meses)")
    return p


def _nota_supuestos(perd, deg):
    print("")
    print("  DE DONDE SALEN TUS SUPUESTOS:")
    if perd == 0:
        print("    - Perdida en proceso 0 %: estas asumiendo fabricacion sin perdidas. Casi nunca es cierto")
        print("      (mezclado, encapsulado, muestreo). Mide el balance de un lote real.")
    else:
        print("    - Perdida en proceso %s %%: debe venir del balance de masa de un lote real." % perd)
    if deg == 0:
        print("    - Degradacion 0 %: estas asumiendo que el activo NO se degrada en toda la vida util.")
        print("      Si no tienes estudio de estabilidad, esto es un deseo, no un dato. Mide.")
    else:
        print("    - Degradacion %s %%: debe venir de tu estudio de estabilidad, no de un supuesto." % deg)
    print("    Usa el modo 'overage-desde-estabilidad' para convertir tu estudio en ese numero.")
    print("  El overage debe estar JUSTIFICADO (ICH Q8) y no puede empujarte por encima de un limite")
    print("  de ingesta segura. Datos regulatorios fechados a %s: verifica lo vigente." % FECHA_REGULATORIA)


def main(argv):
    if "--test" in argv:
        return autotest()
    p = construir_parser()
    args = p.parse_args(argv)
    if not args.modo:
        p.print_help()
        return 0
    try:
        if args.modo == "formular":
            r = formular(args.obj, args.act, args.base, args.humedad, args.perd, args.deg)
            print("FORMULACION POR POTENCIA — cuanto extracto poner por unidad")
            print("  Objetivo       : %s mg de %s por unidad AL FINAL de la vida util"
                  % (n(args.obj, 3), args.activo))
            print("  Extracto (COA) : %s %% p/p, BASE %s" % (n(args.act, 3), args.base.upper()))
            if r["corregido_por_humedad"]:
                print("  Humedad        : %s %% -> %% efectivo sobre polvo real: %s %% p/p"
                      % (n(args.humedad, 2), n(r["pct_efectivo"], 3)))
            elif args.base == "seca":
                print("  Humedad        : no declarada -> se usa el %% de base seca SIN corregir")
                print("                   (vas a quedar corto si el polvo trae agua)")
            print("  Perdida proceso: %s %%    Degradacion vida util: %s %%" % (n(args.perd, 2), n(args.deg, 2)))
            print("")
            print("  Extracto teorico (sin overage) : %s mg por unidad" % n(r["mg_extracto_teorico"], 2))
            print("  EXTRACTO A DOSIFICAR           : %s mg por unidad" % n(r["mg_extracto_real"], 2))
            print("  Overage total                  : %s %%" % n(r["overage_pct"], 2))
            print("")
            print("  %s al tiempo 0     : %s mg por unidad" % (args.activo, n(r["mg_activo_inicio"], 3)))
            print("  %s al vencimiento  : %s mg por unidad  (= el objetivo)"
                  % (args.activo, n(r["mg_activo_final"], 3)))
            if r["overage_pct"] > Decimal("30"):
                print("")
                print("  ATENCION: overage mayor al 30 %. Antes de aceptarlo, pregunta si el problema es")
                print("  la formula o el proceso: un overage grande suele estar tapando una perdida evitable.")
            _nota_supuestos(args.perd, args.deg)

        elif args.modo == "verificar":
            r = verificar(args.mg, args.act, args.base, args.humedad, args.perd, args.deg, args.obj)
            print("VERIFICACION DE UNA FORMULA EXISTENTE")
            print("  Extracto por unidad : %s mg   (COA %s %% p/p, BASE %s)"
                  % (n(args.mg, 2), n(args.act, 3), args.base.upper()))
            if r["corregido_por_humedad"]:
                print("  %% efectivo sobre polvo real: %s %% p/p (humedad %s %%)"
                      % (n(r["pct_efectivo"], 3), n(args.humedad, 2)))
            print("  Perdida proceso     : %s %%    Degradacion vida util: %s %%"
                  % (n(args.perd, 2), n(args.deg, 2)))
            print("  Etiqueta declara    : %s mg de %s por unidad" % (n(args.obj, 3), args.activo))
            print("")
            print("  %s al tiempo 0    : %s mg   ->  %s"
                  % (args.activo, n(r["mg_activo_inicio"], 3), "CUMPLE" if r["cumple_inicio"] else "NO CUMPLE"))
            print("  %s al vencimiento : %s mg   ->  %s"
                  % (args.activo, n(r["mg_activo_final"], 3), "CUMPLE" if r["cumple_final"] else "NO CUMPLE"))
            print("  Margen al vencimiento : %s %% respecto de la etiqueta" % n(r["margen_final_pct"], 2))
            if not r["cumple_final"]:
                falta = formular(args.obj, args.act, args.base, args.humedad, args.perd, args.deg)
                print("")
                print("  PARA CUMPLIR: sube a %s mg de extracto por unidad (+%s mg)"
                      % (n(falta["mg_extracto_real"], 2), n(falta["mg_extracto_real"] - args.mg, 2)))
            _nota_supuestos(args.perd, args.deg)

        elif args.modo == "overage-desde-estabilidad":
            r = degradacion_desde_estabilidad(args.inicial, args.final, args.te, args.vu)
            print("DEGRADACION A USAR EN LA FORMULA (desde tu estudio de estabilidad)")
            print("  Estudio: de %s a %s en %s %s" % (n(args.inicial, 4), n(args.final, 4),
                                                      n(args.te, 2), args.ut))
            print("  Perdida observada : %s %% en %s %s" % (n(r["perdida_estudio_pct"], 2), n(args.te, 2), args.ut))
            print("  k (primer orden)  : %s por %s" % (n(r["k"], 8), args.ut))
            print("")
            print("  Para una vida util de %s %s:" % (n(args.vu, 2), args.ut))
            print("    Queda            : %s %% del activo inicial" % n(r["restante_fraccion"] * 100, 2))
            print("    DEGRADACION A USAR: %s %%   -> pasa este numero a --degradacion" % n(r["degradacion_pct"], 2))
            if r["extrapolado"]:
                print("")
                print("  ATENCION: estas EXTRAPOLANDO mas alla de la duracion del estudio (%s %s de estudio"
                      % (n(args.te, 2), args.ut))
                print("  para declarar %s %s de vida util). ICH Q1E limita cuanto se puede extrapolar."
                      % (n(args.vu, 2), args.ut))
                print("  Ademas se asume que el mecanismo de degradacion no cambia. Verifica con datos reales.")
            print("")
            print("  Se asume cinetica de PRIMER ORDEN. Si tu activo se degrada por otro mecanismo")
            print("  (oxidacion catalizada, hidrolisis dependiente de humedad), este numero no aplica.")
            print("  Ver tambien vida_util_arrhenius.py para extrapolar por temperatura.")
        return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))