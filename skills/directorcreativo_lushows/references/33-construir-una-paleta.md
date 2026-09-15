# 33 — Construir una paleta

Una paleta de marca no es "los colores que me gustan": es un sistema con roles, proporciones y valores reproducibles. Aquí está el proceso paso a paso para construir una que se vea profesional y funcione en web, imprenta y todos los soportes.

## Los roles de una paleta (qué hace cada color)
Toda paleta sólida tiene 4 tipos de color con funciones distintas:

1. **Primario (color de marca)** — el que la gente asocia contigo. Sale de la psicología + sector (ver 31, 36). Es el protagonista: logo, headers, elementos clave.
2. **Secundarios (1–2)** — apoyan al primario, dan riqueza y permiten variar sin perder identidad. Salen de la armonía elegida (ver 30).
3. **Neutros (escala de grises + base)** — blancos, grises y casi-negros. Son el 70%+ de cualquier diseño real: fondos, textos, bordes. Subestimados pero CRÍTICOS.
4. **Acento (1)** — color de alta energía para CTAs y elementos que deben saltar ("Comprar", alertas, destacados). Se usa POCO; ese es su poder.

## La regla 60-30-10 (la proporción que da equilibrio)
Es el secreto de por qué unas paletas se ven pro y otras caóticas. Distribuye el color así:
- **60% — color dominante** (normalmente un neutro o el primario suave): fondos, grandes áreas.
- **30% — color secundario**: secciones, apoyo visual.
- **10% — color de acento**: botones, llamados, detalles que deben destacar.

Esta jerarquía por CANTIDAD es lo que evita que dos colores fuertes peleen. Aplica igual en una web, un empaque o un afiche.

## ¿Cuántos colores?
- **Núcleo de marca: 2 a 4 colores** (1 primario + 1–2 secundarios + 1 acento).
- **+ una escala de neutros** (4–6 grises del casi-blanco al casi-negro).
- **+ colores de estado** si es producto digital: éxito (verde), error (rojo), aviso (amarillo).
Más de 4 colores de marca = difícil de cohesionar y de recordar. **Menos es más memorable** (piensa en Coca-Cola: rojo + blanco).

## Proceso paso a paso
1. **Define el sentimiento** (2–3 palabras) y el sector. → 31 y 36.
2. **Elige el primario** que respalde ese sentimiento.
3. **Elige una armonía** (análoga, complementaria dividida, etc.) → 30. De ahí salen los secundarios.
4. **Elige el acento**: suele ser el complementario del primario, MUY saturado, para que salte.
5. **Construye los neutros**: NO uses gris puro `#808080`. Tíñelos levemente con el matiz del primario (un gris con una gota de tu verde) para cohesión. Crea 4–6 pasos del claro al oscuro.
6. **Ajusta saturación/valor** de todo para el tono emocional (lujo=oscuro/desaturado; juvenil=claro/saturado).
7. **Verifica contraste** de texto sobre fondos (ver 35). Si el acento no contrasta, no sirve de botón.
8. **Documenta cada color** con sus 4 valores (ver 32).

## Plantilla de entrega (esto es lo que se entrega al cliente)
```
PALETA — [Marca]

PRIMARIO · Verde Vital
  HEX #2E7D32 · RGB 46,125,50 · CMYK 78,18,100,5 · Pantone 7740 C
  Uso: logo, encabezados, elementos de marca.

SECUNDARIO · Terracota
  HEX #C75D3A · RGB 199,93,58 · CMYK 16,72,80,4 · Pantone 7416 C
  Uso: apoyo, secciones, fotografía.

ACENTO · Ámbar
  HEX #F2A900 · RGB 242,169,0 · CMYK 4,35,100,0 · Pantone 130 C
  Uso EXCLUSIVO: botones y llamados a la acción.

NEUTROS
  Casi-blanco  #F7F8F5
  Gris claro   #D8DCD4
  Gris medio   #8A8F86
  Texto        #2A2E27
  Casi-negro   #14160F

ESTADOS (si es digital)
  Éxito #2E7D32 · Error #D32F2F · Aviso #F2A900
```

## Cómo elegir bien los neutros (el detalle pro)
- Parte de tu primario, baja saturación casi a cero y ajusta el valor → obtienes grises "de la familia".
- Define al menos: fondo claro, fondo alterno, borde, texto secundario, texto principal.
- El "negro" de marca rara vez es `#000000` puro: un casi-negro tintado se ve más caro y menos duro.

## Errores típicos
- [ ] Demasiados colores de marca (4+) → marca difusa, nadie la recuerda.
- [ ] Sin acento → todo se ve plano, nada destaca, los CTAs se pierden.
- [ ] Grises puros sin teñir → la paleta se siente "desarmada".
- [ ] No definir proporciones → cada pieza usa los colores distinto = inconsistencia.
- [ ] Entregar solo HEX → imprenta y soportes quedan al azar (ver 32).
- [ ] Acento sin contraste suficiente → el botón no se lee (ver 35).

## Mini-checklist
- [ ] Tengo primario, secundario(s), neutros y acento, con rol definido.
- [ ] Apliqué 60-30-10 (jerarquía por cantidad).
- [ ] Máximo 4 colores de marca + escala de neutros.
- [ ] Cada color tiene HEX, RGB, CMYK y Pantone.
- [ ] El texto contrasta sobre todos los fondos (ver 35).
- [ ] Documenté el USO de cada color, no solo el valor.

**Siguiente paso:** convierte esta paleta en un sistema gobernable con nombres semánticos y reglas en 34.
