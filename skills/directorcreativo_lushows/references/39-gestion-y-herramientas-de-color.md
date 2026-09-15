# 39 — Gestión y herramientas de color

De nada sirve elegir el color perfecto si en pantalla, imprenta y soportes sale distinto. La gestión de color es el conjunto de prácticas y herramientas que garantizan FIDELIDAD: que tu verde sea TU verde en todas partes. Aquí está el flujo profesional para un dueño no técnico.

## Perfiles ICC (qué son, en simple)
Un **perfil ICC** es un archivo que le dice a un dispositivo (monitor, impresora) cómo interpretar los colores para que coincidan con un estándar. Es el "traductor" de color entre dispositivos.
- **sRGB** — el estándar para WEB y la mayoría de pantallas. Si dudas en digital, usa sRGB. Es lo que ven los celulares y navegadores.
- **Adobe RGB** — gama más amplia; para fotografía/print profesional. NO lo uses para web (los navegadores lo muestran mal → colores apagados).
- **CMYK con perfil de imprenta** (ej. FOGRA39, GRACoL) — tu imprenta te dice CUÁL usar para convertir bien a tinta.

Regla práctica: **web = sRGB; imprenta = el perfil CMYK que indique tu imprenta.**

## Calibración de pantalla (el paso que casi nadie hace)
Tu monitor de fábrica MIENTE sobre los colores. Si diseñas en una pantalla descalibrada, todo saldrá mal sin que lo notes.
- **Calibrar** = ajustar el monitor a un estándar para que muestre colores reales.
- Profesional: un **colorímetro/sonda** (X-Rite i1Display, Datacolor Spyder) que mide y crea un perfil ICC para tu pantalla.
- Mínimo: usa la calibración del sistema (Windows/macOS tiene un asistente básico) y trabaja con buena luz neutra, sin reflejos.
- Trabaja con la pantalla a brillo medio (no al máximo): al máximo, todo se ve más vivo de lo que es.

## Prueba de color (proof) antes de imprimir grande
Antes de mandar 1.000 etiquetas, valida el color:
- **Proof digital certificado** — impresión de prueba calibrada que predice el resultado final.
- **Pantone físico** — compara tu color contra la guía Pantone real (en papel coated/uncoated según tu soporte, ver 32). Las guías se DECOLORAN con el tiempo: reemplázalas cada ~1–2 años.
- Pide a la imprenta una prueba ANTES de la tirada completa. Cuesta poco y evita desastres caros.

## Herramientas (gratis y de pago)
**Crear y explorar paletas:**
- **Coolols (coolors.co)** — genera paletas, ajusta, exporta. Rápido e ideal para empezar. Tiene checker de contraste.
- **Adobe Color (color.adobe.com)** — rueda con armonías (ver 30), extrae paletas de fotos, herramientas de accesibilidad y simulación de daltonismo. Gratis.
- **Khroma, Huemint** — generadores con IA para inspiración.
- **Paletton** — clásico para armonías sobre la rueda.

**Pantone y conversión:**
- **Pantone Connect** — busca Pantones, convierte a CMYK/RGB/HEX, organiza paletas. La fuente oficial.
- **Guías físicas Pantone** (Formula Guide) — el estándar para validar color impreso en mano.

**Accesibilidad (ver 35):**
- **WebAIM Contrast Checker**, **Stark** (Figma), **Color Oracle / Coblis** (simular daltonismo).

**Extraer color:**
- **Cuentagotas** de cualquier app de diseño, o **ColorZilla** (navegador) para sacar el HEX de cualquier web.

## Flujo de trabajo print-ready (paso a paso)
1. **Diseña en el modo correcto**: si va a imprenta, trabaja en CMYK desde el inicio (o convierte y AJUSTA, no confíes en la conversión ciega).
2. **Define colores críticos en Pantone** (logo, color de marca).
3. **Calibra tu pantalla** (o al menos trabaja en sRGB con luz neutra).
4. **Pide a la imprenta su perfil ICC** y úsalo al convertir/exportar.
5. **Exporta a PDF/X** (estándar de imprenta) con el perfil correcto incrustado.
6. **Incluye marcas y sangrado** si la pieza lo requiere (la imprenta te dice).
7. **Pide un proof** y compáralo contra tu Pantone físico.
8. **Aprueba el proof por escrito** antes de la tirada completa.

## Flujo digital (más simple)
1. Trabaja en **sRGB**.
2. Especifica en **HEX/RGB** (ver 32).
3. Verifica **contraste** (ver 35).
4. Revisa en VARIOS dispositivos (un celular barato, un monitor distinto) — así ves el rango real que verá tu cliente.

## Errores típicos
- [ ] Diseñar en una pantalla sin calibrar y sorprenderse del resultado impreso.
- [ ] Usar Adobe RGB para web (colores salen apagados en navegadores).
- [ ] Mandar a imprenta sin Pantone ni perfil → cada lote sale distinto.
- [ ] No pedir proof y descubrir el error en 1.000 unidades.
- [ ] Confiar en una guía Pantone vieja y decolorada.
- [ ] Revisar el color solo en TU pantalla, nunca en otras.

## Mini-checklist
- [ ] Trabajo en sRGB (digital) o CMYK + perfil de imprenta (print).
- [ ] Mis colores críticos tienen Pantone definido.
- [ ] Mi pantalla está calibrada o trabajo con luz neutra y brillo medio.
- [ ] Pedí el perfil ICC a mi imprenta.
- [ ] Exporté PDF/X para print.
- [ ] Pedí y aprobé un proof antes de la tirada.
- [ ] Revisé el color en varios dispositivos.

**Siguiente paso:** con la gestión resuelta, tu paleta (33) se reproducirá fiel en todos los soportes. Cierra el ciclo documentándola en el sistema de marca (34) y validando accesibilidad (35).
