# 60 · Catálogo de efectos

**Qué resuelve:** saber qué hay construido, qué falta, y decidir sin discutir si un
efecto nuevo merece existir o es capricho.

---

## Dónde viven

`piloto/fx.py` declara un diccionario `F` con `nombre → (ancho, alto, cuerpo HTML)`.
Al ejecutarlo escribe `fx/<nombre>.png` con **fondo transparente**
(`--default-background-color=00000000`). A partir de ahí el motor los trata como
cualquier recorte: `{"r": "camiones", "ancla": "toneladas", ...}` en la tabla del
guion visual. No hay una ruta especial para efectos: `motor.buscar()` los encuentra
igual que a los recortes de archivo.

Los que no salen de HTML salen de **PIL** y se guardan en la misma carpeta con la
misma nomenclatura. El motor no distingue: para él todo es un PNG con alfa.

## Inventario actual (19 PNG)

| Nombre | Tipo | Tamaño | Qué dice |
|---|---|---|---|
| `fajo` | dinero | 300×190 | Un fajo dibujado, para apilar o contar |
| `camiones` | comparación | 1180×420 | Tres camiones rotulados = el peso del dinero |
| `altura` | comparación | 760×900 | La pila de fajos contra una montaña |
| `flujo` | diagrama | 1420×430 | Los 5 pasos del lavado, ya completos |
| `sello_prueba` | documento | 600×200 | EXHIBIT en rojo, girado −7° |
| `sello_clasif` | documento | 600×200 | CLASSIFIED |
| `sello_decomiso` | documento | 600×200 | FORFEITED en amarillo dato |
| `usd_00`…`usd_11` | contador | 900×210 | 12 estados de una cifra que sube |

## Lo que falta (y en qué módulo está su receta)

| Falta | Módulo |
|---|---|
| Lluvia de billetes en bucle, contador genérico, barras que crecen, balanza | `61` |
| Redactado (bloques negros), tachado, subrayado, anotación, firma | `62` |
| Escala humana, superficie, tiempo: el método de elegir la comparación | `63` |
| Ruta trazada, punto que late, frontera | `64` |
| Diagrama que se construye paso a paso (hoy `flujo` entra ya completo) | `65` |
| Grano de película, VHS, fotocopia, escaneo | `66` |
| Flash de archivo, foco, halo, proyector | `67` |

## Las tres preguntas antes de construir uno

1. **¿Hay una frase de la voz que se queda sin imagen sin él?**
   Si el efecto no responde a algo que la locución deja abierto, sobra. Un efecto no
   se hace porque quede bonito: se hace porque una cifra no se entiende sin él.
2. **¿Se puede rotular en cuatro palabras?**
   Si no se le puede poner nombre, el espectador tampoco va a identificarlo, y la
   regla del canal es que todo lo que no se identifica lleva rótulo. Un efecto
   irrotulable es ruido con presupuesto.
3. **¿Lo resuelve uno que ya existe cambiándole el texto?**
   Entonces no es un efecto nuevo: es un parámetro. Convertir el cuerpo HTML en una
   función que recibe el texto es siempre mejor que duplicar el bloque.

Si pasa las tres, hay una cuarta: **¿se va a usar en más de un episodio?** Si no,
vive en `episodio<NN>/fx_local.py`, no en `fx.py`. `fx.py` es la biblioteca del canal;
lo que sirve una vez ensucia la biblioteca.

## Estático o serie

| | Estático (1 PNG) | Serie (N PNG con estado) |
|---|---|---|
| Cuándo | El elemento no cambia por dentro; el movimiento lo pone el motor | El elemento **cuenta**, **crece**, **se construye** o **se traza** |
| Coste | 1 archivo | N archivos y N entradas de ffmpeg |
| Ejemplos | `fajo`, sellos, `camiones` | `usd_00…11`, redactado, ruta, diagrama por pasos |
| Trampa | — | Los fades del motor (0,30 s de entrada fijos) se comen estados cortos |

**Regla de coste:** una serie de más de 24 estados casi siempre se puede sustituir por
**un PNG revelado con `crop`** (ver `41` para el mismo truco aplicado al texto) o por
**un PNG en bucle desplazado con `overlay`** (ver `61`, lluvia de billetes). Antes de
generar 40 archivos, preguntarse si el cambio es geométrico: si lo es, es un recorte
que crece, no una serie.

## Nomenclatura

```
familia_concepto[_NN]
fajo · flujo_03 · sello_prueba · usd_07 · ruta_012 · redact_02
```

- Todo en minúscula, sin tildes ni espacios: el nombre viaja por una ruta de archivo
  y por una línea de comandos.
- Los estados llevan **dos dígitos** (`_00`) para que ordenen bien en disco.
- El prefijo es la familia porque `ls fx/` tiene que leerse como un catálogo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Añadir a `fx.py` un efecto de un solo episodio | La biblioteca deja de ser reutilizable en tres episodios |
| Copiar el bloque HTML para cambiar una palabra | Cinco versiones que se desincronizan al primer retoque de estilo |
| Generar 40 estados para algo que crece | 40 archivos y 40 entradas de ffmpeg donde bastaba un `crop` |
| Un efecto sin rótulo | El espectador ve una forma y no sabe qué es: ruido |
| Dar por bueno el PNG porque el script no falló | Chrome captura páginas en blanco sin protestar: verificar el **peso** (`69`) |
| Nombres con tilde o mayúscula | `buscar()` no lo encuentra y el render muere a mitad |

## Relacionado

`61` · `62` · `63` · `64` · `65` · `66` · `67` · `68` · `69` · `43` rótulos · `27` composición de datos
