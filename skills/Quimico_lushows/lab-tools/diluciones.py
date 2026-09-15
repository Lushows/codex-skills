#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diluciones.py — C1V1 = C2V2, series de dilucion y curva de calibracion con regresion lineal.

QUE CALCULA
  1) c1v1  : resuelve la incognita que falte en C1 x V1 = C2 x V2 (la ecuacion de dilucion).
  2) serie : una serie de diluciones (por ejemplo 1:2 seriada) con el volumen de stock y de diluyente
             que hay que pipetear en cada paso, y la concentracion resultante de cada nivel.
  3) curva : regresion lineal por minimos cuadrados de una curva de calibracion (concentracion vs area),
             con pendiente, intercepto, R^2, desviacion estandar residual, y la concentracion calculada
             a partir de un area de muestra (con su factor de dilucion aplicado).

FORMULAS
  Dilucion (conservacion de masa de soluto):
      C1 x V1 = C2 x V2          ->  V1 = C2 x V2 / C1 ,  C2 = C1 x V1 / V2 , etc.
      factor de dilucion FD = V2 / V1 = C1 / C2

  Serie de diluciones con factor f y volumen final V:
      V_stock  = V / f           V_diluyente = V - V_stock
      C_i      = C0 / f^i        (i = 1..n)

  Regresion lineal y = m x + b por minimos cuadrados ordinarios:
      m  = [n*Sxy - Sx*Sy] / [n*Sxx - Sx^2]
      b  = (Sy - m*Sx) / n
      R^2 = 1 - SSres/SStot ,  SSres = suma (y - y_pred)^2 ,  SStot = suma (y - media_y)^2
      s(y/x) = sqrt(SSres / (n-2))         desviacion estandar residual
      concentracion desde area:  x = (y - b) / m ,  y luego se multiplica por el factor de dilucion.

DE DONDE SALE
  C1V1=C2V2 es balance de masa de soluto. La regresion por minimos cuadrados y el uso de R^2 y de la
  desviacion residual en calibracion analitica siguen el marco de ICH Q2(R2) (linealidad y rango).
  Ojo: la ICH exige linealidad demostrada con al menos 5 niveles de concentracion.

QUE **NO** HACE
  - No hace regresion ponderada (weighted least squares) ni ajustes cuadraticos. En trazas, donde la
    varianza crece con la concentracion, la regresion sin peso SESGA el extremo bajo de la curva.
  - No corrige por estandar interno ni por efecto matriz.
  - R^2 alto NO demuestra exactitud: una curva con R^2 = 0,999 puede tener un intercepto que delata
    contaminacion o efecto matriz. Mira SIEMPRE los residuos y el intercepto, no solo el R^2.
  - No convierte unidades: entra y sale en la unidad que tu declares (--unidad-conc, --unidad-vol).
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

def resolver_c1v1(c1=None, v1=None, c2=None, v2=None):
    """Resuelve la unica incognita de C1*V1 = C2*V2. Devuelve (nombre, valor, dict completo)."""
    dados = {"c1": c1, "v1": v1, "c2": c2, "v2": v2}
    faltan = [k for k, v in dados.items() if v is None]
    exigir(len(faltan) == 1,
           "Debes dar exactamente 3 de los 4 valores (C1, V1, C2, V2). Faltan: %s" % ", ".join(faltan) if faltan
           else "Diste los 4 valores: quita uno, ese es el que se calcula.")
    for k, v in dados.items():
        if v is not None:
            exigir(v > 0, "%s debe ser mayor que cero." % k.upper())

    incognita = faltan[0]
    if incognita == "v1":
        dados["v1"] = c2 * v2 / c1
    elif incognita == "c1":
        dados["c1"] = c2 * v2 / v1
    elif incognita == "v2":
        dados["v2"] = c1 * v1 / c2
    else:
        dados["c2"] = c1 * v1 / v2

    exigir(dados["c1"] >= dados["c2"],
           "C1 (%s) es menor que C2 (%s): no puedes CONCENTRAR diluyendo. Revisa los datos."
           % (dados["c1"], dados["c2"]))
    exigir(dados["v2"] >= dados["v1"],
           "V2 (%s) es menor que V1 (%s): el volumen final no puede ser menor que el de stock."
           % (dados["v2"], dados["v1"]))
    dados["fd"] = dados["v2"] / dados["v1"]
    dados["diluyente"] = dados["v2"] - dados["v1"]
    return incognita, dados[incognita], dados


