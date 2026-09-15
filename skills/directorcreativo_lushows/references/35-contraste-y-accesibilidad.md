# 35 — Contraste y accesibilidad

Un color que se ve precioso pero no deja leer el texto es un color FALLIDO. La accesibilidad no es caridad: es que tu botón, tu precio y tu llamado a la acción los pueda leer TODO el mundo, incluidos los 1 de cada 12 hombres con daltonismo. Esto es lo que necesitas para no fallar.

## Ratio de contraste (el número que importa)
El **ratio de contraste** mide la diferencia de luminosidad entre dos colores (texto vs fondo). Va de **1:1** (idénticos, ilegible) a **21:1** (negro sobre blanco, máximo). Cuanto mayor el número, más legible.

No lo calculas a ojo: una herramienta te da el ratio (ver abajo). Tu trabajo es cumplir el mínimo.

## WCAG: los mínimos oficiales
WCAG (Web Content Accessibility Guidelines) es el estándar mundial de accesibilidad. Define dos niveles:

| Elemento | AA (mínimo legal/profesional) | AAA (óptimo) |
|---|---|---|
| Texto normal (< 18px / 24px) | **4.5:1** | **7:1** |
| Texto grande (≥ 24px, o ≥ 18.66px bold) | **3:1** | **4.5:1** |
| Iconos / bordes de UI / gráficos | **3:1** | — |

**Regla práctica:** apunta a AA (4.5:1) para todo texto como MÍNIMO. AAA donde puedas, sobre todo en cuerpos de texto largos.

## Ejemplos reales
| Texto / Fondo | Ratio | ¿Pasa? |
|---|---|---|
| Negro `#000` / Blanco `#FFF` | 21:1 | AAA ✓ |
| Gris `#767676` / Blanco | 4.54:1 | AA texto normal ✓ (justo) |
| Gris claro `#999` / Blanco | 2.85:1 | ✗ falla todo |
| Blanco / Verde `#2E7D32` | 4.9:1 | AA ✓ (botón legible) |
| Blanco / Ámbar `#F2A900` | 1.9:1 | ✗ el texto blanco sobre amarillo NO se lee |
| Negro / Ámbar `#F2A900` | 11:1 | AAA ✓ (sobre amarillo, texto NEGRO) |

Lección clave: **el amarillo/ámbar casi nunca lleva texto blanco** — usa texto oscuro. Es un error clásico.

## Daltonismo: no dependas SOLO del color
Cerca del **8% de los hombres** (y ~0.5% de mujeres) tiene algún tipo de daltonismo. El más común (deuteranopía/protanopía) confunde **rojo y verde**. Implicaciones:
- Un "rojo = malo / verde = bueno" sin nada más es INVISIBLE para ellos.
- Gráficos que distinguen series solo por color rojo/verde = inservibles.

**Solución — refuerza el color con OTRA señal:**
- [ ] Iconos o formas (✓ / ✗, no solo verde/rojo).
- [ ] Texto/etiqueta ("Éxito", "Error").
- [ ] Patrones o texturas en gráficos.
- [ ] Posición / orden, no solo color.
- [ ] Subrayado en enlaces, no solo color distinto.

Prueba: si pones tu diseño en escala de grises, ¿se sigue entendiendo? Si sí, no dependes solo del color.

## Otras trampas frecuentes
- **Texto sobre foto**: el contraste cambia según la zona de la imagen. Usa una capa oscura/clara (overlay) o caja detrás del texto.
- **Placeholder gris clarito** en formularios: suele fallar AA. Es texto, debe leerse.
- **Estados hover/disabled**: también deben mantener contraste razonable.
- **Modo oscuro**: el primario que pasaba AA en blanco puede fallar en negro. Verifica AMBOS modos.

## Herramientas para verificar (gratis)
- **WebAIM Contrast Checker** — pega dos HEX, te da el ratio y si pasa AA/AAA. El estándar.
- **Coolors Contrast Checker** — rápido, visual.
- **Adobe Color – Accessibility tools** — chequea contraste y simula daltonismo.
- **Stark** (plugin de Figma/Sketch) — verifica y simula daltonismo en el diseño.
- **Chrome DevTools** — muestra el ratio al inspeccionar texto.
- Simuladores de daltonismo (Coblis, Color Oracle) — ve tu diseño como lo ven ellos.

## Proceso de verificación
1. Lista cada combinación texto/fondo de tu sistema (botón, links, cuerpo, sobre primario...).
2. Pasa cada una por el contrast checker.
3. Ajusta valor (oscurece el texto o el fondo) hasta llegar a 4.5:1 mínimo.
4. Revisa en escala de grises que nada dependa solo del color.
5. Simula daltonismo en las señales rojo/verde.
6. Documenta las combinaciones APROBADAS en el manual (ver 34).

## Cómo arreglar un contraste que falla
No cambies el matiz (perderías la marca): **ajusta el VALOR** (luminosidad).
- Texto oscuro que no pasa → más oscuro aún (baja valor).
- Botón claro con texto blanco → oscurece el botón, o cambia el texto a oscuro.
- Si el primario no sirve de fondo de texto, crea una variante más oscura del MISMO matiz solo para esos casos.

## Mini-checklist
- [ ] Todo texto normal cumple 4.5:1 (AA) mínimo.
- [ ] Texto grande cumple 3:1.
- [ ] Verifiqué cada combinación con una herramienta, no a ojo.
- [ ] Nada depende SOLO del color (hay icono/texto/forma de refuerzo).
- [ ] Probé en escala de grises y simulé daltonismo.
- [ ] El amarillo/ámbar lleva texto OSCURO, no blanco.
- [ ] Revisé modo claro Y oscuro.

**Siguiente paso:** ya que la paleta es legible, ubícala dentro de los códigos de su industria y cultura en 36.
