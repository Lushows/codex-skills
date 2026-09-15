# 448 — Textura por capa, no global

`canales/66` ya establece la regla para el canal: el grano va **al elemento**, no al vídeo, y el
`noise` sobre el `concat` final está prohibido. Este módulo no la repite: la **cuantifica** —cuánto
cuesta exactamente cada punto de cobertura— y añade la razón que ahí no aparece, que es de textura y
no de peso: **cada capa tiene un objetivo de textura distinto, y una manta global falla los dos.**

---

## 1. El coste es lineal en superficie cubierta

Mismo plano de 5 s, mismo `noise=alls=5:allf=t+u`, CRF 18 (el de publicación):

| | bytes | × limpio | sobrecoste | % del sobrecoste global |
|---|---|---|---|---|
| limpio | 2 234 030 | 1,00 | — | — |
| grano en el 20 % del cuadro | 2 974 865 | **1,33** | 740 835 | **19,2 %** |
| grano en el 50 % | 4 112 414 | 1,84 | 1 878 384 | 48,7 % |
| grano **global** | 6 092 871 | **2,73** | 3 858 841 | 100 % |

19,2 % de sobrecoste por 20 % de superficie; 48,7 % por 50 %. **El grano se paga por metro
cuadrado.** No hay economía de escala ni penalización por trocear: si lo aplicas al 20 % del cuadro,
pagas el 20 %.

Esto convierte la decisión en aritmética. Un fondo de tinta con degradado ocupa quizá el 60 % del
cuadro útil; los recortes y el texto, el 40 % restante. Aplicar el grano solo al fondo cuesta el 60 %
de 2,73×, o sea **1,04× el archivo limpio más el 60 % del extra** — y deja los recortes intactos.

---

## 2. La razón que no es el peso: cada capa quiere otra textura

De `editpro/447`, medido: la razón p95/suelo del material de archivo real vive entre **10 y 16**, y
la de un fondo del canal entre **2 y 7**, porque un fondo es una superficie y no una fotografía. Son
dos objetivos distintos.

Una manta global de `alls=5` (σ 0,99) hace las dos cosas mal a la vez:

| capa | razón antes | razón después de la manta | resultado |
|---|---|---|---|
| Recorte de archivo | 15,15 | **8,18** | sale del rango del material real: «archivo con filtro» |
| Fondo del canal | 2,03 – 6,69 | baja también | pierde la trama que le daba superficie |
| Texto y rótulos | — | ruido sobre el borde de la letra | se ensucia la legibilidad (`editpro/376`) |

Y hay una cuarta capa a la que el grano global le hace daño puro: **el documento**. Está en pantalla
para leerse; el grano le quita contraste a la tinta contra el papel, que es lo único que lo hace
legible. `canales/197` lo tiene explícito (`virar=0`, `grano=False`, nitidez positiva).

---

## 3. Cómo se hace, por región

Para una capa rectangular —que es el caso del fondo— basta recortar, granular y volver a montar:

```bash
# grano solo en la banda superior, que es donde está el degradado que bandea
ffmpeg -y -i in.mp4 -filter_complex "\
[0:v]split=2[f][z];\
[z]crop=1920:216:0:0,noise=alls=5:allf=t+u[g];\
[f][g]overlay=0:0,format=yuv420p" \
  -c:v libx264 -crf 18 -preset slow -c:a copy out.mp4
```

Para una capa con alfa —un recorte— el grano va **al elemento**, y hay que separar el alfa antes de
tocarlo o `noise` se come el borde. Esa cadena (`alphaextract` / `alphamerge`) ya está resuelta y
verificada en `canales/66`: úsala tal cual.

Para una máscara arbitraria, dos rutas según dónde viva el vídeo:

| Situación | Ruta |
|---|---|
| La capa se genera en el pipeline (PNG, HTML) | Grano horneado **si la capa es papel o documento**; si no, ffmpeg por elemento (`editpro/441`) |
| El montaje ya está aplanado | `maskedmerge` con una máscara en gris, o `crop`+`overlay` por rectángulos |
| El fondo se genera y los recortes se pegan encima | Granular el fondo **antes** de pegar los recortes: es lo más barato y lo más correcto |

