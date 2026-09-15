# 99 — Maestría del vendedor y cómo generar el entregable

Llegaste al final de la skill. Aquí cerramos dos cosas: el **camino del vendedor de élite** —una síntesis honesta de lo que de verdad separa a los grandes— y el **entregable**, cómo convertir todo este conocimiento en un documento profesional (playbook, guiones, propuesta) en PDF, listo para que Lushows lo use y lo comparta.

## La maestría: la verdad honesta

No hay atajos mágicos. El vendedor de élite no nace con un don; se construye con principios aplicados durante mucho tiempo. Lo que de verdad lo separa:

1. **Le importa el cliente de verdad.** La técnica sin intención genuina se siente a manipulación y se nota. El gran vendedor vende porque cree que su producto mejora la vida del otro. Esa convicción es lo que ninguna técnica reemplaza (ver 03).

2. **Domina los fundamentos, no los trucos.** Escuchar más que hablar (ver 40), preguntar bien (ver 41), vender el beneficio y no la característica (ver 51), recibir la objeción con calma (ver 60). Los básicos, ejecutados con maestría, vencen a cualquier truco viral.

3. **Es disciplinado cuando nadie mira.** Prospecta el día que no tiene ganas (ver 96). Hace el seguimiento número cinco que casi todos abandonan (ver 94). Actualiza su pipeline. La disciplina aburrida es la ventaja secreta.

4. **Trata el "no" como parte del oficio, no como herida.** La resiliencia (ver 02) es lo que le permite seguir cuando el promedio se rinde. El rechazo no lo define; es peaje del camino.

5. **Mide, aprende y ajusta.** Conoce sus números (ver 95), revisa qué falló y mejora su sistema (ver 98). No vende por suerte: vende por proceso, y mejora el proceso.

6. **Piensa en la relación, no en la transacción.** La venta de hoy importa menos que el cliente de por vida: postventa (ver 90), retención (ver 91), recompra (ver 92) y referidos (ver 93). El amateur caza; el maestro cultiva.

> La síntesis honesta: vender bien es 20% técnica y 80% carácter aplicado con constancia. La técnica la aprendes en semanas; el carácter lo construyes vendiendo, fallando y volviendo. Esta skill te da el mapa —el camino lo recorres tú.

## El entregable: tu playbook en PDF profesional

La preferencia es entregar un **PDF presentable directo**, no un archivo `.md` suelto para que el usuario lo procese. El flujo: escribir un HTML bien diseñado y convertirlo a PDF con Chrome en modo headless. Es la forma más fiable y portable de producir un documento limpio sin depender de librerías frágiles.

### Paso 1 — Generar el HTML del entregable

Construye un solo archivo HTML autocontenido (CSS embebido, sin dependencias externas) con el contenido del playbook (ver 98), los guiones o la propuesta. Diseño sobrio y profesional: márgenes generosos, tipografía legible, jerarquía clara con títulos. Incluye reglas de impresión para que pagine bien:

```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<style>
  @page { size: A4; margin: 18mm; }
  body { font-family: -apple-system, "Segoe UI", Arial, sans-serif;
         color: #1a1a1a; line-height: 1.5; font-size: 12pt; }
  h1 { font-size: 22pt; border-bottom: 3px solid #2e7d32; padding-bottom: 6px; }
  h2 { font-size: 15pt; color: #2e7d32; margin-top: 22px;
       page-break-after: avoid; }
  table { width: 100%; border-collapse: collapse; margin: 12px 0; }
  th, td { border: 1px solid #ccc; padding: 7px 9px; text-align: left; }
  th { background: #eef5ee; }
  .guion { background: #f6f6f6; border-left: 4px solid #2e7d32;
           padding: 10px 14px; margin: 10px 0; }
  /* evita cortar secciones a la mitad */
  section, table, .guion { page-break-inside: avoid; }
</style>
</head>
<body>
  <h1>Playbook de Ventas — BIO-SETA</h1>
  <section>
    <h2>1. Cliente ideal</h2>
    <p>...</p>
  </section>
  <!-- demás secciones del playbook (ver 98) -->
</body>
</html>
```

### Paso 2 — Convertir a PDF con Chrome headless

Desde la terminal, usa Chrome (o Edge, que comparte motor) en modo headless. En Windows:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless --disable-gpu --no-pdf-header-footer `
  --print-to-pdf="playbook-bioseta.pdf" `
  "file:///C:/ruta/al/playbook.html"
```

Si no hay Chrome, sirve Microsoft Edge con la misma sintaxis (`msedge.exe`). El flag `--no-pdf-header-footer` quita el encabezado/URL automático para un acabado limpio. El resultado es `playbook-bioseta.pdf`, listo para imprimir o compartir.

### Qué entregables puedes generar igual

| Entregable | Contenido | Módulos fuente |
|---|---|---|
| **Playbook de ventas** | El sistema completo | ver 98 |
| **Guiones de venta** | Apertura, descubrimiento, cierre, objeciones | ver 30, 40, 60, 65 |
| **Propuesta comercial** | Oferta a medida para un cliente | ver 50, 51 |
| **Secuencia de postventa** | Mensajes de los 4 momentos | ver 90 |
| **Catálogo de objeciones** | Cada objeción + respuesta | ver 61 |

## Error común

Entregar un `.md` crudo o un muro de texto sin diseño esperando que el usuario lo "convierta él". El valor del entregable está en que llegue terminado y presentable. Otro error: HTML con dependencias externas (fuentes o CSS de internet) que fallan al imprimir sin conexión —mantén todo embebido y autocontenido.

## Checklist del entregable

- [ ] ¿El contenido sale de los módulos reales (no relleno genérico)?
- [ ] ¿El HTML es autocontenido (CSS embebido, sin dependencias)?
- [ ] ¿Incluí reglas `@page` y `page-break` para que pagine bien?
- [ ] ¿Generé el PDF con Chrome/Edge headless (`--print-to-pdf`)?
- [ ] ¿Quité el encabezado automático (`--no-pdf-header-footer`)?
- [ ] ¿El PDF se ve profesional y está listo para compartir?

## Siguiente paso

Esto cierra la skill. El mapa está completo: mentalidad, prospección, descubrimiento, presentación, objeciones, cierre, postventa, sistema y maestría. Ahora el único paso que importa es el de afuera: elige UN cliente o UN deal hoy, aplica un solo módulo, y empieza. La maestría se construye vendiendo, no leyendo. A vender.
