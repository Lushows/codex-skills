# 186 — Portafolio de video

Un portafolio no es una colección de tus mejores trabajos. Es una herramienta de venta con un solo
trabajo: hacer que el cliente correcto piense *"esta persona resuelve mi problema"* en menos de un
minuto.

Casi todos los portafolios de editores fallan por lo mismo: son un demo reel bonito que demuestra
habilidad y no demuestra utilidad. Este módulo es qué mostrar, cómo mostrarlo, y por qué un caso de
estudio con tres números vende más que el reel más espectacular que hayas montado.

---

## Qué está evaluando el cliente de verdad

No está evaluando si sabes editar. Asume que sabes editar; por eso te escribió. Está evaluando tres
cosas, en este orden:

1. **¿Esta persona ha resuelto algo parecido a lo mío?** (relevancia)
2. **¿Le sale bien de forma consistente o tuvo suerte una vez?** (confiabilidad)
3. **¿Le sirvió a alguien, o solo se ve bonito?** (resultado)

Un demo reel de 90 segundos con 40 cortes espectaculares responde ninguna de las tres. Responde una
cuarta pregunta que nadie hizo: "¿sabes hacer cosas impresionantes?".

---

## La regla de la relevancia sobre la calidad

**Un video mediano del rubro del cliente vende más que un video excelente de otro rubro.**

El dueño de restaurante que ve tu pieza espectacular para una marca de ropa no piensa "qué talento".
Piensa "esto no se parece a lo mío" y no logra imaginarse en tu trabajo.

Por eso el portafolio se organiza **por problema del cliente**, no por técnica ni por cronología:

```
❌ Mal:  Motion Graphics · Corrección de color · Documental · Comercial
✅ Bien: Restaurantes · Software B2B · Educación en línea · Marca personal
```

Si tienes un solo nicho (`183`), mejor todavía: un portafolio de un solo rubro, profundo.

---

## Qué mostrar

### La estructura mínima que funciona

**5 a 8 piezas. No más.**

Un portafolio de 25 videos no demuestra experiencia: demuestra que no sabes cuáles son buenos. Y nadie
ve 25 videos. Ven dos y medio.

| Cantidad | Qué | Por qué |
|---|---|---|
| 3–4 | Piezas del nicho que quieres vender | relevancia |
| 1–2 | Casos de estudio con números | resultado |
| 1 | Antes/después de un rescate | demuestra criterio, no equipo |
| 1 | Algo tuyo, personal, con carácter | demuestra que tienes ojo propio |

### El demo reel: cuándo sí y cuándo no

**No sirve para:** vender servicios de contenido a un negocio. El dueño de restaurante no sabe qué
mirar en un montaje de cortes rápidos con música épica.

**Sí sirve para:** que te contrate una productora, una agencia o un director. Ellos sí leen un demo
reel, porque saben ver oficio en 20 segundos.

Si haces uno: **45 a 60 segundos, no 3 minutos**. Los primeros 5 segundos deben ser tu mejor trabajo,
no una intro con tu logo. Nadie ve el minuto 2.

### El antes/después: la pieza más subestimada

Muestra el material bruto (10 segundos, con su audio feo, su encuadre chueco, su plano largo) y después
el resultado. Pantalla dividida o secuencial.

**Por qué funciona tan bien:** demuestra que el valor lo pusiste tú y no la cámara. El cliente que tiene
material feo de celular — o sea, casi todos — se ve reflejado ahí de inmediato.

```bash
# Antes/después en pantalla dividida vertical, 9:16
ffmpeg -i bruto.mp4 -i final.mp4 -filter_complex \
"[0:v]scale=1080:960:force_original_aspect_ratio=increase,crop=1080:960[a];\
 [1:v]scale=1080:960:force_original_aspect_ratio=increase,crop=1080:960[b];\
 [a][b]vstack=inputs=2[v]" \
-map "[v]" -map 1:a -c:v libx264 -crf 20 -pix_fmt yuv420p antes_despues.mp4
```

---

## El caso de estudio: lo que de verdad sube tu precio

Esta es la diferencia entre un editor que cobra $250.000 por reel y uno que cobra $800.000. No es la
calidad del corte. Es que uno puede demostrar que su trabajo produjo algo.

### La estructura, en 6 bloques

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BENDITA POLA — de 400 a 3.100 vistas promedio en 8 semanas

