# 99 · Título, miniatura y descripción

**Qué resuelve:** lo que decide si le dan al play. Un episodio impecable con mala
portada no se ve. Título y miniatura son **una sola pieza** y se diseñan juntos, antes
de terminar el montaje.

---

## El título

### Reglas
- **50-60 caracteres.** Lo que sobra se corta en el móvil, que es donde se decide.
- **Lo fuerte al principio.** La cifra o el nombre en las primeras palabras.
- **Una cifra concreta** siempre que exista. Concreto gana a redondo.
- **Sin signos de admiración ni mayúsculas gritadas.** El canal es frío; el título también.
- **Sin palabras que rebajen el CPM** (violencia, drogas, muerte explícita). El mismo
  caso se titula desde el dinero: es un cambio de foco, no una censura.
- **Promete exactamente lo que el episodio entrega** (§ `94`, el contrato con el gancho).

### Fórmulas que funcionan en este nicho

| Fórmula | Forma |
|---|---|
| **Nombre + mecanismo** | `<Nombre>: el negocio que movía <cifra> sin levantar sospechas` |
| **Cifra + pregunta operativa** | `<cifra> en efectivo: ¿dónde se guarda ese dinero?` |
| **El objeto tapadera** | `La fábrica de <producto> que ocultaba <cifra>` |
| **Contraste declarado/real** | `Declaraba <A>. Movía <B>.` |
| **El detalle que delató** | `Lo hundió <detalle mínimo>` |
| **Cómo se derrumbó** | `Cómo se derrumbó <imperio> en <tiempo>` |
| **La cuenta** | `<cifra> pesa <resultado>. Ese era el problema` |

**El nombre del protagonista va en el título** salvo que el enigma sea explícitamente
el eje. Y si va en el título, el gancho lo dice en voz (§ `94`).

## La miniatura es un contrato

La miniatura promete algo; el vídeo lo paga en los primeros 30 segundos. Si no lo paga,
la retención se hunde y el algoritmo castiga al canal entero, no sólo a ese vídeo.

### Reglas de construcción
- **Tres elementos como máximo:** sujeto, cifra u objeto, y fondo. Nada más.
- **Legible a 210 px de ancho.** Se comprueba reduciendo la imagen a ese tamaño; lo que
  no se lee ahí, no existe.
- **3 o 4 palabras**, en la tipografía de titular del canal (§ `42`).
- **El texto de la miniatura no repite el título**, lo completa. Juntos dicen dos cosas.
- **Lenguaje visual del canal**: collage de revista, recorte con margen de papel,
  sombra y ángulo (SKILL.md). Es lo que hace reconocible al canal en una parrilla.
- **Un punto de color** contra el fondo oscuro. Una miniatura marrón desaparece.
- **Derechos:** la foto es de dominio público verificado o gráfico propio. **Nunca una
  cara real generada con IA.** Si no hay retrato libre, la miniatura se hace con el
  objeto, el documento o la cifra: suelen funcionar mejor.
- **Cara mirando a cámara si la hay** y es libre; el ojo va primero a los ojos.

### Variantes
Preparar dos o tres versiones que apuesten por cosas distintas —cifra / objeto / rostro—
y quedarse con la que se lee más rápido a tamaño pequeño. Si la plataforma permite
probar variantes, se prueba; si no, se compara con el resto del canal en una parrilla.

## La descripción

Estructura fija:

```
[Líneas 1-2]  El gancho en texto: la afirmación completa con la cifra.
              Es lo que se ve sin desplegar y lo que lee el buscador.

[Bloque 2]    Qué explica el episodio, en 3-4 líneas, con las palabras que
              alguien buscaría (nombre, empresa, tipo de fraude, país, año).

[Capítulos]   00:00 Gancho
              00:50 El origen
              ...        (marcas de tiempo reales; mejoran la navegación)

[FUENTES]     Documento 1 — organismo, año — URL
              Documento 2 — organismo, año — URL
              ...

[ARCHIVO]     Material de dominio público (indicar organismos).
              Gráficos, mapas y reconstrucciones: producción propia.
              Música y efectos: sintetizados para este episodio.

[AVISO]       Contenido informativo basado en documentos públicos.
              Los hechos aún no juzgados se presentan como alegaciones.

[CANAL]       Una línea de identidad + enlace a la lista de reproducción.
```

**Las fuentes se citan de verdad, con enlace.** Es lo que separa al canal de un
recopilador, lo que responde a la primera acusación de "esto es IA" y lo que sostiene
una reclamación si alguien se queja. Las mismas entradas están en `archivo/fuentes.json`
(§ `90`).

## Localización de metadatos

**El desbloqueo de SEO en otro idioma es el título traducido, no el audio.** Una pista
de audio doblada no posiciona el vídeo en las búsquedas de ese idioma; los metadatos
localizados sí.

Por cada idioma con pista de audio (inglés, alemán, japonés, francés, español,
portugués) se localizan:

1. **Título** — traducido y **reescrito** con la fórmula que funcione en ese idioma, no
   traducido palabra por palabra. Se respeta el límite de caracteres en cada uno.
2. **Descripción** — al menos el bloque 1-2 y las palabras de búsqueda. Las fuentes y
   el aviso pueden quedar en el idioma original.
3. **Subtítulos** — subidos como pista de texto; también son señal de búsqueda.
4. **La miniatura no se localiza** salvo que el texto sea decisivo; entonces se hace
   una variante con la misma composición.

Recordatorio de la pista de audio: debe durar **lo mismo** que el vídeo (más de un
segundo de diferencia se rechaza), y se cuadra con `atempo` entre 0,85 y 1,15; si no
cuadra, se acorta el texto, no se estira la voz (SKILL.md).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Título que promete lo que el vídeo no entrega | Retención hundida; el algoritmo castiga al canal completo |
| Miniatura con cinco elementos | A 210 px no se lee nada y no se distingue de las demás |
| Texto de la miniatura igual que el título | Se desperdicia la mitad del espacio de comunicación |
| Cara real generada con IA en la portada | Riesgo legal y de retirada; regla roja del canal |
| Título con vocabulario de violencia o drogas | Icono amarillo y CPM hundido en un nicho de $15-30 |
| Descripción de dos líneas sin fuentes | Pierde búsqueda y pierde la defensa documental |
| Traducir el título literalmente | Deja de funcionar como gancho en ese idioma |
| Doblar el audio y no localizar los metadatos | Se paga el trabajo del doblaje sin el alcance que lo justifica |
| Diseñar la portada cuando el vídeo ya está subido | La portada condiciona el gancho; se decide antes |

## Relacionado

`94` el gancho de dinero · `93` estructura de episodio · `42` tipografía del canal ·
`90` fuentes primarias · `96` verificación de datos
