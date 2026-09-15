# 133 · Reclamaciones: qué hacer

**Qué resuelve:** el procedimiento del día en que llega una. No el consejo de «no te
preocupes», sino la secuencia exacta, qué se decide en cada paso y por qué disputar sin
pruebas es la peor de las opciones disponibles.

> ⚖️ **Esto no es asesoría legal.** Los plazos y los nombres de los botones los cambia
> YouTube; las cifras de este módulo están verificadas contra la ayuda oficial a fecha
> de hoy y hay que volver a comprobarlas antes de usarlas. Una disputa es una
> **declaración legal** por tu parte: si el caso es serio, abogado.

---

## Lo primero: distinguir qué te ha llegado

| Llega | Qué es | Riesgo para el canal |
|---|---|---|
| **Reclamación de Content ID** | coincidencia automática (§ 132) | ninguno de por sí: no es una falta |
| **Retirada por derechos de autor** | alguien la presentó a mano | **falta**; varias cierran el canal |

Casi todo lo que llega es lo primero. Todo lo que puede matar el canal es lo segundo, y
**la vía más habitual para pasar de lo primero a lo segundo es escalar una disputa que
no puedes sostener**. Ese es el punto entero de este módulo.

## Las políticas que puede aplicar el reclamante

| Política | Qué le pasa a tu vídeo | Qué le pasa a tu dinero |
|---|---|---|
| **Monetizar** | sigue visible, con anuncios | los ingresos van al reclamante |
| **Rastrear** | sigue visible e igual | nada: solo mide |
| **Bloquear** | no se ve (puede ser solo en ciertos países) | cero |
| **Silenciar** | se ve sin ese audio | según cómo quede el resto |

Pueden aplicarse **por país**: un vídeo monetizado por ti en un sitio y bloqueado en
otro. Al leer la reclamación hay que mirar el territorio, no solo la política.

## La secuencia, paso a paso

```
1. LEER            qué segmento (marca de tiempo) y qué obra reclaman.
                   Sin eso no se decide nada.
2. IDENTIFICAR     buscar ese segmento en audio/pistas.json (§ 138).
                   ¿Es música nuestra, un efecto nuestro, archivo, o
                   algo cuya procedencia no sabemos escribir?
3. DECIDIR         una de las cuatro salidas de abajo.
4. REGISTRAR       la reclamación, la decisión y el resultado en el
                   cuaderno del episodio. Se repiten.
```

### Las cuatro salidas

| Situación | Qué se hace |
|---|---|
| **La pista es nuestra y hay registro** (script, parámetros, fecha, hash) | Se disputa, adjuntando cómo se generó. Es el único caso en que disputar es la jugada correcta |
| **Venía de un banco con licencia** | No se disputa en caliente: primero se registra el canal en la lista blanca del banco y se pide al banco que libere la reclamación (§ 134) |
| **Es archivo con ficha de licencia** | Se disputa **solo** si la ficha cubre el fonograma, no únicamente la obra (§ 130, § 137) |
| **No sabemos de dónde salió** | **No se disputa.** Se quita o se sustituye el audio y se sigue trabajando |

La cuarta es la que cuesta tragar y la que más canales salva. YouTube permite quitar o
silenciar el segmento reclamado sin volver a subir el vídeo: se pierde el audio, no el
vídeo ni su historial.

## Los plazos (verificados hoy, comprobar antes de usar)

- **Disputa:** el reclamante tiene **hasta 30 días** para responder. Si no responde, la
  reclamación caduca y se libera.
- **Apelación** (si rechaza la disputa): el reclamante tiene **7 días**. Puede liberar,
  mantener, o **presentar una retirada** — y ahí es donde aparece la falta.
- **Dinero:** si disputas **dentro de los 5 primeros días**, los ingresos se retienen
  desde el primer día de la reclamación; si disputas después, se retienen desde la fecha
  de la disputa. Se guardan aparte y se pagan a quien gane.

Fuentes: [Disputar una reclamación de Content ID](https://support.google.com/youtube/answer/2797454) ·
[Apelar una reclamación](https://support.google.com/youtube/answer/12104471) ·
[Monetización durante las disputas](https://support.google.com/youtube/answer/7000961).

Consecuencia práctica del último punto: **disputar rápido no es agresividad, es
recuperar el dinero desde el día uno**. Pero solo si se va a ganar.

## Por qué disputar sin pruebas es mala idea

1. **Es una declaración.** Estás afirmando formalmente que tienes derecho. Si no lo
   tienes, lo has dejado por escrito.
2. **Sube la escalera.** Disputa → apelación → el reclamante puede responder con una
   retirada, y una retirada es una falta. Se cambia un riesgo de cero por uno real.
3. **Congela el dinero** durante todo el proceso, que puede durar semanas.
4. **Te marca.** Un canal que dispara disputas que pierde no juega a favor de sí mismo
   en el trato futuro con la plataforma. ⚠️ *No conozco los criterios internos de
   YouTube al respecto y no los voy a describir: lo que sí es seguro es que la retirada
   al final del camino es real.*

Regla corta: **se disputa con el archivo de origen en la mano, o no se disputa.**

## El valor del registro (y por qué existe § 138)

Ganar una disputa sobre una pista sintetizada es fácil **si el registro existía antes**:
el script que la generó, los parámetros, el comando de ffmpeg, la fecha y el hash del
archivo resultante. Eso es prueba reproducible: cualquiera puede volver a ejecutarlo y
obtener el mismo audio.

Ganar esa misma disputa **sin** registro es afirmar «es mía» y esperar. Es la misma
frase que dice todo el que sube música ajena.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Disputar el mismo día, molesto, sin mirar el registro | Se escala una reclamación inofensiva hacia una falta |
| Contestar con argumentos morales o de uso legítimo sin base | No hay nadie leyendo en esa fase; es un formulario |
| No mirar la marca de tiempo reclamada | Se discute sobre una pista que ni siquiera está ahí |
| Dejar la reclamación «para luego» | Los ingresos solo se retienen desde la fecha de la disputa |
| Borrar el vídeo para «limpiar» | Se pierde el historial y la reclamación deja de poder resolverse |
| Volver a subir el vídeo con el audio cambiado | Se pierden vistas y posicionamiento; se podía silenciar el segmento |
| Disputar una pista de banco antes de hablar con el banco | El banco es el reclamante: la disputa va contra quien te licenció |
| No anotar qué pasó | La siguiente reclamación se afronta desde cero otra vez |

## Relacionado

`132` Content ID · `134` bancos de música · `135` sintetizar es la garantía ·
`138` registrar lo propio · `139` lo que nunca entra
