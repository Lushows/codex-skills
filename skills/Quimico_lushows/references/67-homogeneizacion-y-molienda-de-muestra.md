# 67 — Homogeneización y molienda de muestra (por qué el tamaño de partícula decide tu resultado)

Entre los 900 g de muestra compuesta y los 0,5 g que se pesan en la balanza analítica hay un salto de mil
veces. Ese salto solo es honesto si el material está tan finamente dividido y tan bien mezclado que
cualquier medio gramo se parece a cualquier otro. Moler no es un trámite: es la operación que fija el error
mínimo alcanzable de todo el análisis. Y moler mal destruye analitos: los terpenos se evaporan con el calor
del molino y la psilocibina se oxida.

Términos:
- **Malla / mesh (mesh size)** = número de aberturas por pulgada lineal de un tamiz. Malla 40 ≈ 425 µm,
  malla 60 ≈ 250 µm, malla 80 ≈ 180 µm. A mayor número, partícula más fina.
- **Molienda criogénica (cryogenic milling)** = moler con nitrógeno líquido o hielo seco para evitar
  calentamiento y pérdida de volátiles.
- **Error fundamental de muestreo (fundamental sampling error, FSE)** = el error irreducible que depende del
  tamaño de partícula y de la masa analizada.
- **Contaminación cruzada por el molino (carryover)** = residuo del lote anterior que pasa al siguiente.

## Por qué el tamaño de partícula importa tanto

El error fundamental de muestreo crece con el **cubo del diámetro de partícula** y baja con la masa
analizada. En la teoría del muestreo (Pierre Gy) se aproxima así:

```
s²_FSE  ≈  C · d³ / M

  d = diámetro de la partícula más grande (cm)
  M = masa de la alícuota analizada (g)
  C = constante de la matriz (heterogeneidad, densidad, ley del analito)

Consecuencia práctica: reducir d a la mitad reduce la varianza 8 veces.
Aumentar M al doble la reduce solo 2 veces.
```
Traducción: **moler más fino rinde mucho más que pesar más muestra**. Por eso todos los métodos de
farmacopea y de AOAC empiezan con "moler y pasar por tamiz de malla X".

| Analito / matriz | Finura recomendada | Por qué |
|---|---|---|
| β-glucano en polvo de hongo | Malla 40–60 | Extracción enzimática completa; el grano grueso no se digiere |
| Cannabinoides en flor | Molienda a 1–2 mm, homogénea | Los tricomas deben repartirse; sobre-moler apelmaza resina |
| Terpenos en flor | Criogénica, sin calor | Se pierden por volatilidad por encima de ~35 °C |
| Metales pesados | Malla 60–80 | Contaminantes distribuidos en partícula fina |
| Micotoxinas | Malla 40 + masa grande (>= 25 g) | Distribución extremadamente heterogénea ("hot spots") |
| Psilocibina | Fino, en frío y oscuridad | Se oxida y degrada con calor, luz y oxígeno (`255`) |

## El molino que uses cambia el número

| Tipo | Cómo funciona | Riesgo | Bueno para |
|---|---|---|---|
| Molino de cuchillas (blade / knife mill) | Corta a alta velocidad | Calienta: pierde volátiles | Uso general en seco |
| Molino de bolas (ball mill) | Impacto en cámara cerrada | Contaminación metálica (Cr, Ni, Fe) | Polvos finos, no para metales traza |
| Molino criogénico (cryo mill / freezer mill) | Congela y luego fractura | Costo, requiere N₂ líquido | Terpenos, psilocibina, material graso |
| Mortero de ágata | Manual | Lento, no reproducible a escala | Muestras pequeñas, metales traza |
| Molino de cuchillas de titanio/cerámica | Corta sin aportar metal | Costo | Metales pesados por ICP-MS |

Punto crítico y poco conocido: **si vas a medir metales pesados, el molino no puede aportar metales.** Moler
en un molino de acero inoxidable puede sumar cromo y níquel a la muestra. Pregúntale al laboratorio con qué
material muele cuando el ensayo es de trazas metálicas.

## Homogeneizar: mezclar es más difícil de lo que parece

