# 466 — La sombra dura falsa: el borde que no cambia con la distancia

**Qué resuelve:** la sombra proyectada de un recorte, de un rótulo o de un elemento gráfico es uno de
los delatores más fiables que existen, porque **la física de una sombra es simple y todo el mundo la ha
visto diez mil veces sin mirarla**. Un preset de "sombra paralela" la reproduce mal siempre de la misma
manera, y eso se mide con una regla y dos perfiles de píxeles.

Este módulo es el complemento medido de `263-integrar-un-elemento.md`, que es donde está el
procedimiento de integración completo.

---

## 1. La física, en dos frases

La penumbra —el borde difuso de una sombra— **crece con la distancia entre el objeto y la superficie**.
Justo en el punto de contacto la sombra es dura y oscurísima; a un metro, es ancha y clara. Por eso la
sombra de tus pies es nítida y la de tu cabeza no.

De ahí salen las dos magnitudes:

1. **Anchura de penumbra** (píxeles entre el 10% y el 90% del escalón de luminancia), medida a varias
   distancias del punto de contacto. En una sombra real, **crece**.
2. **Densidad**, medida igual. En una sombra real, **se aclara** al alejarse del contacto.

Un preset aplica un difuminado uniforme y una opacidad uniforme: ambas magnitudes salen **planas**.

---

## 2. La medición

```python
def penumbra(im, x):
    """px entre el 10% y el 90% del escalón, en la columna x."""
    col = im[200:300, x].astype(np.float32)
    lo, hi = col.min(), col.max()
    if hi - lo < 3: return float('nan')
    a = (col - lo) / (hi - lo)                 # 1 = suelo claro, 0 = sombra
    return float(abs(np.argmax(a < 0.10) - np.argmax(a < 0.90)))
```

Se mide en cuatro columnas: a 20, 120, 300 y 440 píxeles del punto de contacto. Y se calcula la razón
`penumbra lejos ÷ penumbra cerca`, que es el número que decide.

---

## 3. Los tres casos, medidos

Banco de 700×600: un objeto apoyado en un suelo claro (valor 198) y una banda de sombra recta que se
aleja 460 px. Tres tratamientos: la sombra dura pegada (difuminado σ=1), el preset típico de aplicación
(σ=9 uniforme) y una sombra construida con penumbra creciente y opacidad decreciente.

| Sombra | d=20 px | d=120 px | d=300 px | d=440 px | **Razón lejos/cerca** | Densidad en el contacto | Densidad lejos |
|---|---|---|---|---|---|---|---|
| Dura pegada | 2 px | 2 px | 2 px | 2 px | **1,0×** | 89 | **89** |
| Preset (σ=9 uniforme) | 24 px | 24 px | 24 px | 24 px | **1,0×** | 99 | **92** |
| Construida con física | **6 px** | **26 px** | **54 px** | **56 px** | **9,3×** | **69** | **173** |

Las dos columnas de la derecha son la segunda mitad del delator: en el preset la sombra vale 99 en el
contacto y 92 a 440 píxeles —**es igual de oscura en todas partes**, con el suelo a 198—. En la
construida va de 69 (casi negra, ahí se apoya) a 173 (casi el suelo): **se disuelve**.

> **Umbral: razón lejos/cerca por debajo de 2× y la sombra es una capa pegada.** Una sombra real de un
> objeto apoyado está entre 4× y 15× según el tamaño de la fuente de luz.
>
> **Segundo umbral: si la sombra no es más oscura en el contacto que a media distancia, no hay contacto**
> y el elemento flota. Es el mismo fallo que el recorte sin sombra de contacto de `263`.

---

## 4. Cómo se construye la buena

La receta: difuminar **por franjas de distancia**, cada una con su sigma, y multiplicar por una opacidad
que decrece. En una sola pasada no se puede, porque un difuminado gaussiano tiene un solo radio.

```python
s = np.zeros_like(mascara)
for d0 in range(0, LARGO, 10):                       # franjas de 10 px
    fr = np.zeros_like(mascara)
    fr[:, CONT+d0:CONT+d0+10] = mascara[:, CONT+d0:CONT+d0+10]
    s += gaussian_filter(fr, 1.2 + 0.075*d0)         # la penumbra crece con la distancia
x = np.arange(W)[None, :]
opac = np.clip(0.68 - 0.0011*np.maximum(x-CONT, 0), 0.16, 0.68)
img = suelo * (1 - np.clip(s,0,1) * opac)
```

Los dos coeficientes son los que hay que tocar: `0.075` es cuánto se abre la penumbra por píxel de
distancia (fuente grande y cercana → más; sol → mucho menos) y `0.0011` es cuánto se aclara.

Y en la línea de tiempo, cuando no vas a programar nada, la versión práctica son **dos capas**:

| Capa | Qué es | Difuminado | Opacidad |
|---|---|---|---|
| **Contacto** | la silueta pegada al punto de apoyo, pequeña | 2–4 px | 55–70% |
| **Proyección** | la sombra larga, desplazada y deformada | 20–50 px | 15–25% |

Dos capas dan una razón medida muy por encima de 2× y cuestan un minuto. El resto de la integración
—temperatura, grano común, borde del recorte— está en `263` y en `81-recortes-sin-fondo.md`.

---

## Errores frecuentes

1. **Usar el preset de sombra paralela del programa y subirle el difuminado.** Sube los 24 px a 40 px,
   pero la razón sigue siendo 1,0×: el problema no es cuánto difumina, es que difumina igual en todas
   partes.
2. **Poner solo la proyección y olvidar el contacto.** El elemento flota. Es el fallo más común con
   recortes y rótulos.
3. **Sombra a opacidad uniforme.** Medido: densidad 99 en el contacto y 92 a 440 px. Una sombra real se
   disuelve.
4. **Sombra más oscura que el negro del plano.** Una sombra no es un agujero: es una zona menos
   iluminada. Si tu sombra tiene valor 0 y el negro de la escena es 21, la sombra "brilla" al revés.
5. **Sombra con la dirección de luz equivocada.** Antes de medir nada, mira de dónde viene la luz en la
   placa: la sombra va al lado contrario (`223-esquemas-de-iluminacion.md`).
6. **Sombra perfectamente definida en un plano con luz difusa.** Un día nublado no produce bordes duros;
   una penumbra estrecha en una escena de luz suave se lee como pegatina.
7. **Medir la penumbra en diagonal.** El perfil se toma perpendicular al borde de la sombra; si cruzas
   el borde en ángulo, la anchura sale inflada y sin sentido.

---

## Relacionado

- `263-integrar-un-elemento.md` — **la integración completa: sombra, color, grano, borde.**
- `262-la-tecnica-del-sandwich.md` · `81-recortes-sin-fondo.md` — poner el elemento en la escena.
- `223-esquemas-de-iluminacion.md` — de dónde viene la luz y, por tanto, adónde va la sombra.
- `221-profundidad-de-campo.md` — la otra magnitud que cambia con la distancia.
- `421-medir-lo-que-un-efecto-cambia.md` (§5) — medir sobre una región y no sobre el cuadro entero.
- `56-efectos-que-se-ven-baratos.md` — el marco: por qué un borde demasiado limpio delata.
- `460-el-catalogo-medido.md` — el banco y las seis magnitudes.
