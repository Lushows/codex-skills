# 123 — Vías de administración (la misma molécula, resultados completamente distintos)

La misma cantidad del mismo compuesto puede no hacer nada por vía oral y hacer bastante por vía sublingual
o inhalada. La vía decide cuánto llega, cuándo llega y con cuánta variabilidad entre personas. Este módulo
compara las vías reales para un producto natural y te da los criterios para elegir la forma farmacéutica sin
copiar a la competencia. El error caro que evita: diseñar una gomita para un activo que se destruye en el
estómago, o vender un tópico prometiendo un efecto que solo se logra por vía sistémica.

Términos: **vía enteral (enteral route)** = pasa por el tracto digestivo (oral, sublingual con matices,
rectal). **Vía parenteral (parenteral route)** = no pasa por el digestivo (IV, IM, subcutánea, inhalada,
transdérmica). **Primer paso (first-pass)** = el filtro hepático descrito en `122`. **Latencia (onset)** =
tiempo hasta el inicio del efecto. **Duración (duration)** = cuánto se sostiene.

## Tabla comparativa

| Vía | Latencia típica | Duración típica | Primer paso | Variabilidad entre personas | Uso típico en producto natural |
|---|---|---|---|---|---|
| Oral (cápsula, tableta) | 30–120 min | horas | Sí, completo | Alta | Suplementos en general |
| Oral (líquido, gomita) | 20–90 min | horas | Sí, completo | Alta | Comestibles de cannabis |
| Sublingual / bucal | 5–30 min | horas | Parcial (lo que se absorbe en mucosa lo evita) | Media-alta | Tinturas, aceites |
| Inhalada (vapor) | segundos–minutos | 1–3 h | No | Media | Cannabis; riesgo propio (`197`) |
| Rectal | 10–30 min | horas | Parcial | Alta | Poco usado, mala aceptación |
| Transdérmica (parche) | horas | 12–72 h | No | Media | Requiere permeación real, difícil |
| Tópica (crema, ungüento) | minutos (local) | horas | No | Alta | Efecto **local**, no sistémico |
| Intranasal | 5–15 min | 1–3 h | No | Media | Poco usado en suplementos |
| Intravenosa | inmediata | según t½ | No, F = 100 % por definición | Baja | Solo investigación clínica |

Advertencia sobre las tinturas sublinguales: buena parte de lo que se pone bajo la lengua **se traga**.
La fracción realmente absorbida por mucosa suele ser menor de lo que el marketing sugiere, y depende del
vehículo, del tiempo de contacto y de si la persona salivó o no. Si vas a reclamar ventaja sublingual,
necesitas AUC comparativa (`122`).

## Lo que decide si una vía es viable

1. **Estabilidad en el medio.** ¿La molécula sobrevive a pH 1,5 del estómago? ¿A las proteasas? Los
   péptidos casi nunca; por eso la insulina no es oral.
2. **Tamaño y lipofilia.** Para transdérmica la regla práctica es < 500 Da y logP entre 1 y 3. Un
   β-glucano (decenas o cientos de kDa) no atraviesa piel intacta. Punto.
3. **Dosis necesaria.** Una vía puede ser ideal y aun así inviable si hay que entregar 2 g/día: no cabe en
   un parche ni en una gomita razonable.
4. **Irritación y tolerancia local.** Mucosa oral, nasal y piel tienen límites; los solventes y
   tensioactivos que solubilizan suelen irritar.
5. **Marco regulatorio.** En Colombia, la vía y la forma farmacéutica influyen en si el producto se
   clasifica como suplemento dietario o entra en otra categoría (ver `266`, `270`). A agosto de 2026,
   verificar la clasificación vigente con INVIMA antes de comprometer un desarrollo.

## Tópico ≠ sistémico

Es la confusión más frecuente y la más peligrosa comercialmente. Un tópico bien formulado puede tener efecto
**en la piel y tejidos inmediatamente subyacentes**. Que un compuesto tenga actividad `[in vitro]` no
significa que, aplicado en crema, llegue a una articulación profunda o a la sangre. Para afirmar acción
sistémica desde un tópico hace falta demostrar concentración plasmática, y casi ningún producto natural
tópico del mercado lo ha hecho. Si el estudio no existe, el lenguaje se queda en la piel — literalmente.

## Cómo se comprueba

| Pregunta | Método | Unidad | Nivel |
|---|---|---|---|
| ¿Sobrevive al estómago? | Estabilidad en fluido gástrico simulado (SGF, pH 1,2) 2 h + HPLC | % remanente | `[in vitro]` |
| ¿Se libera del vehículo? | Disolución USP aparato 2 | % liberado vs tiempo | `[in vitro]` |
| ¿Atraviesa piel? | Celda de Franz con piel humana o porcina | µg/cm²/h (flujo) | `[in vitro]` |
| ¿Atraviesa mucosa oral? | Modelo de mucosa bucal reconstituida | Papp (cm/s) | `[in vitro]` |
| ¿Llega a sangre? | PK humana con LC-MS/MS | Cmax, AUC | `[clínico fase 1]` |

## Ejemplo aplicado — decidir la forma de un producto de hongos

BIO-SETA evalúa tres presentaciones para un extracto de reishi con β-glucano 28 % p/p base seca
**(ILUSTRATIVO)** y dosis objetivo de 1.500 mg de extracto/día:

| Opción | Viabilidad | Razón química |
|---|---|---|
| Cápsula 500 mg × 3 | Alta | Cabe, es estable, la vía oral es coherente con un mecanismo intestinal/inmune local (`130`) |
| Tintura sublingual | Baja | 1.500 mg de polisacárido no se solubilizan ni se absorben por mucosa; volumen inviable |
| Crema tópica | Nula para el mecanismo declarado | Polímero grande no permea piel; sería otro producto con otro claim |

Decisión: cápsula. Y el argumento comercial no es "absorción superior" —que sería falso— sino dosis
verificada por COA y trazabilidad de especie por ITS (`245`). Eso sí se sostiene en una auditoría.

## Errores comunes

- Vender un tópico con lenguaje de efecto sistémico. Es el error con más riesgo regulatorio y sanitario.
- Elegir sublingual por moda cuando la molécula ni se solubiliza ni permea mucosa.
- Ignorar la degradación gástrica y lanzar una forma oral de un activo lábil sin recubrimiento entérico.
- Comparar latencias entre vías sin decir la vía: "actúa en 10 minutos" carece de sentido sin contexto.
- Diseñar un parche para una dosis que no cabe físicamente en un parche.
- Suponer que lo sublingual evita el primer paso al 100 %. Buena parte se traga.

## Conexión con otros módulos

→ `122-biodisponibilidad-y-efecto-de-primer-paso.md` — cuánto llega por cada vía.
→ `153-formas-farmaceuticas-panorama.md` — el catálogo de formas y cuándo usar cada una.
→ `196-topicos-y-transdermicos.md` — el detalle de piel y permeación.
→ `197-vapeo-quimica-y-riesgos.md` — la vía inhalada y sus riesgos propios.
→ `161-dosis-y-tamano-de-porcion.md` — de la dosis diaria a la unidad que se vende.
