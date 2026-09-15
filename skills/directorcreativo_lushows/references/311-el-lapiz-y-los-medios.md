# 311 · El lápiz y los medios

> Cada herramienta deja una marca que **no puede imitar** a las otras. Dirigir un dibujo sin
> saber con qué está hecho es como dirigir una foto sin saber el lente. Este módulo es el
> catálogo físico de la marca.

---

## 1 · Grafito

La escala **9H → HB → 9B**: la H es dureza (línea fina, gris claro, no se corre), la B es
blandura (línea gruesa, negro profundo, se corre).

| Dureza | Qué hace | Para qué |
|---|---|---|
| **4H–2H** | Gris pálido, surco en el papel | Construcción que va a quedar debajo |
| **HB–B** | El punto medio | Dibujo general |
| **2B–4B** | Negro con cuerpo, se difumina | Sombreado, valor |
| **6B–9B** | Casi carbón, brillo grafito | Negros máximos |

**Sus tres marcas propias:**
- **Brillo metálico** en las zonas más oscuras — el grafito nunca da negro mate
- **El surco**: la H hunde el papel y deja una marca que ya no se puede tapar
- **Se corre con el canto de la mano** — de ahí las manchas grises de un dibujo real

> El grafito **no llega al negro**. Si el dibujo necesita negro absoluto, es tinta o carbón.

---

## 2 · Carboncillo

- Negro profundo y mate, **cero brillo**
- Se borra con trapo, se levanta con miga de pan o goma moldeable
- **El borrador es una herramienta de dibujo**, no de corrección: se dibuja quitando
- Polvo: se contamina todo, se difumina solo
- **Para qué:** valor grande, atmósfera, retrato, gesto rápido a tamaño grande

---

## 3 · Pluma y tinta

- **Línea sin gradación:** o hay tinta o no hay. El valor solo se construye por densidad
- **No se borra.** Cada trazo es definitivo — de ahí la seguridad que se lee en un dibujo a pluma
- **Puntas:**
  - *Técnica (Rapidograph)* — ancho constante, frío, ideal para esquema y puntillismo
  - *Flexible (plumilla)* — el ancho responde a la presión: es la que da el trazo modulado
  - *Bolígrafo* — tono uniforme, se acumula por capas, permite el garabato largo
  - *Pincel* — máxima variación de ancho, del pelo al brochazo

> **La referencia gestual de BIO-SETA es bolígrafo:** ancho casi constante, valor por
> acumulación, trazos largos que no se levantan.

---

## 4 · Aguada y tinta diluida

- Manchas de valor con **borde duro al secar** (el famoso cerco)
- Se trabaja de claro a oscuro, por capas
- El blanco es el papel: **no hay blanco de vuelta**
- Se combina con línea: la línea define, la aguada llena

---

## 5 · Sanguina, sepia y conté

- Barras de pigmento comprimido: **tierra rojiza, sepia, negro, blanco**
- La marca es ancha y granulosa; el canto da línea, la cara da masa
- **Sobre papel tonal** (gris, crema, azul) con blanco para las luces — la técnica de los
  maestros del Renacimiento: solo se dibujan las sombras y las luces, el medio tono es el papel
- **Para qué:** cualquier dibujo que deba verse clásico y cálido

---

## 6 · El papel: el otro 50 %

| Papel | Grano | Qué hace |
|---|---|---|
| **Satinado / hot-press** | Liso | La línea corre libre. Ideal para pluma y detalle fino |
| **Grano fino / cold-press** | Medio | El estándar. Muerde lo justo |
| **Grano grueso / torchon** | Fuerte | El grafito solo toca las crestas → textura granulada |
| **Papel tonal** | Coloreado | Permite dibujar hacia la luz Y hacia la sombra |

> **El grano decide la textura mucho más que la mano.** Un 6B sobre torchon da granulado
> aunque el trazo sea suave; sobre satinado da negro plano aunque el trazo sea igual.

---

## 7 · Cómo se reconoce cada medio en una imagen

| Si ves… | Es… |
|---|---|
| Brillo plateado en los negros | Grafito |
| Negro mate absoluto y polvo | Carboncillo |
| Solo línea, sin gradación, negro pleno | Pluma y tinta |
| Manchas con cerco duro al borde | Aguada |
| Rojizo cálido sobre papel de color, con blanco | Sanguina / conté |
| Textura granulada uniforme | El papel, no el medio |

---

## 8 · Traducirlo a generativo

| Medio | Cómo se simula |
|---|---|
| **Grafito** | Trazo gris translúcido acumulable + textura de grano en la capa |
| **Carboncillo** | Manchas de borde blando, valor por opacidad, negro mate |
| **Pluma técnica** | Ancho constante, opacidad alta, valor solo por densidad |
| **Plumilla flexible** | **Trazo ahusado** (polígono, no `stroke`) |
| **Bolígrafo** | Ancho casi constante, opacidad media-baja, trazos largos, se acumulan |
| **Aguada** | Formas con borde ligeramente más oscuro que el interior |

Ver [[301-ilustracion-generativa-por-codigo]] y [[303-grabado-y-tecnicas-de-la-lamina]].
