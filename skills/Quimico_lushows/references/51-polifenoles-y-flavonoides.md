# 51 — Polifenoles y flavonoides (los "antioxidantes" que casi todo el mundo mide mal)

Los polifenoles son la familia detrás de la palabra más usada y peor sustentada del mercado de suplementos:
"antioxidante". Están en cannabis (flavonoides y cannflavinas), en hongos (ácidos fenólicos, y en chaga un
complejo polifenólico-melanínico), en frutas y en el té. El problema no es que no existan: es que se miden
con métodos inespecíficos —Folin-Ciocalteu, DPPH— cuyo resultado se presenta como si fuera contenido de un
activo. Este módulo te enseña la química, qué mide de verdad cada método, y cómo pasar de un número
comparativo a un dato defendible.

Términos: **polifenol (polyphenol)** = compuesto con varios grupos fenólicos (-OH sobre anillo aromático).
**Flavonoide (flavonoid)** = polifenol con esqueleto C6-C3-C6. **Aglicona (aglycone)** = el flavonoide sin
el azúcar. **Glicósido (glycoside)** = aglicona + azúcar; es la forma en que suelen estar en la planta.
**Capacidad antioxidante (antioxidant capacity)** = medida funcional *in vitro* de neutralizar radicales; NO
es contenido de una sustancia.

## Mapa de la familia

| Subclase | Esqueleto | Ejemplos | Dónde |
|---|---|---|---|
| Ácidos fenólicos (hidroxibenzoicos) | C6-C1 | Ácido gálico, protocatéquico | Hongos, plantas |
| Ácidos hidroxicinámicos | C6-C3 | Ácido cafeico, clorogénico, ferúlico | Café, hongos |
| **Flavonas** | C6-C3-C6 | Apigenina, luteolina, **cannflavinas A/B** | Cannabis |
| Flavonoles | C6-C3-C6 + OH en C3 | Quercetina, kaempferol, rutina | Plantas |
| Flavanonas | C6-C3-C6 sin C2=C3 | Naringenina, hesperidina | Cítricos |
| Flavanoles (catequinas) | C6-C3-C6 | EGCG, catequina | Té |
| Antocianinas | Catión flavilio | Cianidina | Frutos rojos |
| Estilbenos | C6-C2-C6 | Resveratrol | Uva |
| Lignanos y taninos | Polímeros | Taninos condensados | Corteza, chaga |

**Cannabis:** las **cannflavinas A y B** son prenilflavonas propias del cannabis; se han reportado como
inhibidoras de mediadores inflamatorios [in vitro]. A agosto de 2026 no hay evidencia clínica que soporte
ningún claim, y cualquier afirmación de tratamiento sería un claim de enfermedad (`184`, `268`).

**Chaga (*Inonotus obliquus*):** su color negro es un complejo **melanínico-polifenólico**; muchas fichas
comerciales lo reportan como "polifenoles totales" por Folin, que es exactamente el método más inespecífico
posible para esa matriz (`229`, `56`).

## Química que explica su comportamiento

- El **fenol es ácido débil** (pKa ~9–10). A pH alcalino se ioniza a fenolato, que se oxida rapidísimo: por
  eso los extractos alcalinos se ponen pardos en minutos (`44`, `47`).
- **Quelan metales**: los catecoles (dos OH vecinos) forman complejos con Fe³⁺ y Cu²⁺. Eso da color y
  también explica su capacidad antioxidante indirecta (quelato = corta la iniciación radicalaria).
- **Absorben fuerte en UV**: bandas típicas ~250–290 nm (banda II) y ~320–380 nm (banda I) en flavonoides.
  Por eso se ven muy bien en HPLC-DAD (`80`).
- **La glicosilación cambia todo**: el glicósido es más soluble en agua, menos absorbible y eluye antes en
  C18 que su aglicona. Para comparar contra un patrón de aglicona hay que hidrolizar (`46`).

## Los métodos y qué mide realmente cada uno

| Método | Qué mide de verdad | Unidad | ¿Sirve para etiquetar? |
|---|---|---|---|
| **Folin-Ciocalteu** | Capacidad reductora total: reacciona con fenoles **y** con azúcares reductores, ácido ascórbico, aminas, proteínas | mg equivalentes de ácido gálico (GAE)/g | **No.** Comparativo interno solamente |
| **DPPH** | Neutralización de un radical sintético en solvente orgánico | IC₅₀ (mg/mL) o µmol Trolox eq/g | No. Es *in vitro*, no fisiológico |
| **ABTS/TEAC** | Similar, radical distinto, tolera acuoso | µmol Trolox eq/g | No |
| **ORAC** | Capacidad frente a radicales peroxilo | µmol Trolox eq/g | No; la FDA retiró su base de datos ORAC en 2012 por mal uso |
| **FRAP** | Poder reductor férrico | µmol Fe²⁺ eq/g | No |
| **HPLC-DAD con patrón** | **Un compuesto específico, cuantificado** | mg/g o % p/p base seca | **Sí** |
| **LC-MS/MS** | Compuestos específicos a trazas | µg/g | Sí |

