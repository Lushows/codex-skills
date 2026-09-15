# 17 — Framework de testing

Testear no es "probar cositas a ver qué pasa": es un sistema con orden de prioridades, presupuesto definido y criterio de decisión escrito ANTES de lanzar. Lee este módulo cuando quieras mejorar resultados y no sepas qué tocar primero, o cuando lleves meses "testeando" sin un solo aprendizaje documentado.

## El orden de testeo por impacto (no lo inviertas)

Testea primero lo que más mueve la aguja. De mayor a menor impacto:

1. **Oferta** (qué vendes y cómo lo empaquetas: precio, bundle, garantía, envío gratis): puede mover resultados 2-10×. Una oferta mala con anuncios perfectos pierde contra una oferta brutal con anuncios mediocres (ver 41).
2. **Ángulo del creativo** (la idea/promesa: dolor que ataca, deseo que activa): mueve 2-5× (catálogo de ángulos en 30).
3. **Formato** (video vs imagen vs carrusel vs UGC vs Reels): mueve 1.5-2× (ver 34 para Reels).
4. **Copy/hook** (las primeras palabras/3 segundos): mueve 1.2-1.5×.
5. **Audiencia**: en la era broad casi no hay qué testear — geo y poco más. Lo que era "testing de audiencias" en 2019 hoy lo hace el algoritmo (ver 20).
6. **Landing** (la página de destino): impacto alto pero es OTRO sistema de tests (CRO); para construir/mejorar landings, skill desingweb-lushows.

El error clásico: gastar 3 meses testeando audiencias e intereses (nivel 5) sin haber testeado jamás un segundo ángulo (nivel 2).

## El testing en la era del creativo-es-targeting (2026)

Como GEM (ver 92) usa el creativo para encontrar audiencias, **testear = producir variedad de creativos** y dejar que el sistema elija. Por eso necesitas **10-15 creativos distintos** en rotación (ver 30) y un pipeline que reemplace los que fatigan (vida 2-4 semanas, ver 39). Ojo con el **Entity ID**: si tus "variantes" son casi-duplicados (mismo video, otro texto), Meta las colapsa y NO las prueba como distintas — el test es falso. Variar de verdad significa cambiar el ángulo, el formato o el hook visual, no solo el caption.

## Cómo testear bien: las 3 reglas

1. **Una variable a la vez.** Si cambias ángulo Y formato Y hook, no sabrás qué causó la diferencia. Variantes idénticas salvo en LO que testeas.
2. **Presupuesto suficiente: 3-5× tu CPA esperado POR variante.** Si tu CPA es $40.000 COP y testeas 3 ángulos: 3 × $150.000 ≈ $450.000 COP el test. Menos que eso = el resultado es ruido con disfraz de dato. Si no te alcanza, testea 2 variantes, no 5 a medias.
3. **Criterio de ganador PRE-escrito.** Antes de lanzar, escribe: *"Gano si: CPA ≤ $45.000 con ≥10 conversiones por variante tras 5-7 días o 5× CPA de gasto"*. Lo que NO es criterio: mirar a las 12 horas y decidir por corazonada porque uno "arrancó mejor".

## A/B test formal vs testing operativo

- **A/B test de Meta** (herramienta Experiments): divide audiencias sin solapamiento, científicamente limpio. Úsalo para decisiones GRANDES y caras: landing A vs B, estrategia de puja, estructura de campaña, Advantage+ Sales vs manual broad. Requiere volumen y paciencia. Es también la base de los lift tests de incrementalidad (ver 65).
- **Testing operativo** (lo de todos los días): ad set de testing con ABO (presupuesto fijo, ver 10) donde compiten 2-4 ads nuevos, o varios ads dentro del mismo ad set dejando que el algoritmo reparta. Menos limpio (Meta no reparte parejo: al que arranca bien le da casi todo), pero refleja la realidad de cómo se entregará después. Para testing de creativos, esto basta.
- Truco del reparto desigual: si un ad nuevo no recibe gasto en 3-4 días, no está "probado malo", está "no probado". Dale su propio ad set ABO para forzar gasto.

## Cadencia: pipeline permanente

- **Siempre hay 1 test vivo.** No es un evento trimestral; es una rutina. Cuenta micro: 1 test cada 2-4 semanas. Cuenta media: 1-2 por semana. Grande: pipeline continuo (ver 39 para producción de creativos en serie).
- Flujo: idea → brief → producción → test (ad set testing) → ganador entra a la campaña principal/Advantage+ Sales (ver 12) → perdedor se documenta y se archiva.
- Los ganadores se vuelven el nuevo control a vencer. Si nada vence al control en 2 meses, el problema es la calidad/variedad de las ideas, no el sistema: vuelve al nivel 1-2 (oferta y ángulos).

## Calculadora de un test (ejemplo COP)

| Parámetro | Valor |
|---|---|
| CPA esperado | $40.000 |
| Variantes a probar | 3 ángulos |
| Gasto por variante (4× CPA) | $160.000 |
| Gasto total del test | $480.000 |
| Duración | 5-7 días |
| Criterio ganador (pre-escrito) | CPA ≤ $44.000 con ≥10 conv/variante |

Si solo tienes $250.000 para testear: prueba **2** variantes bien, no 3 a medias. Datos sólidos de 2 valen más que ruido de 5.

## Documentar aprendizajes (la hoja de learnings)

Sin registro, repetirás tests y olvidarás por qué algo funcionó. Hoja simple (Sheets):

| Fecha | Qué testeé (variable) | Hipótesis | Variantes | Gasto | Resultado (CPA/tasa) | Decisión | Aprendizaje |
|---|---|---|---|---|---|---|---|
| 12-jun | Ángulo | "Dolor de espalda vence a productividad" | A: dolor / B: productividad | $300k | A: $32k / B: $51k | A a campaña principal | Audiencia responde a salud, no rendimiento |

El campo "Aprendizaje" es el activo: en 6 meses tendrás un manual de qué mueve a TU cliente — eso vale más que cualquier campaña individual. Esos aprendizajes alimentan tus próximos briefs creativos (ver 30 y directorcreativo_lushows) y tus argumentos de venta (ventas_lushows).

## Errores comunes — blacklist

- Declarar ganador a las 12-24 horas: las primeras horas son ruido de subasta, no señal.
- Testear 6 variantes con presupuesto para 2: seis resultados estadísticamente inútiles.
- Cambiar 3 variables a la vez y "aprender" algo: no aprendiste, adivinaste.
- Testear audiencias antes que ángulos: orden de impacto invertido, meses perdidos.
- "Probar" 5 casi-duplicados: Meta los colapsa en un Entity ID; no testeaste nada.
- No tener control: todo test compite contra tu mejor anuncio actual, no contra el vacío.
- Matar al perdedor sin anotar POR QUÉ perdió: pagaste por el dato y lo botaste.
- Pausar el test cuando "ya parece obvio" a mitad de camino: los vuelcos al día 4-5 son comunes.
- No tener pipeline: ganas un test, lo celebras, y a las 3 semanas el ganador fatigó y no hay reemplazo listo (ver 39).
