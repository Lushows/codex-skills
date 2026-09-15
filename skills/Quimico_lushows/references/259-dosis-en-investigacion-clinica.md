# 259 — Dosis usadas en investigación clínica (información científica, no una guía de uso)

**ADVERTENCIA EXPLÍCITA, LEER ANTES DE SEGUIR.** Este módulo describe qué dosis se han administrado en
**protocolos de investigación clínica publicados**, con psilocibina sintética de grado farmacéutico, en
personas seleccionadas por criterios estrictos de seguridad (`260`), bajo supervisión médica presencial
durante 6 a 8 horas, con monitoreo cardiovascular y con equipo entrenado para manejar reacciones agudas.
**Esto no es una guía de uso, ni una recomendación, ni una referencia para calcular dosis fuera de un
protocolo autorizado.** Fuera de ese marco, la información de dosis no es transferible: el material natural
tiene una variabilidad de contenido que hace imposible administrar una dosis conocida (`254`), y en casi
todos los países el manejo de la sustancia está prohibido (`263`).

Términos: **dosis fija (fixed dose)** = la misma cantidad en mg para todos. **dosis ajustada por peso
(weight-adjusted dose)** = mg/kg. **dosis alta (high dose)** en la literatura del campo = la que produce
efectos psicodélicos completos. **dosis baja activa (low active dose)** = la que produce efectos perceptibles
pero no plenos; se usa como comparador activo.

## Las dos escuelas: dosis fija y mg/kg

| Escuela | Cómo dosifica | Ejemplos de programa | Racional |
|---|---|---|---|
| Dosis fija | mg totales iguales para todos | Compass Pathways (COMP360): 1 mg, 10 mg, 25 mg | Simplicidad clínica; la evidencia de que el peso explique la respuesta es débil |
| Ajustada por peso | mg/kg de peso corporal | Programa de Johns Hopkins: ~0,2–0,43 mg/kg | Tradición farmacológica clásica |

Equivalencia aproximada entre ambas, para leer la literatura:

```
Persona de 70 kg (ILUSTRATIVO, solo para comparar escalas de la literatura):
  0,215 mg/kg × 70 kg = 15,1 mg
  0,300 mg/kg × 70 kg = 21,0 mg
  0,430 mg/kg × 70 kg = 30,1 mg
Por eso "25 mg fijos" y "0,3 mg/kg" se mueven en el mismo territorio para un adulto promedio.
Cualquier conversión se ejecuta en código, nunca de memoria (Matematicas_lushows).
```

## Los niveles de dosis en los protocolos publicados

| Nivel | Dosis típica (sintética, oral) | Uso en el protocolo |
|---|---|---|
| Placebo activo bajo | 1 mg | Control en fase 3 de Compass (COMP005/COMP006) |
| Dosis intermedia | 10 mg | Brazo comparador en COMP006 |
| Dosis terapéutica estudiada | **25 mg** | El brazo principal en fase 3 de COMP360 |
| Rango en estudios académicos | 0,2 – 0,43 mg/kg (≈ 14–30 mg para 70 kg) | Estudios de Johns Hopkins, NYU y otros |
| Microdosis (otro paradigma) | ~1–2 mg, repetida | Ver `264`; evidencia controlada negativa |

**Fuentes y fechas:** el diseño con brazos de 25 mg / 10 mg / 1 mg corresponde al programa fase 3 de
Compass Pathways; COMP005 alcanzó su desenlace primario con una **dosis única de 25 mg** (comunicado de la
compañía, 2025) y COMP006 reportó resultados de 26 semanas de su Parte B el **7 de julio de 2026**. Los
rangos en mg/kg provienen de la literatura académica clásica del campo. Verifica los detalles vigentes en
`ir.compasspathways.com` y en `ClinicalTrials.gov` (`263`).

## Qué acompaña a la dosis (y es tan importante como ella)

En los protocolos publicados, la dosis nunca va sola. El paquete completo incluye:

