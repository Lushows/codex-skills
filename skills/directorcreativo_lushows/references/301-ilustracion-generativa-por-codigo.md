# 301 · Ilustración generativa por código

> Cómo convertir el oficio de [[300-ilustracion-cientifica-y-botanica]] en algo que se genera
> con un script y sale en SVG vectorial. No es "un filtro": es dibujar con reglas.
> Lo que se gana: consistencia absoluta entre piezas, escalabilidad real a imprenta, y un
> sistema que crece solo cuando llega un producto nuevo.

---

## 1 · La regla que ordena todo

**Una morfología, un algoritmo.** Un solo generador para varios sujetos siempre delata el
algoritmo, no el sujeto.

> Caso real (BIO-SETA): se usó *colonización del espacio* para dibujar tres hongos distintos.
> Ese algoritmo nace de un punto y se ramifica, así que **siempre produce un abanico** —
> los tres salieron iguales aunque cada uno tenía su propia silueta de referencia.
> La solución fue estudiar cómo crece cada especie y escribirle su propia ley:
> el haz de clavas, el abanico concéntrico, la cascada colgante.

**Antes de programar, describe el crecimiento en una frase.** Si no puedes, todavía no
entendiste la forma.

---

## 2 · El trazo ahusado — el detalle que más rinde

`stroke-width` en SVG es constante por trazo. Un dibujo hecho de líneas de grosor uniforme
se ve **de máquina**. La solución es dibujar el trazo como un **polígono relleno** cuyo ancho
varía a lo largo del recorrido.

```python
def trazo_ahusado(pts, w0, w1, perfil=lambda t: 1.0):
    """Polígono relleno alrededor de una polilínea, con ancho variable.
    w0 = ancho al inicio, w1 = al final, perfil = modulación extra 0..1."""
    izq, der = [], []
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        # normal a la dirección local
        px, py = pts[max(i-1, 0)]
        qx, qy = pts[min(i+1, n-1)]
        dx, dy = qx - px, qy - py
        L = (dx*dx + dy*dy) ** .5 or 1.0
        nx, ny = -dy/L, dx/L
        w = (w0 + (w1 - w0) * t) * perfil(t) / 2
        izq.append((x + nx*w, y + ny*w))
        der.append((x - nx*w, y - ny*w))
    return izq + der[::-1]      # contorno cerrado
```

Perfiles útiles:

| Perfil | Fórmula | Para qué |
|---|---|---|
| Hoja / espina | `sin(pi*t)**0.6` | Fino, gordo al medio, fino |
| Pincelada | `(1-t)**0.7` | Grueso al inicio, se desvanece |
| Raíz | `(1-t)**1.4` | Se afila rápido |
| Pelo | `1 - t**3` | Aguanta y colapsa al final |

---

## 3 · Modelo de luz mínimo

No hace falta un motor 3D. Con una normal aproximada basta para tener las seis zonas del
módulo 300.

```python
LUZ = (-0.6, -0.8)     # desde arriba-izquierda, normalizado

def valor(nx, ny):
    """0 = luz plena, 1 = sombra profunda. nx,ny = normal aproximada."""
    d = nx*LUZ[0] + ny*LUZ[1]          # producto punto
    v = 1 - (d * 0.5 + 0.5)            # 0..1
    nucleo = max(0.0, 1 - abs(d + 0.15) * 3.2)   # franja más oscura
    reflejo = max(0.0, -d - 0.55) * 0.45         # rebote en la cara oscura
    return min(1.0, max(0.0, v + nucleo*0.30 - reflejo))
```

En una forma cilíndrica (una clava, un tallo), la normal en el offset lateral `u ∈ [-1,1]`
es simplemente `nx = u`, `ny = -sqrt(1-u²)`. Con eso ya tienes el núcleo de sombra bien puesto.

---

## 4 · Trama que envuelve, generada

La clave es **generar la trama en el espacio del objeto, no en el del lienzo**.

1. Parametriza la superficie: `(u, v)` donde `u` recorre el contorno y `v` la longitud.
2. Dibuja líneas de `u` constante (envuelven) o de `v` constante (anillos).
3. Convierte `(u,v) → (x,y)` con la geometría de la forma.

Así la trama sigue el volumen aunque la forma esté torcida. Trazar en el lienzo produce
el rayado en diagonal que delata al aficionado.

---

## 5 · Puntillismo por valor

```python
def puntillismo(rnd, region, valor_fn, densidad=0.9, r=(0.35, 1.1)):
    """Rechazo: la probabilidad de poner un punto sigue el valor local."""
    puntos = []
    for _ in range(int(len(region) * densidad * 40)):
        x, y, u, v = rnd.choice(region)
        val = valor_fn(u, v)
        if rnd.random() < val ** 1.6:          # exponente = contraste
            puntos.append((x, y, rnd.uniform(*r) * (0.6 + 0.7*val)))
    return puntos
```

