# 182 — Terpenos del cannabis: lo que el cliente huele y el proceso destruye

Los terpenos son los compuestos volátiles que le dan el olor y el sabor al cannabis. Comercialmente valen
mucho: son la primera cosa que evalúa un comprador de flor y lo que diferencia un extracto de otro. Y son,
al mismo tiempo, lo más frágil del material: hierven bajo, se evaporan con el secado, se pierden en el
rotavapor y se degradan con la luz. Este módulo te da la química, los rangos que se ven en la vida real, y
cómo medirlos sin engañarte. El error caro es formular "sabor" comprando terpenos botánicos genéricos y
declararlos como "terpenos de cannabis" en la etiqueta.

Términos:
- **terpeno (terpene)** = hidrocarburo construido con unidades de isopreno (C5). Monoterpeno = C10;
  sesquiterpeno = C15. Ver `49`.
- **terpenoide (terpenoid)** = terpeno oxigenado (alcohol, óxido, cetona).
- **volátil (volatile)** = de presión de vapor alta; se evapora fácil.
- **headspace (HS)** = la técnica que muestrea el vapor sobre la muestra, no la muestra (ver `86`).
- **terpeno botánico (botanical terpene)** = el mismo compuesto obtenido de otra planta (limoneno de
  cítricos, mirceno de lúpulo).

## Los que de verdad importan

| Terpeno | Tipo | Punto de ebullición (°C, 1 atm) | Aroma | Presencia típica |
|---|---|---|---|---|
| β-mirceno | Mono | ~167 | Terroso, herbal | El más abundante en muchas variedades |
| D-limoneno | Mono | ~176 | Cítrico | Muy común |
| α-pineno / β-pineno | Mono | ~155 / ~166 | Pino | Común |
| Linalool | Monoterpenoide | ~198 | Floral, lavanda | Frecuente |
| Terpinoleno | Mono | ~187 | Fresco, complejo | Marcador de ciertos quimiovares |
| Ocimeno | Mono | ~177 | Dulce, herbal | Variable |
| **β-cariofileno** | Sesqui | ~262 | Pimienta | Muy común; ligando de CB2 [in vitro] |
| α-humuleno | Sesqui | ~275 | Lúpulo | Acompaña al cariofileno |
| Óxido de cariofileno | Sesquiterpenoide | ~280 | Amaderado | Producto de oxidación; marcador de envejecimiento |
| Bisabolol | Sesquiterpenoide | ~314 | Dulce, manzanilla | Menos frecuente |
| Nerolidol | Sesquiterpenoide | ~276 | Amaderado, floral | Menos frecuente |

Los puntos de ebullición son valores de literatura a presión atmosférica y explican la jerarquía de pérdida:
**los monoterpenos se van primero**. Por eso una flor mal secada huele a heno y un extracto destilado huele
a nada.

El contenido total de terpenos en flor seca de buena calidad se reporta en literatura típicamente entre
**~0,5 y 3 % p/p base seca** (`5–30 mg/g`), con casos excepcionales por encima. **Verifica con tu lote.**
Cualquier proveedor que te ofrezca flor con "8 % de terpenos" está reportando mal o mintiendo.

## Dónde se pierden

| Etapa | Pérdida relativa | Por qué |
|---|---|---|
| Secado a temperatura alta o con aire forzado | Alta | Volatilidad; ver `186` |
| Curado prolongado sin control | Media | Evaporación lenta y oxidación |
| Descarboxilación (`174`) | **Muy alta** en monoterpenos | 100–140 °C está por encima de sus puntos de ebullición |
| Evaporación de solvente / rotavapor | Alta | Se van con el solvente |
| Destilación de cannabinoides (`192`) | Prácticamente total | Por eso el destilado es inodoro |
| Rosin prensado en frío (`190`) | Baja | Es la gran ventaja del solventless |

El β-cariofileno y los sesquiterpenos sobreviven más que los monoterpenos, así que el perfil no solo se
empobrece: **se distorsiona**. Un extracto procesado tiene relación sesqui/mono mucho más alta que la flor de
origen. Eso es una firma auditable.

## El β-cariofileno, con nivel de evidencia

