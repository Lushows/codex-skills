# 322 — Acelerar y desacelerar: cómo se estrecha el ciclo hacia un remate

**Qué resuelve:** tu reel tiene los planos correctos, la mediana correcta y aun así el final no aterriza.
El problema casi nunca es el último plano: es que **los cinco anteriores duraban todos lo mismo**, así que
cuando llegó el remate no había ninguna señal de que estaba llegando.

Este módulo trata la única herramienta de arquitectura rítmica que se puede escribir como una fórmula: la
**rampa**. Acortar el ciclo progresivamente para llegar a algo, y alargarlo progresivamente para dejar
respirar. Es lo que convierte una lista de planos en una curva.

---

## 1. La idea en una frase

> **El espectador no oye duraciones. Oye la derivada.**

Nadie percibe "ese plano duró 1,6 segundos". Lo que sí percibe, y con muchísima precisión, es que **este
plano duró menos que el anterior**. La aceleración es información: le está diciendo que algo se aproxima.
La desaceleración le está diciendo que algo terminó y puede bajar la guardia.

Por eso una secuencia de seis planos de 1,6 s y una de seis planos que van de 2,6 a 0,8 s tienen casi la
misma duración total y producen dos videos completamente distintos. La primera es una lista. La segunda es
una frase con entonación.

---

## 2. La rampa se construye multiplicando, no restando

El error de instinto es hacer la rampa restando: 2,5 → 2,0 → 1,5 → 1,0 → 0,5. Se siente mal, y la razón es
que la percepción de duración es **relativa, no absoluta**: pasar de 2,5 a 2,0 es una reducción del 20%, y
pasar de 1,0 a 0,5 es del 50%. La rampa se acelera de golpe al final y se cae.

La rampa que funciona es **geométrica**: cada plano dura un porcentaje fijo del anterior.

```
d(n) = d(0) × r^n
```

Con **r entre 0,75 y 0,82** para una aceleración que se nota pero no se despeña. Tablas listas para usar:

| Paso | r = 0,78 (aceleración clara) | r = 0,86 (aceleración sutil) | r = 1,35 (desaceleración) |
|---|---|---|---|
| 0 | 2,60 s | 2,60 s | 0,90 s |
| 1 | 2,03 s | 2,24 s | 1,22 s |
| 2 | 1,58 s | 1,92 s | 1,64 s |
| 3 | 1,23 s | 1,66 s | 2,21 s |
| 4 | 0,96 s | 1,42 s | 2,99 s |
| 5 | **0,75 s** ← el disparador | 1,22 s | — |

Cómo elegir `r` cuando ya sabes dónde empiezas y dónde quieres llegar, en `n` pasos:

```
r = (d_final / d_inicial)^(1/n)
```

```bash
# Ejemplo: de 2,6 s a 0,8 s en 5 pasos
awk 'BEGIN{di=2.6; df=0.8; n=5; r=(df/di)^(1/n);
  printf "r = %.3f\n", r;
  for(i=0;i<=n;i++) printf "plano %d: %.2f s\n", i, di*r^i}'
```

Redondea siempre al fotograma. A 30 fps, un fotograma es 0,0333 s: `d_redondeada = round(d*30)/30`.

---

## 3. El suelo: hasta dónde se puede acelerar

La aceleración tiene un piso físico y es el de la **entrada del ciclo** (`320` §2): al ojo le cuesta entre
0,2 y 0,4 s reconocer un encuadre nuevo.

| Duración del plano | Qué se puede meter ahí |
|---|---|
| ≥ 1,0 s | Información nueva completa. Zona normal |
| 0,6 – 1,0 s | Una sola cosa, grande y centrada. Nada de leer texto largo |
| 0,4 – 0,6 s | **Solo si el espectador ya vio ese encuadre antes.** Es un recordatorio, no información |
| 0,2 – 0,4 s | Textura pura. Cuenta como energía, no como contenido |
| < 0,2 s | Un destello. No es un plano |

**La consecuencia de diseño más útil de todo el módulo:** la parte rápida de una rampa se construye con
**material repetido o ya conocido**, no con información nueva. Por eso las ráfagas funcionan con planos de
producto que ya se vieron, con la misma cara desde tres ángulos, con el punch-in de un plano que ya
estaba en pantalla (`22`). Estás gastando 0,5 s en algo que el espectador ya sabe leer.

