# 52 — Lead ads e instant forms

Los lead ads usan **instant forms** (formularios instantáneos): un formulario nativo DENTRO de Meta — el usuario nunca sale a una web, el form carga al instante y sus datos (nombre, teléfono, email) llegan **autocompletados desde su perfil**. Lee este módulo cuando tu negocio necesite capturar datos para contactar después: servicios, cotizaciones, educación, inmobiliaria, B2B. Jerga: "instant form" = formulario nativo de Meta; "CPL" = *Cost Per Lead*, costo por lead; "speed-to-lead" = tiempo entre que entra el lead y lo contactas.

## Lead ads vs CTWA vs landing: el árbol de decisión

| Herramienta | Para qué | Cuándo |
|---|---|---|
| **Instant form** (este módulo) | Capturar datos y contactar DESPUÉS | Servicios con cotización, B2B, agendamiento, bases para llamar |
| **CTWA** (ver 50) | Conversación YA, en caliente | Venta por chat inmediata, ticket bajo-medio, pyme WhatsApp-first |
| **Landing propia** (ver 05, desingweb-lushows) | Vender/educar antes de pedir el dato | Producto que requiere explicación, high-ticket con página de ventas, e-com |

El trade-off central de los instant forms: **más fácil de llenar = lead más frío**. Dos taps con datos autocompletados producen volumen barato de gente que mañana no recuerda haberse registrado. Todo el diseño del form es administrar ese trade-off.

## 🔴 Doble ubicación de conversión y Advantage+ Leads (2026)

Novedad confirmada (ver `actualizacion-2026-06` §9): una sola campaña ahora sirve **instant form a los rápidos Y form web a los que buscan contexto** — Meta reparte por persona. Meta reporta **−60% CPL / +125% volumen** vs solo-web. Y **Advantage+ Leads** automatiza audiencia, ubicaciones y entrega (el equivalente de ASC para lead-gen).

- Receta 2026: deja la doble ubicación encendida salvo que tu form web convierta mucho mejor calificado (mídelo). Para arrancar, Advantage+ Leads con 2-3 creativos y dejar que el sistema reparta.
- Añadidos: **calificación de leads con IA** y verificación dentro del flujo — úsalos para filtrar antes de que el lead toque a tu vendedor.

## Formularios que FILTRAN: setup paso a paso

1. Campaña objetivo **Leads** → ubicación: formulario instantáneo (o doble ubicación, arriba).
2. Crea el form. Primer fork — tipo de formulario:
   - **Más volumen**: mínimo de pasos, submit directo. CPL más bajo, calidad más baja.
   - **Mayor intención**: agrega una **pantalla de revisión** donde el usuario confirma sus datos antes de enviar. Filtra al distraído. Default recomendado para servicios.
3. **Preguntas custom — 1 a 3 máximo**. Cada pregunta filtra ~20-40% del volumen y sube la calidad del resto. Las que más pagan:
   - Presupuesto (opción múltiple con rangos: "Menos de $2M / $2-5M / Más de $5M")
   - Ciudad/zona (si tu cobertura es limitada — descalifica gratis)
   - Cuándo lo necesita ("Esta semana / Este mes / Solo cotizando")
   - Usa opción múltiple, no campo abierto: respuestas comparables y menos abandono.
4. **Pantalla de gracias con siguiente paso**: nunca la dejes en "Gracias, te contactaremos". Pon botón con acción:
   - **Botón a WhatsApp** ("Escríbenos ya y agenda") — el combo **lead form → WhatsApp es oro**: capturas el dato (aunque no escriba) Y le das al caliente la vía rápida (la conversación: ver 54).
   - Alternativas: llamar ahora, link a agenda (Calendly), link a la web.
5. Conecta la entrega de leads a tu CRM/WhatsApp (siguiente sección) ANTES de prender la campaña.

### Plantilla de instant form (servicios)

```
Titular: Cotiza tu [servicio] sin compromiso — respuesta en menos de 1 hora
Imagen: antes/después real o el equipo trabajando (NO stock)
Tipo: Mayor intención (con pantalla de revisión)
Preguntas:
  1) ¿En qué zona/ciudad estás? [Bogotá / Medellín / Cali / Otra]
  2) ¿Cuándo lo necesitas? [Esta semana / Este mes / Solo cotizando]
  3) Presupuesto aproximado [< $2M / $2-5M / > $5M]
Aviso de privacidad: link a tu política
Pantalla de gracias: "¡Listo! Escríbenos ya por WhatsApp y agenda tu visita" + botón WA
```