El β-cariofileno es un sesquiterpeno dietético que se une al receptor CB2 [in vitro] — es la razón por la
que se le llama "cannabinoide dietético". Es un hallazgo farmacológico interesante y bien reportado; **no es
un claim de salud** y no se traduce en un efecto clínico demostrado en producto. Ver `183` para la discusión
honesta del efecto séquito.

## Cómo se mide / cómo se comprueba

- **Técnica de referencia: GC-FID o GC-MS**, con **headspace** o inyección de dilución en solvente. El HPLC
  no sirve: los terpenos no absorben bien en UV y son volátiles (`85`, `86`, `199`).
- **Preparación:** la muestra debe manipularse **fría y rápido**. Moler en caliente antes de muestrear es
  destruir el analito que vas a medir.
- **Patrones:** mezcla certificada de terpenos, mínimo los 15–21 habituales, con estándar interno (`72`).
- **Unidad:** `mg/g` o `% p/p`, con base declarada. `1 % p/p = 10 mg/g`.
- **LOQ por analito.** Muchos terpenos aparecen cerca del LOQ y "ND" sin LOQ no informa (`73`).
- **Autenticidad de origen (cannabis vs botánico):** el análisis rutinario **no** distingue un limoneno de
  cítrico de uno de cannabis: es la misma molécula. Se distingue por (a) el **perfil completo** —una mezcla
  de cannabis tiene una huella de coocurrencia difícil de imitar— y (b) análisis de **relación isotópica**
  (IRMS), caro y poco disponible. En la práctica, la trazabilidad documental es tu prueba (`285`, `104`).

## Ejemplo aplicado

Mismo lote, tres productos (ILUSTRATIVO, GC-MS headspace, `mg/g`):

| Terpeno | Flor seca | Rosin prensado en frío | Destilado |
|---|---|---|---|
| β-mirceno | 6,8 | 4,1 | < 0,05 |
| D-limoneno | 3,2 | 2,0 | < 0,05 |
| α-pineno | 1,4 | 0,7 | < 0,05 |
| Linalool | 0,9 | 0,6 | < 0,05 |
| β-cariofileno | 2,6 | 2,3 | 0,12 |
| α-humuleno | 0,8 | 0,7 | 0,04 |
| **Total** | **15,7 mg/g (1,57 %)** | **10,4 mg/g (1,04 %)** | **0,16 mg/g** |
| Relación sesqui/mono | 0,28 | 0,42 | > 3 |

Lectura: el rosin conserva **66 %** de los terpenos totales de la flor; el destilado, prácticamente nada. Y
la relación sesqui/mono delata el nivel de proceso. Si alguien te vende "destilado con terpenos de cannabis"
y el perfil se ve como la columna de la flor, es porque **se los volvieron a agregar** — lo cual es legítimo
si se declara, y fraude si se presenta como natural del proceso.

## Errores comunes

- Reportar "terpenos totales" sin desglose. El total no dice nada; el perfil sí.
- Medir terpenos por HPLC. No es la técnica.
- Moler y calentar la muestra antes de muestrear para terpenos.
- Declarar "terpenos de cannabis" cuando se usaron botánicos. Químicamente indistinguibles, legalmente no.
- Prometer efectos por terpeno individual ("el mirceno relaja"). Ver `183`: la evidencia clínica no lo
  sostiene.
- Comparar contenido de terpenos entre COA sin ver la base ni el método de preparación.
- Envasar en plástico permeable: los terpenos migran al envase y se pierden (`163`).

## Conexión con otros módulos

→ `49-terpenos-y-terpenoides.md` — la química general de la familia.
→ `183-efecto-sequito-que-dice-la-evidencia.md` — lo que se puede y no se puede afirmar.
→ `186-cosecha-secado-y-curado.md` — dónde se conservan o se pierden.
→ `190-solventless-rosin-y-hash.md` — el proceso que mejor los preserva.
→ `192-destilacion-de-cannabinoides.md` — el proceso que los elimina.
→ `199-analisis-de-perfil-de-terpenos.md` — el método completo, paso a paso.
→ `197-vapeo-quimica-y-riesgos.md` — qué pasa cuando se calientan para inhalar.
