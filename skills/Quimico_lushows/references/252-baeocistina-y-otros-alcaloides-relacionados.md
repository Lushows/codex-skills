# 252 — Baeocistina y los otros alcaloides relacionados (el "entourage" que casi nadie mide)

La psilocibina no viaja sola. En el material fúngico aparecen norbaeocistina, baeocistina, norpsilocina,
aeruginascina y otras triptaminas de la misma familia, en cantidades pequeñas y muy variables. Se habla
mucho de que ese conjunto explicaría diferencias de efecto entre materiales —una idea análoga al "efecto
séquito" del cannabis— pero la evidencia humana para eso es **prácticamente inexistente**. Este módulo
ordena qué son, cuánto hay y qué se sabe de verdad.

**Alcance (línea roja):** química analítica y farmacología descriptiva. No hay aquí ninguna guía de
producción, cultivo, extracción o síntesis.

Términos: **N-metilación** = número de grupos metilo en el nitrógeno de la cadena lateral; es lo que
distingue a estos compuestos entre sí. **cuaternario (quaternary ammonium)** = nitrógeno con cuatro
sustituyentes y carga permanente. **congénere (congener)** = compuesto de la misma familia estructural.

## La familia, ordenada por metilación

| Compuesto | Estructura | Fósforo | Masa molar (g/mol) | Nota |
|---|---|---|---|---|
| Norbaeocistina | 4-fosforiloxi-triptamina (NH₂) | Sí | 256,20 | Sin metilar |
| Baeocistina | 4-fosforiloxi-N-metiltriptamina | Sí | 270,22 | Monometilada |
| **Psilocibina** | 4-fosforiloxi-N,N-dimetiltriptamina | Sí | 284,25 | Dimetilada — la mayoritaria |
| Aeruginascina | 4-fosforiloxi-N,N,N-trimetiltriptamina | Sí | 298,3 (catión) | Trimetilada, amonio cuaternario |
| Norpsilocina | 4-hidroxi-N-metiltriptamina | No | 190,24 | Análogo desfosforilado de baeocistina |
| **Psilocina** | 4-hidroxi-N,N-dimetiltriptamina | No | 204,27 | La molécula activa (`251`) |
| 4-HO-TMT | 4-hidroxi-N,N,N-trimetiltriptamina | No | 218,3 (catión) | Análogo de aeruginascina |

Patrón útil para leer un cromatograma: los fosforilados son mucho más polares y eluyen antes; dentro de cada
grupo, a más metilación, más retención en fase reversa.

## Cuánto hay realmente

Datos de literatura sobre *Psilocybe cubensis* cultivada (Gotvaldová et al., *Drug Testing and Analysis*,
2021, y trabajos posteriores sobre variabilidad entre cepas, *Journal of Fungi*, 2025–2026). Rangos
reportados, **no valores garantizados**:

| Compuesto | Rango reportado (mg/g) | Comentario |
|---|---|---|
| Psilocibina | ~0,2 – 5,3 | Enorme dispersión entre cepas y flushes |
| Psilocina | ~0,7 – 3,5 | Suele venir de degradación de psilocibina |
| Baeocistina | ~0,14 – 0,88 | Un orden de magnitud por debajo |
| Norbaeocistina | ~0,04 – 0,16 | Traza |
| Aeruginascina | ~0,03 – 0,05 | Traza; más asociada a *Inocybe aeruginascens* |

Lectura: **son compuestos minoritarios**, típicamente entre el 1 % y el 10 % del contenido de psilocibina.
Esa proporción es la razón principal para dudar de las narrativas de "efecto séquito" fuerte: para que un
compuesto en traza module el efecto, tendría que ser mucho más potente que el mayoritario, y eso no está
demostrado.

## Qué se sabe farmacológicamente (poco, y hay que decirlo)

