# 38 — Adaptar un video a varios formatos sin rehacerlo


> ⚠️ **Las cifras de zona segura de este módulo no son la referencia.**
> El dueño es `45-zona-segura-por-plataforma`, que además distingue el recorte
> geométrico (se calcula) de la interfaz de la app (se mide, y caduca). Antes de
> montar con un número de aquí, mídelo con `418-medir-la-zona-segura-de-verdad`.
> Adaptar no es recortar al final. Es **decidir al principio** dónde va lo importante, para que después
> el recorte sea mecánico. Un video pensado en un solo formato se rehace entero; uno pensado bien se
> reexporta en tres minutos.

---

## La idea que resuelve el problema: el cuadrado sagrado

Trabaja el máster en **9:16 (1080 × 1920)** y protege el **cuadrado central de 1080 × 1080**.

```
        1080 px
   ┌───────────────┐  0
   │   sacrificable│
   │               │  420
   ├───────────────┤ ────────────
   │               │
   │   CUADRADO    │   1080 × 1080
   │   SAGRADO     │   aquí va TODO
   │               │   lo que no se
   │               │   puede perder
   ├───────────────┤ ────────────
   │               │  1500
   │   sacrificable│
   └───────────────┘  1920
```

**Regla:** cara, producto, texto y acción **siempre dentro del cuadrado sagrado**. Lo de arriba y lo de
abajo es ambiente, y ambiente es lo que se puede botar.

Con eso, **1:1 y 4:5 salen por recorte automático y no hay que revisar nada**. El único formato que
sigue exigiendo trabajo es 16:9, y más abajo está por qué.

---

## Los recortes, con los números exactos

Máster: **1080 × 1920**.

| Destino | Resolución | Recorte desde el máster | ffmpeg |
|---|---|---|---|
| **9:16** vertical completo | 1080 × 1920 | ninguno | — |
| **4:5** feed de Instagram | 1080 × 1350 | quita 285 px arriba y 285 abajo | `crop=1080:1350:0:285` |
| **1:1** cuadrado | 1080 × 1080 | quita 420 px arriba y 420 abajo | `crop=1080:1080:0:420` |
| **16:9** horizontal | 1920 × 1080 | **no sale por recorte** | ver abajo |

```bash
# 9:16 → 4:5
ffmpeg -i master_916.mp4 -vf "crop=1080:1350:0:285" -c:a copy salida_45.mp4

# 9:16 → 1:1
ffmpeg -i master_916.mp4 -vf "crop=1080:1080:0:420" -c:a copy salida_11.mp4
```

> Instagram **recorta los Reels a 4:5 en el feed**. Es decir: aunque subas 9:16, mucha gente lo va a ver
> en 4:5 sin que tú lo decidas. Por eso 4:5 no es un formato opcional: **es cómo se ve tu 9:16 la mitad
> del tiempo**. Revísalo siempre.

---

## El problema real: 16:9

Recortar 9:16 a 16:9 conserva el ancho pero **bota el 68% de la altura**: de 1920 px te quedas con 608.
Casi siempre eso decapita a la persona o deja el producto fuera.

Tres salidas, de mejor a peor:

### A. Reencuadrar plano por plano (lo correcto si el video importa)
Si el bruto se grabó en resolución alta (4K), tienes píxeles de sobra para reencuadrar cada plano sin
perder calidad. Es trabajo, pero es la única versión que se ve pensada. Ver `22-punch-in-y-reencuadre.md`.

### B. Fondo desenfocado (aceptable, honesto)
Pones el vertical centrado sobre una versión ampliada y borrosa de sí mismo.

```bash
ffmpeg -i master_916.mp4 -filter_complex \
"[0:v]scale=1920:-2,boxblur=40:5,crop=1920:1080[bg];\
 [0:v]scale=-2:1080[fg];\
 [bg][fg]overlay=(W-w)/2:0" -c:a copy salida_169.mp4
```

