# 382 — La zona protegida: dentro de un elemento no todo pesa igual

**Qué resuelve:** `381` deja claro que hay que medir el contenido y no el rectángulo. Falta la otra mitad:
**dentro del contenido tampoco todo vale lo mismo.** Un retrato con el 25% tapado está bien si el 25% es el
abrigo y está muerto si son los ojos. Este módulo pone ese «dónde» en un rectángulo que se puede medir.

---

## 1. Tres zonas que se confunden y no son la misma

| Zona | De quién es | Quién la define | Dónde está |
|---|---|---|---|
| **zona segura de plataforma** | del **cuadro** | Instagram, TikTok, YouTube | `45` |
| **zona del sujeto** | del **cuadro** | la composición en capas | `204` §4 |
| **zona protegida** | del **elemento** | el contenido de esa pieza | **este módulo** |

Las dos primeras dicen dónde no se pone nada. Esta dice **qué parte de una pieza no se puede tapar**, y
viaja con la pieza: si el elemento se mueve, su zona protegida se mueve con él.

---

## 2. La zona protegida por clase de pieza

Cada clase tiene su parte irrenunciable, y en todas se puede escribir como una fracción de la caja:

| Clase | Qué hay que salvar | Rectángulo | Por qué |
|---|---|---|---|
| retrato de persona | ojos y frente | **40% superior** | la identidad vive ahí; el cuerpo es relleno |
| rótulo de una línea | la línea entera | **100%** | tapado a medias deja el objeto sin explicar |
| cifra | los dígitos | **caja útil entera** | media cifra es una cifra falsa |
| documento / acta | el encabezado y el sello | 30% superior + sello | es lo que prueba que es un documento |
| ficha de datos | primera fila | 35% superior | el resto se infiere, la primera no |
| línea de tiempo | el hito nuevo | el hito, no la línea | lo viejo ya se vio |
| marca de columna | la palabra | 100% | es una señal, no una ilustración |
| foto de ambiente | nada | 0% | es fondo, se puede morder entera |

La última fila es la que da valor a la tabla: **hay piezas sin zona protegida**, y saberlo permite apilar
sin miedo justo donde antes se dejaba aire por si acaso.

---

## 3. Medirlo: la misma función, otro rectángulo

No hace falta una medida nueva. Es `pisa()` aplicada a un sub-rectángulo:

```python
def zona(c, frac=0.40, desde="arriba"):
    """El rectangulo protegido de un elemento, en fraccion de su alto."""
    x0, y0, x1, y1 = c
    alto = y1 - y0
    if desde == "arriba":
        return (x0, y0, x1, y0 + alto * frac)
    return (x0, y1 - alto * frac, x1, y1)

PROTEGIDA = {          # fraccion protegida por clase (0 = no tiene)
    "heroe": 0.40, "dato": 1.00, "rotulo": 1.00,
    "objeto": 0.00, "micro": 0.35, "peso": 0.00,
}

def dano(c_victima, c_rival, clase):
    frac = PROTEGIDA.get(clase, 0.0)
    if frac <= 0:
        return pisa(c_victima, c_rival)
    return max(pisa(c_victima, c_rival), pisa(zona(c_victima, frac), c_rival))
```

`max()` entre la caja y la zona, no la zona sola: un elemento con la mitad inferior sepultada también está
roto aunque la cabeza se vea.

---

## 4. Lo que cambia al medir por zona: números reales

Mismas parejas, dos varas de medir. Todo de la medición de hoy, con la zona protegida al 40% superior:

**`ep01-lustig`**

| El de abajo | El de encima | Caja | Zona protegida | Dur |
|---|---|---|---|---|
| `columna_doble` | `boveda_servicio` | 23,7% | **59,2%** | 0,33 s |
| `chatarreria` | `torre_construccion` | 10,8% | **27,0%** | 0,98 s |
| `telegrama_marshal` | `torre_postal` | 10,3% | **25,9%** | 1,76 s |
| `torre_citroen_noche` | `monton_chatarra` | 7,5% | 18,8% | 1,57 s |
| `casilla_nombre` | `sin_padre` | 28,0% | 28,0% | 1,07 s |

