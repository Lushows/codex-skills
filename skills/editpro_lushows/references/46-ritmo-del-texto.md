# 46 — El ritmo del texto

## El texto tiene pulso, igual que la imagen

Sabes que la imagen debe cambiar cada 1,5-2 segundos para sostener la atención (ver `20`). El texto tiene
su propio pulso, y es **más rápido**: un cambio cada **0,9 segundos**.

Ese número no se elige: sale de la conversación. Una persona hablando en español a ritmo natural dice
entre 2,2 y 2,6 palabras por segundo. Si agrupas de a **2 palabras por golpe**, cada golpe dura entre
0,77 y 0,91 segundos.

```
2 palabras / 2,3 palabras por segundo = 0,87 s por golpe
```

Por eso 2 palabras por golpe funciona: **no es una decisión de diseño, es la consecuencia de sincronizar
con el habla**.

---

## Por qué 4-6 palabras por golpe mata el video

Es el error de configuración más común, porque es el default de casi todas las herramientas automáticas.

| Palabras por golpe | Duración del golpe | Efecto |
|---|---|---|
| 1 | ~0,45 s | Frenético. Cansa a los 10 segundos. Solo para tramos de énfasis |
| **2** | **~0,9 s** | **El pulso correcto** |
| 3 | ~1,3 s | Aceptable en habla lenta o voz en off pausada |
| 4-6 | **~2,0-2,6 s** | **El texto se queda quieto 2 segundos. El pulso muere** |
| Frase completa | 3-5 s | Diapositiva. El ojo lee, se aburre, se va |

Dos segundos de texto inmóvil en un reel es una eternidad. El ojo termina de leer en 600 ms y se queda sin
nada que hacer durante 1,4 segundos. Ahí es donde la mano sube el dedo.

Con golpes de 2 palabras, **hay siempre algo pasando**. El video se siente rápido aunque los planos duren
lo mismo.

---

## La regla de la palabra colgante

**Nunca termines un golpe en una palabra vacía.**

Palabras colgantes en español: `en`, `la`, `el`, `de`, `del`, `por`, `para`, `una`, `un`, `y`, `o`, `que`,
`con`, `sin`, `a`, `al`, `su`, `lo`, `los`, `las`, `se`, `es`, `no` (cuando es auxiliar).

Estas palabras **no significan nada solas**. Terminar un golpe ahí deja al lector suspendido durante 0,9
segundos con un fragmento incompleto:

```
MAL:
  golpe 1: "TU NEGOCIO PIERDE"     -> ok
  golpe 2: "PLATA POR"             -> ??? "por" qué?
  golpe 3: "CADA PLATO"            -> ahh

BIEN:
  golpe 1: "TU NEGOCIO"
  golpe 2: "PIERDE PLATA"
  golpe 3: "POR CADA PLATO"        -> "por" arranca el golpe, no lo termina
```

### La solución: robar la siguiente palabra

Si el golpe va a terminar en colgante, **róbate la siguiente palabra** y haz un golpe de 3.

```
"la calculadora de costos"

MAL:  [LA CALCULADORA] [DE COSTOS]      -> ok, "de" arranca
MAL:  [LA CALCULADORA DE] [COSTOS]      -> "de" cuelga
BIEN: [LA CALCULADORA] [DE COSTOS]
```

Otro caso:

```
"vas a saber cuánto te cuesta un plato"

MAL:  [VAS A] [SABER CUANTO] [TE CUESTA] [UN PLATO]
      "VAS A" cuelga: "a" no significa nada

BIEN: [VAS A SABER] [CUANTO TE CUESTA] [UN PLATO]
      3 palabras, 3 palabras, 2 palabras. Cada golpe cierra una unidad de sentido.
```

**El principio real detrás de la regla:** cada golpe debe ser una **unidad de sentido mínima**. Un sujeto,
un verbo con su objeto, un complemento. Si al leer el golpe solo te preguntas "¿y?", está mal cortado.

### La regla se aplica al inicio también

Un golpe que **empieza** con colgante está bien: `POR CADA PLATO`, `DE COSTOS`, `QUE NADIE VE`. El lector
lee "por" y sigue de inmediato a la palabra que sí significa. El problema es solo al final.

---

## Los números se juntan y se escriben en cifras

Esta regla salva videos.

Cuando alguien dice **"mil novecientos ocho"**, la transcripción automática te devuelve tres palabras. Si
las agrupas de a dos, obtienes:

```
[MIL NOVECIENTOS] [OCHO]
```

Y eso se lee **terrible**. El lector procesa "mil novecientos" como una cantidad, luego ve "ocho" y tiene
que rehacer todo el número en su cabeza. En 0,9 segundos no alcanza.

**Correcto:**

```
[1908]
```

Un solo golpe. Se lee de un vistazo. Pega.

### Las reglas de los números