Mezclar polvos no siempre homogeneiza: si hay diferencia de tamaño o densidad, la agitación **segrega**
(efecto nuez de Brasil: la partícula grande sube). Prácticas que funcionan:

1. Moler **todo** el material compuesto, no una parte.
2. Mezclar en V o en tambor rotatorio, tiempos cortos (2–5 min), no agitación violenta.
3. Volver a cuartear después de mezclar, no antes.
4. Tomar la alícuota de análisis inmediatamente después de mezclar, no al día siguiente.
5. Si el material es higroscópico (los polvos de hongo lo son), trabajar rápido o en ambiente controlado:
   la humedad cambia la base de reporte (`07`, `35`).

## Cómo se comprueba que la homogeneización sirvió

Es medible y deberías exigirlo cuando el lote vale la pena:

```
Prueba de homogeneidad (ILUSTRATIVO):
  Tomar 5 alícuotas independientes de 0,5 g de la muestra ya molida y mezclada.
  Analizar las 5 por el mismo método, misma corrida.

  Resultados β-glucano (% p/p base seca): 24,3 · 23,9 · 24,6 · 24,1 · 24,0
  media = 24,18 ; s = 0,27 ; RSD = 1,1 %

  Criterio de aceptación típico: RSD <= 2-3 % para un método con
  repetibilidad de ~2 %. Si sale 8 %, la muestra NO está homogénea
  y el problema es la molienda, no el HPLC.
```
Ese RSD (desviación estándar relativa, *relative standard deviation*) es la manera de separar "el material
es variable" de "el laboratorio es impreciso" (`74`, `78`).

## Ejemplo aplicado — flor de cannabis y el fraude involuntario del kief

Un productor manda a analizar 5 g tomados del fondo del tarro donde reposó la flor. El fondo acumula
tricomas desprendidos (kief), que son casi resina pura.

```
Resultado del fondo del tarro   : THC total 27,4 % p/p base seca   (ILUSTRATIVO)
Resultado de la flor bien molida: THC total 19,8 % p/p base seca   (ILUSTRATIVO)
Diferencia relativa: +38 %
```
Nadie mintió; el instrumento tenía razón las dos veces. El COA que se usa para vender es el primero y el
producto que recibe el cliente es el segundo. Ese es exactamente el mecanismo de la inflación de potencia
que se discute en `113`. Se previene con una sola frase en el SOP: *"la muestra compuesta se muele
íntegramente antes de reducir"*.

## Qué preguntarle al laboratorio

1. ¿Muelen la muestra completa o solo la porción que van a pesar?
2. ¿Qué malla y qué tipo de molino usan para esta matriz?
3. ¿Muelen en frío cuando el ensayo incluye terpenos o compuestos termolábiles?
4. ¿Cómo limpian el molino entre muestras y cómo verifican que no hay arrastre?
5. Para metales: ¿el molino aporta metal? ¿Corren un blanco de molienda?
6. ¿Guardan una porción de la muestra molida como retención, y por cuánto tiempo?

## Errores comunes

- **Moler solo lo que cabe en el molino** y descartar el resto: reintroduce todo el sesgo del muestreo.
- **Analizar flor sin moler** ("porque el método lo permite"): resultados irreproducibles entre laboratorios.
- **Moler terpenos en caliente:** se pierden los monoterpenos ligeros y el perfil sale falsamente
  sesquiterpénico (`199`).
- **Usar el mismo molino sin limpiar** entre un lote potente y uno flojo: arrastre y falsos positivos.
- **Homogeneizar agitando fuerte:** segrega en vez de mezclar.
- **Ignorar que la muestra ganó humedad** durante la molienda: el % baja y no es que el activo se haya ido
  (`07`).

## Conexión con otros módulos

→ `66-plan-de-muestreo-y-representatividad.md` — de dónde viene la compuesta.
→ `68-preparacion-de-muestra-solidos.md` — pesada, secado y digestión después de moler.
→ `143-molienda-y-granulometria.md` — molienda a escala de producción, no de laboratorio.
→ `199-analisis-de-perfil-de-terpenos.md` — por qué aquí la criogenia no es opcional.
→ `113-lab-shopping-e-inflacion-de-potencia.md` — cómo la molienda se usa para inflar números.
