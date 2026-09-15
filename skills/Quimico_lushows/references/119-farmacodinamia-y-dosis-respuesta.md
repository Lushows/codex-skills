# 119 — Farmacodinamia y dosis-respuesta (lo que la sustancia le hace al cuerpo)

Farmacodinamia es la mitad de la farmacología: **qué le hace la sustancia al cuerpo**. La otra mitad, qué
le hace el cuerpo a la sustancia, es farmacocinética (`121`). Este módulo te enseña a leer y a exigir una
curva dosis-respuesta, que es el objeto más honesto de toda la farmacología: si alguien afirma un efecto y
no puede mostrar que el efecto crece con la dosis y se satura, probablemente no hay efecto. El error caro
que evita: escoger la dosis de un producto "por lo que hace la competencia" en vez de por una curva.

Términos: **farmacodinamia (pharmacodynamics, PD)** = relación entre concentración y efecto.
**DE50 / ED50 (median effective dose)** = dosis a la que se obtiene la mitad del efecto máximo.
**Emáx (maximum effect)** = el techo del efecto, por más dosis que se ponga. **Índice terapéutico
(therapeutic index)** = distancia entre la dosis que sirve y la dosis que hace daño. **Curva en U
invertida (hormesis)** = más no siempre es mejor; el efecto sube, llega a un máximo y luego baja.

## La curva sigmoidal, en cristiano

Casi todas las respuestas biológicas siguen esta forma cuando se grafica el efecto contra el **logaritmo**
de la dosis:

```
Efecto
Emáx ┤            ┌────────────
     │          ╱
 50% ┤ - - - - ╱  ← ED50
     │       ╱
   0 ┤──────┘
     └──────────────────────► log(dosis)
```

Modelo de Hill:

```
              Emáx · [D]^n
Efecto  =  ────────────────────
             ED50^n  +  [D]^n
```

Donde `n` (coeficiente de Hill) describe qué tan empinada es la curva. n≈1 es la forma clásica; n>1 indica
cooperatividad y una curva más abrupta (el margen entre "nada" y "demasiado" es más estrecho).

Tres lecturas prácticas de la curva:

1. **Por debajo del pie de la curva no pasa nada.** La mitad de los suplementos del mercado dosifican ahí.
2. **Por encima del hombro no pasa más.** Duplicar la dosis solo duplica el costo y el riesgo.
3. **La pendiente importa más que el punto medio** cuando hay que decidir un margen de seguridad.

## Potencia no es eficacia

Es la confusión número uno y hay que ser quirúrgico:

| Concepto | Qué mide | Se lee en la curva como |
|---|---|---|
| **Potencia (potency)** | Cuánta dosis hace falta | Posición horizontal (ED50) |
| **Eficacia (efficacy)** | Cuánto efecto máximo puede lograr | Altura (Emáx) |

Una molécula 100 veces más potente que otra puede tener la mitad del efecto máximo. Para el usuario final,
**Emáx suele importar más** que la potencia; para el formulador, la potencia decide el tamaño de la cápsula.

## Índice terapéutico y margen

```
IT  =  DL50 / DE50          (en preclínica, DL50 = dosis letal 50; ver 134)
MOS =  NOAEL / dosis humana estimada   (margin of safety; ver 135)
```

En suplementos casi nunca hay DE50 humana publicada, y por eso el margen se construye al revés: se parte
del NOAEL toxicológico y se aplica factor de incertidumbre. Ese camino está en `135`.

## Dosis-respuesta que no son lineales

- **Hormesis**: dosis bajas de un estresor producen respuesta adaptativa y dosis altas daño. Se propone
  para muchos fitoquímicos → mayormente `[in vitro]` y `[animal]`; en humanos casi no está demostrado.
- **Curva en campana** en inmunomodulación: dosis altas de un ligando pueden desensibilizar el receptor y
  dar menos efecto que dosis intermedias — reportado con β-glucanos en modelos preclínicos `[animal]`.
  Es una razón real para no asumir que "más mg de β-glucano es mejor" (ver `130`).
- **Tolerancia**: la curva se desplaza a la derecha con el uso repetido (THC vía CB1, `[clínico]`).

## Cómo se mide

| Nivel | Diseño | Qué te da | Costo/tiempo típico |
|---|---|---|---|
| `[in vitro]` | 8–10 concentraciones, triplicado, ajuste de 4 parámetros | EC50, Emáx, n | días |
| `[animal]` | 3–4 grupos de dosis + control, aleatorizado | ED50 aproximada, NOAEL | meses |
| `[clínico fase 1]` | Escalado de dosis (SAD/MAD), seguridad y PK | tolerabilidad, Cmax, AUC | 6–12 meses |
| `[clínico fase 2]` | Dosis-respuesta con desenlace, doble ciego, placebo | dosis eficaz candidata | 1–2 años |

Regla dura para suplementos: **si el producto no tiene curva, la dosis es una opinión.** Se puede ser
honesto con eso — "esta dosis replica la usada en el estudio X" es defendible; "esta es la dosis óptima"
sin curva, no.

## Ejemplo aplicado — elegir la dosis de una cápsula de reishi

Situación real de BIO-SETA. No hay curva dosis-respuesta humana propia. Lo que sí se puede hacer, en orden:

1. Buscar los ensayos clínicos publicados y anotar **la dosis y el material exacto** (¿extracto acuoso?
   ¿cuerpo fructífero? ¿ratio?). Casi siempre están entre 1,5 y 3 g/día de extracto **(ILUSTRATIVO,
   verificar contra las fuentes primarias de `248`)`.
2. Medir el marcador propio: β-glucano por Megazyme (`221`) y triterpenos por HPLC (`224`).
3. Calcular cuántas cápsulas hacen falta para igualar la **exposición de marcador**, no la masa de polvo:

```
Objetivo (ILUSTRATIVO): 500 mg de β-glucano/día
COA del lote: β-glucano 28,4 % p/p base seca
Extracto necesario = 500 / 0,284 = 1.761 mg/día
Cápsula de 500 mg → 3,5 cápsulas → se redondea a 4 (2.000 mg)
```

(Ejecutar en `lab-tools/betaglucano_dosis.py`, no de cabeza.)

4. Declarar honestamente: "dosis alineada con la usada en estudios publicados", con el nivel de evidencia
   de esos estudios, y sin nombrar enfermedad alguna.

## Errores comunes

- Dosificar por lo que hace la competencia. La competencia probablemente copió a otro que tampoco midió.
- Confundir potencia con eficacia y vender "10× más potente" cuando el Emáx es menor.
- Asumir linealidad: extrapolar de 100 mg a 1.000 mg como si el efecto se multiplicara por diez.
- Ignorar la posibilidad de curva en campana en inmunomodulación y sobredosificar por marketing.
- Copiar la dosis de un estudio hecho con **otro material** (micelio vs cuerpo fructífero cambia todo).
- Presentar una curva `[in vitro]` como si fuera dosis-respuesta clínica.

## Conexión con otros módulos

→ `120-afinidad-eficacia-y-agonismo-parcial.md` — la mecánica molecular detrás de Emáx.
→ `121-farmacocinetica-adme.md` — la dosis administrada no es la concentración en el sitio.
→ `126-vida-media-y-regimen-de-dosis.md` — cómo se pasa de dosis única a régimen diario.
→ `134-toxicologia-basica-dosis-y-riesgo.md` — la misma curva, mirando el daño.
→ `161-dosis-y-tamano-de-porcion.md` — cómo se aterriza en la etiqueta.