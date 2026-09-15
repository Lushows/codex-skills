# 441 — Grano temporal o congelado: la diferencia que no se ve en una captura

Este es el módulo que más dinero salva de los diez, y trata de una sola letra: la `t` de
`allf=t`. La regla "pon la `t`" ya está dicha en `editpro/66` y en `canales/66`. Lo que falta —y es
lo que aquí se mide— es **por qué una captura de pantalla no puede detectar el error** y con qué
número se detecta.

---

## 1. El caso real del canal

En el piloto de PAPER EMPIRES los fondos se generan en Chrome (degradados + tres tramas cruzadas) y
**el grano no está en el PNG**. Está en el remate de ffmpeg. El comentario que quedó en el código lo
dice sin adornos:

```python
# piloto/episodio01/fondos.py
# La textura se hace ahora con degradados repetidos, que Chrome tesela sin
# problema, y el grano se aplica despues en ffmpeg (acabar.py ya lleva
# 'noise=alls=5:allf=t+u'), que ademas lo hace temporal en vez de congelado.
```

```python
# piloto/ep01-lustig/acabar.py:191
VF = ("eq=contrast=1.06:saturation=1.05:gamma=1.13:brightness=0.032,"
      "noise=alls=5:allf=t+u,vignette=PI/6.0,format=yuv420p")
```

El grano horneado en el PNG **no es un grano peor: es otra cosa**. Un grano que no cambia entre
fotogramas no se lee como material; se lee como suciedad **de la pantalla**, o como una capa pegada
encima del vídeo. El cerebro sabe distinguirlos porque la suciedad de una pantalla tampoco se mueve.

---

## 2. La prueba: dos vídeos que en una captura son idénticos

Mismo fondo de tinta 1920×1080, 4 s, 25 fps, CRF 18. A: grano horneado en el PNG (ruido uniforme
±5 niveles, fijo). B: PNG limpio + `noise=alls=5:allf=t+u` en ffmpeg.

```python
# medir_temporal.py — lo único que separa un grano vivo de uno muerto
import subprocess, numpy as np
def frames(mp4, W, H, n=12):
    raw = subprocess.run(["ffmpeg","-v","error","-i",mp4,"-frames:v",str(n),
        "-pix_fmt","gray","-f","rawvideo","-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
f = frames("salida.mp4", 1920, 1080)
print("sigma_temporal", f.std(axis=0).mean())   # desviación POR PÍXEL a lo largo del tiempo
print("sigma_espacial", f[0].std())             # desviación dentro de UN fotograma
```

| vídeo | σ **espacial** (lo que ve una captura) | σ **temporal** (lo que ve el ojo) | peso |
|---|---|---|---|
| Fondo limpio, sin grano | 7,138 | 0,002 | 51 062 B |
| **A — grano horneado en el PNG** | **8,010** | **0,000** | 755 300 B |
| **B — `noise=alls=5:allf=t+u`** | 7,208 | **0,586** | 2 577 540 B |

Ahí está todo el módulo:

- **La σ espacial de A es mayor que la de B** (8,010 frente a 7,208). En un fotograma suelto, el
  grano horneado se ve *más*. Una captura de pantalla no solo no detecta el error: **puntúa mejor
  al vídeo estropeado.**
- **La σ temporal de A es 0,000.** Cero absoluto: el mismo patrón, píxel a píxel, en los 100
  fotogramas. La de B es 0,586 *después de pasar por CRF 18*; antes de comprimir era 1,609.
- El grano temporal cuesta **3,4×** lo que el horneado y **50×** lo que el fondo limpio. No es
  gratis, y por eso hay que decidirlo con `editpro/446` y `editpro/448` delante.

> Regla operativa: **σ_temporal < 0,05 sobre material sin movimiento = el grano está muerto.**
> Entre 0,3 y 1,5 es un grano vivo que ha sobrevivido a la compresión.

---

## 3. Por qué se congela sin que nadie lo decida

Cuatro rutas, todas frecuentes:

