# 318 · La mano: velocidad, presión y apoyo

> La parte física del oficio. Dos personas con el mismo lápiz y el mismo modelo dejan marcas
> distintas por cómo mueven el brazo. Entender esto es lo que permite **simular una mano** en
> vez de simular un contorno.

---

## 1 · Los tres motores del trazo

| Motor | Alcance | Qué produce |
|---|---|---|
| **Dedos** | 2–5 cm | Detalle, textura, control máximo. Trazo corto y algo tembloroso |
| **Muñeca** | 5–15 cm | Arcos medianos. El trazo natural del bolígrafo |
| **Hombro** | 15 cm–todo el papel | Líneas largas, rectas y seguras. **La única manera de trazar una recta larga** |

> **La regla:** un dibujo hecho todo con los dedos se ve apretado y tembloroso. Uno hecho todo
> con el hombro se ve suelto pero impreciso. **Los buenos alternan** — hombro para el gesto y
> la construcción, dedos para el remate.

Esto explica algo importante: **una línea larga trazada con los dedos siempre tiembla.** Si el
dibujo tiene líneas largas perfectamente rectas y también textura fina, hubo cambio de motor.

---

## 2 · Velocidad

| Velocidad | Marca |
|---|---|
| **Rápida** | Trazo fino, con entrada y salida en fuga, ligeramente curvo. Se pasa del punto de llegada |
| **Media** | El trazo de trabajo. Ancho estable |
| **Lenta** | Trazo grueso y denso, con temblor visible. Se detiene exacto |

> El trazo rápido **siempre se curva un poco** hacia el lado del hombro que lo mueve. Un trazo
> rápido perfectamente recto es imposible a mano — y por eso delata a la máquina.

---

## 3 · Presión

Dentro de un mismo trazo, la presión hace una curva:

```
  presión
    │      ╭────────╮
    │    ╭─╯        ╰─╮
    │  ╭─╯            ╰──╮
    └──┴────────────────┴────  recorrido
      entrada   cuerpo   salida
```

- **Entrada suave:** la punta baja mientras ya se mueve → el trazo empieza fino
- **Cuerpo:** máximo en el tercio central
- **Salida en fuga:** se levanta antes de parar → el trazo se afina y a veces se corta

**Un trazo con ancho y opacidad constantes de punta a punta no existe en la naturaleza.**

---

## 4 · El apoyo

- **Mano apoyada** en el papel → control fino, pero el canto **mancha** el grafito. De ahí las
  manchas grises características de un dibujo real
- **Mano levantada** → trazo suelto, menos preciso, sin manchas
- **Papel girado** → el dibujante rota la hoja para trazar siempre en su ángulo cómodo (unos
  30–45° respecto al antebrazo). Por eso **las tramas de un mismo dibujo tienden a repetir dos
  o tres ángulos**, no todos los ángulos posibles

> **Ese último detalle es oro para generativo:** las direcciones de trama no son uniformes en
> 360°. Se agrupan alrededor de dos o tres ángulos preferidos, con dispersión.

---

## 5 · El temblor

La mano tiembla siempre, entre 8 y 12 Hz. En el trazo eso aparece como:

- Micro-ondulación en trazos **lentos**
- Nada en trazos **rápidos** (la velocidad la promedia)

Simular temblor uniforme en todos los trazos es un error: **solo los lentos tiemblan**.

---

## 6 · La repetición: el trazo buscado

Cuando el dibujante no está seguro, **no traza una línea: traza varias encima**, cada vez más
cerca de la correcta.

- 2 a 5 trazos casi paralelos, muy juntos
- El definitivo es el más oscuro, y suele ser el último
- Los otros quedan visibles y más claros

Esto es lo que se ve en la referencia de retrato gestual: **el contorno de la nariz no es una
línea, son seis**. Ver `310 §4`.

---

## 7 · Traducción a generativo — la tabla completa

| Fenómeno de la mano | Implementación |
|---|---|
| Tres motores | Tres rangos de longitud de trazo (corto/medio/largo), no uno solo |
| Presión en curva | Ancho y opacidad modulados **dentro** del trazo, con perfil `sin(πt)` |
| Salida en fuga | Los últimos 20 % del trazo se afinan a casi cero |
| Trazo rápido se curva | Deriva angular constante (no aleatoria) en los trazos largos |
| Ángulos preferidos | Muestrear la dirección de **2–3 ángulos base + dispersión**, no uniforme |
| Temblor solo en lentos | Ruido de posición ∝ (1 − velocidad) |
| Trazo buscado | Repetir el contorno 2–5 veces con desplazamiento pequeño y opacidad creciente |
| Mancha del apoyo | Una capa muy tenue de gris en las zonas donde apoyaría la mano |

---

## 8 · Lista de verificación

- [ ] ¿Hay al menos tres longitudes de trazo distintas?
- [ ] ¿El ancho varía DENTRO de cada trazo?
- [ ] ¿Las direcciones se agrupan en 2–3 ángulos o están repartidas al azar?
- [ ] ¿Hay contornos trazados varias veces?
- [ ] ¿Los trazos largos se curvan siempre hacia el mismo lado?
