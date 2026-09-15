# 154 — Cápsulas y encapsulado (el formato con el que empieza casi toda pyme)

La cápsula dura es el formato más perdonador que existe: oculta el sabor, no exige compresión, tolera polvos
que fluyen regular y se puede hacer a escala pequeña con equipo de bajo costo. Es donde debe empezar casi
cualquier proyecto de extracto de hongos en Colombia. Pero tiene dos trampas que cuestan lotes: **el tamaño se
elige por volumen, no por peso**, y **la uniformidad de llenado es un atributo medible que INVIMA y tu propio
cliente pueden verificar**.

Términos: **cápsula dura (hard capsule / two-piece capsule)** = cuerpo + tapa que se encajan. **HPMC
(hypromellose)** = celulosa modificada; alternativa vegetal a la gelatina. **Densidad aparente (bulk density)**
= masa/volumen del polvo sin compactar. **Densidad compactada (tapped density)** = después de golpes normalizados.
**Índice de Carr (Carr index)** = medida de fluidez del polvo. **Uniformidad de masa (mass uniformity)** =
cuánto varían las cápsulas entre sí.

## Tamaños y capacidad real

| Tamaño | Volumen (mL) | Masa a densidad 0,5 g/mL | Masa a 0,7 g/mL | Masa a 0,9 g/mL |
|---|---|---|---|---|
| 000 | 1,37 | 685 mg | 959 mg | 1233 mg |
| 00 | 0,91 | 455 mg | 637 mg | 819 mg |
| 0 | 0,68 | 340 mg | 476 mg | 612 mg |
| 1 | 0,50 | 250 mg | 350 mg | 450 mg |
| 2 | 0,37 | 185 mg | 259 mg | 333 mg |
| 3 | 0,30 | 150 mg | 210 mg | 270 mg |

La tabla lo dice todo: **la misma cápsula 0 puede llevar 340 mg o 612 mg** según la densidad de tu polvo. Por
eso lo primero que se mide antes de comprar cápsulas vacías es la densidad compactada del extracto.

```
MEDIR DENSIDAD (10 minutos, sin instrumentos caros)
  1. Vierte polvo en probeta de 100 mL sin compactar. Pesa.
     densidad aparente = masa (g) / 100 mL
  2. Golpea la probeta 500 veces (o usa tapped density tester). Lee el volumen final.
     densidad compactada = masa (g) / volumen final (mL)
  3. Índice de Carr = (compactada − aparente) / compactada × 100

  Carr < 15 %   flujo excelente        → encapsula bien
  Carr 16–25 %  flujo aceptable        → puede requerir deslizante
  Carr > 25 %   flujo pobre            → necesita deslizante y/o granulación
```

## Gelatina vs HPMC

| Criterio | Gelatina (bovina/porcina) | HPMC (vegetal) |
|---|---|---|
| Costo | Menor | 20–40 % más (orden de magnitud típico) |
| Origen | Animal | Vegetal — apto vegano/halal/kosher |
| Humedad de equilibrio | 13–16 % | 4–6 % |
| Con polvos higroscópicos | Se ablanda y se pega | **Mejor: tolera baja humedad** |
| Fragilidad en clima seco | Se vuelve quebradiza | Estable |
| Percepción de mercado | Neutra a negativa | Positiva |

Para extracto de hongos —que es higroscópico— la **HPMC** suele ser la elección técnica correcta además de la
comercial. La gelatina con un polvo muy seco se deshidrata, se agrieta y el lote se rompe en el frasco.

## La fórmula unitaria: el activo casi nunca va solo

| Función | Ejemplos | % típico |
|---|---|---|
| Activo | Extracto estandarizado | 60–95 % |
| Diluyente / relleno | Celulosa microcristalina, fosfato dicálcico, inulina | 0–35 % |
| Deslizante (glidant) | Dióxido de silicio coloidal (aerosil) | 0,2–1,0 % |
| Lubricante | Estearato de magnesio, estearato vegetal | 0,3–1,0 % |
| Desintegrante | Croscarmelosa (poco usado en cápsula) | 0–3 % |

Nota práctica y comercial: el estearato de magnesio tiene mala prensa injustificada en el mercado de
suplementos. Técnicamente es un lubricante seguro a las dosis usadas; si tu posicionamiento exige evitarlo,
usa dióxido de silicio y arroz en polvo, pero asume que el llenado será menos consistente. Es una decisión de
marca, no de química (`160`).

## Equipo: qué puede hacer una pyme

