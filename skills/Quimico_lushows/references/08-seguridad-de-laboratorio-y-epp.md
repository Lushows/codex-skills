# 08 — Seguridad de laboratorio y EPP (lo que se hace antes de tocar nada)

Antes de que exista un dato, existe una persona manipulando material. Este módulo es el que evita que
alguien pierda un ojo, se queme una mano o incendie una bodega por hacer una extracción con etanol
junto a una estufa. No hace falta tener un laboratorio formal: si en tu operación hay etanol, hexano,
ácidos, estufas, molinos o evaporadores, ya tienes riesgos de laboratorio y ya te aplican reglas. En
Colombia, además, esto se cruza con obligaciones de SG-SST del negocio: no es solo prudencia, es
cumplimiento. El costo de ignorarlo va desde una incapacidad hasta la pérdida total de una planta.

Términos: **EPP (PPE, personal protective equipment)** = equipo de protección personal. **cabina
extractora (fume hood)** = campana con extracción forzada donde se manipulan volátiles. **punto de
inflamación (flash point)** = temperatura mínima a la que un líquido emite vapor suficiente para
encenderse. **LEL/UEL (lower/upper explosive limit)** = rango de concentración de vapor en aire dentro
del cual la mezcla explota. **incompatibilidad química (chemical incompatibility)** = pares de
sustancias que no pueden almacenarse ni mezclarse juntas.

## La jerarquía de controles (en este orden, siempre)

| Nivel | Control | Ejemplo en una planta de extractos |
|---|---|---|
| 1 | **Eliminar** el peligro | No usar hexano si etanol resuelve |
| 2 | **Sustituir** por algo menos peligroso | Etanol grado alimenticio en vez de metanol |
| 3 | **Ingeniería** | Cabina extractora, equipo antichispa, puesta a tierra, ventilación |
| 4 | **Administrativo** | Procedimientos escritos, capacitación, señalización, permisos de trabajo |
| 5 | **EPP** | Gafas, guantes, bata, respirador |

El EPP es el **último** nivel, no el primero. Una operación que solo tiene guantes está mal diseñada.
Mucha gente empieza comprando guantes y termina con una nube de vapor de etanol en un cuarto cerrado.

## EPP mínimo por tarea

| Tarea | Ojos | Manos | Cuerpo | Vías respiratorias |
|---|---|---|---|---|
| Pesar polvo seco / moler | Gafas de seguridad | Nitrilo | Bata | Mascarilla contra polvo (FFP2 o superior) |
| Manejar etanol o solvente volátil | Gafas o monogafas | Nitrilo (cambio frecuente) | Bata sin fibras sintéticas | Ventilación o cabina; respirador con cartucho orgánico si no hay |
| Ácidos y bases concentrados | Monogafas + careta | Neopreno o butilo | Delantal resistente | Cabina obligatoria |
| Evaporación / rotavapor | Gafas | Nitrilo | Bata | Cabina; pantalla si hay vacío |
| Manipular material fúngico seco (esporas) | Gafas | Nitrilo | Bata | FFP2/FFP3: las esporas son alérgeno respiratorio |

Nota importante para hongos: el polvo de esporas es un **sensibilizante respiratorio** documentado. Es
un riesgo laboral real en el cultivo y el secado, y se controla con extracción y protección
respiratoria, no con costumbre (ver `137`).

## Solventes: los números que importan

| Solvente | Punto de inflamación | Riesgo dominante | Nota |
|---|---|---|---|
| Etanol 96 % | ~13 °C | Inflamable; vapor más denso que el aire | Se acumula a nivel del piso |
| Isopropanol | ~12 °C | Inflamable | Similar al etanol |
| Metanol | ~11 °C | Inflamable + **tóxico** (ceguera) | Evitarlo en producción de consumo |
| Hexano | ~−22 °C | Muy inflamable, neurotóxico | Requiere zona clasificada |
| Acetona | ~−20 °C | Muy inflamable | Vapores rápidos |
| Butano/propano | Gas | Explosivo, sin olor propio en calidad pura | Solo en instalación certificada |

