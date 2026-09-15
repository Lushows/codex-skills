# 107 — ISO/IEC 17025 y acreditación (qué significa de verdad el sello del laboratorio)

"Somos un laboratorio certificado" es una frase que no quiere decir nada. Lo que importa es si el laboratorio
está **acreditado** bajo **ISO/IEC 17025:2017**, por **quién**, y —lo que casi nadie revisa— si el ensayo que
tú necesitas está **dentro de su alcance acreditado**. Un laboratorio puede estar acreditado para metales
pesados en agua y no para metales pesados en polvo de hongo; si te firma ese resultado, el sello del
encabezado no lo cubre. Este módulo te enseña a leer una acreditación como se lee un contrato: por lo que
excluye, no por el logo.

Términos: **acreditación (accreditation)** = un tercero evalúa técnicamente al laboratorio contra una norma.
**certificación (certification)** = conformidad con un sistema de gestión (ISO 9001); **no** evalúa competencia
técnica. **alcance acreditado (scope of accreditation)** = lista oficial de ensayo + matriz + método + rango.
**organismo de acreditación (accreditation body)** = ONAC en Colombia, A2LA/ANAB en EE.UU., ENAC en España.
**ILAC MRA** = acuerdo de reconocimiento mutuo que hace que un informe acreditado valga en otros países.

## Certificación ≠ acreditación (la confusión que venden)

| | ISO 9001 (certificación) | ISO/IEC 17025 (acreditación) |
|---|---|---|
| Qué evalúa | Sistema de gestión de calidad | **Competencia técnica** + imparcialidad + gestión |
| ¿Evalúa si el resultado es correcto? | No | Sí: métodos, validación, incertidumbre, personal, equipos |
| ¿Tiene alcance por ensayo? | No | **Sí, ensayo por ensayo y matriz por matriz** |
| Quién lo otorga | Organismo certificador | Organismo de acreditación (ONAC, A2LA, ENAC…) |
| Sirve para un COA defendible | No por sí solo | Sí, dentro del alcance |

Un laboratorio ISO 9001 puede tener procedimientos impecables para hacer mal un análisis, de forma
consistente y documentada. La acreditación 17025 es la que mira si el número es técnicamente válido.

## Qué revisa la norma (y qué le puedes preguntar al laboratorio por eso)

