#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unidades.py — Conversion entre unidades de concentracion masa/masa, EXIGIENDO que declares la base.

QUE CALCULA
  Convierte un mismo valor de composicion entre todas estas unidades a la vez:
      % p/p  <->  mg/g  <->  ppm (= mg/kg)  <->  ug/g  <->  g/kg  <->  mg por porcion
  y obliga a declarar la BASE (seca o humeda), porque un numero sin base no significa nada.
  Con --humedad ademas te muestra el equivalente en la otra base.

FORMULAS (todas son masa/masa; NO sirven para mg/mL sin densidad)
      1 % p/p = 10 mg/g = 10 000 ppm = 10 000 ug/g = 10 g/kg
      ppm     = mg/kg   = ug/g                      (identidad, no aproximacion)
      mg por porcion = (mg/g) x (gramos de la porcion)

DE DONDE SALE
  Definiciones de concentracion masa/masa. ppm = partes por millon = 1 mg en 1 kg = 1 ug en 1 g.
  La equivalencia ppm = mg/L SOLO vale en soluciones acuosas diluidas donde la densidad es ~1 g/mL,
  y por eso este script NO la hace: si necesitas volumen, pasa por densidad explicitamente.

QUE **NO** HACE
  - No convierte a mg/mL, %% p/v ni %% v/v: eso exige densidad y este script no la inventa.
  - No convierte de base humeda a base seca sin que le des la humedad (--humedad).
  - No sabe si tu valor es correcto: solo cambia de unidad. Basura entra, basura sale en otra unidad.
  - No maneja unidades molares (mM, umol/g): para eso hace falta la masa molar del analito.
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP

getcontext().prec = 34

# Factores hacia la unidad interna canonica: mg/g
A_MG_G = {
    "pct": Decimal("10"),        # 1 % p/p  = 10 mg/g
    "mg/g": Decimal("1"),
    "ppm": Decimal("0.001"),     # 1 ppm    = 0,001 mg/g
    "ug/g": Decimal("0.001"),    # 1 ug/g   = 1 ppm
    "mg/kg": Decimal("0.001"),
    "g/kg": Decimal("1"),        # 1 g/kg   = 1 mg/g
}
UNIDADES = sorted(A_MG_G.keys())
MAX_MG_G = Decimal("1000")       # 1000 mg/g = 100 % p/p = el material entero


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

def a_mg_g(valor, unidad):
    exigir(unidad in A_MG_G, "Unidad no reconocida: %s. Validas: %s" % (unidad, ", ".join(UNIDADES)))
    exigir(valor >= 0, "Una concentracion no puede ser negativa.")
    mg_g = valor * A_MG_G[unidad]
    exigir(mg_g <= MAX_MG_G,
           "El valor equivale a %s mg/g (> 1000 mg/g = 100 %% p/p). Un componente no puede pesar "
           "mas que la muestra entera: revisa la unidad." % mg_g)
    return mg_g


def desde_mg_g(mg_g, unidad):
    exigir(unidad in A_MG_G, "Unidad no reconocida: %s" % unidad)
    return mg_g / A_MG_G[unidad]


def tabla(mg_g):
    return {
        "pct": desde_mg_g(mg_g, "pct"),
        "mg/g": mg_g,
        "g/kg": desde_mg_g(mg_g, "g/kg"),
        "ppm": desde_mg_g(mg_g, "ppm"),
        "ug/g": desde_mg_g(mg_g, "ug/g"),
        "mg/kg": desde_mg_g(mg_g, "mg/kg"),
    }


def por_porcion(mg_g, gramos_porcion):
    exigir(gramos_porcion > 0, "La porcion (--porcion-g) debe ser mayor que cero.")
    return mg_g * gramos_porcion