def serie_diluciones(c0, factor, niveles, volumen_final):
    exigir(c0 > 0, "La concentracion del stock debe ser mayor que cero.")
    exigir(factor > 1, "El factor de dilucion debe ser mayor que 1 (un factor de 1 no diluye nada).")
    exigir(niveles >= 1, "La serie necesita al menos 1 nivel.")
    exigir(niveles <= 30, "Mas de 30 niveles no tiene sentido practico (error acumulado enorme).")
    exigir(volumen_final > 0, "El volumen final de cada tubo debe ser mayor que cero.")
    v_stock = volumen_final / factor
    filas = []
    c = c0
    for i in range(1, int(niveles) + 1):
        c = c / factor
        filas.append({"nivel": i, "conc": c, "fd_acumulado": factor ** i,
                      "v_stock": v_stock, "v_diluyente": volumen_final - v_stock})
    return filas


def regresion(xs, ys):
    exigir(len(xs) == len(ys), "Hay %d concentraciones y %d areas: no coinciden." % (len(xs), len(ys)))
    m_n = len(xs)
    exigir(m_n >= 3, "Se necesitan al menos 3 puntos para una regresion util (ICH Q2 pide 5 niveles).")
    for x in xs:
        exigir(x >= 0, "Las concentraciones de los patrones no pueden ser negativas.")
    nn = Decimal(m_n)
    sx = sum(xs, Decimal(0))
    sy = sum(ys, Decimal(0))
    sxx = sum((x * x for x in xs), Decimal(0))
    sxy = sum((x * y for x, y in zip(xs, ys)), Decimal(0))
    denom = nn * sxx - sx * sx
    exigir(denom != 0, "Todas las concentraciones son iguales: no se puede ajustar una recta.")
    m = (nn * sxy - sx * sy) / denom
    b = (sy - m * sx) / nn
    media_y = sy / nn
    ss_res = sum(((y - (m * x + b)) ** 2 for x, y in zip(xs, ys)), Decimal(0))
    ss_tot = sum(((y - media_y) ** 2 for y in ys), Decimal(0))
    exigir(ss_tot != 0, "Todas las areas son iguales: no hay respuesta que modelar.")
    r2 = Decimal(1) - ss_res / ss_tot
    s_yx = (ss_res / (nn - Decimal(2))).sqrt() if m_n > 2 else Decimal(0)
    return {"n": m_n, "pendiente": m, "intercepto": b, "r2": r2, "ss_res": ss_res,
            "ss_tot": ss_tot, "s_yx": s_yx, "media_y": media_y}


def concentracion_desde_area(area, pendiente, intercepto, factor_dilucion=Decimal(1)):
    exigir(pendiente != 0, "La pendiente es cero: la curva no responde a la concentracion.")
    exigir(factor_dilucion > 0, "El factor de dilucion debe ser mayor que cero.")
    return ((area - intercepto) / pendiente) * factor_dilucion


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
        print("OK - %d pruebas pasaron (diluciones.py)" % self.n)
        return 0


def _regresion_float(xs, ys):
    """Segunda via INDEPENDIENTE en float, para contrastar la implementacion en Decimal."""
    try:
        import statistics
        if hasattr(statistics, "linear_regression"):
            r = statistics.linear_regression([float(x) for x in xs], [float(y) for y in ys])
            return r.slope, r.intercept
    except Exception:
        pass
    fx = [float(x) for x in xs]
    fy = [float(y) for y in ys]
    k = len(fx)
    sx, sy = sum(fx), sum(fy)
    sxx = sum(v * v for v in fx)
    sxy = sum(a * b for a, b in zip(fx, fy))
    m = (k * sxy - sx * sy) / (k * sxx - sx * sx)
    return m, (sy - m * sx) / k