| Compuesto | Estado del conocimiento | Nivel de evidencia |
|---|---|---|
| Baeocistina | Se propuso actividad psicoactiva por analogía estructural; un estudio en ratón no encontró el efecto conductual típico de psicodélicos | `[animal]`, sin datos humanos controlados |
| Norbaeocistina | Sin caracterización farmacológica humana | `[preclínico escaso]` |
| Aeruginascina | Amonio cuaternario: por carga permanente, es poco probable que cruce la barrera hematoencefálica; la hipótesis del "efecto distinto" es especulación | `[teórico]` / `[anecdótico]` |
| Norpsilocina | Actividad en 5-HT2A descrita in vitro; sin datos humanos | `[in vitro]` |

Conclusión honesta: a agosto de 2026, **no existe evidencia clínica controlada en humanos de que estos
congéneres cambien el efecto de la psilocibina**. Cualquiera que lo afirme está extrapolando.

## Cómo se mide / cómo se comprueba

Los congéneres exigen más sensibilidad que la psilocibina, porque están en traza:

| Elemento | Requisito |
|---|---|
| Técnica | LC-MS/MS en MRM; HPLC-DAD casi nunca alcanza para los minoritarios |
| Columna | C18 polar-embedded o HILIC (los fosforilados son muy polares) |
| Patrones | Certificados de cada congénere — el cuello de botella real; muchos no están disponibles comercialmente |
| Cuantificación sin patrón | Solo semicuantitativa: se reporta como "estimado frente a psilocibina", nunca como valor absoluto |
| Estándar interno | Deuterado de psilocibina/psilocina; para congéneres se acepta el más cercano, declarándolo |
| LOQ objetivo | ≤ 0,01 mg/g para tener sentido en traza |
| Unidad | mg/g base seca, con la humedad reportada |

Regla de oro aplicada aquí: **sin patrón de referencia no hay cuantificación, hay estimación** (`70`). Muchos
"perfiles de alcaloides" que circulan son áreas de pico relativas presentadas como concentraciones.

## Ejemplo aplicado (ILUSTRATIVO) — perfil de un material de investigación

```
Lote PSY-2026-007, material seco homogeneizado, LC-MS/MS MRM, base seca

  Psilocibina      6,91 mg/g   (patrón certificado)
  Psilocina        0,74 mg/g   (patrón certificado)
  Baeocistina      0,31 mg/g   (patrón certificado)
  Norbaeocistina   0,08 mg/g   (SEMICUANTITATIVO — sin patrón, estimado vs psilocibina)
  Aeruginascina    < 0,02 mg/g (< LOQ)

  Baeocistina como % de psilocibina = 0,31 / 6,91 = 4,5 %
```

Fíjate en la línea de norbaeocistina: marcada como semicuantitativa. Esa honestidad es lo que separa un
informe analítico de un folleto.

## Errores comunes

- **Vender "efecto séquito" de triptaminas como hecho.** No hay evidencia clínica humana que lo sostenga.
- **Reportar congéneres sin patrón como si fueran cuantitativos.** Es el error más frecuente en este campo.
- **Asumir que aeruginascina es psicoactiva por vía oral.** Su carga permanente lo hace improbable; es
  hipótesis, no dato.
- **Usar un método de UV para traza.** No tiene la sensibilidad; los picos minoritarios se pierden en ruido.
- **Comparar perfiles entre laboratorios con métodos distintos.** Sin método común, los perfiles no se
  comparan.
- **Olvidar la base seca.** Los rangos de literatura están casi siempre en base seca.

## Conexión con otros módulos

→ `251-psilocibina-y-psilocina-quimica.md` — las dos moléculas principales.
→ `253-biosintesis-de-psilocibina.md` — por qué existen estos intermediarios.
→ `254-variabilidad-de-potencia-entre-especies.md` — la dispersión de contenidos.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — el método que los detecta.
→ `70-patrones-de-referencia-y-trazabilidad.md` — por qué sin patrón no hay número.
→ `183-efecto-sequito-que-dice-la-evidencia.md` — el mismo debate en cannabis, mejor documentado.
