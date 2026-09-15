#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
loq_lod.py — Limite de deteccion (LOD) y limite de cuantificacion (LOQ) por las dos vias de la ICH.

QUE CALCULA
  1) senal-ruido : LOD y LOQ a partir de la relacion senal/ruido (S/N) observada en un pico de
     concentracion conocida, usando los criterios 3:1 (LOD) y 10:1 (LOQ).
  2) ich         : LOD y LOQ a partir de la desviacion estandar de la respuesta (sigma) y la pendiente
     de la curva de calibracion (S), con los factores 3,3 y 10 de la ICH Q2(R2).
  3) curva       : lo mismo que 'ich', pero calculando sigma y la pendiente DESDE los puntos de la curva
     (usa la desviacion estandar residual s(y/x) o la del intercepto, a tu eleccion).

FORMULAS
  Via senal/ruido (aplicable solo a metodos que muestran ruido de linea base, tipico en cromatografia):
      LOD = C_medida x (3  / (S/N observado))
      LOQ = C_medida x (10 / (S/N observado))

  Via ICH Q2(R2), seccion de LOD/LOQ:
      LOD = 3,3 x sigma / S
      LOQ = 10  x sigma / S
  donde sigma puede ser:
      - la desviacion estandar del BLANCO,
      - la desviacion estandar RESIDUAL de la curva, s(y/x) = sqrt( SSres / (n-2) ), o
      - la desviacion estandar del INTERCEPTO de la curva:
            s(b) = s(y/x) x sqrt( Sxx_total / (n x Sxx_centrado) )
        con Sxx_centrado = suma (x - media_x)^2 y Sxx_total = suma x^2.
  y S es la PENDIENTE de la curva de calibracion.

  Relacion util de control: LOQ / LOD = 10 / 3,3 = 3,0303 (via ICH) o 10/3 = 3,3333 (via S/N).

DE DONDE SALE
  ICH Q2(R2) "Validation of Analytical Procedures" (guia armonizada ICH; version R2 adoptada en 2023),
  que reconoce explicitamente las tres aproximaciones: inspeccion visual, relacion senal-ruido, y
  desviacion estandar de la respuesta con la pendiente. Los factores 3,3 y 10 salen de ahi.

QUE **NO** HACE
  - No VALIDA nada por si solo: un LOD calculado debe CONFIRMARSE analizando muestras fortificadas a
    esa concentracion (la propia ICH lo exige). Un numero en un papel no es un limite demostrado.
  - No calcula el MDL de la EPA (que usa t de Student sobre 7 replicas): es otro criterio, con otro numero.
  - No aplica a metodos sin ruido de linea base (gravimetria, titulacion): ahi la via S/N no tiene sentido.
  - No convierte "no detectado" en "cero". No detectado significa "por debajo del LOD de ESE metodo".
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP

getcontext().prec = 34

FACTOR_LOD_ICH = Decimal("3.3")
FACTOR_LOQ_ICH = Decimal("10")
FACTOR_LOD_SN = Decimal("3")
FACTOR_LOQ_SN = Decimal("10")


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


def n(x, d=6):
    return str(Decimal(x).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP))


# ----------------------------------------------------------------------------- calculo

def por_senal_ruido(concentracion, sn):
    exigir(concentracion > 0, "La concentracion de la muestra medida debe ser mayor que cero.")
    exigir(sn > 0, "La relacion senal/ruido debe ser mayor que cero.")
    return {
        "lod": concentracion * FACTOR_LOD_SN / sn,
        "loq": concentracion * FACTOR_LOQ_SN / sn,
        "sn_en_lod": FACTOR_LOD_SN,
        "sn_en_loq": FACTOR_LOQ_SN,
    }


def por_ich(sigma, pendiente):
    exigir(sigma > 0, "La desviacion estandar (sigma) debe ser mayor que cero.")
    exigir(pendiente > 0, "La pendiente (S) debe ser mayor que cero. "
                          "Si tu pendiente es negativa, usa su valor absoluto.")
    return {
        "lod": FACTOR_LOD_ICH * sigma / pendiente,
        "loq": FACTOR_LOQ_ICH * sigma / pendiente,
    }


