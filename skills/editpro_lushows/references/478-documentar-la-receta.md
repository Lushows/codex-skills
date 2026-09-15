# 478 — Documentar la receta

> **Un efecto sin ficha se vuelve a inventar cada vez.** Y cada reinvención sale un poco distinta, así
> que a los seis episodios ya no tienes un efecto: tienes cinco primos parecidos. Este módulo es el
> artefacto más aburrido del bloque y el que más horas devuelve: **la ficha escrita de un efecto**, con
> sus números exactos, sus costes medidos y sus contraindicaciones.

**Frontera.** La **plantilla ejecutable** —el fragmento parametrizado listo para instanciar— es `88`.
El **render reproducible** es `132`. El **diario de aprendizajes** de la cuenta es `306`. La ficha no
sustituye a ninguno: es lo que hace que los tres sigan significando lo mismo dentro de un año.

---

## 1. Qué lleva una ficha

Ocho campos, y ninguno es opcional:

```
NOMBRE        como lo llamas tu, siempre igual
QUE HACE      una frase. Si no cabe en una, el efecto no esta definido
CUANDO        el sitio donde paga (471)
NUNCA         donde esta prohibido, y por que
PARAMETROS    los numeros exactos, separando fijos de variables
CODIGO        el filtro real, copiable, que se ejecuta
COSTE MEDIDO  render, peso, y si sobrevive a la recompresion (472, 476)
TRAMPAS       lo que falla en silencio
```

El campo **NUNCA** es el que casi nadie escribe y el que más veces salva el vídeo. Un efecto sin
contraindicaciones escritas acaba puesto en todas partes, porque no hay nada que diga que no.

---

## 2. La ficha del destello, completa

Todo lo que sigue está medido en los módulos anteriores de este bloque, no estimado.

```
NOMBRE        destello
QUE HACE      un fogonazo corto de luz sobre TODO el cuadro, anclado a una palabra;
              es el flash de una camara de archivo, no un lens flare

CUANDO        uno por bloque como maximo, en la palabra que decide el bloque;
              el mas fuerte en el golpe de la promesa

NUNCA         - en los primeros ~7 s: ahi la atencion ya la tienes
              - sobre un elemento lavado contra su fondo (<10 de diferencia de luz)
              - en un tramo de "ruido" (mas de 4 elementos a la vez)
              - sobre una imagen ya quemada: no le queda recorrido de brillo
              - mudo: un fogonazo sin golpe se lee como un error del reproductor

PARAMETROS    tecnica         campana de Gauss sobre brillo y contraste   FIJO
              ancho           0,075 s de medio ancho                      FIJO
              contraste/brillo 1,4                                        FIJO
              offset          -0,04 / -0,05 s (entra ANTES de la palabra) FIJO
              ancla           la palabra                                  contenido
              fuerza          0,14 - 0,22                                 VARIABLE

CODIGO        bri = "+".join(f"{f:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))" ...)
              con = "+".join(f"{f*1.4:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))" ...)
              f"[{ultimo}]eq=brightness='{bri}':contrast='1+{con}':eval=frame[fx]"

COSTE MEDIDO  render: despreciable (es una expresion por fotograma, no un filtro de imagen)
              peso:   despreciable (no anade alta frecuencia)
              llega:  SI. Es luminancia a gran escala; sobrevive a 400 kbps (476)
              firma:  deja un pico de +17 a +32 de YAVG, detectable en el render (477)

TRAMPAS       - sin 'eval=frame' el destello NO OCURRE y el render sale perfecto
              - la coma de pow() hay que escaparla: rompe el grafo de filtros
              - un escalon en vez de campana se lee como fotograma corrupto
```

Compárala con la ficha de un efecto que **no** merece la pena y verás para qué sirve el formato:

```
NOMBRE        grano sobre la mezcla final
COSTE MEDIDO  render: +152%   peso: +55%   cambio de imagen: PSNR 43,6 dB (apenas)
              llega:  NO como lo hiciste. A 400 kbps el codec lo convierte en otra cosa
VEREDICTO     solo en piezas que NO se recompriman. En redes, no.
```

Cuatro líneas y la discusión se acabó. Sin ficha, esa misma discusión vuelve cada tres meses.

---

## 3. Dónde vive la ficha

**Pegada al código que la ejecuta.** No en un documento aparte, no en una carpeta de notas, no en tu
cabeza. La razón es simple: un documento separado deriva del código y no hay nada que lo impida; un
comentario encima de la función se actualiza cuando alguien toca la función, porque lo tiene delante.

Así está resuelto en el motor del piloto, y este es exactamente el tono que hay que copiar:

