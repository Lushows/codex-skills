# 373 — Jerarquía dentro de la frase: quién crece, quién se pinta, quién se sacude

Cuando hay más de una palabra en pantalla, alguien manda. Si no decides quién, decide el azar —y el azar
siempre elige mal. Este módulo es el reparto de énfasis: **las tres palancas, en qué orden se usan, y
cuántas se pueden usar a la vez.**

---

## 1. Las tres palancas (y su costo)

| Palanca | Qué comunica | Costo visual | Cuántas veces por video |
|---|---|---|---|
| **Escala** (crecer) | Importancia, volumen, magnitud | Bajo | Todas las que quieras |
| **Color** (pintar distinto) | Categoría, alerta, marca | Medio | 2-4 |
| **Movimiento** (sacudir, pulsar) | Urgencia, impacto, emoción | **Alto** | 1-2 |

La regla de oro: **usa la palanca más barata que resuelva el problema.** El 80% de los énfasis se
resuelven con escala. El color se reserva para lo que tiene *significado* distinto, no solo importancia
distinta. El movimiento es el último recurso y el que más rápido se ve barato (`56`).

> **Nunca las tres a la vez sobre la misma palabra.** Una palabra grande, roja y temblando no dice
> "importante": dice "amateur". Dos palancas máximo, y la segunda solo si la primera no bastó.

---

## 2. Palanca 1 — Escala: la que siempre se usa

Dentro de un grupo de palabras, la portadora del sentido va **más grande**. En la gramática medida esto
es literal: se sube la escala de esa palabra y se dejan las demás en su tamaño calculado.

Cuánto más grande:

| Diferencia | Efecto |
|---|---|
| +10% | No se nota. Se lee como error de alineación. |
| **+25 a +40%** | **Jerarquía clara y elegante. El rango correcto.** |
| +60% | Fuerte. Sirve para una sola palabra en todo el video. |
| +100% o más | La palabra grande y las otras se ven como pie de foto |

Cuidado: la escala se aplica **sobre la escala ya calculada por longitud** (`378`), no sobre 1.0.

```js
const base    = Math.max(0.85, Math.min(2.6, (2.6 * 5) / Math.max(palabra.length, 5)));
const escala  = esPortadora ? base * 1.3 : base;   // +30%
```

Si aplicas el +30% antes del cálculo por longitud, una palabra larga y portadora te revienta el ancho.
**Primero longitud, después énfasis.**

### La jerarquía invertida (truco poco usado)
En vez de agrandar la portadora, **encoge las demás** al 75%. Ocupa menos pantalla, se ve más elegante y
funciona igual de bien. Úsalo cuando la portadora ya es larga y no puede crecer más.

---

## 3. Palanca 2 — Color: solo para significado

El error universal es usar el color para decir "esto es importante". El color debe decir **qué clase de
cosa es**. Un sistema de tres colores, sostenido en todo el video:

```
BLANCO   → información normal (el 85% del texto)
MARCA    → lo que es tuyo: producto, precio, nombre, beneficio
ALERTA   → el dolor, lo que se pierde, lo que está mal
```

Con eso, el espectador aprende el código en 5 segundos y después el color trabaja solo:

> `ESTÁS PERDIENDO` (alerta) / `PLATA` (alerta) — corte — `LA TABLA` (marca) / `TE LA MUESTRA` (blanco)

El significado se transmite antes de leer. Eso es diseño funcionando.

### Cómo se aplica el color sin romper la legibilidad
Dos formas, y una es mejor:

- **Relleno de color, contorno oscuro** — el color va en la letra. Se ve fuerte pero pierde contraste
  contra fondos claros.
- **Relleno blanco, contorno de color** — la letra sigue siendo blanca (máximo contraste, siempre legible)
  y el color vive en el borde. **Esta es la buena** para pantalla pequeña. Es además la que sostiene tu
  estilo base de "contorno sí, sombra no": el contorno ya está ahí, solo cambia de color.

Máximo **3 colores** en toda la pieza, contando el blanco.

---

## 4. Palanca 3 — Movimiento: caro y peligroso

Mover una palabra para enfatizarla es lo que más rápido delata a un editor. Casi todo lo que ofrece
CapCut en "animación de bucle" se ve barato en 2026: parpadeo, ondas, rebote elástico, giros.

Lo que sí sobrevive, en orden de seguridad:

1. **Pulso de escala único.** La palabra entra al 108% y en 0,12 s baja al 100%. Casi imperceptible,
   fortísimo en efecto. Es el énfasis por movimiento más usado por editores buenos.
2. **Sacudida de 2 fotogramas.** Desplazamiento de ±8 px en X e Y durante 0,08 s, sincronizado con un
   golpe grave. Sirve para una palabra de impacto (`ROBO`, `NUNCA`, `PARA`). **Una vez por video.**
3. **Empuje vertical mínimo.** La palabra entra 20 px más abajo y sube a su sitio en 0,15 s. Sutil,
   funciona con la Aparición progresiva.

Lo que **no**:
- Temblor continuo mientras la palabra está en pantalla. Cansa en 1 segundo.
- Rebote elástico con sobrepaso grande. Es la firma visual de plantilla gratuita.
- Rotación. Nunca, salvo que la marca lo pida.
- Cualquier cosa que siga moviéndose después de 0,3 s.

> **La regla de los 0,3 s:** todo movimiento de énfasis debe estar terminado a los 0,3 s de entrar la
> palabra. Después de eso la palabra está quieta y se deja leer.

---

## 5. La regla del uno

En cualquier instante de la pantalla, **hay exactamente un protagonista**.

