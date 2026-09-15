# 48 — Escalas y ritmo tipográfico

La diferencia entre un texto que se ve "profesional" y uno "amateur" rara vez es la fuente: es el ESPACIO. Tamaños con lógica, interlineado correcto y líneas de la medida justa. Esto es matemática al servicio de la lectura.

## Términos clave (en simple)
- **Leading / interlineado**: el espacio vertical entre líneas (en CSS, `line-height`). Demasiado junto ahoga; demasiado suelto desconecta.
- **Tracking**: espacio uniforme entre TODAS las letras de un texto.
- **Kerning**: ajuste entre dos letras específicas (ver 46).
- **Medida** (measure): el ancho de una columna de texto, medido en caracteres por línea.
- **Escala tipográfica**: el conjunto de tamaños que usarás, generados con una proporción.

## La escala modular (tamaños con lógica)
En vez de inventar tamaños al azar (15, 19, 23, 31...), eliges UN tamaño base (ej. 16px) y una RAZÓN, y multiplicas. Cada nivel = el anterior × la razón. Resultado: una escala armónica.

| Razón | Nombre | Carácter | Uso típico |
|---|---|---|---|
| 1.125 | Segunda mayor | Sutil, denso | Dashboards, mucha info |
| 1.200 | Tercera menor | Equilibrado | UI general, web de producto |
| 1.250 | Tercera mayor | Claro, cómodo | Landing pages, blogs |
| 1.333 | Cuarta | Dramático | Editorial, marketing |
| 1.414–1.618 | Aumentada / áurea | Muy dramático | Posters, hero impactante |

Ejemplo con base 16px y razón 1.25:
16 → 20 → 25 → 31 → 39 → 49 → 61 px. Esos son tus tamaños. Redondea para limpieza (16, 20, 25, 31, 40, 49, 61). Para más contraste, usa una razón mayor en titulares y una menor en el rango de texto.

## Interlineado (leading) ideal
Regla base: **cuanto más pequeño y más larga la línea, MÁS interlineado.** Cuanto más grande el titular, MENOS (líneas más juntas).

| Elemento | line-height recomendado |
|---|---|
| Cuerpo de texto | 1.4 – 1.6 (web ~1.5; lectura larga 1.6) |
| Titulares grandes | 1.0 – 1.2 (apretado, compacto) |
| Subtítulos | 1.25 – 1.35 |
| Texto en mayúsculas | un poco más (las mayúsculas piden aire) |
| Caption pequeño | 1.4 – 1.5 |

Error clásico: dejar el cuerpo en 1.2 (se ahoga, cansa) o el titular en 1.6 (se desarma en líneas flotantes).

## Medida de línea (la regla de oro de la legibilidad)
**45 a 75 caracteres por línea** (espacios incluidos). El óptimo ronda los **66**. Para columnas múltiples, 40–50.

- Líneas **muy largas** (>80–90): el ojo se pierde al saltar de renglón, cansa.
- Líneas **muy cortas** (<40): el ojo salta demasiado seguido, ritmo entrecortado.
- En web: controla con `max-width` de la columna de texto (aprox. **60–75ch** o ~600–720px para cuerpo a 18px). NO dejes párrafos a todo el ancho de la pantalla.

Truco rápido: si una línea de cuerpo cruza toda una pantalla de laptop, es DEMASIADO larga. Pon un ancho máximo.

## Ritmo vertical / baseline
Idea: que todos los espacios verticales (entre párrafos, antes de títulos, etc.) sean múltiplos de una misma unidad base (ej. 8px). Eso crea un "ritmo" donde todo se alinea a una grilla invisible y la página se siente ordenada.
- Define una **unidad base** (4 u 8 px).
- Márgenes, padding e interlineados = múltiplos de esa unidad (8, 16, 24, 32...).
- Resultado: armonía sin que el ojo sepa por qué.

## Tracking: cuándo tocarlo
- **Mayúsculas y textos pequeños** (etiquetas, kickers): ABRE un poco el tracking (las mayúsculas se aprietan). +5% a +10%.
- **Titulares muy grandes**: a veces CIERRA ligeramente el tracking (se ven más sólidos).
- **Cuerpo de texto**: déjalo en 0 (default). No toques el tracking del párrafo; la fuente ya está espaciada para eso.

## Detalles de pulido (los que se notan)
- [ ] Usa **comillas tipográficas** « » " " y apóstrofo ', no las rectas " '.
- [ ] **Guion largo** (—) para incisos, no el corto.
- [ ] Evita **viudas y huérfanas** (una palabra sola colgando al final/inicio).
- [ ] No justifiques texto en web sin partición de palabras (genera "ríos" de espacio feos). Mejor alineado a la izquierda.
- [ ] **Sangría o espacio** entre párrafos, no ambos.

## Checklist de ritmo
- [ ] ¿Mis tamaños salen de una escala (no inventados)?
- [ ] ¿Cuerpo con line-height ~1.5 y titular ~1.1?
- [ ] ¿Líneas de 45–75 caracteres (puse max-width)?
- [ ] ¿Espacios verticales en múltiplos de 8?
- [ ] ¿Comillas y guiones tipográficos correctos?

## Siguiente paso
Aplica esta escala a los roles de jerarquía (ver 43). Ajusta los valores según el medio: la pantalla pide cuerpo 16px+ y rem (ver 47). Con la escala lista, ya tienes el sistema tipográfico completo para documentar en el manual de marca (ver 44).
