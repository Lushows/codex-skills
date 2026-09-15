# 374 — Ritmo del texto contra ritmo del corte: el contratiempo

Aquí está lo que separa un video que "se ve bien editado" de uno que **se siente**. `46` cubre el ritmo
del texto contra la voz. Este módulo es el otro par: **texto contra corte**. Son dos pulsos
independientes, y lo que hagas con la relación entre ellos es una decisión de dirección, no de montaje.

---

## 1. Dos relojes

Un video corto tiene dos relojes corriendo al mismo tiempo:

- **El reloj de la imagen:** cada cuánto cambia el plano.
- **El reloj del texto:** cada cuánto entra una palabra.

Casi todo el mundo los amarra: cambia el plano y cambia el texto, siempre. Es el ajuste por defecto y
funciona… durante unos 8 segundos. Después el video se vuelve **plano**: todo pasa al mismo tiempo, todo
tiene el mismo peso, y la atención se va porque no hay sorpresa.

> El ritmo no está en la velocidad. Está en **la variación de la relación entre los dos relojes.**

---

## 2. Las cuatro relaciones

| Relación | Qué es | Qué produce | Cuánto usar |
|---|---|---|---|
| **Al unísono** | Texto y corte en el mismo fotograma | Golpe, contundencia, cierre | 30-40% |
| **Anticipación** | Texto entra 2-4 fotogramas ANTES del corte | El texto "provoca" el corte. Fluidez | 25% |
| **Retardo** | Texto entra 3-8 fotogramas DESPUÉS del corte | El plano respira y luego habla | 20% |
| **Contratiempo** | Texto entra a mitad de camino entre dos cortes | Energía, síncopa, sensación de dos capas vivas | 15-25% |

Nota que "al unísono" no es el 100%. Ese es todo el punto.

A 30 fps, 1 fotograma = 0,033 s. A 60 fps = 0,017 s. Los desfases de abajo están en fotogramas porque en
CapCut se ajustan moviendo el segmento, no escribiendo un número.

---

## 3. Al unísono: el golpe

Texto y corte caen exactos en el mismo fotograma. El impacto se suma: el ojo recibe cambio de plano +
aparición de palabra + golpe de sonido en un solo evento.

**Se reserva para tres momentos:**
- El primer texto del video (el gancho).
- El remate de una cascada.
- El llamado a la acción final.

Usado en todo el video pierde su efecto: si todo golpea, nada golpea.

**Detalle técnico:** "exacto" significa exacto. Un fotograma de desfase se percibe como error, no como
intención. En CapCut, acércate al máximo en la línea de tiempo y usa el imán; si generas por código,
calcula el inicio del texto a partir del inicio del segmento de video, no a ojo.

---

## 4. Anticipación: el texto que jala el corte

El texto entra **2 a 4 fotogramas antes** del corte (0,07-0,13 s a 30 fps).

Efecto perceptivo: el espectador no distingue conscientemente los dos eventos, pero registra que el
texto llegó primero. Eso produce la sensación de que **el texto causó el corte** — de que la edición está
respondiendo al mensaje y no al revés.

Es el ajuste que más "profesionaliza" un corte sin que nadie sepa por qué. Si tienes que elegir un solo
truco de este módulo, es este.

**Dónde usarlo:** en enumeraciones donde cada plano ilustra una palabra. `COMPRAS` (aparece) → corte al
plano del mercado. `NÓMINA` (aparece) → corte al plano de la cocina. El texto manda, la imagen obedece.

---

## 5. Retardo: el plano que respira

El texto entra **3 a 8 fotogramas después** del corte (0,10-0,27 s).

Efecto: el espectador alcanza a *ver* el plano nuevo antes de que le pongan una palabra encima. El plano
existe por sí mismo un instante, y luego el texto lo comenta.

**Dónde usarlo:**
- Cuando el plano es bonito y vale la pena verlo (comida, producto, la cara de alguien).
- En el plano de apertura después de un corte fuerte.
- Cuando el texto es un comentario sobre lo que se ve, no una etiqueta de lo que se ve.

