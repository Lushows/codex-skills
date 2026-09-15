# 151 — Relación planta:extracto y ratios (por qué "10:1" no dice absolutamente nada del activo)

"Extracto 10:1" es la frase más repetida y más vacía del mercado de suplementos. Suena a concentración, a
potencia, a premium. No lo es. El ratio es una **relación de masa**: cuántos kilos de material seco entraron por
cada kilo de extracto que salió. No dice qué salió, ni cuánto activo hay, ni si el activo sobrevivió. Y como
nadie lo audita, es el número más fácil de inflar del sector. Este módulo desarma el truco para que puedas
comprar bien y para que tu propia etiqueta no dependa de un número que no significa nada.

Términos: **ratio planta:extracto (drug-to-extract ratio, DER)** = masa de material de partida / masa de
extracto obtenido, ambas en base seca. **DER genuino (native DER)** = el ratio del extracto **sin** soporte.
**Extracto nativo (native extract)** = el sólido que sale de la extracción, sin carrier. **Equivalente de
material vegetal (herb equivalent)** = los mg de material de partida que representa una dosis de extracto.

## Qué es y qué no es el ratio

```
DER = masa de materia prima seca (kg)  /  masa de extracto nativo seco (kg)

Ejemplo: 10,0 kg de cuerpo fructífero seco → 1,0 kg de extracto seco   →  DER = 10:1
```

Lo que el ratio **sí** dice: cuánta masa se fue. Nada más.

Lo que el ratio **no** dice:
- Cuánto β-glucano, triterpeno o cannabinoide hay en ese kilo.
- Si el material de partida era rico o pobre. Un 10:1 de material malo es peor que un 4:1 de material bueno.
- Si el extracto trae soporte (maltodextrina) que rebajó todo (`150`).
- Con qué solvente se hizo. Un 10:1 acuoso y un 10:1 alcohólico son productos químicamente distintos (`146`).
- Si el proceso degradó el activo por calor.
- Si el "10:1" es real o si simplemente se lo inventaron. No hay un análisis que lo verifique en el producto
  terminado: el ratio **no es medible aguas abajo**, solo documentable aguas arriba.

Ese último punto es demoledor y hay que decirlo sin rodeos: **el ratio no es un atributo verificable de
calidad.** Un laboratorio puede medirte β-glucano. Ningún laboratorio del mundo puede abrir tu cápsula y
decirte "esto es 10:1".

## El truco aritmético del titular

El uso comercial del ratio es convertir una dosis pequeña en un número grande en el frente del frasco:

```
Cápsula real: 50 mg de extracto 10:1
Titular de etiqueta: "equivalente a 500 mg de hongo"
                     y a veces, directamente: "500 mg"

Lo que el consumidor entiende:  500 mg de producto.
Lo que se tomó:                  50 mg de un polvo del que no sabemos el contenido de activo.
```

Documentación del sector describe exactamente esta mecánica: un ratio 10:1 convierte 50 mg de extracto en un
titular de "500 mg", y la etiqueta no aporta ninguna información sobre el compuesto activo real. Es legal en
muchos mercados y es, técnicamente, información vacía.

## Cómo se infla un ratio sin mentir del todo

| Maniobra | Efecto sobre el ratio | Efecto sobre el activo |
|---|---|---|
| Partir de material de baja calidad | Sube (rinde menos extracto) | Baja |
| Extraer poco tiempo / mal | Sube (menos masa extraída) | Baja |
| Calcular sobre material **húmedo** | Sube artificialmente | Ninguno (es truco de base, `07`) |
| Contar el soporte como extracto | Baja el DER real, no se declara | Baja por dilución |
| Declarar DER "teórico" del proceso original de otro | Cualquiera | Ninguno |
| Usar material fresco como base ("10:1 desde fresco") | Sube ~5–8× por el agua | Ninguno |

La maniobra del **material fresco** merece un párrafo. Si un hongo fresco tiene ~88 % de agua, 10 kg de fresco
son ~1,2 kg de seco. Un "10:1 desde fresco" es, en base seca, aproximadamente un 1,2:1. Es decir: casi polvo
sin extraer. Por eso la única forma seria de escribir un ratio es **base seca a base seca, y decirlo**.

## Cómo se calcula honestamente

```
DER NATIVO (el único que vale)

  DER = MP_seca (kg) / extracto_nativo_seco (kg)

  donde extracto_nativo_seco = polvo_total × (1 − fracción de soporte)

Ejemplo (ILUSTRATIVO):
  MP: 11,80 kg base seca
  Polvo entregado: 1,512 kg con 25 % p/p de fibra de acacia como soporte
  Extracto nativo = 1,512 × 0,75 = 1,134 kg
  DER nativo = 11,80 / 1,134 = 10,4 : 1
  DER aparente (si contaras el soporte) = 11,80 / 1,512 = 7,8 : 1

  → Publicar "10:1" sin decir que hay 25 % de soporte NO es falso,
    pero le esconde al comprador que cada gramo de polvo trae 750 mg de extracto.
```

