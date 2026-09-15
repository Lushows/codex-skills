# 377 — El texto detrás del sujeto: coreografía dentro del sándwich

`262` explica la técnica: mismo clip dos veces, normal abajo, recortado arriba, el contenido en medio.
Ese módulo es la mecánica. **Este es la coreografía del texto dentro de ella**: qué palabra se gana el
puesto de atrás, cuánto puede taparse sin volverse ilegible, cómo cambian las reglas de entrada y
tamaño, y —lo más importante— cuándo no vale la pena.

Usas sándwich en **27 de 52** proyectos. Es tu firma. Vale la pena afinarla.

---

## 1. La pila, recordada en tres líneas

```
PISTA 3   ▸  el mismo clip, con recorte de sujeto
PISTA 2   ▸  EL TEXTO            ← de esto trata este módulo
PISTA 1   ▸  el mismo clip, normal
```

Lo que hay que retener para lo que sigue: **el texto está en un plano espacial detrás de la persona.** Y
si está detrás, tiene que comportarse como algo que está detrás. Casi todos los errores de sándwich con
texto salen de olvidar eso.

---

## 2. Qué palabra se gana el puesto de atrás

No todas. **Una o dos por video.** El sándwich es un recurso de énfasis, y un énfasis usado seis veces
deja de ser énfasis.

**Se lo ganan:**
- El **titular del gancho**. La primera idea, la que decide si se quedan.
- La **palabra emocional** que la persona está diciendo en ese momento: `PERDIENDO`, `NUNCA`, `GRATIS`.
- El **nombre del producto** cuando aparece por primera vez.
- El **precio**, si la pieza es de oferta (ver `379`).

**No se lo ganan:**
- Los textos de servicio: llamado a la acción, letra legal, horarios, dirección.
- Las palabras de una cascada larga (con excepción, ver §6).
- Cualquier texto que necesite leerse **rápido y completo**. Ocluir cuesta tiempo de lectura.

Criterio de decisión en una frase: **si la palabra tiene que ser sentida, va detrás; si tiene que ser
leída, va delante.**

---

## 3. La regla de oclusión: cuánto se puede tapar

El dato práctico que nadie dice: una palabra tapada parcialmente sigue leyéndose **si se cumplen tres
cosas**.

1. **Queda visible al menos el 60% del ancho de la palabra.** Por debajo de eso el cerebro no puede
   completar y el espectador se frustra.
2. **La primera letra está visible, siempre.** Reconocemos las palabras mucho por su arranque y por su
   silueta general; si tapas el inicio, la palabra deja de ser recuperable. Tapar el final es tolerable;
   tapar el principio, no.
3. **La oclusión pasa por el medio, no por la altura.** Si la persona tapa la mitad *superior* de las
   letras, se pierde la parte que más información da (las mayúsculas se distinguen por arriba). Que tape
   verticalmente, no horizontalmente.

Traducido a composición: **la persona debe estar a un lado del cuadro y la palabra debe extenderse hacia
el otro lado, pasando por detrás del hombro o del torso, nunca por detrás de la cara.**

```
   ┌──────────────────────┐
   │        ▓▓▓▓          │   ▓ = persona
   │       ▓▓▓▓▓▓         │
   │  CE▓▓▓▓EZA           │   ← mal: tapa el medio y el arranque queda justo
   │      ▓▓▓▓▓▓▓         │
   └──────────────────────┘

   ┌──────────────────────┐
   │            ▓▓▓▓      │
   │           ▓▓▓▓▓▓     │
   │  CERVE▓▓▓▓▓▓         │   ← bien: arranque libre, oclusión al final
   │         ▓▓▓▓▓▓▓      │
   └──────────────────────┘
```

---

## 4. Las reglas del texto cambian cuando va detrás

Cinco cosas que hacías delante y que **no puedes hacer** detrás:

| Regla normal | Dentro del sándwich | Por qué |
|---|---|---|
| Entrada con desplazamiento | **Prohibido** | La palabra cruza el borde del recorte y ahí se ve la máscara sucia |
| Escala pequeña permitida | **Sube 20-30%** | Vas a perder ancho por oclusión; hay que compensar |
| Sombra opcional | **Contorno obligatorio, grueso** | El borde de la letra tiene que competir contra el borde de la persona |
| Salida seca | **Salida seca, sí** | Igual que siempre; Flash desactivado |
| Puede estar en cualquier sitio | **A la altura del torso** | Cara no, encima de la cabeza tampoco (queda de sombrero) |

