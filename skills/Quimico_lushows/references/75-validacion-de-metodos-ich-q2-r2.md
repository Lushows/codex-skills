# 75 — Validación de métodos analíticos según ICH Q2(R2), parámetro por parámetro

Validar un método es demostrar con datos que sirve **para el uso que le vas a dar**, no que es bonito. Es el
documento que separa un resultado defendible de una opinión con membrete, y es lo primero que pide una
autoridad sanitaria o un cliente serio. Si contratas laboratorios, no necesitas ejecutar la validación:
necesitas saber leerla, exigirla para **tu matriz** y detectar cuándo el resumen que te mandan no cubre lo
que te van a cobrar.

Términos:
- **Procedimiento analítico (analytical procedure)** = el método completo escrito: muestra, prep, equipo,
  condiciones, cálculo, criterios.
- **Validación (validation)** = demostrar con evidencia experimental que cumple su propósito.
- **Verificación (verification)** = comprobar en tu laboratorio que un método ya oficial (USP, AOAC) funciona
  en tus manos y tu matriz. Es más corta que una validación completa.
- **Transferencia (method transfer)** = pasar un método validado de un laboratorio a otro, con demostración.
- **ATP (analytical target profile)** = el objetivo declarado del método (qué mide, en qué rango, con qué
  exactitud). Concepto de ICH Q14.

## Qué cambió con Q2(R2) — estado a agosto de 2026

ICH Q2(R2) fue finalizada en **noviembre de 2023** y adoptada como Step 5 en las regiones ICH (en la UE con
aplicación desde **junio de 2024**). Se publica junto con **ICH Q14 (Analytical Procedure Development)**, que
cubre el desarrollo y el ciclo de vida del método. Verifica siempre el texto vigente en `database.ich.org` y
la adopción local (en Colombia, lo que exija el INVIMA para tu tipo de producto).

Los cambios que importan en la práctica:

1. **Alcance ampliado**: además de fisicoquímicos, cubre procedimientos biológicos/biotecnológicos y
   **multivariantes** (NIR, quimiometría — ver `92`, `105`).
2. **Enfoque de ciclo de vida** alineado con Q14: la validación no termina, continúa como verificación
   continua del desempeño.
3. **"Linealidad" deja de ser un fin**: se habla de **relación respuesta-concentración**, y se aceptan modelos
   no lineales debidamente justificados.
4. **Exactitud y precisión pueden evaluarse en un estudio combinado**, con criterios predefinidos e informe
   de estimados **con intervalos de confianza**.
5. **No hay criterios numéricos universales.** La guía exige que tú los definas y los justifiques según el
   uso previsto. Cualquiera que te diga "ICH exige RSD < 2 %" está citando costumbre, no la guía.

## Los parámetros, uno por uno

| Parámetro | Qué demuestra | Diseño experimental típico | Criterio típico de la industria (ILUSTRATIVO — defínelo y justifícalo) |
|---|---|---|---|
| **Especificidad / selectividad** (specificity) | Que mides el analito y no otra cosa | Blanco de matriz, placebo, muestra degradada a propósito (forced degradation), coelución | Sin picos interferentes en el tiempo de retención; **pureza de pico** por DAD o razón de iones por MS (`80`, `83`) |
| **Rango** (range) | Intervalo donde todo se cumple | 80–120 % del nivel nominal (contenido); LOQ–120 % del límite (impurezas) | Exactitud, precisión y respuesta demostradas en todo el intervalo |
| **Respuesta / linealidad** (response) | Relación entre concentración y señal | >= 5 niveles, réplicas; residuales | Residuales aleatorios; %RE por nivel dentro de criterio; R² se reporta pero no decide |
| **Exactitud** (accuracy / trueness) | Cercanía al valor verdadero | 3 niveles x 3 réplicas (9 determinaciones) con spike o CRM | 98–102 % (fármaco), 95–105 % (natural), 70–120 % (trazas) |
| **Precisión — repetibilidad** | Dispersión intradía | 6 determinaciones al 100 % **o** 3 niveles x 3 réplicas | RSD <= 1–2 % (mayores); <= 15 % (trazas) |
| **Precisión — intermedia** | Dispersión intralaboratorio | >= 2 días x 2 analistas (a veces 2 equipos), 6 corridas independientes | RSD <= 2–3 % (mayores); <= 20 % (trazas) |
| **Precisión — reproducibilidad** | Entre laboratorios | Estudio colaborativo (solo si el método será oficial) | Según el estudio; ver Horwitz (`74`) |
| **LOD** (detection limit) | Mínimo detectable | S/N = 3, o 3,3·σ/m | Confirmado analizando muestras a ese nivel |
| **LOQ** (quantitation limit) | Mínimo cuantificable | S/N = 10, o 10·σ/m | Verificado con exactitud y precisión al nivel del LOQ |
| **Robustez** (robustness) | Tolerancia a variaciones pequeñas | Variar deliberadamente pH ±0,2, temperatura ±5 °C, % orgánico ±2 %, lote de columna | El resultado no cambia más allá del criterio; se identifican los parámetros críticos |
| **Estabilidad de solución** (solution stability) | Cuánto duran muestra y patrón | Reanalizar a 0, 24, 48 h, refrigerado y ambiente | Variación <= 2 % del valor inicial |

Qué parámetros se exigen depende del tipo de ensayo:

