# 159 · Cómo se caza un fallo que no avisa

**Qué resuelve:** el método. Sin traza, sin excepción y sin línea que señalar, la
tentación es **adivinar y parchear**. Eso alarga el fallo; no lo cierra.

---

## El método, en cuatro pasos

Los nueve casos del bloque se cerraron con la misma secuencia. Ninguno se cerró
cambiando parámetros a ver qué pasaba.

### 1 · Reproducir antes de afirmar

No se toca nada hasta tener **un comando que produzca el fallo a voluntad** y **un
número que lo cuantifique**. «Se ve raro» no es reproducible; «`f_peso` tiene 2,36% del
cuadro en blanco» sí.

```bash
python -c "from fondos import blancos; print(blancos('render/f_peso.png'))"
# 13721
```

⚠️ **Si no es determinista, el número es la reproducción.** El fallo de `151` no se
repite siempre: el mismo fondo en solitario sale limpio. Se reproduce ejecutando la
pasada completa **cinco veces** y contando cuántas ensucian. Eso convierte «a veces
pasa» en «5 de 6 fondos, entre 0,33% y 2,36%», que ya es un hecho.

### 2 · Aislar la pieza

Cortar el pipeline por la mitad y preguntar **de qué lado está el fallo**. Cada corte
descarta la mitad del sistema:

| Pregunta | Comando |
|---|---|
| ¿El PNG ya nace mal? | `python -c "from PIL import Image; Image.open('render/f_peso.png').crop((0,2100,600,2430)).show()"` |
| ¿Es el HTML o es Chrome? | abrir `_f_peso.html` en Chrome normal y mirar |
| ¿Es el filtro o es el material? | renderizar la escena con un solo elemento |
| ¿Es el guion o es el motor? | `python auditar.py ep01-lustig` — mide sin renderizar |
| ¿Es la imagen o es el tiempo? | ver el mudo sin audio (`165`) |

Cuando el corte deja de reducir, la pieza está aislada.

### 3 · Comparar con el caso que sí funciona

Es el paso que más fallos ha cerrado, y el que más se salta. **Casi siempre hay un
hermano sano**: otro fondo limpio, otra escena que sí renderiza, otro alias que sí
resuelve. La diferencia entre los dos es el fallo.

```python
import motor                 # ficha_policial sale mal, ficha_juicio sale bien
for alias in ("ficha_policial", "ficha_juicio"):
    print(f"{alias:<18} {motor.buscar(alias)}")
# ficha_policial     .../piloto/fx/ficha_policial.png       <-- debía ser recortes/
# ficha_juicio       .../piloto/recortes/ficha_juicio.png
```

Ahí estaba `155`, en dos líneas de salida. De la misma forma: `f_piezas` era el único
fondo limpio, y era el que menos superficie filtrada tenía.

### 4 · Convertir el hallazgo en una comprobación

**Un fallo silencioso no está cerrado hasta que existe el código que lo impide.** Esta
es la diferencia entre arreglar y aprender: el fondo se puede volver a ensuciar, el
alias se puede volver a repetir, la próxima tabla de eventos volverá a descartar un
elemento a mitad de escena.

La comprobación tiene que cumplir tres cosas:

- **Mide el contenido**, no el continente (`150`).
- **No grita en falso.** Una que avisa cuando no pasa nada acaba ignorándose, que es
  peor que no tenerla: el corrector de tildes de `auditar.py` se escribió con
  `\b…\b` precisamente por eso, y su comentario lo documenta — *«buscando subcadena,
  'segun' salta dentro de SEGUNDA, 'aqui' dentro de CHECOSLOVAQUIA, 'como' dentro de
  COMODIN y 'anos' dentro de ALGUNOS. Probado contra esos seis casos: cero falsos
  positivos.»*
- **Aborta.** Un aviso que no corta el pipeline se lee dos veces y luego se salta.

```python
def cerrar(nombre, medir, tope, casos_ok, casos_mal):
    """La plantilla: antes de dejarla puesta, la comprobación se prueba contra los
    casos que debe aprobar y los que debe cazar."""
    for c in casos_ok:
        assert medir(c) <= tope, f"{nombre}: falso positivo con {c}"
    for c in casos_mal:
        assert medir(c) > tope, f"{nombre}: no caza {c}"
    print(f"  {nombre}: {len(casos_ok)} OK, {len(casos_mal)} cazados")
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cambiar parámetros «a ver si mejora» | Con un fallo no determinista, una pasada limpia no prueba nada; se da por cerrado y vuelve |
| Envolver en `try/except` para que no moleste | El fallo sigue, sin la única pista que había |
| Arreglar dos cosas a la vez | No se sabe cuál era; las dos se quedan puestas «por si acaso» |
| Renderizar el episodio entero para comprobar | 8 minutos por iteración en un i7 de 2009; se dejan de hacer iteraciones |
| Creer al log | El fallo silencioso no está en el log; por eso es silencioso |
| Arreglar sin medir antes | No hay forma de demostrar que quedó arreglado |

## La libreta

Cada caso cerrado deja tres líneas, y de ahí salen los módulos `151`–`158`:

```
FALLO      · qué se veía (con el número)
CAUSA      · la línea concreta, con archivo
GUARDIA    · el código que lo impide, y dónde vive
```

Un ejemplo real, completo:

```
FALLO   · 5 de 6 fondos con 0,33-2,36% del cuadro en blanco plano; en el vídeo,
          dos rectángulos grises pegados al borde inferior
CAUSA   · dos feTurbulence en el CSS; a 4320x2430 Chrome no rasteriza y abandona
          trozos. No determinista: en solitario sale limpio
GUARDIA · fondos.blancos() cuenta píxeles con min(RGB)>235 y reintenta 3 veces;
          la textura pasa a degradados repetidos y el grano a ffmpeg
```

**Regla del bloque:** ningún fallo silencioso se cierra dos veces. Si vuelve, es que la
guardia no medía el contenido, o gritaba en falso, o no abortaba.

## Relacionado

`150` el catálogo del fallo silencioso · `151`–`158` los nueve casos ·
`140` medir antes de renderizar · `143` una comprobación que grita en falso se ignora ·
`160` la grilla de fotogramas · `165` la prueba del mudo · `168` reproducir antes de
afirmar · `169` el informe de auditoría
