#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
betaglucano_dosis.py — Del % de beta-glucano del COA a los miligramos que de verdad entrega tu producto.

QUE CALCULA
  1) DIRECTO: partiendo del % de beta-glucano del certificado de analisis (COA), en base seca,
     cuantos mg de beta-glucano hay por capsula y cuantos por porcion diaria.
  2) INVERSO: cuanto extracto (mg por dia, y cuantas capsulas) hace falta para entregar X mg/dia
     de beta-glucano.
  3) El aporte real de una MEZCLA de extractos (varias especies en la misma capsula).

FORMULAS
      mg_beta_por_capsula = mg_extracto_por_capsula x (%BG_base_seca/100) x (1 - humedad/100)
      mg_beta_por_dia     = mg_beta_por_capsula x capsulas_por_dia
      inverso:
      mg_extracto_por_dia = mg_beta_objetivo / [(%BG/100) x (1 - humedad/100)]
      capsulas_por_dia    = mg_extracto_por_dia / mg_extracto_por_capsula   (se redondea HACIA ARRIBA)

  El termino (1 - humedad/100) es el que casi todo el mundo olvida: el COA reporta en BASE SECA,
  pero tu llenas la capsula con polvo REAL, que trae agua. Si no lo corriges, sobreestimas la dosis.
  Si tu COA ya viene en base tal cual ("as is"), usa --base humeda y no se aplica esa correccion.

DE DONDE SALE
  Es aritmetica de composicion (masa de analito / masa de material). Lo delicado no es la cuenta,
  es el DATO DE ENTRADA:
  - beta-glucano se mide por metodo ENZIMATICO (Megazyme K-YBGL o equivalente AOAC/AACC), que
    calcula beta-glucano = glucano total - alfa-glucano.
  - "Polisacaridos totales" (fenol-sulfurico) NO es beta-glucano: incluye almidon (alfa-glucano) y
    por eso un micelio sobre grano puede reportar "40 % de polisacaridos" siendo casi todo arroz.
  Si tu COA dice "polisacaridos", este script te dara mg de un numero que no es lo que crees.

QUE **NO** HACE
  - No convierte polisacaridos totales en beta-glucano (no existe factor valido para eso).
  - No dice cual es la dosis "correcta" ni "efectiva": eso depende de la evidencia por especie y
    por indicacion, y este script no la contiene. Ver los modulos de dosificacion de la skill.
  - No hace ningun claim de salud. Un miligramo no es un beneficio.
  - No corrige por perdida en proceso ni por degradacion en vida util: para eso usa potencia_formula.py.
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP, ROUND_CEILING

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

def valida_pct(valor, nombre):
    exigir(valor >= 0, "%s no puede ser negativo." % nombre)
    exigir(valor <= 100, "%s no puede superar 100 %%." % nombre)
    return valor


def factor_efectivo(bg_pct, base, humedad_pct):
    """
    Fraccion de beta-glucano por gramo de polvo REAL (tal cual se pesa para llenar la capsula).
    """
    valida_pct(bg_pct, "El % de beta-glucano")
    if base == "seca":
        if humedad_pct is None:
            return bg_pct / Decimal(100), False
        exigir(Decimal(0) <= humedad_pct < Decimal(100),
               "La humedad debe estar entre 0 y 100 % (100 % es imposible).")
        return (bg_pct / Decimal(100)) * (Decimal(1) - humedad_pct / Decimal(100)), True
    # base humeda: el COA ya viene tal cual
    return bg_pct / Decimal(100), True


def directo(mg_extracto_capsula, capsulas_dia, bg_pct, base, humedad_pct):
    exigir(mg_extracto_capsula > 0, "Los mg de extracto por capsula deben ser mayores que cero.")
    exigir(capsulas_dia > 0, "Las capsulas por dia deben ser mayores que cero.")
    f, corregido = factor_efectivo(bg_pct, base, humedad_pct)
    por_capsula = mg_extracto_capsula * f
    return {
        "factor": f,
        "corregido_por_humedad": corregido,
        "mg_por_capsula": por_capsula,
        "mg_por_dia": por_capsula * capsulas_dia,
        "mg_extracto_dia": mg_extracto_capsula * capsulas_dia,
    }


