# 446 — Ruido que sobrevive a la compresión

`editpro/93` enseña a encontrar el CRF óptimo y `editpro/66` avisa de que el grano cuesta bitrate.
`editpro/428` ya demostró, con `YDIF` y cuatro etapas de entrega, que **el grano fino no llega a la
audiencia** (+20 % en el mezzanine, +0,5 % tras el reencode de red) y que **CRF 24 es el acantilado**.
Esas conclusiones están establecidas ahí; no se repiten.

Este módulo usa otro instrumento —la **varianza por píxel a lo largo del tiempo**, no la diferencia
media entre fotogramas— y con él aparece algo que la medida de cuadro entero no puede ver:
**el grano no muere igual en todas partes del cuadro. Muere primero exactamente donde hacía falta.**

---

## 1. La medida: σ temporal, no SSIM

No se puede preguntar «¿queda grano?» con una métrica de calidad; para SSIM el grano *es* el daño
(`editpro/449`). La única medida que responde es la varianza por píxel a lo largo del tiempo, sobre
material sin movimiento:

```python
import subprocess, numpy as np
def sigma_temporal(mp4, W, H, n=12):
    raw = subprocess.run(["ffmpeg","-v","error","-i",mp4,"-frames:v",str(n),
        "-pix_fmt","gray","-f","rawvideo","-"], capture_output=True).stdout
    f = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
    return f.std(axis=0).mean()
```

---

## 2. Grano sobre fondo plano: muere a CRF 24

Degradado de tinta 1920×1080, 4 s, `noise=alls=5:allf=t+u`, `preset medium`:

| CRF | bytes | σ temporal | supervive |
|---|---|---|---|
| 0 (sin pérdida) | 103 203 797 | 1,609 | 100 % (referencia) |
| 14 | 39 601 881 | 1,528 | 95 % |
| 18 | 2 577 540 | 0,586 | **36 %** |
| 21 | 237 377 | 0,072 | 4,5 % |
| 24 | 31 346 | **0,003** | **0,2 %** |
| 28 | 14 026 | 0,001 | 0,06 % |

A CRF 24 el grano no está debilitado: **está borrado**. σ 0,003 es indistinguible de un vídeo sin
grano (0,002 medido sobre el mismo fondo limpio). El derrumbe está entre 18 y 21: de 36 % a 4,5 %.

---

## 3. Sobre material detallado sobrevive… y ahí no hacía falta

El mismo grano sobre un fotograma de collage real (σ espacial 51,3 frente a 7,1 del degradado):

| CRF | σ temporal | supervive (ref = CRF 12) |
|---|---|---|
| 12 | 1,310 | 100 % |
| 18 | 0,760 | 58 % |
| 21 | 0,408 | 31 % |
| 24 | 0,218 | **17 %** |

`editpro/428` mide lo mismo con `YDIF` sobre el cuadro entero y da, para `alls=12`, un 8 % de
supervivencia a CRF 24 — un número **de cuadro**, que cae entre estos dos. Pon las dos tablas una al
lado de la otra y sale el hecho que cualquier promedio de cuadro esconde:

> **A CRF 24 el grano conserva el 17 % sobre el collage y el 0,2 % sobre el degradado.**
> El codificador lo mantiene donde ya hay detalle que lo enmascara y lo elimina donde el bloque es
> plano — que es exactamente donde el grano estaba haciendo su trabajo de antibandeo.

Ochenta y cinco veces menos supervivencia en la zona que lo necesitaba. Por eso «le puse grano y la
banda sigue ahí» es tan frecuente: el grano estaba en el master y no llegó al export.

---

## 4. El recomprimido de red: el grano no llega, y encima estorba

Simulación de lo que hace una plataforma: subes 1080p CRF 18 y ella reescala a 1080 de ancho y
recodifica a CRF 28 con tope de 2 Mb/s. Mismo plano con movimiento, con grano y sin él:

| | bytes | σ temporal |
|---|---|---|
| original limpio (1080p, CRF 12) | 5 979 626 | 8,281 |
| lo que subes, con grano (CRF 18) | 6 335 068 | 8,461 |
| **lo que la red devuelve, desde el grano** | **124 594** | **5,715** |
| **lo que la red devuelve, desde el limpio** | **125 967** | **5,798** |

Los dos archivos que salen de la red pesan lo mismo (1 % de diferencia) y el que llevaba grano tiene
**menos** varianza temporal que el que no lo llevaba. Es decir: pagaste el grano en la subida, la red
lo borró, y además gastó parte de su presupuesto de bits en intentar codificarlo, así que devolvió una
imagen **algo más lavada** que si no lo hubieras puesto.

Y el caso extremo, ya medido en `editpro/442`: a CRF 24 el archivo **con** grano pesa 188 362 B frente
a 218 904 B del limpio. Un 14 % menos de bytes, el grano muerto, y ese 14 % salió del detalle real.

---

## 5. Qué hacer con esto

