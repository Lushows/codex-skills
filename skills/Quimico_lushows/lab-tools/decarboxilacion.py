#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decarboxilacion.py — THCA -> delta-9-THC: factor de masa molar y cinetica de descarboxilacion.

QUE CALCULA
  1) El factor de conversion por masa molar THCA -> delta-9-THC (el famoso 0,877) y de donde sale.
  2) Cuanto delta-9-THC se obtiene al descarboxilar una cantidad de THCA, cerrando el balance de masa
     (se pierde CO2, asi que la masa del material BAJA y los % suben si se refieren a la masa final).
  3) La conversion esperada por tiempo y temperatura con un modelo cinetico de PRIMER ORDEN (Arrhenius).
  4) El tiempo necesario para llegar a una conversion objetivo a una temperatura dada.

FORMULAS
  Factor de masa molar:
      f = MM(delta-9-THC) / MM(THCA) = 314,469 / 358,478 = 0,8772...  -> se usa 0,877
      MM se calcula aqui mismo desde las formulas moleculares:
          delta-9-THC = C21 H30 O2      THCA = C22 H30 O4
      con pesos atomicos estandar IUPAC (C 12,011  H 1,008  O 15,999).
      La diferencia THCA - THC es exactamente C O2 (44,009 g/mol): el CO2 que se pierde.

  Descarboxilacion (masa):
      THC_generado = THCA_convertido * 0,877
      CO2_perdido  = THCA_convertido * (1 - 0,877) = THCA_convertido * 0,123

  Cinetica de primer orden (Arrhenius):
      k(T) = A * exp(-Ea / (R * T))          T en KELVIN, k en min^-1
      alfa(t) = 1 - exp(-k * t)              alfa = fraccion de THCA convertida
      t(alfa) = -ln(1 - alfa) / k

DE DONDE SALEN LOS NUMEROS
  - El factor 0,877 es aritmetica de masas molares. No es opinion ni convencion: es estequiometria.
    Es el mismo factor que usan la USDA (regla final del hemp) y los laboratorios de potencia.
  - Los parametros cineticos por DEFECTO (Ea = 86,5 kJ/mol; A = 1,9e10 min^-1) son una APROXIMACION
    de orden de magnitud construida a partir de los estudios de descarboxilacion de acidos cannabinoides
    publicados (linea Perrotin-Brunel et al., 2011; Wang et al., Cannabis Cannabinoid Res. 2016), que
    reportan cinetica de primer orden con energias de activacion del orden de 80-100 kJ/mol.
    NO son un dato de tu material. La matriz (flor, extracto, aceite), el espesor de capa, la
    transferencia de calor de tu horno y la humedad cambian el resultado. Usa --ea y --a para meter
    tus propios parametros, o calibralos midiendo por HPLC a 3 tiempos.

QUE **NO** HACE
  - No modela la degradacion posterior de delta-9-THC a CBN (a tiempos/temperaturas altas SI ocurre y
    hace que la potencia baje despues del maximo). Este script solo modela THCA -> THC.
  - No modela la evaporacion de terpenos ni la perdida de agua.
  - No sustituye una medicion por HPLC. La cinetica es una GUIA para diseniar el experimento, no un COA.
  - No decide cumplimiento regulatorio: eso es thc_total.py.
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP

getcontext().prec = 34

R_GAS = Decimal("8.314462618")          # J / (mol K)
EA_DEFECTO = Decimal("86500")           # J/mol  (APROXIMACION de literatura)
A_DEFECTO = Decimal("1.9E10")           # min^-1 (APROXIMACION de literatura)

PESOS_ATOMICOS = {
    "C": Decimal("12.011"),
    "H": Decimal("1.008"),
    "O": Decimal("15.999"),
}


class ErrorDeEntrada(Exception):
    pass


def dec(texto):
    """Convierte texto a Decimal aceptando coma o punto decimal."""
    try:
        return Decimal(str(texto).strip().replace(" ", "").replace(",", "."))
    except (InvalidOperation, ValueError):
        raise argparse.ArgumentTypeError("'%s' no es un numero valido" % texto)