1. EL PROBLEMA
Publicaban 3 veces por semana y promediaban 400 vistas. El contenido era bueno
pero los videos arrancaban con el logo del bar y una panorámica del local.

2. QUÉ ENCONTRÉ
Revisé las 30 publicaciones anteriores. Los 4 videos que sí funcionaron tenían
algo en común: arrancaban con comida en primer plano y sonido real, sin música.
El resto arrancaba con marca.

3. QUÉ HICE
- Movimos el gancho: primer plano de comida o de gente, siempre en el segundo 0
- Sacamos el logo del arranque y lo pusimos en el remate
- Subtítulos siempre, porque el 82% ve sin sonido
- Sonido ambiente real por encima de la música
- Un solo llamado a la acción, y el mismo durante 8 semanas

4. EL RESULTADO
Vistas promedio:        400  →  3.100
Retención a 3 s:        41%  →  68%
Mensajes por WhatsApp:  2/sem → 11/sem
Reservas atribuidas:    0    →  14 en el mes 2

5. QUÉ APRENDÍ
El logo al principio le costaba al bar un 25% de la retención. Era la decisión
que más quería el dueño y la que más le estaba costando.

6. QUÉ DIJO EL CLIENTE
"Llevábamos un año publicando sin que pasara nada."  — [nombre], dueño
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Por qué esto vende diez veces más que un reel bonito

- **El bloque 2 demuestra criterio.** Cualquiera monta; pocos investigan antes de montar. Ese bloque es
  la prueba de que piensas, y el pensamiento es lo caro en 2026 (`189`).
- **El bloque 4 son números.** Un número es verificable; un adjetivo no. "Quedó espectacular" no
  significa nada; "retención de 41% a 68%" sí.
- **El bloque 5 te vuelve un asesor.** El que aprende del proyecto es alguien con quien vale la pena
  trabajar el año entrante.

### Cómo conseguir los números si nunca los has pedido

Empieza hoy. En cada entrega (`181`, paso 7):

> Cuando publiques, a los 3 días mándame captura de las estadísticas: vistas, retención y mensajes
> recibidos. Con eso ajusto el gancho del próximo. Es la única forma de que esto mejore mes a mes en
> vez de que sea una lotería.

Estás pidiendo un dato que te sirve para trabajar mejor. Es verdad, y además te construye el caso.

**Si el cliente no comparte números:** usa lo que sea público. Vistas, comentarios, guardados. Y pide
una frase de testimonio, que siempre la dan.

**Nunca inventes un número.** Un caso de estudio con datos falsos es una bomba de tiempo: llega el
cliente que sí pregunta detalles y se cae todo, incluida tu reputación en un mercado que es pequeño.

---

## Cómo mostrarlo

### Dónde vive el portafolio, por prioridad

1. **Instagram / TikTok.** Para venderle a negocios, es el portafolio principal. Es donde el cliente
   ya está y donde puede ver el trabajo en el mismo formato en que va a vivir. **Publica el trabajo
   de tus clientes en tu propio perfil** (con permiso), no solo tips.
2. **Una página de una sola pantalla.** 5 videos incrustados, 2 casos de estudio, precios de los
   paquetes (`184`), botón de WhatsApp. Nada más. Se hace en un día.
3. **Un PDF o presentación** para clientes corporativos y agencias, con los casos de estudio completos.
4. **Un Drive ordenado** para mandar rápido por WhatsApp cuando alguien pregunta.

**Lo que no necesitas:** Behance, Vimeo Pro, un sitio con animaciones de scroll. Nada de eso está donde
tu cliente busca.

### Reglas de presentación

- **Los videos se ven en el formato en que se publicaron.** Un reel vertical embebido en un marco
  horizontal negro se ve amateur y comunica que no entiendes el medio.
- **Autoplay sin sonido, con subtítulos.** Como en la vida real.
- **Cada pieza con una línea de contexto:** *"Reel para restaurante · objetivo: reservas entre semana ·
  68% de retención a 3 s"*. Sin contexto, el cliente no sabe qué está mirando ni qué juzgar.
- **Carga rápido o no existe.** Comprime bien (`93`). Un portafolio que tarda 6 segundos en cargar
  pierde a la mitad de la gente.
- **Un botón de contacto visible siempre.** El momento de mayor intención es justo después del segundo
  video, no al final de la página.

### El orden importa

