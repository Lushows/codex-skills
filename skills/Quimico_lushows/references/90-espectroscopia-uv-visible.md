# 90 — Espectroscopía UV-visible (el instrumento más barato del laboratorio, y el más fácil de creerle de más)

El UV-Vis mide cuánta luz absorbe una solución a una longitud de onda determinada. Es barato, rápido y está
en cualquier laboratorio universitario de Colombia. Por eso muchísimos "análisis" de suplementos salen de
ahí: polifenoles totales, "polisacáridos totales", proteína, color. El problema es que el UV-Vis **no
identifica**: te dice que algo absorbe a 490 nm, no *qué* absorbe. Si vas a comprar o vender un número que
salió de un UV-Vis, tienes que saber exactamente qué mide y qué se le cuela. Ese malentendido es el motor de
buena parte del fraude en hongos y en extractos vegetales.

Términos: **absorbancia (absorbance, A)** = logaritmo de cuánta luz se quedó en la muestra; adimensional.
**longitud de onda (wavelength, λ)** = "color" de la luz, en nanómetros (nm). **blanco (blank)** = la misma
matriz sin el analito, para restar lo que absorbe el fondo. **absortividad molar (molar absorptivity, ε)** =
qué tan fuerte absorbe una sustancia, en L·mol⁻¹·cm⁻¹. **matriz (matrix)** = todo lo demás que hay en la
muestra además de lo que quieres medir.

## La ley que lo gobierna todo: Lambert-Beer

```
A = ε · c · b

A = absorbancia (sin unidad)
ε = absortividad molar (L·mol⁻¹·cm⁻¹)
c = concentración (mol·L⁻¹)
b = camino óptico de la celda (cm), normalmente 1,00 cm
```

Cuando no conoces ε (caso típico en productos naturales), no usas la ley directa: usas una **curva de
calibración** con un patrón (ver `71-curva-de-calibracion.md`) y despejas la concentración de la recta.

Rango útil de trabajo: **A entre 0,1 y 1,0**. Por debajo de 0,1 el ruido se come el dato; por encima de 1,0
la respuesta deja de ser lineal (el detector se satura y la ley de Beer se dobla). Si tu lectura da 1,8,
no reportes: diluye y vuelve a leer.

## Qué se puede y qué no se puede hacer con UV-Vis

| Uso | ¿Sirve? | Por qué |
|---|---|---|
| Cuantificar una sustancia **pura y conocida** en solución limpia | Sí | Un solo cromóforo, matriz simple |
| Seguir una cinética (degradación, reacción) | Sí | Cambio relativo en el tiempo, mismo error en todos los puntos |
| Ensayos colorimétricos con reactivo específico | Sí, con cuidado | Ver `91-metodos-colorimetricos-y-enzimaticos.md` |
| Cuantificar cannabinoides individuales | No | Δ9-THC, THCA, CBD y CBDA absorben casi igual (~208 y ~230 nm); no los separa |
| "Polisacáridos totales" en hongos | No para β-glucano | Mide también almidón; ver `222-polisacaridos-totales-por-que-no-sirve.md` |
| Identificar una sustancia desconocida | No | Un espectro UV ancho no es una huella; para eso está MS o RMN |

La regla dura: **UV-Vis sin separación previa mide una suma, no un compuesto.** Si quieres el compuesto,
tienes que separarlo antes (HPLC con detector UV, `79-hplc-y-uhplc.md` y `80-deteccion-uv-dad-y-pureza-de-pico.md`).

## Interferencias que arruinan el dato

- **Turbidez y partículas.** La luz dispersada se lee como absorbancia falsa. Centrifuga o filtra a 0,45 µm.
- **Color propio de la matriz.** Un extracto de chaga es café oscuro; ese color se suma a tu señal si el
  blanco no lo contempla. El blanco debe ser la **misma matriz** sin la reacción, no agua.
