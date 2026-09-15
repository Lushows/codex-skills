# 288 — Cómo diseñar un estudio piloto honesto con recursos de pyme

Tarde o temprano llega la idea: "hagamos un estudio con 20 personas y ya podemos decir que funciona". El
problema no es hacer el estudio; es lo que se concluye después. Un piloto pequeño **puede** darte cosas
valiosas y defendibles: si el producto se tolera, si la gente lo toma como se le indica, cuánta variabilidad
hay, y si vale la pena invertir en algo mayor. Lo que **no** puede darte es una prueba de eficacia — y
usarlo como si lo fuera es, en Colombia y en casi todo el mundo, un claim de enfermedad disfrazado (`268`).
Este módulo te enseña a diseñar el piloto para que sirva y no te meta en problemas.

Términos: **estudio piloto (pilot study / feasibility study)** = estudio pequeño cuyo objetivo declarado es
evaluar factibilidad, tolerabilidad y variabilidad, no eficacia. **n** = número de participantes.
**control (control group)** = grupo que recibe placebo o nada, para tener con qué comparar. **cegado
(blinding)** = que el participante (simple ciego) y/o el evaluador (doble ciego) no sepan qué recibió.
**aleatorización (randomization)** = asignar al grupo por azar, no por criterio. **desenlace primario
(primary endpoint)** = la única medida principal, definida ANTES de empezar. **preregistro
(preregistration)** = publicar el protocolo antes de recoger datos.

## Lo primero: decide qué pregunta estás haciendo

| Pregunta | Tipo de estudio | ¿Alcanza una pyme? | Qué se puede afirmar después |
|---|---|---|---|
| ¿La gente lo tolera y no reporta molestias? | Piloto de tolerabilidad | Sí | "En n=30, durante 8 semanas, no se reportaron eventos adversos serios" |
| ¿La gente logra tomarlo como se indica? | Estudio de adherencia | Sí | "Adherencia del 84 %" |
| ¿Cuánta variabilidad tiene la medida X? | Piloto de variabilidad | Sí | Sirve para calcular el n de un estudio real |
| ¿La formulación se absorbe? | Farmacocinética pequeña | Con laboratorio aliado | Curva plasma-tiempo; es un dato químico duro (`121`) |
| ¿El producto mejora un síntoma? | Ensayo clínico controlado | No, salvo con universidad y comité de ética | Solo con n suficiente, control, cegado y análisis preespecificado |
| ¿El producto trata una enfermedad? | Ensayo clínico regulado | No | Nunca desde un piloto |

Si tu objetivo real es la última fila, tu camino no es un piloto: es una alianza con una universidad y un
comité de ética (`289`). Hacerlo "por tu cuenta" no te da el dato y sí te da el riesgo.

## Diseño mínimo que sí es defendible

```
OBJETIVO PRIMARIO:   tolerabilidad y adherencia (declarado y escrito antes de empezar)
DISEÑO:              abierto o simple ciego, un solo brazo o con control paralelo
n:                   20–40 participantes (un piloto no se dimensiona por potencia estadística;
                     se justifica por factibilidad — declara eso explícitamente)
DURACIÓN:            4–12 semanas, según cuándo esperarías ver algo
CRITERIOS DE ENTRADA: adultos sanos, sin las condiciones de exclusión (ver 260 y 250)
CRITERIOS DE SALIDA:  quién sale y por qué; se cuentan y se reportan todos
PRODUCTO:            UN solo lote, con su COA completo (110) — si cambias de lote, cambias el estudio
DESENLACES:           1 primario + máximo 3 secundarios, todos definidos antes
RECOLECCIÓN:          formulario idéntico para todos, en las mismas fechas
ANÁLISIS:             preespecificado; se reporta también a quienes abandonaron
```

## Los cuatro controles que separan un piloto serio de una encuesta de clientes

1. **Control.** Sin un grupo de comparación, cualquier mejoría puede ser el paso del tiempo, la
   expectativa o el clima. Si no puedes tener placebo, al menos usa un **diseño antes-después con línea de
   base medida dos veces** (para ver cuánto se mueve la medida sola).
2. **Cegado.** Si el participante sabe que tomó "el bueno", reporta mejor. El efecto placebo en desenlaces
   subjetivos (energía, ánimo, sueño) es enorme. Cegar exige un placebo idéntico en color, olor y sabor:
   esto lo diseña el formulador (`162`).
3. **Aleatorización.** Sobre de asignación cerrado o lista generada por computador. No "los primeros 15 al
   grupo A".
4. **Preespecificación.** Escribe el protocolo, féchalo, y si puedes regístralo en un repositorio público
   antes de recoger el primer dato. Esto es lo que impide el pecado capital: mirar todos los desenlaces y
   reportar el único que salió bonito (*p-hacking*).

