# 259 — Cuando el color no arregla

Este es el módulo honesto del bloque. Los ocho anteriores te enseñaron a arreglar cosas. Este te
enseña a **reconocer lo que no tiene arreglo**, decirlo a tiempo y no quemar seis horas persiguiendo
un imposible.

La regla de fondo:

> **El color redistribuye información. No la inventa.**
> Si el dato no está en el archivo, ningún filtro lo va a traer.

Y el corolario profesional, que es lo que separa a alguien que cobra por esto de alguien que no:

> **Decir "esto no se arregla, hay que volver a grabar" el primer día es servicio.
> Decirlo el quinto día es una factura que nadie quiere pagar.**

---

## 1. La pregunta única: ¿hay dato o no hay dato?

Todo se reduce a eso. Y se responde midiendo, no mirando.

### Prueba 1 — ¿Está quemado?

```bash
ffmpeg -y -v error -i clip.mp4 -vf "signalstats=stat=brng,metadata=print:file=diag.txt" -frames:v 1 -f null -
grep -E "YMIN=|YMAX=|YHIGH=|BRNG=" diag.txt | head -4
```

| Lo que ves | Diagnóstico |
|---|---|
| `YMAX=255` **y** `YHIGH` cerca de 255 | zona grande quemada. **Sin dato.** |
| `YMAX=255` con `YHIGH` en 200 | solo unos reflejos en el tope. Normal y sano |
| `YMIN=0` **y** `YLOW=0` | negros aplastados. **Sin dato** en las sombras |
| `BRNG` alto (> 0,10) | mucho píxel fuera del rango legal |

Números reales medidos, para calibrar la escala: un clip sano da `BRNG = 0,025`. El mismo clip
aplastado a la fuerza da `BRNG = 0,397`. O sea: **el 40 % de los píxeles fuera del rango legal**. Eso
ya no es un problema de grado, es un archivo roto.

### Prueba 2 — ¿Cuánto ruido hay, y qué pasa si levanto?

`TOUT` mide valores atípicos en el tiempo, que en la práctica es **ruido**.

```bash
ffmpeg -y -v error -i clip.mp4 -vf "signalstats=stat=tout,metadata=print:file=n.txt" -frames:v 1 -f null -
grep TOUT n.txt | head -1
```

| `TOUT` | Lectura |
|---|---|
| < 0,0002 | limpio |
| 0,0005 – 0,0015 | ruido visible en sombras |
| > 0,002 | ruidoso; levantar sombras va a doler |

Y aquí está la medición que decide muchas discusiones. Mismo clip, antes y después de levantar las
sombras con `eq=gamma=2.2`:

```
antes de levantar:   TOUT = 0,00126
después de levantar: TOUT = 0,00215     (+70 % de ruido)
```

**Levantar sombras multiplica el ruido**, medido. No es una opinión de "puristas": es lo que pasa
cuando amplificas una señal que casi no tenía señal. Cuando alguien dice "súbelo en post", esto es lo
que está pidiendo sin saberlo.

### Prueba 3 — ¿Está enfocado?

El enfoque no se recupera. Punto. Pero conviene demostrarlo en vez de discutirlo:

```bash
# saca el mismo instante de dos tomas y compáralas al 200%
ffmpeg -y -ss 5 -i toma_a.mp4 -vf "crop=400:400:760:340,scale=800:800:flags=neighbor" -frames:v 1 foco_a.png
ffmpeg -y -ss 5 -i toma_b.mp4 -vf "crop=400:400:760:340,scale=800:800:flags=neighbor" -frames:v 1 foco_b.png
```

`unsharp` no devuelve el foco: **aumenta el contraste de los bordes que quedaron**. En material
desenfocado lo único que hace es engordar el ruido y crear halos.

---

## 2. La tabla honesta: qué sí y qué no

| Problema | ¿Se arregla? | Con qué / por qué no |
|---|---|---|
| Tinte de color (todo verde, todo azul) | ✅ **sí, completamente** | `colorbalance`, `gamma_r/b` (`255`) |
| Subexposición leve (1 paso) | ✅ sí | `eq=gamma` — sube algo de ruido, aceptable |
| Sobreexposición leve, sin recorte | ✅ sí | `curves` con hombro |
| Planos disparejos entre sí | ✅ sí, es el oficio | `62`, `255` |
| Piel con dominante | ✅ sí | secundarias (`253`, `254`) |
| Saturación excesiva | ✅ sí | `eq=saturation` |
| Bandeado leve | 🟡 se disimula | `deband` + grano (`251`) |
| Subexposición fuerte (3+ pasos) | 🟡 a medias | sale ruido y color sucio antes que detalle |
| Ruido | 🟡 a medias | `nlmeans`/`hqdn3d` limpian pero **plastifican** |
| Nitidez de fábrica del celular | 🟡 se disimula | no se puede des-afilar |
| **Altas luces quemadas** | ❌ **no** | los tres canales en el máximo: no hay información |
| **Negros aplastados** | ❌ **no** | todo el detalle quedó en el mismo valor |
| **Fuera de foco** | ❌ no | `unsharp` solo engorda los bordes que ya hay |
| **Movido / trepidado fuerte** | ❌ no | `vidstab` ayuda con el temblor, no con el barrido |
| **Dos fuentes de luz de color distinto en la misma cara** | ❌ casi nunca | una mitad cálida y otra fría no se separa por color |
| **Piel del mismo matiz que la luz dominante** | ❌ no | sin separación de matiz no hay secundaria posible |
| **Material de IA temporalmente inestable** | ❌ no | la textura muta; no es un problema de color |
| **Fondo feo, mal encuadre, mala actuación** | ❌ no | eso no es color, es rodaje |

