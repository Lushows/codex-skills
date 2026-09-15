# 126 — Diseño responsivo y fluido

Una interfaz se ve en un celular de 360 px y en un monitor de 2560 px. Que se vea bien en ambos —y en todo lo del medio— es **diseño responsivo**. Hacerlo bien a 2026 ya no es solo "poner breakpoints": es pensar en escalas **fluidas** que respiran con la pantalla. Este módulo explica responsive vs fluid, y las herramientas modernas (clamp, container queries, escala fluida) en términos que entiendas.

## Responsive vs fluid (la distinción clave)
| | Responsive (clásico) | Fluid (moderno) |
|---|---|---|
| Cómo cambia | a **saltos**, en breakpoints fijos | de forma **continua**, suave |
| Analogía | escaleras (escalón a escalón) | rampa (subida gradual) |
| Ejemplo | el texto salta de 16 a 20 px en tablet | el texto crece poco a poco entre móvil y desktop |
| Estado a 2026 | sigue vigente para layout | preferido para tipografía y espaciado |

Lo mejor combina ambos: **breakpoints** para reorganizar el layout (de 1 columna a 3) y **fluidez** para que letras y espacios escalen sin saltos bruscos.

## Breakpoints (puntos de quiebre)
Un **breakpoint** es el ancho donde el layout cambia de estructura. No los inventes alrededor de dispositivos concretos (cambian cada año); ponlos **donde el contenido se rompe**.
```
~640px   → de móvil a layout más ancho
~768px   → tablet
~1024px  → desktop
~1280px+ → desktop amplio
```
Filosofía **mobile-first**: diseña primero lo chico (lo más restrictivo) y luego "agranda". Es más fácil expandir que comprimir.

## clamp(): la herramienta estrella del fluid
`clamp(mínimo, ideal, máximo)` define un valor que crece con la pantalla pero nunca se pasa de los límites. Es la base de la escala fluida:
```css
/* El título: nunca menor a 1.8rem, nunca mayor a 3rem,
   y en el medio crece con el ancho de pantalla */
font-size: clamp(1.8rem, 1rem + 3vw, 3rem);
```
- `1.8rem` → tope mínimo (en móvil no se hace ilegible de chico).
- `1rem + 3vw` → el valor que respira (`vw` = % del ancho de ventana).
- `3rem` → tope máximo (en monitor enorme no se vuelve gigante).

Una sola línea reemplaza tres breakpoints de tipografía. Aplícalo también a espaciados (`padding: clamp(1rem, 5vw, 4rem)`).

## Escala tipográfica fluida
En vez de tamaños fijos por breakpoint, define una escala que crece suave (ver 48 escalas y ritmo):
```css
--text-sm:  clamp(0.875rem, 0.8rem + 0.3vw, 1rem);
--text-base:clamp(1rem,    0.95rem + 0.4vw, 1.125rem);
--text-lg:  clamp(1.25rem, 1.1rem + 0.8vw, 1.5rem);
--text-xl:  clamp(1.8rem,  1.3rem + 2.5vw, 3rem);
```
Resultado: la jerarquía se mantiene proporcional en cualquier pantalla, sin docenas de media queries. Estos valores son **tokens** (ver 121): defínelos una vez, úsalos en todo.

## Container queries (la revolución reciente)
Hasta hace poco, los componentes solo podían reaccionar al tamaño de la **ventana**. Las **container queries** (ya soportadas ampliamente a 2026) permiten que un componente reaccione al tamaño de **su contenedor**, no de la pantalla.
```css
@container (min-width: 400px) {
  .card { display: grid; grid-template-columns: auto 1fr; }
}
```
Por qué es enorme para design systems: la **misma tarjeta** se adapta sola esté en una barra lateral estrecha o en una columna ancha, sin saber nada del layout global. Componente verdaderamente reutilizable. Es el complemento perfecto del pensamiento por componentes (ver 120).

## Imágenes y media responsivas
- Usa imágenes que sirvan el tamaño adecuado a cada pantalla (no cargues una foto de 4000 px en un móvil).
- Define proporciones (aspect-ratio) para que no haya saltos al cargar.
- Vectoriales (SVG) escalan sin pérdida — ideales para logos e íconos (ver 93).

## Errores comunes
- Diseñar solo para desktop y "ver luego el móvil" → casi siempre se rompe.
- Breakpoints atados a dispositivos de moda en vez de al contenido.
- Texto fijo que en móvil queda enorme o minúsculo → usa clamp().
- Tocar todo con media queries cuando una container query lo resuelve sola.
- No probar en el rango intermedio (se prueban móvil y desktop, pero el tablet queda roto).

## Para Lushows (no técnico)
No tienes que escribir el CSS, pero pide/verifica esto en cualquier web o dashboard: (1) que se vea bien en TU celular real, (2) que el texto no quede ni gigante ni microscópico, (3) que nada se salga de la pantalla en horizontal. El dashboard de BIO-SETA debe pasar esas tres pruebas en un teléfono de gama media.

## Mini-checklist
- [ ] Mobile-first: probado primero en pantalla chica
- [ ] Breakpoints según el contenido, no según dispositivos
- [ ] Tipografía y espaciados con clamp() (fluidos), como tokens
- [ ] Container queries para componentes reutilizables
- [ ] Imágenes que sirven el tamaño correcto + aspect-ratio
- [ ] Probado en el rango intermedio, no solo móvil y desktop

**Siguiente paso**: para que todo esto pase de diseño a producto sin fricción, hay que entregarlo bien. Pasa a 127 handoff diseño → desarrollo.