1. **Un número hablado es un solo golpe**, sin importar cuántas palabras ocupe al decirlo.
2. **Se escribe en cifras**, no en letras. `1908`, no `MIL NOVECIENTOS OCHO`.
3. **Con separador de miles según la convención local.** En Colombia: `$10.000`, `1.500 gramos`.
4. **Con su unidad o símbolo pegado.** `$10.000`, `30%`, `48 h`, `2 kg`. La unidad es parte del número.
5. **Puede llevar la palabra que lo califica** si es corta: `[$10.000 PESOS]`, `[30% MENOS]`, `[48 HORAS]`.
6. **Un número merece más tiempo en pantalla.** Un golpe normal dura 0,9 s; un número denso (`$1.250.000`)
   merece 1,2-1,4 s aunque la voz haya pasado. El lector necesita procesarlo.

### Casos frecuentes

| Se dice | MAL en pantalla | BIEN |
|---|---|---|
| "diez mil pesos" | `DIEZ MIL` / `PESOS` | `$10.000` |
| "el treinta por ciento" | `EL TREINTA` / `POR CIENTO` | `30%` |
| "dos mil veintiséis" | `DOS MIL` / `VEINTISEIS` | `2026` |
| "cuarenta y ocho horas" | `CUARENTA Y` / `OCHO HORAS` | `48 HORAS` |
| "tres de cada cuatro" | `TRES DE` / `CADA CUATRO` | `3 DE CADA 4` |
| "un millón doscientos mil" | `UN MILLON` / `DOSCIENTOS MIL` | `$1.200.000` |
| "el punto cinco por ciento" | `EL PUNTO` / `CINCO POR CIENTO` | `0,5%` |

Ojo con la coma decimal: en Colombia el decimal es coma (`0,5%`) y el separador de miles es punto
(`$10.000`). No lo escribas a la inglesa.

---

## Sincronía con la voz

### El golpe llega antes, nunca después

El texto debe caer entre **30 y 60 milisegundos antes** de la sílaba tónica de su primera palabra.

La tolerancia del ojo es **asimétrica**: un texto 50 ms adelantado se percibe como perfectamente
sincronizado; un texto 50 ms atrasado se percibe como tarde. Aprovecha esa asimetría.

Regla práctica: al timecode de inicio de la palabra según la transcripción, **réstale 0,04 s**.

### Qué hacer con las pausas

Cuando la persona hace una pausa larga (respira, piensa, cambia de tema):

- **Pausa corta (< 0,5 s):** extiende el golpe anterior hasta que empiece el siguiente. Sin huecos.
- **Pausa media (0,5-1,5 s):** deja el último golpe en pantalla hasta que arranca el siguiente. Que el
  texto acompañe el silencio.
- **Pausa larga (> 1,5 s):** **saca el texto**. Pantalla limpia. Es un respiro deliberado y sirve para
  marcar un cambio de sección. Aprovéchalo para meter un b-roll fuerte.

**Nunca** dejes microhuecos de 100-200 ms entre golpes: se ve como un parpadeo y se siente descuidado. Si
dos golpes son consecutivos, el `End` del primero debe ser exactamente el `Start` del segundo.

```
Dialogue: 0,0:00:01.20,0:00:02.08,Golpe,,0,0,0,,{...}TU NEGOCIO
Dialogue: 0,0:00:02.08,0:00:02.95,Golpe,,0,0,0,,{...}PIERDE PLATA
                       ^^^^^^^^^^ mismo valor exacto
```

### Cuando la voz se acelera

En un tramo rápido (una enumeración, un remate), los golpes se acortan solos a 0,6-0,7 s. Está bien: el
texto sigue a la voz, no al reloj. Lo que **no** debe pasar es que un golpe baje de **0,4 s** — a esa
velocidad no se lee. Si la voz va tan rápido, junta más palabras aunque rompas los 2 por golpe: es mejor
un golpe de 4 palabras leíble que dos de 0,3 s ilegibles.

---

## El ritmo del texto vs. el ritmo de la imagen

Dos pulsos corriendo a la vez:

- **Imagen:** cambio cada 1,5-2 s
- **Texto:** cambio cada 0,9 s

Es decir, **aproximadamente 2 golpes de texto por cada plano**. Eso funciona bien: el texto marca la
subdivisión y el corte marca el compás.

**Regla de oro:** que el corte de imagen coincida con un cambio de texto. Nunca a medio golpe. Un corte
que cae en la mitad de un golpe de texto crea una sensación de desajuste que la gente siente sin saber
por qué.

Al montar: primero fija los tiempos del texto (que dependen de la voz y no se negocian), y luego mueve
los cortes de imagen **a los límites de golpe más cercanos**. Ver `24`.

---

## Herramientas: cómo obtener los tiempos

Necesitas timecodes **por palabra**, no por frase. Un modelo de transcripción tipo Whisper con
`word_timestamps` te los da.

Lo que recibes:

```json
[
  {"palabra": "tu",      "ini": 1.24, "fin": 1.38},
  {"palabra": "negocio", "ini": 1.38, "fin": 1.92},
  {"palabra": "pierde",  "ini": 2.12, "fin": 2.51},
  {"palabra": "plata",   "ini": 2.51, "fin": 2.96}
]
```

Y el agrupador aplica las reglas:

```javascript
const COLGANTES = new Set([
  "en","la","el","de","del","por","para","una","un","y","o","que",
  "con","sin","a","al","su","lo","los","las","se","es","mi","tu"
]);

function agrupar(palabras, max = 2) {
  const golpes = [];
  let i = 0;
  while (i < palabras.length) {
    let n = Math.min(max, palabras.length - i);
    // si el ultimo del golpe es colgante y hay mas texto, roba una palabra
    while (
      n < palabras.length - i &&
      COLGANTES.has(palabras[i + n - 1].palabra.toLowerCase())
    ) {
      n++;
    }
    const grupo = palabras.slice(i, i + n);
    golpes.push({
      ini: grupo[0].ini - 0.04,
      fin: grupo[grupo.length - 1].fin,
      txt: grupo.map(p => p.palabra).join(" ").toUpperCase()
    });
    i += n;
  }
  // cerrar huecos: el fin de cada golpe es el inicio del siguiente si estan pegados
  for (let k = 0; k < golpes.length - 1; k++) {
    if (golpes[k + 1].ini - golpes[k].fin < 0.5) {
      golpes[k].fin = golpes[k + 1].ini;
    }
  }
  return golpes;
}
```

**Lo que este código NO hace y tú sí tienes que hacer a mano:** juntar los números. La detección de
"mil novecientos ocho" → `1908` requiere entender el idioma. Repasa la lista de golpes generada, busca
números partidos, y júntalos. Es el paso manual que separa un subtitulado bueno de uno automático.

---

## Errores comunes

- **Dejar el default de 4-6 palabras por golpe.** Es lo que traen las herramientas automáticas y es lo que
  mata el pulso. Cámbialo siempre.
- **Terminar un golpe en `de`, `la`, `por`, `que`.** Deja al lector suspendido. Roba la siguiente palabra.
- **Partir un número en dos golpes.** `MIL NOVECIENTOS` / `OCHO`. Es el error que más daño hace por lo
  poco que cuesta arreglarlo.
- **Escribir los números en letras.** `DIEZ MIL PESOS` en vez de `$10.000`. Las cifras se leen de un
  vistazo, las letras hay que procesarlas.
- **Usar punto decimal y coma de miles a la inglesa.** En Colombia es `$10.000` y `0,5%`.
- **Poner el texto después de la voz.** Se siente tarde. Adelántalo 40 ms.
- **Microhuecos entre golpes consecutivos.** Parpadeo. El `End` de uno es el `Start` del siguiente,
  exactamente.
- **Dejar texto en pantalla durante un silencio largo.** Si hay más de 1,5 s sin voz, saca el texto.
- **Golpes por debajo de 0,4 s.** No se leen. Junta palabras aunque rompas la regla de 2.
- **Cortar la imagen a mitad de un golpe de texto.** Los dos pulsos deben coincidir en los límites.
- **Aplicar el agrupador automático y publicar sin revisar.** El código agrupa; los números y las
  unidades de sentido los revisa un humano.
- **Ritmo uniforme de principio a fin.** El ritmo del texto sigue a la voz. Si la voz acelera en el
  remate, el texto acelera. Un ritmo mecánico se siente robótico.

---

## Checklist

- [ ] El agrupamiento es de **2 palabras por golpe** como base (3 cuando hay que robar palabra).
- [ ] Ningún golpe termina en palabra colgante (`en`, `la`, `de`, `por`, `una`, `y`, `que`...).
- [ ] Cada golpe es una unidad de sentido: leído solo, no deja al lector preguntándose "¿y?".
- [ ] **Todos los números están juntos en un solo golpe y escritos en cifras.**
- [ ] Los números llevan su símbolo o unidad pegada: `$10.000`, `30%`, `48 HORAS`.
- [ ] Separadores a la colombiana: punto para miles, coma para decimales.
- [ ] Los golpes con número denso duran 1,2-1,4 s, no 0,9 s.
- [ ] Cada golpe arranca 30-60 ms **antes** de la sílaba tónica.
- [ ] No hay microhuecos: `End` de un golpe = `Start` del siguiente cuando son consecutivos.
- [ ] En pausas de más de 1,5 s la pantalla queda limpia.
- [ ] Ningún golpe dura menos de 0,4 s.
- [ ] Los cortes de imagen coinciden con límites de golpe, no caen a mitad.
- [ ] Revisé **a mano** la lista completa de golpes generada por el script.
- [ ] El ritmo acompaña a la voz, incluidos los tramos rápidos y las pausas.