Sobre el penúltimo caso "imposible": en el caso del bar hubo **suerte medible**. La piel vive en HUE
133–140 y el neón morado en HUE 225–246 (`254`). Noventa grados de separación es lo que permitió que
`selectivecolor` arreglara la cara sin tocar el neón. Si el bar hubiera tenido luz naranja de sodio
—HUE ~40–60, pegado a la piel— **no habría habido nada que hacer**, y la respuesta correcta habría
sido cambiar la luz o cambiar el plano.

> **La viabilidad de una secundaria se puede calcular antes de intentarla: mide el HUE de lo que
> quieres corregir y el HUE de lo que quieres proteger. Si están a menos de ~25 grados, no hay
> secundaria que los separe.**

---

## 3. Los tres autoengaños del que empieza

**"Lo subo en post."**
Ya viste la medición: +70 % de ruido al levantar. Y si venía de un celular a 8 bits, además aparece
bandeado. Lo que se grabó oscuro se ve oscuro y ruidoso, no bien expuesto.

**"Lo bajo en post."**
Peor todavía. Una zona quemada tiene los tres canales en el máximo: **no hay matiz que recuperar**. Al
bajarla no aparece la ventana ni la nube: aparece un gris plano. Y si la cara está quemada, al
bajarla queda gris cadáver.

**"Le meto una LUT y ya."**
Una LUT es una función. La misma función sobre entradas distintas da salidas distintas. En material
disparejo (dispersión de luma de 34 puntos, como el caso del bar) la LUT **mantiene o aumenta** la
disparidad (`256`).

---

## 4. Qué hacer con lo que no tiene arreglo

No siempre "volver a grabar" es la respuesta. Hay una escalera, de más barata a más cara:

**1. Acortar el plano.** El más subvalorado. Un plano con problema que dura 10 cuadros no se juzga; el
mismo de 3 segundos es lo primero que el cliente señala. **El corte arregla lo que el color no puede.**

**2. Cambiar el encuadre.** Si la ventana quemada está en la esquina, recórtala:

```bash
ffmpeg -i clip.mp4 -vf "crop=iw*0.78:ih*0.78:iw*0.14:0,scale=1080:1920,format=yuv420p" \
  -c:v libx264 -crf 16 -c:a copy recortado.mp4
```

Pierdes resolución, pero si vas de 4K a 1080 vertical te sobra.

**3. Taparlo con otra cosa.** Un rótulo, un gráfico, un plano de apoyo encima (`80`, `200`).

**4. Convertirlo en decisión.** Si el plano está muy contrastado y no hay detalle, llévalo al extremo:
alto contraste declarado, o blanco y negro. Un problema asumido a propósito se lee como estilo; un
problema a medio arreglar se lee como error.

```bash
ffmpeg -i imposible.mp4 -vf "hue=s=0,curves=all='0/0 0.35/0.22 0.7/0.85 1/1',noise=c0s=8:allf=t" \
  -c:v libx264 -crf 16 -c:a copy decision.mp4
```

**5. Sacarlo del corte.** Ocho planos buenos ganan a doce con dos malos. Siempre.

**6. Volver a grabar.** Cuando el plano es imprescindible (el producto, la cara del dueño, la toma que
sostiene el mensaje) y no hay sustituto.

---

## 5. Cómo se dice, sin quedar mal

La conversación importa tanto como el diagnóstico. Lo que funciona:

1. **Muestra la evidencia, no la opinión.** Un PNG con la zona quemada al 200 % y el número de
   `BRNG`. "Aquí el 40 % de los píxeles está fuera de rango" pesa distinto a "quedó feo".
2. **Di qué SÍ se puede.** "El tinte lo arreglo completo, la piel también. Lo que no vuelve es la
   ventana quemada del segundo 12."
3. **Ofrece las alternativas en escalera**, con su costo: acortar (gratis), recortar (gratis),
   tapar (30 min), volver a grabar (media jornada).
4. **Deja que decida el cliente.** Es su plata y su plano.
5. **Ponlo por escrito.** Una línea en el correo evita la discusión de dentro de dos semanas.

Lo que NO funciona: entregar el plano "lo mejor que se pudo" sin avisar. El cliente lo va a notar,
solo que en la reunión de aprobación y delante de más gente.