| Equipo | Capacidad | Costo relativo | Nota |
|---|---|---|---|
| Encapsuladora manual 100 huecos | ~2 000–4 000 cáps/h con práctica | Muy bajo | La entrada real |
| Encapsuladora manual 400 huecos | ~8 000–12 000 cáps/h | Bajo | Requiere 2 personas |
| Semiautomática | 15 000–25 000 cáps/h | Medio-alto | Ya es planta |
| Automática | 50 000+ cáps/h | Alto | Maquila |
| Pulidora / desempolvadora | — | Bajo | Necesaria: el polvo por fuera ensucia el frasco |
| Balanza analítica 0,001 g | — | Bajo | **Obligatoria** para control de uniformidad |

Advertencia de cumplimiento: **encapsular en tu casa o en una bodega no certificada no te da un producto
vendible legalmente** en Colombia como suplemento dietario. Sirve para desarrollo, muestras internas y
pruebas; para vender hay que fabricar en planta con BPM, propia o de maquila (`167`, `269`).

## Cómo se comprueba un lote de cápsulas

```
CONTROL DE PROCESO (durante el llenado, cada 15–30 min)
  Tomar 10 cápsulas al azar, pesar una a una.
  Calcular masa media y % de desviación individual.

CRITERIO DE UNIFORMIDAD DE MASA (criterio farmacopeico general para cápsulas)
  Para masa promedio ≥ 300 mg:
    - ninguna cápsula fuera de ±7,5 % de la media, salvo un máximo de 2 unidades
    - ninguna fuera de ±15 %
  (Verificar el texto vigente de la farmacopea que adoptes: USP <2091> / Ph. Eur. 2.9.5, `280`.)

CONTROL DE LOTE (al final)
  - masa media del contenido (descontando la cápsula vacía)
  - contenido de activo sobre muestra compuesta de 10–20 cápsulas
  - desintegración (típicamente ≤ 30 min en medio acuoso)
  - humedad y a_w
  - microbiología (`100`)
```

La uniformidad de masa **no** prueba uniformidad de contenido: si la mezcla estaba mal homogeneizada, todas las
cápsulas pueden pesar igual y tener distinta potencia. Por eso la mezcla se valida aparte (muestreo en varios
puntos del mezclador, `166`).

## Ejemplo aplicado — diseñar la cápsula de BIO-SETA

```
Objetivo (de `161`): 150 mg de β-glucano por cápsula.
Extracto disponible: β-glucano 32,0 % p/p base seca, densidad compactada 0,62 g/mL.

1. Masa de extracto necesaria = 150 / 0,320 = 469 mg
2. + deslizante 0,5 % y lubricante 0,5 %  →  469 / 0,99 = 474 mg de mezcla
3. Volumen requerido = 0,474 g / 0,62 g/mL = 0,765 mL
4. ¿Qué cápsula? La 0 tiene 0,68 mL → NO ALCANZA. Sube a 00 (0,91 mL). ✔
5. Fórmula unitaria final (cápsula 00, HPMC):
       extracto de reishi dual         469,0 mg
       dióxido de silicio coloidal       2,4 mg
       estearato de magnesio vegetal     2,4 mg
       -------------------------------------------
       masa de llenado                 473,8 mg   (llenado ~52 % del volumen: holgado, buen flujo)
6. Etiqueta: "cada cápsula aporta ≥ 150 mg de β-glucano (Megazyme K-YBGL)".
```

Todas las cifras son **(ILUSTRATIVAS)**; el cálculo se ejecuta en `lab-tools/potencia_formula.py` y se verifica
por segunda vía. Fíjate en el paso 4: comprar cápsulas tamaño 0 antes de hacer esta cuenta es el error que
cuesta el pedido entero.

## Errores comunes

- Comprar cápsulas por peso deseado sin medir la densidad del polvo. El tamaño se elige por **volumen**.
- Usar gelatina con un extracto higroscópico y encontrarse cápsulas blandas o pegadas.
- No pulir las cápsulas: polvo residual afuera, frasco sucio, cliente desconfiado.
- Encapsular un polvo con Carr > 25 % sin deslizante: el llenado varía 20 % entre cápsulas.
- Suponer que uniformidad de masa = uniformidad de contenido.
- Encapsular en ambiente húmedo: el polvo toma agua durante el proceso y la humedad final se sale de spec.
- Vender producto encapsulado en instalación sin BPM. Es riesgo sanitario y legal, no un atajo.

## Conexión con otros módulos

→ `161-dosis-y-tamano-de-porcion.md` — de dónde salen los 150 mg del ejemplo.
→ `160-excipientes-y-compatibilidad.md` — deslizantes, lubricantes y qué puede reaccionar con qué.
→ `143-molienda-y-granulometria.md` — el tamaño de partícula que hace que el polvo fluya.
→ `155-tabletas-y-compresion.md` — el salto siguiente, y por qué casi nunca conviene al principio.
→ `167-bpm-gmp-para-suplementos.md` — dónde se puede encapsular legalmente.