**`episodio01`**

| El de abajo | El de encima | Caja | Zona protegida | Dur |
|---|---|---|---|---|
| `fajo` | `fajo` | 28,7% | **67,1%** | 1,03 s |
| `diag_lavado` | `con_cifuentes` | 30,5% | **56,7%** | 0,13 s |
| `jerarquia` | `jerarquia` | 22,1% | **55,3%** | 0,56 s |
| `planta_pescado` | `planta_pescado` | 19,6% | **37,1%** | 3,16 s |

Dos cosas que salen solas de estas tablas:

1. **El factor típico entre caja y zona es 2,3–2,6×.** Un 25% de caja es rutinariamente un 60% de cabeza.
2. **Cuando la pisada entra por abajo, los dos números coinciden** (`casilla_nombre`, 28,0% y 28,0%): la
   zona no se toca. Ahí la caja ya bastaba y la medida extra no molesta.

El caso que justifica todo el módulo es el último de `episodio01`: `planta_pescado` bajo otra copia de sí
misma, **19,6% de caja durante 3,16 s**. Por caja es la pisada número doce del episodio y nadie la mira.
Por zona protegida es un 37,1% de cabeza tapada durante más de tres segundos: es de las peores del
episodio.

---

## 5. Cuándo la zona protegida no es el tercio de arriba

Tres excepciones que hay que declarar a mano o el automatismo se equivoca:

- **Retrato de cuerpo entero o plano medio bajo.** La cara ocupa el 15% superior, no el 40%; medir al 40%
  mete el torso y diluye el daño. Se declara `frac` por pieza, no por clase.
- **Documento con el sello abajo.** `desde="abajo"`. El sello rojo es lo que cierra el asunto
  (`canales_lushows/26`) y taparlo deja el documento sin sentencia.
- **Pieza de dos columnas** (`columna_doble` del piloto). La zona protegida es vertical, no horizontal: hay
  que salvar el eje que separa las dos mitades, porque la forma **es** el argumento.

---

## 6. Lo que ya está dicho en otro sitio

- La lista prescriptiva de lo que **nunca** se tapa —la cifra mientras se dice, el rótulo, los ojos, el
  elemento que sostiene la frase que se oye— es `canales_lushows/26`, sección «Lo que nunca se tapa». No se
  repite: este módulo solo la traduce a rectángulos medibles.
- Cuánto de una **palabra** puede taparse sin dejar de leerse (60% del ancho visible, primera letra
  siempre, oclusión por el final y no por el medio) es `377` §3.
- La zona del cuadro donde no va texto porque se la come la interfaz es `45`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Usar la misma fracción protegida para todas las clases | En un plano medio bajo, el 40% incluye el torso y diluye el daño |
| Medir **solo** la zona y no la caja | Un elemento con la mitad inferior sepultada pasa la prueba |
| Olvidar que la zona viaja con el elemento | Con `deriva` activa, la zona se calcula en el sitio de la entrada (`389`) |
| Dar zona protegida a las fotos de ambiente | Se pierde la libertad de apilar justo donde no importa |
| Poner la zona arriba en un documento con sello abajo | Se protege el encabezado y se entierra la sentencia |
| Confundirla con la zona segura de la plataforma | Son cosas distintas: una es del elemento, la otra del cuadro (`45`) |
| Declarar la zona y no meterla en el umbral | Se mide y no se actúa: el informe crece y el vídeo no mejora (`383`) |

## Relacionado

`380` qué es pisar en números · `381` el área que importa · `383` umbrales por tipo de contenido ·
`386` el elemento enterrado · `377` §3 cuánto puede taparse una palabra · `45` zona segura por plataforma ·
`204` §4 la zona segura por capa · `canales_lushows/26` lo que nunca se tapa
