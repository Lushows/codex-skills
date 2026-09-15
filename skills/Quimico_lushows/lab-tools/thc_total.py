#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
thc_total.py — THC total y evaluacion de cumplimiento (concentracion y miligramos por envase).

QUE CALCULA
  1) THC total = delta-9-THC + (THCA x 0,877). Acepta la entrada en % p/p o en mg/g.
  2) Convierte entre base humeda y base seca usando la humedad del COA.
  3) Evalua cumplimiento contra DOS limites distintos, que son cosas diferentes:
       a) LIMITE DE CONCENTRACION: 0,3 % p/p de THC total en BASE SECA (definicion de hemp/canamo
          en EE.UU.). Aplica sobre el material vegetal.
       b) LIMITE POR ENVASE: 0,4 mg de THC total POR ENVASE (contenedor de producto terminado).
          Aplica sobre el producto que compra el consumidor, no sobre la planta.
  4) Modo inverso: cual es la concentracion maxima que puede tener un producto para no pasarse
     de los mg por envase, dado el tamanio del envase.

FORMULAS
  THC_total (% p/p)  = THC + THCA * 0,877
  mg/g               = % p/p * 10
  base seca          = base humeda / (1 - humedad/100)
  base humeda        = base seca * (1 - humedad/100)
  mg por envase      = (mg/g tal cual) * (gramos de producto en el envase)
  concentracion max  = limite_mg_envase / gramos_envase   [mg/g]

DE DONDE SALEN LOS LIMITES (FECHADOS A AGOSTO DE 2026 — VERIFICA VIGENCIA)
  - 0,3 % p/p de THC total en base seca: definicion federal de hemp en EE.UU. (Agricultural Improvement
    Act de 2018 y regla final de la USDA), que ademas define "THC total" exactamente como
    delta-9-THC + 0,877 x THCA. Colombia y la UE manejan sus propios umbrales y su propia definicion:
    NO asumas que el 0,3 % aplica en tu pais.
  - 0,4 mg de THC total por envase: umbral por CONTENEDOR discutido/adoptado en la normativa federal
    de EE.UU. para productos de hemp de consumo. A agosto de 2026 este limite y su fecha de entrada
    en vigor han cambiado varias veces.
  ==> AMBOS limites son configurables (--limite-pct, --limite-mg-envase) precisamente porque cambian.
      ANTES DE TOMAR UNA DECISION COMERCIAL, verifica el texto vigente con tu abogado regulatorio y
      con la autoridad del pais de destino. Este script no es asesoria legal.

QUE **NO** HACE
  - No decide la legalidad de tu producto en Colombia, la UE ni ningun otro pais.
  - No convierte delta-8-THC, THCP, HHC ni otros isomeros/analogos: solo delta-9-THC y THCA.
    Varias normas cuentan "THC total" incluyendo otros isomeros. Revisa la definicion aplicable.
  - No mide nada: consume el resultado de un COA. Si el COA no dice metodo, base y limite de
    cuantificacion, el numero no sirve para sostener cumplimiento.
  - No estima incertidumbre de medida: un valor de 0,29 % con incertidumbre +/- 0,03 % NO esta
    limpiamente por debajo de 0,3 %.
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP

getcontext().prec = 34

FACTOR_THCA = Decimal("0.877")
LIMITE_PCT_DEFECTO = Decimal("0.3")          # % p/p THC total, base seca
LIMITE_MG_ENVASE_DEFECTO = Decimal("0.4")    # mg THC total por envase
FECHA_LIMITES = "agosto de 2026"


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

def a_porcentaje(valor, unidad):
    """Normaliza a % p/p. Unidades aceptadas: pct (% p/p) y mg/g."""
    exigir(valor >= 0, "Las concentraciones no pueden ser negativas.")
    if unidad == "pct":
        exigir(valor <= 100, "Un porcentaje p/p no puede superar 100 %.")
        return valor
    if unidad == "mg/g":
        exigir(valor <= 1000, "mg/g no puede superar 1000 (= 100 % p/p).")
        return valor / Decimal(10)
    raise ErrorDeEntrada("Unidad no reconocida: %s" % unidad)


def thc_total_pct(thc_pct, thca_pct, factor=FACTOR_THCA):
    exigir(thc_pct >= 0 and thca_pct >= 0, "Las concentraciones no pueden ser negativas.")
    exigir(thc_pct + thca_pct <= 100, "delta-9-THC + THCA no puede superar 100 % p/p.")
    return thc_pct + (thca_pct * factor)


