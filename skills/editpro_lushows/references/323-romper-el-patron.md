# 323 — Romper el patrón a propósito: el plano largo después de la ráfaga

**Qué resuelve:** tienes un reel con buen ritmo, buena mediana, buena dispersión, y aun así no se recuerda
nada de él. Todo pasó a la misma velocidad, así que nada tuvo más peso que lo demás. Este módulo es sobre
el único recurso que le da **jerarquía** a un montaje sin cambiar una sola palabra del guion: establecer un
patrón y romperlo.

Es el complemento exacto de `322`. Allí construimos la rampa; aquí construimos el golpe que la rampa
justifica.

---

## 1. La mecánica: el contraste no está en el plano, está en el vecino

Un plano de 3,5 segundos, solo, no es nada. Un plano de 3,5 segundos **después de cuatro planos de 0,9**
es un frenazo, y se siente enorme.

```
0,9   0,8   0,9   0,8   │        3,5        │
▮     ▮     ▮     ▮     │▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮│
    la ráfaga           │     el freno      │
```

La misma imagen, en el mismo video, con planos vecinos de 3,0 s, no se nota. **El significado de una
duración es siempre relativo a las duraciones que la rodean.** No hay planos largos: hay planos más largos
que los de al lado.

De ahí sale la regla operativa central del módulo:

> **Un plano no se destaca porque dure mucho. Se destaca porque los anteriores duraron poco.**

Si quieres que algo se recuerde, no lo alargues: **acorta lo que va antes**.

---

## 2. Por qué el cerebro reacciona a la ruptura

Hay dos cosas que decir aquí, una sólida y una de oficio, y conviene no mezclarlas.

**Lo sólido.** En neurociencia auditiva existe un fenómeno muy replicado: el paradigma *oddball*. Si le
presentas a alguien una secuencia regular de estímulos idénticos y de pronto metes uno distinto, el
cerebro genera una respuesta eléctrica específica al desviado (la *mismatch negativity*), incluso cuando la
persona no está prestando atención a la secuencia. La respuesta necesita que el estándar se haya
establecido antes: con una o dos repeticiones no hay "estándar" que violar.

**Lo que no se puede afirmar.** Ese trabajo se hizo con tonos en un laboratorio, no con planos de video. No
existe un estudio publicado que mida la respuesta a una ruptura de cadencia de montaje en un reel. Quien te
diga "está científicamente probado que romper el ritmo aumenta la retención un X%" se lo inventó.

Lo que sí se traslada, y es lo útil: **la ruptura necesita un patrón previo, y el patrón necesita
repeticiones para existir.** De ahí el número operativo:

> **Tres unidades mínimo para establecer el patrón. La cuarta es la que rompe.**

Con dos planos parecidos no hay patrón: hay coincidencia. Ver también `327`, donde el mismo número aparece
por otra razón distinta.

---

## 3. La receta: la ráfaga y el freno

### Parámetros que funcionan

| Elemento | Valor | Por qué |
|---|---|---|
| Planos de la ráfaga | **3 a 5** | Menos de 3 no establece patrón; más de 5 agota |
| Duración de cada uno | **0,7 – 1,2 s** | Suficiente para leer algo conocido, no para algo nuevo |
| Variación dentro de la ráfaga | **< 15%** | La ráfaga tiene que ser *regular* o no hay patrón que romper |
| Duración del freno | **≥ 2,5 × la mediana de la ráfaga** | Por debajo de 2,5× no se lee como ruptura, se lee como plano largo |
| Rupturas por reel de 25 s | **1, máximo 2** | Ver §6 |

Con ráfaga de 0,9 s, el freno debe durar **al menos 2,25 s**, y funciona mejor entre 3,0 y 4,0 s.

### Qué va dentro del freno

Esto es lo que la mayoría hace mal. En el plano largo va **lo único que quieres que se recuerde del video**:

- El producto, quieto, bien iluminado, grande.
- La cara de alguien diciendo la frase que importa.
- El precio. El nombre. La dirección.
- El resultado final del proceso que acabas de mostrar comprimido.

