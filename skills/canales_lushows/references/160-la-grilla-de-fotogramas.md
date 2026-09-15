# 160 · La grilla de fotogramas

**Qué resuelve:** ver un minuto entero de golpe. Es la única herramienta que enseña el
episodio **como lo ve el espectador** y no como lo describe la tabla de eventos. Tres
gráficos ilegibles y un recorte lavado pasaron las once medidas del auditor y sólo
aparecieron aquí.

---

## El comando

```bash
ffmpeg -y -v error -i salida/ep01-lustig-min1.mp4 \
  -vf "fps=1/2,scale=440:-1,tile=6x6" -frames:v 1 salida/_grid.png
```

Tres filtros y cada uno decide una cosa:

| Filtro | Qué hace | Cómo se elige |
|---|---|---|
| `fps=1/N` | un fotograma cada **N** segundos | N tal que `duración/N ≤ filas×columnas` |
| `scale=440:-1` | ancho de cada casilla; `-1` conserva la proporción | 440 px → casilla 440×248 |
| `tile=CxF` | rejilla de C columnas por F filas | 6×6 = 36 casillas |

**Medido en la máquina real** (i7 de 2009, vídeo de 63,45 s y 55,7 MB):
la grilla de 6×6 tarda **21,6 s** y pesa 4,3 MB a 2640×1488. Es el precio de una
revisión completa; un render del mismo minuto cuesta 6-10 minutos.

## Cada cuánto muestrear

`fps=1/N` es un compromiso: con N grande se pierden planos enteros, con N pequeño la
casilla queda tan chica que no se lee nada.

| Duración | N | Rejilla | Casillas | Cubre hasta | Qué se ve |
|---|---|---|---|---|---|
| 0-45 s | 1,5 | 6×5 | 30 | 45 s | se leen los rótulos |
| 45-70 s | **2** | **6×6** | 36 | 72 s | **el ajuste por defecto** |
| 70-145 s | 3 | 7×7 | 49 | 147 s | ya no se leen cifras pequeñas |
| 145-360 s | 5 | 9×8 | 72 | 360 s | sólo exposición y color |
| más de 6 min | — | una grilla **por bloque**, no una del episodio | | | |

⚠️ **Si el episodio dura más de lo que cabe, ffmpeg no avisa:** `tile` emite el mosaico
en cuanto junta las casillas que le pidieron y `-frames:v 1` se queda con el primero.
**Comprobado:** `episodio01.mp4` dura 80,28 s; con `fps=1/2,tile=6x6` la grilla sale con
**las 36 casillas llenas** —ni una vacía, ni un aviso— y los **últimos 8 segundos no
aparecen en ninguna**. No hay pista visual: la grilla parece completa. Comprobar siempre
`duración/N ≤ casillas`.

⚠️ **N no debe ser múltiplo de la duración media de plano** (1,6-2,4 s, módulo `13`).
Con N = 2 y planos de 2 s se cae siempre en la misma fase y hay elementos que no salen
en ninguna casilla. Por eso 1,5 y 3 son mejores muestreadores que 2 cuando hay dudas.

## Qué se caza aquí y en ningún otro sitio

Las métricas de `17` miden **presencia y superficie**: cuentan lo que la tabla declara.
La grilla mide **lo que llegó al fotograma**.

| Defecto | Por qué ninguna métrica lo ve |
|---|---|
| **Rótulo ilegible** | La tabla sabe el `w` del PNG, no el tamaño de la letra en pantalla (`164`) |
| **Recorte lavado** | Está presente, ocupa su superficie y suma cobertura; simplemente no se distingue del fondo (`163`) |
| **Episodio entero marrón** | Cada plano por separado está bien expuesto. El defecto es la **secuencia** |
| **La misma imagen dos veces en 8 s** | El antirrepetición cuenta gestos, no parecidos: dos fotos distintas del mismo barco son dos recursos |
| **Imagen que no corresponde a la voz** | Es un error factual. Ninguna medida puede tenerlo |
| **Bloque blanco de Chrome** | El PNG pesa sus 10 MB y pasa la comprobación de peso (`151`) |
| **Elemento enterrado bajo otro** | Se mide por rectángulos, pero una rotación o un `deriva` lo mueven |