def autotest():
    t = _T()
    print("AUTOTEST diluciones.py")

    # 1. C1V1: calcular el volumen de stock
    inc, val, d = resolver_c1v1(c1=Decimal("100"), c2=Decimal("10"), v2=Decimal("100"))
    t.cierto("c1v1 identifica la incognita (v1)", inc == "v1", "detecto %s" % inc)
    t.cerca("V1 para pasar de 100 a 10 ppm en 100 mL", val, "10", "1e-12")
    t.cerca("diluyente a agregar", d["diluyente"], "90", "1e-12")
    t.cerca("factor de dilucion", d["fd"], "10", "1e-12")
    # VERIFICACION POR SEGUNDA VIA: la masa de soluto se conserva
    t.cerca("balance de masa C1*V1 = C2*V2", d["c1"] * d["v1"], d["c2"] * d["v2"], "1e-12")
    # y la inversa: con V1 conocido recupero C2
    inc2, val2, _ = resolver_c1v1(c1=Decimal("100"), v1=Decimal("10"), v2=Decimal("100"))
    t.cierto("c1v1 inverso identifica c2", inc2 == "c2", "detecto %s" % inc2)
    t.cerca("inversa: C2 recuperado", val2, "10", "1e-12")

    # 2. Serie de diluciones 1:2, 5 niveles, 2 mL finales
    s = serie_diluciones(Decimal("1000"), Decimal("2"), 5, Decimal("2"))
    t.cerca("serie 1:2 nivel 1 [ppm]", s[0]["conc"], "500", "1e-12")
    t.cerca("serie 1:2 nivel 5 [ppm]", s[4]["conc"], "31.25", "1e-12")
    t.cerca("volumen de stock por tubo [mL]", s[0]["v_stock"], "1", "1e-12")
    t.cerca("volumen de diluyente por tubo [mL]", s[0]["v_diluyente"], "1", "1e-12")
    # segunda via: C0 / 2^5
    t.cerca("segunda via: C0 / 2^5", Decimal("1000") / (Decimal("2") ** 5), s[4]["conc"], "1e-12")

    # 3. Curva perfecta y = 3x + 2
    xs = [Decimal("1"), Decimal("2"), Decimal("5"), Decimal("10"), Decimal("20")]
    ys = [Decimal("5"), Decimal("8"), Decimal("17"), Decimal("32"), Decimal("62")]
    r = regresion(xs, ys)
    t.cerca("curva perfecta: pendiente", r["pendiente"], "3", "1e-12")
    t.cerca("curva perfecta: intercepto", r["intercepto"], "2", "1e-12")
    t.cerca("curva perfecta: R^2", r["r2"], "1", "1e-12")
    t.cerca("curva perfecta: s(y/x) residual", r["s_yx"], "0", "1e-12")
    # inversa: area 20 -> concentracion 6
    t.cerca("inversa: area 20 -> concentracion", concentracion_desde_area(Decimal("20"), r["pendiente"], r["intercepto"]), "6", "1e-12")
    # con factor de dilucion 10
    t.cerca("con factor de dilucion x10",
            concentracion_desde_area(Decimal("20"), r["pendiente"], r["intercepto"], Decimal("10")), "60", "1e-12")
    # cada patron devuelve su propia concentracion (ida y vuelta completa)
    ok = all(abs(concentracion_desde_area(y, r["pendiente"], r["intercepto"]) - x) < Decimal("1e-20")
             for x, y in zip(xs, ys))
    t.cierto("cada patron se recupera desde su area", ok, "algun patron no se recupera")

    # 4. Curva con ruido: contraste contra statistics.linear_regression (segunda via en float)
    xs2 = [Decimal("0.5"), Decimal("1"), Decimal("2"), Decimal("5"), Decimal("10")]
    ys2 = [Decimal("1230"), Decimal("2510"), Decimal("4980"), Decimal("12600"), Decimal("24900")]
    r2 = regresion(xs2, ys2)
    m_f, b_f = _regresion_float(xs2, ys2)
    t.cerca("curva con ruido: pendiente vs statistics", r2["pendiente"], Decimal(str(m_f)), "1e-6")
    t.cerca("curva con ruido: intercepto vs statistics", r2["intercepto"], Decimal(str(b_f)), "1e-6")
    t.cierto("R^2 entre 0,999 y 1", Decimal("0.999") < r2["r2"] <= Decimal("1"), "R2=%s" % r2["r2"])
    t.cierto("s(y/x) mayor que cero cuando hay ruido", r2["s_yx"] > 0, "s=%s" % r2["s_yx"])

    # 5. Validaciones
    for descripcion, fn in [
        ("rechaza dar los 4 valores", lambda: resolver_c1v1(Decimal("1"), Decimal("1"), Decimal("1"), Decimal("1"))),
        ("rechaza dar solo 2 valores", lambda: resolver_c1v1(c1=Decimal("1"), v1=Decimal("1"))),
        ("rechaza volumen negativo", lambda: resolver_c1v1(c1=Decimal("100"), c2=Decimal("10"), v2=Decimal("-5"))),
        ("rechaza 'diluir' para concentrar (C2 > C1)",
         lambda: resolver_c1v1(c1=Decimal("10"), c2=Decimal("50"), v2=Decimal("100"))),
        ("rechaza C1 = 0 (stock sin analito)",
         lambda: resolver_c1v1(c1=Decimal("0"), c2=Decimal("10"), v2=Decimal("100"))),
        ("rechaza factor de dilucion 1", lambda: serie_diluciones(Decimal("100"), Decimal("1"), 3, Decimal("2"))),
        ("rechaza serie de 0 niveles", lambda: serie_diluciones(Decimal("100"), Decimal("2"), 0, Decimal("2"))),
        ("rechaza curva con 2 puntos", lambda: regresion([Decimal("1"), Decimal("2")], [Decimal("1"), Decimal("2")])),
        ("rechaza curva con x todos iguales",
         lambda: regresion([Decimal("1")] * 4, [Decimal("1"), Decimal("2"), Decimal("3"), Decimal("4")])),
        ("rechaza concentracion de patron negativa",
         lambda: regresion([Decimal("-1"), Decimal("2"), Decimal("3")], [Decimal("1"), Decimal("2"), Decimal("3")])),
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
        prog="diluciones.py",
        description="C1V1=C2V2, series de dilucion y curva de calibracion con pendiente, intercepto y R^2.",
        epilog="Las unidades las declaras tu y se imprimen siempre. R^2 alto no es sinonimo de exactitud.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--test", action="store_true", help="corre los autotests y sale")
    sub = p.add_subparsers(dest="modo")

    c = sub.add_parser("c1v1", help="resuelve la incognita de C1 x V1 = C2 x V2")
    c.add_argument("--c1", type=dec, help="concentracion del stock")
    c.add_argument("--v1", type=dec, help="volumen de stock a tomar")
    c.add_argument("--c2", type=dec, help="concentracion final deseada")
    c.add_argument("--v2", type=dec, help="volumen final")
    c.add_argument("--unidad-conc", default="ppm", dest="uc", help="unidad de concentracion (def. ppm)")
    c.add_argument("--unidad-vol", default="mL", dest="uv", help="unidad de volumen (def. mL)")

    s = sub.add_parser("serie", help="serie de diluciones seriadas")
    s.add_argument("--c0", type=dec, required=True, help="concentracion del stock inicial")
    s.add_argument("--factor", type=dec, required=True, help="factor de dilucion por paso (ej. 2 = 1:2)")
    s.add_argument("--niveles", type=int, required=True, help="cuantos niveles")
    s.add_argument("--volumen-final", type=dec, required=True, dest="vf", help="volumen final de cada tubo")
    s.add_argument("--unidad-conc", default="ppm", dest="uc", help="unidad de concentracion (def. ppm)")
    s.add_argument("--unidad-vol", default="mL", dest="uv", help="unidad de volumen (def. mL)")

    k = sub.add_parser("curva", help="regresion de curva de calibracion y calculo de muestra")
    k.add_argument("--conc", type=str, required=True,
                   help="concentraciones de los patrones separadas por coma (ej: 1,2,5,10,20)")
    k.add_argument("--area", type=str, required=True,
                   help="areas correspondientes separadas por coma (mismo orden)")
    k.add_argument("--area-muestra", type=dec, default=None, dest="am",
                   help="area de la muestra para calcular su concentracion")
    k.add_argument("--factor-dilucion", type=dec, default=Decimal("1"), dest="fd",
                   help="factor de dilucion de la muestra (def. 1)")
    k.add_argument("--unidad-conc", default="ppm", dest="uc", help="unidad de concentracion (def. ppm)")
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


