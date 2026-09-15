# 205 · El primer fotograma

**Qué resuelve:** en el episodio largo el primer fotograma es un detalle: el espectador ya
ha decidido entrar y lo que ve es una portada aparte (`99`). En vertical **el primer
fotograma es la miniatura**, se muestra fijo mientras el vídeo carga, y se ve antes de que
suene la voz, antes de que entre el primer elemento y antes de que arranque la música. Es
lo único que se juzga antes de haber visto nada. Y el del episodio actual está vacío.

`editpro 94` cubre miniatura y portada como pieza de diseño y `94` de esta skill el gancho
de dinero como decisión de guion. Aquí sólo el fotograma **cero del render**: qué hay en
él hoy, medido, y qué tiene que haber.

---

## Lo que hay hoy, medido

Extraído del render real:

```bash
ffmpeg -v error -i ep01-lustig/salida/_mudo.mp4 -frames:v 1 -y f0.png
```

| | Fotograma 0 de `ep01-lustig` |
|---|---|
| Elementos vivos | **0** |
| Cobertura | **0,0 %** |
| Luz media | 71,0 |
| Desviación (contraste) | 32,6 |
| Ventana 9:16 centrada (656–1264) | luz 78,0 · desv 41,5 |
| Tercio inferior | luz 37,9 · **desv 8,3** |

Un fondo, y nada más. El tercio inferior con desviación 8,3 es una superficie
prácticamente plana: no hay forma, no hay borde, no hay dónde mirar.

Y no es que llegue tarde por poco:

| Instante | Elementos vivos | Cobertura |
|---|---|---|
| t = 0,00 s (fotograma 0) | 0 | 0,0 % |
| t = 0,04 s (fotograma 1) | 0 | 0,0 % |
| t = 0,40 s (fotograma 10) | 1 | 6,2 % |
| t = 0,80 s (fotograma 20) | 3 | **53,4 %** |

El primer elemento (`casilla_hospital`) entra a t = 0,10 y cruza el umbral de opacidad a
**t = 0,21 — fotograma 5**. El cuadro no está lleno hasta el fotograma 20. **La miniatura
del corte vertical es medio segundo anterior a que empiece el vídeo.**

El auditor ya lo señalaba y nadie lo leyó como lo que era:

```
--- tramos con el cuadro casi vacío (<14% cubierto) ---
   0.00 -   0.80  (0.80 s)  muerte    max 13.0%  "el once de"
```

Ese aviso está escrito para 16:9, donde 0,8 s flojos son un defecto de ritmo. En vertical
son **la portada**.

## Por qué el fondo no sirve de miniatura

Un fondo del canal es una fotografía de archivo tratada, oscurecida y con viñeta (`50`,
`53`) precisamente para que los elementos se despeguen de ella. Es decir: está diseñada
para **no** llamar la atención. Como miniatura hace exactamente lo contrario de lo que
hay que hacer.

Y la voz tampoco llega a tiempo: la primera palabra empieza en **t = 0,227**. Durante los
primeros cinco fotogramas el vídeo no tiene ni imagen ni sonido.

## Lo que tiene que haber

El fotograma 0 del corte vertical es una composición deliberada, no el primer instante de
una escena. Tres cosas, y las tres a plena opacidad desde el fotograma cero:

| Elemento | Registro (`201`) | Por qué |
|---|---|---|
| La **cifra o la palabra del gancho** | arriba, `y ≈ 500` | Es lo que hace parar el pulgar; arriba porque abajo aún hay dedo |
| El **rostro o el objeto** de la historia | centro, `y ≈ 800` | Da la cara de lo que se va a contar |
| Nada más | — | Una miniatura con tres ideas no tiene ninguna |

Dos elementos, no tres: el mismo límite de pila que fija `203`. Y la regla dura:

> **El fotograma 0 no tiene fundido de entrada.** Los elementos del gancho entran con
> `dur_entrada = 0` y opacidad 1 desde el primer fotograma. Todo lo demás del corte sigue
> entrando con su gesto.

En el motor eso es un caso especial, y hay que escribirlo como caso especial porque la
subida de 0,30 s está fijada en `motor.py` para todo:

```python
# el gancho del vertical existe ANTES de que el video arranque: es la miniatura
for ele in escena["elementos"]:
    if ele.get("gancho"):
        ele["entrada"], ele["dur_entrada"], ele["desde"] = "duro", 0.0, 0.0
```

## La comprobación, que cuesta un segundo

No hace falta renderizar el corte entero para saber si la miniatura sirve:

```bash
ffmpeg -v error -i corte_vertical.mp4 -frames:v 1 -y f0.png
python - <<'PY'
from PIL import Image, ImageStat
im = Image.open("f0.png").convert("L")
s = ImageStat.Stat(im)
print("luz %.1f  contraste %.1f" % (s.mean[0], s.stddev[0]))
for i, (a, b) in enumerate([(0, 640), (640, 1280), (1280, 1920)]):
    t = ImageStat.Stat(im.crop((0, a, 1080, b)))
    print("  tercio %d: luz %.1f contraste %.1f" % (i+1, t.mean[0], t.stddev[0]))
PY
```

El listón es el mismo que usa el auditor para los elementos lavados: **si el contraste de
un tercio baja de 15, ahí no hay nada**. El fotograma 0 de hoy da 8,3 en el tercio
inferior y 32,6 de media, y el 32,6 es del fondo, no de un objeto.

## Y el que no se ve nunca

Un detalle que sólo aparece cuando se publica: **algunas superficies no usan el fotograma
0 como miniatura**, sino uno elegido por la plataforma o el que suba uno a mano. La regla
del canal es subir miniatura a mano siempre que la red lo permita y componer igualmente el
fotograma 0, porque en las que no lo permiten es lo que se ve, y porque el fotograma 0 es
además **lo que ve quien llega al vídeo con el sonido apagado y el dedo ya subiendo**.

## Errores frecuentes

| Error | Consecuencia medida |
|---|---|
| Dejar que el corte empiece donde empieza la escena | Fotograma 0 con 0 elementos y 0,0 % de cobertura |
| Contar con el fundido de entrada en el gancho | El primer elemento llega al fotograma 5; la miniatura ya se vio |
| Usar el fondo como miniatura | Está tratado para no llamar la atención (`50`, `53`) |
| Esperar a la voz | La primera palabra entra en t = 0,227 |
| Tres ideas en la miniatura | Ninguna; dos elementos es el tope (`203`) |
| Leer el aviso de «cuadro casi vacío» como ritmo | En vertical esos 0,80 s son la portada |
| Componerla en el monitor y no mirar el fotograma | Un `ffmpeg -frames:v 1` cuesta un segundo |

## Relacionado

`201` la columna · `203` densidad en vertical · `94` el gancho de dinero · `99` título,
miniatura y descripción · `247` el primer elemento del plano · `163` contraste
elemento-fondo · `208` el cierre que devuelve al largo · editpro `94` miniatura y portada