La frase que hay que decirle a un proveedor y a un cliente: *"Folin no mide polifenoles; mide todo lo que
reduzca el reactivo. Si quieres declarar un número en la etiqueta, necesitas HPLC con patrón del compuesto
que declaras."* Es la misma lógica de "polisacáridos totales" en hongos (`222`).

## Cómo se mide bien: el método por HPLC

```
Esquema general (ILUSTRATIVO — validar en tu matriz, `75`):
  1. Muestra seca y molida, humedad conocida (`07`, `67`)
  2. Extracción: metanol o etanol acuoso 70 % v/v, ultrasonido 30 min, 2 ciclos
     (para agliconas: hidrólisis ácida previa, HCl 1,2 M en metanol 50 %, 80 °C, 2 h)
  3. Filtrar 0,22 µm, diluir
  4. HPLC-DAD, columna C18 150 × 4,6 mm 3,5 µm, gradiente agua+0,1 % ácido fórmico / acetonitrilo
  5. Detección: 280 nm (ácidos fenólicos), 320 nm (hidroxicinámicos), 360 nm (flavonoles)
  6. Curva de 5–6 puntos con patrón certificado de CADA analito declarado (`71`)

Reporte: "Quercetina 0,42 mg/g base seca; ácido protocatéquico 0,18 mg/g base seca; HPLC-DAD 360/280 nm,
patrones certificados; LOQ 0,02 mg/g." ← esto sí sostiene una especificación.
```

## Ejemplo aplicado — comparar dos extractos de chaga

```
Proveedor A: "Polifenoles totales 12,4 % (Folin, GAE)"   Precio X
Proveedor B: "Polifenoles totales 4,1 % (Folin, GAE)"    Precio 1,4 X

Lectura ingenua: A es tres veces mejor y más barato.
Lectura química:
  · Folin reacciona con azúcares reductores. Si A tiene más azúcar residual del sustrato, infla el número.
  · Ninguno declara β-glucano ni α-glucano (`221`, `220`), ni identidad de especie por ITS (`245`).
  · Ninguno declara un compuesto específico cuantificado por HPLC.
Datos que hay que exigir para decidir:
  1. β-glucano y α-glucano, % p/p base seca, Megazyme K-YBGL
  2. Identidad por ITS y origen (chaga silvestre sobre abedul vs cultivo)
  3. Un marcador específico por HPLC (p. ej. derivados del ácido protocatéquico o betulina, `60`)
  4. Metales pesados y **oxalato**, que en chaga es un riesgo real y documentado (`230`)
  5. Humedad, para comparar en la misma base
Sin esos cinco, la comparación de precio no significa nada.
```

## Lo que sí y lo que no se puede decir

- **Sí:** "contiene compuestos fenólicos, cuantificados en X mg/g base seca por HPLC".
- **Sí:** "en ensayos *in vitro* (DPPH) el extracto mostró capacidad de neutralizar radicales, con IC₅₀ de
  X mg/mL" — describiendo el ensayo y su naturaleza [in vitro].
- **No:** "antioxidante que protege tus células", "combate el envejecimiento", "reduce la inflamación". Son
  claims funcionales o de enfermedad sin soporte, y en Colombia caen bajo el Decreto 3249 de 2006 y la
  vigilancia del INVIMA (`267`, `268`).
- Un valor ORAC alto **no** predice efecto en humanos: la biodisponibilidad de la mayoría de polifenoles es
  baja y el metabolismo de fase II los transforma antes de que lleguen a ningún lado (`125`).

## Errores comunes

- Declarar en etiqueta un valor Folin como si fuera contenido de polifenoles. Es el error #1 de la categoría.
- Comparar valores DPPH entre laboratorios: dependen del solvente, del tiempo de reacción y de la
  concentración de DPPH. Solo valen dentro de la misma corrida.
- No hidrolizar los glicósidos y luego reportar "quercetina baja": estaba como rutina.
- Extraer con agua caliente prolongada y oxidar los fenoles antes de medirlos.
- Presentar µmol Trolox equivalente como si fuera una dosis. No lo es: no hay dosis-respuesta humana detrás.
- Ignorar que el color oscuro también viene de Maillard y de melaninas, no solo de polifenoles (`62`, `56`).

## Conexión con otros módulos

→ `133-estres-oxidativo-y-antioxidantes.md` — qué significa "antioxidante" en fisiología, con evidencia.
→ `91-metodos-colorimetricos-y-enzimaticos.md` — los métodos colorimétricos y sus límites.
→ `56-quinonas-y-pigmentos.md` — qué pasa cuando el fenol se oxida.
→ `59-ruta-del-shikimato-y-policetidos.md` — de dónde vienen los fenoles.
→ `268-claims-prohibidos-el-caso-bioseta.md` — qué se puede decir en Colombia.
