# 49 — Testing de copy y ángulos

Cómo testear PALABRAS sin contaminar variables ni quemar plata: qué probar primero, con qué método, cuánto presupuesto y cómo guardar lo aprendido. Léelo antes de lanzar variantes de copy. El testing de creativos visuales vive en el 39; aquí es el texto y el ángulo. Regla madre: un test sin hipótesis ni criterio de decisión no es un test, es lotería con factura. La viabilidad económica del ganador (margen real, no solo CPA) se cierra con economist_lushows.

> **Snapshot jun-2026 (ver actualizacion-2026-06 §2, §6):** tres cosas que cambian cómo testeas copy. ① **Entity ID**: Meta colapsa creativos casi-iguales en una sola entidad que compite contra sí misma — testea **ángulos conceptualmente distintos**, no 10 variantes de la misma frase. ② **Vida útil del ad bajó a ~2-4 semanas** (antes 6-8): el ganador de hoy se fatiga más rápido, refresca más seguido. ③ **Meta quitó las ventanas view-through de 7/28 días del API (12-ene-2026)**: juzga por **7d-click / 1d-view**, no por view-through, sobre todo en retargeting/WhatsApp. ④ La **atribución incremental** reporta MENOS conversiones (las reales) — no te asustes si el número baja al activarla.

## Jerarquía: qué testear primero

De mayor a menor impacto. NO bajes de nivel hasta tener un ganador en el de arriba:

1. **ÁNGULO** (la razón de compra: foco para trabajar vs energía para entrenar vs regalo para papá — ver 38). Cambiar de ángulo puede mover el CPA 2-5×. Es donde está casi toda la plata.
2. **HOOK / primera línea** (mismo ángulo, distinta puerta de entrada — fórmulas en el 40).
3. **OFERTA** (mismo ángulo y hook, distinta estructura de oferta: con/sin garantía, bundle vs unidad — ver 41). Puede mover tanto como el ángulo.
4. **Estructura larga vs corta** (mismo ángulo y hook, distinto desarrollo).
5. **CTA y cierre** (ver 45).
6. **Detalles** (emojis, orden de bullets, palabra suelta). Casi nunca mueven nada: testéalos solo cuando lo demás está exprimido.

**Variar sinónimos no es un test.** "Recupera tu foco" vs "Recupera tu concentración" = la misma cosa dos veces; Meta repartirá impresiones al azar (y con Entity ID las colapsa) y tú leerás ruido como señal. Dos variantes son test solo si un cliente DISTINTO respondería a cada una.

## Método

- **Base limpia**: mismo visual + 3-5 primary texts que representen ángulos o hooks DE VERDAD distintos, en el mismo ad set, todo lo demás congelado (misma landing, misma oferta, mismo botón). **Una variable por test.**
- **Dynamic/flexible creative** (Meta combina textos, visuales y headlines automáticamente): útil para PRODUCIR combinaciones ganadoras en Advantage+, pero el reporting por variante es limitado — sabes que el CONJUNTO funcionó, no qué texto lo hizo. Para **LEER** resultados de copy: ads separados, un copy por ad, con UTM distinto por variante para verlas en analytics (setup de UTMs: ver 66).
- En la práctica: usa flexible para ESCALAR lo ya validado; usa ads separados para APRENDER.
- En la era Advantage+ (jun-2026), recuerda que el sistema quiere optimizar por ti — pero si lo que quieres es leer qué copy ganó, necesitas la separación manual. Automatización para escalar, separación para aprender.

## Presupuesto y criterio de decisión

- Regla mínima: **3-5× tu CPA objetivo gastado POR VARIANTE** antes de declarar ganador o perdedor (el marco completo de presupuestos de test: ver 17). Con CPA objetivo de $30.000 COP y 4 variantes, presupuesta ~$360.000-600.000 para el test completo.
- Matar antes solo con desastre evidente (gasto de 2-3× CPA y cero señal de compra/chat).
- **5 clics no deciden nada. 2 conversiones contra 1 tampoco.** Si no puedes financiar el criterio, testea MENOS variantes, no con menos datos. Dos ángulos bien medidos > cinco ángulos a medias.

## Qué mirar por capa (y no confundir señales)

| Capa | Métrica que la mide | Por qué |
|---|---|---|
| Hook / primera línea | CTR, thumbstop (3-sec views/impresiones) | Solo mide si DETUVO y dio clic |
| Copy completo + ángulo | CVR post-clic y CPA final | Un hook morboso da CTR alto y compras cero |
| Oferta | CPA + margen por pedido (ver 41) | Puede convertir y perder plata |
| CTWA | Ventas cerradas en chat, NO "conversaciones iniciadas" | El curioso infla la métrica (ver 46/53) |