Dos ajustes que deciden la calidad:
- **El exponente** (`1.6`) controla el contraste. Bajo = plano; alto = duro.
- **El radio ligado al valor** — puntos más gordos en sombra — evita el aspecto de ruido digital.

---

## 6 · Jerarquía del detalle, programada

```python
def factor_detalle(x, y, foco, radio):
    """1.0 en el punto focal, cae hacia afuera. Multiplica densidades."""
    d = ((x-foco[0])**2 + (y-foco[1])**2) ** .5
    return max(0.18, 1.0 - (d / radio) ** 1.5)
```

Se multiplica por la densidad de puntillismo, por el número de líneas de trama y por la
opacidad. **Sin esto, todo el dibujo tiene el mismo peso y se lee como textura, no como forma.**

---

## 7 · Bordes: cómo se pierde uno a propósito

En código, un borde perdido es simplemente **opacidad que cae a cero en la zona de luz**:

```python
op = 0.85 * min(1.0, valor(nx, ny) * 1.6 + 0.10)
```

Donde la superficie mira a la luz, `valor→0` y el trazo casi desaparece. El contorno se
interrumpe solo, sin tener que decidirlo a mano.

---

## 7bis · El dibujo gestual de garabato *(scribble)*

La técnica más **estética** de las generativas, y la más fácil de arruinar. Sus cinco leyes:

1. El valor se construye por **acumulación de trazos sueltos que se cruzan**, no por puntos
   ni por trama ordenada.
2. Los trazos van **en muchas direcciones**. Se cruzan libremente.
3. **NO hay contorno dibujado.** El borde aparece donde los trazos se detienen.
4. Los trazos **se pasan del borde**. Ese desborde es lo que se lee como mano.
5. Hay **trazos de fuga**: líneas largas y sueltas que salen del dibujo y no describen nada.
   Son la firma del estilo — sin ellas se ve tímido.

El grosor es casi constante (es una pluma). Lo que cambia es **cuántos trazos hay**.

### Las cuatro pasadas, en este orden

| # | Pasada | Qué hace | Si falta |
|---|---|---|---|
| 1 | **Relleno de papel** | Cada cuerpo se rellena del color del fondo antes de rayarse | Los garabatos de un cuerpo invaden al vecino y todo se lee como un bloque macizo |
| 2 | **Volumen** | Garabatos con densidad ∝ valor, **alineación baja (0.2–0.3)** | Con alineación alta todo se lee como pasto peinado |
| 3 | **Filo** | Trazos cortos pegados al borde y **alineados con él** | El volumen se lee pero la silueta no: queda una mancha |
| 4 | **Fuga** | Pocos trazos largos, sueltos, fuera del dibujo | Se ve rígido y digital |

### Los dos números que deciden todo

- **`gamma`** en la aceptación por valor. Con 1.2 el dibujo se llena y muere; con 2.4 la mitad
  iluminada desaparece. **El punto dulce está en 1.8–1.9.**
- **`alineacion`** 0 = caos, 1 = todos siguen la forma. Volumen ~0.2, filo ~0.95.

> **Aprendizaje duro:** el filo de una forma con cúpula (una clava, una cabeza) necesita su
> **propia pasada de arcos**. Si solo se perfila el eje, la forma se lee como tallo largo y
> nunca como clava, por muy bien que esté el volumen.

---

## 8 · Reglas de producción

- **Semilla fija** (`random.Random(26)`): la ilustración es un activo de marca, tiene que
  salir idéntica siempre. Una pieza que cambia cada vez que se corre el script no es un activo.
- **SVG de salida**, no PNG: escalable, editable, apto para imprenta.
- **Nada de `mix-blend-mode` ni `mask-image`** si va a un PDF — hay visores que no los componen
  y borran la capa. Todo efecto se hornea en el píxel o se resuelve con opacidad simple.
- **Parámetros con nombre arriba del archivo**: número de elementos, radios, densidades.
  El dibujo se ajusta cambiando números, no reescribiendo el generador.
- **Un archivo por morfología**, no un generador universal con banderas.

---

## 9 · Lista de verificación

- [ ] ¿Describí el crecimiento en una frase antes de programar?
- [ ] ¿Cada sujeto tiene su propio generador?
- [ ] ¿Los trazos son ahusados o todos del mismo grosor?
- [ ] ¿La trama envuelve la forma o va en diagonal del lienzo?
- [ ] ¿Hay núcleo de sombra y luz reflejada, o solo un degradado?
- [ ] ¿Hay jerarquía de detalle o todo tiene la misma densidad?
- [ ] ¿La semilla está fija?
- [ ] ¿La textura distingue el material?