La primera pieza es la que decide si ven la segunda. **Pon primero la más relevante para el cliente que
quieres, no la que más te enorgullece.** Si sabes con quién vas a hablar, reordena antes de mandar. Un
portafolio en Drive con carpetas por rubro te permite mandar exactamente lo que corresponde.

---

## Portafolio sin clientes

El problema del principio. Tres salidas, todas legítimas:

### 1. Trabajo especulativo con material real

Baja el material público de un negocio (sus propios videos de Instagram), reedítalo y publícalo
marcándolo claramente como ejercicio. Sirve de portafolio y de prospección al tiempo (`183`).

### 2. Tus propios negocios

Si tienes un bar-restaurante o cualquier negocio propio, es tu mejor cliente cero. Tienes acceso total,
puedes medir de verdad y puedes contar el caso completo con números reales sin pedir permiso a nadie.

### 3. Un proyecto propio con intención

No un "video artístico". Un formato con hipótesis: *"probé si un gancho de pregunta retiene más que uno
de afirmación en 6 videos del mismo tema"*. Eso demuestra exactamente lo que un cliente quiere comprar:
que piensas antes de cortar.

**Lo que NO cuenta como portafolio:** trabajo de curso, plantillas de CapCut rellenadas, ejercicios de
motion sin propósito, y videos de "tips de edición" (esos te traen audiencia de editores, no de
compradores).

---

## Mantenimiento

- **Revisa cada 3 meses.** Saca lo viejo. Un trabajo de hace tres años en el portafolio comunica que no
  has hecho nada mejor desde entonces.
- **Regla de reemplazo:** si entra una pieza, sale una. El portafolio no crece, mejora.
- **Cada proyecto bueno se documenta el mismo día que se entrega.** A los dos meses ya no te acuerdas
  de qué decidiste ni por qué, y el caso de estudio se vuelve genérico.
- **Guarda siempre:** el bruto original (10 segundos bastan), el corte final, la captura de resultados,
  la frase del cliente. Cuatro archivos por proyecto, en una carpeta con el nombre del cliente.
- **Pide permiso para publicar** antes de subir trabajo de un cliente. Casi siempre dicen que sí, pero
  algunos tienen acuerdos de confidencialidad. Déjalo escrito en el contrato desde el principio
  (`187`).

---

## Errores comunes

- **Portafolio organizado por técnica.** Al cliente no le importa que sepas motion. Le importa si has
  resuelto su problema.
- **Demasiadas piezas.** 25 videos comunican que no distingues cuáles son buenos. 6 bien elegidos
  comunican criterio.
- **Solo trabajos "impresionantes".** El cliente que tiene material de celular no se ve reflejado en un
  comercial con dron y steadicam.
- **Ningún número en ninguna parte.** Sin resultados, compites por gusto, y por gusto siempre gana el
  más barato.
- **Inventar los números.** Se cae en la primera conversación seria y en un mercado pequeño eso se
  sabe.
- **Demo reel para vender a negocios.** No lo saben leer. Sirve para agencias y productoras.
- **Reels verticales embebidos en marcos horizontales.** Comunica que no dominas el medio.
- **No pedir estadísticas al entregar.** Es el único momento en que el cliente las tiene a la mano y
  está contento.
- **Publicar trabajo de clientes sin permiso.** Riesgo legal real y daño de relación evitable.
- **No actualizar en años.** Un portafolio congelado dice que llevas años sin hacer nada bueno.
- **Contenido para editores en vez de para compradores.** Los tips de edición te traen colegas.

---

## Checklist

- [ ] El portafolio está organizado por problema/rubro, no por técnica
- [ ] Tiene entre 5 y 8 piezas, no 25
- [ ] La primera pieza es la más relevante para el cliente objetivo
- [ ] Cada pieza tiene una línea de contexto: objetivo y resultado
- [ ] Los videos verticales se ven verticales
- [ ] Tengo al menos 1 caso de estudio con la estructura de 6 bloques
- [ ] El caso de estudio tiene números reales y verificables
- [ ] Tengo al menos un antes/después que demuestre criterio sobre material feo
- [ ] Pido estadísticas y testimonio en cada entrega
- [ ] Tengo permiso escrito para publicar el trabajo de cada cliente
- [ ] El portafolio vive donde mi cliente está (Instagram, WhatsApp), no en Behance
- [ ] Hay botón de contacto visible desde el primer scroll
- [ ] Documento cada proyecto bueno el mismo día que lo entrego
- [ ] Reviso y reemplazo piezas cada 3 meses
