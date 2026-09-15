# 234 · Deriva de concatenación

**Qué resuelve:** la pregunta que decide si este método aguanta doce minutos. Cada escena
se renderiza aparte y luego se pegan con `concat -c copy`; la voz, en cambio, es **un solo
fichero continuo**. Si al pegar sesenta trozos la imagen se separa de la locución, el motor
por escenas no sirve para episodios largos por muy bien que esté todo lo demás.

Respuesta corta, medida: **el pegado no deriva nada. Lo que deriva es el redondeo a
fotograma, y se corrige con dos líneas.**

---

## De dónde puede salir la deriva

Sólo hay dos candidatos, y conviene separarlos porque tienen arreglos distintos:

1. **El pegado.** `-c copy` reescribe marcas de tiempo. Si las recalculase mal, cada
   costura metería un salto.
2. **El redondeo.** `motor.py:148` convierte la duración declarada en fotogramas enteros:
   ```python
   nf = max(2, int(round(dur * FPS)))
   ```
   A 25 fps el fotograma dura 40 ms, así que cada escena se acorta o se alarga hasta
   **±20 ms** respecto de lo que dice el guion visual. Y esos errores **se suman**.

## El pegado no deriva: medido a doce minutos

No hace falta esperar a tener un episodio largo para comprobarlo. Se cogen las cinco
escenas ya renderizadas de `ep01-lustig` y se pegan doce veces seguidas, que son
**12,7 minutos y 60 costuras**:

```bash
ffmpeg -hide_banner -loglevel error -f concat -safe 0 -i lista12.txt -c copy -y largo.mp4
ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames \
        -show_entries format=duration -of default=nw=1 largo.mp4
```

```
nb_frames=19032
duration=761.280000
esperado: 1586 x 12 = 19032 fotogramas = 761,28 s
```

**Exacto al fotograma.** Ni uno de más ni uno de menos en sesenta costuras. El pegado
tarda 35,7 s para 12,7 minutos —es copia de paquetes, no recodificación— y aporta **cero**
deriva. Ese candidato queda descartado, y con él la duda de fondo: la arquitectura por
escenas escala.

## El redondeo sí deriva, y se ve en el fichero

La deriva real del piloto, calculada sobre la tabla de escenas:

| Escena | ini | fin | dur | `nf` | `nf/25` | error | **acumulado** |
|---|---|---|---|---|---|---|---|
| muerte | 0,00 | 16,15 | 16,15 | 404 | 16,16 | **+10 ms** | +10 ms |
| oficio | 16,15 | 22,88 | 6,73 | 168 | 6,72 | −10 ms | 0 ms |
| nombre | 22,88 | 34,41 | 11,53 | 288 | 11,52 | −10 ms | −10 ms |
| torre | 34,41 | 50,29 | 15,88 | 397 | 15,88 | 0 ms | −10 ms |
| metodo | 50,29 | 63,45 | 13,16 | 329 | 13,16 | 0 ms | −10 ms |

Y no es aritmética de papel: está **en el fichero**. Cada parte empieza con un fotograma
clave, así que las costuras se leen directamente:

```bash
ffprobe -v error -select_streams v:0 -show_packets \
        -show_entries packet=pts_time,flags -of csv=p=0 salida/_mudo.mp4 | grep K
```

```
0.000000  10.000000  16.160000  22.880000  32.880000  34.400000  ...
```

`16.160000` donde el guion dice 16,15. `34.400000` donde dice 34,41. Los `10.000000` y
`32.880000` intercalados no son costuras: son los fotogramas clave que x264 mete cada
250 fotogramas dentro de cada parte.

Diez milisegundos es un cuarto de fotograma. Nadie lo ve. **El problema es que crece.**

## Qué pasa a doce minutos

Un episodio de doce minutos con escenas de la duración media del piloto (12,69 s) tiene
unas **57 escenas**, o sea 57 redondeos encadenados. Es un paseo aleatorio de paso
±20 ms. Simulado 3.000 veces con fronteras al centésimo de segundo, que es la resolución
real de `tiempos.json`:

| | desfase al final | peor desfase del episodio |
|---|---|---|
| media | 69,5 ms | 103,8 ms |
| mediana | 60,0 ms | 100,0 ms |
| percentil 95 | 170,0 ms | 190,0 ms |
| máximo de 3.000 | 290,0 ms | 300,0 ms |

