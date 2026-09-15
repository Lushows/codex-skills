# 29 — Enriquecimiento de datos

Enriquecer (data enrichment = agregarle a cada contacto los datos que no tenías) es lo que convierte una lista de "correo + nombre" en una lista con **munición para personalizar**. Sin enriquecimiento, tu único ángulo es "Hola {nombre}" — que no es personalización (`52`) y rinde reply rates de miseria. Con enriquecimiento tienes la señal, el detalle, el dato que hace que el correo **solo tenga sentido para esa persona**. Este módulo: qué datos agregar, la técnica del **waterfall** para conseguirlos con máxima cobertura, y cómo cada dato se traduce en una línea de mensaje.

## El principio: la personalización relevante necesita un dato

Un cold email que responde tiene una primera línea que demuestra que investigaste la cuenta (`53`). Esa línea necesita un **hecho**: contrataron 5 vendedores, abrieron sede nueva, usan tal software, el CEO posteó sobre X, levantaron una ronda. El enriquecimiento es cómo consigues ese hecho **a escala** — para 1.000 contactos, no a mano uno por uno. La relación es directa: **más datos relevantes por fila → más ángulos de personalización → más respuestas positivas**, sin perder volumen (resuelve el trade-off de `66`).

## Qué datos vale la pena agregar

| Categoría | Ejemplos de dato | Para qué sirve en el mensaje |
|---|---|---|
| **Firmographics** (`15`) | tamaño, ingresos, sector, nº sedes, año fundación | Segmentar y calibrar el pitch (`18`) |
| **Technographics** (`134`) | qué software/stack usan (CRM, e-commerce, etc.) | "Vi que usan Shopify…" ángulo técnico |
| **Señales / triggers** (`14`, `37`, `135`) | contrataron, ronda de inversión, cambio de cargo, expansión | El correo con timing perfecto (`128`) |
| **Datos de la persona** | cargo exacto, antigüedad, posts recientes, intereses | Opener humano y relevante (`53`) |
| **Datos del negocio local** | nº reseñas, calificación, servicios, zona | PYMES LatAm: "vi que tienen 4,7★ con 800 reseñas…" |
| **Intent** (`36`, `131`) | está investigando tu categoría (Bombora, G2) | Priorizar a quien ya busca |
| **Contacto** | correo verificado, móvil, LinkedIn, WhatsApp (`23`, `24`) | Multicanal (`61`) |

No enriquezcas por enriquecer: agrega **solo los datos que vas a usar** en el mensaje o para priorizar (`16`). Un campo que no cambia ni el mensaje ni la decisión es ruido que cuesta créditos.

## El waterfall enrichment — la técnica clave

**Waterfall** = encadenar varios proveedores en cascada: si el primero no tiene el dato, prueba el segundo, luego el tercero, y así. Pagas solo por el que acierta. Sube la cobertura de ~60 % (un solo proveedor) a ~85–90 % (varios encadenados) — decisivo en LatAm, donde ningún proveedor solo cubre bien.

```
WATERFALL para el correo (ejemplo en Clay, `31`):
  paso 1: Apollo         → ¿tiene email? sí → usar / no → paso 2
  paso 2: Prospeo        → ¿tiene? sí → usar / no → paso 3
  paso 3: Hunter         → ¿tiene? sí → usar / no → paso 4
  paso 4: FindThatLead   → ¿tiene? sí → usar / no → marcar "sin dato"
  luego: NeverBounce verifica el ganador (`28`)
```
El mismo patrón sirve para móviles (Apollo → Lusha → Cognism) y para señales. La herramienta que orquesta esto sin código es **Clay** (`31`, `101`); waterfall a fondo en `130`.

## Herramientas de enriquecimiento

| Herramienta | Qué enriquece | Nota |
|---|---|---|
| **Clay** | Todo, vía waterfalls + 100+ integraciones + IA | El orquestador estándar 2026 (`31`, `101`) |
| **Clearbit (HubSpot Breeze)** | Datos de empresa y persona sobre tu CRM | Enriquecer registros existentes (`25`) |
| **Apollo** | Firmographics + contacto + algo de señales | Ya lo tienes si es tu base (`100`) |
| **ZoomInfo / Cognism** | Firmographics ricos + intent + org charts | Enterprise (`25`, `106`) |
| **Bombora / G2 / 6sense** | Intent data (quién investiga tu categoría) | `36`, `131` |
| **IA (GPT/Claude en Clay)** | Resumir la web de la empresa, sacar el ángulo, escribir la línea 1 | Personalización a escala (`120`) — cuida costos con `optimizer_tokens_lushows` |

## De dato a línea de mensaje (el pago del enriquecimiento)

El dato solo vale si se vuelve texto. Ejemplos de traducción:

```
Dato: "contrató 6 SDRs en 90 días" (señal, `14`)
→ "Vi que están armando el equipo comercial (6 SDRs este trimestre).
   Justo cuando el equipo crece rápido es cuando [problema que resuelves]..."

Dato: "usa Shopify + factura mucho" (technographic, `134`)
→ "Con Shopify a ese volumen, normalmente [dolor específico]..."

Dato PYME: "restaurante 4,8★, 3 sedes en Bogotá"
→ "Felicidades por las 3 sedes y el 4,8 en Chapinero —justo a ese tamaño
   el control de costos por sede se vuelve el cuello de botella..."
```
La estructura completa del opener y del correo → `53`, `50`. La personalización con IA a escala → `120`.

## Ejemplo real: enriquecer 500 cuentas para personalizar

```
Entrada: 500 empresas con web + decisor + email verificado.
En Clay:
  1. Enrichment de empresa (Clay/Apollo): tamaño, sector, nº empleados.
  2. Technographic (BuiltWith/Clay): ¿usan X software?
  3. Señal: ¿contrataron / abrieron sede / ronda? (Clay + LinkedIn).
  4. IA (Claude en Clay): lee la web → 1 frase de "qué hacen" + ángulo.
  5. Salida: columna angulo_personalizacion lista para el {{merge}} del email.
Resultado: 500 correos con línea 1 única, enviados a escala. Reply rate ↑.
```

## Errores comunes (qué NO hacer)

- **Enriquecer datos que no usarás** → quemas créditos sin subir respuestas.
- **Un solo proveedor** en vez de waterfall → cobertura pobre en LatAm.
- **Personalizar el nombre y creer que enriqueciste** (`52`).
- **No verificar tras enriquecer** → el email recién hallado también puede rebotar (`28`).
- **IA sin control de costo** al personalizar miles → factura sorpresa; optimiza con `optimizer_tokens_lushows`.

## Frontera y siguiente paso

Enriquecer = darle munición a la máquina; **usar esa munición para convencer y cerrar** en la conversación → `ventas_lushows`. Con la lista enriquecida cierras el Bloque 2: tienes cuentas (`21`), decisores (`22`), correos (`23`), multicanal (`24`), verificada (`28`) y con ángulos (`29`). Ahora configura el envío seguro (`40`–`44`) y escribe el copy que usa esos ángulos (`50`–`56`). Waterfall a fondo: `130`. Orquestar todo en Clay: `31`.
