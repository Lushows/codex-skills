# 288 · Cuando la voz sobra

**Qué resuelve:** los sitios donde el narrador tiene que callarse. En un canal sin cara y
sin entrevistados, la voz es la única presencia humana, y por eso hay una tentación
constante de no soltarla nunca. Pero lo que hace que una frase pese es **el hueco que
tiene delante**, y ese hueco la puntuación no lo puede comprar.

> Ojo a los tres silencios distintos del canal, que se confunden: el silencio de **música**
> (§ `118`), el **hueco de mezcla** que deja sitio a un golpe (§ `124`) y el silencio de
> **voz**, que es este. Aquí la música puede seguir sonando: lo que se calla es el
> narrador.

---

## Lo que ya hay, y por qué no basta

Medido sobre `tiempos.json` de los dos episodios del piloto:

| Episodio | duración | silencios | callado | **hueco mayor** | mediana |
|---|---|---|---|---|---|
| `ep01-lustig` | 63,45 s | 27 | 17,80 s (**28,1%**) | **1,13 s** | 0,36 s |
| `episodio01` | 80,25 s | 31 | 20,73 s (25,8%) | 0,93 s | 0,90 s |

**Más de la cuarta parte del minuto ya es silencio** y aun así no hay un solo hueco que
llegue a segundo y medio. Ése es el techo del motor: el punto compra 1,06 s y ningún
apilamiento de signos compra más (§ `282`). Para los silencios que de verdad cuentan
—dos, tres, cuatro segundos sobre un documento— **hay que fabricarlos**.

## Fabricar un silencio, y por qué antes de la fase 4

Se corta el audio, se inyecta silencio y se vuelve a pegar:

```bash
ffmpeg -i locucion.mp3 -filter_complex "\
[0:a]atrim=0:22.30,asetpts=PTS-STARTPTS[a];\
[0:a]atrim=22.30,asetpts=PTS-STARTPTS[b];\
anullsrc=r=44100:cl=stereo,atrim=0:2.5,asetpts=PTS-STARTPTS[s];\
[a][s][b]concat=n=3:v=0:a=1[o]" -map "[o]" -y locucion_pausa.wav
```

El corte va **dentro de una pausa que ya existe**, nunca sobre una consonante: en
`ep01-lustig` el segundo 22,30 cae en el hueco de 1,11 s que sigue a «aprendiz de
vendedor».

Comprobado después de inyectar 2,5 s y realinear con `tiempos.py`:

| Palabra | Antes | Después | Desplazamiento |
|---|---|---|---|
| `vendedor.` (anterior al corte) | 21,27 s | 21,27 s | 0,00 s |
| `Nunca` | 25,07 s | 27,57 s | **+2,50 s** |
| `consta.` | 62,98 s | 65,48 s | **+2,50 s** |

**Desviación media respecto al desplazamiento puro: 0,000 s.** El alineador ve el
silencio inyectado como un silencio más —de hecho como el más largo— y lo reparte
perfectamente. O sea: la técnica es exacta, y por eso mismo es peligrosa. **Todo lo
posterior se corre 2,5 s.** Si el silencio se inyecta después de la fase 4, las 36 anclas
del minuto se caen (§ `284`).

> **La regla:** el silencio de voz se decide en el guion, se fabrica en la fase 3 y se
> aprueba con la locución. Nunca después.

## Los seis sitios donde el narrador se calla

| Sitio | Duración | Por qué |
|---|---|---|
| **Antes del golpe del gancho** | 1,0-1,5 s | Es lo que hace que «aprendiz de vendedor» sea un golpe y no una frase más |
| **Después de una revelación** | 1,5-2,5 s | El espectador necesita tiempo para entender lo que acaba de oír |
| **Sobre un documento que se lee en pantalla** | 2-4 s | Si el texto está en pantalla, narrarlo a la vez es competir consigo mismo |
| **En la cifra que hay que dejar caer** | 1,0-2,0 s | Ciento veintiséis toneladas. Y nada más |
| **En el cambio de terreno** | 1,0-1,5 s | El paso de «lo que se cuenta» a «lo que consta» tiene que oírse |
| **El último segundo del episodio** | 1,5-3,0 s | Un episodio que termina con la voz aún hablando no termina: se corta |

Y los sitios donde **no**: en mitad de una enumeración, entre dos frases que forman una
sola idea, y en cualquier punto del primer bloque de desarrollo — ahí la densidad manda.

## El silencio de voz no es silencio de pantalla

🔴 Callarse **no** significa cortar a negro ni dejar el cuadro quieto. El canal tiene una
regla de hierro: ningún tramo sin elemento (§ `11`). Un silencio de tres segundos es el
sitio donde el montaje trabaja solo:

| Durante el silencio de voz | Qué pasa |
|---|---|
| Imagen | Sigue: el travelling sobre el documento, la casilla que se revela |
| Música | Sigue, y normalmente **sube**: es el único momento en que puede (§ `120`) |
| Efectos | Es donde caben los que en habla no cabrían: papel, máquina de escribir |
| Ducking | Se suelta: sin voz, el `sidechaincompress` deja de agachar el colchón solo |

Ese último punto es gratis y es la mitad del efecto: la mezcla se abre sola en cuanto la
voz calla, y el colchón recupera los 4-6 LU que el ducking le quitaba, sin tocar nada
(§ `85`).

## Callarse también es escribir menos

Antes de fabricar un silencio, la pregunta barata: **¿la frase hace falta?** Tres casos
en los que la voz sobra y lo que hay que hacer es borrar, no pausar:

1. **La frase que describe lo que se está viendo.** Si en pantalla hay un certificado de
   defunción con la fecha, «el certificado está fechado el once de marzo» sobra.
2. **La frase que anuncia lo que va a decir.** «Y ahora viene lo importante» no es
   narración: es relleno de podcast.
3. **La frase que repite la cifra que ya está en el rótulo.** El reparto es magnitud al
   oído, exacto al ojo (§ `283`).

A 147 ppm, cada frase de doce palabras cuesta cinco segundos de episodio. Borrar tres
frases de relleno paga un silencio de tres segundos y sobra tiempo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Esperar que la puntuación dé un silencio de 2 s | El techo del motor es 1,06 s |
| Inyectar el silencio después de la fase 4 | Todo lo posterior se corre exactamente esa cantidad; 36 anclas fuera |
| Cortar el audio fuera de una pausa existente | Se oye el corte en mitad de la palabra |
| Cortar a negro o congelar durante el silencio | Tramo sin elemento: el espectador cree que se ha colgado (§ `11`) |
| Bajar también la música en el silencio de voz | Es justo donde la música tenía su hueco |
| Silencios largos en el primer bloque de desarrollo | Se confunde con falta de material |
| Terminar el episodio con la voz todavía hablando | No termina: se corta |
| Narrar lo que ya se está leyendo en pantalla | La voz compite consigo misma y pierde |

## Relacionado

`118` cuando no debe haber música · `124` el silencio como instrumento · `282` la
puntuación como partitura · `284` una sola pasada · `16` el plano de descanso ·
`11` el hueco prohibido · `85` ducking y espacio · `120` la curva de intensidad