def cambiar_base(mg_g, base, humedad_pct):
    """Devuelve el valor en la OTRA base. Devuelve None si no se puede."""
    if humedad_pct is None:
        return None
    exigir(Decimal(0) <= humedad_pct < Decimal(100),
           "La humedad debe estar entre 0 y 100 % (100 % es imposible).")
    solidos = Decimal(1) - humedad_pct / Decimal(100)
    return mg_g / solidos if base == "humeda" else mg_g * solidos


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
            print("  ok  %-56s %s" % (nombre, o))

    def cierto(self, nombre, condicion, detalle=""):
        self.n += 1
        if condicion:
            print("  ok  %-56s %s" % (nombre, "cumple"))
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
        print("OK - %d pruebas pasaron (unidades.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST unidades.py")

    # 1. Equivalencias de libro a partir de 0,3 % p/p
    mg_g = a_mg_g(Decimal("0.3"), "pct")
    tb = tabla(mg_g)
    t.cerca("0,3 % p/p -> mg/g", tb["mg/g"], "3", "1e-12")
    t.cerca("0,3 % p/p -> ppm", tb["ppm"], "3000", "1e-12")
    t.cerca("0,3 % p/p -> ug/g", tb["ug/g"], "3000", "1e-12")
    t.cerca("0,3 % p/p -> g/kg", tb["g/kg"], "3", "1e-12")
    t.cierto("ppm = mg/kg = ug/g (identidad)",
             tb["ppm"] == tb["mg/kg"] == tb["ug/g"], "no son iguales")

    # 2. VERIFICACION POR SEGUNDA VIA: ida y vuelta por CADA unidad
    for u in UNIDADES:
        v = desde_mg_g(mg_g, u)
        t.cerca("ida y vuelta por %s" % u, a_mg_g(v, u), mg_g, "1e-12")

    # 3. Un caso tipico de metales pesados: 0,5 ppm de plomo
    pb = a_mg_g(Decimal("0.5"), "ppm")
    t.cerca("0,5 ppm -> mg/g", pb, "0.0005", "1e-15")
    t.cerca("0,5 ppm -> % p/p", desde_mg_g(pb, "pct"), "0.00005", "1e-15")

    # 4. mg por porcion, y su inversa
    bg = a_mg_g(Decimal("30"), "pct")                 # 30 % p/p = 300 mg/g
    p = por_porcion(bg, Decimal("2"))                 # porcion de 2 g
    t.cerca("30 % p/p en porcion de 2 g [mg]", p, "600", "1e-12")
    t.cerca("inversa: mg por porcion / gramos = mg/g", p / Decimal("2"), bg, "1e-12")

    # 5. Cambio de base con humedad (y su inversa)
    seca = cambiar_base(bg, "humeda", Decimal("8"))
    t.cerca("300 mg/g tal cual con 8 % humedad -> base seca", seca, "326.086956521739130", "1e-12")
    t.cerca("inversa: de base seca a tal cual", cambiar_base(seca, "seca", Decimal("8")), bg, "1e-12")
    t.cierto("sin humedad no inventa la otra base", cambiar_base(bg, "humeda", None) is None, "invento")

    # 6. Limite fisico: 100 % p/p es el tope
    t.cerca("100 % p/p = 1000 mg/g (tope fisico)", a_mg_g(Decimal("100"), "pct"), "1000", "1e-12")

    # 7. Validaciones
    for descripcion, fn in [
        ("rechaza 120 % p/p", lambda: a_mg_g(Decimal("120"), "pct")),
        ("rechaza 1 200 000 ppm (> 100 %)", lambda: a_mg_g(Decimal("1200000"), "ppm")),
        ("rechaza concentracion negativa", lambda: a_mg_g(Decimal("-1"), "mg/g")),
        ("rechaza unidad inventada", lambda: a_mg_g(Decimal("1"), "mg/onza")),
        ("rechaza porcion de 0 g", lambda: por_porcion(Decimal("1"), Decimal("0"))),
        ("rechaza humedad de 100 %", lambda: cambiar_base(Decimal("1"), "humeda", Decimal("100"))),
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
        prog="unidades.py",
        description="Convierte %% p/p <-> mg/g <-> ppm <-> ug/g <-> g/kg <-> mg por porcion. "
                    "Exige declarar la base (seca o humeda).",
        epilog="Solo unidades masa/masa. Para mg/mL o %% p/v necesitas densidad: este script no la asume.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    p.add_argument("--valor", type=dec, help="valor numerico a convertir")
    p.add_argument("--unidad", choices=UNIDADES, help="unidad del valor de entrada")
    p.add_argument("--base", choices=["seca", "humeda"],
                   help="OBLIGATORIA: base del dato (seca = dry basis, humeda = tal cual / as is)")
    p.add_argument("--humedad", type=dec, default=None,
                   help="humedad en %% p/p; si la das, se imprime tambien el valor en la otra base")
    p.add_argument("--porcion-g", type=dec, default=None, dest="porcion_g",
                   help="gramos por porcion o por capsula, para calcular mg por porcion")
    p.add_argument("--analito", default="analito", help="nombre del analito, solo para la salida")
    return p


def main(argv):
    if "--test" in argv:
        return autotest()
    p = construir_parser()
    args = p.parse_args(argv)
    if args.valor is None or args.unidad is None or args.base is None:
        p.print_help()
        print("")
        print("Faltan --valor, --unidad y --base. La BASE es obligatoria a proposito:")
        print("un porcentaje sin base no se puede comparar con nada.")
        return 0
    try:
        mg_g = a_mg_g(args.valor, args.unidad)
        tb = tabla(mg_g)
        otra = cambiar_base(mg_g, args.base, args.humedad)

        print("CONVERSION DE UNIDADES  —  analito: %s" % args.analito)
        print("  Entrada       : %s %s   BASE %s" % (n(args.valor, 6), args.unidad, args.base.upper()))
        print("")
        print("  EN BASE %s:" % args.base.upper())
        print("    %-8s %s" % ("% p/p", n(tb["pct"], 6)))
        print("    %-8s %s" % ("mg/g", n(tb["mg/g"], 6)))
        print("    %-8s %s" % ("g/kg", n(tb["g/kg"], 6)))
        print("    %-8s %s" % ("ppm", n(tb["ppm"], 4)))
        print("    %-8s %s   (identico a ppm)" % ("ug/g", n(tb["ug/g"], 4)))
        print("    %-8s %s   (identico a ppm)" % ("mg/kg", n(tb["mg/kg"], 4)))

        if args.porcion_g is not None:
            mg = por_porcion(mg_g, args.porcion_g)
            print("")
            print("  POR PORCION (%s g por porcion, BASE %s):" % (n(args.porcion_g, 4), args.base.upper()))
            print("    %s mg de %s por porcion" % (n(mg, 4), args.analito))

        print("")
        if otra is None:
            print("  OTRA BASE: no calculada. Da --humedad para convertir entre base seca y humeda.")
        else:
            destino = "SECA" if args.base == "humeda" else "HUMEDA (tal cual)"
            tb2 = tabla(otra)
            print("  EN BASE %s (con humedad %s %% p/p):" % (destino, n(args.humedad, 2)))
            print("    %s %% p/p   |   %s mg/g   |   %s ppm" % (n(tb2["pct"], 6), n(tb2["mg/g"], 6), n(tb2["ppm"], 4)))
            if args.porcion_g is not None:
                print("    %s mg por porcion de %s g" % (n(por_porcion(otra, args.porcion_g), 4), n(args.porcion_g, 4)))

        print("")
        print("  Recordatorio: ppm = mg/kg = ug/g es exacto en masa/masa. ppm = mg/L SOLO vale en")
        print("  soluciones acuosas diluidas (densidad ~1 g/mL) y este script no lo asume por ti.")
        return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))