Si hay 4 palabras en cascada, una es más grande. Si hay 2, una manda. Si todas son iguales, ninguna
manda y el bloque se lee como decoración.

Cómo se verifica en 3 segundos: **entrecierra los ojos** mirando el cuadro. Lo que sigue siendo legible
cuando todo lo demás se hizo borroso es tu protagonista. Si sobreviven dos cosas igual de fuerte,
todavía no hay jerarquía.

Esta prueba también revela el error contrario: si al entrecerrar sobrevive el logo o la marca de agua y
no la palabra, tu marca de agua está compitiendo con tu mensaje (`87`).

---

## 6. Jerarquía en el tiempo, no solo en el espacio

Aparte de tamaño y color, tienes una cuarta palanca gratis que casi nadie usa: **el orden de entrada**.

- Lo que entra **primero** se lee como premisa.
- Lo que entra **último** se lee como conclusión.
- Lo que entra **después de una pausa** se lee como lo importante.

Por eso el hueco antes del remate en la cascada (`372`) es una herramienta de jerarquía, no de ritmo. Un
espacio de 0,35 s antes de una palabra la vuelve importante sin cambiarle ni el tamaño ni el color.

Combinación más fuerte que existe, y no cuesta nada:

```
palabra   →  palabra   →  palabra   →  [ 0,35 s de silencio ]  →  PALABRA GRANDE
```

---

## 7. Los cuatro casos concretos

**Caso A — Precio.** `SOLO` pequeño, `$10.000` grande y en color de marca, `PAGO ÚNICO` pequeño debajo.
Dos niveles, un color. Ver `379`.

**Caso B — Dolor.** `ESTÁS` normal, `PERDIENDO` +35% y en alerta, `PLATA` normal. La emoción está en el
verbo, no en el sustantivo: es el verbo el que crece.

**Caso C — Negación.** `NO` gigante, `NECESITAS CONTADOR` pequeño al lado. La negación es la palabra más
poderosa del español comercial y aguanta escala extrema porque son 2 letras (`378` explica por qué eso
importa).

**Caso D — Comparación.** `ANTES` y `AHORA` del mismo tamaño, colores distintos, entrando en momentos
distintos. Aquí **no hay protagonista**: el protagonista es la relación. Es la única excepción a la
regla del uno, y solo dura mientras se sostiene la comparación.

---

## 8. Cómo se guarda esto en CapCut

Los tres énfasis viven en sitios distintos del `draft_content.json`:

- **Escala:** en el `segment`, dentro de `clip.scale.x` / `clip.scale.y`. Mantenlos iguales: escalar solo
  en X deforma la letra y se nota inmediatamente.
- **Color y contorno:** dentro del material de texto, en la cadena de estilo enriquecido (relleno,
  color del borde, grosor del borde). La forma segura de acertar: crea a mano **una** palabra con el
  color correcto, ábrelo y **copia esa estructura** en las demás. Los nombres exactos de campo cambian
  entre versiones de CapCut y no vale la pena adivinarlos.
- **Movimiento:** o bien como animación de bucle (referenciada desde el material de animaciones), o bien
  con `keyframe_refs` sobre la escala/posición. Para el pulso de escala, dos keyframes bastan.

Regla de oro con el JSON: **nunca inventes un `resource_id`.** Haz el efecto una vez en la app, encuentra
su id en el JSON, y reúsalo. Es la diferencia entre un generador que funciona y uno que abre proyectos
corruptos (`119`).

---

## Errores comunes

1. **Ninguna palabra manda.** Todas del mismo tamaño y color: el bloque se lee como decoración.
2. **Dos protagonistas simultáneos.** Se pelean y el ojo no elige ninguno.
3. **Las tres palancas sobre la misma palabra** (grande + color + temblor). Grita amateur.
4. **Diferencia de escala menor al 20%.** No se lee como jerarquía, se lee como desalineación.
5. **Aplicar el énfasis antes del cálculo por longitud**, y reventar el ancho con una palabra larga.
6. **Escalar solo en X o solo en Y.** Deforma la tipografía; en pantalla pequeña se ve inmediatamente.
7. **Usar el color para decir "importante"** en vez de para decir "de esta clase".
8. **Más de 3 colores** en una pieza. El código deja de ser código y se vuelve ruido.
9. **Relleno de color sobre fondo claro.** Pierde contraste; mejor relleno blanco y contorno de color.
10. **Movimiento que sigue después de 0,3 s.** Cansa y distrae de la lectura.
11. **Rebote elástico con sobrepaso.** La firma visual de plantilla gratis.
12. **Olvidar el orden de entrada como palanca.** Una pausa de 0,35 s enfatiza gratis y no ensucia nada.
13. **No hacer la prueba de entrecerrar los ojos.** Toma 3 segundos y detecta la falta de jerarquía al
    instante.

---

## Checklist

- [ ] En cada instante hay exactamente un protagonista (salvo comparación)
- [ ] La palabra portadora está entre +25% y +40% sobre las demás
- [ ] El énfasis se aplicó DESPUÉS del cálculo de escala por longitud
- [ ] La escala se movió en X e Y por igual
- [ ] El color codifica clase (normal / marca / alerta), no importancia
- [ ] Máximo 3 colores en toda la pieza
- [ ] El color va preferentemente en el contorno, con relleno blanco
- [ ] Ninguna palabra tiene más de dos palancas de énfasis
- [ ] Todo movimiento de énfasis termina antes de 0,3 s
- [ ] Hay como máximo 1-2 momentos de movimiento en todo el video
- [ ] Usé al menos una pausa como herramienta de jerarquía
- [ ] Entrecerré los ojos frente al cuadro y sobrevivió la palabra correcta
