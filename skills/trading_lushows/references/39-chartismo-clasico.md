# 39 — Chartismo clásico (figuras) y su crítica honesta

El **chartismo** es la escuela de las figuras dibujadas por el precio: triángulos, banderas,
hombro-cabeza-hombro… Tiene un siglo de tradición y un problema serio de subjetividad. Aquí va
lo útil y lo honesto.

## Las figuras principales

| Figura | Cómo se ve | Lectura clásica |
|---|---|---|
| **Triángulo** | El precio se comprime entre dos líneas convergentes | Compresión → expansión; se opera la ruptura, no la dirección adivinada |
| **Bandera** | Rally fuerte (mástil) + pausa lateral/contraria corta (bandera) | Continuación: descanso a mitad del movimiento |
| **Hombro-cabeza-hombro (HCH)** | Tres máximos, el del medio más alto, sobre una "línea de cuello" | Reversión bajista si rompe el cuello |
| **Doble techo / doble piso** | Dos máximos (o mínimos) al mismo nivel | El nivel aguantó dos veces: reversión si rompe el valle intermedio |

Lo que estas figuras tienen de real por debajo del dibujo: **son compresión de volatilidad
(triángulo, bandera) o fallos de estructura (HCH, doble techo)**. El triángulo es la compresión
de `37`; el doble techo es un LH que no pudo hacer HH (`32`). La figura es el envoltorio;
la mecánica de fondo es lo que vale.

## La crítica honesta

- **Subjetividad**: dale el mismo gráfico a cinco chartistas y trazarán cinco figuras distintas.
  Una figura que solo existe según dónde apoyes la línea no es una señal, es un dibujo.
- **Sesgo de confirmación**: el ojo encuentra la figura que quiere encontrar. ¿Alcista? Verás
  banderas. ¿Bajista? Verás HCH. El gráfico es un test de Rorschach con velas.
- **Sesgo de supervivencia en los libros**: los manuales muestran los HCH que funcionaron.
  Nadie publica los cientos de "casi-HCH" que se anularon a mitad de camino.
- **Evidencia estadística**: los intentos serios de medir figuras (detección algorítmica sobre
  datos históricos) encuentran, en el mejor de los casos, ventajas marginales — y muy sensibles
  a cómo se define la figura. Nada parecido a la fiabilidad que promete la tradición.
- **Los targets medidos** ("proyecta la altura del mástil") son convención sin base sólida:
  útiles como referencia compartida, no como física del mercado.

## Uso prudente (si se usan)

- Definir la figura ANTES de la ruptura, con reglas escritas (cuántos toques, dónde anula).
- Exigir confirmación de volumen en la ruptura (`36`): la figura sin participación es decoración.
- Tratarlas como contexto que suma o resta a la confluencia (`45`), jamás como señal autónoma.

## Cómo aplica al AGENTE TRADING

- El bot NO detecta figuras y **no debería**: codificar "detectar HCH" es heredar toda la
  subjetividad en forma de parámetros arbitrarios (¿cuánta tolerancia entre hombros?) — terreno
  fértil para el overfitting de `47`.
- Lo que sí puede hacer Claude al leer las velas: describir la mecánica sin el nombre —
  "compresión de rango", "segundo rechazo del mismo nivel", "rebote que no alcanzó el máximo
  previo". Eso es objetivo, verificable y suficiente. El nombre de la figura no agrega nada.