def exigir(condicion, mensaje):
    if not condicion:
        raise ErrorDeEntrada(mensaje)


def n(x, d=4):
    return str(Decimal(x).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP))


def masa_molar(c, h, o):
    return (PESOS_ATOMICOS["C"] * c) + (PESOS_ATOMICOS["H"] * h) + (PESOS_ATOMICOS["O"] * o)


MM_THC = masa_molar(21, 30, 2)      # 314,469 g/mol
MM_THCA = masa_molar(22, 30, 4)     # 358,478 g/mol
MM_CO2 = masa_molar(1, 0, 2)        # 44,009 g/mol
FACTOR_EXACTO = MM_THC / MM_THCA
FACTOR = Decimal("0.877")           # el que se usa en regulacion y en el laboratorio


# ----------------------------------------------------------------------------- calculo

def k_arrhenius(temp_c, ea=EA_DEFECTO, a=A_DEFECTO):
    """k en min^-1 a partir de temperatura en grados Celsius."""
    exigir(temp_c > Decimal("-273.15"), "La temperatura no puede estar por debajo del cero absoluto.")
    t_kelvin = temp_c + Decimal("273.15")
    exigir(t_kelvin > 0, "Temperatura absoluta invalida.")
    exigir(ea > 0, "La energia de activacion (--ea) debe ser mayor que cero.")
    exigir(a > 0, "El factor pre-exponencial (--a) debe ser mayor que cero.")
    return a * (-ea / (R_GAS * t_kelvin)).exp()


def conversion(k, minutos):
    exigir(minutos >= 0, "El tiempo no puede ser negativo.")
    return Decimal(1) - (-k * minutos).exp()


def tiempo_para(k, alfa):
    exigir(Decimal(0) < alfa < Decimal(1), "La conversion objetivo debe estar entre 0 y 1 (excluidos).")
    return -((Decimal(1) - alfa).ln()) / k


def balance_descarboxilacion(thca_pct, thc_pct, alfa, factor=FACTOR):
    """
    Todo en % p/p referido a la masa INICIAL del material.
    Devuelve un diccionario con el balance completo, incluyendo la correccion por perdida de CO2.
    """
    exigir(thca_pct >= 0 and thc_pct >= 0, "Los porcentajes no pueden ser negativos.")
    exigir(thca_pct + thc_pct <= 100, "THCA + THC no puede superar 100 % p/p.")
    exigir(0 <= alfa <= 1, "La conversion debe estar entre 0 y 1.")

    thca_convertido = thca_pct * alfa
    thca_remanente = thca_pct - thca_convertido
    thc_generado = thca_convertido * factor
    co2 = thca_convertido * (Decimal(1) - factor)
    thc_final = thc_pct + thc_generado

    masa_final_pct = Decimal(100) - co2                       # por 100 g iniciales
    exigir(masa_final_pct > 0, "Balance de masa imposible: se perderia toda la masa.")

    return {
        "thca_convertido": thca_convertido,
        "thca_remanente_ini": thca_remanente,
        "thc_generado": thc_generado,
        "co2_perdido": co2,
        "thc_final_base_inicial": thc_final,
        "masa_final_pct": masa_final_pct,
        "thc_final_base_final": thc_final * Decimal(100) / masa_final_pct,
        "thca_remanente_base_final": thca_remanente * Decimal(100) / masa_final_pct,
    }


# ----------------------------------------------------------------------------- salida

def imprimir_factor():
    print("FACTOR DE CONVERSION THCA -> delta-9-THC")
    print("  MM delta-9-THC (C21H30O2) : %s g/mol" % n(MM_THC, 3))
    print("  MM THCA        (C22H30O4) : %s g/mol" % n(MM_THCA, 3))
    print("  MM CO2         (CO2)      : %s g/mol   (diferencia THCA - THC)" % n(MM_CO2, 3))
    print("  factor exacto  = %s" % n(FACTOR_EXACTO, 6))
    print("  factor de uso  = %s  (el que exige la regulacion y usa el laboratorio)" % FACTOR)
    print("  comprobacion   : MM(THC) + MM(CO2) = %s g/mol = MM(THCA)" % n(MM_THC + MM_CO2, 3))
    print("  Pesos atomicos estandar IUPAC: C 12,011  H 1,008  O 15,999.")