La primera es la más importante y la que más gente rompe: **con sándwich, la entrada solo puede ser
Aparición progresiva.** Cualquier movimiento delata el recorte. Es una de las razones por las que tu
gramática de una sola animación de entrada es técnicamente correcta y no solo una preferencia (`375`).

---

## 5. El tiempo: el sujeto tiene que moverse

Aquí está la diferencia entre un sándwich que impresiona y uno que se ve como una calcomanía mal puesta:

> **El efecto no vive en el recorte. Vive en el movimiento del sujeto contra el texto quieto.**

Si la persona está totalmente inmóvil, el sándwich se ve como si hubieras pegado la palabra alrededor de
una silueta —correcto, pero muerto—. Si la persona se mueve un poco —gesticula, se inclina, gira—, el
texto se revela y se oculta solo, y ahí el cerebro confirma la profundidad.

**Elige el momento así:**
- Busca en el material un tramo de **1,5 a 3 s** donde la persona tenga movimiento suave.
- Descarta los tramos donde se mueva **muy rápido**: ahí el recorte automático falla y se ven bordes
  fantasma.
- Descarta donde las manos crucen delante del torso: los dedos son lo que peor recorta cualquier
  algoritmo.

Duración del texto detrás: **1,5 a 3 s**. Menos de 1,5 y no da tiempo de leer una palabra ocluida. Más
de 3 y el ojo ve el borde del recorte, que nunca es perfecto.

---

## 6. Cascada detrás del sujeto (la versión difícil)

Se puede, y es de lo más impresionante que se logra con un celular. Requisitos:

- La persona ocupa **un tercio lateral** del cuadro (izquierda o derecha), no el centro.
- La columna de texto va en el tercio opuesto, y solo su borde interno pasa por detrás.
- Máximo **4 palabras**, no 6: la columna larga baja hasta la zona donde el cuerpo es más ancho y la
  oclusión se vuelve total.
- Alineación **al lado contrario del sujeto**: si la persona está a la derecha, la columna alineada a la
  izquierda.

Si el sujeto está centrado, no lo hagas. Reencuadra el plano (mueve el clip lateralmente en la pista 1 y
en la 3 **por igual**) o renuncia al sándwich para esa cascada.

---

## 7. En CapCut: el orden de pistas y lo que se rompe

Los tres detalles operativos que salvan la sesión:

1. **La pista de texto va en medio, no arriba.** Es contraintuitivo porque CapCut pone el texto arriba
   por defecto. Hay que bajarlo. Si el video se ve sin efecto, esto es el 80% de las veces.
2. **Las pistas 1 y 3 son el mismo archivo en el mismo tiempo.** Cualquier ajuste —recorte, velocidad,
   zoom, color— hay que hacerlo **en las dos**. Un zoom aplicado solo arriba desalinea el recorte y
   produce un fantasma en el borde.
3. **Si mueves el texto en el tiempo, no muevas los clips.** El texto es lo único que se reajusta.

En `draft_content.json` el orden lo determina el **`render_index`** de cada segmento: mayor índice, más
arriba. La pila queda así:

```
clip recortado   render_index: 30
TEXTO            render_index: 20
clip normal      render_index: 10
```

Al generar por código (`112`, `114`), el bug clásico es asignar al texto un índice mayor que al clip
recortado, "porque el texto siempre va arriba". Resultado: un proyecto que abre bien y no tiene ningún
efecto. Si vas a automatizar sándwiches, **valida el orden de índices antes de escribir el archivo.**

Otro detalle: los dos clips de video deben compartir exactamente el mismo `target_timerange` y el mismo
`source_timerange`, en **microsegundos**. Un microsegundo de diferencia no se ve; mil sí.

---

## 8. Cuándo NO vale la pena

El sándwich cuesta entre 3 y 8 minutos por uso, entre recortar, alinear y corregir bordes. No siempre lo
vale:

