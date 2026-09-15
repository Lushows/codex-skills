# 244 — Micotoxinas y contaminación en hongos (el hongo bueno no produce la toxina; el que llegó de colado, sí)

Aquí hay una confusión que cuesta lotes: las micotoxinas relevantes en un suplemento de hongos **no las
produce el hongo que cultivas**, las producen mohos contaminantes (*Aspergillus*, *Penicillium*,
*Fusarium*) que llegan al sustrato, al grano o al producto mal secado. Por eso el control de micotoxinas en
hongos es en el fondo un control de humedad, sustrato y almacenamiento — y por eso los productos de micelio
sobre grano tienen un riesgo estructuralmente más alto que un cuerpo fructífero bien secado.

Términos: **micotoxina (mycotoxin)** = metabolito tóxico producido por ciertos mohos. **aflatoxinas
(aflatoxins B1, B2, G1, G2)** = las más reguladas, producidas por *Aspergillus flavus/parasiticus*.
**ocratoxina A (OTA)** = otra micotoxina común en granos. **aw (water activity)** = agua disponible; por
debajo de 0,70 los mohos no crecen.

## De dónde viene el riesgo

| Fuente | Riesgo | Por qué |
|---|---|---|
| Grano del sustrato (arroz, sorgo, avena) | Alto | Los granos traen esporas de *Aspergillus* y *Fusarium* de campo |
| Micelio sobre grano (MOG) que se muele con el grano | Alto | El grano contaminado se va entero al producto |
| Secado lento o al aire libre | Alto | El material pasa horas en la ventana de aw favorable al moho |
| Almacenamiento con humedad > 10 % o aw > 0,70 | Alto | El moho crece en bodega |
| Cuerpo fructífero bien secado y bien envasado | Bajo | Se sale de la ventana de crecimiento |
| Chaga y silvestres | Variable | Depende de recolección y secado en campo |

Punto clave que el sector no dice en voz alta: si el producto es micelio cultivado sobre grano y el grano
va al polvo final, estás vendiendo cereal fermentado — con el perfil de riesgo de un cereal (`218`).

## Límites de referencia — a agosto de 2026

| Marco | Analito | Orden de magnitud del límite |
|---|---|---|
| Unión Europea | Aflatoxina B1 en alimentos/ingredientes vegetales | Unidades de µg/kg (típicamente 2–5 µg/kg) |
| Unión Europea | Aflatoxinas totales | Típicamente 4–10 µg/kg |
| Unión Europea | Ocratoxina A | Unidades de µg/kg según categoría |
| Colombia | Resolución de contaminantes del Minsalud + criterio INVIMA | Se fija en el expediente |
| EE.UU. | FDA action level para aflatoxinas totales en alimentos | 20 µg/kg (ppb) |

**Verificación obligatoria:** los valores europeos vigentes están en el Reglamento (UE) 2023/915 y sus
enmiendas; los de EE.UU. en las guías de niveles de acción de FDA; en Colombia se revisan con Minsalud e
INVIMA al momento del registro. Esta tabla es orientación fechada, no norma certificada (`265`, `266`).

## Microbiología: el otro control del mismo problema

Micotoxinas y microbiología van juntas en el plan de control, porque comparten causa raíz (agua):

| Ensayo | Método típico | Para qué |
|---|---|---|
| Recuento total aerobios mesófilos | ISO 4833 / USP <61> | Higiene general del proceso |
| Mohos y levaduras | ISO 21527 / USP <61> | Detecta la contaminación que produce toxina |
| *E. coli* / coliformes | ISO 16649 | Contaminación fecal, agua de proceso |
| *Salmonella* (ausencia/25 g) | ISO 6579 | Requisito casi universal |
| *S. aureus* | ISO 6888 | Manipulación |

Ojo con un detalle específico de hongos: los ensayos de **mohos y levaduras dan positivo por el propio
hongo** si el material no está bien inactivado o si el laboratorio no entiende la matriz. Hay que acordar el
criterio con el laboratorio antes de correr la muestra, o vas a rechazar lotes buenos.

## Cómo se mide / cómo se comprueba

| Paso | Detalle |
|---|---|
| Muestreo | Es lo más crítico: las micotoxinas se distribuyen en "puntos calientes". Muestra compuesta de muchos incrementos (`66`) |
| Extracción | Metanol/agua o acetonitrilo/agua; limpieza por columna de inmunoafinidad o QuEChERS (`69`) |
| Medición | **LC-MS/MS en modo MRM** es el estándar actual: multi-micotoxina en una corrida (`83`, `101`) |
| Alternativa | HPLC con detección de fluorescencia y derivatización post-columna (solo aflatoxinas) |
| Tamizaje | ELISA rápido en recepción de materia prima; confirmar positivos por LC-MS/MS |
| LOQ esperable | 0,1–1 µg/kg por analito con LC-MS/MS |
| Laboratorio | Acreditado ISO/IEC 17025 para micotoxinas en esa matriz (`107`) |

## Ejemplo aplicado (ILUSTRATIVO) — dos proveedores, mismo precio

```
Proveedor A — "extracto de melena de león" (micelio sobre arroz, no declarado)
  Aflatoxinas totales: 6,4 µg/kg     Mohos y levaduras: 4,2 × 10³ UFC/g
  α-glucano: 41 % p/p b.s.  ← el arroz que trae la toxina es el mismo que trae el almidón

Proveedor B — extracto de cuerpo fructífero, secado a 50 °C, aw 0,42
  Aflatoxinas totales: < 1,0 µg/kg (LOQ)   Mohos y levaduras: < 100 UFC/g
  α-glucano: 3,8 % p/p b.s.
```

Lectura: el mismo análisis que delata el fraude de composición (α-glucano alto) explica el riesgo
toxicológico. No son dos problemas, es uno solo con dos caras.

## Errores comunes

- **Analizar micotoxinas una vez y nunca más.** Es un parámetro de lote, no de "una vez al año", sobre todo
  si compras a varios proveedores.
- **Muestrear un puñado del centro del saco.** La distribución en puntos calientes hace que un muestreo malo
  dé un falso negativo casi garantizado.
- **Pedir "aflatoxinas" y olvidar ocratoxina A.** En granos la OTA es tan frecuente como las aflatoxinas.
- **Confundir el conteo de mohos con contaminación cuando la matriz es un hongo.** Define el criterio con el
  laboratorio antes.
- **Creer que el secado mata la toxina.** El moho muere; la micotoxina es termoestable y se queda.
- **No controlar aw en bodega.** La contaminación puede nacer después del análisis de liberación.

## Conexión con otros módulos

→ `101-analisis-de-micotoxinas.md` — el método analítico completo.
→ `100-microbiologia-de-producto.md` — el panel microbiológico y sus criterios.
→ `35-actividad-de-agua-y-humedad.md` — la variable que controla todo esto.
→ `218-el-fraude-del-micelio-en-grano.md` — por qué el grano es el vector.
→ `240-secado-y-perdida-de-activos.md` — el secado como control preventivo.
→ `247-especificacion-de-producto-de-hongos.md` — los límites en tu especificación.