ISO/IEC 17025:2017 organiza los requisitos de proceso en las cláusulas 7.1 a 7.11: revisión de solicitudes
(7.1), **selección y validación de métodos** (7.2), **muestreo** (7.3), manipulación de ítems de ensayo (7.4),
registros técnicos (7.5), **evaluación de la incertidumbre de medición** (7.6), **aseguramiento de la validez
de los resultados** (7.7), **informe de resultados** (7.8), quejas (7.9), trabajo no conforme (7.10) y control
de datos (7.11)
([estructura de la cláusula 7 de la norma, consultada a agosto de 2026](https://17025store.com/iso-iec-17025-2017-requirements/clause-7-process-requirements/)).
La norma exige que los resultados se entreguen de manera exacta, clara, inequívoca y objetiva, y que sean
revisados y autorizados antes de liberarse.

Traducido a preguntas que sí puedes hacer por correo:

1. "¿Su alcance acreditado cubre **este ensayo en esta matriz**? Mándeme el anexo técnico." (7.2)
2. "¿El muestreo lo hacen ustedes y está acreditado, o yo les mando la muestra?" (7.3)
3. "¿Cuál es la **incertidumbre expandida** de este ensayo a este nivel de concentración?" (7.6)
4. "¿Participan en **ensayos de aptitud** para este analito y cuál fue su último desempeño?" (7.7)
5. "Si van a declarar 'cumple / no cumple', ¿cuál es su **regla de decisión**?" (7.8)

## Regla de decisión: la pregunta de las cinco que más gente pierde

Cuando el laboratorio escribe "Cumple" en un COA, está comparando un resultado **con incertidumbre** contra un
límite. Si el resultado es 0,48 mg/kg, el límite es 0,50 mg/kg y la incertidumbre expandida es ±0,06 mg/kg,
¿cumple? Depende de la **regla de decisión** acordada:

```
Resultado: 0,48 mg/kg   Limite: 0,50 mg/kg   Incertidumbre expandida U = 0,06 mg/kg (k=2)

Regla "aceptacion simple" (riesgo compartido): 0,48 < 0,50  -> CUMPLE
Regla "banda de guarda estricta" (proteger al consumidor): se exige resultado + U < limite
                                          0,48 + 0,06 = 0,54 > 0,50 -> NO CUMPLE
```

Mismo dato, veredicto opuesto. Por eso la norma exige que la regla de decisión esté documentada y declarada.
Si un COA dice "Cumple" y no dice con qué regla ni con qué incertidumbre, esa declaración no se puede
defender ante un cliente B2B ni ante una autoridad (ver `76`, `111`).

## Ensayos de aptitud: la prueba de que el laboratorio mide bien

Un **ensayo de aptitud (proficiency testing, PT)** es una muestra de valor conocido que un proveedor
independiente manda a muchos laboratorios; cada uno reporta y recibe una calificación de desempeño. La norma
de los proveedores de PT es **ISO/IEC 17043**, y el tratamiento estadístico de los resultados sigue **ISO
13528** ([referencia consultada a agosto de 2026](https://www.mollabs.com/Documentos/BlogDocs/EAISO17043.pdf)).
Es la evidencia más contundente que puedes pedir: no te dice que el laboratorio tenga buenos procedimientos,
te dice que **acertó** en una muestra que no controlaba. Pide el resultado de PT del analito que te interesa,
no de la lista completa.

## Cómo se verifica una acreditación (5 minutos, gratis)

```
1. Anota el numero de acreditacion que aparece en el COA. Si no aparece -> bandera roja (111).
2. Entra al directorio del organismo acreditador:
     Colombia  -> ONAC (onac.org.co), directorio de organismos acreditados
     EE.UU.    -> A2LA, ANAB, PJLA
     Espana/UE -> ENAC y su equivalente nacional
3. Busca el laboratorio por nombre o por numero. Descarga el ANEXO TECNICO del alcance.
4. Busca en el anexo: el ENSAYO + la MATRIZ + el METODO + el RANGO que a ti te interesan.
5. Verifica la VIGENCIA. Las acreditaciones se suspenden, se reducen y se vencen.
```

ONAC hace parte de los acuerdos multilaterales de ILAC, lo que hace que un informe emitido bajo su
acreditación sea aceptable en más de cien economías
([ONAC, laboratorios de ensayo, consultado a agosto de 2026](https://onac.org.co/en/services/testing-laboratories/)).
Ese es el valor real de la acreditación cuando piensas exportar: no es el sello, es el reconocimiento mutuo.

## Ejemplo aplicado (ILUSTRATIVO)

Un laboratorio te manda un COA de metales pesados en polvo de reishi con el logo de acreditación en la
esquina. Verificación:

| Qué revisas | Lo que encuentras | Veredicto |
|---|---|---|
| Número de acreditación | Aparece: 20-LAB-XXX | Verificable |
| Anexo técnico: ensayo | Metales por ICP-MS | Cubierto |
| Anexo técnico: **matriz** | "Aguas y bebidas" | **No cubre matriz sólida vegetal/fúngica** |
| Vigencia | Vigente | Correcto |
| PT del analito | No participan en PT de sólidos | Sin evidencia de desempeño en tu matriz |

El COA está firmado por un laboratorio acreditado, y aun así **ese resultado está fuera del alcance**. El
laboratorio no mintió; tú leíste el logo en vez del anexo. Cifras **(ILUSTRATIVO)**. La conversación correcta
no es acusar: es preguntar si el ensayo se reportó como "fuera de alcance de acreditación" —lo cual es
legítimo y frecuente— y decidir si eso te sirve para lo que vas a hacer con el número.

## Errores comunes

- **Leer el logo y no el anexo técnico.** El alcance es lo que se acredita, no el laboratorio entero.
- **Confundir ISO 9001 con ISO/IEC 17025.** La primera no dice nada sobre si el resultado es correcto.
- **No pedir la incertidumbre** y luego discutir un "cumple/no cumple" que dependía de ella.
- **Aceptar "Cumple" sin regla de decisión declarada.** No es defendible.
- **No pedir el desempeño en ensayos de aptitud** del analito específico.
- **Asumir que la acreditación cubre el muestreo.** Casi nunca lo cubre si la muestra la mandaste tú (`109`).
- **No revisar la vigencia.** Un anexo de hace tres años puede estar reducido hoy.

## Conexión con otros módulos

→ `108-como-elegir-un-laboratorio.md` — el proceso completo de selección, con la lista de preguntas.
→ `110-como-leer-un-coa.md` — dónde aparece la acreditación dentro del certificado.
→ `76-incertidumbre-de-medida.md` — el número sin el cual "cumple" no significa nada.
→ `75-validacion-de-metodos-ich-q2-r2.md` — qué hace válido un método dentro del alcance.
→ `112-como-impugnar-un-resultado.md` — qué hacer cuando el resultado no cuadra.
→ `280-farmacopeas-usp-ep-y-monografias.md` y `281-metodos-oficiales-aoac.md` — los métodos que suelen estar
  en el alcance.