def valida_humedad(h):
    exigir(h is None or (Decimal(0) <= h < Decimal(100)),
           "La humedad debe estar entre 0 y 100 % (100 % es imposible: seria todo agua).")
    return h


def humeda_a_seca(valor, humedad_pct):
    valida_humedad(humedad_pct)
    return valor / (Decimal(1) - humedad_pct / Decimal(100))


def seca_a_humeda(valor, humedad_pct):
    valida_humedad(humedad_pct)
    return valor * (Decimal(1) - humedad_pct / Decimal(100))


def mg_por_envase(pct_tal_cual, gramos_envase):
    exigir(gramos_envase > 0, "El tamanio del envase (--envase-g) debe ser mayor que cero.")
    return pct_tal_cual * Decimal(10) * gramos_envase   # (mg/g) * g = mg


def concentracion_maxima(gramos_envase, limite_mg=LIMITE_MG_ENVASE_DEFECTO):
    exigir(gramos_envase > 0, "El tamanio del envase (--envase-g) debe ser mayor que cero.")
    exigir(limite_mg > 0, "El limite por envase debe ser mayor que cero.")
    mg_por_g = limite_mg / gramos_envase
    return {"mg_g": mg_por_g, "pct": mg_por_g / Decimal(10)}


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
            print("  ok  %-54s %s" % (nombre, o))

    def cierto(self, nombre, condicion, detalle=""):
        self.n += 1
        if condicion:
            print("  ok  %-54s %s" % (nombre, "cumple"))
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
        print("OK - %d pruebas pasaron (thc_total.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST thc_total.py")

    # 1. Caso de libro: 20 % THCA + 1 % THC
    total = thc_total_pct(Decimal("1"), Decimal("20"))
    t.cerca("THC total de 1 % THC + 20 % THCA [% p/p]", total, "18.54", "1e-12")

    # 2. Misma cuenta entrando en mg/g -> tiene que dar lo mismo (segunda via)
    thc2 = a_porcentaje(Decimal("10"), "mg/g")
    thca2 = a_porcentaje(Decimal("200"), "mg/g")
    t.cerca("mismo caso entrando en mg/g [% p/p]", thc_total_pct(thc2, thca2), total, "1e-12")
    t.cerca("expresado de vuelta en mg/g", total * 10, "185.4", "1e-12")

    # 3. Base humeda -> base seca (inversa incluida)
    seca = humeda_a_seca(Decimal("0.276"), Decimal("8"))
    t.cerca("0,276 % base humeda con 8 % humedad -> base seca", seca, "0.3", "1e-12")
    t.cerca("inversa: base seca -> base humeda", seca_a_humeda(seca, Decimal("8")), "0.276", "1e-12")

    # 4. Cumplimiento de concentracion (limite 0,3 % base seca)
    t.cierto("0,34 % THCA (sin THC) CUMPLE 0,3 % base seca",
             thc_total_pct(Decimal("0"), Decimal("0.34")) <= LIMITE_PCT_DEFECTO,
             "total = %s" % thc_total_pct(Decimal("0"), Decimal("0.34")))
    t.cierto("0,35 % THCA (sin THC) NO cumple 0,3 % base seca",
             thc_total_pct(Decimal("0"), Decimal("0.35")) > LIMITE_PCT_DEFECTO,
             "total = %s" % thc_total_pct(Decimal("0"), Decimal("0.35")))

    # 5. Miligramos por envase
    mg = mg_por_envase(Decimal("0.004"), Decimal("10"))
    t.cerca("0,004 % p/p en envase de 10 g [mg THC total]", mg, "0.4", "1e-12")
    t.cierto("ese envase queda JUSTO en el limite (no lo supera)", mg <= LIMITE_MG_ENVASE_DEFECTO, "mg=%s" % mg)
    t.cierto("un envase de 30 g a la misma concentracion SI se pasa",
             mg_por_envase(Decimal("0.004"), Decimal("30")) > LIMITE_MG_ENVASE_DEFECTO, "no se pasa")

    # 6. VERIFICACION POR SEGUNDA VIA: el modo inverso reproduce la concentracion
    inv = concentracion_maxima(Decimal("10"), LIMITE_MG_ENVASE_DEFECTO)
    t.cerca("inversa: concentracion max para 0,4 mg en 10 g [% p/p]", inv["pct"], "0.004", "1e-12")
    t.cerca("inversa: la misma en mg/g", inv["mg_g"], "0.04", "1e-12")
    t.cerca("ida y vuelta envase: mg(conc_max) = limite",
            mg_por_envase(inv["pct"], Decimal("10")), LIMITE_MG_ENVASE_DEFECTO, "1e-12")

    # 7. Caso real que sorprende: flor legal por concentracion pero ilegal por envase
    flor = thc_total_pct(Decimal("0.05"), Decimal("0.28"))          # 0,29556 % p/p base seca
    t.cierto("flor de 0,2956 % CUMPLE el limite de concentracion", flor <= LIMITE_PCT_DEFECTO, "total=%s" % flor)
    t.cierto("...y sin embargo un envase de 3,5 g de esa flor supera 0,4 mg",
             mg_por_envase(flor, Decimal("3.5")) > LIMITE_MG_ENVASE_DEFECTO,
             "mg = %s" % mg_por_envase(flor, Decimal("3.5")))

    # 8. Validaciones de entrada
    for descripcion, fn in [
        ("rechaza concentracion negativa", lambda: thc_total_pct(Decimal("-1"), Decimal("0"))),
        ("rechaza porcentaje > 100", lambda: a_porcentaje(Decimal("120"), "pct")),
        ("rechaza mg/g > 1000", lambda: a_porcentaje(Decimal("1200"), "mg/g")),
        ("rechaza humedad de 100 %", lambda: humeda_a_seca(Decimal("1"), Decimal("100"))),
        ("rechaza humedad negativa", lambda: humeda_a_seca(Decimal("1"), Decimal("-2"))),
        ("rechaza envase de 0 g", lambda: mg_por_envase(Decimal("0.1"), Decimal("0"))),
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
        prog="thc_total.py",
        description="THC total = delta-9-THC + (THCA x 0,877), con cumplimiento por concentracion y por envase.",
        epilog="LIMITES FECHADOS A %s. Verifica la norma vigente antes de decidir nada comercial." % FECHA_LIMITES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    sub = p.add_subparsers(dest="modo")

    e = sub.add_parser("evaluar", help="calcula THC total y evalua los dos limites")
    e.add_argument("--thc", type=dec, default=Decimal("0"), help="delta-9-THC (def. 0)")
    e.add_argument("--thca", type=dec, default=Decimal("0"), help="THCA (def. 0)")
    e.add_argument("--unidad", choices=["pct", "mg/g"], required=True,
                   help="unidad de --thc y --thca: pct (%% p/p) o mg/g")
    e.add_argument("--base", choices=["seca", "humeda"], required=True,
                   help="base del dato del COA (obligatorio declararla)")
    e.add_argument("--humedad", type=dec, default=None,
                   help="humedad en %% p/p; necesaria para pasar de una base a la otra")
    e.add_argument("--envase-g", type=dec, default=None, dest="envase_g",
                   help="gramos de producto por envase; activa la evaluacion de mg por envase")
    e.add_argument("--limite-pct", type=dec, default=LIMITE_PCT_DEFECTO, dest="limite_pct",
                   help="limite de concentracion en %% p/p base seca (def. 0,3)")
    e.add_argument("--limite-mg-envase", type=dec, default=LIMITE_MG_ENVASE_DEFECTO, dest="limite_mg",
                   help="limite de mg de THC total por envase (def. 0,4)")

    m = sub.add_parser("max-concentracion",
                       help="inverso: concentracion maxima para no pasar el limite por envase")
    m.add_argument("--envase-g", type=dec, required=True, dest="envase_g", help="gramos por envase")
    m.add_argument("--limite-mg-envase", type=dec, default=LIMITE_MG_ENVASE_DEFECTO, dest="limite_mg",
                   help="limite de mg por envase (def. 0,4)")
    return p


def _veredicto(valor, limite):
    return "CUMPLE" if valor <= limite else "NO CUMPLE"


def main(argv):
    if "--test" in argv:
        return autotest()
    p = construir_parser()
    args = p.parse_args(argv)
    if not args.modo:
        p.print_help()
        return 0
    try:
        if args.modo == "max-concentracion":
            r = concentracion_maxima(args.envase_g, args.limite_mg)
            print("CONCENTRACION MAXIMA POR ENVASE (modo inverso)")
            print("  Envase                 : %s g de producto" % n(args.envase_g, 3))
            print("  Limite por envase      : %s mg de THC total" % n(args.limite_mg, 3))
            print("  Concentracion maxima   : %s mg/g = %s %% p/p (BASE TAL CUAL, no base seca)"
                  % (n(r["mg_g"], 6), n(r["pct"], 6)))
            print("")
            print("  Limite fechado a %s. VERIFICA VIGENCIA antes de formular." % FECHA_LIMITES)
            return 0

        thc = a_porcentaje(args.thc, args.unidad)
        thca = a_porcentaje(args.thca, args.unidad)
        valida_humedad(args.humedad)
        total = thc_total_pct(thc, thca)

        print("THC TOTAL Y CUMPLIMIENTO")
        print("  Entrada: delta-9-THC %s %% p/p | THCA %s %% p/p | BASE DECLARADA: %s"
              % (n(thc), n(thca), args.base.upper()))
        print("  Formula: THC total = delta-9-THC + (THCA x %s)" % FACTOR_THCA)
        print("")
        print("  THC total en base %-7s: %s %% p/p  = %s mg/g" % (args.base, n(total), n(total * 10)))

        total_seca = None
        total_tal_cual = None
        if args.base == "seca":
            total_seca = total
            if args.humedad is not None:
                total_tal_cual = seca_a_humeda(total, args.humedad)
                print("  THC total tal cual (%s %% humedad): %s %% p/p = %s mg/g"
                      % (n(args.humedad, 2), n(total_tal_cual), n(total_tal_cual * 10)))
        else:
            total_tal_cual = total
            if args.humedad is not None:
                total_seca = humeda_a_seca(total, args.humedad)
                print("  THC total en base SECA (%s %% humedad): %s %% p/p = %s mg/g"
                      % (n(args.humedad, 2), n(total_seca), n(total_seca * 10)))

        print("")
        print("  --- LIMITE DE CONCENTRACION: %s %% p/p BASE SECA ---" % n(args.limite_pct, 3))
        if total_seca is None:
            print("  NO EVALUABLE: diste base humeda y no diste --humedad. Sin la humedad no hay base seca,")
            print("  y este limite SOLO se evalua en base seca. Pidele la humedad al laboratorio.")
        else:
            print("  Valor evaluado: %s %% p/p base seca  ->  %s" % (n(total_seca), _veredicto(total_seca, args.limite_pct)))
            margen = args.limite_pct - total_seca
            print("  Margen al limite: %s puntos porcentuales" % n(margen))
            if abs(margen) < Decimal("0.03"):
                print("  ATENCION: estas dentro de la incertidumbre tipica del metodo. Un resultado a")
                print("  0,03 puntos del limite no es una defensa: pide la incertidumbre expandida del lab.")

        print("")
        print("  --- LIMITE POR ENVASE: %s mg de THC total por envase ---" % n(args.limite_mg, 3))
        if args.envase_g is None:
            print("  NO EVALUADO: falta --envase-g (gramos de producto por envase).")
        else:
            base_para_envase = total_tal_cual if total_tal_cual is not None else total_seca
            conservador = total_tal_cual is None
            mg = mg_por_envase(base_para_envase, args.envase_g)
            print("  Envase: %s g  ->  %s mg de THC total por envase  ->  %s"
                  % (n(args.envase_g, 3), n(mg, 4), _veredicto(mg, args.limite_mg)))
            if conservador:
                print("  (Calculado con el valor en base SECA por falta de --humedad: es el peor caso,")
                print("   el producto tal cual tendra un poco menos. Sirve para descartar, no para aprobar.)")
            r = concentracion_maxima(args.envase_g, args.limite_mg)
            print("  Para cumplir, la concentracion tal cual no puede pasar de %s %% p/p (%s mg/g)"
                  % (n(r["pct"], 6), n(r["mg_g"], 6)))

        print("")
        print("  LIMITES FECHADOS A %s. La regulacion de THC total cambia seguido y NO es la misma" % FECHA_LIMITES)
        print("  en Colombia, EE.UU. y la UE. Verifica el texto vigente del pais de destino.")
        print("  Este script no es asesoria legal y no cubre delta-8, HHC, THCP ni otros analogos.")
        return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))