La tercera es la buena, y es gratis: el grano entra en la cadena del fondo y nadie paga nada extra.

---

## 4. La contradicción del piloto, y qué hacer con ella

`canales/66` dice, con razón:

> ❌ `noise` sobre el `concat` final

Y sin embargo la cadena de acabado real hace exactamente eso, en las tres versiones del episodio:

```python
# piloto/ep01-lustig/acabar.py:191
VF = ("eq=contrast=1.06:saturation=1.05:gamma=1.13:brightness=0.032,"
      "noise=alls=5:allf=t+u,vignette=PI/6.0,format=yuv420p")
# piloto/acabar.py:96-97
"noise=alls=6:allf=t+u,"
"vignette=PI/5.6,"
```

No es una chapuza: es un intercambio consciente. El grano global **es lo único que hace el grano
temporal** cuando los fondos vienen de PNG (ver `editpro/441` §1), y hacerlo por capa exige tocar el
motor. Pero conviene saber qué se está pagando: **×2,73 el archivo a CRF 18**, más la razón p95/suelo
de los recortes cayendo de 15,15 a 8,18.

La salida ordenada, en orden de esfuerzo:

1. **Bajar `alls` a 2–3.** El antibandeo, que es la única función técnica, está hecho en σ 0,5
   (`editpro/440` §2). Cuesta la mitad y no toca los recortes.
2. **Granular el fondo dentro de su propia cadena**, antes de componer. Coste ≈ el de la superficie
   del fondo. Es la solución correcta.
3. **Grano por elemento para los recortes que deban temblar**, con la receta de alfa de `canales/66`.

---

## 5. El orden dentro de cada capa

La regla general (`editpro/66`) es que el grano va al final. Por capa, hay que añadirle una segunda:
**el grano va después del movimiento de esa capa**. Si la capa tiene `zoompan` o `scale` animado y el
grano va antes, viaja con la imagen y se lee como suciedad pegada al recorte (`editpro/441` §5).

```
fondo:    degradados → trama → [grano] → componer
recorte:  pieza → virado → escalado/zoompan → [grano con alfa separado] → componer
texto:    sin grano, nunca
remate:   look → viñeta → [grano de antibandeo mínimo, si la viñeta lo pide] → yuv420p
```

Ese «grano de antibandeo mínimo» del remate es el único que sí es global, y tiene justificación: la
viñeta **crea** una rampa nueva después de todo lo demás (`editpro/444` §4), y esa rampa necesita
dither. Pero es `alls=2-3`, no `alls=5`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `noise` sobre el vídeo entero por comodidad | ×2,73 el archivo, y la textura de todas las capas igualada |
| Suponer que trocear el grano sale más caro | Medido: el coste es lineal en superficie, sin penalización |
| Grano sobre el texto | Ensucia el borde de la letra y no aporta nada |
| Grano sobre un documento | Le quita el contraste tinta/papel, que es su única función |
| Grano sobre un recorte rgba sin separar el alfa | El borde se come y salen puntos transparentes (`canales/66`) |
| Grano antes del `zoompan` de la capa | Viaja con la imagen |
| Granular el fondo *después* de pegar los recortes | Pagas el cuadro entero pudiendo pagar el 60 % |
| Duplicar el grano: el del fondo más el del remate | Se suman y el fondo queda al doble sin que nadie lo decida |
| Dar por buena la cadena global sin saber qué cuesta | Es una decisión legítima; no saberla no lo es |

---

## Relacionado

`canales/66` grano al elemento, la cadena de alfa y las cuatro recetas por procedencia ·
`canales/50` el esqueleto de capas del fondo y su capa de grano ·
`editpro/441` grano temporal o congelado · `editpro/440` cuánto grano hace falta ·
`editpro/446` ruido que sobrevive a la compresión · `editpro/447` el objetivo de textura por capa ·
`editpro/444` la rampa que crea la viñeta · `editpro/449` medir si la textura suma ·
`editpro/66` el orden de la cadena de acabado · `editpro/105` superponer capas en ffmpeg
