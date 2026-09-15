# 49 — Testing de creativos de video

Lee este módulo cuando tengas varios videos y no sepas cuál dejar corriendo, o cuando quieras mejorar un anuncio de YouTube/Demand Gen sin guiarte por "el que me gusta más a mí". En performance no se decide por gusto: se decide por datos. Pero el testing de video tiene una trampa — si cambias cinco cosas a la vez no sabes cuál movió la aguja, y terminas adivinando con cara de ciencia. Este módulo te da el método para testear limpio. La **creación de las variantes** (concepto, dirección de arte) es de `directorcreativo_lushows`; con IA/Gemini generas variaciones rápido (ver 91); aquí decides **qué** testear y **qué métrica manda**.

## Qué testear — de mayor a menor impacto

No todo pesa igual. Testea en este orden, porque así está el retorno:

| Prioridad | Variable | Por qué pesa tanto |
|---|---|---|
| 1 | **El hook (primeros 5s)** | Decide si te saltan o se quedan (ver 42). Es la palanca #1 |
| 2 | **El ángulo/promesa** | Qué problema atacas y cómo lo prometes cambia a quién enganchas |
| 3 | **Duración** | 15s vs 30s vs 60s rinden distinto según público y formato |
| 4 | **CTA** | Cómo y cuándo pides la acción (ver 45) |
| 5 | Detalles (música, color, voz, subtítulos) | Importan, pero mueven poco comparado con lo de arriba |

Empieza siempre por el **hook**: tres aperturas distintas del mismo video suelen separar más resultados que tres videos completamente distintos. Es el cambio más barato (recortas/cambias 5 segundos, o lo regeneras con Gemini, ver 91) y el de mayor efecto.

### Ejemplo de batería de hooks (GastroLatam)

```
Mismo video base, solo cambian los primeros 5s:
HOOK A (dolor):     "Vendes lleno y la plata no aparece. ¿Por qué?"
HOOK B (pregunta):  "¿Sabes cuánto te cuesta DE VERDAD cada plato?"
HOOK C (cifra):     "El 60% de los restaurantes no sabe su costo real."
→ Todo lo demás IDÉNTICO. Mide cuál trae chats WhatsApp más baratos (CPA).
```

## No contaminar variables — la regla de oro

"Contaminar variables" es cambiar varias cosas al tiempo de modo que no sabes cuál causó el cambio. Para testear limpio:

1. **Una variable por prueba.** Si testeas el hook, los videos deben ser **idénticos salvo el hook**. Mismo CTA, misma duración, misma oferta. Si cambias hook *y* duración a la vez, el resultado no enseña nada.
2. **Mismo entorno.** Misma audiencia, misma puja, mismo presupuesto, al mismo tiempo. Probar el video A esta semana y el B la otra los contamina (cambió el contexto, no solo el video).
3. **Suficiente data antes de decidir.** No mates un video con 200 impresiones; el dato es ruido. Regla práctica: espera al menos **~30 conversiones** o varios cientos de acciones por variante antes de declarar ganador. Decidir temprano es superstición, no testing.
4. **Cuidado con el aprendizaje del algoritmo.** En Demand Gen/YouTube con smart bidding (ver 13), el sistema reparte presupuesto entre assets; eso ayuda pero también significa que no es un A/B perfecto (le da más a lo que cree mejor, sesgando la muestra). Úsalo como dirección, no como verdad de laboratorio. Para rigor, los **experimentos de video de Google** (drafts & experiments) son la vía limpia: dividen audiencia 50/50 de verdad.

### Cuánta plata para un test válido

Orden de magnitud Colombia: si tu CPA por chat ronda $8.000 COP y quieres ~30 conversiones por variante, son ~$240.000 COP por variante. Con 3 hooks → ~$720.000 COP de presupuesto de test. Por debajo de eso, decides por azar. No corras un "test" de $50.000 y te creas el resultado.

## Dónde leer los datos: asset reporting

