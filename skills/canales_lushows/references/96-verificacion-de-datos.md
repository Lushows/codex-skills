# 96 · Verificación de datos

**Qué resuelve:** el error factual es lo único que puede matar un canal de
documentales. Este módulo es el control de calidad: nada aparece en pantalla —ni dicho
ni mostrado— sin fuente, y la imagen tiene que corresponder con lo que dice la voz.

---

## Las tres reglas

1. **Nada en pantalla sin fuente.** Cada cifra, fecha, nombre y lugar del guion tiene
   una entrada en `archivo/fuentes.json` con documento y página.
2. **Cada imagen se verifica dos veces:** por licencia (¿podemos usarla?) y por
   contenido (¿es lo que la voz está diciendo?). Son dos comprobaciones distintas.
3. **Ante la duda, se cae.** Un dato dudoso no se suaviza con "presuntamente": se
   sustituye por uno documentado o se elimina el plano. El episodio no se resiente; la
   credibilidad sí.

## El pasaporte de cada afirmación

Antes de grabar la voz, cada afirmación verificable del guion pasa por esta ficha:

```
AFIRMACIÓN ....... <tal como se dice en la voz>
TIPO ............. cifra / fecha / nombre / lugar / relación / valoración
FUENTE ........... <documento, organismo, página, párrafo>
NIVEL ............ 1 documento · 2 informe · 3 comunicado · 4 prensa   (§ 90)
ESTADO ........... alegado / admitido / probado / estimado
QUÉ MIDE ......... <ingreso bruto, perjuicio, incautado, reclamado…>   (§ 91)
PERIODO .......... <fechas exactas>
CÓMO SE DICE ..... <la fórmula de atribución que exige ese estado>
```

Si el nivel es 4 (prensa), hay dos salidas: subir a nivel 1-2 buscando el documento, o
atribuir en voz ("según la investigación de <medio>"). No hay tercera.

## El chequeo imagen ↔ voz

**El error del Altiplano.** Se usó un mapa etiquetado "Altiplano" que resultaba ser el
altiplano andino —Bolivia y Perú— mientras la voz hablaba del penal mexicano del
Altiplano. Nadie mintió: el nombre coincidía. Ese es exactamente el error que hunde un
canal de documentales, porque el espectador que lo detecta deja de creer todo lo demás.

Por cada plano con material de archivo se responde por escrito:

| Pregunta | Si no hay respuesta clara |
|---|---|
| **¿Qué es exactamente** lo que se ve? (objeto, lugar, edificio) | No se usa |
| **¿Dónde** fue tomada? (país, ciudad, coordenadas si las hay) | No se usa |
| **¿Cuándo**? ¿Es de la época que narra la voz? | No se usa, o se rotula la fecha real |
| **¿Quién** aparece? ¿Es la persona que la voz nombra? | No se usa |
| **¿La voz en este segundo dice justo eso?** | Se recoloca el plano |
| **¿Es una reconstrucción nuestra?** | Se rotula "reconstrucción · Paper Empires" |

Trampas concretas: **topónimos repetidos** (el mismo nombre en dos países), banderas y
uniformes del país equivocado, edificios modernos en una escena de hace treinta años,
billetes de una serie posterior a los hechos, mapas con fronteras de otra década,
matrículas y señales que delatan otro lugar.

## Verificación de licencia

Cada pieza, antes de entrar a `archivo/`:

- Origen exacto y **página del ítem**, no la del buscador.
- Licencia textual copiada tal cual (dominio público, CC0, CC BY, etc.).
- Si es Wikimedia Commons: abrir la ficha del archivo y leer la licencia **de ese
  archivo**; estar en Commons no significa que sea libre.
- Si es obra del gobierno federal de EE.UU.: comprobar que la foto es **suya** y no una
  imagen de agencia reproducida en su web. Es la confusión más común.
- Prohibido siempre: agencia (Getty, AP, Reuters), fotogramas de cine o televisión,
  música con derechos, **caras reales generadas con IA**.
- La ficha se escribe en `archivo/fuentes.json` en el momento de descargar, no después.

## El barrido antes del render

Se hace sobre el guion cerrado y la tabla de eventos, antes de renderizar:

1. **Extraer todas las cifras y fechas** del guion (buscar dígitos, `%`, `$`, "millones",
   "mil"). Cada una debe tener su entrada en `fuentes.json`. Sin excepción.
2. **Extraer todos los nombres propios** y comprobar grafía y pronunciación fijada.
3. **Recorrer la tabla de eventos** y confirmar que cada elemento visual tiene `id` de
   fuente y que su descripción coincide con la frase que suena en ese segundo.
4. **Comprobar los estados** (alegado / probado) contra la fórmula usada en la voz.
5. **Revisar los rótulos**: todo objeto no identificable lleva etiqueta (regla del canal).
6. **Grilla de fotogramas** al final: leer todos los textos en pantalla buscando erratas,
   fechas cruzadas y rótulos que no corresponden al plano.

## Qué se hace con lo dudoso

| Caso | Decisión |
|---|---|
| Cifra que sólo aparece en prensa | Se atribuye en voz o se cae |
| Dos fuentes con cifras distintas | Se dice el rango, citando ambas; nunca se elige la mayor |
| Anécdota sin documento | Fuera. Aunque sea la mejor del episodio |
| Foto que "parece" del lugar correcto | Fuera. "Parece" no es una verificación |
| Cita traducida de un documento | Se marca como traducción propia y se conserva el original |
| Dato que se desmintió después | Se cuenta el desmentido: suele ser mejor historia |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Imagen que coincide sólo por el nombre | El error del Altiplano: destruye la confianza en todo el episodio |
| Verificar la licencia y no el contenido | Material legal pero factualmente falso |
| Registrar las fuentes al final del proyecto | Se olvida el origen de media docena de piezas y hay que rehacerlas |
| Guardar el enlace en vez del archivo | El respaldo desaparece cuando el sitio cambia |
| Suavizar un dato flojo con "presuntamente" | No arregla nada: sigue siendo un dato sin fuente |
| Fecha de la foto sin comprobar | Un edificio o un coche del año equivocado en pantalla |
| Dar por buena una IA como fuente | No es fuente de nada; sólo pista para ir al documento |

## Relacionado

`90` fuentes primarias · `91` leer un expediente · `92` el aporte original ·
`43` rótulos y etiquetas · `99` descripción con fuentes citadas
