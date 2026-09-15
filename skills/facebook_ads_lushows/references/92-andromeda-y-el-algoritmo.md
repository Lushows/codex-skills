# 92 — Andromeda, GEM y el algoritmo: el modelo mental correcto de 2026

Andromeda es el motor de **retrieval** (recuperación y ranking con machine learning) que Meta usa para decidir, entre millones de anuncios candidatos, cuáles mostrarle a cada persona — personalización a escala de individuo, no de "audiencia". Sobre él, desde noviembre-2025, corre **GEM (Generative Era Model / modelo generativo)**: una capa que no solo recupera y rankea sino que *generaliza* mejor entre señales escasas, prediciendo a quién le hablará un creativo aunque tenga poco historial. Traducción operativa: el sistema lee el contenido de tu anuncio con más finura que nunca y necesita **más candidatos diversos** para hacer su trabajo. Lee este módulo para entender CÓMO piensa la entrega y dejar de pelear contra ella; cambia qué optimizas tú y qué le dejas al sistema. No es teoría: cada implicación de abajo es una decisión operativa. (La jerga "Lattice" que circula en YouTube **no es oficial** — no decidas nada con base en ella.)

## Qué premia el sistema (Andromeda + GEM)

**Diversidad y volumen creativo REAL.** El sistema construye una representación de cada anuncio a partir de su contenido (visual, texto, audio) y lo matchea con personas. GEM hace ese matching más generalizable: incluso con poca señal histórica, predice mejor a quién le habla un creativo nuevo. Consecuencia directa:

- 10 ads que dicen lo mismo con otro color = **1 anuncio** para el sistema: ocupan un solo "espacio" de match.
- 10 ángulos distintos (precio, dolor, prueba social, demo, contraste, ver 30/38) = **10 oportunidades de match** con 10 tipos de persona distintos.
- Más candidatos diversos = más superficie de personalización = más subastas donde puedes ganar barato.

Por eso "sube más creativos" no es un consejo genérico: es literalmente cómo se alimenta el motor. Pero volumen sin diversidad es ruido, no comida (ver 39).

## Entity ID: por qué tus "10 variantes" pueden contar como 1

En 2026 el sistema agrupa creativos casi-duplicados bajo un mismo **Entity ID** (identidad de entidad): si subes 8 ads que para el modelo son visualmente y textualmente equivalentes, colapsa esos casi-duplicados y los trata como **una sola entidad** en la subasta. Implicaciones:

- Cambiar el color del fondo o reordenar una frase **no crea diversidad** — crea otro casi-duplicado que se colapsa.
- La diversidad que cuenta es de **ángulo, hook, formato y prueba** (ver 38/37/33), no de retoque cosmético.
- Subir 50 variantes cosméticas no engaña al sistema: las colapsa y desperdicias slots y presupuesto de aprendizaje (ver 91).

## Vida útil del creativo: 2-4 semanas, planéala

Bajo GEM, un creativo ganador **satura su superficie de match en 2-4 semanas** típicas (más rápido en nichos chicos, más lento en universos grandes). No es castigo ni conspiración: el mismo anuncio recorrió a la gente con la que matcheaba bien. Operativa: el pipeline creativo no es opcional ni estacional — es una **línea de producción permanente** que mete variantes nuevas cada 2-4 semanas (ver 39/91). La cuenta que no produce muere por fatiga, no por algoritmo.

## Las 4 implicaciones prácticas

1. **Consolida la estructura.** Pocos ad sets con presupuesto suficiente > 12 ad sets fragmentados. El sistema explora MEJOR dentro de un ad set consolidado que tú segmentando a mano (ver 10). Cada ad set extra divide la señal y alarga el aprendizaje (ver 13).
2. **El creativo ES el targeting.** El sistema lee el contenido del anuncio para decidir a quién mostrarlo: tu hook le DICE al algoritmo a quién buscar. "¿Te duele la rodilla al subir escaleras?" targetea mejor que cualquier interés seleccionado a mano (ver 30/37). Si quieres llegar a otro público, no cambies la audiencia: cambia el ángulo. GEM hace esto más cierto que nunca.
3. **La señal es el combustible.** Más y mejores eventos (píxel + CAPI con buen Event Match Quality, ver 06) = matching más fino = CPA más bajo. Una cuenta con CAPI bien implementado le da al sistema ojos; una sin señal lo deja adivinando. Si vendes por WhatsApp, reportar la venta cerrada vía CAPI cierra el loop (ver 53).
4. **Los hacks de estructura murieron.** Duplicar ad sets "para resetear", segmentar por interés micro, horarios manuales, "estructuras secretas" de gurú: el sistema optimiza la entrega mejor que tu micro-gestión. **Tu ventaja competitiva ya no es la estructura: es oferta (ver 41) + creativo (ver 30) + señal (ver 06) + disciplina (ver 70).** La estructura solo puede estorbar; ya no puede ganar.