| Destino | CRF de export | Grano |
|---|---|---|
| Master / archivo | 12–16 | el que quieras; sobrevive |
| YouTube largo (recomprime suave) | 16–18 | `alls=4-6` con `u`, y verificar con σ |
| Reels / TikTok / Shorts | 18–20 | `alls=2-3` **solo por antibandeo** (`editpro/440`) |
| WhatsApp / CTWA | — | **ninguno**: no llega. Usa polvo (`editpro/442`) |

Tres tácticas que sí funcionan, en orden de eficacia:

1. **Bajar el CRF 2 puntos y bajar el grano a la mitad.** Cuesta menos bits que subir el grano y
   llegar con el 4 %.
2. **Textura escasa en vez de densa.** El polvo conserva el 86,8 % a CRF 18 y el 81,9 % a CRF 24, y
   cuesta 0 bytes. Un rasgo escaso de alto contraste se defiende; un rasgo denso de bajo contraste no.
3. **Grano solo donde hay banda.** Ver `editpro/448`. Aplicado en el 20 % del cuadro, el grano cuesta
   el 20 % y sobrevive igual, porque el codificador no lo tiene que sostener en todas partes.

Y `-tune grain`, que es lo primero que todo el mundo prueba, **depende del CRF**. Medido sobre el
mismo plano quieto con detalle:

| | CRF 18 bytes | σ | CRF 24 bytes | σ |
|---|---|---|---|---|
| sin `-tune` | 2 166 279 | 0,735 | 246 228 | 0,216 |
| `-tune film` | 3 168 316 (+46 %) | 0,844 (+15 %) | 270 419 (+10 %) | 0,254 (+18 %) |
| `-tune grain` | 3 873 085 (**+79 %**) | 0,916 (+25 %) | 353 623 (+44 %) | 0,382 (**+77 %**) |

En CRF 18 es un mal negocio: +79 % de archivo por +25 % de grano. En CRF 24, donde el grano se está
muriendo, sí compensa: +44 % de archivo por +77 % de grano. Y `-tune film` es el término medio
sensato en los dos. Nada de esto sobrevive al recomprimido de red del §4: allí el peso extra se
recorta igual.

---

## 6. La trampa del `-loglevel` (verificada hoy)

Todos los filtros de medida de ffmpeg —`psnr`, `ssim`, `signalstats`— **imprimen en nivel `info`**.
Con `-loglevel error`, que es lo que lleva casi todo script de producción, no sale **nada**: ni
resultado ni aviso. Parece que la medición ha fallado, o peor, se da por buena una tabla vacía.

```bash
# ❌ silencio absoluto: ni error, ni resultado
ffmpeg -loglevel error -i con_grano.mp4 -i limpio.mp4 -lavfi "[0:v][1:v]ssim" -f null -

# ✅
ffmpeg -hide_banner -loglevel info -i con_grano.mp4 -i limpio.mp4 -lavfi "[0:v][1:v]ssim" \
  -f null - 2>&1 | grep -i SSIM
# [Parsed_ssim_0 @ ...] SSIM Y:0.977967 (16.569262) ... All:0.976462 (16.282230)
```

Lo mismo con `-stats_file` si prefieres el volcado por fotograma. Y ojo: `-hide_banner` sí se puede
dejar, solo esconde la cabecera de compilación.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Juzgar el grano en el master y no en el export | El 96 % de supervivencia del master no dice nada del 4 % del export |
| Subir `alls` porque «se pierde al exportar» | Pagas más bits para llegar igual de muerto; baja el CRF en su lugar |
| Poner grano para WhatsApp o CTWA | No llega ni un 1 % |
| Medir la supervivencia con SSIM o VMAF | Miden la diferencia con el original, no si el grano vive (`editpro/449`) |
| Medir σ temporal sobre material con movimiento | El movimiento genera varianza y tapa el resultado |
| `-loglevel error` al medir | Silencio total; parece que falló |
| `-tune grain` a CRF 18 | +79 % de archivo por +25 % de grano: mal negocio |
| `-tune grain` esperando que sobreviva a la red | El peso extra se recorta igual en el reencode |
| Ver el archivo con grano más pequeño y pensar que comprime bien | Está más pequeño porque el codificador se comió el detalle |

---

## Relacionado

`editpro/428` el efecto que se rompe en la compresión (`YDIF`, las cuatro etapas de entrega, la tabla
de supervivencia por efecto y el simulador de entrega) · `editpro/421` el coste en bitrate como medida
de textura · `editpro/93` compresión sin perder calidad (el barrido de CRF y las tres métricas) ·
`editpro/440` cuánto grano hace falta de verdad · `editpro/441` grano temporal o congelado ·
`editpro/442` la textura escasa que sí sobrevive · `editpro/448` textura por capa, no global ·
`editpro/449` medir si la textura suma · `editpro/66` el grano y el CRF en la cadena de acabado ·
`canales/66` por qué el grano no va sobre el `concat` final