**Dos de cada tres episodios pasan de un fotograma entero de desfase** (64,7 % por encima
de 40 ms), y uno de cada veinte se acerca a los 200 ms — que ya no es «un cuarto de
fotograma que nadie ve»: es un destello que cae después de su palabra y un recorte que
entra tarde a su frase durante el último tercio del episodio. Justo donde peor sienta,
porque el espectador que llega al minuto diez es el que decide el alcance del siguiente
vídeo.

## El arreglo: contar fotogramas absolutos, no duraciones

El error nace de redondear **una duración**. Si en vez de eso se redondean las dos
**fronteras** y se resta, cada escena se cuelga de la línea de tiempo del episodio y el
error deja de acumularse: queda acotado a medio fotograma para siempre.

```python
# motor.py:148 — lo que hay
nf = max(2, int(round(dur * FPS)))

# lo que debería haber
nf = max(2, round(t1 * FPS) - round(t0 * FPS))
```

Simulado sobre los mismos 3.000 episodios de 57 escenas:

| | desfase al final | peor del episodio |
|---|---|---|
| **por duración** (hoy) | 69,5 ms de media · 290 ms el peor | 103,8 ms de media · 300 ms el peor |
| **por frontera absoluta** | 10,0 ms de media · **20 ms el peor** | 20,0 ms de media · **20 ms el peor** |

Medio fotograma, sin excepciones, dure lo que dure el episodio. En `ep01-lustig` las dos
fórmulas dan **exactamente los mismos 404, 168, 288, 397 y 329 fotogramas**: el cambio no
altera el piloto, y por eso se puede meter sin volver a renderizar nada. A cinco escenas
da igual; a cincuenta y siete es la diferencia entre un método que escala y uno que no.

## Lo que la deriva NO es

- **No es un salto visible en la costura.** No hay fotograma negro ni tirón: la imagen
  simplemente ocurre 60 ms antes o después de lo que se está diciendo.
- **No es un problema dentro de la escena.** Los elementos se sitúan en tiempo relativo al
  arranque de su escena, así que dentro de un bloque todo está donde debe. Lo que se
  desplaza es la escena entera, en bloque, y con ella sus veinte elementos.
- **No la ve el auditor.** `auditar.py` mide la tabla de eventos, y en la tabla la escena
  dura 16,15 s. El redondeo ocurre después, al renderizar (`140`, `142`).
- **No la ve el peso ni el total de fotogramas.** Los 1.586 fotogramas del piloto dan
  63,44 s contra 63,454 s de locución: 14 ms al final, justo el tipo de número que se
  descarta como ruido.

## Comprobarlo en un episodio propio

```bash
# 1. donde EMPIEZA de verdad cada escena en el montaje pegado
ffprobe -v error -select_streams v:0 -show_packets -show_entries packet=pts_time,flags \
        -of csv=p=0 salida/_mudo.mp4 | grep K > costuras.txt
```

```python
# 2. contra lo que declara la tabla
import sys; sys.path.insert(0, "ep01-lustig")
from guion_visual import ESCENAS
a = 0.0
for e in ESCENAS:
    print("%-9s declara %7.2f  render %7.2f  %+.0f ms"
          % (e["id"], e["ini"], a, (a - e["ini"]) * 1000))
    a += max(2, round((e["fin"] - e["ini"]) * 25)) / 25
```

Si la última línea pasa de ±40 ms, el episodio ya tiene un fotograma de desfase entre la
imagen y la voz, y hay que arreglar el redondeo antes de montar tramos encima.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Redondear la duración de cada escena por separado | Paseo aleatorio: 100 ms de media a los doce minutos |
| Suponer que `concat -c copy` deriva | Se recodifica «por seguridad» y se pagan horas para nada |
| Buscar la deriva mirando la duración total | 14 ms al final esconden 190 ms en el minuto nueve |
| Buscarla en el auditor | Mide la tabla, no el fichero: ahí la escena dura lo que declara |
| Dar por bueno «no se ve el salto» | No hay salto; hay desfase progresivo, que es otra cosa |
| Mezclar escenas con fps o `time_base` distintos | Entonces sí: el pegado deja de ser exacto (`98`) |
| Corregir el desfase moviendo la voz | Se arregla el final y se rompe el principio |

## Relacionado

`240` la tabla de eventos · `241` resolución de anclas · `238` render por lotes y
reanudar · `237` el intermedio no tiene que ser bonito · `232` presupuesto de render ·
`98` episodios largos · `142` la medida que miente · `150` catálogo del fallo silencioso
