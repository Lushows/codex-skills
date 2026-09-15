# 134 — Toxicología básica: dosis y riesgo (por qué "es natural" no significa nada)

La frase fundacional de la toxicología tiene 500 años y sigue vigente: **la dosis hace el veneno**
(Paracelso). Todo es tóxico a suficiente dosis, incluidos el agua y el oxígeno; y nada es tóxico por debajo
de cierta exposición, salvo casos particulares. Este módulo te da el vocabulario para hablar de seguridad
con propiedad —DL50, NOAEL, peligro vs riesgo— y para responder con datos cuando alguien argumenta que su
producto es seguro "porque es natural". El error caro que evita: lanzar un producto sin haber pensado
nunca en su margen de seguridad y descubrirlo por un reporte de evento adverso.

Términos: **peligro (hazard)** = la capacidad intrínseca de causar daño. **Riesgo (risk)** = la
probabilidad de que ese daño ocurra en las condiciones reales de uso. **DL50 / LD50 (median lethal dose)**
= dosis que mata al 50 % de los animales de ensayo; se expresa en mg/kg de peso corporal. **NOAEL (no
observed adverse effect level)** = dosis más alta sin efecto adverso observado. **LOAEL (lowest observed
adverse effect level)** = dosis más baja donde ya se observa efecto adverso.

## Peligro no es riesgo

Es la distinción que resuelve el 80 % de las discusiones mal planteadas:

```
Riesgo  =  Peligro  ×  Exposición
```

El cianuro es un peligro altísimo; la exposición al comer una manzana es despreciable, así que el riesgo es
despreciable. La amanitina de *Amanita phalloides* es peligrosísima; el riesgo depende enteramente de si
alguien la recolecta por error. Un titular que diga "encuentran sustancia tóxica en X" está hablando de
peligro y omitiendo exposición: es información incompleta por diseño.

Consecuencia práctica: cuando un cliente pregunta "¿esto es seguro?", la respuesta técnica es "¿a qué dosis,
por cuánto tiempo, en quién?". Sin esas tres, no hay respuesta.

## Los descriptores de toxicidad

| Descriptor | Qué mide | Unidad | Limitación |
|---|---|---|---|
| DL50 oral | Letalidad aguda | mg/kg pc | Solo dice sobre muerte aguda; hoy se prefieren métodos con menos animales |
| NOAEL | Umbral sin efecto observado | mg/kg pc/día | Depende de las dosis ensayadas y del tamaño del grupo |
| LOAEL | Primer nivel con efecto | mg/kg pc/día | Se usa cuando no se encontró NOAEL |
| BMDL (benchmark dose lower limit) | Dosis asociada a un incremento definido de respuesta, por modelado | mg/kg pc/día | **Preferido hoy** sobre NOAEL: usa toda la curva |
| DL50 dérmica / CL50 inhalatoria | Otras vías | mg/kg, mg/L | Vía específica |

Clasificación orientativa de toxicidad aguda oral (categorías del GHS, ver `09`):

| Categoría GHS | DL50 oral (mg/kg pc) |
|---|---|
| 1 | ≤ 5 |
| 2 | > 5 – 50 |
| 3 | > 50 – 300 |
| 4 | > 300 – 2.000 |
| 5 | > 2.000 – 5.000 |

## Tipos de toxicidad que hay que distinguir

- **Aguda**: una dosis o pocas, efecto rápido.
- **Subcrónica**: 28 o 90 días; es donde se detecta la mayoría de los efectos relevantes para suplementos.
- **Crónica**: 6–24 meses; incluye carcinogenicidad.
- **Genotoxicidad**: daño al ADN. Batería estándar: Ames (mutación en bacterias), aberraciones
  cromosómicas o micronúcleos in vitro, y micronúcleos in vivo.
- **Toxicidad reproductiva y del desarrollo**: la razón por la que casi todo suplemento lleva advertencia
  de embarazo y lactancia — no porque se haya demostrado daño, sino porque **no se ha estudiado**.
- **Sensibilización**: alergia (ver `137`).
- **Toxicidad de órgano diana**: hígado y riñón son los más frecuentes en productos botánicos.

Sobre hepatotoxicidad: las **lesiones hepáticas inducidas por hierbas y suplementos** (HILI, herb-induced
liver injury) son una causa reconocida y creciente de daño hepático agudo en registros clínicos de varios
países `[clínico, registros]`. Es la razón número uno para tomarse en serio la farmacovigilancia (`138`).

