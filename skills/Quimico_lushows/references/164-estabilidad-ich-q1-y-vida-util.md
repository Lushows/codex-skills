# 164 — Estabilidad ICH Q1 y vida útil (cómo se diseña un estudio de verdad)

La fecha de vencimiento del frasco no es una estimación optimista: es una afirmación técnica que se sostiene
con datos. Un estudio de estabilidad responde una pregunta concreta: **¿este producto, en este envase, sigue
cumpliendo su especificación después de N meses en estas condiciones?** La referencia internacional es la guía
**ICH Q1A(R2)**, escrita para medicamentos, y que la industria de suplementos adopta como marco porque no hay
nada mejor. Este módulo te enseña a diseñar el estudio, no solo a nombrarlo.

Términos: **estabilidad a largo plazo (long-term stability)** = almacenamiento en la condición de uso real.
**Acelerada (accelerated)** = condición más severa para forzar la degradación. **Intermedia (intermediate)** =
condición entre ambas. **Vida útil (shelf life)** = período durante el cual el producto cumple especificación.
**Bracketing / matrixing** = estrategias para reducir el número de muestras a analizar. **Método indicador de
estabilidad (stability-indicating method)** = método analítico capaz de separar el activo de sus productos de
degradación.

## Las condiciones de ICH Q1A(R2)

| Estudio | Condición | Duración mínima en el momento de presentar |
|---|---|---|
| Largo plazo | 25 °C ± 2 °C / 60 % HR ± 5 % **o** 30 °C ± 2 °C / 65 % HR ± 5 % | 12 meses |
| Intermedio | 30 °C ± 2 °C / 65 % HR ± 5 % | 6 meses |
| Acelerado | 40 °C ± 2 °C / 75 % HR ± 5 % | 6 meses |

El estudio intermedio no se requiere si ya usaste 30 °C/65 % HR como condición de largo plazo. La evaluación de
los datos y la extrapolación a una vida útil propuesta se rigen por la guía complementaria **ICH Q1E**.

**Colombia y la zona climática.** Las zonas climáticas de la OMS ubican los países cálidos y húmedos en zona IV
(IVA: 30 °C/65 % HR; IVB: 30 °C/75 % HR). Colombia es un país cálido-húmedo en buena parte de su territorio, lo
que hace que la condición de largo plazo razonable sea **30 °C/65 % HR o 30 °C/75 % HR**, no 25 °C/60 %. A
agosto de 2026, confirma con INVIMA la condición exigida para tu categoría de producto antes de arrancar el
estudio: correr 12 meses en la condición equivocada es perder un año (`266`, `269`).

## Qué se mide (y por qué "contenido" no basta)

Un estudio de estabilidad mide **atributos que pueden cambiar**, no una lista genérica:

| Atributo | Método | Por qué cambia |
|---|---|---|
| Contenido de activo/marcador | HPLC-DAD, Megazyme, LC-MS/MS | Degradación química |
| Productos de degradación | El mismo cromatograma, picos nuevos | Aparecen aunque el activo "aguante" |
| Humedad | Karl Fischer (`98`) | Permeación del envase |
| Actividad de agua | Higrómetro (`35`) | Predice apelmazamiento y microbiología |
| Aspecto, color, olor | Visual/organoléptico documentado con foto | Oxidación, Maillard (`62`) |
| Desintegración / disolución | Farmacopea (`280`) | La cápsula endurece con el tiempo |
| Uniformidad de masa | Balanza | Pérdida de volátiles |
| Microbiología | Recuentos y patógenos (`100`) | Crecimiento si a_w sube |
| pH (líquidos) | Potenciómetro | Hidrólisis, migración |
| Peróxidos / índice de acidez (aceites) | Titulación | Rancidez |
| Tamaño de gota (emulsiones) | DLS (`157`) | Ostwald ripening |

**El requisito silencioso:** el método analítico tiene que ser **indicador de estabilidad**. Si tu HPLC no
separa el activo de su producto de degradación, vas a reportar "sin cambios" mientras el producto se descompone
debajo del mismo pico. Se demuestra con un estudio de degradación forzada (ácido, base, oxidante, calor, luz) y
verificación de pureza de pico (`75`, `80`).

## El diseño completo, paso a paso

