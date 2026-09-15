# 345 — El color de la comida

**Qué resuelve:** cómo corregir un video de comida para que se vea apetitoso **sin que se note que lo
tocaste**. La línea entre "esa hamburguesa se ve increíble" y "esa foto está photoshopeada" es de unos
pocos números, y aquí están medidos. Es la aplicación de `60`, `250` y `254` al caso de comida y bebida,
y trae la trampa de ffmpeg que más gente quema: **`gamma` menor que 1 OSCURECE**.

---

## 1. Los colores del apetito, en números

Todo lo que sigue se midió con `signalstats` de ffmpeg sobre parches de color representativos, en YUV
de 8 bits. **Y = brillo (0–255). U = eje azul↔amarillo (128 = neutro). V = eje rojo↔verde (128 =
neutro). SAT = distancia al gris. HUE = ángulo de color en grados.**

| Objeto | Muestra | Y | U | V | SAT | HUE |
|---|---|---|---|---|---|---|
| **Espuma de cerveza** | #F5EFE0 | 221 | 121 | 132 | **8** | 119 |
| **Cerveza ámbar** | #C87A18 | 131 | 73 | 169 | 68 | 126 |
| **Piel clara** | #FFDBAC | 209 | 102 | 147 | 32 | 126 |
| **Piel media** | #C89070 | 151 | 106 | 155 | 34 | 140 |
| **Piel oscura** | #8D5524 | 99 | 98 | 156 | 41 | 133 |
| **Tomate** | #B8342A | 94 | 104 | 187 | 63 | 157 |
| **Lechuga** | #5A8A3C | 115 | 101 | 112 | 31 | 59 |
| **Neón morado** | #9B59D0 | 121 | 170 | 148 | 46 | 244 |
| **Neón magenta** | #E040FB | 130 | 186 | 185 | 81 | 225 |

De ahí salen las tres reglas del módulo:

**Regla 1 — La piel siempre tiene U por debajo de 128.** Las tres pieles: 102, 106, 98. Sin excepción,
de cualquier tono. Si en tu video la piel mide U por encima de 128, **no es piel: es una cara teñida**
(`67`, `254`, `224`).

**Regla 2 — La espuma es tu blanco de referencia.** Saturación **8**, prácticamente gris: cualquier
plano con espuma trae su propia carta de blancos incorporada (`341`).

**Regla 3 — El neón vive lejos de la comida y de la piel.** El neón morado/magenta está en HUE
**225–246**; la piel en **126–140** y la cerveza en **126**: **~90 a 120 grados de separación**. Eso es
lo que hace posible corregir la piel y la comida **sin tocar el neón**, con un selector por tono
(`253`, `348`).

---

## 2. La trampa: en ffmpeg, `gamma` menor que 1 OSCURECE