- **Solvente que absorbe.** Por debajo de 220 nm casi todo estorba: acetona, DMSO, acetato de etilo. Metanol
  y acetonitrilo grado HPLC llegan más abajo. Consulta el "corte UV" (UV cutoff) del solvente.
- **pH.** Fenoles, flavonoides y muchos alcaloides cambian de espectro con el pH. Si no fijas el pH con
  buffer, tu número se mueve entre días (ver `23-buffers-y-control-de-ph.md`).
- **Burbujas y huellas dactilares en la celda.** Suenan a chiste; son la causa #1 de puntos fuera de la recta.

## Cómo se mide (procedimiento tipo)

1. Escoge λ en el **máximo de absorción** del analito (haz primero un barrido, *scan*, de 200 a 800 nm).
2. Prepara **patrón** certificado y una curva de 5–6 niveles que abarque tu muestra (ver `70` y `71`).
3. Lee el blanco. Cero contra blanco, no contra aire.
4. Lee patrones en orden ascendente, luego muestras, y **re-lee un patrón intermedio al final** para
   confirmar que el instrumento no se movió (esto es control de calidad, ver `77`).
5. Reporta: analito, λ, método/kit, curva y R², diluciones, **unidad y base**.

Unidades típicas de salida: `mg equivalentes de X por g de muestra en base seca` — y ojo con la palabra
**equivalentes**: significa "medido contra el patrón X", no "es X".

## Ejemplo aplicado (ILUSTRATIVO)

Extracto de melena de león (*Hericium erinaceus*), cuerpo fructífero, lote HE-2604.

```
Analito         : polifenoles totales (Folin-Ciocalteu)
λ               : 765 nm
Patrón          : ácido gálico, curva 0-100 µg/mL, R² = 0,9987
Lectura muestra : A = 0,412  (dentro de 0,1-1,0, OK)
Concentración   : 46,8 µg/mL de equivalentes de ácido gálico
Dilución total  : x 250
Humedad         : 6,2 % p/p
Resultado       : 12,5 mg GAE/g base seca   (GAE = gallic acid equivalents)
```

Lo que **no** puedes decir con este dato: "el extracto tiene 12,5 mg/g de polifenoles". Puedes decir
"12,5 mg de equivalentes de ácido gálico por gramo en base seca, por Folin-Ciocalteu". El reactivo de
Folin también reacciona con azúcares reductores, ácido ascórbico y proteínas: es un ensayo de **poder
reductor**, no de polifenoles. (Cifra ilustrativa, no es un resultado real de BIO-SETA.)

## Errores comunes

- **Reportar "polisacáridos" o "polifenoles" como si fuera el compuesto.** Son *equivalentes* de un patrón.
  Cambiar de patrón cambia el número sin que cambie la muestra.
- **Blanco de agua en una matriz coloreada.** Infla el resultado; en extractos oscuros el error puede ser
  del mismo tamaño que el resultado.
- **Leer fuera del rango lineal** y confiar en que la recta "se extrapola". No se extrapola.
- **No reportar la base.** Un 30 % base húmeda con 10 % de humedad es 33,3 % base seca (ver `07`).
- **Usar UV-Vis para decidir cumplimiento regulatorio** (THC, metales, micotoxinas). Ningún regulador serio
  acepta UV-Vis para eso; se exige cromatografía o ICP-MS.
- **Curva vieja.** Reusar la calibración de la semana pasada porque "el equipo es estable". Recalibra.

## Conexión con otros módulos

→ `91-metodos-colorimetricos-y-enzimaticos.md` — el UV-Vis aplicado a kits: dónde sí y dónde el fraude.
→ `71-curva-de-calibracion.md` — cómo se construye y se valida la recta que sostiene el número.
→ `80-deteccion-uv-dad-y-pureza-de-pico.md` — el mismo detector, pero después de separar por HPLC.
→ `222-polisacaridos-totales-por-que-no-sirve.md` — el caso concreto donde el UV-Vis engaña en hongos.
→ `07-base-seca-vs-humeda.md` — sin base declarada, el número no se compara con nada.