Retardo largo (0,4-0,8 s) para un plano de mucho peso: la cerveza sirviéndose, el plato saliendo. Ahí el
texto llega cuando la imagen ya hizo su trabajo, y se lee como conclusión.

---

## 6. Contratiempo: donde está lo bueno

El texto entra **entre** dos cortes, lejos de los dos. Si el plano dura 1,2 s, el texto entra a los 0,5.

Esto es síncopa: el mismo principio que hace que una batería suene con groove en vez de sonar a
metrónomo. La imagen marca el pulso fuerte; el texto marca el débil. El resultado es que el video se
siente **denso** —pasan cosas todo el tiempo— sin estar cortado más rápido.

```
CORTE      |█████████|█████████|█████████|█████████|
TEXTO           ▲          ▲         ▲          ▲
                 al contratiempo, no en el corte
```

**Dónde brilla:**
- Planos largos que necesitan energía sin poder cortarse más.
- Secuencias musicales donde el corte va con el beat: el texto va con el contratiempo.
- Videos de 30-60 s que se sienten lentos aunque el contenido esté bien.

**Diagnóstico rápido:** si un video "está bien pero se siente lento" y ya no puedes cortar más rápido,
casi siempre la solución es mover los textos al contratiempo. No cambias ni un plano y el video cambia.

---

## 7. La estructura de un video de 20 s, con los dos relojes

```
t(s)  CORTE          TEXTO                          RELACIÓN
0,0   ▓ plano 1      TE VA A DOLER (0,0)            unísono   ← gancho, máximo golpe
2,3   ▓ plano 2                                      —         ← el plano respira
2,5                  NO SABES (2,5)                  retardo
3,4                  CUÁNTO CUESTA (3,4)             contratiempo
4,1   ▓ plano 3                                      —
4,6                  CADA PLATO (4,6)                retardo
5,8                  COMPRAS (5,8)                   contratiempo  ┐
5,98                 NÓMINA                                        │ cascada
6,16                 SERVICIOS                                     │ (372)
6,52                 Y AL FINAL NADA                               ┘
7,9   ▓ plano 4      [limpia]                                      ← salen todas en el corte
9,2                  LA TABLA (9,15)                 anticipación  ← el texto jala
9,3   ▓ plano 5
...
18,0  ▓ plano final  $10.000 (18,0)                  unísono   ← remate
19,2                 ESCRÍBEME (19,2)                contratiempo
```

Lee la columna de la derecha. **Nunca dos relaciones iguales seguidas más de dos veces.** Ese es todo el
secreto del ritmo.

---

## 8. Texto que atraviesa el corte (puente)

Una jugada aparte, y muy poderosa: **la misma palabra se queda en pantalla mientras el plano cambia
debajo.**

```
plano A  ──────corte──────  plano B
      [ PERDIENDO PLATA ────────── ]   ← el texto no se mueve
```

Qué produce: la palabra se vuelve el elemento estable y la imagen el elemento variable. Se lee como
"esto que digo aplica a todo lo que estás viendo". Es la forma más rápida de hacer que tres planos
distintos se sientan como un solo argumento.

Reglas para que funcione:
- La palabra tiene que estar **quieta**: si se mueve durante el corte, se rompe la ilusión.
- Máximo **2 cortes** por debajo. Con tres, la palabra empieza a sentirse pegada.
- No lo uses con sándwich (`377`): el recorte cambia con el plano y el texto parpadearía.

---

## 9. Cuando el corte manda y cuando manda el texto

Una decisión de fondo que conviene tomar conscientemente al empezar la pieza:

**El corte manda** (cortas primero, texto encima): videos con material fuerte —comida, gente, lugares—.
El texto se acomoda a la imagen. Es lo normal en piezas de restaurante y bar.

**El texto manda** (escribes la lista de palabras y cortas para ellas): videos de argumento, listas,
explicaciones, ofertas. Aquí el corte existe para dar variedad detrás del texto, y muchas veces ni
siquiera hay planos distintos: hay un plano con zooms.