Ejecuta esta cuenta en `lab-tools/rendimiento_extraccion.py`. Para decisiones de compra o de etiqueta, verifica
por segunda vía con `Matematicas_lushows`.

## Cómo se comprueba (o mejor: qué medir en vez del ratio)

No se comprueba. Se **sustituye**. Lo honesto y auditable es declarar el activo medido:

| En vez de… | Declara… | Método |
|---|---|---|
| "Extracto de reishi 10:1" | "≥ 25 % p/p de β-glucano base seca" | Megazyme K-YBGL (`221`) |
| "Extracto de reishi 20:1" | "≥ 2,0 % de triterpenos como ác. ganodérico A" | HPLC-DAD (`224`) |
| "Extracto de cordyceps 8:1" | "≥ 0,3 % de cordicepina" | HPLC/LC-MS (`228`) |
| "Extracto de cannabis 5:1" | "50,0 mg de CBD por mL" | HPLC-DAD (`198`) |

Ese es todo el módulo `152`: **estandarizar**. El ratio describe el proceso; la estandarización describe el
producto. Solo el segundo se puede medir, defender y sostener en una etiqueta.

## Cuándo el ratio sí es información útil

No es que el DER sea inútil siempre. Sirve para:

- **Control interno de proceso.** Si tus lotes pasan de 10:1 a 14:1, algo cambió: materia prima, tiempo,
  temperatura. Es una señal de alarma temprana (`169`).
- **Costeo.** El DER te dice cuánta materia prima necesitas por kilo de producto. Es un insumo directo del
  costo unitario; rutea a `contador_lushows` y `economist_lushows`.
- **Expediente técnico.** Documentar el DER del proceso es parte de describir cómo se fabrica (`286`).
- **Comparar lotes tuyos entre sí**, con el mismo material y el mismo proceso.

Lo que no sirve es como **argumento de venta** ni como **especificación de compra**.

## Ejemplo aplicado — auditar una oferta de proveedor

```
Oferta recibida: "Extracto de melena de león 15:1, 500 kg disponibles, USD X/kg"

Preguntas que hay que hacer ANTES de cotizar:
  1. ¿DER en base seca sobre material seco, o desde fresco?            → puede cambiar 6×
  2. ¿Parte usada: cuerpo fructífero o micelio en grano?                → (`217`, `218`)
  3. ¿Lleva soporte? ¿Cuál y en qué %?                                  → define el DER nativo
  4. ¿Solvente: agua, etanol o dual?                                    → define qué hay adentro
  5. ¿β-glucano por Megazyme, en % p/p base seca, de este lote?          → EL número que compras
  6. ¿α-glucano del mismo ensayo?                                       → detecta grano/maltodextrina
  7. ¿COA de laboratorio tercero acreditado?                            → (`107`, `108`)

Si contestan las 7, es un proveedor serio aunque el número no sea espectacular.
Si esquivan la 5 y la 6 y solo repiten "15:1", ya sabes lo que compras: un ratio.
```

## Errores comunes

- Comprar por ratio y venderse a sí mismo la idea de que un número mayor es mejor producto.
- Poner el "equivalente en planta" en grande y los mg reales en chiquito. Funciona en ventas y se cae en
  auditoría (`272`, `293`).
- Calcular el ratio con la materia prima húmeda y el extracto seco. Es mezclar bases (`07`).
- Contar el soporte como extracto y publicar el DER aparente.
- Suponer que el ratio se puede verificar en el producto terminado. No se puede.
- Cambiar de proveedor manteniendo el "10:1" de la etiqueta: el nuevo 10:1 casi seguro tiene otra potencia.
- Aceptar "espectro completo 10:1" como si fueran dos datos. Son cero datos (`146`).

## Conexión con otros módulos

→ `152-estandarizacion-de-extractos.md` — lo que sí se puede declarar y medir.
→ `242-ratios-de-extraccion-y-etiquetado-honesto.md` — el caso específico de hongos, con ejemplos de etiqueta.
→ `150-secado-por-aspersion-y-liofilizacion.md` — de dónde sale el soporte que rebaja el DER.
→ `111-banderas-rojas-en-un-coa.md` — cómo se ve este truco en un certificado.
→ `293-como-comunicar-ciencia-sin-mentir.md` — cómo se vende la versión honesta.