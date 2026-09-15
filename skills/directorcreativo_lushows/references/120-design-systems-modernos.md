# 120 — Design systems modernos

Un manual de marca (ver 80) dice cómo se ve la marca. Un **design system** va más lejos: es un kit de piezas reales, reutilizables y conectadas —colores, botones, tarjetas, formularios— que diseñadores y programadores usan para construir productos digitales sin reinventar nada cada vez. Es la diferencia entre tener un libro de recetas y tener una cocina industrial montada.

## Qué es (en simple)
Un design system es el **conjunto vivo** de:
- **Tokens** — los valores base: colores, tamaños de letra, espacios (ver 87 y 121).
- **Componentes** — piezas listas: botón, input, tarjeta, modal.
- **Patrones** — combinaciones que resuelven una tarea: un formulario de registro, una tabla con filtros.
- **Guías** — cómo y cuándo usar cada cosa, con ejemplos.
- **Código** — los componentes existen también como código real, no solo como dibujo.

No es solo un archivo de Figma bonito. Es la fuente única de verdad que mantiene un producto (o muchos) coherente mientras crece.

## Atomic Design (el modelo mental que todos usan)
Brad Frost propuso pensar la interfaz como química, de lo pequeño a lo grande:

| Nivel | Qué es | Ejemplo |
|---|---|---|
| Átomos | Lo mínimo, no se divide más | un color, un botón, un input |
| Moléculas | 2-3 átomos juntos | input + label + botón = barra de búsqueda |
| Organismos | Bloques completos | un header, una tarjeta de producto |
| Plantillas | Estructura de página sin contenido real | layout de un dashboard |
| Páginas | Plantilla con contenido real | el dashboard de un cliente concreto |

No es dogma —pocos equipos clasifican todo con rigor— pero da un vocabulario compartido brutalmente útil para hablar de "de qué está hecha" una pantalla.

## Las capas (cómo se conecta todo)
```
TOKENS        →  color-primary, space-4, font-body
   ↓ alimentan
COMPONENTES   →  Botón, Input, Tarjeta (usan tokens)
   ↓ se combinan en
PATRONES      →  Formulario, Tabla, Navegación
   ↓ arman
PÁGINAS       →  pantallas reales del producto
```
La clave: si cambias un token (el verde primario), se actualiza hacia arriba en todos los componentes y páginas. Una sola edición, efecto global. Esa es la magia (y por eso 121 sobre tokens es el corazón del sistema).

## Referentes reales que vale estudiar
- **Material Design 3** (Google) — el más completo y didáctico; tokens, theming dinámico.
- **Apple HIG** (Human Interface Guidelines) — principios y patrones de iOS/macOS.
- **Polaris** (Shopify) — excelente para e-commerce y tono de voz.
- **Carbon** (IBM) — robusto, empresarial, muy documentado.
- **Spotify Encore** — multi-plataforma y multi-marca real.
- **Airbnb DLS** (Design Language System) — pionero en componentes ↔ código.

Mira cómo documentan un botón: estados, tamaños, cuándo NO usarlo. Ese nivel de detalle es el estándar (ver 59 sistemas de diseño visual para la versión gráfica/no-digital).

## ¿Cuándo construir uno? (la pregunta honesta)
Construir un design system cuesta tiempo y dinero. No siempre vale la pena.

**SÍ tiene sentido cuando:**
- [ ] Tienes un producto digital que crecerá (app, dashboard, e-commerce propio).
- [ ] Hay varias personas tocando la interfaz (diseñador + dev, o varios devs).
- [ ] Repites las mismas piezas en muchas pantallas.
- [ ] Tienes varias marcas o productos que deben sentirse parientes (ver 125).

**NO lo necesitas (todavía) cuando:**
- [ ] Es una sola landing estática.
- [ ] Eres una persona haciendo todo y el proyecto es chico.
- [ ] Aún no validas el producto (no sistematices algo que puede cambiar entero).

Para Lushows: empieza por un **mini-sistema** —tokens de color/tipo/espacio + 5 componentes clave (botón, input, tarjeta, header, footer)— antes de soñar con Carbon. Crece cuando duela la inconsistencia, no antes.

## Las 3 mentiras del design system
1. *"Es solo una librería de Figma."* No: sin código y sin reglas de uso, es decoración.
2. *"Se hace una vez y listo."* No: es **vivo**, se mantiene o muere (ver 123 y 124).
3. *"Frena la creatividad."* Al revés: libera tiempo de lo repetitivo para pensar lo difícil.

## Señales de que YA necesitas uno
- El verde de la marca tiene 6 versiones distintas en el producto.
- Cada pantalla nueva tarda el doble porque "rehacemos el botón".
- Diseño dice una cosa y el producto en vivo se ve diferente.
- Nadie sabe cuál es la versión "buena" de un componente.

## Mini-checklist de arranque
- [ ] Defino tokens base (color, tipografía, espaciado) — ver 121
- [ ] Elijo 5-8 componentes esenciales primero
- [ ] Cada componente tiene estados (normal, hover, foco, deshabilitado, error)
- [ ] Hay reglas do/don't escritas — ver 123
- [ ] Existe en Figma Y en código (aunque sea simple)
- [ ] Alguien es responsable de mantenerlo — ver 124

**Siguiente paso**: el cimiento de todo sistema son los tokens. Antes de dibujar componentes, define los valores reutilizables con rigor — pasa a 121 design tokens avanzado.
