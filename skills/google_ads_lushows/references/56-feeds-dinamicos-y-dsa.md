# 56 — Feeds dinámicos y DSA

Lee este módulo cuando tu cuenta de Search ya rinde pero **sabes que se te escapan búsquedas** que no alcanzaste a mapear con keywords — la *long-tail* (búsquedas largas, raras, de poco volumen pero alta intención que nadie predice). En vez de adivinar miles de variantes, dejas que Google las pesque solo leyendo tu web. Eso es DSA. Útil, pero peligroso si lo sueltas sin freno: aquí cuándo SÍ, qué controles y qué negativos son **obligatorios**.

## Qué es DSA (y qué NO es)

**DSA** (*Dynamic Search Ads* — anuncios dinámicos de búsqueda) funciona al revés del Search normal:

| | Search normal | DSA |
|---|---|---|
| Tú das | Keywords + título del anuncio | Solo una descripción; Google hace el resto |
| Google empareja por | Tus keywords | El **contenido de tu web** (o un feed de páginas) |
| Título del anuncio | Lo escribes tú | Google lo **genera** según la búsqueda y tu página |
| A dónde manda | La landing que elegiste | La página más relevante de tu web, automático |

En vez de pujar por palabras, le dices a Google "lee mi sitio y muéstrame cuando alguien busque algo que mis páginas resuelven". Google escribe el titular al vuelo y manda a la página que mejor calce. Cubre lo que tú no escribiste.

Lo que **no** es: no es magia ni reemplaza el Search bien armado. Es un **complemento de cobertura** para tapar huecos, no la columna de la cuenta. Y si tu web es pobre o desordenada, DSA genera anuncios pobres — basura entra, basura sale.

**Nota jun-2026 — DSA vs AI Max for Search:** Google está empujando **AI Max for Search** (un toggle en campañas de Search normales que activa expansión tipo broad, generación de assets y *final URL expansion* — mandar a la URL más relevante de tu sitio). AI Max hace, dentro de tu campaña buena, mucho de lo que antes pedías a DSA, y es la dirección a la que va Google (ver `actualizacion-2026-06`, 21, 22). DSA sigue existiendo y sirviendo, pero si arrancas hoy, considera AI Max controlado en tu campaña principal **antes** de montar una DSA aparte. Ambos comparten la misma regla de oro: **exigen negativos férreos o se van a búsquedas basura.**

## Cuándo SÍ usar DSA

DSA (o AI Max) gana en casos concretos:

- **Catálogo grande / muchas páginas** (e-commerce, muchos servicios): imposible escribir keywords para todo. DSA cubre la cola larga sin trabajo manual infinito.
- **Descubrir keywords nuevas:** el reporte de términos de búsqueda de DSA te revela cómo busca la gente DE VERDAD — y esas joyas las pasas a campañas de Search normales con su propio anuncio y puja (ver 20 keywords, 68 search-terms). Es research gratis.
- **Web bien estructurada** con contenido claro por página. DSA depende de tu web; si está bien, rinde.

DSA **NO** es para ti si:
- Tienes **una sola página / un solo producto** (este proyecto: una calculadora). Con tan poco que leer, DSA aporta poco y arriesga emparejamientos raros. Mejor Search transaccional preciso (ver 11, 20).
- Tu web tiene poco contenido o está desordenada.
- No tienes tiempo para vigilar términos de búsqueda y agregar negativos seguido (ver abajo — es obligatorio, no opcional).

## Controles: cómo no soltarlo a lo loco

DSA sin control gasta en búsquedas irrelevantes (Google empareja de más). Las riendas, en orden:

1. **Targets dinámicos por secciones, no "toda la web".** En vez de "todas las páginas", apunta a categorías específicas: reglas de URL que contengan `/restaurante` o `/servicios`, o solo tu página de producto. Acotas a lo que sí vendes.
2. **Excluir páginas que no venden:** blog, "nosotros", "trabaja con nosotros", soporte, términos. Si DSA manda tráfico pago a tu blog informativo, quemas plata. Exclúyelas con reglas de exclusión.
3. **Smart Bidding con tCPA/tROAS** (ver 15) para que la puja se contenga sola por resultado, no por volumen.
4. **Presupuesto acotado y campaña separada.** DSA en su **propia campaña**, nunca revuelto con tu Search bueno, para verlo y cortarlo sin afectar lo que funciona (ver 10 estructura).
5. **Revisión de términos de búsqueda al menos semanal** — no opcional. Es donde vive el control real.

## Negativos: obligatorios, no opcionales

Esta es la parte donde la mayoría quema plata. DSA empareja por significado, así que **siempre** atrae búsquedas que no quieres: gratis, empleo, tutorial, "cómo hacer", competidores, productos que no vendes.

**Régimen de negativos para DSA (setup):**
- Arranca con una **lista de negativos base** compartida a nivel cuenta (ver 22 negativas): `gratis`, `empleo`, `trabajo`, `vacante`, `curso gratis`, `pdf gratis`, `cómo hacer`, `diy`, `usado`, `pirata`, `crack`, y marcas que no manejas.
- **Cada semana**, abre el reporte de términos de búsqueda de la campaña DSA, mira **por qué término te mostró** y a qué página mandó, y **agrega como negativa** todo lo irrelevante. Lleelo de arriba a abajo por gasto.
- Vigila el **destino**: si DSA manda gente a páginas que no convierten, excluye esa URL con una regla.

Sin esta disciplina, DSA es un grifo abierto. Con ella, es una red que pesca ventas que tu keyword research no vio (ver 20). La misma disciplina aplica a AI Max: el toggle es cómodo, los negativos son el seguro.

## Calendario de manejo (sin esto, no lo prendas)

DSA y AI Max no son "prender y olvidar". El que los suelta y se va, pierde. Ritmo mínimo:

| Frecuencia | Tarea |
|---|---|
| Primeros 3 días | Revisar términos a diario — al inicio entra lo más raro; negativiza rápido |
| Semanal | Reporte de términos completo, ordenar por gasto, negativizar lo irrelevante, cosechar lo bueno a Search normal |
| Quincenal | Revisar a qué páginas mandó; excluir URLs que no convierten |
| Mensual | Comparar costo por conversión de DSA vs tu Search bueno; si DSA cuesta mucho más, recortar presupuesto |

Si no tienes tiempo para este ritmo, **no es para ti**: una campaña de keywords exactas/frase bien armada (ver 11, 20, 21) rinde sin tanta vigilancia. DSA paga su libertad con tu atención semanal.

## Errores comunes — blacklist

1. **Apuntar DSA a "toda la web".** Incluye blog, "nosotros" y soporte → tráfico pago que no vende. Apunta a secciones que venden y excluye el resto.
2. **No agregar negativos cada semana.** DSA (y AI Max) atraen basura por diseño. Sin negativos constantes, es un hueco de plata. Revisa términos semanal, sí o sí.
3. **Mezclar DSA con tu Search bueno.** No puedes ver ni cortar lo malo sin tocar lo bueno. DSA va en campaña aparte.
4. **Usar DSA con una sola página/producto.** Poco que leer, mucho riesgo de emparejamiento raro. No es tu caso: usa Search transaccional preciso (ver 11, 20).
5. **Confiar en los titulares automáticos sin revisarlos.** Google a veces genera títulos torcidos o que dañan tu marca. Revisa qué está mostrando y excluye lo que no calce.
6. **Olvidar que DSA depende de tu web.** Web pobre = anuncios pobres. Si la web está mal, arréglala antes (desingweb-lushows) o DSA solo expone el problema.
7. **No cosechar las keywords que DSA descubre.** Su mayor valor es revelarte búsquedas nuevas. Pásalas a Search normal con anuncio y puja propios en vez de dejarlas solo en DSA (ver 20, 30).