Saber cuál de los dos es la pieza te ahorra horas. Si tienes material fuerte y estás forzando el texto, o
si tienes un argumento y estás buscando planos bonitos, estás trabajando contra la pieza.

---

## 10. Cómo se ajusta esto en CapCut, en la práctica

- Acércate al máximo con dos dedos: a máximo zoom, CapCut mueve segmentos **fotograma a fotograma**.
- **Desactiva el imán** cuando estés poniendo anticipación o retardo. Con el imán activo, el texto se
  pega al corte y pierdes exactamente el efecto que buscas. Actívalo solo para los unísonos.
- Ajusta **oyendo**, no mirando: pon el golpe de sonido del texto y mueve el texto hasta que el conjunto
  "caiga bien". El oído detecta desfases de 20 ms; el ojo no.
- Si generas por código: guarda los tiempos de corte en un arreglo y calcula los tiempos de texto
  **relativos** a ellos.

```js
const cortes = [0.0, 2.30, 4.10, 7.90, 9.30];   // segundos
const F = 1 / 30;                                // 1 fotograma a 30 fps

const rel = {
  unison:      c => c,
  anticipa:    c => c - 3 * F,                   // 3 fotogramas antes
  retarda:     c => c + 6 * F,                   // 6 fotogramas después
  contratiempo:(c, siguiente) => c + (siguiente - c) * 0.42,
};
// microsegundos al escribir el draft: Math.round(s * 1_000_000)
```

El 0,42 en vez de 0,5 no es capricho: el contratiempo exacto a la mitad se siente mecánico. Un poco
antes de la mitad se siente vivo. Es la misma razón por la que un baterista humano no está nunca
exactamente en el grid.

---

## Errores comunes

1. **Amarrar todos los textos al corte.** El video se aplana a los 8 segundos.
2. **Dejar el imán activo** mientras buscas anticipación o retardo: el editor te devuelve el texto al corte.
3. **Un fotograma de desfase en un unísono.** Se lee como error, no como intención. O exacto o desfasado
   de verdad.
4. **Anticipación mayor a 5 fotogramas.** Deja de leerse como causa y se lee como texto suelto.
5. **Retardo mayor a 0,8 s** en un plano corto: el texto llega cuando el plano ya se fue.
6. **Contratiempo en el gancho.** Los primeros 2 segundos necesitan golpe, no groove.
7. **Tres o más relaciones iguales seguidas.** Ahí es donde el video se siente monótono.
8. **Contratiempo exactamente en la mitad.** Suena a cuadrícula. Usa ~42%.
9. **Mover el texto puente durante el corte**: rompe la ilusión de estabilidad.
10. **Texto puente sobre más de dos cortes.** Empieza a sentirse pegado a la pantalla.
11. **Combinar puente con sándwich.** El recorte cambia con el plano y el texto parpadea.
12. **Ajustar solo mirando.** El oído detecta el desfase antes que el ojo: monta con el golpe puesto.
13. **No decidir quién manda.** Forzar texto sobre material fuerte, o buscar planos bonitos para un
    argumento, cuesta horas y se nota.

---

## Checklist

- [ ] Decidí conscientemente si en esta pieza manda el corte o manda el texto
- [ ] Anoté la relación (unísono / anticipación / retardo / contratiempo) de cada entrada de texto
- [ ] No hay tres relaciones iguales seguidas
- [ ] Los unísonos están reservados para gancho, remate y llamado a la acción
- [ ] Los unísonos están al fotograma exacto
- [ ] Hay al menos un texto con anticipación de 2-4 fotogramas
- [ ] Los planos bonitos tienen retardo antes de que entre el texto
- [ ] Si el video se sentía lento, moví textos al contratiempo antes de tocar los cortes
- [ ] El contratiempo cae alrededor del 42%, no en la mitad exacta
- [ ] Si usé texto puente, la palabra está quieta y cruza máximo 2 cortes
- [ ] Ajusté con el golpe de sonido puesto, escuchando
- [ ] Desactivé el imán para los desfases y lo reactivé para los unísonos