## Lo que un piloto de n=30 puede y no puede concluir

| SÍ puedes decir | NO puedes decir |
|---|---|
| "Se completó el estudio con 28 de 30 participantes" | "El producto funciona" |
| "No se reportaron eventos adversos serios en 8 semanas" | "El producto es seguro" (8 semanas y 30 personas no cubren seguridad) |
| "La adherencia fue del 84 %" | "El 84 % de los usuarios mejoró" |
| "La variabilidad de la medida X fue DE = 12 puntos, lo que sugiere n ≈ 120 para un estudio de eficacia" | "Hay una tendencia significativa" |
| "Se observó un cambio promedio de X, que este diseño no permite atribuir al producto" | "El producto produjo un cambio de X" |
| "Estos resultados justifican un ensayo controlado" | Cualquier frase con "trata", "cura", "previene" |

La frase que salva: **"este estudio fue diseñado para evaluar factibilidad y tolerabilidad; no fue diseñado
ni tiene el tamaño para evaluar eficacia"**. Ponla en el informe, en la presentación y en cualquier material
que salga de ahí. Cómo comunicar el resultado sin mentir está en `293`.

## Cálculo de tamaño de muestra (para el estudio grande que vendría después)

El piloto no se dimensiona por potencia, pero **sí produce el dato para dimensionar el siguiente**. Fórmula
básica para comparar dos medias, dos colas, α = 0,05 y potencia 80 %:

```
n por grupo ≈ 16 × (DE / Δ)²      donde DE = desviación estándar observada en el piloto
                                        Δ  = diferencia mínima que te importaría detectar

Ejemplo (ILUSTRATIVO): DE = 12 puntos, Δ = 5 puntos
n ≈ 16 × (12/5)² = 16 × 5,76 = 92,2 → 93 por grupo → 186 en total (+ 15 % por abandono ≈ 214)
```

Ese número es el que le pones enfrente a quien te propone "un estudio con 20 personas para probar que
funciona". Ejecuta y verifica el cálculo con `Matematicas_lushows`; la constante 16 es una aproximación
para esos valores de α y potencia, no una ley universal.

## Ejemplo aplicado (BIO-SETA)

Piloto abierto de 8 semanas, n = 30, con cápsulas de melena de león de un solo lote (β-glucano medido,
COA adjunto). Objetivo primario declarado: tolerabilidad. Secundarios: adherencia y variabilidad de una
escala de sueño autoreportada. Resultado hipotético **(ILUSTRATIVO)**: 27 completan, 0 eventos adversos
serios, 3 reportan molestia digestiva leve, adherencia 86 %, DE de la escala = 3,4 puntos.

Comunicación honesta: *"30 personas tomaron el producto durante 8 semanas sin eventos adversos serios; el
estudio no fue diseñado para evaluar eficacia"* [nivel de evidencia: piloto abierto sin control]. Eso ya es
más de lo que la mayoría de marcas del mercado puede decir, y no viola ninguna norma. Comunicar cualquier
otra cosa, sí.

## Errores comunes

- **Llamar "estudio clínico" a una encuesta de satisfacción de clientes.** No lo es, y un competidor o la
  autoridad lo va a notar.
- **Sin control ni cegado, y luego atribuir la mejoría al producto.** Es el error #1 y es siempre el mismo.
- **Cambiar el desenlace después de ver los datos.** Invalida todo el estudio.
- **No reportar a los que abandonaron.** Los que se fueron suelen ser los que peor les fue.
- **Usar varios lotes distintos** sin caracterizarlos: no sabes qué tomó cada quien (`283`).
- **No pasar por comité de ética ni consentimiento informado** (`289`). Sin eso, ninguna revista, ninguna
  universidad y ningún cliente serio te va a tomar el dato.
- **Publicitar el piloto como si fuera evidencia clínica.** Ahí es donde el piloto deja de ser un activo y
  se vuelve un pasivo legal.

## Conexión con otros módulos

→ `289-etica-de-la-investigacion-y-consentimiento.md` — el paso obligatorio antes de reclutar a nadie.
→ `12-niveles-de-evidencia.md` — dónde queda tu piloto en la escala de evidencia.
→ `293-como-comunicar-ciencia-sin-mentir.md` — cómo se cuenta el resultado sin cruzar la línea.
→ `287-diseno-de-experimentos-doe.md` — el equivalente cuando el experimento es de proceso.
→ `14-como-trabajar-con-un-quimico-de-universidad.md` — cómo conseguir el aliado que te dé rigor.
→ `260-screening-de-seguridad-y-contraindicaciones.md` — a quién NO puedes incluir.