## La escalera de evaluación de seguridad, de barata a cara

| Paso | Qué responde | Costo relativo |
|---|---|---|
| Historial de uso documentado | ¿Se ha consumido tradicionalmente y en qué forma y cantidad? | Muy bajo |
| Revisión de literatura toxicológica | ¿Hay NOAEL publicado para la especie? | Bajo |
| Composición y contaminantes | Metales (`136`), micotoxinas, pesticidas, microbiología | Medio |
| Ames + citotoxicidad | Genotoxicidad y toxicidad celular básica | Medio |
| Subcrónico 28 o 90 días en roedor | NOAEL propio | Alto |
| Farmacovigilancia post-lanzamiento | Eventos adversos reales | Continuo, obligatorio |

**El uso tradicional no sustituye a la toxicología**, pero es un dato legítimo. Lo que hay que verificar es
que la forma de uso tradicional coincida con la del producto: una decocción acuosa de reishi consumida
ocasionalmente no es lo mismo que un extracto hidroalcohólico 10:1 en cápsula tomado a diario durante un
año. Ese cambio de matriz y de dosis **es** un cambio de exposición y hay que decirlo (`146`, `151`).

## Cómo se mide

Directrices de referencia (verificar versión vigente a la fecha de uso):

| Ensayo | Guía OECD |
|---|---|
| Toxicidad aguda oral (dosis fija / up-and-down) | OECD 420 / 425 |
| Toxicidad oral repetida 28 días | OECD 407 |
| Toxicidad oral repetida 90 días | OECD 408 |
| Ames (mutación reversa bacteriana) | OECD 471 |
| Micronúcleos in vitro | OECD 487 |
| Micronúcleos in vivo | OECD 474 |
| Irritación dérmica / sensibilización | OECD 404 / 442 |

En Colombia, para un suplemento dietario, lo que exige el trámite sanitario no suele ser una batería
toxicológica completa sino composición, seguridad de ingredientes y ausencia de contaminantes; verificar el
requerimiento vigente con INVIMA a la fecha (ver `266`, `269`). Que no lo exijan no significa que no
convenga tenerlo: el día que haya un evento adverso, el expediente es tu defensa.

## Ejemplo aplicado — margen de seguridad de un extracto

Supuesto **(ILUSTRATIVO)**: NOAEL publicado en rata para un extracto de reishi = 1.000 mg/kg pc/día
(estudio 90 días). Dosis humana propuesta: 1.500 mg/día en persona de 70 kg.

```
Dosis humana = 1.500 / 70 = 21,4 mg/kg pc/día
Margen (MOS) = 1.000 / 21,4 = 46,7
```

Interpretación: el margen es ~47×, por debajo del factor de incertidumbre estándar de 100 que se usa por
defecto (10× por diferencias entre especies × 10× por variabilidad entre personas, ver `135`). Conclusión:
o se busca un NOAEL más alto o mejor caracterizado, o se justifica el factor con datos propios, o se
reconsidera la dosis. **Ejecutar la cuenta en código, no de cabeza** (`Matematicas_lushows`).

## Errores comunes

- Decir "es natural, es seguro". La amanitina, la aflatoxina y el cianuro son naturales.
- Confundir peligro con riesgo y alarmar (o tranquilizar) sin hablar de exposición.
- Extrapolar seguridad de una infusión tradicional a un extracto concentrado. Distinta exposición.
- Usar DL50 como único descriptor. Dice poco sobre uso crónico, que es como se toman los suplementos.
- No advertir sobre embarazo, lactancia y pediatría cuando simplemente no hay datos.
- Ignorar señales de hepatotoxicidad. HILI es real y está creciendo en los registros clínicos.

## Conexión con otros módulos

→ `135-noael-ida-y-limites-de-exposicion.md` — cómo se convierte un NOAEL en un límite de uso.
→ `136-toxicidad-de-metales-pesados.md` — el contaminante más relevante para hongos.
→ `138-farmacovigilancia-y-eventos-adversos.md` — qué hacer cuando algo pasa.
→ `09-fichas-de-seguridad-sds-y-ghs.md` — clasificación y comunicación de peligro.
→ `119-farmacodinamia-y-dosis-respuesta.md` — la misma curva, mirando el beneficio.