Se ve claramente como "esto era vertical". No es elegante, pero no engaña y no rompe nada. Sirve para
YouTube y para pantallas en local.

### C. Barras negras (último recurso)
Solo cuando el destino es una pantalla que ya vas a controlar. En redes, las barras negras se leen como
descuido.

> **Lo que nunca se hace:** estirar la imagen para que llene. Deforma caras y se nota siempre.

**Si sabes de antemano que necesitas 16:9 bueno**, la decisión no es de montaje sino de rodaje: se graba
en 4K horizontal y el vertical sale por recorte, no al revés. Eso se pide en el brief
(`170-briefing-de-rodaje-desde-la-edicion.md`).

---

## La zona segura: dónde NO puede ir el texto

Aquí el problema no es el recorte, es que **la interfaz de cada app tapa partes del video**. Datos
verificados a agosto 2026 sobre lienzo de 1080 × 1920:

| Plataforma | Arriba | Abajo | Izquierda | Derecha |
|---|---|---|---|---|
| **Instagram Reels** | ~15% (≈288 px) | ~10% (≈192 px) | ~35 px | ~35 px |
| **TikTok** (estándar) | 108 px | 320 px | 60 px | 120 px |
| **TikTok** (recomendada) | 220 px | **420 px** | 60 px | 120 px |

### La zona segura universal (una sola, para no pensar más)

Tomando el peor caso de cada borde:

```
x:  120 → 960     (840 px de ancho útil)
y:  300 → 1490    (1190 px de alto útil)
```

**Todo el texto dentro de esa caja y no vuelves a tener un rótulo tapado por un botón.**

Fíjate que esta caja está **casi contenida en el cuadrado sagrado** (420–1500). No es casualidad: si
respetas el cuadrado sagrado para el contenido y esta caja para el texto, los tres formatos verticales
te salen bien de una sola pasada.

Detalle por plataforma: `45-zona-segura-por-plataforma.md`.

---

## Qué se pierde en cada formato (la tabla honesta)

| Formato | Qué gana | Qué pierde | Cuándo usarlo |
|---|---|---|---|
| **9:16** | Pantalla completa, máxima inmersión, es el nativo de todo | Nada de contexto lateral: no cabe una mesa, un local, dos personas | Reels, TikTok, Shorts, Stories, anuncios |
| **4:5** | Ocupa mucho en el feed sin ser vertical total; sobrevive al recorte de IG | Pierde el aire de arriba y abajo; los rótulos altos se salen | Feed de Instagram y Facebook |
| **1:1** | Se ve igual en todos lados, imposible que se recorte mal | El más aburrido: no tiene la fuerza del vertical ni el aire del horizontal | Cuando no sabes dónde va a terminar |
| **16:9** | Contexto, dos personas, el espacio, sensación de cine | La cara queda chica en un celular; en feed vertical se ve diminuto | YouTube largo, web, pantallas, presentaciones |

**Lo que se pierde siempre al adaptar, en cualquier dirección:** la **composición**. Un plano encuadrado
con intención en un formato queda descentrado en otro. Por eso el cuadrado sagrado no es una comodidad,
es una renuncia consciente: encuadras con menos gracia para poder adaptar sin dolor.

---

## Los elementos que hay que rehacer aunque el recorte funcione

Aunque la imagen quepa, estas cuatro cosas **casi siempre necesitan mano** en cada formato:

1. **El tamaño del texto.** Un rótulo de 84 px es correcto en 1080 × 1920. En 16:9 (1920 × 1080) ese
   mismo texto se ve pequeñísimo porque el ancho creció al doble. Regla: el texto se dimensiona como
   **% de la altura del cuadro**, no en píxeles fijos. Un titular ronda el **5–7% de la altura**.

2. **La posición del texto.** En vertical el texto va arriba (la interfaz tapa abajo). En horizontal va
   abajo (queda la zona de subtítulos). No es el mismo sitio y no se puede automatizar.