**Nunca declares ganador por CTR solo**: el hook gana atención, el CPA gana plata. Un titular morboso ("lo que las marcas no quieren que sepas") puede tener el mejor CTR y cero ventas. Métricas y diagnóstico completo en 60-61. Si CTR sano + CVR muerta → sospecha congruencia ad-landing antes que copy (ver 48).

## La hoja de learnings (el activo real)

Cada test alimenta una hoja (sheet simple) que vive ENTRE campañas — el aprendizaje compuesto es lo que te separa del que empieza de cero cada mes:

| Fecha | Ángulo | Primera línea | Gasto | CPA | Margen/pedido | Resultado | Decisión |
|---|---|---|---|---|---|---|---|
| 12-jun | Foco oficinista | "La cabeza embotada a las 3pm..." | $180.000 | $24.000 | +$38.000 | Ganador (CPA -30%) | Escalar + variantes de hook |
| 12-jun | Regalo día del padre | "El regalo que no termina en un cajón" | $180.000 | $61.000 | +$1.000 | Perdedor | Matar; reintentar en temporada |
| 19-jun | Foco estudiante | "La noche antes del parcial..." | $200.000 | $29.000 | +$33.000 | Empate técnico | Mantener; testear hook nuevo |

Reglas de la hoja:
- Se escribe el MISMO día que se decide (la memoria edita).
- Los PERDEDORES se anotan igual que los ganadores (te ahorran repetirlos).
- Incluye **margen por pedido**, no solo CPA: un CPA bajo que pierde plata no es ganador (ver 41).
- Cada trimestre se relee antes de planear (ver 70).

## Reciclar ganadores fuera de ads

Una primera línea que ganó en subasta es lenguaje VALIDADO con plata real — exprímelo en todo el ecosistema:
- → **Headline del hero de la landing** de ese ángulo (se implementa con desingweb 17).
- → **Apertura del chat de WhatsApp / ice-breaker** para leads de ese ad (ventas 82, copy CTWA 46): si el ad que lo trajo decía "la cabeza embotada a las 3pm", el saludo que retoma esa frase convierte más.
- → Asunto de email/broadcast, descripción del producto, guion del próximo video UGC (ver 32).
- → Próximo ángulo de TikTok o Google si pautas multicanal (tiktok_ads / google_ads).

El testing de copy no es un gasto: es I+D de lenguaje que rinde en cada canal donde hablas.

## La fatiga del ganador (jun-2026)

Con vida útil del ad en ~2-4 semanas, ningún ganador es eterno. Síntomas de fatiga: CTR cae, CPA sube, frecuencia alta (ver 62). Cuando un ángulo gana, no lo dejes solo: testea **variantes de hook del mismo ángulo ganador** en paralelo, para tener el reemplazo listo antes de que el original muera. La hoja de learnings te dice qué ganador reintentar y cuándo (temporada, evento del calendario — ver 27/47).

## Flujo completo de un test de copy

1. Hipótesis: "El ángulo foco-oficinista venderá más barato que el ángulo energía-gym." (no "voy a probar copys").
2. Aterriza 3-4 primarios que sean ángulos/hooks DE VERDAD distintos (40/42).
3. Pásalos por claims (44) y localización (47).
4. Congela todo lo demás (visual, oferta, landing, botón). Una variable.
5. Presupuesta 3-5× CPA objetivo por variante (17).
6. Deja correr sin tocar durante la fase de aprendizaje (no mates a las 6h — ver 13).
7. Lee por la capa correcta (CPA + margen, no CTR solo).
8. Anota en la hoja el MISMO día. Escala el ganador, recicla su lenguaje, archiva el perdedor.

## Errores comunes — blacklist

- ❌ Testear emojis cuando nunca has testeado ángulos: optimizas la cortina con la casa sin paredes.
- ❌ Cambiar copy Y visual Y landing a la vez: ganó "algo", no sabes qué, no aprendiste nada.
- ❌ Declarar ganador con 2 conversiones contra 1, o por CTR sin mirar CPA.
- ❌ Variar sinónimos y llamarlo test (Entity ID los colapsa y lees ruido).
- ❌ Usar flexible creative para un test que necesitas LEER por variante.
- ❌ Matar variantes a las 6 horas "porque no arrancan" (fase de aprendizaje: ver 13).
- ❌ No anotar el resultado: en 3 meses repetirás el mismo test perdedor.
- ❌ Anotar CPA pero no margen: un CPA bajo que pierde plata por pedido no es ganador (ver 41).
- ❌ Tratar un ganador como eterno: con vida útil de 2-4 semanas, los ángulos se fatigan (ver 62) — ten el reemplazo listo.
- ❌ Juzgar CTWA por "conversaciones iniciadas" y declarar ganador a un ángulo que solo trae saludadores (ver 46/53).
- ❌ Medir retargeting/WhatsApp por view-through en jun-2026: Meta ya lo quitó del API; usa 7d-click/1d-view.