**Caso real.** El episodio 01 salió del auditor con *APTO PARA RENDER*: cero huecos,
simultaneidad 2,04, 47,9 eventos/min. En la grilla se veían **tres gráficos con los
rótulos convertidos en una mancha gris** y un retrato que parecía una marca de agua
sobre el fondo. Ninguno de los dos defectos tiene una fila en la tabla de eventos.
De ahí salieron los módulos `163` y `164`.

## Cómo se mira

1. **Sin ampliar, de un vistazo.** Lo primero es el color: ¿hay blancos vivos y un punto
   de color en cada fila, o el episodio entero es marrón? Ese juicio se pierde al
   ampliar casilla a casilla.
2. **Recorrer por columnas**, no por filas: las casillas contiguas verticalmente están
   separadas por `N × columnas` segundos, así que revelan si el episodio vuelve al mismo
   sitio cada 12 s.
3. **Ampliar sólo lo sospechoso.** Para una casilla concreta se extrae el fotograma
   completo, que es donde se lee de verdad:
   ```bash
   ffmpeg -y -v error -ss 35.2 -i salida/ep01-lustig-min1.mp4 -frames:v 1 salida/_t35.2.png
   ```
4. **Guardar la grilla con versión.** En `piloto/episodio01/salida/` conviven
   `_grid.png`, `_grid_nuevo.png` y `_grid_v3` a `_grid_v9`: **nueve grillas para un
   episodio de 80 s**. Comparar la v6 con la v7 es lo que demuestra que el arreglo
   arregló algo (`168`).

## Variantes útiles

```bash
# grilla de UN bloque: -ss antes de -i es busqueda rapida, -t limita
ffmpeg -y -v error -ss 34.41 -t 15.88 -i salida/ep01-lustig-min1.mp4 \
  -vf "fps=1/0.6,scale=520:-1,tile=5x5" -frames:v 1 salida/_grid_torre.png

# grilla DENSA de un plano sospechoso: un fotograma cada 4 (0,16 s a 25 fps)
ffmpeg -y -v error -ss 35.0 -t 4 -i salida/ep01-lustig-min1.mp4 \
  -vf "select='not(mod(n,4))',scale=480:-1,tile=5x5" -vsync 0 -frames:v 1 _paso.png

# con el segundo escrito en cada casilla: para poder citar el defecto en el informe
ffmpeg -y -v error -i salida/ep01-lustig-min1.mp4 -vf \
 "fps=1/2,drawtext=text='%{pts\:hms}':x=8:y=8:fontsize=34:fontcolor=yellow:box=1:boxcolor=black@0.6,scale=440:-1,tile=6x6" \
  -frames:v 1 salida/_grid_t.png
```

⚠️ En `drawtext` los `:` son separadores del filtro: hay que escaparlos (`pts\:hms`).
Es el mismo error que dejó un rótulo `20:52` rompiendo la cadena entera.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Grilla que no cubre el episodio entero | Se revisa el primer minuto creyendo que se revisó todo |
| Casilla por debajo de 380 px de ancho | No se puede juzgar legibilidad; hace falta `164` igualmente |
| Mirar la grilla sobre fondo negro del visor | Los halos de los recortes se disimulan (`161`) |
| Sobrescribir siempre `_grid.png` | Se pierde la prueba de que el arreglo cambió algo |
| Sacar la grilla del `_mudo.mp4` | Falta la mezcla; sirve para imagen, no para juzgar el episodio |
| Dar por bueno un plano porque en la casilla "se ve bien" | 440 px perdonan; el espectador lo ve a 1920 |

## Relacionado

`161` auditar sobre gris · `163` contraste elemento-fondo · `164` legibilidad por
altura · `165` la prueba del mudo · `166` la prueba del pulgar · `17` medir el montaje
