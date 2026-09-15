# 134 · Bancos de música: la letra pequeña

**Qué resuelve:** la idea de que «libre de derechos» y «gratis» significan «sin riesgo».
Ninguna de las dos cosas lo significa. Un banco de música no te regala una obra: te da
una **licencia**, y una licencia es un contrato con condiciones, con caducidad y con
alguien al otro lado que puede reclamarte tu propio vídeo.

> ⚖️ **Esto no es asesoría legal.** Las cláusulas concretas cambian de un banco a otro y
> de un año a otro. Lo único que vale es **leer la licencia que te dan a ti, en la fecha
> en que la aceptas, y guardarla**.

---

## Qué significan de verdad las etiquetas

| Etiqueta | Lo que la gente entiende | Lo que suele significar |
|---|---|---|
| *Royalty-free* / «libre de derechos» | «no tiene derechos» | tiene dueño; pagas una vez y no pagas **regalías por uso**. Sigue siendo una licencia |
| «Gratis» | «puedo hacer lo que quiera» | licencia gratuita **con condiciones** (atribución, ámbito, usos prohibidos) |
| «Sin copyright» | «dominio público» | casi nunca. Suele ser una licencia permisiva… o material subido por un tercero sin comprobar |
| «Uso comercial permitido» | «permitido todo» | permitido **ese** uso comercial, dentro del ámbito que define la licencia |

## Las seis cláusulas que muerden

1. **Atribución obligatoria.** Si no pones el crédito exacto —en el formato que pidan y
   donde lo pidan— la licencia deja de cubrirte. Es la más fácil de incumplir sin darse
   cuenta: nadie revisa la descripción de un vídeo de hace ocho meses.
2. **Licencia por proyecto, no por canal.** Muchas te cubren *el vídeo en el que la
   usaste*, no todo lo que subas. Reutilizar la misma pista en diez episodios puede
   requerir diez licencias.
3. **Revocabilidad y suscripción.** Si el banco funciona por suscripción, hay que mirar
   qué pasa con lo ya publicado cuando cancelas. Algunos mantienen cubiertos los vídeos
   publicados durante la vigencia; otros no. **No lo asumas: búscalo y guarda la
   captura.**
4. **Territorio y medio.** Puede excluir publicidad, cine, televisión, o limitar
   países.
5. **Uso no independiente.** Suele prohibirse distribuir la pista *como pista* —
   recopilarla, revenderla, subirla suelta. Un episodio no es eso, pero un *corte de
   solo música* sí puede serlo.
6. **Sin sublicencia.** No puedes pasarle la pista a un colaborador para que la use en
   lo suyo aunque trabaje para ti.

## La trampa del banco que te reclama a ti

Esta es la que sorprende a todo el mundo: **muchos bancos registran su propio catálogo
en Content ID**. Es razonable desde su lado —así detectan a quien usa sus pistas sin
licencia— y significa que tu vídeo, licencia en mano, recibe una reclamación automática
(§ 132).

La solución que ofrecen es registrar el **ID de tu canal** en su lista blanca. Funciona,
con tres letras pequeñas:

- Hay que hacerlo **antes** de publicar, o llega la reclamación igual.
- Cubre **ese** canal: si abres un segundo canal, o publicas en un canal de otro idioma,
  vuelve a empezar.
- Si el vídeo se resube o se reutiliza el audio en un corte vertical, puede volver a
  saltar.

Es decir: aunque hagas todo bien, el uso de un banco **añade un trámite recurrente y un
punto de fallo permanente** a cada publicación.

## El riesgo que no se ve: la cadena de arriba

Un banco gratuito que acepta subidas de usuarios **no comprueba de dónde salió cada
pista**. Si un usuario subió música que no era suya y tú la usas, el titular real
reclama a tu vídeo, no al banco. La licencia que tienes no vale más que el derecho de
quien te la dio, y si quien te la dio no tenía ninguno, no tienes nada.

Señales de que un banco no es de fiar:
- No dice quién compuso cada pista.
- No hay una página de licencia con fecha y versión.
- La licencia está en una imagen o en un vídeo de YouTube en vez de en un texto.
- «Sin copyright» en el título del archivo, y nada más.
- Las pistas se parecen sospechosamente a temas comerciales conocidos.

## Por qué el canal no usa bancos

Paper Empires sintetiza su música (§ 135). No es purismo: es que el banco **no elimina
ninguno de los problemas de arriba, solo los traslada a un contrato que hay que
administrar para siempre**. Con la síntesis, la grabación es nuestra y no hay contrato
que administrar.

## Si alguna vez entrara una pista de banco

El procedimiento mínimo, sin excepciones:

```
1. PDF de la licencia, descargado el día de la compra, con la versión y la fecha.
2. Captura de la página del producto: título de la pista, autor, ID interno.
3. Correo de confirmación guardado en el proyecto, no en el buzón.
4. El ID del canal registrado en la lista blanca del banco, con captura.
5. Entrada en audio/pistas.json con origen = banco y ruta al PDF (§ 138).
6. El crédito exacto en la descripción del episodio, copiado literal.
```

Si cualquiera de los seis no se puede cumplir, la pista no entra.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Entender «libre de derechos» como «sin dueño» | Se usa material licenciado como si fuera propio |
| Guardar el enlace de la licencia en vez del PDF | La página cambia y no queda prueba de lo que aceptaste |
| Reutilizar una pista licenciada por proyecto en varios episodios | Uso fuera de ámbito en todos menos en uno |
| Olvidar la atribución | La licencia deja de cubrirte, con licencia pagada |
| No registrar el canal en la lista blanca del banco | Reclamación sobre material que sí licenciaste |
| Cancelar la suscripción sin leer qué pasa con lo publicado | Catálogo entero potencialmente descubierto |
| Bajar pistas de un agregador gratuito con subidas de usuarios | Tu vídeo responde por un robo que hizo otro |
| Disputar la reclamación del banco en vez de escribirle | Se pelea contra quien te dio la licencia |

## Relacionado

`132` Content ID · `133` reclamaciones · `135` sintetizar es la garantía ·
`138` registrar lo propio · `139` lo que nunca entra