```
DISEÑO DE UN ESTUDIO DE ESTABILIDAD

1. LOTES:      mínimo 3 lotes distintos (ICH pide 3 para producto nuevo).
               Con presupuesto de pyme: arranca con 1 lote piloto para aprender,
               pero el estudio que sostiene la fecha necesita ≥ 3.

2. ENVASE:     el envase primario REAL de venta (`163`). No un frasco genérico.

3. ORIENTACIÓN: para líquidos, muestras en posición normal E invertida
                (para evaluar contacto con el cierre).

4. CONDICIONES: largo plazo 30 °C/65 % o 30 °C/75 % HR (Colombia)
                acelerado    40 °C/75 % HR

5. TIEMPOS:  Acelerado:   0, 3, 6 meses
             Largo plazo: 0, 3, 6, 9, 12, 18, 24, 36 meses
             (y anualmente después)

6. MUESTRAS: unidades suficientes por punto de tiempo × condición × lote,
             más un 30 % de reserva para repeticiones.
             CUENTA: 3 lotes × 8 puntos × 2 condiciones × 3 réplicas = 144 unidades mínimo.
             Reserva el material ANTES de vender el lote.

7. ESPECIFICACIÓN DE ESTABILIDAD: los criterios que debe cumplir EN CADA PUNTO.
             Normalmente iguales a la spec de liberación, salvo atributos
             que se permite que evolucionen dentro de un rango.

8. CRITERIO DE CAMBIO SIGNIFICATIVO (ICH): en acelerado se considera cambio
             significativo, entre otros, una pérdida de contenido ≥ 5 % respecto a t=0,
             o el incumplimiento de cualquier criterio de la especificación.
             Si ocurre en acelerado → hay que correr el estudio intermedio.

9. INFORME:  tablas por atributo, tendencia, y la vida útil PROPUESTA con su racional (`294`).
```

## Estabilidad fotoquímica: el estudio que casi nadie hace

ICH tiene una guía específica para fotoestabilidad (Q1B). La versión práctica: exponer el producto —en envase
y fuera de envase— a una fuente de luz definida, y comparar contra un control envuelto en aluminio. Es el
estudio que decide si tu frasco tiene que ser ámbar. Para extractos ricos en fenoles, triterpenos y para THC
(que fotodegrada a CBN, `204`), es una prueba que vale mucho más de lo que cuesta.

## Cómo se comprueba: la lectura de los datos

```
LECTURA DE UNA TABLA DE ESTABILIDAD (ILUSTRATIVO)
Producto: cápsulas de extracto de reishi, 150 mg de β-glucano declarados
Condición: 30 °C / 75 % HR

Mes    β-glucano (mg/cáp)   % de t=0   Humedad (%)   a_w    Aspecto
  0         163                100        4,1        0,32   conforme
  3         162                 99,4      4,4        0,35   conforme
  6         160                 98,2      4,9        0,39   conforme
  9         159                 97,5      5,3        0,42   conforme
 12         157                 96,3      5,8        0,45   conforme
 18         154                 94,5      6,6        0,51   leve aglomeración
 24         151                 92,6      7,4        0,58   aglomeración visible

Lectura:
  - El β-glucano baja poco (polímero robusto). A 24 meses aún supera los 150 mg declarados.
  - El atributo LIMITANTE no es el activo: es la HUMEDAD y el aspecto.
  - La vida útil la define el primer atributo que se sale, no el activo.
  → Vida útil propuesta: 24 meses, con acción correctiva sobre el envase
    (más desecante o mayor barrera) si se quiere llegar a 36.
```

Ese es el aprendizaje más útil del módulo: **en suplementos de hongos, el que suele reprobar es el envase, no
la molécula.**

## Ejemplo aplicado — el presupuesto real de una pyme

```
Escenario: BIO-SETA quiere declarar 24 meses.
  - No hay cámara climática propia. Se contrata almacenamiento en cámara certificada.
  - Análisis por punto: β-glucano + humedad + a_w + aspecto + microbiología (a 0, 12, 24).
  - Puntos: acelerado 0/3/6 + largo plazo 0/3/6/9/12/18/24 = 10 puntos por lote.
  - Con 3 lotes: 30 sesiones de análisis.
  → Cotiza con 2 laboratorios (`114`, `291`) y presupuéstalo como un costo de lanzamiento,
    no como un imprevisto.

Estrategia de arranque honesta:
  Mes 0    : iniciar acelerado + largo plazo con 1 lote piloto
  Mes 6    : con acelerado completo, ESTIMAR vida útil provisional (`165`)
  Mes 12   : con 12 meses de largo plazo, declarar vida útil de 24 con extrapolación ICH Q1E
  Mes 24   : confirmar con datos reales; ajustar si hace falta (control de cambios, `169`)
```

## Errores comunes

- Poner "24 meses" en la etiqueta sin un solo dato. Es la práctica más extendida y la más indefendible.
- Correr el estudio en un envase distinto al de venta.
- Usar un método analítico que no separa el activo de sus degradados y creer que "no pasó nada".
- Medir solo contenido y no medir humedad, aspecto ni microbiología: el producto reprueba por ahí.
- Guardar las muestras "en la oficina" en vez de en cámara controlada y con registro de T/HR.
- No reservar suficientes unidades y quedarse sin muestra para el punto de 24 meses.
- Elegir 25 °C/60 % HR como condición de largo plazo en un país de zona climática IV.
- Cambiar la fórmula, el proveedor o el envase y seguir usando el estudio viejo (`169`).

## Conexión con otros módulos

→ `165-estudios-acelerados-y-arrhenius.md` — cómo estimar vida útil sin esperar 24 meses.
→ `163-envase-primario-y-compatibilidad.md` — el sistema que se está poniendo a prueba.
→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — los mecanismos de degradación.
→ `282-especificacion-de-producto-terminado.md` — los criterios contra los que se compara cada punto.
→ `75-validacion-de-metodos-ich-q2-r2.md` — cómo se demuestra que el método es indicador de estabilidad.