def main(argv):
    if "--test" in argv:
        return autotest()
    p = construir_parser()
    args = p.parse_args(argv)
    if not args.modo:
        p.print_help()
        return 0
    try:
        if args.modo == "c1v1":
            inc, val, d = resolver_c1v1(args.c1, args.v1, args.c2, args.v2)
            print("DILUCION  C1 x V1 = C2 x V2")
            print("  Incognita resuelta: %s = %s" % (inc.upper(), n(val, 6)))
            print("")
            print("  C1 (stock)   : %s %s" % (n(d["c1"], 6), args.uc))
            print("  V1 (a tomar) : %s %s" % (n(d["v1"], 6), args.uv))
            print("  C2 (final)   : %s %s" % (n(d["c2"], 6), args.uc))
            print("  V2 (final)   : %s %s" % (n(d["v2"], 6), args.uv))
            print("")
            print("  PROCEDIMIENTO: toma %s %s de stock y lleva a %s %s con diluyente"
                  % (n(d["v1"], 4), args.uv, n(d["v2"], 4), args.uv))
            print("                 (es decir, agrega %s %s de diluyente)" % (n(d["diluyente"], 4), args.uv))
            print("  Factor de dilucion: %s x" % n(d["fd"], 4))
            print("  Comprobacion masa : C1*V1 = %s = C2*V2 = %s"
                  % (n(d["c1"] * d["v1"], 6), n(d["c2"] * d["v2"], 6)))

        elif args.modo == "serie":
            filas = serie_diluciones(args.c0, args.factor, args.niveles, args.vf)
            print("SERIE DE DILUCIONES 1:%s" % n(args.factor, 2))
            print("  Stock: %s %s   Volumen final por tubo: %s %s" % (n(args.c0, 6), args.uc, n(args.vf, 4), args.uv))
            print("")
            print("  %-7s %18s %14s %14s %12s" % ("nivel", "concentracion", "stock (%s)" % args.uv,
                                                  "diluyente", "FD acum."))
            for f in filas:
                print("  %-7d %18s %14s %14s %12s"
                      % (f["nivel"], n(f["conc"], 6), n(f["v_stock"], 4), n(f["v_diluyente"], 4),
                         n(f["fd_acumulado"], 1)))
            print("")
            print("  Todas las concentraciones estan en %s. Volumenes en %s." % (args.uc, args.uv))
            print("  Cada paso usa %s %s del tubo ANTERIOR (no del stock original)." % (n(filas[0]["v_stock"], 4), args.uv))
            print("  El error de pipeteo se acumula: en el nivel %d ya llevas %d transferencias."
                  % (len(filas), len(filas)))

        elif args.modo == "curva":
            xs = _lista(args.conc, "--conc")
            ys = _lista(args.area, "--area")
            r = regresion(xs, ys)
            print("CURVA DE CALIBRACION (minimos cuadrados, sin ponderar)")
            print("  Puntos       : %d   (ICH Q2(R2) pide minimo 5 niveles)" % r["n"])
            print("  Rango        : %s a %s %s" % (n(min(xs), 6), n(max(xs), 6), args.uc))
            print("")
            print("  Ecuacion     : area = %s x conc + %s" % (n(r["pendiente"], 6), n(r["intercepto"], 6)))
            print("  Pendiente (S): %s unidades de area por %s" % (n(r["pendiente"], 6), args.uc))
            print("  Intercepto   : %s unidades de area" % n(r["intercepto"], 6))
            print("  R^2          : %s" % n(r["r2"], 6))
            print("  s(y/x) resid.: %s unidades de area" % n(r["s_yx"], 6))
            if r["media_y"] != 0:
                rel = abs(r["intercepto"]) * Decimal(100) / abs(r["media_y"])
                print("  |intercepto| como %% de la respuesta media: %s %%" % n(rel, 2))
                if rel > Decimal("5"):
                    print("  ATENCION: intercepto grande. Revisa blanco, contaminacion o efecto matriz.")
            if r["r2"] < Decimal("0.99"):
                print("  ATENCION: R^2 por debajo de 0,99. Para cuantificacion analitica suele exigirse >= 0,995.")
            print("")
            if args.am is not None:
                c = concentracion_desde_area(args.am, r["pendiente"], r["intercepto"], args.fd)
                print("  MUESTRA")
                print("    Area medida        : %s" % n(args.am, 4))
                print("    Factor de dilucion : %s x" % n(args.fd, 4))
                print("    Concentracion en el vial : %s %s"
                      % (n(concentracion_desde_area(args.am, r["pendiente"], r["intercepto"]), 6), args.uc))
                print("    Concentracion en la muestra original : %s %s" % (n(c, 6), args.uc))
                if args.am > max(ys) or args.am < min(ys):
                    print("    ATENCION: el area de la muestra esta FUERA del rango de la curva.")
                    print("    Extrapolar no es cuantificar: diluye la muestra o amplia la curva.")
                print("")
            print("  BASE: la concentracion sale en la base del PATRON. Si tu patron esta en base seca,")
            print("  el resultado esta en base seca. Declaralo en el informe.")
            print("  R^2 alto no demuestra exactitud: mira los residuos y el intercepto.")
        return 0
    except ErrorDeEntrada as e:
        print("ERROR DE ENTRADA: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))