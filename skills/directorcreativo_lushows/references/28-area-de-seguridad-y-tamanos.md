# 28 — Área de seguridad y tamaños

Diseñar el logo es la mitad del trabajo; la otra mitad es **protegerlo en uso**. Un logo bien hecho se arruina si lo pegan a un borde, lo achican hasta volverlo barro o le cambian los colores. Estas son las reglas que van en el manual de marca para que cualquiera lo use bien.

## Área de seguridad (zona de exclusión / espacio de respeto)

**Área de seguridad** = el espacio vacío mínimo que debe rodear al logo, donde **nada** más puede entrar (ni texto, ni otro logo, ni el borde de la imagen, ni una foto).

¿Por qué? El logo necesita "aire" para respirar y ser legible. Apretado contra otras cosas, pierde fuerza y se ve amateur.

**Cómo definirla (método estándar):** usa una **medida del propio logo** como unidad, para que el área escale con él. Lo común:
- Tomar la altura de una letra clave (ej. la "X" de FedEx, la "O" del nombre) y usar **1× esa medida** como margen mínimo por los 4 lados.
- O usar el ancho/alto del isotipo como unidad.

```
┌─────────────────────────────┐
│        ← x →                │   x = altura de la inicial
│   ┌───────────────────┐     │
│ x │   [ LOGO AQUÍ ]   │ x   │   nada puede entrar
│   └───────────────────┘     │   en la franja "x"
│        ← x →                │
└─────────────────────────────┘
```

Defínela con una medida relativa, **nunca** en centímetros fijos (un logo se usa a muchos tamaños).

## Tamaño mínimo

**Tamaño mínimo** = el tamaño más pequeño al que el logo aún se lee bien. Por debajo de eso, no se debe usar.

Se especifica para dos medios:
- **Digital:** en píxeles de ancho (ej. "logo principal mínimo 120px de ancho; isotipo mínimo 24px").
- **Impreso:** en milímetros (ej. "mínimo 20mm de ancho").

Cómo encontrarlo: achica el logo hasta que un detalle empiece a perderse o el texto deje de leerse; el tamaño justo antes de ese punto es tu mínimo. **Aquí entra la versión responsive (ver 27):** por debajo del mínimo del logo completo, se usa el isotipo simplificado, que tiene su propio mínimo más pequeño.

## Fondos permitidos

Define sobre qué fondos puede ir el logo y con qué versión:

| Fondo | Versión a usar |
|---|---|
| Blanco / muy claro | Principal a color o monocromo positivo |
| Color de marca claro | Principal, verificando contraste |
| Color de marca oscuro | Versión negativa (blanca) |
| Negro / muy oscuro | Negativa (blanca) |
| Foto | Negativa sobre zona oscura, o caja de protección |

**Regla de contraste:** el logo siempre debe destacar del fondo. Si no hay contraste suficiente, usa la otra versión o una caja de fondo sólido detrás (ver 30 sobre contraste y accesibilidad).

## Usos incorrectos — la lista de "NO hacer"

Esta lista va en el manual con ejemplos tachados en rojo. Prohíbe explícitamente:

- [ ] **No deformar** (estirar/aplastar — cambiar la proporción).
- [ ] **No rotar** (a menos que esté permitido por diseño).
- [ ] **No cambiar los colores** fuera de la paleta oficial.
- [ ] **No agregar efectos** (sombras, brillos, contornos, 3D, degradados no oficiales).
- [ ] **No reorganizar** los elementos (mover el símbolo, cambiar el tipo de letra del nombre).
- [ ] **No usar sobre fondos sin contraste** (logo que se pierde).
- [ ] **No poner sobre fondos recargados** sin caja de protección.
- [ ] **No invadir el área de seguridad** con texto u otros elementos.
- [ ] **No usar por debajo del tamaño mínimo.**
- [ ] **No recolorear el isotipo** ni mezclar versiones (símbolo de color con texto de otro).
- [ ] **No rehacer/redibujar** el logo "a mano" o pedirle a otro que lo "mejore".

> Estas reglas no son capricho de diseñador: protegen la **consistencia**, que es lo que construye reconocimiento. Un logo usado de 10 formas distintas no se recuerda como ninguna.

## Ejemplo trabajado: especificación de BIO-SETA
- **Área de seguridad:** margen = altura del isotipo (hongo) ÷ 2, por los 4 lados. Nada entra ahí.
- **Tamaño mínimo:** principal 110px / 22mm de ancho; isotipo solo 24px / 8mm.
- **Fondos:** verde claro → versión a color; verde oscuro y fotos del producto → versión blanca (negativa).
- **NO:** no recolorear el hongo a otros verdes, no estirar el nombre, no poner sobre fotos sin caja.

## Mini-manual de página (lo mínimo entregable)
1. Logo principal + área de seguridad ilustrada con la unidad "x".
2. Tamaños mínimos (px y mm).
3. Versiones y sobre qué fondo va cada una.
4. Grilla de "usos incorrectos" tachados en rojo.
5. Colores con códigos (remite a 30/31).

## Siguiente paso
Documenta área de seguridad, tamaño mínimo, fondos y la grilla de "no hacer" en una página del manual. Con esto el logo queda protegido. Si más adelante la marca cambia, revisa 29 (rediseño) antes de tocar el logo.
