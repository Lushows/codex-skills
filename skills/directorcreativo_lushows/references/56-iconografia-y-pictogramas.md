# 56 — Iconografía y pictogramas

Un ícono es un **símbolo gráfico simple** que representa una idea, objeto o acción. Un sistema de íconos consistente hace que una marca se sienta profesional y ordenada; un set de íconos descoordinados la delata como amateur al instante. La regla madre: **todos tus íconos deben parecer dibujados por la misma mano.**

## Ícono vs pictograma
- **Ícono:** símbolo en interfaces y comunicación (un sobre = email, una lupa = buscar).
- **Pictograma:** símbolo de señalética/orientación, suele estar solo, sin texto (baño, salida, no fumar). Más universal y reductivo.
Ambos siguen las mismas reglas de consistencia; el pictograma exige aún más simplicidad porque se lee de lejos y sin contexto.

## Las variables que DEBEN ser consistentes
Un sistema coherente fija reglas para TODAS estas variables y no las viola:

| Variable | Decisión a tomar | Ejemplo |
|---|---|---|
| **Grid base** | Tamaño de caja donde se dibujan todos | 24×24 px con área segura interior |
| **Grosor de línea (stroke)** | El MISMO en todos | 2 px parejo |
| **Estilo** | Línea (outline) vs relleno (filled) vs dos tonos | Elige uno como principal |
| **Esquinas** | Redondeadas o rectas, y cuánto | Radio 2 px en todas |
| **Terminaciones** | Puntas rectas o redondas (line cap) | Redondas en todo |
| **Nivel de detalle** | Igual de simples todos | Sin detalles en unos y muchos en otros |
| **Ángulos** | Misma lógica geométrica | Ej. solo 0/45/90° |
| **Perspectiva** | Plana frontal (casi siempre) | Nada de 3D mezclado con plano |

Si un ícono tiene línea de 2 px y otro de 3 px, o uno es de línea y otro relleno, el sistema se rompe. La consistencia se nota más que el dibujo.

## Línea vs relleno: cuándo cada uno

| | Línea (outline) | Relleno (filled) |
|---|---|---|
| Sensación | Ligero, moderno, elegante | Sólido, claro, contundente |
| Legible en tamaño chico | Menos (líneas se cierran) | Más |
| Uso típico | UI, web, marcas premium | Apps móviles, señalética, estados "activos" |
| Truco común | Línea por defecto, relleno al estar activo/seleccionado | — |

Puedes usar un sistema **dual** (línea + relleno) si lo defines como par coherente: misma silueta, mismo grid.

## Cómo construir un sistema de íconos (proceso)
1. **Define el grid y el área segura.** Ej. caja de 24 px con 2 px de margen interno. Todos los íconos viven ahí.
2. **Fija el grosor de línea único.** Ej. 2 px. Inquebrantable.
3. **Define el lenguaje formal:** esquinas (radio), terminaciones (cap), ángulos permitidos, nivel de simplificación. Anótalo.
4. **Dibuja 3 íconos "ancla"** muy distintos (ej. casa, usuario, carrito). Si esos tres se ven hermanos, el lenguaje está bien.
5. **Extiende el set** respetando las reglas. Cada ícono nuevo se mide contra los anclas.
6. **Prueba en tamaño real** (16, 24, 32 px). Si a 16 px se vuelve mancha, simplifica.
7. **Prueba en grupo:** pon 20 juntos. ¿Parecen una familia? ¿Pesan visualmente igual? Ajusta el que destaque por densidad.
8. **Documenta** el sistema (ver 59 y manual de marca).

## Pictogramas de señalética (lección de los maestros)
Cuando el símbolo debe leerse de lejos, sin texto, sin idioma:
- **Reduce a lo esencial.** Quita todo lo que no sea indispensable para reconocer la idea.
- **Silueta clara.** Se debe entender en negativo, a contraluz, pequeño.
- **Geometría sistemática.** Misma lógica de ángulos y proporciones en todos.
- **Universalidad.** Evita referencias culturales que no se entiendan en otro país.

**Otl Aicher** creó los pictogramas de los **Juegos Olímpicos de Múnich 1972**: un sistema basado en una **grilla con ángulos de 0°, 45° y 90°** que volvió cada figura humana reconocible y unificada. Es el manual de oro de la pictografía moderna y la base de la señalética que hoy ves en aeropuertos.

## Errores típicos (no técnicos)
- Descargar íconos de fuentes distintas → grosores y estilos que no combinan. Usa UN solo set o líbrería coherente.
- Mezclar línea y relleno sin regla → se ve descuidado.
- Íconos con demasiado detalle → se vuelven mancha en tamaño chico.
- Pesos visuales dispares (uno denso, otro fino) → el set "salta".
- Íconos que necesitan explicación → si hay que rotularlos todos, no funcionan; refuérzalos con texto o rediséñalos.

## Consejo práctico para el no técnico
La forma más segura de tener íconos consistentes sin saber dibujar: **adopta una sola librería coherente** (ej. una familia completa de íconos con un mismo estilo y grosor) y úsala SIEMPRE. No mezcles. Si necesitas uno que no existe, pídelo en el mismo estilo (mismo grid, mismo stroke). Un set unido vale más que íconos "más lindos" pero dispares.

## Referentes
- **Otl Aicher** — pictogramas de Múnich 1972; señalética sistemática.
- **AIGA / DOT** — set de símbolos de transporte (los del aeropuerto).
- **Susan Kare** — íconos originales de Macintosh (pixel-perfect, carácter).
- **Gerd Arntz / Isotype (Otto Neurath)** — pictogramas para datos.

## Mini-checklist
- [ ] ¿Todos comparten grid y área segura?
- [ ] ¿El grosor de línea es idéntico en todos?
- [ ] ¿Elegí un estilo (línea/relleno) y lo mantengo?
- [ ] ¿Esquinas, terminaciones y ángulos siguen una regla?
- [ ] ¿Se leen bien a 16 px?
- [ ] Al ver 20 juntos, ¿parecen una familia con peso parejo?

**Siguiente paso:** si la marca usa dibujos además de íconos, define tu estilo ilustrativo propio (ver 57).
