#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
base_seca.py — Conversion base humeda <-> base seca y comparacion honesta de dos COA.

QUE CALCULA
  1) Un valor de composicion (% p/p, mg/g, ppm) de base HUMEDA (tal cual, "as is") a base SECA
     ("dry basis", "dry weight basis / DWB"), y al reves.
  2) La comparacion de dos certificados de analisis (COA) con humedades distintas, llevando ambos a
     base seca, que es la UNICA forma valida de compararlos.
  3) El reajuste de un valor medido a otra humedad objetivo (por ejemplo: "mi COA salio con 9,2 %
     de humedad, pero mi especificacion de producto exige reportar a 8 %").

FORMULAS
  Sea h la humedad en % p/p (masa de agua / masa total tal cual x 100).
  Fraccion de solidos (materia seca):   s = 1 - h/100
      valor_base_seca   = valor_tal_cual / s
      valor_tal_cual    = valor_base_seca * s
      valor a humedad h2 = valor a humedad h1 * (1 - h2/100) / (1 - h1/100)

  Todo esto es balance de masa puro: el analito no cambia, cambia el denominador.

DE DONDE SALE
  Es la definicion misma de base seca, usada en farmacopeas (USP <731> "Loss on drying", Ph. Eur. 2.2.32)
  y en los metodos AOAC de composicion. La humedad se mide por perdida por secado (LOD, "loss on drying")
  o por Karl Fischer; NO son intercambiables y el COA debe decir cual uso.

QUE **NO** HACE
  - No mide humedad. Consume la humedad que te reporta el laboratorio.
  - No corrige por solventes residuales ni por volatiles distintos del agua: si secaste a 105 C, lo que
    se fue no fue solo agua (tambien terpenos y otros volatiles). Por eso LOD y Karl Fischer difieren.
  - No convierte entre base seca y base "libre de cenizas" ni base "libre de solvente".
  - No compara dos COA que midieron el analito con METODOS distintos: llevar ambos a base seca los hace
    comparables en la BASE, no en el METODO. Un beta-glucano por Megazyme y un "polisacarido total" por
    fenol-sulfurico no se comparan aunque los pongas en la misma base.
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP

getcontext().prec = 34


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

def fraccion_solidos(humedad_pct):
    exigir(humedad_pct >= 0, "La humedad no puede ser negativa.")
    exigir(humedad_pct < 100, "La humedad no puede ser 100 % ni mas: seria agua pura, sin materia seca.")
    return Decimal(1) - humedad_pct / Decimal(100)


def a_base_seca(valor, humedad_pct):
    exigir(valor >= 0, "El valor no puede ser negativo.")
    return valor / fraccion_solidos(humedad_pct)


def a_base_humeda(valor, humedad_pct):
    exigir(valor >= 0, "El valor no puede ser negativo.")
    return valor * fraccion_solidos(humedad_pct)


def rehumedecer(valor, humedad_origen, humedad_destino):
    """Pasa un valor medido a humedad h1 hacia como se veria a humedad h2."""
    seco = a_base_seca(valor, humedad_origen)
    return a_base_humeda(seco, humedad_destino)


def comparar(valor_a, humedad_a, valor_b, humedad_b):
    seca_a = a_base_seca(valor_a, humedad_a)
    seca_b = a_base_seca(valor_b, humedad_b)
    exigir(seca_b != 0, "El COA B da 0 en base seca: no se puede calcular la diferencia relativa.")
    return {
        "seca_a": seca_a,
        "seca_b": seca_b,
        "diferencia": seca_a - seca_b,
        "diferencia_rel_pct": (seca_a - seca_b) * Decimal(100) / seca_b,
        "mejor": "A" if seca_a > seca_b else ("B" if seca_b > seca_a else "empate"),
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
        print("OK - %d pruebas pasaron (base_seca.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST base_seca.py")

    # 1. Caso de referencia: 30 % p/p tal cual con 8 % de humedad
    seco = a_base_seca(Decimal("30"), Decimal("8"))
    t.cerca("30 % p/p tal cual, 8 % humedad -> base seca", seco, "32.6086956521739130", "1e-12")
    # segunda via: ida y vuelta
    t.cerca("inversa: base seca -> tal cual", a_base_humeda(seco, Decimal("8")), "30", "1e-12")
    # segunda via independiente: 30 / 0,92
    t.cerca("segunda via 30/0,92", Decimal("30") / Decimal("0.92"), seco, "1e-12")

    # 2. Humedad 0 no cambia nada
    t.cerca("humedad 0 % no cambia el valor", a_base_seca(Decimal("12.5"), Decimal("0")), "12.5", "1e-12")

    # 3. Base seca siempre >= tal cual
    t.cierto("base seca >= tal cual (siempre)", a_base_seca(Decimal("5"), Decimal("15")) > Decimal("5"), "no")

    # 4. Reajuste de humedad y su inversa
    r = rehumedecer(Decimal("28.5"), Decimal("9.2"), Decimal("8"))
    t.cerca("28,5 % a 9,2 % humedad, reportado a 8 % humedad", r, "28.8766519823788546", "1e-12")
    t.cerca("inversa del reajuste", rehumedecer(r, Decimal("8"), Decimal("9.2")), "28.5", "1e-12")

    # 5. Comparacion de dos COA: el que parece mejor tal cual no siempre lo es en base seca
    c = comparar(Decimal("29.0"), Decimal("4.0"), Decimal("29.5"), Decimal("11.0"))
    t.cerca("COA A 29,0 % con 4 % humedad -> base seca", c["seca_a"], "30.2083333333333333", "1e-12")
    t.cerca("COA B 29,5 % con 11 % humedad -> base seca", c["seca_b"], "33.1460674157303371", "1e-12")
    t.cierto("tal cual gana A, en base seca gana B (la trampa clasica)",
             Decimal("29.0") < Decimal("29.5") and c["mejor"] == "B", "no reproduce la trampa")
    t.cerca("diferencia relativa A vs B [%]", c["diferencia_rel_pct"], "-8.8629943502824859", "1e-10")

    # 6. Consistencia de escala: la conversion es lineal, sirve igual para % , mg/g y ppm
    t.cerca("linealidad: 300 mg/g con 8 % humedad", a_base_seca(Decimal("300"), Decimal("8")), seco * 10, "1e-12")

    # 7. Validaciones
    for descripcion, fn in [
        ("rechaza humedad de 100 %", lambda: a_base_seca(Decimal("30"), Decimal("100"))),
        ("rechaza humedad > 100 %", lambda: a_base_seca(Decimal("30"), Decimal("120"))),
        ("rechaza humedad negativa", lambda: a_base_seca(Decimal("30"), Decimal("-1"))),
        ("rechaza valor negativo", lambda: a_base_seca(Decimal("-5"), Decimal("8"))),
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
        prog="base_seca.py",
        description="Base humeda <-> base seca por humedad, y comparacion de dos COA con humedades distintas.",
        epilog="La unidad la eliges tu (--unidad) y se imprime siempre junto con la base.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    sub = p.add_subparsers(dest="modo")

    def unidad(sp):
        sp.add_argument("--unidad", default="% p/p",
                        help="etiqueta de unidad para la salida (def. '%% p/p'); no altera el calculo")

    a = sub.add_parser("a-seca", help="de base humeda (tal cual) a base seca")
    a.add_argument("--valor", type=dec, required=True, help="valor medido tal cual")
    a.add_argument("--humedad", type=dec, required=True, help="humedad en %% p/p")
    unidad(a)

    b = sub.add_parser("a-humeda", help="de base seca a base humeda (tal cual)")
    b.add_argument("--valor", type=dec, required=True, help="valor en base seca")
    b.add_argument("--humedad", type=dec, required=True, help="humedad objetivo en %% p/p")
    unidad(b)

    r = sub.add_parser("reajustar", help="pasar un valor de una humedad a otra")
    r.add_argument("--valor", type=dec, required=True, help="valor medido")
    r.add_argument("--humedad-origen", type=dec, required=True, dest="h1", help="humedad a la que se midio")
    r.add_argument("--humedad-destino", type=dec, required=True, dest="h2", help="humedad a la que quieres reportar")
    unidad(r)

    c = sub.add_parser("comparar", help="compara dos COA llevandolos a base seca")
    c.add_argument("--valor-a", type=dec, required=True, dest="va", help="valor tal cual del COA A")
    c.add_argument("--humedad-a", type=dec, required=True, dest="ha", help="humedad del COA A en %%")
    c.add_argument("--valor-b", type=dec, required=True, dest="vb", help="valor tal cual del COA B")
    c.add_argument("--humedad-b", type=dec, required=True, dest="hb", help="humedad del COA B en %%")
    unidad(c)
    return p


def main(argv):
    if "--test" in argv:
        return autotest()
    p = construir_parser()
    args = p.parse_args(argv)
    if not args.modo:
        p.print_help()
        return 0
    u = args.unidad
    try:
        if args.modo == "a-seca":
            s = fraccion_solidos(args.humedad)
            r = a_base_seca(args.valor, args.humedad)
            print("CONVERSION A BASE SECA")
            print("  Entrada        : %s %s  BASE HUMEDA (tal cual)" % (n(args.valor), u))
            print("  Humedad        : %s %% p/p   (materia seca = %s %% p/p)" % (n(args.humedad, 2), n(s * 100, 2)))
            print("  Resultado      : %s %s  BASE SECA" % (n(r), u))
            print("  Comprobacion   : %s x %s = %s %s tal cual" % (n(r), n(s, 6), n(r * s), u))

        elif args.modo == "a-humeda":
            s = fraccion_solidos(args.humedad)
            r = a_base_humeda(args.valor, args.humedad)
            print("CONVERSION A BASE HUMEDA (TAL CUAL)")
            print("  Entrada        : %s %s  BASE SECA" % (n(args.valor), u))
            print("  Humedad objetivo: %s %% p/p" % n(args.humedad, 2))
            print("  Resultado      : %s %s  BASE HUMEDA (tal cual)" % (n(r), u))
            print("  Comprobacion   : %s / %s = %s %s base seca" % (n(r), n(s, 6), n(r / s), u))

        elif args.modo == "reajustar":
            r = rehumedecer(args.valor, args.h1, args.h2)
            print("REAJUSTE DE HUMEDAD")
            print("  Valor medido a %s %% de humedad : %s %s" % (n(args.h1, 2), n(args.valor), u))
            print("  Base seca equivalente          : %s %s BASE SECA" % (n(a_base_seca(args.valor, args.h1)), u))
            print("  Valor equivalente a %s %% humedad: %s %s BASE HUMEDA" % (n(args.h2, 2), n(r), u))

        elif args.modo == "comparar":
            c = comparar(args.va, args.ha, args.vb, args.hb)
            print("COMPARACION DE DOS COA (la unica valida es en base seca)")
            print("  COA A: %s %s tal cual con %s %% humedad -> %s %s BASE SECA"
                  % (n(args.va), u, n(args.ha, 2), n(c["seca_a"]), u))
            print("  COA B: %s %s tal cual con %s %% humedad -> %s %s BASE SECA"
                  % (n(args.vb), u, n(args.hb, 2), n(c["seca_b"]), u))
            print("")
            print("  Diferencia (A - B) en base seca : %s %s" % (n(c["diferencia"]), u))
            print("  Diferencia relativa             : %s %% respecto de B" % n(c["diferencia_rel_pct"], 2))
            print("  Mas concentrado en base seca    : %s" % c["mejor"])
            if (args.va > args.vb) != (c["seca_a"] > c["seca_b"]):
                print("")
                print("  OJO: el orden SE INVIRTIO al pasar a base seca. Tal cual parecia ganar uno y")
                print("  en base seca gana el otro. Esta es la trampa mas comun al comparar proveedores.")
            print("")
            print("  Recordatorio: misma base NO es lo mismo que mismo metodo. Verifica que ambos COA")
            print("  midieron el analito con la misma tecnica antes de declarar un ganador.")
        return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))