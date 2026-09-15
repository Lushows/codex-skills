# 310 · El trazo vivo: gesto, ritmo y acento

> Por qué un dibujo hecho a mano se siente **vivo** y uno hecho por máquina se siente muerto,
> aunque los dos describan la misma forma con la misma precisión. La respuesta no está en la
> forma: está en el trazo.

---

## 1 · La línea de acción

Antes de dibujar nada, el dibujante traza **una sola línea** que captura hacia dónde va el
sujeto: la curva que recorre todo el gesto de punta a punta.

- No describe contorno. No describe volumen. Describe **intención**.
- Todo lo demás se cuelga de ella.
- Si la línea de acción es tímida, el dibujo entero es tímido — por muy correcto que sea.

> En un hongo, la línea de acción es la curva del tallo desde donde nace hasta la punta.
> Si todos los tallos tienen la misma curva, el grupo está muerto.

---

## 2 · Ritmo: la línea que atraviesa las formas

Bridgman: **las formas no se dibujan una por una, se encadenan.**

Un trazo que empieza en un objeto y **continúa** dentro del siguiente crea unidad. Un dibujo
donde cada parte tiene su propio contorno cerrado se ve como collage de piezas.

| Sin ritmo | Con ritmo |
|---|---|
| Cada forma se contornea aparte | El trazo cruza de una forma a la siguiente |
| Bordes cerrados en todas partes | Bordes que se pierden y reaparecen |
| Se lee como recorte | Se lee como cuerpo |

---

## 3 · El acento: dónde engorda la línea

**Este es el detalle que más rinde y el que casi nadie programa.** La línea no engorda al azar:
engorda en cuatro sitios concretos.

| El acento va… | Por qué |
|---|---|
| **Donde una forma pasa por delante de otra** | El solape es la información espacial más valiosa del dibujo |
| **En los rincones y quiebres** | Donde la dirección cambia bruscamente |
| **Donde la forma se apoya o carga peso** | La base, el punto de contacto |
| **En el núcleo de sombra** | Ver `300 §2` |

> **La regla del solape:** cuando dos cuerpos se cruzan, la línea del que está delante se
> **engrosa y oscurece** justo en el cruce, y la del de atrás se interrumpe. Sin eso, dos
> formas superpuestas se leen como una sola silueta plana. Con eso, hay profundidad.

---

## 4 · El pentimento: las líneas que no se borraron

Un dibujo real conserva su **andamiaje**: los ejes, los arcos de búsqueda, los contornos que
se corrigieron y quedaron ahí, más flojos.

Eso no es suciedad. **Es la prueba visible de que hubo una mano decidiendo.**

- Un dibujo sin construcción visible se lee como calco.
- Un dibujo con dos o tres líneas "equivocadas" tenues se lee como dibujo.
- La corrección va **más clara** que el trazo definitivo, nunca más oscura.

> En generativo: una capa de arcos y ejes largos al 8–15 % de opacidad, colocados **antes**
> del dibujo bueno y ligeramente desplazados respecto a él.

---

## 5 · Presión y velocidad

Una mano real no mantiene la presión constante:

- **Entrada suave** — el trazo empieza fino porque la punta va bajando
- **Cuerpo pleno** — la presión máxima está en el tercio central
- **Salida en fuga** — el trazo se levanta y se afina, a veces se corta

Un trazo de ancho y opacidad constantes de punta a punta es la firma inconfundible de la máquina.

> En generativo: modular **opacidad y ancho a lo largo del trazo**, no solo entre trazos.
> El perfil `sin(πt)` con las puntas afiladas resuelve el 80 % del problema.

---

## 6 · La economía: el trazo que dice todo

Un dibujo bueno tiene zonas de **muchísimo** trabajo y zonas resueltas con **dos líneas**.
Esa desigualdad es la que produce jerarquía y la que hace que el ojo descanse.

- Si todo está igual de trabajado, el dibujo se lee como textura
- La zona resuelta con dos líneas es la que se ve más segura
- **Quitar es más difícil que agregar**, y se nota

---

## 7 · Los seis errores que matan un trazo

- ⛔ Ancho constante de punta a punta
- ⛔ Todos los trazos de la misma longitud
- ⛔ Contornos cerrados en todas las formas
- ⛔ Sin acento en los solapes → todo plano
- ⛔ Sin líneas de construcción → se ve calcado
- ⛔ Detalle uniforme en toda el área

---

## 8 · Lista de verificación

- [ ] ¿Hay una línea de acción clara?
- [ ] ¿Algún trazo cruza de una forma a otra?
- [ ] ¿La línea engorda en los solapes?
- [ ] ¿Quedó alguna línea de construcción visible?
- [ ] ¿La presión varía dentro de cada trazo?
- [ ] ¿Hay una zona resuelta con muy pocas líneas?

Ver [[311-el-lapiz-y-los-medios]] para cómo se comporta cada herramienta,
y [[301-ilustracion-generativa-por-codigo]] para programarlo.
