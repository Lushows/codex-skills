#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rendimiento_extraccion.py — Rendimiento, factor de concentracion, ratio planta:extracto y recuperacion
del activo. La herramienta para auditar un extracto que dice "10:1".

QUE CALCULA
  1) Rendimiento de extraccion en % p/p (cuanto extracto sale por cada 100 g de biomasa).
  2) Ratio planta:extracto REAL (el 10:1, 4:1, etc.) y su comparacion con el ratio DECLARADO
     por el proveedor. Si no coinciden, alguien esta redondeando a su favor.
  3) Factor de concentracion del marcador: cuantas veces mas concentrado quedo el activo en el
     extracto respecto de la biomasa de partida.
  4) Recuperacion del activo: que porcentaje del marcador que habia en la planta termino en el
     extracto. Lo demas se quedo en el bagazo o se destruyo.

FORMULAS
      rendimiento (%)        = masa_extracto / masa_biomasa x 100
      ratio planta:extracto  = masa_biomasa / masa_extracto        (ej. 10 -> "10:1")
      ratio = 100 / rendimiento(%)                                  (son el mismo dato al reves)

      factor de concentracion = %activo_extracto / %activo_biomasa
      recuperacion (%)        = (masa_extracto x %activo_extracto) / (masa_biomasa x %activo_biomasa) x 100

  IDENTIDAD CLAVE (la que usa este script para verificarse por segunda via):
      recuperacion (%) = rendimiento (fraccion) x factor_de_concentracion x 100
  Si el factor de concentracion es MAYOR que el ratio planta:extracto, la recuperacion pasaria de
  100 %: eso es fisicamente imposible y el script lo marca como bandera roja.

  Todo con humedades opcionales para llevar biomasa y extracto a BASE SECA, que es la unica forma
  honesta de comparar (biomasa fresca con 70 % de agua "rinde" mucho peor que la misma seca).

DE DONDE SALE
  Balance de masa. El ratio planta:extracto (DER, "drug-to-extract ratio") esta definido asi en las
  monografias de extractos vegetales (Ph. Eur. "Extracta", USP) y en el etiquetado de suplementos.

QUE **NO** HACE
  - No dice si el extracto es BUENO. Un 10:1 con recuperacion del 20 % del activo es un mal extracto
    con un buen numero de marketing. El ratio es de MASA, no de potencia.
  - No corrige por excipientes ni por soportes (maltodextrina, arroz): si el "extracto" trae 40 % de
    soporte, el ratio real es otro. Este script calcula con las masas que le des.
  - No modela la cinetica ni el equilibrio de extraccion (no predice cuanto sacaria otro solvente).
  - No mide nada: consume masas de balanza y % de COA.
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

def masa_seca(masa, humedad_pct):
    exigir(masa > 0, "Las masas deben ser mayores que cero.")
    if humedad_pct is None:
        return masa, False
    exigir(Decimal(0) <= humedad_pct < Decimal(100),
           "La humedad debe estar entre 0 y 100 % (100 % es imposible: seria agua pura).")
    return masa * (Decimal(1) - humedad_pct / Decimal(100)), True


def rendimiento(masa_biomasa, masa_extracto, hum_biomasa=None, hum_extracto=None):
    mb, cb = masa_seca(masa_biomasa, hum_biomasa)
    me, ce = masa_seca(masa_extracto, hum_extracto)
    exigir(me <= mb,
           "El extracto (%s) pesa mas que la biomasa de partida (%s) en la misma base. "
           "Eso no es una extraccion: revisa masas, humedades o si hay soporte agregado." % (me, mb))
    r = me * Decimal(100) / mb
    return {
        "masa_biomasa_base": mb, "masa_extracto_base": me,
        "corregido": cb or ce,
        "rendimiento_pct": r,
        "ratio": mb / me,
    }


def ratio_a_rendimiento(ratio):
    exigir(ratio > 0, "El ratio planta:extracto debe ser mayor que cero.")
    exigir(ratio >= 1, "Un ratio menor que 1:1 significaria que sale mas extracto que planta.")
    return Decimal(100) / ratio


