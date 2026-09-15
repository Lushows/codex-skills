# 246 — Adulteración y fraude en suplementos de hongos (el catálogo completo y cómo se detecta cada uno)

Este es probablemente el módulo más útil de todo el bloque de hongos, porque el mercado de suplementos de
hongos es uno de los más adulterados que existen: la materia prima es un polvo café, el consumidor no puede
verificar nada, y los ensayos baratos que se usan como "prueba de calidad" están diseñados —a veces
deliberadamente— para no detectar el fraude. Aquí está el catálogo de las trampas reales, cada una con el
análisis exacto que la desnuda y con lo que cuesta hacerlo.

Términos: **MOG (mycelium on grain)** = micelio cultivado sobre grano y molido junto con el grano.
**α-glucano (alpha-glucan)** = almidón, principalmente; marcador de grano. **β-glucano (beta-glucan)** =
el polisacárido característico de la pared fúngica. **spiking** = añadir un compuesto puro para inflar un
resultado. **fingerprinting** = huella instrumental (NMR, LC-QToF) que compara perfiles completos.

## El catálogo de fraudes

| # | Fraude | Cómo se ve en la etiqueta | Cómo se detecta | Método / costo aprox. |
|---|---|---|---|---|
| 1 | **Micelio sobre grano vendido como hongo** | "Mushroom powder", "full spectrum", "US grown" | α-glucano alto (30–60 %) y β-glucano bajo (1–8 %) | Megazyme K-YBGL · USD 80–150 |
| 2 | **"Polisacáridos totales 40 %"** | Suena a beta-glucano | El ensayo mide también almidón; se pide β y α por separado | Megazyme vs fenol-sulfúrico · `222` |
| 3 | **Spiking con β-glucano de levadura o avena** | "≥ 50 % beta-glucanos" | Ratio β-1,3/1,6 y perfil de enlace por metilación o NMR; balance de masa imposible | NMR / análisis de enlaces · USD 300–800 |
| 4 | **Sustitución de especie** | "Reishi" que es *G. applanatum* | ITS + filogenia | Sanger ITS · USD 60–150 · `245` |
| 5 | **Chaga "extracto" que es grano fermentado** | "Chaga extract 10:1" | NMR fingerprint y LC-QToF muestran perfil de grano, no de esclerocio silvestre (estudio 2025) | NMR/LC-QToF · USD 400+ |
| 6 | **Ratio inflado (20:1 que no existe)** | "20:1", "50:1" | Balance de masa contra el activo; auditoría del registro de lote | Cálculo + auditoría · `242` |
| 7 | **Maltodextrina no declarada** | "Extracto puro" | α-glucano alto sin grano visible; azúcares reductores; DP por HPAEC | Megazyme + HPLC · USD 150 |
| 8 | **COA de otro lote** | Todo perfecto y siempre igual | Número de lote, fecha y firma no cuadran; valores idénticos entre lotes | Lectura crítica · `110`, `111` |
| 9 | **COA de un laboratorio no acreditado o del propio proveedor** | Logo bonito, sin alcance | Verificar la acreditación ISO 17025 y el alcance del método | Consulta al organismo · `107` |
| 10 | **Lab shopping** | Solo muestran el COA bueno | Pedir todos los COA del año y las no conformidades | Auditoría · `113` |
| 11 | **Cordicepina "de Cordyceps sinensis"** | Muy común | *C. sinensis* silvestre casi no se comercializa; medir cordicepina por HPLC (suele ser < LOQ) | HPLC-DAD · USD 120 · `228` |
| 12 | **Triterpenos declarados en extracto acuoso** | "Reishi dual" | HPLC de triterpenos: salen < 5 mg/g | HPLC-DAD · `224` |
| 13 | **Hericenonas/erinacinas sin cuantificar** | "Con hericenonas" | Pedir método y valor; casi nadie los mide de verdad | HPLC/LC-MS · `226` |
| 14 | **Metales o micotoxinas no analizados** | No aparecen en el COA | Pedirlos; si no existen, el lote no está liberado | ICP-MS, LC-MS/MS · `243`, `244` |
| 15 | **"Orgánico" sin certificado** | Sello genérico | Pedir número de certificado y verificarlo en el ente certificador | Verificación documental |