Si metes un dato nuevo en un plano de 0,5 s, ese dato no existió.

---

## 4. Las cuatro rampas de un reel de negocio local

### Rampa A — La entrada al remate (la que más te va a servir)

Estructura de los últimos 6–8 segundos de un reel:

```
...planos normales (2,5–3 s)...
   ↓ empieza la rampa
1,9 s  →  1,5 s  →  1,2 s  →  0,9 s  →  [REMATE 3,0 s]
```

Los cuatro planos de la rampa duran juntos 5,5 s y **son los que hacen que el remate se sienta como un
remate**. Sin ellos, el remate es simplemente el plano que venía después.

El remate no participa de la rampa: **rompe la rampa**. Es lo que `323` desarrolla.

### Rampa B — El arranque (los primeros 3 segundos)

Al revés de lo que dice el instinto, el arranque **no** se acelera: se hace corto y luego se estabiliza.

```
0,8 s (el gancho, plano fuerte)  →  1,0 s  →  2,4 s  →  2,8 s  →  ritmo de crucero
```

Dos planos cortos al principio establecen que este video **es** de los rápidos, y después bajas a la
cadencia normal. Si empiezas ya rápido y sigues rápido, a los 6 segundos no te queda nada. Ver `30`.

### Rampa C — El proceso comprimido

Cuando muestras algo que se hace paso a paso (montar el plato, servir, preparar el local), la rampa va
**hacia adentro**: cada paso dura menos que el anterior porque cada paso es más obvio que el anterior.

```
paso 1: 2,4 s  (hay que entender qué estamos haciendo)
paso 2: 1,8 s
paso 3: 1,4 s
paso 4: 1,1 s
paso 5: 0,9 s  (ya se entiende, solo confirma)
resultado final: 2,5 s
```

Y aquí tu herramienta favorita hace la mitad del trabajo: en vez de cortar cinco veces, **acelera el clip**
a 2,0x o 2,5x (`201`) y deja que la velocidad haga la compresión sin romper continuidad. Una rampa de
velocidad dentro de un plano continuo es rítmicamente equivalente a una rampa de cortes, y se ve mejor.

### Rampa D — La desaceleración de salida

Después del remate, si vas a poner un cierre (la marca, el llamado a la acción, el dato de contacto), el
ciclo se **alarga**:

```
[REMATE]  →  2,2 s  →  3,0 s (cierre en pantalla, quieto)
```

Un cierre que entra en medio de un ritmo rápido no se lee. La desaceleración es lo que le da al espectador
permiso para leer. Y es el único lugar del reel donde un plano quieto de 3 segundos es correcto.

---

## 5. Cómo se hace en CapCut, un domingo

1. Arma el corte normalmente, sin pensar en rampas.
2. Identifica **dónde está el remate**. Solo ese punto.
3. Cuenta cuatro planos hacia atrás desde el remate. Esa es tu rampa.
4. Escribe la tabla con `r = 0,78` a partir de la duración actual del primero de esos cuatro.
5. Ajusta cada uno **recortando por el final** (`320` §7). Si un plano no da para acortarse tanto porque
   se come una palabra, no lo fuerces: baja la rampa a `r = 0,86` para toda la serie.
6. Si a un plano le sobra imagen pero le falta velocidad, **acelera en vez de recortar**.
7. Reproduce solo esos 6 segundos, tres veces seguidas. Si el remate no "aterriza", el problema es que la
   rampa es demasiado suave, no demasiado agresiva.

**Regla de tijera:** en la rampa nunca recortes hasta el punto de partir una palabra. La sílaba manda sobre
la aritmética (`325`). Si la duración objetivo cae dentro de una palabra, vete al límite de palabra más
cercano y acepta el desvío de 0,1–0,2 s. Nadie percibe 0,15 s de desvío; todo el mundo percibe una palabra
partida.

---

## 6. Verificar la rampa con datos

```bash
# Duraciones de los últimos 6 planos, desde el draft de CapCut
jq -r '.tracks[] | select(.type=="video") | .segments[] |
  "\(.target_timerange.start/1000000)\t\(.target_timerange.duration/1000000)"' \
  draft_content.json | sort -n | tail -6 | \
awk '{d=$2; if(NR>1) printf "plano %d: %.2f s   ratio vs anterior: %.2f\n", NR, d, d/p;
      else printf "plano %d: %.2f s\n", NR, d; p=d}'
```

