# 242 · Colocación por rectángulo

**Qué resuelve:** una banda es una **etiqueta**; lo que se solapa en pantalla son
**rectángulos**. Mientras la colocación razonó con etiquetas, dos elementos en bandas
distintas se enterraban uno a otro y no había forma de saberlo sin ver el vídeo.

---

## El caso que lo obligó

Las bandas `centro` y `lado` se cruzan en el lienzo. Reservar la banda no impedía nada:
en el episodio 01 un retrato quedó **100 % enterrado durante 1,8 s** bajo un
organigrama, y se descubrió mirando la rejilla de fotogramas, ya renderizado. El
sistema decía que todo estaba en su sitio porque estaban en bandas distintas.

## Las tres funciones

**`proporcion(recurso)`** — `alto/ancho` del PNG, cacheado. Sin esto no hay rectángulo:
la tabla declara ancho, no alto.

**`rect(pos, ancho, recurso, encajar=True, centrado=False)`** — convierte una posición
declarada (`"W*0.26"` o píxeles) en `(x0, y0, x1, y1)`:

```python
x, y = px(pos[0], W_LIENZO), px(pos[1], H_LIENZO)
alto = ancho * pr
if centrado:                       # las BANDAS son centros; motor.py usa esquina
    x, y = x - ancho / 2.0, y - alto / 2.0
if encajar:
    mx, my = W_LIENZO * SANGRE, H_LIENZO * SANGRE
    x = min(max(x, -mx), W_LIENZO + mx - ancho)
    y = min(max(y, -my), H_LIENZO + my - alto)
return (x, y, x + ancho, y + alto)
```

`encajar` corre el elemento hacia dentro en vez de descartarlo, que es lo que conserva
la densidad (`245`). `encajar=False` es para **medir**: cuando se quiere saber cuánto se
sale de verdad, no cuánto se saldría si se le dejara.

**`pisa(a, b)`** — cuánto de `a` queda debajo de `b`, en tanto por uno de la superficie
de `a`. No es simétrica, y por eso se comprueban las dos direcciones: un rótulo pequeño
puede quedar al 90 % tapado por un documento que solo pierde el 8 % de sí mismo.

```python
ch = max(pisa(c, o), pisa(o, c))
```

## Dos umbrales, no uno

El listón no puede ser el mismo para una foto que para una cifra. Tapar el 20 % de una
fotografía no molesta a nadie; tapar el 20 % de un número lo hace ilegible.

```python
tope = 0.05 if (txt or es_texto(recurso)) else 0.42
```

Con el umbral único del 42 % entraban recortes encima de las cifras y el sistema los
daba por buenos. `es_texto()` decide por dos vías: el recurso vive en `texto/`, o su
alias empieza por uno de los prefijos del canal (`sello_`, `m_`, `linea_`, `t_`, `d_`,
`r_`, `c_`, `f_`, `p_`).

## Lo que cuesta de verdad

Instrumentando los `continue` de `generar()` sobre `ep01-lustig` (16 posiciones
candidatas por palabra):

```
  posiciones probadas                    672
  rechazadas por no caber                  0
  rechazadas por pisar TEXTO (tope 5%)   374
  rechazadas por pisar FOTO  (tope 42%)  157
  palabras perdidas (ninguna posicion)    15
  colocadas                               27
```

Tres lecturas que no se ven mirando el vídeo:

1. **El texto rechaza más del doble que la foto.** 374 contra 157. El 5 % es un listón
   durísimo, y es el correcto: la mitad del contenido del canal son documentos.
2. **`no cabe` no rechaza nada.** Con anclaje central y encaje activo, toda posición
   entra en el lienzo (`243`). Esa comprobación hoy es un cinturón de seguridad, no un
   filtro.
3. **15 palabras mapeadas se quedan fuera** de 42 intentos. Eso no es un fallo: es la
   decisión de que amontonar un elemento encima de otro cuesta un evento y no comunica
   nada. Si el número sube mucho, lo que falta es material o bandas, no umbral.

## Buscar donde busca el motor

`proporcion()` necesita encontrar el fichero. Si busca en menos carpetas o con menos
extensiones que `motor.buscar()`, pasa lo peor que puede pasar:

> el motor encuentra `billete.jpg` en `archivo/` y lo renderiza; `proporcion()` no lo
> encuentra, devuelve `None`, `rect()` devuelve `None` y el elemento **desaparece de la
> colocación y de la medida… pero sale en el vídeo**.

El montaje medido deja de ser el montaje renderizado, y **las métricas mejoran al no
medir lo que sobra**. Pasó con 36 y 77 ficheros `.jpg`/`.webp` de las dos carpetas de
archivo. Por eso las constantes están escritas como constantes, para que se vean:

```python
CARPETAS = ("texto", "fx", "recortes", "recursos", "render", "archivo")
EXTENSIONES = (".png", ".jpg", ".webp")
```

## El aire temporal

Dos elementos que no coinciden en el tiempo no se pisan aunque compartan rectángulo.
`_solapan()` añade 0,15 s de aire por si acaso:

```python
def _solapan(a0, a1, b0, b1, aire=0.15):
    return a0 < b1 + aire and b0 < a1 + aire
```

El aire existe porque la vida declarada no es la vida visible: `motor.py` sube en 0,30 s
y baja en `fade_out` (`13`, `144`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Razonar con la etiqueta de la banda | Un retrato enterrado 1,8 s bajo un organigrama |
| Un solo umbral de solape | Recortes encima de las cifras, aprobados por el sistema |
| Usar `pisa()` en un solo sentido | El pequeño queda tapado y la comprobación no lo ve |
| Buscar en menos carpetas que `motor.buscar()` | Elementos invisibles para la medida y visibles en el vídeo |
| Medir con `encajar=True` | Se mide dónde debería estar, no dónde está |
| Descartar en vez de encajar | Se pierde densidad por elementos que solo había que correr |

## Relacionado

`20` retícula del collage · `26` superposición y oclusión · `243` bandas y anclaje
central · `244` el techo de altura · `245` la sangría · `246` equilibrio del cuadro