def imprimir_balance(b, thca_pct, thc_pct, base, alfa, encabezado):
    print(encabezado)
    print("  BASE DECLARADA: %s" % base.upper())
    print("  Entrada  : THCA %s %% p/p  |  delta-9-THC %s %% p/p" % (n(thca_pct), n(thc_pct)))
    print("  Conversion aplicada: %s %% del THCA" % n(alfa * 100, 2))
    print("")
    print("  --- referido a la MASA INICIAL (100 g de material de partida) ---")
    print("  THCA convertido            : %s g  (= %s %% p/p)" % (n(b["thca_convertido"]), n(b["thca_convertido"])))
    print("  THCA remanente             : %s %% p/p" % n(b["thca_remanente_ini"]))
    print("  delta-9-THC generado       : %s %% p/p" % n(b["thc_generado"]))
    print("  delta-9-THC total          : %s %% p/p" % n(b["thc_final_base_inicial"]))
    print("  CO2 perdido                : %s g por 100 g  (masa que SE VA del material)" % n(b["co2_perdido"]))
    print("")
    print("  --- referido a la MASA FINAL (lo que queda despues de descarboxilar) ---")
    print("  Masa final                 : %s g por cada 100 g iniciales" % n(b["masa_final_pct"]))
    print("  delta-9-THC                : %s %% p/p  <- este es el que vera el laboratorio" % n(b["thc_final_base_final"]))
    print("  THCA remanente             : %s %% p/p" % n(b["thca_remanente_base_final"]))
    print("")
    print("  Nota: la base (%s) no la cambia este script; se reporta tal como la declaraste." % base)
    print("  Nota: no se modela la perdida de delta-9-THC hacia CBN por sobrecoccion.")


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
            print("  ok  %-52s %s" % (nombre, o))

    def cierto(self, nombre, condicion, detalle=""):
        self.n += 1
        if condicion:
            print("  ok  %-52s %s" % (nombre, "cumple"))
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
        print("OK - %d pruebas pasaron (decarboxilacion.py)" % self.n)
        return 0