## La prueba de dos números que resuelve el 80 % de los casos

Si solo puedes pagar un análisis, paga **β-glucano y α-glucano por el mismo kit enzimático**, en base seca.

```
Interpretación práctica (rangos orientativos de la literatura del sector; verifica con tu lote):

  Cuerpo fructífero real, seco:      β 20–40 % p/p b.s.   ·  α 1–8 %
  Extracto acuoso de fructífero:     β 25–45 % p/p b.s.   ·  α 2–10 %
  Micelio sobre grano (MOG):         β 1–8 %  p/p b.s.    ·  α 30–60 %  ← el grano
  Producto con maltodextrina:        β variable            ·  α alto sin declararlo
```

Reportes independientes del sector (Nammex y auditorías de mercado publicadas entre 2024 y 2026) describen
justamente ese patrón en productos MOG: almidón alto y beta-glucano de un dígito. Trátalo como **evidencia
de sector, no como norma**: la conclusión se toma sobre tu propio COA.

## Cómo se comprueba, en orden de costo

1. **Gratis:** leer el COA con lupa (`110`, `111`). Método, laboratorio, lote, fecha, unidades, base.
2. **Gratis:** hacer el balance de masa del ratio contra el activo (`242`). Muchos fraudes mueren aquí.
3. **Barato (USD ~100–200):** β-glucano y α-glucano por Megazyme, en base seca, en un laboratorio tuyo.
4. **Medio (USD ~60–150):** ITS para identidad de especie (`245`).
5. **Medio (USD ~120–300):** el marcador específico de tu claim (triterpenos, cordicepina, ergotioneína).
6. **Alto (USD ~400+):** fingerprint por NMR o LC-QToF cuando sospechas sustitución sofisticada o spiking.

El punto: **nunca aceptes el COA del vendedor como única evidencia**. El COA del proveedor es un documento
comercial; el COA de tu laboratorio es un control de calidad.

## Ejemplo aplicado (ILUSTRATIVO) — auditoría de 4 lotes de "reishi 10:1"

| Lote | β-glucano | α-glucano | ITS | Triterpenos | Veredicto |
|---|---|---|---|---|---|
| A | 31,2 % b.s. | 3,9 % | *G. lingzhi* 99,7 % | 18,4 mg/g | Conforme |
| B | 6,1 % | 44,8 % | *G. lingzhi* 99,5 % | 2,1 mg/g | MOG disfrazado |
| C | 52,7 % | 2,1 % | *G. lingzhi* 99,6 % | 1,8 mg/g | Sospecha de spiking con β-glucano de levadura |
| D | 28,9 % | 5,2 % | *G. applanatum* | 9,7 mg/g | Especie equivocada |

Fíjate en C: el número **más alto** es el más sospechoso. Con una materia prima de ~30 % de β-glucano y un
DER de 10:1, un extracto al 52,7 % es posible en teoría pero exige una recuperación irreal; combinado con
triterpenos casi nulos, apunta a adición externa. Aquí es donde vale el NMR.

## Errores comunes

- **Comprar por precio por kilo.** Compra por **costo por gramo de activo** — la aritmética cambia todo.
- **Creer que el sello "GMP" del proveedor prueba composición.** GMP habla del proceso, no del contenido.
- **Pedir un solo análisis y no repetirlo.** El fraude aparece cuando cambian de lote o de subproveedor.
- **Aceptar "full spectrum" como categoría técnica.** No lo es: es lenguaje de marketing para incluir grano.
- **No guardar contramuestra de cada lote.** Sin contramuestra no puedes impugnar nada (`112`).
- **No poner las especificaciones en el contrato de compra.** Sin límite escrito, no hay incumplimiento.

## Conexión con otros módulos

→ `218-el-fraude-del-micelio-en-grano.md` — el fraude central del sector, en detalle.
→ `220-alfa-glucanos-y-almidon-el-confusor.md` y `222-polisacaridos-totales-por-que-no-sirve.md`.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el método que decide.
→ `245-identidad-de-especie-por-its.md` — sustitución de especie.
→ `111-banderas-rojas-en-un-coa.md` y `113-lab-shopping-e-inflacion-de-potencia.md`.
→ `247-especificacion-de-producto-de-hongos.md` — cómo blindarte por contrato.