```python
# ── DESTELLOS: el gancho visual de este canal ────────────────────────────
# Un fogonazo corto de luz sobre TODO el cuadro, anclado a una palabra. Es el
# flash de una camara de archivo, no un lens flare: sube brillo y contraste
# durante ~0,12 s y vuelve. Se hace con una campana de Gauss sobre 't', que
# es lo unico que evita el escalon de un interruptor.
#
# Ojo: 'eq' solo evalua expresiones si se le pide 'eval=frame'. Sin eso lee
# el valor una vez al iniciar y el destello no ocurre.
```

Y este otro, que es la forma correcta de anotar un coste:

```python
# ffmpeg reescala cada elemento EN CADA FOTOGRAMA. Con recortes de archivo de
# 3.000-8.000 px mostrados a 600, eso son cuatrocientas reducciones identicas por
# elemento: medido, una escena de 16 s con 14 elementos tardaba 7 minutos.
```

**«Medido».** Esa palabra es la diferencia entre documentación y opinión. Un coste sin la condición en
la que se midió —qué material, qué máquina, qué escena— no es un dato: es una impresión con decimales.

---

## 4. La regla de que ficha y código no pueden discrepar

Si la ficha dice `ancho 0,075 FIJO` y el código tiene un 0,095 suelto, una de las dos miente y siempre
miente la ficha, porque el código es el que se ejecuta. Por eso la comprobación de deriva del `473` no
es opcional:

```bash
grep -h -A10 '^DESTELLOS = {' */guion_visual.py \
  | grep -oE '"(fuerza|ancho|offset)": [-0-9.]+' | sort | uniq -c
```

Corrido sobre el piloto, `ancho` ya tiene **dos** valores (0,09 y 0,095) donde la ficha declara uno.
Con dos episodios eso se arregla en treinta segundos. La ficha no sirve para que nadie se desvíe: sirve
para que la desviación **se pueda ver**.

---

## 5. Cuándo se escribe

| Momento | Qué se escribe |
|---|---|
| Primera vez que usas un efecto | nada: es un experimento (`473`) |
| Segunda vez | el nombre, qué hace y el código |
| **Tercera vez** | **la ficha entera, con los costes medidos** |
| Cuando lo descartas | la ficha del descarte: por qué no, con el número |

La última fila es la que más gente se salta y la que más tiempo ahorra. **Un «no» bien documentado vale
tanto como un «sí»**, porque lo que vuelve cada tres meses no son los efectos que funcionan: son los que
parecen buena idea y no lo son.

---

## Errores frecuentes

1. **No escribir la ficha porque «me acuerdo».** Te acuerdas del efecto, no de los números.
2. **Guardarla en un documento aparte del código.** Deriva, y nada lo impide.
3. **Apuntar el coste sin la condición en que se midió.** Qué material, qué máquina, qué duración.
4. **No separar parámetros fijos de variables.** Si no está escrito cuál es la perilla, todas lo son.
5. **Dejar vacío el campo NUNCA.** Un efecto sin contraindicaciones acaba puesto en todas partes.
6. **No documentar las trampas.** El `eval=frame` te va a costar media hora dos veces si no está escrito.
7. **No fichar los descartes.** La misma mala idea vuelve cada tres meses con ropa nueva.
8. **Escribir la ficha la primera vez.** La primera vez es un experimento; documentar un experimento es
   burocracia.
9. **Dar por buena una ficha que el código contradice.** El código es el que se ejecuta.
10. **Escribir «queda bien» en el campo QUE HACE.** Eso no es una descripción, es una impresión.
11. **Copiar una ficha de otro proyecto sin volver a medir el coste.** Otro material, otro coste.

---

## Relacionado

- `88` — **plantillas reutilizables**: el efecto parametrizado y ejecutable. La ficha lo describe; la
  plantilla lo instancia.
- `473` — el sistema de marca y la comprobación de deriva que valida la ficha.
- `472` — de donde salen los costes medidos que van en la ficha.
- `476` — de donde sale el campo «llega / no llega».
- `477` — de donde sale el campo «firma detectable en el render».
- `132` — render reproducible; `136` — scripts que se explican solos; `139` — mantener un pipeline vivo.
- `306` — el diario de aprendizajes: donde van los resultados de audiencia, que es otra libreta.
- `429` — cuándo quitar un efecto: los seis disparadores y **cómo se documenta una retirada**, que es la
  ficha del «no» de la que habla el §5.
- `420` — la forma de enunciar una hipótesis de efecto, que es de donde sale el campo QUE HACE.
- `96` — versiones y nomenclatura.
- `canales/249-extender-el-motor-sin-romperlo` — cómo se añade algo nuevo a un motor ya documentado.
- `canales/169-el-informe-de-auditoria` — el otro documento que produce este oficio.
