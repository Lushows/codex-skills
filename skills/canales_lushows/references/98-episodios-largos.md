# 98 · Episodios largos

**Qué resuelve:** doce minutos no se producen como un piloto de ochenta segundos. Se
producen **por tramos de un minuto**, y cada tramo se cierra del todo antes de escribir
el siguiente. Es la única forma de que un episodio largo no se convierta en un
proyecto interminable con dos minutos buenos y diez de relleno.

---

## La regla del tramo cerrado

Un tramo está **cerrado** cuando pasa las cinco casillas:

```
[ ] texto      escrito, leído en voz alta y cronometrado (§ 95)
[ ] voz        grabada en UNA pasada y aprobada a oído
[ ] tiempos    alineación palabra→segundo hecha sobre esa voz
[ ] visual     tabla de eventos completa, auditada (§ 17) y renderizada
[ ] visto bueno  visto entero, con la grilla de fotogramas revisada
```

**No se escribe el tramo N+1 con el tramo N a medias.** Si se cambia el texto del
minuto 3 cuando el 4 ya está montado, se rehacen los tiempos y el guion visual de los
dos. El coste de reordenar crece con cada tramo abierto.

## El mapa del episodio

Antes del primer tramo se escribe el mapa completo: **una línea por minuto**. El mapa
se aprueba antes de escribir prosa; es lo que se discute y lo que se corrige barato.

```
MIN  TRAMO            HECHO NUCLEAR         BUCLE                    CIFRA   FONDO
01   gancho+promesa   ...                   abre: ¿cómo lo movía?    ancla?  A
02   origen           ...                   —                        —       A
03   origen 2         ...                   abre: el socio           —       B
04   la máquina       ...                   —                        sí      B
...
12   remate           ...                   cierra todos             final   F
```

Columnas obligatorias: **hecho, bucle, cifra y fondo**. El fondo se planifica en el
mapa (§ `50`, `58`) porque la coherencia de color se decide a nivel de episodio, no de
tramo: si cada minuto elige su paleta por separado, los doce no parecen el mismo vídeo.

## Anatomía de un tramo de un minuto

| Segundos | Función |
|---|---|
| 0-5 | **Enganche del tramo**: recoge la promesa con la que cerró el anterior |
| 5-45 | **Cuerpo**: un solo hecho nuclear desarrollado, con su material visual |
| 45-55 | **Punto alto**: la cifra, el documento o el giro del tramo |
| 55-60 | **Micro-promesa**: la frase que obliga a seguir al minuto siguiente |

Un tramo = **un hecho nuclear**. Si al escribirlo aparecen dos, son dos tramos y el
mapa se actualiza. Dos hechos en sesenta segundos no se entienden ninguno.

## Continuidad entre tramos

Lo que hay que vigilar cuando el episodio se produce a trozos:

| Eje | Qué se comprueba |
|---|---|
| **Nivel de voz** | Mismo LUFS integrado en todos los tramos. Se mide, no se estima |
| **Timbre y ritmo** | Misma voz, mismos ajustes, misma pronunciación de nombres |
| **Room tone** | La capa de sala cruza los cortes: nunca se apaga entre tramos |
| **Paleta** | Recorrido de color planificado en el mapa, no elegido por tramo |
| **Densidad** | Cada tramo dentro del objetivo de su tipo de bloque (§ `18`) |
| **Repetición** | El mismo movimiento, transición o plantilla no se repite entre tramos vecinos |
| **Datos ya dichos** | Una cifra se explica una vez; después se referencia |

## El montaje por tramos

- Cada tramo se renderiza a su propio `_mudo.mp4` y su propio audio, con nomenclatura
  `t01`, `t02`… Nunca se sobrescribe un tramo aprobado.
- La unión se hace al final, con las **mismas** características de vídeo y audio en
  todos los tramos (resolución, fps, frecuencia de muestreo y canales). Un tramo con
  parámetros distintos rompe la concatenación o mete un salto.
- La **mezcla final se hace sobre el episodio entero**, no tramo a tramo: la
  normalización de loudness y el colchón necesitan la pieza completa.
- Verificación final sobre el archivo unido: saltos de LUFS, picos, grilla de
  fotogramas y peso de cada render (SKILL.md, § verificación).

## Ritmo de trabajo realista

| Fase | Qué produce |
|---|---|
| Investigación y mapa | El mapa de 12 líneas y las fuentes descargadas |
| Tramos 1-2 | Los que más se rehacen: fijan tono, voz y paleta |
| Tramos 3-10 | Ritmo de crucero; el trabajo se vuelve mecánico |
| Tramos 11-12 | El remate: se escribe con el episodio ya visto entero |
| Cierre | Unión, mezcla, verificación, título, miniatura y descripción (§ `99`) |

**El remate se escribe al final, no en el mapa.** Cuando los once minutos anteriores
existen ya se sabe cuál es la frase que cierra; escrita de antemano, casi siempre sobra.

## Cuándo un tramo se corta entero

Al revisar el episodio unido hay tramos que estorban. Señales: no abre ni cierra ningún
bucle, no aporta hecho nuevo, o repite algo ya explicado. **Un episodio de 10 minutos
sólidos rinde más que uno de 12 con dos de relleno**: la retención media es lo que
decide el alcance del siguiente vídeo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Escribir los doce minutos de una vez y luego producirlos | El minuto 9 obliga a reescribir el 4 y se rehace todo |
| Grabar la voz del episodio entero antes de tener el visual del tramo 1 | Un cambio de texto invalida toda la locución |
| Elegir la paleta tramo a tramo | Doce minutos que no parecen del mismo vídeo |
| Tramos con parámetros de render distintos | La unión falla o mete un salto visible |
| Normalizar el audio tramo a tramo | Escalones de volumen audibles en cada frontera |
| Dos hechos nucleares en un tramo | No se entiende ninguno de los dos |
| Alargar para llegar a doce minutos | Cae la retención media y con ella el alcance del canal |
| Reutilizar la misma transición en tramos vecinos | El montaje se vuelve previsible |

## Relacionado

`93` estructura de episodio · `95` escribir para el oído · `17` medir el montaje ·
`58` coherencia entre fondos · `86` medir el audio · `99` título, miniatura y descripción