Es el error que más veces manda a alguien a rehacer una corrección: mucha gente asume la convención
contraria (la de `salida = entrada^gamma`, donde bajar el exponente aclara). El filtro `eq` de ffmpeg
hace lo opuesto. **Medición real** sobre un gris 50% (#808080), que sin filtro mide Y = 126:

```
eq=gamma=0.5   ->  Y =  62     MUCHO MAS OSCURO
eq=gamma=0.7   ->  Y =  93     mas oscuro
eq=gamma=1.0   ->  Y = 126     sin cambio
eq=gamma=1.4   ->  Y = 154     mas claro
eq=gamma=2.0   ->  Y = 179     MUCHO MAS CLARO
```

> **Memorízalo así: en ffmpeg, `gamma` se lee como un multiplicador de brillo de los medios tonos.
> Más de 1 aclara. Menos de 1 oscurece.**

Por qué importa tanto en comida: si tu plano quedó un poco oscuro y escribes `eq=gamma=0.9` creyendo
que lo aclaras, lo oscureces más, "compensas" subiendo `brightness` —que es un desplazamiento plano que
**lava los negros**— y terminas con un velo gris sobre la comida y un plano peor que el original.

```
Rangos seguros para comida:
eq=gamma=1.02 a 1.10       levantar medios tonos. Casi siempre suficiente.
eq=contrast=1.04 a 1.10    mas alla de 1.15 se tapa el detalle de la textura
eq=saturation=1.02 a 1.10  ver seccion 4: por que NO subir mas
eq=brightness              casi nunca. Prefiere gamma.
```

---

## 3. Por qué NO se calienta la imagen entera (con la prueba)

El instinto de todo el mundo es: "la comida se ve rica cuando es cálida, entonces caliento el video".
Es exactamente lo que produce el aspecto de falso. Se midieron las dos cadenas:

```
PRUEBA A (calentar todo):  colortemperature=temperature=5400:pl=1,
                           eq=contrast=1.06:saturation=1.12,
                           selectivecolor=yellows=0 0 0.12 0:reds=0 0.06 0.06 0

PRUEBA B (selectiva):      eq=contrast=1.06:saturation=1.04,
                           selectivecolor=yellows=0 0 0.14 0:reds=0 0.05 0.05 0
```

| Objeto | SAT original | SAT con A | SAT con B |
|---|---|---|---|
| Cerveza ámbar | 68 | **79** | **75** |
| Tomate | 63 | 79 | 68 |
| **Espuma** | **8** | **22** ❌ amarilla, se lee sucia | **10** ✅ sigue blanca |
| **Piel media** | **34** | **52** ❌ naranja de bronceador | **39** ✅ |
| Piel oscura | 41 | — | 46 ✅ |
| Lechuga | 31 | 40 mustia | 35 ✅ |

**Las dos cadenas dan una cerveza casi igual de rica** (79 contra 75). La diferencia está en todo lo
demás. La primera te delata; la segunda no.

> **Conclusión, y es la tesis del módulo: la comida se satura por zonas de color, no subiendo la
> temperatura de toda la imagen.**

---

## 4. Las tres barandas: cómo sabes que te pasaste

No es cuestión de gusto. Hay tres medidas que te dicen si cruzaste la línea:

```
BARANDA 1 — LO BLANCO (espuma, crema, queso blanco, servilleta, plato)
  SAT <= 12   BIEN, se lee blanco
  SAT 13-20   sospechoso, se empieza a leer amarillento
  SAT >  20   MAL, se lee sucio o viejo

BARANDA 2 — LA PIEL
  U < 128 SIEMPRE (si sube de 128, la cara esta teñida). SAT entre 25 y 45.
  SAT > 50 -> naranja de autobronceante

BARANDA 3 — LOS VERDES (lechuga, cilantro, limon, aguacate)
  V por DEBAJO de 128. Si se acerca a 128, la ensalada se ve mustia.
  Calentar la imagen entera SIEMPRE empuja los verdes hacia 128.
```

**Cómo las mides, en una línea** (`108`):
`ffmpeg -i corregido.mp4 -vf "crop=100:100:X:Y,signalstats,metadata=print" -f null -`

`crop=ancho:alto:X:Y` recorta un cuadrito. Ponlo **encima de la espuma**, luego **encima de una cara**,
luego **encima de la lechuga**. Tres mediciones, 30 segundos, y sabes si tu corrección miente.

---

## 5. Las cadenas listas para usar

**a) Comida caliente / frita / carne / hamburguesa**

```bash
ffmpeg -i entrada.mp4 -vf "eq=contrast=1.06:gamma=1.04:saturation=1.04,selectivecolor=yellows=0 0 0.14 0:reds=0 0.05 0.05 0,unsharp=5:5:0.5:5:5:0" -c:v libx264 -crf 18 -preset slow -c:a copy salida.mp4
```

`unsharp=5:5:0.5:...` es enfoque suave que resalta la costra y el crocante. Por encima de 0.8 aparecen
halos y se ve digital.

**b) Cerveza y bebidas ámbar**

```bash
ffmpeg -i entrada.mp4 -vf "eq=contrast=1.05:gamma=1.03,selectivecolor=yellows=0 0 0.16 0:reds=0 0.04 0.06 0,vibrance=intensity=0.15" -c:v libx264 -crf 18 -preset slow -c:a copy salida.mp4
```

`vibrance` sube lo poco saturado y respeta lo ya saturado — al revés de `eq=saturation`, que sube todo
por igual. Para cerveza es ideal: levanta el ámbar sin empujar la espuma. **Igual mide la espuma
después.**

**c) Verdes y frescos (ensaladas, ceviche, limonada)**

```bash
ffmpeg -i entrada.mp4 -vf "eq=contrast=1.06:gamma=1.03,selectivecolor=greens=0.10 0 0.06 0:yellows=0 0 0.08 0" -c:v libx264 -crf 18 -preset slow -c:a copy salida.mp4
```

En `selectivecolor` los cuatro números por color son **cian, magenta, amarillo, negro** (rango −1 a 1).
Cian en los verdes los hace más frescos; amarillo los pone mustios.

**d) Arreglar un plano frío / azuloso**

```bash
ffmpeg -i entrada.mp4 -vf "colortemperature=temperature=5200:pl=1" -c:a copy salida.mp4
```

Medido: `temperature=5000` sobre piel media llevó U de 106 a 101 y V de 155 a 163 → **más cálido**;
`8000` hizo lo contrario (U 114, V 149). **`pl=1` es importante**: sin él el filtro también oscurece
(Y bajó de 151 a 140); con `pl=1` el brillo se mantiene (Y 150).

---

## 6. El orden que evita rehacer el trabajo

