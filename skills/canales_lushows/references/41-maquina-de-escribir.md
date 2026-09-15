# 41 · Máquina de escribir (efecto teletipo)

**Qué resuelve:** el texto que aparece de golpe se lee como rótulo de plantilla. El
texto que **se escribe** se lee como documento en curso — y en un canal de expedientes
eso no es un adorno: es coherencia. Además añade eventos sin ensuciar (cada línea que
se escribe es movimiento continuo, no un corte más).

---

## Cuándo usarlo (y cuándo no)

| Sí | No |
|---|---|
| Citas textuales de un expediente | Titulares grandes (ahí manda el golpe) |
| Datos de ficha: nombre, expediente, fecha | Cifras de impacto (esas entran de golpe) |
| Listas que se enumeran mientras la voz las dice | Texto sobre un plano que ya tiene mucho |
| Sellos y clasificaciones que "se teclean" | Cuando el espectador debe leer rápido |

**Regla de oro:** la máquina de escribir sirve para lo que la voz está diciendo **en
ese momento**. Si el texto se adelanta o se retrasa respecto a la locución, estorba.

---

## Implementación en ffmpeg

### Método 1 · Revelado progresivo del alfa (el bueno)

Se dibuja el texto completo y se revela recortando su **canal alfa**. Es exacto, no
depende de fuentes monoespaciadas y permite cualquier tipografía.

⚠️ **No se hace con `crop`.** `crop` evalúa `w` y `h` una sola vez al inicializar el
filtro: una anchura con `t` dentro aborta el render con *«Error when evaluating the
expression»*. Quien lo haya copiado de un tutorial se lo ha encontrado. El filtro que sí
evalúa por fotograma es `geq`:

```bash
# El texto vive en un PNG con transparencia (generado con Chrome, como todo).
# Se revela de izquierda a derecha en 1,4 s, a partir del segundo 2,0.
ffmpeg -i fondo.mp4 -loop 1 -i texto.png -filter_complex "
[1:v]format=rgba,
     geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':
         a='if(lt(X, W*clip((T-2.0)/1.4,0,1)), alpha(X,Y), 0)'[txt];
[0:v][txt]overlay=x=120:y=H-260:enable='gte(t,2.0)'
" -y salida.mp4
```

- `clip((T-2.0)/1.4,0,1)` → empieza en el segundo 2,0, tarda 1,4 s y se acota solo
- En `geq` el reloj es **`T` mayúscula**; `X`/`Y` son el píxel y `W`/`H` el tamaño del
  PNG. `alpha(X,Y)` devuelve el alfa original: el antialias del borde se conserva
- El lienzo no cambia de tamaño, así que el `overlay` no se desplaza y no hace falta `pad`
- `geq` evalúa píxel a píxel: el PNG debe medir lo que mide el texto, nunca 1920x1080

**Velocidad correcta:** entre **18 y 26 caracteres por segundo**. Más lento aburre;
más rápido se lee como aparición y pierde el efecto.

```
duración = nº de caracteres / 22
```

### Método 2 · Cursor parpadeante

El cursor es un bloque que sigue al borde del recorte y late a 2 Hz:

```bash
[2:v]format=rgba[cur];
[v][cur]overlay=
  x='120 + TW*min(1,max(0,(t-2.0)/1.4))':
  y='H-260':
  enable='lt(mod(t*2,1),0.55)*gte(t,2.0)'
```

donde `TW` es el ancho del PNG de texto. El cursor debe **desaparecer** cuando la
línea termina de escribirse, salvo que sea la última línea en pantalla.

### Método 3 · Línea a línea

Para una ficha con varios campos, cada línea es un PNG y arranca cuando la anterior
termina. Se declara en la tabla de eventos como elementos encadenados:

```python
{"r": "linea_alias",     "ancla": "chapo",  "offset": 0.10, "escribir": 1.1},
{"r": "linea_expediente","ancla": "chapo",  "offset": 1.35, "escribir": 1.4},
{"r": "linea_distrito",  "ancla": "chapo",  "offset": 2.90, "escribir": 1.2},
```

---

## El sonido va pegado

Sin sonido, el efecto se ve incompleto. La biblioteca ya trae `ob_teletipo.wav`:
golpes cada 0,16 s. Se recorta a la duración exacta del texto y se pega al mismo
tiempo de inicio. **El sonido termina cuando termina el texto**, nunca después.

Para una sola línea corta, `ob_obturador` funciona mejor: un golpe seco al final,
como el retorno de carro.

---

## Tipografía

Monoespaciada siempre: **Consolas** o **Courier New** (ambas en Windows). El efecto
depende de que las letras ocupen lo mismo — con una proporcional, el texto "salta"
al revelarse.

| Uso | Tamaño | Color |
|---|---|---|
| Cita de expediente | 34-42 px | papel `#EDE6D6` |
| Campo de ficha | 26-32 px | `#B3A891` |
| Clasificación / sello | 20-24 px | rojo `#E3120B` |

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Velocidad fija para todos los textos | Uno de 12 caracteres tarda lo mismo que uno de 60 |
| Cursor que sigue latiendo tras acabar | Se lee como que el video se colgó |
| Tipografía proporcional | El texto salta al revelarse |
| Escribir un titular grande | Los titulares van de golpe; escribir es para documento |
| Sonido más largo que el texto | Delata que es un efecto pegado |
| Revelar con `crop=w='iw*…t…'` | El render aborta: `crop` solo evalúa `w`/`h` al iniciar |
| `t` minúscula dentro de `geq` | No existe esa variable ahí; el reloj es `T` |

## Relacionado

`40` el texto como canal principal · `42` tipografía del canal ·
`44` la cifra en pantalla · `47` tipografía cinética · `89` biblioteca de sonido