- **Plano oscuro o de bajo contraste.** El recorte automático necesita separar al sujeto del fondo; si el
  fondo es del mismo tono, el borde queda irregular y se ve peor que sin efecto.
- **Pelo suelto, gorra, humo, vapor.** Todo lo que tiene borde complejo. Un vapor de cocina detrás de la
  cabeza destruye cualquier recorte.
- **Movimiento rápido.** El recorte va un fotograma atrasado y se ve un halo.
- **Sujeto centrado y palabra larga.** Vas a tapar el arranque, y ahí ya no se lee.
- **Texto de servicio.** El llamado a la acción tiene que leerse limpio, no sentirse profundo.
- **Cuando el video ya tiene tres sándwiches.** Deja de ser efecto y pasa a ser el estilo, y entonces
  nada destaca.

**La prueba honesta:** exporta el fotograma con sándwich y el mismo sin sándwich, ponlos lado a lado en
el celular. Si tienes que mirar dos veces para ver la diferencia, no valía la pena y acabas de ahorrarte
cinco minutos.

---

## 9. Diagnóstico rápido de fallas de texto

| Síntoma | Causa | Arreglo |
|---|---|---|
| No se ve ningún efecto | El texto está en la pista de arriba | Bájalo al medio |
| Se ve un halo alrededor de la persona | Los dos clips no están alineados | Alinéalos al fotograma |
| El borde parpadea | Recorte fallando por movimiento rápido | Cambia de tramo |
| La palabra no se entiende | Se tapó el arranque | Mueve el texto lateralmente |
| Se ve la máscara al entrar el texto | La entrada tiene desplazamiento | Cambia a Aparición progresiva |
| El texto "flota" y no se siente detrás | El sujeto está inmóvil | Elige un tramo con movimiento |
| Se ve como sombrero | El texto está encima de la cabeza | Bájalo a la altura del torso |

---

## Errores comunes

1. **Dejar el texto en la pista de arriba.** El error número uno, y produce cero efecto.
2. **Tapar la primera letra de la palabra.** Deja de ser recuperable para el cerebro.
3. **Dejar visible menos del 60% del ancho.** Frustra en vez de intrigar.
4. **Poner el texto detrás de la cara.** Nunca. Torso u hombro.
5. **Entrada con desplazamiento**, que arrastra la palabra por el borde del recorte y muestra la máscara.
6. **No subir el tamaño.** Detrás del sujeto se pierde ancho: hay que compensar 20-30%.
7. **Ajustar zoom o velocidad en un solo clip** de los dos. Desalineación y fantasma.
8. **Elegir un tramo donde el sujeto no se mueve.** El efecto queda muerto.
9. **Elegir un tramo con manos cruzando el torso.** Los dedos son lo que peor recorta.
10. **Cascada de 6 palabras con sujeto centrado.** La mitad inferior queda tapada por completo.
11. **Usarlo para el llamado a la acción.** Ese texto tiene que leerse limpio.
12. **Tres o más sándwiches por video.** Deja de destacar y solo suma tiempo de trabajo.
13. **`render_index` del texto mayor que el del clip recortado** al generar por código: proyecto sin
    efecto que parece correcto.
14. **Dejar el texto más de 3 s** detrás: da tiempo de ver los defectos del borde.

---

## Checklist

- [ ] Máximo 2 sándwiches con texto en toda la pieza
- [ ] La palabra elegida es de las que se sienten, no de las que se leen rápido
- [ ] La pista de texto está en medio de los dos clips de video
- [ ] Los dos clips de video son el mismo archivo, alineados al fotograma
- [ ] Cualquier zoom, recorte o color está aplicado igual en los dos clips
- [ ] La primera letra de la palabra queda visible
- [ ] Al menos el 60% del ancho de la palabra queda visible
- [ ] El texto está a la altura del torso, no de la cara ni encima de la cabeza
- [ ] La entrada es Aparición progresiva, sin desplazamiento
- [ ] El tamaño está 20-30% por encima de lo normal
- [ ] El tramo elegido tiene movimiento suave del sujeto, sin manos cruzando
- [ ] El texto dura entre 1,5 y 3 s
- [ ] Comparé el fotograma con y sin sándwich y la diferencia se nota a la primera
- [ ] Si generé por código, validé que `render_index` del texto está entre los dos clips