Lo que **no** va: transición, logo animado, un plano de relleno "para bajar la energía". Si el freno no
contiene el mensaje, gastaste tu único momento de atención máxima en nada.

### Cómo hacer que el freno no se sienta muerto

Un plano largo se muere si dentro no pasa nada. Tienes cuatro formas de meterle vida sin cortarlo:

1. **Movimiento interno lento.** Un punch-in progresivo del 100% al 108% durante los 3 segundos (`22`,
   `203`). El ojo tiene algo que seguir y no lo registra como zoom.
2. **La entrada del texto.** El texto entra en el segundo 0,4 del freno, no en el 0,0. Ese retraso es la
   diferencia entre "apareció texto" y "el video me está diciendo algo".
3. **El sonido.** Un silencio de la música justo en el corte al freno, y la música vuelve 0,8 s después.
   Es la ruptura equivalente en audio y multiplica la visual (`296`, `298`).
4. **Que algo termine de moverse.** La espuma que sigue bajando, el vapor, la mano que sale de cuadro. El
   plano está quieto pero la imagen no.

---

## 4. Las cuatro rupturas útiles

### Ruptura A — El freno (la principal)

Ráfaga rápida → plano largo. Es la que acabas de leer. Se usa **una vez por reel**, en el remate o justo
antes de él.

### Ruptura B — El destello

Al revés: pasaje de planos largos → **un plano de 0,3 s** → vuelta a lo largo. Sirve para meter un dato,
un chiste visual o una reacción sin cambiar la estructura. Solo funciona si ese plano de 0,3 s contiene
algo instantáneamente legible: una cara, un número grande, un objeto conocido.

### Ruptura C — El corte que no llega

Estableces un patrón donde cada plano dura ~1,5 s y el espectador ya espera el corte... **y no llega**. El
plano sigue 2 segundos más. Es la versión rítmica del silencio incómodo, y en comedia es oro: la cara que
se queda en pantalla más de lo que corresponde es un chiste por sí sola.

Riesgo: entre "chiste" y "el editor se durmió" hay unos 0,5 segundos. Pruébalo con alguien más.

### Ruptura D — El corte anticipado

El opuesto: patrón de 2,5 s y el corte cae a los 1,1 s, antes de que la acción termine. Se siente como una
interrupción, y por eso funciona para cortar a alguien a media frase cuando eso es el chiste, o para
saltar a la conclusión. Ver `25` (elipsis).

---

## 5. Medir si tu ruptura es de verdad una ruptura

```bash
# Duraciones en orden, con el ratio contra la mediana de los 3 planos anteriores
jq -r '.tracks[] | select(.type=="video") | .segments[] |
  "\(.target_timerange.start/1000000)\t\(.target_timerange.duration/1000000)"' \
  draft_content.json | sort -n | awk '{print $2}' | \
awk '{
  d[NR]=$1
}
END{
  for(i=4;i<=NR;i++){
    a=d[i-1]; b=d[i-2]; c=d[i-3];
    # mediana de los 3 anteriores
    m=(a+b+c) - ((a>b?(a>c?a:c):(b>c?b:c))) - ((a<b?(a<c?a:c):(b<c?b:c)));
    r=d[i]/m;
    marca = (r>=2.5 ? "  ◄── RUPTURA" : (r<=0.45 ? "  ◄── destello" : ""));
    printf "plano %2d: %.2f s   ratio vs 3 anteriores: %.2f%s\n", i, d[i], r, marca;
  }
}'
```

Lectura de la salida:

| Resultado | Diagnóstico |
|---|---|
| Ningún ratio ≥ 2,5 | **No hay ruptura.** El video es plano aunque la dispersión parezca bien |
| Un ratio ≥ 2,5 cerca del final | ✅ Es lo normal y lo correcto |
| Tres o más ratios ≥ 2,5 | ❌ La ruptura dejó de ser ruptura. Es solo un montaje irregular |
| Ratio ≥ 2,5 pero los 3 anteriores varían mucho entre sí | ⚠️ No había patrón que romper. Empareja la ráfaga primero |