def inverso(mg_objetivo_dia, mg_extracto_capsula, bg_pct, base, humedad_pct):
    exigir(mg_objetivo_dia > 0, "El objetivo de mg/dia debe ser mayor que cero.")
    exigir(mg_extracto_capsula > 0, "Los mg de extracto por capsula deben ser mayores que cero.")
    f, corregido = factor_efectivo(bg_pct, base, humedad_pct)
    exigir(f > 0, "Con 0 % de beta-glucano no se puede llegar a ninguna dosis.")
    mg_extracto_dia = mg_objetivo_dia / f
    capsulas_exactas = mg_extracto_dia / mg_extracto_capsula
    capsulas_enteras = capsulas_exactas.to_integral_value(rounding=ROUND_CEILING)
    entregado = capsulas_enteras * mg_extracto_capsula * f
    return {
        "factor": f,
        "corregido_por_humedad": corregido,
        "mg_extracto_dia": mg_extracto_dia,
        "capsulas_exactas": capsulas_exactas,
        "capsulas_enteras": capsulas_enteras,
        "mg_entregados_dia": entregado,
        "exceso_pct": (entregado - mg_objetivo_dia) * Decimal(100) / mg_objetivo_dia,
    }


def mezcla(componentes, capsulas_dia):
    """
    componentes: lista de (nombre, mg_extracto_por_capsula, bg_pct, base, humedad|None)
    """
    exigir(len(componentes) > 0, "La mezcla necesita al menos un componente.")
    exigir(capsulas_dia > 0, "Las capsulas por dia deben ser mayores que cero.")
    filas = []
    total_cap = Decimal(0)
    total_bg = Decimal(0)
    for nombre, mg, bg, base, hum in componentes:
        exigir(mg > 0, "Los mg de '%s' deben ser mayores que cero." % nombre)
        f, _ = factor_efectivo(bg, base, hum)
        aporte = mg * f
        filas.append({"nombre": nombre, "mg_extracto": mg, "bg_pct": bg, "base": base,
                      "mg_bg_capsula": aporte})
        total_cap += mg
        total_bg += aporte
    exigir(total_cap <= Decimal("1500"),
           "La mezcla suma %s mg por capsula: no cabe en una capsula estandar (00 = ~800-1000 mg de "
           "polvo). Revisa el reparto." % total_cap)
    return {
        "filas": filas,
        "mg_extracto_capsula": total_cap,
        "mg_bg_capsula": total_bg,
        "mg_bg_dia": total_bg * capsulas_dia,
        "bg_pct_mezcla": total_bg * Decimal(100) / total_cap,
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
        print("OK - %d pruebas pasaron (betaglucano_dosis.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST betaglucano_dosis.py")

    # 1. Caso limpio sin humedad: 30 % BG, 500 mg/capsula, 2 capsulas/dia
    d = directo(Decimal("500"), Decimal("2"), Decimal("30"), "seca", None)
    t.cerca("30 % BG, 500 mg/cap -> mg BG por capsula", d["mg_por_capsula"], "150", "1e-12")
    t.cerca("2 capsulas/dia -> mg BG por dia", d["mg_por_dia"], "300", "1e-12")

    # 2. VERIFICACION POR SEGUNDA VIA: el inverso devuelve exactamente esas 2 capsulas
    i = inverso(Decimal("300"), Decimal("500"), Decimal("30"), "seca", None)
    t.cerca("inverso: mg de extracto/dia para 300 mg BG", i["mg_extracto_dia"], "1000", "1e-12")
    t.cerca("inverso: capsulas exactas", i["capsulas_exactas"], "2", "1e-12")
    t.cerca("inverso: capsulas enteras (redondeo hacia arriba)", i["capsulas_enteras"], "2", "1e-12")
    t.cerca("inverso: mg entregados = objetivo", i["mg_entregados_dia"], "300", "1e-12")

    # 3. Correccion por humedad (el error que casi nadie hace)
    dh = directo(Decimal("500"), Decimal("2"), Decimal("30"), "seca", Decimal("6"))
    t.cerca("mismo caso con 6 % de humedad -> mg BG por capsula", dh["mg_por_capsula"], "141", "1e-12")
    t.cerca("...y por dia", dh["mg_por_dia"], "282", "1e-12")
    t.cierto("corregir por humedad SIEMPRE baja la dosis entregada",
             dh["mg_por_dia"] < d["mg_por_dia"], "no bajo")
    # inverso con humedad y su ida-vuelta
    ih = inverso(Decimal("282"), Decimal("500"), Decimal("30"), "seca", Decimal("6"))
    t.cerca("inverso con humedad devuelve 2 capsulas", ih["capsulas_enteras"], "2", "1e-12")
    t.cerca("inverso con humedad: mg entregados", ih["mg_entregados_dia"], "282", "1e-12")

    # 4. Redondeo hacia arriba de capsulas (nunca se entrega de menos)
    i2 = inverso(Decimal("400"), Decimal("500"), Decimal("30"), "seca", None)
    t.cerca("400 mg BG objetivo -> capsulas exactas", i2["capsulas_exactas"], "2.6666666666666667", "1e-12")
    t.cerca("400 mg BG objetivo -> capsulas enteras", i2["capsulas_enteras"], "3", "1e-12")
    t.cierto("con capsulas enteras nunca se entrega de menos",
             i2["mg_entregados_dia"] >= Decimal("400"), "entrega de menos")
    t.cerca("exceso por redondear a 3 capsulas [%]", i2["exceso_pct"], "12.5", "1e-12")

    # 5. Base humeda: el COA ya viene tal cual, no se corrige dos veces
    dhum = directo(Decimal("500"), Decimal("2"), Decimal("28.2"), "humeda", Decimal("6"))
    t.cerca("COA en base humeda 28,2 % -> mg/dia", dhum["mg_por_dia"], "282", "1e-12")
    t.cerca("coincide con el de base seca 30 % + 6 % humedad", dhum["mg_por_dia"], dh["mg_por_dia"], "1e-12")

    # 6. Mezcla de dos extractos
    m = mezcla([
        ("reishi", Decimal("300"), Decimal("30"), "seca", None),
        ("melena de leon", Decimal("200"), Decimal("25"), "seca", None),
    ], Decimal("2"))
    t.cerca("mezcla: mg de extracto por capsula", m["mg_extracto_capsula"], "500", "1e-12")
    t.cerca("mezcla: mg BG por capsula (90 + 50)", m["mg_bg_capsula"], "140", "1e-12")
    t.cerca("mezcla: mg BG por dia (2 caps)", m["mg_bg_dia"], "280", "1e-12")
    t.cerca("mezcla: % BG resultante de la mezcla", m["bg_pct_mezcla"], "28", "1e-12")
    # segunda via: el % de la mezcla usado en el modo directo da lo mismo
    dm = directo(Decimal("500"), Decimal("2"), m["bg_pct_mezcla"], "seca", None)
    t.cerca("segunda via: directo con el % de la mezcla", dm["mg_por_dia"], m["mg_bg_dia"], "1e-12")

    # 7. Validaciones
    for descripcion, fn in [
        ("rechaza % de beta-glucano > 100", lambda: directo(Decimal("500"), Decimal("1"), Decimal("120"), "seca", None)),
        ("rechaza % negativo", lambda: directo(Decimal("500"), Decimal("1"), Decimal("-5"), "seca", None)),
        ("rechaza 0 mg de extracto", lambda: directo(Decimal("0"), Decimal("1"), Decimal("30"), "seca", None)),
        ("rechaza 0 capsulas/dia", lambda: directo(Decimal("500"), Decimal("0"), Decimal("30"), "seca", None)),
        ("rechaza humedad de 100 %", lambda: directo(Decimal("500"), Decimal("1"), Decimal("30"), "seca", Decimal("100"))),
        ("rechaza objetivo de 0 mg/dia", lambda: inverso(Decimal("0"), Decimal("500"), Decimal("30"), "seca", None)),
        ("rechaza extracto con 0 % de BG en el inverso",
         lambda: inverso(Decimal("300"), Decimal("500"), Decimal("0"), "seca", None)),
        ("rechaza mezcla que no cabe en una capsula",
         lambda: mezcla([("a", Decimal("1200"), Decimal("30"), "seca", None),
                         ("b", Decimal("600"), Decimal("30"), "seca", None)], Decimal("1"))),
    ]:
        try:
            fn()
            t.cierto(descripcion, False, "no lanzo ErrorDeEntrada")
        except ErrorDeEntrada:
            t.cierto(descripcion, True)

    return t.resultado()


# ----------------------------------------------------------------------------- CLI

def _nota_metodo(bg_pct):
    print("")
    print("  METODO DEL DATO DE ENTRADA: este calculo vale solo si el %s %% viene de un metodo" % n(bg_pct, 2))
    print("  ENZIMATICO de beta-glucano (Megazyme K-YBGL / AOAC-AACC: glucano total - alfa-glucano).")
    print("  Si tu COA dice 'polisacaridos totales', NO es beta-glucano y estos mg son ficcion.")
    print("  Sin claims de salud: un miligramo no es un beneficio.")


def construir_parser():
    p = argparse.ArgumentParser(
        prog="betaglucano_dosis.py",
        description="Del %% de beta-glucano del COA (base seca) a mg por capsula y por porcion diaria, "
                    "y el inverso.",
        epilog="Siempre se imprime la unidad y la base. La correccion por humedad es opcional pero "
               "es la diferencia entre la dosis de la etiqueta y la dosis real.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    sub = p.add_subparsers(dest="modo")

    d = sub.add_parser("directo", help="del %% del COA a mg por capsula y por dia")
    d.add_argument("--bg-pct", type=dec, required=True, dest="bg", help="%% de beta-glucano del COA")
    d.add_argument("--base", choices=["seca", "humeda"], required=True, help="base del dato del COA")
    d.add_argument("--mg-capsula", type=dec, required=True, dest="mg_cap",
                   help="mg de extracto por capsula")
    d.add_argument("--capsulas-dia", type=dec, default=Decimal("1"), dest="caps",
                   help="capsulas por dia (def. 1)")
    d.add_argument("--humedad", type=dec, default=None,
                   help="humedad del polvo en %% p/p (corrige de base seca a polvo real)")

    i = sub.add_parser("inverso", help="cuanto extracto hace falta para entregar X mg/dia")
    i.add_argument("--objetivo-mg-dia", type=dec, required=True, dest="obj",
                   help="mg de beta-glucano que quieres entregar por dia")
    i.add_argument("--bg-pct", type=dec, required=True, dest="bg", help="%% de beta-glucano del COA")
    i.add_argument("--base", choices=["seca", "humeda"], required=True, help="base del dato del COA")
    i.add_argument("--mg-capsula", type=dec, required=True, dest="mg_cap",
                   help="mg de extracto por capsula")
    i.add_argument("--humedad", type=dec, default=None, help="humedad del polvo en %% p/p")

    m = sub.add_parser("mezcla", help="aporte real de una mezcla de extractos")
    m.add_argument("--componente", action="append", required=True, dest="componentes",
                   metavar="NOMBRE:MG:BGPCT",
                   help="repetible. Formato NOMBRE:MG_POR_CAPSULA:PORCENTAJE_BG "
                        "(ej: reishi:300:30). Se asume base seca.")
    m.add_argument("--capsulas-dia", type=dec, default=Decimal("1"), dest="caps",
                   help="capsulas por dia (def. 1)")
    m.add_argument("--humedad", type=dec, default=None,
                   help="humedad comun de los polvos en %% p/p")
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
        if args.modo == "directo":
            r = directo(args.mg_cap, args.caps, args.bg, args.base, args.humedad)
            print("BETA-GLUCANO ENTREGADO POR EL PRODUCTO")
            print("  COA            : %s %% p/p de beta-glucano, BASE %s" % (n(args.bg, 2), args.base.upper()))
            if r["corregido_por_humedad"] and args.base == "seca":
                print("  Humedad polvo  : %s %% p/p -> corregido a polvo real" % n(args.humedad, 2))
            elif args.base == "seca":
                print("  Humedad polvo  : no declarada -> SIN corregir (la dosis real sera algo menor)")
            print("  Extracto       : %s mg por capsula x %s capsulas/dia = %s mg de extracto/dia"
                  % (n(args.mg_cap, 2), n(args.caps, 2), n(r["mg_extracto_dia"], 2)))
            print("")
            print("  Beta-glucano por capsula : %s mg" % n(r["mg_por_capsula"], 2))
            print("  Beta-glucano por dia     : %s mg" % n(r["mg_por_dia"], 2))
            _nota_metodo(args.bg)
            return 0

        if args.modo == "inverso":
            r = inverso(args.obj, args.mg_cap, args.bg, args.base, args.humedad)
            print("CUANTO EXTRACTO HACE FALTA (modo inverso)")
            print("  Objetivo       : %s mg de beta-glucano por dia" % n(args.obj, 2))
            print("  COA            : %s %% p/p de beta-glucano, BASE %s" % (n(args.bg, 2), args.base.upper()))
            if args.humedad is not None:
                print("  Humedad polvo  : %s %% p/p" % n(args.humedad, 2))
            print("")
            print("  Extracto necesario : %s mg por dia" % n(r["mg_extracto_dia"], 2))
            print("  Capsulas de %s mg  : %s (exacto)  ->  %s capsulas/dia (redondeo hacia arriba)"
                  % (n(args.mg_cap, 0), n(r["capsulas_exactas"], 3), r["capsulas_enteras"]))
            print("  Entrega real       : %s mg de beta-glucano/dia (%s %% por encima del objetivo)"
                  % (n(r["mg_entregados_dia"], 2), n(r["exceso_pct"], 2)))
            _nota_metodo(args.bg)
            return 0

        if args.modo == "mezcla":
            comps = []
            for c in args.componentes:
                partes = c.split(":")
                exigir(len(partes) == 3,
                       "Componente mal escrito: '%s'. Formato NOMBRE:MG:BGPCT (ej: reishi:300:30)." % c)
                try:
                    comps.append((partes[0], Decimal(partes[1].replace(",", ".")),
                                  Decimal(partes[2].replace(",", ".")), "seca", args.humedad))
                except InvalidOperation:
                    raise ErrorDeEntrada("Numeros invalidos en el componente '%s'." % c)
            r = mezcla(comps, args.caps)
            print("MEZCLA DE EXTRACTOS — APORTE REAL DE BETA-GLUCANO")
            print("  Base de todos los datos: SECA%s" %
                  ("" if args.humedad is None else " (corregida por humedad %s %%)" % n(args.humedad, 2)))
            print("")
            print("  %-20s %10s %10s %14s" % ("componente", "mg/cap", "% BG", "mg BG/cap"))
            for f in r["filas"]:
                print("  %-20s %10s %10s %14s"
                      % (f["nombre"][:20], n(f["mg_extracto"], 1), n(f["bg_pct"], 2), n(f["mg_bg_capsula"], 2)))
            print("  %-20s %10s %10s %14s"
                  % ("TOTAL", n(r["mg_extracto_capsula"], 1), n(r["bg_pct_mezcla"], 2), n(r["mg_bg_capsula"], 2)))
            print("")
            print("  Beta-glucano por dia (%s capsulas): %s mg" % (n(args.caps, 2), n(r["mg_bg_dia"], 2)))
            print("  Equivale a una mezcla de %s %% p/p de beta-glucano" % n(r["bg_pct_mezcla"], 2))
            print("")
            print("  METODO: cada %% debe venir de metodo enzimatico (Megazyme K-YBGL) sobre ESE extracto.")
            print("  Sumar %% de COA distintos solo es valido si los tres se midieron igual y en la misma base.")
            return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))