```
1. NEUTRALIZAR. Encuentra algo que DEBE ser blanco: espuma, plato, servilleta.
   Corrige hasta que mida U y V cerca de 128. Nunca empieces "poniendo look":
   empiezas quitando el tinte de la luz del sitio.
2. EXPOSICION Y CONTRASTE. gamma 1.02-1.10, contrast 1.04-1.10.
   Revisa que no haya zonas quemadas a 255 planas.
3. COLOR SELECTIVO sobre lo que vende: yellows y reds para caliente,
   greens para fresco. NUNCA subas la temperatura global.
4. MIDE LAS TRES BARANDAS.
5. ENFOQUE al final, suave (unsharp 0.4-0.6). Nunca despues de comprimir.
6. EMPAREJA los planos entre si (62). Un reel con un color por plano se lee
   como amateur mas rapido que uno con el mismo color mediocre en todos.
```

---

## 7. Lo que el color NO arregla

- **Comida gris por luz frontal.** Ninguna corrección devuelve la textura que la luz nunca creó (`340`).
- **Piel teñida de morado por el neón.** Si U está por encima de 128, la información de piel ya no
  existe en el archivo. Se corrige **al grabar** (`224`).
- **Ruido de grabar a 240 fps de noche.** Subir saturación multiplica el ruido de color (`344`).
- **Plano quemado.** Si el brillo llegó a 255 plano, no hay dato que recuperar.

Regla honesta que ahorra horas: **si el problema está en el archivo, se vuelve a grabar; si está en la
interpretación del archivo, se corrige** (`259`, `228`).

---

## 8. Después de la corrección: la plataforma vuelve a comprimir

Instagram y TikTok recomprimen todo. La **saturación alta se degrada peor** (un rojo muy saturado se
vuelve bloques) y el **enfoque agresivo se convierte en halos**: dos motivos más para no pasarte.
**Exporta con bitrate alto** aunque te lo bajen, para darle mejor material de partida al compresor
(`93`, `92`). Y **revisa el resultado en el teléfono, no en el computador**: un plano que en el monitor
se ve elegante y oscuro, en un celular a la mitad de brillo se ve negro.

---

## Errores comunes

1. **Usar `gamma` menor que 1 creyendo que aclara.** Oscurece. Medido: 0.7 → Y de 126 a 93.
2. **Compensar con `brightness` en vez de `gamma`.** `brightness` desplaza todo y lava los negros: velo
   gris sobre la comida.
3. **Subir la temperatura de toda la imagen** para que la comida se vea rica. Delata el video: la espuma
   se vuelve amarilla (SAT de 8 a 22, medido) y la piel naranja (SAT de 34 a 52).
4. **Subir `eq=saturation` por encima de 1.10.** Todo se vuelve caricatura y la compresión de la
   plataforma lo rompe.
5. **No medir la espuma / los blancos.** Es el chivato más rápido y más barato de que te pasaste.
6. **Dejar la piel con U por encima de 128** y llamar a eso un "look". Es una cara teñida.
7. **Empezar poniendo el look antes de neutralizar.** Estás construyendo sobre un tinte.
8. **Enfocar antes de corregir, o después de comprimir.** El enfoque va al final de la cadena de color
   y antes de exportar.
9. **`unsharp` por encima de 0.8.** Halos visibles alrededor de cada borde.
10. **Usar `colortemperature` sin `pl=1`.** También te oscurece la imagen (Y de 151 a 140, medido).
11. **Corregir cada plano por separado sin emparejarlos** (`62`), o **aplicar una LUT genérica de
    "food"** descargada: están hechas para otro material y mueven la piel y los blancos justo donde no
    debe.
12. **Revisar el resultado solo en el computador.** Se publica para celulares.
13. **Intentar salvar en color un plano grabado con luz frontal.** No se puede: se vuelve a grabar.

---

## Checklist

- [ ] Se **neutralizó primero** usando un objeto que debe ser blanco (espuma, plato, servilleta).
- [ ] Se usó `gamma` **mayor que 1** para aclarar (1.02–1.10), no menor.
- [ ] `contrast` está entre **1.04 y 1.10**.
- [ ] La saturación se subió **por zonas** (`selectivecolor` / `vibrance`), no global.
- [ ] **No se subió la temperatura de toda la imagen.**
- [ ] **Baranda 1 medida:** espuma / blancos con SAT ≤ 12.
- [ ] **Baranda 2 medida:** piel con U < 128 y SAT entre 25 y 45.
- [ ] **Baranda 3 medida:** verdes con V < 128.
- [ ] Si se usó `colortemperature`, lleva **`pl=1`**.
- [ ] `unsharp` con cantidad **≤ 0.6** y aplicado **al final**, antes de exportar.
- [ ] No hay zonas **quemadas a 255** en la comida.
- [ ] Todos los planos del reel están **emparejados entre sí** (`62`).
- [ ] Se exportó con **bitrate alto** sabiendo que la plataforma recomprime.
- [ ] Se revisó el resultado **en un celular**, no solo en el computador.
- [ ] Se aceptó que lo que está mal grabado (luz frontal, piel teñida, plano quemado) **se vuelve a
      grabar**, no se corrige.
