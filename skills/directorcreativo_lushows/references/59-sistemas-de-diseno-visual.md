# 59 — Sistemas de diseño visual

Un sistema de diseño convierte **piezas sueltas en un mecanismo repetible**: reglas, plantillas y componentes que permiten producir muchas piezas coherentes, rápido, y sin que un experto rehaga todo cada vez. Es el puente entre "diseñé algo lindo" y "tengo una marca que escala". Es la culminación de todo el bloque 5.

## El problema que resuelve
Sin sistema, cada pieza se diseña desde cero: lenta, inconsistente, dependiente de una persona. Con sistema:
- **Coherencia automática** — todo respeta las mismas reglas (ver 55).
- **Velocidad** — armas una pieza nueva combinando piezas existentes.
- **Escalabilidad** — otra persona (o un no técnico) produce sin romper la marca.
- **Mantenimiento** — cambias una regla en un lugar y se propaga.

## Las tres capas de un sistema

### 1. Reglas (los fundamentos / "tokens")
Las decisiones base que TODO usa. En diseño digital se llaman *design tokens*; en print, "fundamentos de marca":
- **Color:** paleta exacta (códigos) + proporciones de uso (ej. 60% neutro, 30% base, 10% acento).
- **Tipografía:** familias, pesos, y una **escala** (ej. 12/14/16/20/28/40 — múltiplos coherentes).
- **Espaciado:** sistema de 8 px / o módulos en mm (ver 51).
- **Retícula:** márgenes y columnas estándar por formato.
- **Radios, grosores de línea, sombras:** valores fijos.
- **Iconografía, patrones, texturas:** los definidos en 56 y 58.

### 2. Componentes (piezas reutilizables)
Bloques ya resueltos que se combinan:
- Botones, tarjetas de producto, encabezados, pies, banners.
- En print: ficha de producto, plantilla de etiqueta, módulo de precio.
- Cada componente respeta las reglas de la capa 1 y se reusa idéntico.

### 3. Plantillas (composiciones completas)
Layouts listos para rellenar con contenido nuevo:
- Plantilla de post de producto, story, afiche de evento, ficha de catálogo, encabezado de email.
- El no técnico solo cambia foto y texto; el sistema garantiza que salga bien.

## Cómo construir el sistema (proceso)
1. **Audita lo que ya tienes.** Junta todas las piezas existentes. Detecta lo repetido (eso son componentes futuros) y las inconsistencias (eso son reglas faltantes).
2. **Fija los fundamentos** (capa 1). Sin esto no hay sistema. Decide color, tipo, escala, espaciado, grid.
3. **Identifica los componentes** que más se repiten y diséñalos una vez, bien.
4. **Crea las plantillas** de las piezas más frecuentes (lo que produces cada semana).
5. **Documenta todo** con ejemplos de uso correcto e incorrecto (el "haz / no hagas").
6. **Distribuye y entrena.** Un sistema que nadie sabe usar no existe. Entrega plantillas editables y una guía simple.
7. **Versiona y mantén.** El sistema evoluciona; lleva control de cambios y un responsable.

## Reglas de oro de un buen sistema
- **Pocas reglas, claras.** Un sistema con 200 excepciones no es sistema. Menos decisiones, más obediencia.
- **Tokens antes que piezas.** Define los valores base primero; los componentes los heredan.
- **Consistencia > novedad.** El sistema premia la repetición disciplinada (ver 50).
- **Diseñado para el menos experto.** Si solo el diseñador estrella puede usarlo, falló. Que un asistente arme un post correcto.
- **"Haz / No hagas" explícito.** Las imágenes de uso correcto e incorrecto evitan el 80% de los errores.

## Ejemplo concreto: sistema mínimo para una pyme
Para un negocio pequeño no hace falta un sistema enorme. Un kit mínimo viable:
- **Fundamentos:** 1 página con paleta, 2 tipografías + 4 tamaños, espaciado base, márgenes.
- **3 plantillas editables:** post cuadrado, story, ficha de producto/etiqueta.
- **Componentes:** bloque de precio, máscara de foto (ver 58), set de íconos (ver 56).
- **Guía de 1 hoja:** "siempre / nunca" con 5 reglas (ej. "nunca estires el logo", "siempre deja margen X", "siempre usa estos 2 tipos").
Con eso, el dueño produce piezas coherentes solo, sin diseñador en cada post.

## El puente al manual de marca
El sistema de diseño visual es la **antesala del manual de marca** (brand guidelines): el documento que reúne logo, paleta, tipografía, fotografía, íconos, patrones, voz y reglas de uso. La diferencia:
- **Sistema de diseño:** orientado a PRODUCIR (plantillas, componentes, tokens vivos).
- **Manual de marca:** orientado a NORMAR y comunicar (qué es la marca, cómo se usa, qué no se permite).
Un buen sistema alimenta el manual y viceversa (ver módulo de manual de marca).

## Referentes (sistemas reales)
- **Material Design (Google)** y **Human Interface Guidelines (Apple)** — sistemas digitales de referencia mundial.
- **NASA Graphics Standards Manual (1976)** y **New York City Transit (Vignelli/Unimark)** — sistemas pre-digitales legendarios, todo basado en grid y reglas.
- **IBM (Paul Rand)** y su evolución a **Carbon Design System** — del logo a un sistema escalable.
- **Spotify, Airbnb (DLS)** — sistemas de marca modernos y documentados.

## Errores típicos (no técnicos)
- Saltar al diseño de plantillas sin fijar fundamentos → inconsistencia desde la base.
- Sistema demasiado complejo → nadie lo usa, vuelven a improvisar.
- No documentar el "no hagas" → se cometen los errores obvios.
- No entregar archivos editables → el sistema muere al primer pedido nuevo.
- Nadie mantiene el sistema → en 6 meses cada pieza es distinta otra vez.

## Mini-checklist
- [ ] ¿Tengo fundamentos fijos (color, tipo, escala, espaciado, grid)?
- [ ] ¿Diseñé una vez los componentes que más repito?
- [ ] ¿Tengo plantillas editables de mis piezas frecuentes?
- [ ] ¿Documenté "haz / no hagas" con ejemplos?
- [ ] ¿Un no experto puede producir una pieza correcta con esto?
- [ ] ¿Hay un responsable de mantener y versionar el sistema?

**Siguiente paso:** con el sistema en pie, formaliza todo en el manual de marca (brand guidelines) — el documento que protege y comunica la identidad. Con esto cierras el bloque 5 (composición y diseño gráfico) y conectas con la identidad de marca.