def autotest():
    t = _T()
    print("AUTOTEST decarboxilacion.py")

    # 1. El factor sale de las masas molares y redondea a 0,877
    t.cerca("MM delta-9-THC (C21H30O2) g/mol", MM_THC, "314.469", "1e-3")
    t.cerca("MM THCA (C22H30O4) g/mol", MM_THCA, "358.478", "1e-3")
    t.cerca("factor exacto MM(THC)/MM(THCA)", FACTOR_EXACTO, "0.8772337", "1e-6")
    t.cerca("factor redondeado a 3 decimales", FACTOR_EXACTO.quantize(Decimal("0.001")), "0.877")

    # 2. VERIFICACION POR SEGUNDA VIA: la diferencia de masas molares tiene que ser exactamente CO2
    t.cerca("MM(THCA) - MM(THC) = MM(CO2)", MM_THCA - MM_THC, MM_CO2, "1e-12")

    # 3. Descarboxilacion total de 20 % THCA
    b = balance_descarboxilacion(Decimal("20"), Decimal("0"), Decimal("1"))
    t.cerca("THC generado desde 20 % THCA (100 % conv)", b["thc_generado"], "17.54", "1e-12")
    t.cerca("CO2 perdido por 100 g", b["co2_perdido"], "2.46", "1e-12")
    t.cerca("masa final por 100 g iniciales", b["masa_final_pct"], "97.54", "1e-12")
    # segunda via: balance de masa cerrado
    t.cerca("balance: THC + CO2 = THCA convertido",
            b["thc_generado"] + b["co2_perdido"], b["thca_convertido"], "1e-12")
    # segunda via: el % sobre masa final reconstruye la misma masa absoluta de THC
    masa_thc = b["thc_final_base_final"] * b["masa_final_pct"] / Decimal(100)
    t.cerca("masa absoluta de THC coincide en ambas bases", masa_thc, b["thc_final_base_inicial"], "1e-12")

    # 4. Conversion parcial + operacion inversa
    b2 = balance_descarboxilacion(Decimal("18"), Decimal("1.2"), Decimal("0.75"))
    t.cerca("THCA remanente (18 %, 75 % conv)", b2["thca_remanente_ini"], "4.5", "1e-12")
    t.cerca("THC total base inicial", b2["thc_final_base_inicial"], "13.0395", "1e-12")
    # inversa: desde el THC generado recupero el THCA convertido
    t.cerca("inversa THC_generado/0,877 = THCA convertido",
            b2["thc_generado"] / FACTOR, b2["thca_convertido"], "1e-12")

    # 5. Cinetica: ida y vuelta k -> alfa -> t
    k110 = k_arrhenius(Decimal("110"))
    a30 = conversion(k110, Decimal("30"))
    t_vuelta = tiempo_para(k110, a30)
    t.cerca("inversa cinetica: t(alfa(30 min)) = 30 min", t_vuelta, "30", "1e-9")
    t.cierto("k(110 C) en rango razonable (1e-3 a 1 min^-1)",
             Decimal("0.001") < k110 < Decimal("1"), "k=%s" % k110)
    t.cierto("conversion a 110 C crece con el tiempo",
             conversion(k110, Decimal("10")) < conversion(k110, Decimal("60")), "no crece")
    t.cierto("mayor temperatura -> mayor k",
             k_arrhenius(Decimal("130")) > k110, "k(130) <= k(110)")

    # 6. VERIFICACION POR SEGUNDA VIA: recuperar Ea desde dos constantes (Arrhenius de dos puntos)
    k1 = k_arrhenius(Decimal("100"))
    k2 = k_arrhenius(Decimal("140"))
    t1 = Decimal("100") + Decimal("273.15")
    t2 = Decimal("140") + Decimal("273.15")
    ea_recuperada = R_GAS * (k2 / k1).ln() / ((Decimal(1) / t1) - (Decimal(1) / t2))
    t.cerca("Ea recuperada desde k(100 C) y k(140 C) [J/mol]", ea_recuperada, EA_DEFECTO, "1e-6")

    # 7. Validaciones de entrada
    for descripcion, fn in [
        ("rechaza THCA negativo", lambda: balance_descarboxilacion(Decimal("-1"), Decimal("0"), Decimal("1"))),
        ("rechaza THCA+THC > 100 %", lambda: balance_descarboxilacion(Decimal("80"), Decimal("30"), Decimal("1"))),
        ("rechaza conversion > 1", lambda: balance_descarboxilacion(Decimal("10"), Decimal("0"), Decimal("1.5"))),
        ("rechaza T bajo cero absoluto", lambda: k_arrhenius(Decimal("-300"))),
        ("rechaza tiempo negativo", lambda: conversion(Decimal("0.01"), Decimal("-5"))),
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
        prog="decarboxilacion.py",
        description="THCA -> delta-9-THC: factor 0,877 (masa molar) y cinetica de descarboxilacion.",
        epilog="Todos los resultados se imprimen con unidad y con la base declarada. "
               "Los parametros cineticos por defecto son una APROXIMACION de literatura: calibralos.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    sub = p.add_subparsers(dest="modo")

    sub.add_parser("factor", help="muestra las masas molares y de donde sale el 0,877")

    c = sub.add_parser("convertir", help="descarboxilacion con una conversion que tu declaras")
    c.add_argument("--thca", type=dec, required=True, help="THCA en %% p/p")
    c.add_argument("--thc", type=dec, default=Decimal("0"), help="delta-9-THC ya presente en %% p/p (def. 0)")
    c.add_argument("--conversion", type=dec, default=Decimal("100"),
                   help="%% del THCA que se convierte (def. 100)")
    c.add_argument("--base", choices=["seca", "humeda"], required=True,
                   help="base del dato de entrada (obligatorio declararla)")

    k = sub.add_parser("cinetica", help="conversion esperada por tiempo y temperatura")
    k.add_argument("--thca", type=dec, required=True, help="THCA en %% p/p")
    k.add_argument("--thc", type=dec, default=Decimal("0"), help="delta-9-THC ya presente en %% p/p")
    k.add_argument("--temp", type=dec, required=True, help="temperatura en grados Celsius")
    k.add_argument("--min", type=dec, required=True, dest="minutos", help="tiempo en minutos")
    k.add_argument("--base", choices=["seca", "humeda"], required=True, help="base del dato de entrada")
    k.add_argument("--ea", type=dec, default=EA_DEFECTO, help="energia de activacion en J/mol")
    k.add_argument("--a", type=dec, default=A_DEFECTO, help="factor pre-exponencial en min^-1")

    tt = sub.add_parser("tiempo", help="cuanto tiempo hace falta para llegar a una conversion objetivo")
    tt.add_argument("--temp", type=dec, required=True, help="temperatura en grados Celsius")
    tt.add_argument("--objetivo", type=dec, default=Decimal("95"),
                    help="conversion objetivo en %% (def. 95)")
    tt.add_argument("--ea", type=dec, default=EA_DEFECTO, help="energia de activacion en J/mol")
    tt.add_argument("--a", type=dec, default=A_DEFECTO, help="factor pre-exponencial en min^-1")
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
        if args.modo == "factor":
            imprimir_factor()
            return 0

        if args.modo == "convertir":
            exigir(0 <= args.conversion <= 100, "--conversion debe estar entre 0 y 100 %.")
            alfa = args.conversion / Decimal(100)
            b = balance_descarboxilacion(args.thca, args.thc, alfa)
            imprimir_balance(b, args.thca, args.thc, args.base, alfa,
                             "DESCARBOXILACION (conversion declarada por el usuario)")
            return 0

        if args.modo == "cinetica":
            k = k_arrhenius(args.temp, args.ea, args.a)
            alfa = conversion(k, args.minutos)
            b = balance_descarboxilacion(args.thca, args.thc, alfa)
            print("CINETICA DE DESCARBOXILACION (primer orden, Arrhenius)")
            print("  Temperatura : %s C   Tiempo: %s min" % (n(args.temp, 1), n(args.minutos, 1)))
            print("  Ea          : %s J/mol   A: %s min^-1   (APROXIMACION de literatura)" % (n(args.ea, 0), args.a))
            print("  k(T)        : %s min^-1" % n(k, 6))
            print("  vida media  : %s min  (t para 50 %% de conversion)" % n(tiempo_para(k, Decimal("0.5")), 2))
            print("")
            imprimir_balance(b, args.thca, args.thc, args.base, alfa, "BALANCE RESULTANTE")
            print("")
            print("  ADVERTENCIA: modelo aproximado. Verifica con HPLC a por lo menos 3 tiempos.")
            return 0

        if args.modo == "tiempo":
            exigir(0 < args.objetivo < 100, "--objetivo debe estar entre 0 y 100 % (excluidos).")
            k = k_arrhenius(args.temp, args.ea, args.a)
            alfa = args.objetivo / Decimal(100)
            minutos = tiempo_para(k, alfa)
            print("TIEMPO NECESARIO PARA DESCARBOXILAR")
            print("  Temperatura       : %s C" % n(args.temp, 1))
            print("  Conversion objetivo: %s %% del THCA" % n(args.objetivo, 2))
            print("  k(T)              : %s min^-1" % n(k, 6))
            print("  Tiempo necesario  : %s min  (= %s horas)" % (n(minutos, 1), n(minutos / 60, 2)))
            print("  Vida media        : %s min" % n(tiempo_para(k, Decimal("0.5")), 2))
            print("")
            print("  ADVERTENCIA: parametros cineticos aproximados de literatura, no de tu material.")
            print("  El horno real tiene gradientes: mide, no confies en el numero.")
            return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))