def activo(masa_biomasa, pct_biomasa, masa_extracto, pct_extracto,
           hum_biomasa=None, hum_extracto=None):
    """Factor de concentracion y recuperacion del marcador. Los % deben venir en la MISMA base."""
    exigir(Decimal(0) <= pct_biomasa <= 100, "El % de activo en la biomasa debe estar entre 0 y 100.")
    exigir(Decimal(0) <= pct_extracto <= 100, "El % de activo en el extracto debe estar entre 0 y 100.")
    exigir(pct_biomasa > 0, "Con 0 % de activo en la biomasa no se puede calcular concentracion ni recuperacion.")
    r = rendimiento(masa_biomasa, masa_extracto, hum_biomasa, hum_extracto)
    masa_act_bio = r["masa_biomasa_base"] * pct_biomasa / Decimal(100)
    masa_act_ext = r["masa_extracto_base"] * pct_extracto / Decimal(100)
    factor = pct_extracto / pct_biomasa
    recuperacion = masa_act_ext * Decimal(100) / masa_act_bio
    r.update({
        "masa_activo_biomasa": masa_act_bio,
        "masa_activo_extracto": masa_act_ext,
        "masa_activo_perdida": masa_act_bio - masa_act_ext,
        "factor_concentracion": factor,
        "recuperacion_pct": recuperacion,
        "factor_maximo_posible": r["ratio"],
    })
    return r


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
        print("OK - %d pruebas pasaron (rendimiento_extraccion.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST rendimiento_extraccion.py")

    # 1. Caso base: 100 g de biomasa -> 10 g de extracto
    r = rendimiento(Decimal("100"), Decimal("10"))
    t.cerca("rendimiento 100 g -> 10 g [% p/p]", r["rendimiento_pct"], "10", "1e-12")
    t.cerca("ratio planta:extracto", r["ratio"], "10", "1e-12")
    # segunda via: ratio y rendimiento son el mismo dato al reves
    t.cerca("segunda via: 100/ratio = rendimiento", ratio_a_rendimiento(r["ratio"]), r["rendimiento_pct"], "1e-12")

    # 2. Activo: 1 % en biomasa -> 8 % en extracto
    a = activo(Decimal("100"), Decimal("1"), Decimal("10"), Decimal("8"))
    t.cerca("factor de concentracion (8 % / 1 %)", a["factor_concentracion"], "8", "1e-12")
    t.cerca("recuperacion del activo [%]", a["recuperacion_pct"], "80", "1e-12")
    t.cerca("masa de activo en la biomasa [g]", a["masa_activo_biomasa"], "1", "1e-12")
    t.cerca("masa de activo en el extracto [g]", a["masa_activo_extracto"], "0.8", "1e-12")
    t.cerca("activo perdido en el bagazo [g]", a["masa_activo_perdida"], "0.2", "1e-12")
    # VERIFICACION POR SEGUNDA VIA: identidad recuperacion = rendimiento x factor
    t.cerca("identidad: rendimiento x factor = recuperacion",
            (a["rendimiento_pct"] / Decimal(100)) * a["factor_concentracion"] * Decimal(100),
            a["recuperacion_pct"], "1e-12")

    # 3. Un extracto perfecto (recuperacion 100 %) tiene factor = ratio
    perfecto = activo(Decimal("100"), Decimal("1"), Decimal("10"), Decimal("10"))
    t.cerca("recuperacion 100 % cuando factor = ratio", perfecto["recuperacion_pct"], "100", "1e-12")
    t.cerca("y el factor iguala al ratio", perfecto["factor_concentracion"], perfecto["ratio"], "1e-12")

    # 4. Bandera roja: recuperacion imposible (> 100 %) delata datos inconsistentes
    imposible = activo(Decimal("100"), Decimal("1"), Decimal("10"), Decimal("15"))
    t.cierto("detecta recuperacion imposible (> 100 %)",
             imposible["recuperacion_pct"] > Decimal("100"),
             "recuperacion = %s" % imposible["recuperacion_pct"])
    t.cierto("...y el factor supera el maximo fisico (el ratio)",
             imposible["factor_concentracion"] > imposible["factor_maximo_posible"], "no lo supera")

    # 5. Correccion por humedad: biomasa fresca vs seca
    hum = rendimiento(Decimal("1000"), Decimal("100"), Decimal("70"), Decimal("5"))
    t.cerca("biomasa 1000 g al 70 % humedad -> 300 g secos", hum["masa_biomasa_base"], "300", "1e-12")
    t.cerca("extracto 100 g al 5 % humedad -> 95 g secos", hum["masa_extracto_base"], "95", "1e-12")
    t.cerca("rendimiento en base seca [% p/p]", hum["rendimiento_pct"], "31.6666666666666667", "1e-12")
    t.cerca("ratio en base seca", hum["ratio"], "3.1578947368421053", "1e-12")
    sin_corregir = rendimiento(Decimal("1000"), Decimal("100"))
    t.cierto("ignorar la humedad SUBESTIMA el rendimiento (10 % vs 31,7 %)",
             sin_corregir["rendimiento_pct"] < hum["rendimiento_pct"], "no")

    # 6. Ratio declarado vs real
    real = rendimiento(Decimal("100"), Decimal("12.5"))
    t.cerca("12,5 g de extracto -> ratio real", real["ratio"], "8", "1e-12")
    t.cierto("un '10:1' declarado con ratio real 8:1 esta inflado",
             real["ratio"] < Decimal("10"), "no detecta la inflacion")
    t.cerca("inversa: ratio 8 -> rendimiento 12,5 %", ratio_a_rendimiento(Decimal("8")), "12.5", "1e-12")

    # 7. Validaciones
    for descripcion, fn in [
        ("rechaza masa de biomasa 0", lambda: rendimiento(Decimal("0"), Decimal("10"))),
        ("rechaza masa negativa", lambda: rendimiento(Decimal("100"), Decimal("-2"))),
        ("rechaza extracto que pesa mas que la biomasa", lambda: rendimiento(Decimal("10"), Decimal("20"))),
        ("rechaza humedad de 100 %", lambda: rendimiento(Decimal("100"), Decimal("10"), Decimal("100"))),
        ("rechaza humedad negativa", lambda: rendimiento(Decimal("100"), Decimal("10"), Decimal("-3"))),
        ("rechaza % de activo > 100", lambda: activo(Decimal("100"), Decimal("1"), Decimal("10"), Decimal("150"))),
        ("rechaza 0 % de activo en la biomasa",
         lambda: activo(Decimal("100"), Decimal("0"), Decimal("10"), Decimal("8"))),
        ("rechaza ratio menor que 1:1", lambda: ratio_a_rendimiento(Decimal("0.5"))),
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
        prog="rendimiento_extraccion.py",
        description="Rendimiento %% p/p, ratio planta:extracto real vs declarado, factor de concentracion "
                    "y recuperacion del activo.",
        epilog="Si das las humedades, todo se calcula en BASE SECA (lo correcto). Si no, se calcula "
               "tal cual y se advierte.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    p.add_argument("--biomasa-g", type=dec, dest="mb", help="masa de biomasa de partida en gramos")
    p.add_argument("--extracto-g", type=dec, dest="me", help="masa de extracto obtenido en gramos")
    p.add_argument("--humedad-biomasa", type=dec, default=None, dest="hb",
                   help="humedad de la biomasa en %% p/p (para calcular en base seca)")
    p.add_argument("--humedad-extracto", type=dec, default=None, dest="he",
                   help="humedad del extracto en %% p/p")
    p.add_argument("--activo-biomasa", type=dec, default=None, dest="ab",
                   help="%% del marcador en la biomasa (misma base que el extracto)")
    p.add_argument("--activo-extracto", type=dec, default=None, dest="ae",
                   help="%% del marcador en el extracto")
    p.add_argument("--ratio-declarado", type=dec, default=None, dest="rd",
                   help="ratio que declara el proveedor (ej. 10 para un '10:1')")
    p.add_argument("--marcador", default="activo", help="nombre del marcador, solo para la salida")
    return p


def main(argv):
    if "--test" in argv:
        return autotest()
    p = construir_parser()
    args = p.parse_args(argv)
    if args.mb is None or args.me is None:
        p.print_help()
        print("")
        print("Faltan --biomasa-g y --extracto-g, que son el minimo para calcular algo.")
        return 0
    try:
        hay_activo = args.ab is not None and args.ae is not None
        if hay_activo:
            r = activo(args.mb, args.ab, args.me, args.ae, args.hb, args.he)
        else:
            r = rendimiento(args.mb, args.me, args.hb, args.he)

        base = "SECA" if r["corregido"] else "TAL CUAL (humeda)"
        print("RENDIMIENTO DE EXTRACCION")
        print("  BASE DE CALCULO: %s" % base)
        print("  Biomasa  : %s g%s  ->  %s g en la base de calculo"
              % (n(args.mb, 3), "" if args.hb is None else " (humedad %s %%)" % n(args.hb, 2),
                 n(r["masa_biomasa_base"], 3)))
        print("  Extracto : %s g%s  ->  %s g en la base de calculo"
              % (n(args.me, 3), "" if args.he is None else " (humedad %s %%)" % n(args.he, 2),
                 n(r["masa_extracto_base"], 3)))
        print("")
        print("  Rendimiento           : %s %% p/p" % n(r["rendimiento_pct"], 3))
        print("  Ratio planta:extracto : %s : 1  (REAL, calculado de tus masas)" % n(r["ratio"], 3))
        if not r["corregido"]:
            print("")
            print("  ADVERTENCIA: no diste humedades, asi que esto NO es base seca. Si la biomasa venia")
            print("  humeda, el rendimiento real en base seca es MAYOR que el que ves aqui.")

        if args.rd is not None:
            print("")
            print("  --- RATIO DECLARADO vs REAL ---")
            print("  Declarado por el proveedor : %s : 1  (rendimiento implicito %s %% p/p)"
                  % (n(args.rd, 2), n(ratio_a_rendimiento(args.rd), 3)))
            print("  Real segun tus masas       : %s : 1" % n(r["ratio"], 3))
            dif = (r["ratio"] - args.rd) * Decimal(100) / args.rd
            print("  Diferencia                 : %s %% respecto del declarado" % n(dif, 2))
            if r["ratio"] < args.rd * Decimal("0.9"):
                print("  BANDERA ROJA: el ratio real es bastante MENOR que el declarado. O hay soporte")
                print("  agregado (maltodextrina, arroz), o el '%s:1' es marketing." % n(args.rd, 0))
            elif r["ratio"] > args.rd * Decimal("1.1"):
                print("  El ratio real es MAYOR que el declarado: el extracto esta mas concentrado en masa")
                print("  de lo que dice la etiqueta. Verifica que no sea un error de pesaje.")

        if hay_activo:
            print("")
            print("  --- MARCADOR: %s ---" % args.marcador)
            print("  En biomasa  : %s %% p/p  ->  %s g de %s"
                  % (n(args.ab, 4), n(r["masa_activo_biomasa"], 4), args.marcador))
            print("  En extracto : %s %% p/p  ->  %s g de %s"
                  % (n(args.ae, 4), n(r["masa_activo_extracto"], 4), args.marcador))
            print("  Perdido     : %s g (se quedo en el bagazo o se degrado)" % n(r["masa_activo_perdida"], 4))
            print("")
            print("  Factor de concentracion : %s x  (maximo fisico posible: %s x, que es el ratio)"
                  % (n(r["factor_concentracion"], 3), n(r["factor_maximo_posible"], 3)))
            print("  Recuperacion del activo : %s %%" % n(r["recuperacion_pct"], 2))
            print("  Comprobacion (2a via)   : rendimiento x factor = %s %%"
                  % n((r["rendimiento_pct"] / Decimal(100)) * r["factor_concentracion"] * Decimal(100), 2))
            if r["recuperacion_pct"] > Decimal("100"):
                print("")
                print("  BANDERA ROJA: recuperacion mayor al 100 %. Eso es fisicamente imposible: no puede")
                print("  salir mas activo del que entro. Causas tipicas: los dos %% estan en bases distintas,")
                print("  el extracto trae otro material, o alguno de los dos COA esta inflado.")
            elif r["recuperacion_pct"] < Decimal("50"):
                print("")
                print("  ATENCION: se esta quedando mas de la mitad del %s en el bagazo. El extracto puede")
                print("  ser 'muy concentrado' y aun asi ser un mal proceso." % args.marcador)
            print("")
            print("  Recordatorio: el ratio es de MASA, no de potencia. Un 10:1 no dice nada del activo")
            print("  hasta que mides el marcador, que es exactamente lo que acabas de hacer.")
        else:
            print("")
            print("  Para saber si el extracto sirve, agrega --activo-biomasa y --activo-extracto:")
            print("  el ratio de masa no dice nada sobre cuanto principio activo quedo.")
        return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))