| Ruta | Qué pasa |
|---|---|
| Grano horneado en el PNG del fondo | El fondo es una imagen fija: su grano también |
| `allf=u` o `allf=p` sin `t` | `p` es patrón fijo por definición; `u` sin `t` se calcula una vez |
| Grano en una capa PNG superpuesta con `overlay` | La capa es un still: se repite idéntica |
| Grano aplicado a un `loop`/`zoompan` de una foto antes del bucle | Entra en el bucle y se repite con él |

La cuarta es la más traicionera: el grano *sí* está en el filtro, pero por delante del `loop`, así
que se calcula una vez y luego se duplica. Se detecta igual: σ_temporal ≈ 0.

---

## 4. Las dos excepciones, y son de verdad

**Papel escaneado y fotocopia llevan grano FIJO.** Un documento cuyo grano tiembla se lee como vídeo
con filtro, no como papel: el papel está quieto porque es papel. `canales/66` lo tiene resuelto con
`allf=u` sin `t` en la receta de fotocopia; no lo repitas aquí, rútalo.

La segunda: **el polvo y el arañazo de una pieza escaneada van congelados con la pieza**, mientras
que los de película van por fotograma. `editpro/442` lo separa.

---

## 5. Dónde ponerlo si la pieza se mueve

Si el elemento tiene `zoompan`, `scale` animado o `rotate`, el grano tiene que ir **después** del
movimiento. Si va antes, el grano se mueve *con* la pieza, y un grano que hace paneo con la imagen
es exactamente el aspecto de "PNG con textura encima" que se intentaba evitar.

```bash
# ✅ correcto: la pieza se mueve, el grano se queda en el plano de la pantalla
... zoompan=z='min(zoom+0.0012,1.10)':d=125:s=1920x1080:fps=25, noise=alls=5:allf=t+u ...

# ❌ el grano viaja con la imagen: se lee como suciedad pegada al recorte
... noise=alls=5:allf=t+u, zoompan=z='min(zoom+0.0012,1.10)':d=125:s=1920x1080:fps=25 ...
```

Es la misma razón por la que el grano va al final de la cadena de acabado (`editpro/66`), pero por un
motivo distinto: allí es para no afilarlo; aquí es para que no viaje.

---

## 6. El coste, con números

Sobre 5 s de collage real a 1080p, CRF 12, en el equipo de trabajo:

| | tiempo | ×ref | bytes | ×ref |
|---|---|---|---|---|
| Sin filtro | 22,1 s | 1,00 | 5 979 626 | 1,00 |
| `noise=alls=5:allf=t+u` | 35,7 s | 1,62 | 50 758 199 | **8,49** |

El grano temporal es **barato en CPU y carísimo en bits**. Ese 8,49× es la cifra que obliga a los dos
módulos siguientes: no se puede pagar ocho veces el archivo por una textura que la red va a borrar
(`editpro/446`) ni por cubrir zonas que no la necesitan (`editpro/448`).

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Validar el grano mirando un fotograma exportado | La captura puntúa **mejor** al grano congelado (8,010 vs 7,208) |
| Hornear el grano en el PNG del fondo | σ_temporal 0,000: suciedad de pantalla, no material |
| `allf=p` creyendo que es "patrón de película" | `p` es el patrón fijo: el peor de los tres |
| Grano antes del `zoompan` o del `loop` | Viaja con la imagen o se repite con el bucle |
| Poner grano temporal a un documento escaneado | Papel que tiembla: se lee como filtro |
| Dar por bueno un σ_temporal medido sobre material con movimiento | El movimiento también genera varianza: solo vale sobre plano quieto o comparando dos versiones del mismo plano |
| Subir `alls` porque "no se nota" cuando lo que pasa es que está congelado | Se nota menos cuanto más congelado: se integra como textura de pantalla |

---

## Relacionado

`editpro/440` grano: por qué y cuánto · `editpro/442` papel, polvo y arañazo · `editpro/446` ruido
que sobrevive a la compresión · `editpro/448` textura por capa, no global · `editpro/449` medir si la
textura suma · `editpro/66` el orden de la cadena de acabado · `canales/66` grano por procedencia y
la receta de fotocopia con ruido fijo · `canales/35` animar una foto fija · `canales/50` la capa de
grano del canal
