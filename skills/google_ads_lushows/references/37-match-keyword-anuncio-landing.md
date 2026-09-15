# 37 — Match keyword→anuncio→landing

Lee este módulo cuando tu Quality Score esté flojo y no sepas por qué, tengas un solo grupo de anuncios con 200 keywords mezcladas, o quieras la estructura que hace que las campañas de Search rindan en vez de quemar plata.

Este es el módulo más importante de toda la sección de Search, porque resume el principio que mueve TODO: **el clic debe sentirse como una sola conversación coherente desde que el usuario escribe hasta que aterriza en tu página.** Lo que el usuario buscó (keyword), lo que tu anuncio le dijo (RSA) y lo que vio al llegar (landing) tienen que decir lo mismo. A esa coherencia se le llama **message match**, y es lo único que sube Quality Score Y tasa de conversión a la vez (ver 33, 36). Rompe el match en cualquier eslabón y pagas más por vender menos. Si memorizas un solo módulo de Google Ads, que sea este.

## La cadena de 3 eslabones

| Eslabón | Pregunta del usuario | Tu respuesta |
|---|---|---|
| **Keyword** | "necesito X" (lo que escribe) | la palabra por la que pujas |
| **Anuncio (RSA)** | "¿esto es X?" | título que contiene X (ver 31) |
| **Landing** | "¿de verdad es X?" | H1 + oferta que rematan X (ver 33) |

Ejemplo coherente de punta a punta:
- Keyword: `calculadora costos para cafetería`
- Título: "Calculadora de Costos para Cafetería"
- H1 landing: "Calcula los Costos de tu Cafetería"
- Oferta visible: "$10.000 · pago único · descarga ya"

El cerebro del usuario nunca duda. Eso convierte. Ahora rompe un eslabón — mismo anuncio pero landing que dice "Software de gestión integral GastroLatam" — y el usuario siente que llegó al lugar equivocado. Se va. Pagaste el clic para nada y Google baja tu Quality Score por "experiencia de destino" mala. El daño es doble: perdiste la venta Y encareciste el próximo clic.

## La estructura que produce el match: grupos por tema

El error #1 en cuentas colombianas es **un grupo de anuncios gigante con todas las keywords mezcladas**. Si en un grupo tienes "calculadora costos restaurante", "software inventario cocina" y "precio menú app", NINGÚN anuncio le queda bien a las tres. El anuncio se vuelve genérico, baja la relevancia y baja el QS (ver 36).

La solución es **agrupar por tema**: cada grupo de anuncios trata UNA sola idea, con sus keywords cercanas, su RSA dedicado y su landing dedicada.

| Grupo de anuncios | Keywords (mismo tema) | Anuncio dedicado | Landing dedicada |
|---|---|---|---|
| Costos restaurante | calculadora costos restaurante, food cost restaurante | "...para Restaurante" | /restaurante |
| Costos cafetería | calculadora costos cafetería, costos café | "...para Cafetería" | /cafeteria |
| Costos dark kitchen | costos dark kitchen, costos cocina oculta | "...para Dark Kitchen" | /dark-kitchen |
| Fijar precios menú | cómo fijar precios menú, precio de un plato | "Fija el Precio de tu Menú" | /precios-menu |

Regla simple: **si dos keywords necesitarían un anuncio distinto para sonar relevantes, van en grupos distintos.** Pocas keywords muy parecidas por grupo (3-15 suele bastar). Cada grupo es una mini-campaña con su mensaje afilado.

### SKAG murió, "temas afilados" vive

Hace años se usaba SKAG (Single Keyword Ad Group: un grupo por keyword exacta). En 2026 eso está muerto: con concordancia amplia + Smart Bidding, Google necesita más señal por grupo para aprender, y mil grupos de una keyword fragmentan los datos. La práctica actual es **STAG (Single Theme Ad Group): un grupo por TEMA**, con un puñado de keywords del mismo concepto. No persigas la keyword exacta uno-a-uno; persigue el tema coherente. Esto conecta con concordancias (ver 21): hoy con amplia + Smart Bidding los grupos pueden ser más reducidos en cantidad de keywords pero deben seguir siendo de UN tema, porque el anuncio y la landing se escriben PARA ese tema.

## El match como sistema, no como truco

No basta con arreglar el anuncio o la landing por separado. El match es de la CADENA completa:
- Mejoras el anuncio pero la landing sigue genérica → el match se rompe en el último metro (ver 33).
- Mejoras la landing pero el anuncio no menciona la keyword → se rompe en el primero (ver 31).
- Mezclas temas en un grupo → ni anuncio ni landing pueden ser específicos → se rompe en la raíz.

### Checklist de diagnóstico (cuando algo no rinde)

Antes de tocar la puja, recorre la cadena de arriba a abajo:

1. ¿El **término de búsqueda real** (ver 68, no la keyword que escribiste) coincide con tu tema? Si entran búsquedas raras, faltan negativas (ver 22).
2. ¿El **título** del RSA contiene la keyword del grupo? (ver 31)
3. ¿La **landing** tiene la keyword en el H1 y muestra la oferta sin scroll? (ver 33)
4. ¿La landing **carga rápido** en móvil? (Core Web Vitals, ver 33)
5. ¿El **grupo** tiene un solo tema o están mezclados? (la raíz del problema 80% de las veces)

Si los cinco están bien y aún no rinde, ahí sí mira puja, presupuesto o producto (ver 61).

Por eso este módulo es la columna vertebral: la congruencia total (ver 48) es lo que produce Quality Score alto (CPC barato, ver 36) y CVR alto (más ventas, ver 33) al mismo tiempo. Es la diferencia entre una cuenta que escala y una que sangra. Cuando algo no rinde, lo primero que revisas no es la puja: es si la cadena keyword→anuncio→landing está rota en algún eslabón. Para el copy persuasivo de la landing apóyate en `ventas_lushows`; para construirla, `desingweb-lushows`.

## Errores comunes — blacklist

- **Un grupo gigante con keywords de varios temas**: ningún anuncio les queda bien, la relevancia se hunde y el QS cae (ver 36). Agrupa por tema.
- **Reutilizar el mismo RSA en grupos de temas distintos**: pierdes el reconocimiento de la keyword en el título; cada grupo merece su anuncio.
- **Mandar todos los grupos a la misma landing genérica**: rompe el match en el último eslabón; cada tema a su página/sección (ver 33).
- **Arreglar solo un eslabón**: el match es de la cadena completa; revisa keyword, anuncio Y landing juntos.
- **Volver a SKAG (un grupo por keyword)**: fragmentas datos y Smart Bidding no aprende; usa STAG, un grupo por tema (ver 21).
- **Meter 100 keywords por grupo "por si acaso"**: hoy con amplia + Smart Bidding sobran; pocas keywords del MISMO tema bastan.
- **Empezar por la puja cuando algo no rinde**: el 80% de las veces el problema es match roto; recorre el checklist de diagnóstico primero (ver 61).
- **Olvidar que el match sube QS Y CVR a la vez**: tratarlo como "detalle de relevancia" subestima que es la palanca doble más rentable de la cuenta (ver 48).