## "Darle de comer al algoritmo" — qué significa de verdad

| Comida buena | Por qué |
|---|---|
| Volumen de conversiones del evento correcto (ver 14) | Es lo que el modelo aprende a predecir |
| Diversidad creativa real (ángulos, formatos, hooks) en Entity IDs distintos | Más superficie de match; los casi-duplicados se colapsan |
| Presupuesto estable, cambios ≤20-30% (ver 72) | Las predicciones se calibran con condiciones estables |
| NO tocar cada 12 horas (ver 70) | Cada edición significativa resetea aprendizaje |
| Señal limpia vía CAPI con EMQ alto | Matching a nivel de persona; GEM generaliza mejor con señal de calidad |
| Reposición creativa cada 2-4 semanas | Compensa la vida útil corta de cada asset |

## Mitos del algoritmo — desmentidos

- **"Primero calienta la cuenta con engagement orgánico / campañas de likes"**: falso. Los likes no entrenan nada útil para conversión; optimiza desde el día 1 por el evento más cercano a la venta que tu volumen permita (ver 14).
- **"Las cuentas nuevas pagan novatada eterna"**: pagan aprendizaje (semanas, ver 13), no condena. Con señal y creativo correctos, una cuenta de 2 meses compite contra una de 5 años — y GEM lo hace más cierto al generalizar con menos historial.
- **"Meta te castiga por editar"**: te resetea el aprendizaje del ad set editado, que no es castigo sino recalibración. El problema es editar a cada rato, no editar (ver 70).
- **"Hay horarios mágicos para lanzar"**: el sistema reparte la entrega según cuándo convierte TU público; lanzar martes 9am vs domingo 11pm no cambia el destino de la campaña.
- **"El algoritmo me quema la audiencia a propósito para que pague más"**: la fatiga es real pero es creativa, no conspiración: el mismo ad mostrado mil veces deja de funcionar (ver 39). La solución es creativo nuevo, no teorías.
- **"Broad es para cuentas grandes, las chicas necesitan intereses"**: al revés — la cuenta chica necesita MÁS que el sistema explore libre, porque no tiene gasto para sostener segmentos fragmentados (ver 20).
- **"Lattice/GEM es un algoritmo nuevo que requiere otra estrategia"**: GEM mejora el matching; el sistema (oferta→creativo→señal→disciplina) no cambia. "Lattice" ni siquiera es término oficial.

## Cómo trabajar CON el sistema: el rol del media buyer 2026

Tu trabajo dejó de ser operar palancas de entrega y pasó a ser: (1) definir la oferta que hace fácil el match (ver 41), (2) producir el portafolio creativo diverso (en Entity IDs distintos) que le da candidatos (ver 39, 91), (3) garantizar señal limpia y completa (ver 06/62), (4) medir contra margen real, no contra la plataforma (ver 64), y (5) tener la disciplina estadística de no intervenir por ansiedad (ver 70/71). Todo lo demás de esta skill cuelga de esas cinco cosas.

## Checklist: ¿estás alimentando bien al sistema?

- [ ] ≤ 2-3 campañas / pocos ad sets concentran ≥ 80% del gasto (consolidación, ver 10).
- [ ] 6-15 ads activos con al menos 3 ángulos genuinamente distintos — y que NO se colapsen en un Entity ID (ver 38).
- [ ] CAPI activo y Event Match Quality bueno en el evento principal (ver 06/62).
- [ ] Evento de optimización = el más cercano a la venta que tu volumen sostiene (ver 14).
- [ ] Última edición estructural hace ≥ 7 días; cambios de presupuesto ≤ 20-30% (ver 70/72).
- [ ] Pipeline creativo: hay variantes nuevas entrando cada 2-4 semanas (vida útil del asset, ver 39/91).

Si marcas las 6, tu cuenta está dándole al motor todo lo que puede usar; lo que falte de resultado ya no es "el algoritmo": es oferta, precio o mercado (ver 61, y si es de negocio, economist_lushows).

## Errores comunes — blacklist

- Subir 10 "variantes" que son el mismo ad con otro fondo y creer que diste diversidad: el Entity ID las colapsa en uno solo.
- Fragmentar en micro ad sets "para controlar a quién le llega": le quitas al motor su capacidad de explorar y a tu señal su masa crítica.
- Optimizar por evento de vanidad (clics, mensajes vacíos) y quejarse de que "el algoritmo trae basura": traes exactamente lo que pediste (ver 14).
- Tocar presupuesto/creativos cada 12h: nunca sales de la fase de calibración.
- Buscar el "hack de estructura 2026" o la "estrategia para Lattice" en YouTube: ya no existe; esa energía va a oferta y creativo.
- No reponer creativo asumiendo que el ganador dura para siempre: su vida útil es 2-4 semanas (ver 39).
- Ignorar CAPI porque "el píxel ya funciona": estás alimentando al motor con la mitad de la señal y GEM generaliza peor (ver 06).