Demand Gen y las campañas de video traen **reportes de assets**: te muestran cómo rinde cada video, imagen y texto. Google los etiqueta (**Mejor / Bueno / Bajo**) y reparte más presupuesto a los que rinden. Úsalo así:

- Mira qué **video** acumula las acciones a menor costo, no cuál tiene más vistas.
- Quita los assets marcados "Bajo" tras suficiente data y reemplázalos por variaciones nuevas del ganador.
- Itera: el ganador de hoy se convierte en la base del próximo test (cambia un solo elemento y vuelve a medir).
- Ojo: la etiqueta de Google compara assets *dentro de la misma campaña*; un "Bajo" puede ser víctima de que el algoritmo nunca le dio impresiones suficientes. Cruza con volumen antes de matarlo.

## Qué métrica decide — y en qué orden

Aquí está el corazón del módulo. Las métricas de video engañan si las lees en el orden equivocado:

| Métrica | Qué mide | ¿Decide? |
|---|---|---|
| View rate | % que ve el video (no salta) | Solo señal de **hook**, no de venta |
| CTR | % que hace clic | Señal de interés, todavía no plata |
| **CVR** | % que convierte (lead/chat/venta) | Importa de verdad |
| **CPA** | Costo por acción (lead/venta) | **La que manda** |
| ROAS / CPA-venta (con OCI) | Costo por venta real, no por lead | La verdad final (ver 53) |

La verdad incómoda: un video puede tener **view rate altísimo y cero ventas** (gusta, entretiene, pero no vende). Por eso el orden es: *view rate* te dice si el hook funciona; *CVR* te dice si convierte; pero **quien decide qué video se queda es el CPA** — el costo real de conseguir un lead o una venta. Y si conectas las ventas offline (OCI, ver 53), el juez final es el **CPA por venta**, no por lead: un hook que trae muchos chats baratos pero ninguno compra pierde contra el que trae menos chats que sí cierran. Mata el video con view rate hermoso y CPA imposible; quédate con el video "feo" que trae leads que compran. El que paga la pauta es el resultado, no el aplauso.

## Plantilla de test limpio

```
TEST #___  FECHA: ___
VARIABLE TESTEADA (una sola): [ ] hook  [ ] ángulo  [ ] duración  [ ] CTA
VARIANTES: A "______"  B "______"  C "______"  (todo lo demás IDÉNTICO)
ENTORNO: misma audiencia ___ | misma puja ___ | mismo presupuesto ___ | mismo periodo ___
MÉTRICA QUE DECIDE: CPA por [chat/lead/venta]
DATA MÍNIMA: ~30 conversiones por variante (no decidir antes)
GANADOR: ______  → se vuelve la base del próximo test (itera 1 variable más)
```

## Errores comunes — blacklist

1. **Cambiar varias cosas a la vez.** Hook + duración + CTA juntos = no sabes qué funcionó. Una variable por prueba.
2. **Decidir con poca data.** 200 impresiones es ruido. Espera ~30 conversiones por variante o decidirás por azar disfrazado de dato.
3. **Elegir el video que "más me gusta".** Tu gusto no paga la pauta. Decide por CPA, no por estética.
4. **Confundir view rate con éxito.** Un video muy visto y sin ventas es entretenimiento caro. El view rate solo valida el hook.
5. **No empezar por el hook.** Es la palanca #1 y la más barata de cambiar. Testear música antes que hook es optimizar al revés.
6. **Probar A esta semana y B la otra.** El contexto cambió; los contaminaste. Corren al mismo tiempo, misma audiencia (o usa experimentos de Google para split limpio).
7. **No reciclar al ganador.** El test no termina: el ganador es la base del próximo. Iterar con variaciones (IA acelera, ver 91; concepto en `directorcreativo_lushows`).
8. **Optimizar a CPA por lead ignorando si cierran.** Sin OCI (ver 53), premias el hook que trae chats baratos que no compran. El juez es la venta, no el lead.