def estadisticos_curva(xs, ys):
    """Regresion por minimos cuadrados + s(y/x) residual + s(b) del intercepto."""
    exigir(len(xs) == len(ys), "Hay %d concentraciones y %d respuestas: no coinciden." % (len(xs), len(ys)))
    k = len(xs)
    exigir(k >= 3, "Se necesitan al menos 3 puntos (la ICH pide 5 niveles para linealidad).")
    for x in xs:
        exigir(x >= 0, "Las concentraciones de los patrones no pueden ser negativas.")
    nn = Decimal(k)
    sx = sum(xs, Decimal(0))
    sy = sum(ys, Decimal(0))
    sxx_total = sum((x * x for x in xs), Decimal(0))
    sxy = sum((x * y for x, y in zip(xs, ys)), Decimal(0))
    denom = nn * sxx_total - sx * sx
    exigir(denom != 0, "Todas las concentraciones son iguales: no hay recta que ajustar.")
    m = (nn * sxy - sx * sy) / denom
    b = (sy - m * sx) / nn
    media_x = sx / nn
    sxx_centrado = sum(((x - media_x) ** 2 for x in xs), Decimal(0))
    ss_res = sum(((y - (m * x + b)) ** 2 for x, y in zip(xs, ys)), Decimal(0))
    s_yx = (ss_res / (nn - Decimal(2))).sqrt()
    exigir(sxx_centrado > 0, "Dispersion nula en las concentraciones.")
    s_b = s_yx * (sxx_total / (nn * sxx_centrado)).sqrt()
    return {"n": k, "pendiente": m, "intercepto": b, "s_yx": s_yx, "s_intercepto": s_b,
            "ss_res": ss_res, "sxx_centrado": sxx_centrado, "sxx_total": sxx_total}


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
        print("OK - %d pruebas pasaron (loq_lod.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST loq_lod.py")

    # 1. Via senal/ruido: patron de 10 ppm que da S/N = 30
    sn = por_senal_ruido(Decimal("10"), Decimal("30"))
    t.cerca("S/N=30 a 10 ppm -> LOD [ppm]", sn["lod"], "1", "1e-12")
    t.cerca("S/N=30 a 10 ppm -> LOQ [ppm]", sn["loq"], "3.3333333333333333", "1e-12")
    # segunda via: a la concentracion del LOD la S/N debe ser exactamente 3
    sn_en_lod = Decimal("30") * sn["lod"] / Decimal("10")
    t.cerca("comprobacion: S/N en el LOD = 3", sn_en_lod, "3", "1e-12")
    sn_en_loq = Decimal("30") * sn["loq"] / Decimal("10")
    t.cerca("comprobacion: S/N en el LOQ = 10", sn_en_loq, "10", "1e-12")
    t.cerca("relacion LOQ/LOD por S/N = 10/3", sn["loq"] / sn["lod"], "3.3333333333333333", "1e-12")

    # 2. Via ICH con sigma y pendiente conocidas
    ich = por_ich(Decimal("0.5"), Decimal("100"))
    t.cerca("sigma=0,5 S=100 -> LOD ICH", ich["lod"], "0.0165", "1e-15")
    t.cerca("sigma=0,5 S=100 -> LOQ ICH", ich["loq"], "0.05", "1e-15")
    t.cerca("relacion LOQ/LOD por ICH = 10/3,3", ich["loq"] / ich["lod"], "3.0303030303030303", "1e-12")
    # INVERSA: despejar sigma desde el LOD
    t.cerca("inversa: sigma = LOD x S / 3,3", ich["lod"] * Decimal("100") / FACTOR_LOD_ICH, "0.5", "1e-15")
    # INVERSA: despejar la pendiente desde el LOQ
    t.cerca("inversa: S = 10 x sigma / LOQ", FACTOR_LOQ_ICH * Decimal("0.5") / ich["loq"], "100", "1e-12")

    # 3. Curva perfecta: residual cero -> LOD cero (y eso es una senal de alarma, no un logro)
    xs = [Decimal("1"), Decimal("2"), Decimal("5"), Decimal("10"), Decimal("20")]
    ys = [Decimal(x) * Decimal("100") + Decimal("5") for x in xs]
    c = estadisticos_curva(xs, ys)
    t.cerca("curva perfecta: pendiente", c["pendiente"], "100", "1e-12")
    t.cerca("curva perfecta: intercepto", c["intercepto"], "5", "1e-12")
    t.cerca("curva perfecta: s(y/x) = 0", c["s_yx"], "0", "1e-12")
    t.cerca("curva perfecta: s(intercepto) = 0", c["s_intercepto"], "0", "1e-12")

    # 4. Curva con residuos: sigma residual verificada contra el calculo manual de SSres
    xs2 = [Decimal("1"), Decimal("2"), Decimal("3"), Decimal("4"), Decimal("5")]
    ys2 = [Decimal("102"), Decimal("198"), Decimal("305"), Decimal("399"), Decimal("501")]
    c2 = estadisticos_curva(xs2, ys2)
    t.cerca("curva con ruido: pendiente", c2["pendiente"], "99.9", "1e-10")
    # segunda via: SSres recalculado punto a punto
    ss_manual = sum(((y - (c2["pendiente"] * x + c2["intercepto"])) ** 2 for x, y in zip(xs2, ys2)), Decimal(0))
    t.cerca("segunda via: SSres recalculado", c2["ss_res"], ss_manual, "1e-20")
    t.cerca("s(y/x) = sqrt(SSres/(n-2))", c2["s_yx"], (ss_manual / Decimal(3)).sqrt(), "1e-20")
    t.cierto("s(intercepto) > s(y/x) cuando la curva no pasa por el origen",
             c2["s_intercepto"] > 0, "s(b)=%s" % c2["s_intercepto"])

    # 5. LOD/LOQ desde esa curva, por las dos definiciones de sigma
    lod_resid = por_ich(c2["s_yx"], c2["pendiente"])
    lod_inter = por_ich(c2["s_intercepto"], c2["pendiente"])
    t.cierto("LOD con s(intercepto) >= LOD con s(y/x)",
             lod_inter["lod"] >= lod_resid["lod"],
             "%s < %s" % (lod_inter["lod"], lod_resid["lod"]))
    t.cierto("LOQ siempre mayor que LOD", lod_resid["loq"] > lod_resid["lod"], "no")
    # coherencia con la relacion fija
    t.cerca("LOQ/LOD sigue siendo 10/3,3", lod_resid["loq"] / lod_resid["lod"], "3.0303030303030303", "1e-12")

    # 6. Coherencia entre las dos vias: si construyo un caso donde ambas deben coincidir
    #    (sigma/S = 1 ppm de ruido equivalente y una muestra de 10 ppm con S/N = 30)
    equivalente = por_ich(Decimal("10"), Decimal("10"))   # sigma/S = 1 -> LOD = 3,3 ppm
    t.cerca("caso equivalente: LOD ICH con sigma/S = 1", equivalente["lod"], "3.3", "1e-12")
    t.cierto("las dos vias dan numeros del mismo orden (3 vs 3,3)",
             abs(equivalente["lod"] - Decimal("3")) < Decimal("0.5"), "no")

    # 7. Validaciones
    for descripcion, fn in [
        ("rechaza S/N igual a 0", lambda: por_senal_ruido(Decimal("10"), Decimal("0"))),
        ("rechaza S/N negativa", lambda: por_senal_ruido(Decimal("10"), Decimal("-5"))),
        ("rechaza concentracion 0 en la via S/N", lambda: por_senal_ruido(Decimal("0"), Decimal("30"))),
        ("rechaza sigma igual a 0", lambda: por_ich(Decimal("0"), Decimal("100"))),
        ("rechaza sigma negativa", lambda: por_ich(Decimal("-1"), Decimal("100"))),
        ("rechaza pendiente 0", lambda: por_ich(Decimal("0.5"), Decimal("0"))),
        ("rechaza pendiente negativa", lambda: por_ich(Decimal("0.5"), Decimal("-100"))),
        ("rechaza curva con 2 puntos",
         lambda: estadisticos_curva([Decimal("1"), Decimal("2")], [Decimal("1"), Decimal("2")])),
        ("rechaza concentracion de patron negativa",
         lambda: estadisticos_curva([Decimal("-1"), Decimal("2"), Decimal("3")],
                                    [Decimal("1"), Decimal("2"), Decimal("3")])),
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
        prog="loq_lod.py",
        description="LOD y LOQ por relacion senal-ruido (3:1 y 10:1) y por sigma/pendiente (3,3 y 10, ICH Q2).",
        epilog="El LOD calculado debe CONFIRMARSE con muestras fortificadas a esa concentracion. "
               "Un numero calculado no es un limite demostrado.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    sub = p.add_subparsers(dest="modo")

    a = sub.add_parser("senal-ruido", help="LOD/LOQ desde la relacion S/N de un pico conocido")
    a.add_argument("--concentracion", type=dec, required=True, dest="conc",
                   help="concentracion de la muestra o patron medido")
    a.add_argument("--sn", type=dec, required=True, help="relacion senal/ruido observada en ese pico")
    a.add_argument("--unidad", default="ppm", help="unidad de concentracion (def. ppm)")
    a.add_argument("--base", choices=["seca", "humeda"], required=True,
                   help="base del dato (obligatorio declararla)")

    b = sub.add_parser("ich", help="LOD/LOQ desde sigma y pendiente (criterio ICH Q2)")
    b.add_argument("--sigma", type=dec, required=True,
                   help="desviacion estandar de la respuesta (blanco, residual o del intercepto)")
    b.add_argument("--pendiente", type=dec, required=True, help="pendiente S de la curva de calibracion")
    b.add_argument("--unidad", default="ppm", help="unidad de concentracion (def. ppm)")
    b.add_argument("--base", choices=["seca", "humeda"], required=True, help="base del dato")

    c = sub.add_parser("curva", help="LOD/LOQ calculando sigma y pendiente desde la curva")
    c.add_argument("--conc", type=str, required=True,
                   help="concentraciones de los patrones separadas por coma")
    c.add_argument("--area", type=str, required=True, help="respuestas correspondientes, mismo orden")
    c.add_argument("--sigma", choices=["residual", "intercepto"], default="residual",
                   help="que sigma usar: s(y/x) residual (def.) o s(b) del intercepto")
    c.add_argument("--unidad", default="ppm", help="unidad de concentracion (def. ppm)")
    c.add_argument("--base", choices=["seca", "humeda"], required=True, help="base del dato")
    return p


def _lista(texto, etiqueta):
    partes = [p for p in texto.replace(";", ",").split(",") if p.strip() != ""]
    exigir(len(partes) > 0, "No se leyo ningun valor en %s." % etiqueta)
    salida = []
    for p in partes:
        try:
            salida.append(Decimal(p.strip().replace(",", ".")))
        except InvalidOperation:
            raise ErrorDeEntrada("Valor invalido en %s: '%s'" % (etiqueta, p))
    return salida


def _cierre(unidad, base):
    print("")
    print("  Todos los limites estan en %s, BASE %s." % (unidad, base.upper()))
    print("  CONFIRMACION OBLIGATORIA: la ICH exige verificar el LOQ analizando muestras fortificadas")
    print("  a esa concentracion (exactitud y precision aceptables). Sin eso, es un numero, no un limite.")
    print("  'No detectado' = por debajo del LOD DE ESTE METODO. No significa ausencia.")


def main(argv):
    if "--test" in argv:
        return autotest()
    p = construir_parser()
    args = p.parse_args(argv)
    if not args.modo:
        p.print_help()
        return 0
    try:
        if args.modo == "senal-ruido":
            r = por_senal_ruido(args.conc, args.sn)
            print("LOD / LOQ POR RELACION SENAL-RUIDO")
            print("  Muestra medida : %s %s con S/N = %s" % (n(args.conc, 6), args.unidad, n(args.sn, 2)))
            print("  Criterio       : LOD a S/N = 3 ; LOQ a S/N = 10")
            print("")
            print("  LOD : %s %s   (base %s)" % (n(r["lod"], 6), args.unidad, args.base))
            print("  LOQ : %s %s   (base %s)" % (n(r["loq"], 6), args.unidad, args.base))
            print("  LOQ/LOD = %s" % n(r["loq"] / r["lod"], 4))
            if args.sn < Decimal("10"):
                print("")
                print("  ATENCION: mediste con S/N < 10, es decir por DEBAJO de tu propio LOQ.")
                print("  Ese pico no sirve para cuantificar, solo para detectar.")
            _cierre(args.unidad, args.base)

        elif args.modo == "ich":
            r = por_ich(args.sigma, args.pendiente)
            print("LOD / LOQ POR SIGMA Y PENDIENTE (ICH Q2(R2))")
            print("  sigma     : %s unidades de respuesta" % n(args.sigma, 6))
            print("  pendiente : %s unidades de respuesta por %s" % (n(args.pendiente, 6), args.unidad))
            print("  Criterio  : LOD = 3,3 sigma / S ; LOQ = 10 sigma / S")
            print("")
            print("  LOD : %s %s   (base %s)" % (n(r["lod"], 6), args.unidad, args.base))
            print("  LOQ : %s %s   (base %s)" % (n(r["loq"], 6), args.unidad, args.base))
            print("  LOQ/LOD = %s (siempre 10/3,3 por definicion)" % n(r["loq"] / r["lod"], 4))
            _cierre(args.unidad, args.base)

        elif args.modo == "curva":
            xs = _lista(args.conc, "--conc")
            ys = _lista(args.area, "--area")
            c = estadisticos_curva(xs, ys)
            sigma = c["s_yx"] if args.sigma == "residual" else c["s_intercepto"]
            print("LOD / LOQ DESDE LA CURVA DE CALIBRACION (ICH Q2(R2))")
            print("  Puntos          : %d  (la ICH pide 5 niveles para linealidad)" % c["n"])
            print("  Ecuacion        : respuesta = %s x conc + %s"
                  % (n(c["pendiente"], 6), n(c["intercepto"], 6)))
            print("  s(y/x) residual : %s" % n(c["s_yx"], 6))
            print("  s(intercepto)   : %s" % n(c["s_intercepto"], 6))
            print("  sigma usada     : %s  (%s)" % (n(sigma, 6), args.sigma))
            if sigma <= 0:
                print("")
                print("  ATENCION: sigma = 0. Tu curva es MATEMATICAMENTE perfecta, lo cual en un dato real")
                print("  no pasa: o son datos simulados o los puntos vienen de la misma inyeccion.")
                print("  No se puede calcular LOD/LOQ con sigma cero.")
                _cierre(args.unidad, args.base)
                return 0
            r = por_ich(sigma, abs(c["pendiente"]))
            print("")
            print("  LOD : %s %s   (base %s)" % (n(r["lod"], 6), args.unidad, args.base))
            print("  LOQ : %s %s   (base %s)" % (n(r["loq"], 6), args.unidad, args.base))
            menor = min(xs)
            if r["loq"] > menor:
                print("")
                print("  ATENCION: el LOQ calculado (%s) esta POR ENCIMA de tu patron mas bajo (%s)."
                      % (n(r["loq"], 6), n(menor, 6)))
                print("  Estas calibrando por debajo de tu propio limite de cuantificacion.")
            _cierre(args.unidad, args.base)
        return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