| Tipo de ensayo | Especificidad | Rango/respuesta | Exactitud | Precisión | LOD | LOQ |
|---|---|---|---|---|---|---|
| Identificación | Sí | No | No | No | No | No |
| Contenido / potencia (assay) | Sí | Sí | Sí | Sí | No | No |
| Impurezas — cuantitativo | Sí | Sí | Sí | Sí | (Sí) | Sí |
| Impurezas — límite | Sí | No | No | No | Sí | No |
| Contaminantes (metales, pesticidas) | Sí | Sí | Sí | Sí | Sí | Sí |

## Degradación forzada: la prueba que casi nadie pide y que lo destapa todo

Para demostrar **especificidad indicativa de estabilidad (stability-indicating)** se somete la muestra a
condiciones agresivas y se comprueba que los productos de degradación no coeluyen con el analito.

```
Condiciones típicas (ILUSTRATIVO):
  ácido    : HCl 0,1 M, 60 °C, 2-24 h
  base     : NaOH 0,1 M, 60 °C, 2-24 h
  oxidativo: H2O2 3 %, temperatura ambiente, 24 h
  térmico  : 80 °C en seco, 48 h
  fotólisis: ICH Q1B (luz visible + UV)
Objetivo: 5-20 % de degradación. Más del 20 % genera degradantes secundarios irreales.

En cannabis esto es especialmente revelador: el THC se oxida a CBN, y si tu método
no separa THC de CBN, la potencia de un producto viejo sale inflada (204).
```

## Ejemplo aplicado — validar potencia de cannabinoides por HPLC-DAD en flor

```
ATP declarado: cuantificar THCA, D9-THC, CBDA, CBD, CBN, CBG en flor seca,
               rango 0,05 - 25 % p/p base seca, con exactitud 95-105 % y RSD <= 3 %.

Especificidad : cromatograma de blanco (metanol), de placebo (matriz sin cannabinoides
                si se consigue) y de mezcla de 16 cannabinoides; verificar resolución
                Rs > 1,5 entre pares críticos (CBD/CBG, THC/CBN) y pureza de pico DAD.
Respuesta     : 6 niveles, 1-500 µg/mL, por analito, en duplicado.
Exactitud     : spike de flor a 3 niveles x 3 → 96-104 %.  (ILUSTRATIVO)
Repetibilidad : 6 réplicas → RSD 1,4 %.  (ILUSTRATIVO)
Interm.       : 2 días x 2 analistas → RSD 2,6 %.  (ILUSTRATIVO)
LOQ           : 0,01 % p/p verificado con réplicas fortificadas.
Robustez      : ácido fórmico 0,05 % vs 0,1 %; 30 vs 35 °C; dos lotes de columna C18.
                Hallazgo típico: el par CBD/CBG es sensible a la temperatura → parámetro crítico.
Estabilidad   : extracto en metanol estable 48 h a 4 °C, protegido de la luz;
                THCA descarboxila si el vial se calienta en el automuestreador (174).

Costo y tiempo de una validación así (ILUSTRATIVO): 8-25 millones COP y 4-10 semanas
de trabajo de laboratorio, según número de analitos y matrices.
```

## Qué preguntarle al laboratorio

1. ¿Este método está **validado** o solo **verificado**? ¿En qué matriz exacta?
2. ¿Me mandan el resumen de validación (no el protocolo completo, el resumen con resultados y criterios)?
3. ¿Es indicativo de estabilidad? ¿Hicieron degradación forzada?
4. ¿Qué parámetros resultaron críticos en robustez? (Si responden "ninguno", no hicieron robustez.)
5. ¿Está dentro de su **alcance acreditado** ISO 17025, o es un método interno fuera de alcance? (`107`)
6. Si es un método oficial (USP, AOAC, farmacopea), ¿tienen la verificación documentada en su laboratorio?
7. ¿Cómo hacen la verificación continua del desempeño (cartas de control, aptitud)? (`77`)

## Errores comunes

- **Pagar por "método validado" y recibir uno validado en otra matriz.** El extracto oleoso no valida la
  gomita, ni el shiitake valida el reishi.
- **Creer que ICH fija los números.** No los fija; el laboratorio debe predefinirlos y justificarlos.
- **Confundir validación con calibración del equipo.** Son cosas distintas (calibración es metrología del
  instrumento; validación es del procedimiento).
- **Omitir robustez.** Es el parámetro que predice si el método sobrevivirá al lote 200 y al cambio de columna.
- **No validar el LOQ.** Muy frecuente: se calcula por fórmula y nunca se comprueba experimentalmente.
- **No revalidar tras un cambio.** Cambiar de columna, de proveedor de reactivo o de matriz exige al menos
  una verificación documentada (`169`).
- **Aceptar un COA de un ensayo fuera del alcance acreditado** creyendo que "el laboratorio es ISO 17025".
  La acreditación es por ensayo y por matriz, no por empresa.

## Conexión con otros módulos

→ `71`, `73`, `74` — los parámetros individuales en detalle.
→ `76-incertidumbre-de-medida.md` — el cierre estadístico de la validación.
→ `77-control-de-calidad-analitico-y-cartas-control.md` — el ciclo de vida después de validar.
→ `80-deteccion-uv-dad-y-pureza-de-pico.md` — cómo se demuestra especificidad con DAD.
→ `107-iso-17025-y-acreditacion.md` — alcance acreditado y qué significa.
→ `280-farmacopeas-usp-ep-y-monografias.md` y `281-metodos-oficiales-aoac.md` — cuándo basta verificar.
