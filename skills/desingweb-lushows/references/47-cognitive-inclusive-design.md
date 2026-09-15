# 47 — Accesibilidad cognitiva & diseño inclusivo

Más allá del WCAG/ARIA técnico (ref 16): la capa humana, cognitiva, de neurodiversidad e inclusión. **Léelo para que un sitio funcione con el rango más amplio de humanos.** Mentalidad: **diseña para el usuario cognitivamente sobrecargado** (cansado, ansioso, con prisa, en su 2º idioma, en móvil bajo el sol) — si funciona para él, funciona para todos (*curb-cut effect*). Pareja de 16, 17 (copy), 19.

## 1. Accesibilidad cognitiva — los 8 objetivos W3C COGA

Del documento *Content Usable* (W3C):
1. **Entender qué es cada cosa:** headings que resumen, jerarquía y patrones *familiares* (no reinventes la UI), diseño consistente entre páginas, controles claramente clickeables, iconos familiares + texto.
2. **Encontrar lo que se necesita:** destaca tareas clave, estructura comprensible, secciones separadas con divisores/headings/whitespace, info crítica visible **sin scroll**, búsqueda con autocompletado tolerante a errores.
3. **Contenido claro** (§3).
4. **Evitar errores y corregirlos:** nada de movimiento inesperado de controles, acciones **reversibles** (undo), revela costos *antes*, labels pegados al campo, acepta varios formatos de entrada, **guarda el progreso** (no pierdas datos por timeout), feedback que explica, confirmación antes de destructivo.
5. **Mantener el foco:** minimiza interrupciones (pop-ups/notificaciones), rutas críticas **cortas**, evita sobrecarga por página, informa requisitos *antes* de empezar.
6. **No depender de la memoria:** login sin memorizar (passkeys/magic links/"recuérdame"), no exijas cálculos ni recordar datos previos, muestra de nuevo lo ya escrito.
7. **Ayuda y soporte:** contacto humano real, versiones simplificadas, ayuda contextual en forms, recordatorios.
8. **Adaptación/personalización:** deja controlar cambios, ocultar lo no esencial, usar sus preferencias (§6).
**Reglas de oro:** un paso = una idea; numera pasos; muestra dónde está el usuario (breadcrumbs/progreso); nunca solo color para significado; navegación idéntica en todo el sitio.

## 2. Neurodiversidad — do's por grupo

**Dislexia** (es procesamiento del *lenguaje*, no solo visual): sans limpias (**Lexend, Atkinson Hyperlegible, Verdana, Tahoma**); sobre **OpenDyslexic la evidencia es contradictoria** (Wery & Diliberto 2017 no halló mejora) → ofrécela como *opción*, nunca por defecto/única solución; `line-height:1.5-1.8`, espaciado amplio, **alineación a la izquierda NUNCA justificado** (los "ríos" rompen la lectura); párrafos cortos, ~70-80 car/línea, permite cambiar tamaño/fondo (evita blanco puro brillante → off-white/crema).
**TDAH:** elimina distracciones (nada de autoplay video/audio, carruseles solos, pop-ups, exceso de links); foco claro y único, jerarquía fuerte, *chunking* en bloques cortos con bullets; barras de **progreso** (sensación de avance); sin límites de tiempo (o extensibles).
**Autismo:** **predecibilidad** total (navegación consistente, nada que salte sin acción); **lenguaje literal** (evita metáforas/idioms/sarcasmo — "está chupado" → explícalo); sensorial (colores suaves no neón, sin parpadeos/movimiento brusco/sonido inesperado, respeta `prefers-reduced-motion`); instrucciones concretas (números, no "pronto"/"varios").

## 3. Lenguaje claro (plain language)

Nivel de lectura **6º-8º grado**, frases de **15-20 palabras** · **voz activa, presente** ("Haz clic en Guardar") · evita jerga (o explícala en un clic), cero double-negatives · lo importante primero (pirámide invertida) · headings descriptivos, listas, párrafos cortos, **negrita** para lo clave (no MAYÚSCULAS/cursiva/subrayado para énfasis) · **iconos + texto** (nunca icono solo) · **error accionable**: qué pasó + por qué + cómo arreglarlo ("El correo necesita una @. Ej: nombre@correo.com"), junto al campo, texto+icono+color.