3. **La duración de los planos.** En 16:9 hay más información por plano, y más información necesita más
   tiempo. Un corte cada 1,6 s que funciona en vertical se siente epiléptico en horizontal. Regla
   práctica: en 16:9 alarga los planos **un 20–30%** (`20`).

4. **El gancho.** El primer segundo de un vertical y el de un horizontal no se ven igual: en horizontal
   el rostro es más pequeño y hay más entorno compitiendo. A veces toca un plano más cerrado (`30`).

---

## Flujo de trabajo recomendado

1. **Decide los formatos ANTES de montar.** Si sabes que hay 16:9, se rueda distinto.
2. **Monta el máster en 9:16**, respetando cuadrado sagrado y zona segura universal.
3. **Exporta el máster** sin texto quemado si puedes — con los subtítulos como archivo `.ass` aparte
   (`43-formato-ass-y-libass.md`). Así el texto se re-renderiza por formato en vez de recortarse.
4. **Genera 4:5 y 1:1 por recorte automático.**
5. **Revisa el 4:5** — es el que más gente va a ver y el que más rótulos pierde.
6. **Trabaja 16:9 aparte**, con reencuadre o fondo desenfocado.
7. **Verifica cada salida** (`98`): texto dentro de zona segura, nada cortado, audio íntegro.

**Nomenclatura** para no perderte (`96`):
```
costos-07_916_v3.mp4
costos-07_45_v3.mp4
costos-07_11_v3.mp4
costos-07_169_v3.mp4
```

---

## Errores comunes

1. **Recortar al final sin haber protegido el cuadrado sagrado.** Termina en caras decapitadas.
2. **Ignorar el 4:5.** Es cómo se ve tu Reel en el feed, lo hayas decidido o no.
3. **Estirar la imagen para llenar** en vez de recortar o rellenar. Deforma caras.
4. **Texto en píxeles fijos.** Se dimensiona como % de la altura, si no, el 16:9 queda ilegible.
5. **Poner el texto en el mismo sitio en vertical y en horizontal.** Arriba en vertical, abajo en
   horizontal.
6. **Mismo ritmo en 16:9 que en 9:16.** Alarga los planos 20–30% en horizontal.
7. **Texto quemado en el máster.** Si va quemado, cada formato hay que rehacerlo a mano. Deja el `.ass`
   suelto.
8. **Sacar 16:9 de un máster vertical cuando el 16:9 importaba.** Esa decisión es de rodaje, no de
   montaje.
9. **Rótulos en la franja baja** — 420 px de TikTok se comen cualquier CTA.
10. **Exportar los cuatro formatos y revisar solo el vertical.** Cada salida se verifica.
11. **Barras negras en redes.** Se leen como descuido.
12. **Nombres de archivo sin el formato.** A los tres días no sabes cuál es cuál.

---

## Checklist

- [ ] Los formatos de salida están **decididos antes de montar**
- [ ] El máster es **1080 × 1920** y todo lo esencial está en el **cuadrado sagrado** (y: 420–1500)
- [ ] Todo el texto está en la **zona segura universal** (x: 120–960 · y: 300–1490)
- [ ] Los subtítulos van como **`.ass` aparte**, no quemados en el máster
- [ ] El **4:5 está revisado a ojo**, no solo generado
- [ ] En 16:9: hay **reencuadre real** o fondo desenfocado — nunca estiramiento ni barras negras
- [ ] El texto está dimensionado como **% de la altura**, no en píxeles fijos
- [ ] En 16:9 los planos son **20–30% más largos**
- [ ] En 16:9 el texto se movió a la **parte baja**
- [ ] El gancho funciona **en cada formato**, no solo en el vertical
- [ ] Los archivos están nombrados **con el formato incluido** (`96`)
- [ ] **Cada salida** pasó la verificación de `98`, no solo el máster