| Componente | Detalle típico |
|---|---|
| Preparación previa | Varias sesiones con el equipo antes del día de dosificación |
| Ayuno | Desayuno ligero o ayuno, para reducir variabilidad de absorción (`258`) |
| Ambiente | Sala acondicionada, música curada, antifaz; ver `262` |
| Acompañamiento | Uno o dos facilitadores presentes toda la sesión |
| Monitoreo | Presión arterial y frecuencia cardíaca en varios puntos; el aumento agudo es esperable |
| Duración | 6–8 horas, hasta que los efectos se resuelven |
| Integración | Sesiones posteriores de seguimiento |
| Medicación de rescate | Definida por protocolo (por ejemplo, benzodiacepina) para ansiedad severa |
| Criterios de elegibilidad | Screening estricto (`260`) |

Ese conjunto es la razón por la que el resultado de un ensayo **no se transfiere** a un contexto sin
supervisión. La dosis es una variable de un sistema, no una instrucción independiente.

## Cómo se comprueba que la dosis es la dosis

En un ensayo clínico serio, "25 mg" es una afirmación que se demuestra:

| Control | Método |
|---|---|
| Contenido del producto | Valoración por HPLC contra patrón certificado (`256`) |
| Uniformidad de contenido | USP <905>, ±15 % del declarado |
| Impurezas | HPLC/HRMS con límites definidos, ICH Q3A |
| Estabilidad | ICH Q1A, con método indicativo de estabilidad (`255`, `164`) |
| Forma sólida | Polimorfo controlado (`99`) |
| Confirmación de exposición | PK plasmática de psilocina en un subconjunto (`258`) |
| Cegamiento | Cápsulas idénticas; y aun así el cegamiento funcional es limitado (`262`) |

Es exactamente lo que el material natural no puede ofrecer: con RSD de contenido superiores al 20 % dentro
del mismo lote (`254`), la frase "una dosis conocida" no es sostenible.

## Ejemplo aplicado — traducir un resultado sin exagerarlo

```
Reportado: en el brazo de 25 mg del ensayo fase 3 COMP006, alrededor del 39 % de los participantes
alcanzó una reducción relevante en la escala MADRS a la semana 6, mantenida en promedio hasta la
semana 26 (comunicado de Compass Pathways, 7 de julio de 2026 — verificar la cifra exacta y su
definición en la publicación revisada por pares cuando esté disponible).

Cómo NO se dice: "la psilocibina cura la depresión en el 39 % de los casos".
Cómo SÍ se dice: "en un ensayo fase 3 en depresión resistente al tratamiento, una dosis única de
25 mg de psilocibina sintética administrada con acompañamiento psicológico mostró una proporción
de respuesta a la semana 6 que se mantuvo en promedio hasta la semana 26" [clínico fase 3].
```

## Errores comunes

- **Convertir mg de sustancia sintética a gramos de material natural.** No es válido: la potencia del
  material es desconocida y variable (`254`).
- **Citar la dosis sin citar el contexto.** Sin preparación, supervisión y screening, el número no describe
  la intervención estudiada.
- **Presentar la dosis como recomendación.** Este módulo describe protocolos; no recomienda nada.
- **Ignorar que el brazo de 1 mg es un control, no una "microdosis terapéutica".**
- **Comparar mg/kg con dosis fija sin hacer la conversión.** Se llega a conclusiones falsas sobre potencia.
- **Tomar un comunicado de prensa como si fuera una publicación revisada por pares.** No lo es; hay que
  esperar el paper y decirlo.

## Conexión con otros módulos

→ `260-screening-de-seguridad-y-contraindicaciones.md` — quién queda fuera y por qué.
→ `262-set-setting-y-diseno-de-estudio.md` — el resto del sistema alrededor de la dosis.
→ `263-estado-clinico-y-regulatorio-2026.md` — el estado del desarrollo y la ley.
→ `258-farmacocinetica-de-psilocibina.md` y `257-farmacologia-de-la-psilocibina.md`.
→ `254-variabilidad-de-potencia-entre-especies.md` — por qué no se traduce a material natural.
→ `289-etica-de-la-investigacion-y-consentimiento.md` — el marco ético obligatorio.