Valores de referencia de fichas de seguridad; **verifica la SDS del producto exacto que compres**
(ver `09`). El vapor de etanol es más denso que el aire y se acumula abajo: los extractores que están
en el techo no lo sacan. Ese detalle ha causado incendios reales en talleres de extracción.

## Cómo se comprueba que tu operación está en control

Auditoría corta que puedes hacer tú mismo, hoy:

```
[ ] Toda sustancia tiene su SDS impresa y accesible en español (ver 09)
[ ] Todo envase tiene etiqueta con nombre, pictograma GHS y fecha de apertura
[ ] Hay ducha de emergencia y lavaojos funcionando, probados y con registro
[ ] Extintores adecuados al riesgo (clase B para solventes), vigentes
[ ] Ventilación: renovaciones de aire suficientes; extracción a nivel bajo si hay solventes
[ ] Equipos eléctricos en zona de solventes: antichispa y con puesta a tierra
[ ] Incompatibles separados: ácidos ≠ bases ≠ oxidantes ≠ inflamables
[ ] Procedimiento escrito de derrame, con kit disponible y personal entrenado
[ ] Nadie trabaja solo con solventes o con material peligroso
[ ] Registro de capacitación firmado por cada persona
```

Si alguna casilla falla, esa es tu tarea de la semana. Ninguna de estas cuesta mucho comparada con lo
que evita.

## Ejemplo aplicado (BIO-SETA)

Vas a montar la extracción hidroalcohólica de reishi en un local arrendado, 30 m², con 40 L de etanol
96 % en proceso. Análisis rápido:

- **Eliminar/sustituir**: ¿la fracción de triterpenos justifica el alcohol, o el producto se sostiene
  con extracción acuosa? Si el claim es β-glucanos, el alcohol quizá no aporta (ver `146`, `241`).
- **Ingeniería**: extracción localizada sobre el reactor, toma a nivel bajo, equipo eléctrico
  antichispa, puesta a tierra del recipiente al trasvasar, bandeja de contención.
- **Administrativo**: máximo de solvente en área de trabajo, almacén de inflamables separado, permiso
  de trabajo en caliente prohibido durante la operación.
- **EPP**: monogafas, nitrilo, bata de algodón, respirador con cartucho de vapores orgánicos.
- **Papeles**: matriz de riesgos y capacitación dentro del SG-SST; esto se coordina con el frente de
  cumplimiento operativo (ruteo a `AVIS_lushows`).

Costo de hacerlo bien desde el inicio: bajo comparado con una pérdida total. Costo de aprenderlo
después de un incidente: el negocio.

## Errores comunes

- **Empezar por el EPP** y saltarse ingeniería y ventilación.
- **Guardar solventes en la nevera doméstica.** El termostato hace chispa; es una fuente clásica de
  explosión. Se requiere nevera antichispa.
- **Trasvasar sin puesta a tierra.** La electricidad estática enciende vapores de etanol.
- **Extractor en el techo para vapores más densos que el aire.** No sirve.
- **Reenvasar sin reetiquetar.** Un frasco sin etiqueta es un accidente esperando.
- **Trabajar solo de noche.** Si pasa algo, no hay quien active la respuesta.
- **Ignorar el polvo de esporas** porque "es natural". El asma ocupacional también lo es.

## Conexión con otros módulos

→ `09-fichas-de-seguridad-sds-y-ghs.md` — la SDS, que es la fuente de todos estos datos.
→ `63-quimica-verde-y-solventes.md` — cómo elegir el solvente menos peligroso que sirva.
→ `87-solventes-residuales.md` — el otro lado del solvente: lo que queda en el producto.
→ `137-alergenos-e-hipersensibilidad.md` — esporas y sensibilización.
→ `145-extraccion-hidroalcoholica-y-tinturas.md` — el proceso donde más aplica esto.
→ `188-extraccion-con-hidrocarburos.md` — el escenario de mayor riesgo del oficio.
→ `AVIS_lushows` — SG-SST, bomberos y papeles del local en Colombia.
