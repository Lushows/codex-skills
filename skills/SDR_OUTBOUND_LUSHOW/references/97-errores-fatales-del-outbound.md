# 97 — Errores fatales del outbound (el anti-manual)

Este es el módulo al revés: no lo que debes hacer, sino **lo que mata campañas enteras**. Importa porque en outbound la mayoría de los fracasos no vienen de no saber una táctica avanzada, sino de cometer uno de un puñado de errores fatales que echan a perder todo el sistema — a veces de forma irreversible (un dominio quemado no se recupera fácil). Aprender el anti-manual te ahorra meses de "el outbound no funciona" cuando el problema era evitable. Cada error aquí es de los que hacen que **nada de lo demás importe**: la mejor lista y el mejor copy no sirven si cometes el #1. Úsalo como checklist antes de lanzar y como diagnóstico cuando algo se cae.

## El principio: en outbound, un error fatal anula todo lo bueno

El outbound es una cadena: lista → datos → deliverability → copy → cadencia → calificación (ver `39`, `98`). La cadena **se rompe por el eslabón más débil**. Puedes tener nueve pasos perfectos, pero si mandas desde tu dominio principal y lo quemas, cero resultado. Por eso estos errores son "fatales" y no "mejorables": no restan un poco, **anulan**. La disciplina de evitarlos vale más que cualquier truco de optimización.

## Los errores fatales, ordenados por daño

### 1. Mandar cold email desde tu dominio principal
El más caro y el más común. Un lote de fríos quema la reputación de tu dominio real y dejas de recibir hasta los correos de tus clientes. **Nunca.** Dominios secundarios con warmup, siempre (ver `41`, `43`). Daño: irreversible o costosísimo.

### 2. Saltarse la autenticación y el warmup
Enviar sin SPF/DKIM/DMARC (ver `42`) o sin calentar los buzones (ver `43`) = directo a spam desde el correo uno. Toda tu campaña existe pero nadie la ve. Daño: 100% del esfuerzo perdido, invisible (crees que "no responden").

### 3. Lista mala (targeting equivocado)
Mensaje perfecto a la persona equivocada = ruido + quejas de spam que hunden tu reputación (ver `40`). **30 cuentas que encajan > 3.000 al azar** (ver `10`, `20`). Comprar listas y mandarles en frío es la versión extrema: bounces + quejas destruyen la reputación en un día (ver `28`, `49`).

### 4. Spray-and-pray (volumen sin relevancia)
Miles de correos genéricos idénticos. Está muerto en 2026: quema dominios, marca y reputación, y convierte casi en cero. El outbound que funciona es **relevancia a escala, no spam a escala** (ver `07`, `52`, `66`). Daño: reputación + marca.

### 5. "Personalización" falsa
Creer que "Hola {nombre}" es personalizar. No lo es. La personalización es una línea que **prueba que investigaste su cuenta** (ver `52`, `53`). Un merge-field con el nombre en una plantilla genérica se nota y no mueve la aguja.

### 6. Pedir la venta en el primer toque
El outbound no cierra: **agenda una micro-conversación** (ver `55`). "¿Compras mi producto?" en el correo uno espanta. El CTA es de interés/reunión, no de compra. El cierre viene después y es otro oficio → `ventas_lushows`.

### 7. No hacer follow-up
La mayoría de las respuestas llegan en el toque 2–5, no en el primero. Mandar un solo correo y rendirse tira a la basura el 60–70% de los resultados posibles (ver `60`, `63`). Un solo toque no es una cadencia.

### 8. Un solo canal
Solo email o solo WhatsApp deja conversiones sobre la mesa. Email + LinkedIn + teléfono + WhatsApp entrelazados convierten mucho más (ver `61`). Monocanal = techo bajo.

### 9. Pasarle leads basura al vendedor
Un SDR que pasa leads que no encajan destruye la confianza del vendedor y el forecast. Un "no" rápido vale más que un "tal vez" eterno (ver `70`, `78`). Califica duro o rompes el handoff (ver `73`).

### 10. No medir (o medir lo que no importa)
Medir "correos enviados" en vez de respuestas positivas y reuniones. Sin las métricas correctas no sabes qué arreglar y "optimizas" a ciegas (ver `80`, `83`). Números que deban ser exactos → `Matematicas_lushows`.

### 11. Ignorar la ley
Listas compradas ilegales, sin opt-out, sin respetar Habeas Data (Colombia), GDPR o CAN-SPAM. Multas reales y reputación destruida (ver `49`, `181`). El ahorro no compensa el riesgo.

### 12. Rendirse antes de tiempo
Warmup toma 2–4 semanas; una campaña necesita semanas para dar señal estadística. Apagar todo al día 3 porque "no funciona" es abandonar antes de que el sistema arranque. Outbound es un sistema que madura, no una lotería instantánea.

## Checklist anti-fatal (antes de lanzar)

```
[ ] ¿Envío desde dominio SECUNDARIO, no el principal?      (err 1)
[ ] ¿SPF + DKIM + DMARC configurados y verificados?        (err 2)
[ ] ¿Buzones calentados 2–4 semanas?                       (err 2)
[ ] ¿La lista encaja con el ICP escrito? ¿Verificada?      (err 3)
[ ] ¿El mensaje sería relevante SOLO para este prospecto?  (err 4,5)
[ ] ¿El CTA pide una reunión/interés, no la venta?         (err 6)
[ ] ¿Tengo 3–6 toques en la cadencia, multicanal?          (err 7,8)
[ ] ¿Tengo criterio de calificación antes del handoff?     (err 9)
[ ] ¿Mido reply positivo y reuniones, no envíos?           (err 10)
[ ] ¿Cumplo la ley de datos del país? ¿Opt-out real?       (err 11)
```

## Siguiente paso

Corre el checklist contra tu campaña actual antes del próximo lanzamiento. Si ya estás en problemas, cruza tus síntomas con el diagnóstico por métrica (ver `83`) para ubicar qué error fatal estás cometiendo. El compilado exhaustivo de anti-patrones (incluyendo los del equipo y la agencia) está en `196`. Para construir el sistema que evita todo esto por diseño ver `98`.
