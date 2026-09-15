# 153 — Tipografía multilingüe

Tu marca crece y de repente el texto aparece en inglés, portugués, francés… o tu cliente en Colombia necesita acentos perfectos y la "ñ" bien dibujada. O abres mercado y necesitas árabe, chino o cirílico. Una fuente que se ve increíble en español puede romperse feo en otro idioma. Este módulo te enseña a no quedar mal cuando la marca habla varias lenguas.

## Empecemos por casa: español bien hecho
Aunque solo trabajes en español, hay caracteres que MUCHAS fuentes (sobre todo gratis o de moda) dibujan mal o no traen:

- [ ] **Ñ / ñ** — que la tilde de la eñe esté bien proporcionada, no pegada ni gigante.
- [ ] **Vocales acentuadas:** á é í ó ú — y que NO choquen con la línea superior en mayúsculas (Á, É).
- [ ] **Ü / ü** (diéresis: pingüino, vergüenza).
- [ ] **Signos de apertura: ¿ ¡** — exclusivos del español. Muchas fuentes display los olvidan. Sin ellos, tu titular "¡Bienvenido!" queda cojo.
- [ ] **Comillas angulares « »** (usadas en español formal, ver 159).

Prueba rápida antes de adoptar una fuente: escribe **"¡Pingüino español: ¿añejo o niñez?"** Si todo se ve perfecto, la fuente cubre bien el español.

## La regla de oro multilingüe
**No mezcles fuentes distintas para distintos idiomas si puedes evitarlo.** El texto en inglés y en español deben sentirse de la MISMA marca. Por eso eliges fuentes con buena **cobertura de glifos** (cuántos caracteres/idiomas trae el archivo).

| Cobertura | Qué cubre | Para qué |
|---|---|---|
| Latin basic | Inglés y poco más | Insuficiente para español serio |
| Latin Extended | Español, portugués, francés, alemán, polaco, etc. | Lo mínimo para LatAm + Europa occidental |
| Latin + Cyrillic + Greek | Suma ruso/ucraniano y griego | Marca europea amplia |
| Pan-script | Suma árabe, hebreo, devanagari, CJK… | Marca global |

## Scripts no latinos (cuando el alfabeto cambia)
| Script | Idiomas | Reto principal |
|---|---|---|
| **Cirílico** | Ruso, ucraniano, búlgaro, serbio | Formas propias; el serbio cambia letras en cursiva |
| **Griego** | Griego | Sistema de acentos propio |
| **Árabe** | Árabe, persa, urdu | Se lee de DERECHA a izquierda; letras se unen y cambian de forma según posición |
| **Hebreo** | Hebreo | De derecha a izquierda; sin minúsculas |
| **Devanagari** | Hindi, marathi | Letras cuelgan de una línea superior |
| **CJK** | Chino, japonés, coreano | Miles de caracteres; archivos enormes |

Para estos casos NO traduzcas la fuente latina "a ojo". Necesitas:
1. Una fuente diseñada por especialistas de ESE script, o
2. Una superfamilia pensada multi-script (mismo ADN visual en todos los idiomas).

## Fuentes con buena cobertura (reales, junio 2026)
| Fuente | Cobertura | Notas |
|---|---|---|
| **Noto** (Google) | TODOS los idiomas del mundo | "No tofu" (sin cuadritos vacíos); por script: Noto Sans Arabic, etc. Gratis |
| **IBM Plex** | Latin, Cyrillic, Greek, Arabic, Thai, Devanagari, CJK | Superfamilia coherente, gratis |
| **Inter** | Latin Extended completo | UI multilingüe occidental |
| **Source Sans/Serif** (Adobe) | Latin, Cyrillic, Greek + Source Han para CJK | Gratis, robusta |
| **Roboto** + variantes | Amplísima | Estándar Android |

Para marca de pago multilingüe: familias de Dalton Maag o Commercial Type suelen ofrecer extensiones por script.

## Consistencia entre idiomas (el detalle pro)
Cuando un mismo texto convive en varios idiomas:
- **Igualar el "color" del texto:** el árabe o el devanagari pueden verse más "pesados" que el latino al mismo tamaño. Ajusta tamaño/peso por idioma para que la mancha de texto se sienta igual.
- **Altura-x y alineación vertical** coherentes entre scripts (ver 40 anatomía).
- **Dirección:** en árabe/hebreo todo el layout se espeja (botones, flechas, alineación). En web: `dir="rtl"`.
- **Expansión de texto:** el alemán y el español son ~20–30% más largos que el inglés. Diseña botones y cajas con holgura o se desbordarán.

```css
:root { font-family: "IBM Plex Sans", "IBM Plex Sans Arabic", sans-serif; }
[lang="ar"] { font-size: 1.1em; }   /* compensa la densidad del árabe */
[dir="rtl"] { text-align: right; }
```

## Ejemplo trabajado
Marca de turismo colombiana que se expande a EE.UU. y Brasil. Idiomas: español, inglés, portugués — todos latinos. Solución simple: una sola fuente con **Latin Extended** (ej. Inter o Plex Sans), que ya cubre ñ, ç, ã, acentos y signos ¿¡. Botones diseñados con 25% de holgura para la expansión del español/portugués. Sin necesidad de scripts extra. Si mañana abren mercado en Medio Oriente, suman *Plex Sans Arabic* — misma familia, layout espejado, coherencia total.

## Siguiente paso
Lista los idiomas que tu marca usa HOY y los que usará en 2–3 años. Elige UNA fuente (o superfamilia) que los cubra a todos antes de comprometerte (revisa 49 licencias y 41 elegir tipografías). Haz la prueba del "¡Pingüino!" para el español y un texto real para cada idioma extra.
