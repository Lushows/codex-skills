# 242 — Ratios de extracción y etiquetado honesto (por qué "10:1" no significa nada por sí solo)

"Extracto 10:1" es la cifra más usada y menos entendida del mercado de hongos. Suena a potencia y no lo es:
es una **relación de masa** entre materia prima y extracto seco. Un 10:1 puede tener 30 % de beta-glucano o
5 %; puede venir de cuerpo fructífero o de micelio en grano; puede ser real o puede ser aritmética inventada
en un catálogo. Este módulo te enseña a leer el ratio, a calcularlo bien y a escribir una etiqueta que un
inspector o un químico no puedan tumbar.

Términos: **DER (drug-extract ratio)** = relación materia prima : extracto, la forma técnica de decir
"10:1". **DER nativo (native DER)** = el ratio del extracto puro, sin excipientes ni soportes.
**soporte / carrier** = maltodextrina, almidón o similar añadido para poder secar el extracto.
**marcador (marker)** = compuesto que se cuantifica para estandarizar (`152`).

## Qué dice y qué no dice un ratio

```
DER = masa de materia prima seca usada / masa de extracto seco obtenido

10 kg de cuerpo fructífero seco → 1 kg de extracto seco  ⇒  DER 10:1  (rendimiento 10 %)
```

| El ratio SÍ dice | El ratio NO dice |
|---|---|
| Cuánta biomasa se concentró en masa | Cuánto activo hay |
| Qué tan agotadora fue la extracción | Con qué solvente se hizo |
| Un orden de magnitud del costo | Si la materia prima era cuerpo fructífero o micelio en grano |
| Nada más | Si el extracto lleva 40 % de maltodextrina |

Regla dura: **un ratio no sustituye una cuantificación**. La única cifra que sostiene una etiqueta es el
activo medido por un método declarado (`02-ningun-dato-sin-metodo.md`).

## El truco aritmético del 10:1 imposible

Si un cuerpo fructífero seco tiene, digamos, 30 % p/p base seca de beta-glucano, y alguien te vende un
"extracto 10:1", el extracto no puede tener más beta-glucano del que permite el balance de masa:

```
Balance de masa (β-glucano):
  Entrada = 10,0 kg × 0,30 = 3,00 kg de β-glucano
  Si el extracto es 1,0 kg y toda la extracción fuera perfecta (recuperación 100 %),
  el extracto tendría 3,00 kg / 1,0 kg = 300 %  → IMPOSIBLE.
  Techo real: 100 %. Con recuperaciones realistas de 40–70 %, esperarías 30–50 % p/p b.s.
```

Al revés funciona como detector de mentiras: si te ofrecen un **8:1 con 70 % de beta-glucano** proveniente
de una materia prima que tiene 25 %, el balance no cierra ni con recuperación del 100 % de un solo golpe —
o el ratio es falso, o el porcentaje es falso, o el "beta-glucano" en realidad es beta-glucano de levadura
añadido. Verifica siempre el balance con `Matematicas_lushows` o `lab-tools/rendimiento_extraccion.py`.

## Cómo se mide / cómo se comprueba

| Paso | Qué se hace | Evidencia que debes exigir |
|---|---|---|
| 1. Identidad de la materia prima | ITS/ADN + inspección | Certificado de identidad (`245`) |
| 2. Masa de entrada | Pesaje del lote seco, con humedad medida | Registro de lote (`168`) |
| 3. Masa de salida | Pesaje del extracto seco, con humedad medida | Registro de lote |
| 4. DER nativo | Cálculo con ambas masas en base seca | Hoja de cálculo del lote |
| 5. Soportes | Declarar % de maltodextrina u otro | Ficha técnica del proveedor |
| 6. Activo | Megazyme (β-glucano), HPLC (triterpenos) | COA con método explícito (`110`) |

```
Corrección obligatoria a base seca antes de calcular el DER:
  Materia prima: 10,50 kg con 8,0 % humedad  → 9,66 kg base seca
  Extracto:       1,12 kg con 5,0 % humedad  → 1,06 kg base seca
  DER = 9,66 / 1,06 = 9,1 : 1   (no 9,4:1 como saldría en base húmeda)
```

## Cómo se escribe una etiqueta que no se cae

Mal (típico del mercado):

```
Reishi 10:1 — 500 mg
```

Bien (defendible ante INVIMA, FDA o un químico):

```
Extracto seco de cuerpo fructífero de Ganoderma lingzhi (reishi)
  Cantidad por cápsula: 500 mg de extracto
  DER nativo: 9:1 (materia prima seca : extracto seco)
  Extracción: agua caliente + etanol (dual), sin soportes añadidos
  Estandarizado a: β-glucano ≥ 25 % p/p base seca (método enzimático Megazyme K-YBGL)
  Aporte por cápsula: ≥ 125 mg de β-glucano
  Parte usada: cuerpo fructífero (fruiting body), 0 % micelio en grano
```

Todo lo que ahí aparece es **medible y auditable**. Eso es exactamente lo que hace la diferencia entre un
producto y una promesa. Nada de esa etiqueta afirma efecto sobre ninguna enfermedad — la parte de qué se
puede decir vive en `267`, `268` y `276`.

## Ejemplo aplicado (ILUSTRATIVO) — dos ofertas del mismo precio

| | Proveedor A | Proveedor B |
|---|---|---|
| Etiqueta | "Extracto 20:1" | "DER 8:1, β-glucano ≥ 30 % (Megazyme)" |
| β-glucano medido | 11,2 % p/p b.s. | 31,4 % p/p b.s. |
| α-glucano medido | 34,7 % p/p b.s. | 4,1 % p/p b.s. |
| Precio | USD 48/kg | USD 62/kg |
| Costo por gramo de β-glucano | 48 / (1000 × 0,112) = USD 0,43 | 62 / (1000 × 0,314) = USD 0,20 |

El "20:1 más barato" cuesta más del doble por gramo de lo que realmente compras, y su α-glucano alto grita
micelio en grano (`218`, `220`). El ratio grande era el disfraz.

## Errores comunes

- **Comparar ratios entre proveedores como si fueran potencia.** No lo son; compara mg de activo por gramo.
- **Calcular el DER en base húmeda.** Infla o desinfla el ratio según la humedad de cada lado (`07`).
- **No declarar el soporte.** Un extracto con 40 % de maltodextrina y DER "10:1" es en realidad un 6:1
  disfrazado; el DER nativo es el que cuenta.
- **Aceptar ratios que rompen el balance de masa.** Hazle siempre la cuenta al catálogo antes de comprar.
- **Poner el ratio en la etiqueta y nada más.** En una inspección, un número sin método es una afirmación
  sin respaldo.
- **Mezclar ratio con "equivalente a X mg de hongo".** Esa frase solo es válida si el DER es real, está
  documentado y el material de partida está identificado por especie.

## Conexión con otros módulos

→ `151-relacion-planta-extracto-y-ratios.md` — el concepto general de DER.
→ `152-estandarizacion-de-extractos.md` — estandarizar por marcador en vez de por ratio.
→ `218-el-fraude-del-micelio-en-grano.md` y `220-alfa-glucanos-y-almidon-el-confusor.md` — el fraude que el
ratio suele esconder.
→ `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — el catálogo completo de trampas.
→ `247-especificacion-de-producto-de-hongos.md` — dónde se fija todo esto por escrito.
→ `272-etiquetado-en-colombia.md` — qué exige la norma colombiana en la etiqueta.