## Speed-to-lead: la variable que más mueve el cierre

Un lead contactado en **menos de 5 minutos convierte hasta 21× más** que uno contactado después de 30 minutos (estudios clásicos de lead response, y en LatAm con WhatsApp es peor: el que cotiza, cotiza con tres a la vez y le compra al primero que responde).

- **Nunca** "descargo el CSV cuando pueda": los leads se entregan en Ads Manager/Meta Business Suite y mueren ahí.
- Integra entrega automática: Meta → CRM o Meta → webhook → mensaje de WhatsApp saliente al lead en segundos (plantilla de la API). Herramientas: integración nativa de tu CRM, Zapier/Make, o tu propio backend (stack: ver 96).
- Si no hay stack: configura las notificaciones de leads en el celular del vendedor y exige contacto <15 min en horario hábil. Es artesanal pero funciona.

### Plantilla de primer mensaje automático (WhatsApp, Utility template)

```
Hola {{nombre}} 👋 Soy {{asesor}} de {{empresa}}. Vi que te interesa cotizar
{{servicio}} en {{zona}}. Para darte el precio exacto, ¿me confirmas [dato clave]?
Te puedo agendar la visita esta misma semana 🙌
```

## La métrica real: costo por lead CALIFICADO

El CPL (costo por lead) es vanidad. La métrica que decide presupuesto es **costo por lead calificado** y costo por venta:

```
CPL $8.000 con 50% calificados  → calificado a $16.000  ✓ mejor
CPL $4.000 con 15% calificados  → calificado a $26.600  ✗ "más barato" y peor
```

Define "calificado" por escrito (tiene presupuesto + zona + respondió al contacto), etiquétalo en el CRM y reporta por campaña cada semana. Devuelve el evento "lead calificado" a Meta vía CAPI para que optimice por él, no por lead pelado (ver 53). Para high-ticket esta lógica completa está en 58.

## Receta resumida por vertical

| Negocio | Tipo de form | Preguntas filtro | Pantalla de gracias |
|---|---|---|---|
| Remodelaciones / servicios high-ticket | Mayor intención | Presupuesto + cuándo + zona | Botón WhatsApp "agenda tu visita" |
| Educación / cursos | Mayor intención | Cuándo empezaría + modalidad | Botón WhatsApp o llamada |
| Inmobiliaria | Mayor intención | Presupuesto + zona + crédito pre-aprobado | Agenda de visita |
| Seguros / financiero B2C | Más volumen + 1 filtro | Edad/rango de ingreso | Llamada o WhatsApp |
| Gimnasio / clínica estética | Mayor intención | Zona + objetivo | Botón WhatsApp "agenda valoración" |

> ⚠️ Si pautas productos financieros con targeting hacia EE. UU. aplica la categoría especial "Financial Products and Services" (restringe targeting). Para Colombia no aplica esa restricción, pero crédito/seguros mal declarados son causa común de restricción de cuenta — revisa políticas (ver 08, `actualizacion-2026-06` §10).

## Errores comunes — blacklist

- Form "más volumen" sin preguntas filtro: bandeja llena de curiosos, vendedores quemados, "los leads de Facebook son malos".
- 5+ preguntas custom: mataste el volumen; 1-3 bien elegidas.
- Pantalla de gracias muerta sin botón de siguiente paso: regalas el momento de mayor intención.
- Contactar leads al día siguiente: cada hora de espera pudre la tasa de cierre (regla 21×).
- Medir y celebrar CPL en vez de costo por calificado/venta: optimizas hacia la basura barata.
- No probar el form tú mismo antes de lanzar (hay preview y herramienta de prueba): forms con preguntas rotas corren semanas sin que nadie lo note.
- Olvidar que los leads expiran en Meta (90 días descargables): sin integración automática, pierdes hasta la base.
- Apagar la doble ubicación de conversión sin medir: muchas veces es −60% CPL gratis (ver `actualizacion-2026-06` §9).
