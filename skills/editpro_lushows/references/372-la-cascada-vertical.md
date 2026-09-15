# 372 — La cascada vertical: palabras que se acumulan

La firma de ritmo de tu gramática. En los proyectos medidos aparecen hasta **6 palabras acumuladas en
columna**, entrando una cada **0,15 a 0,30 s**, cada una con su golpe de sonido. Este módulo es cómo se
arma bien, cuánto dura, y —lo que casi nadie resuelve— **cuándo se limpia la pantalla**.

---

## 1. Qué es y por qué funciona

La cascada es una lista que se construye delante del espectador. Palabra 1 entra y **se queda**. Palabra
2 entra debajo y las dos se quedan. Y así hasta 4-6.

Funciona por tres razones distintas, y conviene saberlas porque cada una se puede romper:

1. **Acumulación = argumento.** Ver tres cosas *al mismo tiempo* no es lo mismo que verlas una tras otra.
   La cascada convierte una enumeración en un peso: "mira todo esto junto".
2. **Movimiento sin mover nada.** Cada entrada es un evento visual. Seis eventos en 1,5 s dan sensación
   de energía en un plano completamente estático. Es la forma más barata de que un plano fijo no aburra.
3. **Relectura gratis.** Cuando entra la palabra 4, el ojo vuelve a barrer 1-2-3. El espectador lee tu
   mensaje tres o cuatro veces sin que le cueste.

La contraparte: **la cascada no sirve para narrar**, sirve para **listar**. Si tu contenido no es una
lista de cosas comparables, la cascada lo hace ver desordenado.

---

## 2. Cuándo se usa

**Sí:**
- Enumeración de beneficios: `SIN EXCEL` / `SIN CONTADOR` / `SIN FÓRMULAS`
- Enumeración de dolores: `COMPRAS` / `NÓMINA` / `SERVICIOS` / `Y AL FINAL NADA`
- Lo que incluye algo: `LA TABLA` / `+ 3 CURSOS` / `+ PLANTILLAS`
- Acumulación de números que suman a un total (ver `379`)
- El remate de un gancho: tres golpes cortos antes del corte

**No:**
- Una idea sola. Una idea sola es una palabra sola, centrada y grande.
- Frases que dependen entre sí gramaticalmente ("cuando" / "tú" / "sabes"). Eso es un subtítulo
  desarmado, no una cascada.
- Encima de una cara. La cascada come alto y va a chocar contra el rostro (salvo sándwich, ver `377`).

---

## 3. La geometría

Sobre 1080x1920:

```
        y=520   ┌──────────────────────┐   ← la primera palabra empieza ALTA
                │  SIN EXCEL           │
        y=690   │  SIN CONTADOR        │
        y=860   │  SIN FÓRMULAS        │
        y=1030  │  SIN DOLOR DE CABEZA │
                └──────────────────────┘
        y=1480  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ← límite inferior seguro (ver 376)
```

- **Interlínea:** 1,25 a 1,4 veces la altura de la palabra. Menos y se pegan; más y se deshace la
  columna en palabras sueltas sin relación.
- **Alineación:** a la **izquierda**, con el margen izquierdo en x≈140. La alineación centrada convierte
  la columna en un rombo y se pierde el borde que guía al ojo hacia abajo. Centrar solo si son exactamente
  2 palabras o si todas miden casi lo mismo.
- **Punto de arranque:** calcula hacia arriba desde el final. Si van 5 palabras con paso de 170 px, la
  última cae en y=arranque+680. Con el límite inferior en 1480, el arranque no puede pasar de y=800.
  **Empieza siempre más arriba de lo que crees que necesitas.**

### Fórmula del arranque

```
paso        = altura_texto * 1.3
alto_total  = paso * (n_palabras - 1)
y_arranque  = y_centro_bloque - alto_total / 2     // y_centro_bloque ≈ 900
```

Con 6 palabras, texto de 130 px, paso 170: alto_total = 850. Arranque en 900-425 = **475**. La última cae
en 1325. Cabe, pero apretado: por eso 6 es el máximo real, no un capricho.

---

## 4. El tiempo: el corazón del asunto

El intervalo entre entradas define el carácter:

| Intervalo | Sensación | Cuándo |
|---|---|---|
| 0,10-0,14 s | Ráfaga, casi simultáneo | Gancho de arranque, 3 palabras cortas |
| **0,15-0,20 s** | **Rápido y contundente** | El más usado. Beneficios, dolores |
| 0,22-0,30 s | Medido, cada palabra pesa | Cifras, promesas, cosas que quieres que se lean |
| 0,35-0,50 s | Solemne, lento | Rara vez; solo con 2-3 palabras y música lenta |
| 0,60+ s | Ya no es cascada | Son palabras sueltas consecutivas |

**Detalle que separa lo bueno de lo mediocre:** el intervalo no tiene que ser constante. La última
palabra de la cascada —la que remata— entra con **el doble de espera**:

```
SIN EXCEL        0,00
SIN CONTADOR     0,18   (+0,18)
SIN FÓRMULAS     0,36   (+0,18)
                          ← silencio
Y SIN PERDER PLATA 0,72  (+0,36)  ← el remate respira
```

Ese hueco antes del remate es lo que hace que el remate se sienta como remate. Sin él, la cascada es una
lista; con él, es un argumento con conclusión.

---

## 5. Cuánto se queda en pantalla y cómo se limpia

La pregunta que nadie responde. Tres reglas:

### Regla 1 — la cascada completa vive de 1,2 a 2,5 s
Contado **desde que entra la última palabra**. Menos de 1,2 s y no alcanzas a leer la columna completa;
más de 2,5 s y el plano se congela.

Cuenta rápida: `duración total = (n-1) × intervalo + 1,5 s`. Con 5 palabras a 0,20 s: 0,8 + 1,5 = **2,3 s**.

### Regla 2 — la cascada sale ENTERA, nunca palabra por palabra
Sacarlas en el mismo orden en que entraron es el error número uno: dura el doble y se siente como si el
video estuviera rebobinando. **Todas salen al mismo tiempo**, con Flash desactivado, en el mismo
fotograma. Idealmente **en el corte**: el plano cambia y el texto ya no está.

### Regla 3 — la pantalla se limpia SIEMPRE antes de la siguiente cascada
Nunca encadenes cascada con cascada. Entre una y otra van mínimo **0,4 s de pantalla limpia**. Ese vacío
es lo que hace que la siguiente cascada vuelva a sentirse como un evento. Sin vacío, el espectador ve un
muro de texto continuo de 12 segundos.

**Un video de 20 s aguanta 2 cascadas. Tres ya es demasiado.**

---

## 6. La tabla de tiempos, lista para copiar

Cascada de 5 palabras, intervalo 0,18 s, remate a 0,36 s, arrancando en t=6,00 s:

| # | Palabra | Entra | Sale | Escala (`378`) | Sonido |
|---|---|---|---|---|---|
| 1 | `COMPRAS` | 6,00 | 9,10 | 1.86 | golpe A |
| 2 | `NÓMINA` | 6,18 | 9,10 | 2.17 | golpe A |
| 3 | `SERVICIOS` | 6,36 | 9,10 | 1.44 | golpe A |
| 4 | `ARRIENDO` | 6,54 | 9,10 | 1.63 | golpe A |
| 5 | `Y AL FINAL NADA` | 6,90 | 9,10 | 0.87 | golpe B (más grave) |

Fíjate en tres cosas: todas **salen en 9,10** (regla 2); el remate espera 0,36 (regla del hueco); y el
remate lleva **otro** sonido, más grave, porque es una idea distinta.

---

## 7. En CapCut, sin morir en el intento

Cada palabra es su propio cuadro de texto en su propia pista. Con 6 palabras son 6 pistas de texto.
CapCut lo aguanta.

Truco de armado que ahorra la mitad del tiempo:

1. Haz **solo la primera palabra** completa: tamaño 15, contorno, sin sombra, Aparición progresiva,
   Flash desactivado, posición y=475.
2. Copia y pega ese segmento 5 veces.
3. A cada copia: cambia el texto, baja la posición 170 px, corre el inicio 0,18 s.
4. Selecciona los 6 finales y **arrástralos al mismo punto**. (Este paso es el que la gente olvida.)
5. Ajusta la escala de cada una según su longitud.

Si generas por código (`112`, `114`), la cascada es un `for`:

```js
const palabras = ["COMPRAS","NÓMINA","SERVICIOS","ARRIENDO","Y AL FINAL NADA"];
const t0 = 6.0, paso = 0.18, fin = 9.10, y0 = 475, dy = 170;
const us = s => Math.round(s * 1_000_000);

palabras.forEach((p, i) => {
  const esRemate = i === palabras.length - 1;
  const inicio = t0 + paso * i + (esRemate ? paso : 0);   // el remate respira
  crearSegmentoTexto({
    texto: p,
    start: us(inicio),
    duration: us(fin - inicio),          // TODAS terminan en 'fin'
    y: y0 + dy * i,
    escala: Math.max(0.85, Math.min(2.6, (2.6 * 5) / Math.max(p.length, 5))),
  });
});
```

Recuerda: `target_timerange.start` y `.duration` van en **microsegundos**, y `duration` no es el fin, es
la duración. Restar mal ahí es el bug clásico que deja palabras colgadas 8 segundos.

---

## 8. Variantes que valen la pena

- **Cascada tachada.** Las 3 primeras entran normales; al entrar la cuarta, las 3 se tachan de rojo.
  `SIN EXCEL` `SIN CONTADOR` `SIN FÓRMULAS` → todas tachadas → `SOLO ESTO`. Es un giro visual de 0,3 s
  que se recuerda.
- **Cascada que se acumula sobre un número.** Cada línea suma y abajo del todo un total que crece.
  Ver `379`.
- **Cascada horizontal.** Palabras que entran de izquierda a derecha en una sola línea. Solo funciona con
  2-3 palabras muy cortas; con más te quedas sin ancho.
- **Cascada detrás del sujeto.** La cascada con sándwich (`377`) es lo más caro que se ve por lo poco que
  cuesta hacerlo. Requiere que la persona esté a un lado del cuadro y la columna al otro.

---

## Errores comunes

1. **Sacar las palabras una por una.** Duplica el tiempo y se siente como rebobinado. Salen todas juntas.
2. **Arrancar demasiado abajo** y que la última palabra caiga en la zona de la interfaz.
3. **Más de 6 palabras.** A la séptima ya no se lee la columna, se ve un bloque gris.
4. **Intervalo constante hasta el final.** Sin el hueco antes del remate, la cascada no concluye.
5. **Encadenar dos cascadas sin limpiar la pantalla.** Mínimo 0,4 s de vacío entre ellas.
6. **Escala igual para todas** siendo de longitudes distintas: la columna queda con bordes desiguales
   (ver `378`).
7. **Centrar la columna.** Alineada a la izquierda el ojo baja por el borde; centrada se desarma.
8. **Interlínea menor a 1,2×**: las palabras se tocan y el contorno de una invade a la otra.
9. **Cascada sobre una cara** sin sándwich: choca con el rostro y las dos cosas pierden.
10. **Usar cascada para una frase gramatical** ("cuando" / "tú" / "compras"). Eso es un subtítulo partido.
11. **Un solo golpe de sonido para toda la cascada.** Cada palabra lleva el suyo (~0,27 s); si no, el
    movimiento se siente mudo.
12. **Mismo sonido para el remate.** El remate cambia de timbre, o no se lee como remate.
13. **Dejar la cascada más de 2,5 s** después de la última entrada: el plano se congela y la retención cae.

---

## Checklist

- [ ] Máximo 6 palabras, y son una lista real (elementos comparables)
- [ ] Alineadas a la izquierda, interlínea entre 1,25 y 1,4×
- [ ] La última palabra cae por encima de y=1480
- [ ] Intervalo entre entradas dentro de 0,15-0,30 s
- [ ] El remate entra con el doble de espera
- [ ] Todas las palabras terminan en el mismo fotograma
- [ ] La salida es una sola, con Flash desactivado, idealmente sobre el corte
- [ ] La cascada completa dura entre 1,2 y 2,5 s desde la última entrada
- [ ] Hay al menos 0,4 s de pantalla limpia antes de cualquier otra cascada
- [ ] Máximo 2 cascadas en un video de 20 s
- [ ] Cada palabra tiene su golpe de sonido; el remate tiene uno distinto
- [ ] Escala calculada por longitud, palabra por palabra