---

## 6. Lo que hay que pedir en rodaje para no volver aquí

Este módulo existe porque alguien no hizo estas seis cosas. En orden de cuánto dolor evitan:

| Pedido | Evita |
|---|---|
| **Bloquear el balance de blancos** (no automático) | la deriva de color dentro del clip (`258`) |
| **No quemar las altas**: mejor un pelo subexpuesto | lo irrecuperable |
| **Exponer para la cara**, no para el fondo | el sujeto oscuro con la pared perfecta |
| **Grabar 3–5 s de una hoja blanca** en cada montaje de luz | te da la referencia de neutro gratis |
| **Una sola temperatura de luz por escena** | la cara mitad cálida mitad fría |
| **Grabar un plano de referencia** (mismo encuadre, sin nadie) | material para tapar y para medir |

Y el que resume todo: **si en el monitor ya se ve mal, en post se va a ver mal.** El color es la
etapa que pule, no la que rescata.

---

## 7. El cálculo que casi nadie hace

Antes de meterle tres horas a un plano imposible, haz la cuenta:

```
Costo de rescatar      = horas × tu tarifa + el riesgo de que igual quede regular
Costo de volver a grabar = traslado + tiempo de rodaje + coordinación
Costo de sacarlo       = cero, si el video funciona sin él
```

En un video social de 60 segundos, un plano suele valer 4 segundos de pantalla. **Tres horas de
rescate por 4 segundos casi nunca sale a cuenta**, y el resultado sigue siendo el plano más feo del
video.

La pregunta honesta: *si le quito este plano, ¿el video sigue contando lo mismo?* Si la respuesta es
sí, ya tienes la decisión y te ahorraste la tarde.

---

## 8. Lo que este bloque sí puede prometer

Para cerrar sin dejar mal sabor: con material grabado decentemente, el color **sí** hace una
diferencia enorme y medible. En el caso del bar, sin volver a grabar nada:

| Métrica | Mejora medida |
|---|---|
| Dispersión de saturación (SAT de 13 a 57) | **−43 %** |
| Magenta (distancia de U y V al neutro) | **−40 %** |
| Dispersión de luminancia (Y de 70 a 104) | **−55 %** |
| Piel morada | resuelta con `selectivecolor` en `reds` y `magentas` |

Eso es un video que pasó de "se nota que son tomas de días distintos" a "es una sola pieza". Ninguna
de esas mejoras inventó información: todas **redistribuyeron** la que había.

Esa es exactamente la frontera de este oficio, y saber dónde está es lo que te hace confiable.

---

## Errores comunes

- **Prometer que se arregla antes de medir.** Cinco minutos de `signalstats` te dicen si es posible.
- **Intentar recuperar altas quemadas.** Los tres canales están en el máximo: no hay matiz.
- **Levantar sombras muy oscuras sin avisar del ruido.** Medido: +70 % de `TOUT` al levantar.
- **Usar `unsharp` para arreglar foco.** Engorda el ruido y crea halos; el foco no vuelve.
- **Intentar una secundaria entre dos colores separados por menos de 25 grados de HUE.** No hay nada
  que separar.
- **Meterle una LUT a material disparejo esperando que empareje.** Estiliza, no empareja.
- **Limpiar ruido a fondo con `nlmeans` y entregar caras de plástico.** Peor que el ruido.
- **Insistir tres horas en un plano de 4 segundos.**
- **No mostrar la evidencia al cliente.** Un número y una captura valen más que "no se pudo".
- **Entregar sin avisar del plano problemático.** Se descubre en la reunión, con público.
- **Culpar al material y no dejar por escrito qué pedir la próxima vez.** El mismo problema vuelve el
  mes entrante.

---

## Checklist

- [ ] Antes de prometer nada, corrí `signalstats` con `brng` y `tout` sobre los planos dudosos.
- [ ] Revisé `YMAX`/`YHIGH` (quemado) y `YMIN`/`YLOW` (aplastado) en los planos críticos.
- [ ] Si hay que levantar sombras, medí `TOUT` antes y después y sé cuánto ruido voy a sumar.
- [ ] Si planeo una secundaria, medí el HUE de lo que corrijo y de lo que protejo, y están a más de
      25 grados.
- [ ] Separé la lista en tres: **se arregla · se disimula · no tiene arreglo**.
- [ ] Para lo que no tiene arreglo, recorrí la escalera: acortar → recortar → tapar → asumir como
      estilo → sacar → volver a grabar.
- [ ] Hice el cálculo de horas de rescate contra segundos de pantalla.
- [ ] Le mostré al cliente la evidencia (captura + número), no una opinión.
- [ ] Ofrecí alternativas con su costo y dejé que decidiera.
- [ ] Lo dejé por escrito.
- [ ] Anoté qué pedir en el próximo rodaje para que esto no se repita.
- [ ] Medí y reporté lo que el color **sí** logró, en números.