Ese último caso es el más común y el más invisible: **para que la ruptura funcione, la ráfaga tiene que ser
aburridamente regular.** Si tus cuatro planos rápidos duran 0,7 · 1,3 · 0,8 · 1,1, el espectador nunca
aprendió el patrón y el freno no le sorprende nada.

---

## 6. La economía de la ruptura

Una ruptura cuesta atención y la atención no se recarga dentro del mismo reel. Presupuesto:

| Duración del video | Rupturas |
|---|---|
| < 15 s | **1**, y es el remate |
| 15 – 30 s | **1**, o 2 si una es un destello (tipo B) |
| 30 – 60 s | **2**, separadas por al menos 12 s |
| > 60 s | 1 cada 20–25 s aproximadamente |

Si rompes el patrón cada 5 segundos, **la ruptura es el patrón** y vuelves al punto de partida: un montaje
sin jerarquía, solo que ahora también sin cadencia. Es exactamente el error de los reels que se sienten
epilépticos: tienen mucha variación y ninguna estructura.

---

## Errores comunes

1. **Romper sin haber establecido nada.** Tres unidades mínimo, o no hay patrón. La ruptura sin patrón es
   simplemente un plano largo.
2. **Ráfaga irregular.** Si los planos rápidos varían más del 15% entre sí, el espectador no aprende el
   patrón y el freno no contrasta.
3. **Freno demasiado corto.** Por debajo de 2,5× la mediana de la ráfaga no se lee como ruptura.
4. **Poner relleno en el freno.** El plano largo es el momento de máxima atención del video. Ahí va el
   mensaje, no un plano de apoyo.
5. **Freno completamente muerto.** Sin movimiento interno, sin entrada de texto, sin evento sonoro, tres
   segundos son eternos. Mete una de las cuatro cosas de §3.
6. **Más de dos rupturas en un reel corto.** La tercera ruptura ya no rompe nada.
7. **Poner la ruptura al principio.** No hay patrón todavía: es el segundo 2 del video. Las rupturas viven
   en la segunda mitad.
8. **Confundir ruptura con transición.** Un fundido no rompe el patrón: lo suaviza. La ruptura se hace con
   corte duro, siempre.
9. **Que la música siga igual durante el freno.** Si el ritmo visual frena y la música no, la ruptura se
   diluye. Corta la música, bájala, o déjala caer en el mismo fotograma (`75`, `298`).
10. **Usar la ruptura C (el corte que no llega) sin probarla con alguien.** La frontera entre chiste y error
    es de medio segundo y tú no la puedes juzgar porque ya sabes el chiste.
11. **Justificar un plano largo que sobraba llamándolo "ruptura".** Si el plano no contiene el mensaje, es
    grasa con nombre elegante. Aplícale la prueba de la carga (`320` §2).
12. **Citar el efecto oddball como si estuviera medido en video.** Está medido con tonos. Es una analogía
    útil, no una prueba.

---

## Checklist

- [ ] El video tiene **una** ruptura clara, y sé exactamente cuál plano es
- [ ] Antes de la ruptura hay **3 a 5 planos** que establecen el patrón
- [ ] Esos planos varían entre sí **menos del 15%**
- [ ] El plano de ruptura dura **≥ 2,5 ×** la mediana de la ráfaga
- [ ] Dentro del plano de ruptura está **el mensaje** que quiero que se recuerde
- [ ] El plano de ruptura tiene vida interna: movimiento lento, entrada de texto, o evento sonoro
- [ ] La música acompaña la ruptura en lugar de ignorarla
- [ ] La ruptura está en la **segunda mitad** del video
- [ ] No hay una tercera ruptura compitiendo con esta
- [ ] Corrí el comando de §5 y el ratio real es ≥ 2,5
- [ ] Le mostré los últimos 8 segundos a alguien que no vio el video antes
