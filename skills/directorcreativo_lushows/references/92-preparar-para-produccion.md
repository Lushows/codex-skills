# 92 — Preparar para producción

El momento donde más diseños mueren no es el diseño: es la entrega a imprenta. Un archivo mal preparado sale con colores apagados, textos movidos o bordes blancos. Este es el checklist que evita el desastre.

## Las dos producciones: print y digital
- **Print (imprenta):** etiquetas, tarjetas, empaques, brochures. Tinta sobre material físico. Reglas estrictas.
- **Digital (pantalla):** web, redes, apps. Luz emitida. Reglas distintas.

Confundirlas es el error clásico: un diseño en colores de pantalla (RGB) impreso sale opaco; una imagen de imprenta (300dpi, CMYK) subida a la web pesa de más.

## Conceptos clave en simple

| Término | Qué es | Print | Digital |
|---|---|---|---|
| **RGB** | Color por luz (rojo, verde, azul) | NO | SÍ |
| **CMYK** | Color por tinta (cian, magenta, amarillo, negro) | SÍ | NO |
| **DPI / PPI** | Densidad de puntos: nitidez al imprimir | 300 dpi | 72 dpi basta |
| **Sangrado (bleed)** | Margen extra de color que se recorta | 3 mm | no aplica |
| **Marcas de corte** | Líneas que indican dónde cortar | SÍ | no |
| **Trazar fuentes** | Convertir texto en formas vectoriales | SÍ (o incrustar) | no |
| **Perfil de color** | "Receta" de cómo se interpretan los colores | SÍ (pide a la imprenta) | sRGB |

## Checklist de PREPRENSA (print) — antes de mandar a imprimir
- [ ] **Modo de color: CMYK** (no RGB). Convierte y revisa que los colores no se apaguen feo.
- [ ] **Resolución: 300 dpi** en todas las imágenes incrustadas.
- [ ] **Sangrado: 3 mm** por cada lado en piezas con color hasta el borde.
- [ ] **Márgenes de seguridad:** texto y logos a 3–5 mm del borde de corte (que nada importante quede al filo).
- [ ] **Fuentes trazadas o incrustadas:** convierte el texto a curvas/contornos, o incrusta las fuentes en el PDF. Si no, la imprenta verá otra letra.
- [ ] **Negro correcto:** texto pequeño en negro 100% K (no negro "rico" de 4 tintas, que se ve borroso). Negros grandes/sólidos sí pueden llevar negro rico.
- [ ] **Tintas especiales (Pantone):** si la marca usa un color exacto (oro, un verde específico), defínelo como Pantone y avísale a la imprenta. Es más caro pero exacto.
- [ ] **Material y acabado definidos:** papel, mate/brillante, barniz, troquel. Habla con la imprenta ANTES de diseñar.
- [ ] **Exporta PDF de alta / PDF-X** con marcas de corte y sangrado.
- [ ] **Prueba de color (proof):** si el color es crítico, pide una prueba física antes de la tirada grande.

## Checklist de EXPORTACIÓN digital
- [ ] **Modo de color: RGB / sRGB.**
- [ ] **Resolución de pantalla:** no necesitas 300 dpi; optimiza para que pese poco.
- [ ] **Formato correcto:** JPG para fotos, PNG para transparencias, SVG para logos/íconos, WebP para web rápida (ver 93).
- [ ] **Tamaños múltiples:** prepara cada pieza en el tamaño que pide la plataforma (post cuadrado, historia vertical, etc.).
- [ ] **Comprime imágenes** para web sin que se vean pixeladas.
- [ ] **Logo en SVG y PNG** para que se use bien en cualquier lado.

## El error que arruina etiquetas (caso real frecuente)
Diseñar la etiqueta en RGB, con texto sin trazar, sin sangrado, exportada en PNG. La imprenta la rechaza o la imprime y sale: colores apagados, una letra cambiada, y un borde blanco donde debía haber color. **Los tres culpables:** RGB en vez de CMYK, fuente no trazada, falta de sangrado. Este checklist los mata a los tres.

## Habla con tu proveedor ANTES de diseñar
Cada imprenta tiene sus requisitos. La conversación de 5 minutos antes de empezar evita rehacer todo:
- ¿En qué formato quieres el archivo? (casi siempre PDF-X)
- ¿Cuánto sangrado? (normalmente 3 mm)
- ¿Perfil de color CMYK que usas?
- ¿Manejas Pantone? ¿Costo extra?
- ¿Qué materiales y acabados ofreces?

## Mini-checklist final antes de "Enviar a imprenta"
- [ ] CMYK ✓  300 dpi ✓  sangrado 3 mm ✓
- [ ] Fuentes trazadas/incrustadas ✓
- [ ] Márgenes de seguridad respetados ✓
- [ ] PDF-X con marcas de corte ✓
- [ ] Hablé con la imprenta y cumplo sus specs ✓
- [ ] (Si el color importa) pedí proof físico ✓

**Siguiente paso:** elige bien el formato de exportación según el destino — lee 93. Antes de entregar cualquier cosa, pásala por el QA de 98.