## 4. Baja visión, motora & situacional

**Baja visión:** soporta **zoom 200% (mín) y 400%** con **reflow** (sin scroll horizontal, re-fluye a una columna); contraste alto; nunca `px` fijos que ignoren el zoom (usa `rem`); respeta la hoja de estilo del usuario.
**Motora:** target **24×24px** (WCAG 2.2 AA) / **44×44px** ideal (AAA, úsalo en móvil); espaciado entre targets; evita precisión/timing; **nunca solo drag-and-drop** (ofrece botones/click); todo por teclado; soporta voz.
**Situacional** ("todos estamos temporalmente discapacitados a veces"): una mano (bebé en brazos), sol (contraste), ruido (subtítulos), conexión lenta (`prefers-reduced-data`), distracción (rutas cortas). Diseñar para estos beneficia a todos.

## 5. Principios inclusivos & business case

**Microsoft Inclusive Design — 3 principios:** (1) reconoce la exclusión; (2) **resuelve para uno, extiende a muchos**; (3) diseña **CON, no PARA** ("nada sobre nosotros sin nosotros").
**Persona Spectrum** — cada necesidad en 3 grados: **permanente** (una mano) → **temporal** (brazo roto) → **situacional** (cargando algo). Diseñar para lo permanente captura a los demás (de miles a +20M). Es el **curb-cut effect** (la rampa sirve a coches de bebé, maletas, repartidores).
**Business case:** mercado más grande (1.300M con discapacidad + familias, ~$13B de gasto) · mejor UX para todos · mejor SEO (semántica) · cobertura legal (ADA, **EAA vigente 2025**, demandas). Diseña sin asumir género/edad/cultura/idioma/nivel tecnológico.

## 6. Implementación 2026 — respeta las preferencias

```css
@media (prefers-reduced-motion: reduce){ *{ animation:none!important; transition:none!important; scroll-behavior:auto!important } }
@media (prefers-contrast: more){ :root{ --fg:#000; --bg:#fff } }
@media (prefers-reduced-data: reduce){ /* sin webfonts/imágenes pesadas/video */ }
@media (forced-colors: active){ /* respeta alto contraste del SO; forced-color-adjust con cuidado */ }
```
Respeta `font-size`/zoom del navegador (usa `rem`), `prefers-reduced-transparency`, y ofrece un **panel de personalización propio** (tamaño de texto, espaciado, tema, modo "lectura simple", apagar animaciones).
**IA para a11y (2026):** alt-text auto, subtítulos en vivo, simplificación a "easy read", navegación por voz — útiles pero **verifica**, no sustituyen el diseño accesible base.
**WCAG 3.0 (Working Draft):** dirección **basada en resultados** (no pass/fail), scoring 0-4, niveles **Bronze/Silver/Gold** (Bronze ≈ WCAG 2.2 AA como nuevo piso; Silver exige validación con usuarios con discapacidad). Adopción ~2027-2030.
**Testea CON personas con discapacidad reales** — el paso más crítico (no solo tus usuarios actuales; busca a los excluidos).

## Inclusive-design anti-patterns — blacklist
muros de texto sin headings/listas/whitespace · autoplay (video/audio/carrusel) o parpadeo no pausable · sobrecarga cognitiva (demasiadas opciones/densidad/interrupciones) · límites de tiempo sin extender / pérdida de datos por timeout · jerga/idioms/metáforas/double-negatives sin explicar · targets <24px o pegados / drag-only sin alternativa · color como único canal (errores solo en rojo, links solo por color) · texto justificado, blanco puro brillante, fuentes decorativas para cuerpo · ignorar `prefers-*` (forzar animación/contraste/tema; `px` que rompen el zoom) · no respetar reflow a 400% · errores inútiles ("Error 422") sin causa ni solución · CAPTCHAs visuales/cognitivos sin alternativa; login que depende de memoria · diseñar PARA sin testear CON usuarios reales.