Qué buscar en la salida:

| Lo que ves | Diagnóstico |
|---|---|
| Ratios entre 0,72 y 0,85, consistentes | ✅ Rampa sana |
| Ratios alrededor de 1,0 | ❌ No hay rampa. Es una lista |
| Un ratio de 0,45 en medio | ⚠️ Salto brusco. Se va a sentir como error, no como aceleración |
| Ratios que suben y bajan (0,8 · 1,3 · 0,7 · 1,2) | ❌ Ruido, no rampa |
| Último ratio > 2,0 | ✅ Eso es el remate rompiendo la rampa. Correcto (`323`) |

---

## 7. Lo que no se puede afirmar

No existe, que sea público y verificable, un estudio que demuestre que una rampa de aceleración aumenta la
retención en video corto. Ni Meta ni TikTok publican datos de cadencia de corte. Lo que hay es:

- Práctica de oficio, consistente y verificable a ojo en cualquier tráiler, comercial o reel que funcione.
- El hallazgo de Cutting et al. (2010) de que las duraciones de plano en cine se correlacionan con las
  vecinas (`321` §3), que es evidencia de que la **estructura** de la secuencia importa — no una receta.

Así que trata la rampa como lo que es: **una herramienta de oficio con una fórmula, que puedes probar
contra tu propio historial**. Corre el experimento en tus propios videos (`304`) antes de creerle a nadie,
incluido este módulo.

---

## Errores comunes

1. **Rampa restando en vez de multiplicando.** Se despeña al final y se siente como un error de montaje.
2. **Acelerar con información nueva.** Un dato en un plano de 0,5 s no se transmitió. La parte rápida se
   hace con material ya conocido.
3. **Empezar la rampa demasiado pronto.** Una rampa de 8 planos no es una rampa: es un video que se acelera
   y el espectador se agota antes de llegar.
4. **No romper la rampa en el remate.** Si el remate también es corto, la aceleración no significó nada. La
   rampa existe para que el remate contraste (`323`).
5. **Forzar la duración objetivo partiendo una palabra.** La aritmética pierde siempre contra la sílaba.
6. **Confundir aceleración de cortes con aceleración de velocidad.** Son dos instrumentos distintos; se
   pueden combinar, pero acelerar el clip a 2x no acorta el ciclo si el plano sigue durando lo mismo en la
   línea de tiempo.
7. **Meter la rampa donde no hay nada que rematar.** Si el video no tiene un punto de llegada, la
   aceleración es energía sin destino y se siente ansiosa.
8. **Desacelerar antes del remate.** Alargar el plano justo antes del golpe mata el golpe. La desaceleración
   va **después**.
9. **Cerrar el video en ritmo rápido.** Un llamado a la acción que entra a 0,9 s no se lee y no se recuerda.
10. **Aplicar la rampa a los cortes pero no a la música.** Si la música mantiene su intensidad plana, la
    aceleración visual pelea contra ella. Ver `24` y `298`.
11. **Revisar la rampa solo mirándola.** Es de los pocos defectos que se detectan mejor **cerrando los ojos
    y escuchando**: la cadencia de los empalmes de audio delata la rampa.

---

## Checklist

- [ ] Sé exactamente **cuál plano es el remate** del video
- [ ] Los 4 planos anteriores al remate forman una rampa con ratio entre **0,72 y 0,85**
- [ ] La rampa se construyó **multiplicando**, y las duraciones están redondeadas al fotograma
- [ ] Ningún plano de la rampa baja de **0,6 s** salvo que sea material ya visto
- [ ] El **remate rompe la rampa**: dura al menos el doble que el plano anterior
- [ ] Ninguna duración de la rampa partió una palabra
- [ ] El arranque tiene 1–2 planos cortos y después baja a cadencia de crucero
- [ ] Si hay cierre o llamado a la acción, va en **desaceleración** y dura ≥ 2,5 s
- [ ] Verifiqué los ratios reales con el comando de la sección 6
- [ ] Escuché los últimos 8 segundos con los ojos cerrados y la rampa se oye
- [ ] Comparé el resultado contra un reel mío anterior sin rampa, no contra una teoría
