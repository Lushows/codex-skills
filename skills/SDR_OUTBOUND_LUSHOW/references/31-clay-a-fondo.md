# 31 — Clay a fondo

Clay (clay.com) es la herramienta que redefinió el outbound moderno. La forma más simple de entenderlo: es **una hoja de cálculo con superpoderes** donde cada fila es un prospecto y cada columna puede *buscar datos en internet, cruzar 50+ proveedores, o pedirle a una IA que investigue y escriba*. Antes, enriquecer una lista y personalizar 500 correos era trabajo manual de días; con Clay lo montas una vez como una "receta" y corre solo para miles de filas. Este es el corazón del stack de datos+enrichment (categoría 2 del `30`). Su versión avanzada vive en `101`.

## El principio: waterfall + IA en columnas

Dos ideas hacen a Clay distinto de un Apollo o un Excel normal:

1. **Waterfall enrichment (enriquecimiento en cascada).** Para conseguir, por ejemplo, el correo de un contacto, Clay pregunta al proveedor 1; si no lo encuentra, al 2; luego al 3… hasta agotar decenas de fuentes. Tú solo pagas por el dato que **sí** se encontró. Resultado: cobertura mucho más alta que cualquier proveedor solo (un proveedor cubre ~40–70%; el waterfall llega a 80–90%). Detalle en `130`.
2. **Columnas con IA (Claygent).** Una columna puede ser un mini-agente de IA que "visita" la web de la empresa, lee su LinkedIn o busca en Google y devuelve una respuesta estructurada: *"¿esta empresa tiene tienda física? ¿qué venden? ¿cuál fue su última noticia?"*. Eso es lo que alimenta la personalización a escala (ver `35`, `52`, `120`).

Juntas: Clay convierte "una lista de nombres" en "una lista enriquecida con el dato exacto que hace relevante cada mensaje".

## Los bloques de Clay (cómo se construye una tabla)

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Tabla (table)** | Tu lista; una fila por cuenta o contacto | 500 restaurantes de Bogotá |
| **Fuente (source)** | De dónde entran las filas | Import CSV, Apollo, Sales Nav, Google Maps, HubSpot, webhook |
| **Columna de enrichment** | Trae un dato de un proveedor | "Buscar email de trabajo", "empleados", "tecnología web" |
| **Columna de IA (Claygent)** | Un prompt que investiga y responde | "Resume qué hace esta empresa en 1 frase" |
| **Fórmula / lookup** | Lógica tipo Excel entre columnas | `if empleados > 50 then "Tier A"` |
| **Condition (run if)** | Solo corre la columna si se cumple algo | "buscar teléfono solo si no hay email" → ahorra créditos |
| **Write-back / integración** | Manda el resultado afuera | a Instantly, HubSpot, Smartlead vía nativo o webhook (ver `34`) |

Clay cobra por **créditos** (cada enrichment consume créditos). Por eso las **condiciones** importan: no gastes un crédito buscando teléfono en filas que ya tienen email.

## El cómo, paso a paso: tu primera tabla útil

Objetivo: lista de 300 cuentas por nicho, enriquecida y lista para secuencia.

1. **Trae las cuentas.** Source → importa desde Apollo/Sales Nav/Google Maps o sube un CSV. Ej.: "clínicas dentales, 5–50 empleados, México".
2. **Encuentra al decisor.** Columna "Find people" con filtro de cargo (director, gerente, dueño). Ver `22`.
3. **Consigue el correo (waterfall).** Columna "Find work email" → activa varios proveedores en cascada. Ver `23`, `130`.
4. **Verifícalo.** Columna de verificación (NeverBounce/ZeroBounce integrados) → marca válido/catch-all/inválido. Nunca envíes a inválidos (ver `28`).
5. **Enriquece para personalizar.** Columna Claygent: *"Visita el sitio de {dominio} y dime en 8 palabras su especialidad o algo reciente."* Esto es tu munición de relevancia.
6. **Califica / puntúa.** Fórmula que asigna Tier A/B/C por encaje (ver `16`, `38`).
7. **Escribe la línea 1 con IA.** Columna IA que redacta el opener usando el dato del paso 5 (ver `53`, `120`).
8. **Exporta.** Write-back a tu sequencer (Instantly/Smartlead) solo de las filas con email válido + Tier A/B. Ver `33`, `34`.

## Ejemplo real: prompt de Claygent para personalización

Columna de IA sobre una tabla de restaurantes:

```
Rol: investigador de ventas.
Entrada: {company_name}, {website}, {city}.
Tarea: visita el sitio web y dime en UNA frase de máximo 12 palabras
algo específico y verificable del negocio (su especialidad, un plato
estrella, una promo visible o una sede nueva). Español neutro.
Si no encuentras nada concreto, responde exactamente: "SIN_DATO".
Formato de salida: solo la frase, sin comillas.
```

Luego una columna-fórmula arma el opener:
```
"Vi que en {company_name} {claygent_frase} —"
→ "Vi que en Parrilla El Fogón su especialidad es cordero al horno —"
```
Las filas que devuelven `SIN_DATO` las mandas por un camino de plantilla genérica o las descartas: nunca envíes un correo con `SIN_DATO` visible.

## Casos de uso donde Clay brilla

- **Listas por señal:** cruzar una fuente de empresas que están contratando (job posts) con enrichment de decisor → outbound por señal (ver `37`, `128`).
- **Deduplicar y limpiar** una base vieja antes de re-atacarla.
- **Enriquecer inbound:** cuando alguien llena un formulario, un webhook lo mete a Clay, lo enriquece y lo puntúa antes de que llegue al CRM (ver `38`, `147`).
- **Scoring automático** combinando firmographics + intent (ver `137`).

## Errores comunes

- **Quemar créditos sin condiciones.** Corres 40 columnas sobre 5.000 filas y agotas el plan. Usa "run if" y filtra antes de enriquecer.
- **Confiar en la IA sin verificar el email.** Clay puede escribir un opener bellísimo hacia un correo que rebota. Verifica **siempre** (paso 4) antes de exportar.
- **Sobre-automatizar de entrada.** Clay tiene curva. Empieza con una tabla de 3 columnas (import → email → verify) y crece. No montes un waterfall de 12 proveedores el día 1.
- **Personalización falsa.** Un Claygent que inventa datos ("hallucina") arruina la credibilidad. El prompt debe forzar `SIN_DATO` cuando no hay evidencia (como arriba).

## Siguiente paso

Monta la tabla de 8 pasos de arriba con 50 filas de prueba y revisa a mano las columnas de email y de IA antes de escalar a 300. Para el waterfall a fondo → `130`; para Clay avanzado (integraciones, agentes, write-backs complejos) → `101`. Conecta la salida a tu sequencer (`33`) vía integración (`34`). Para bajar el costo de la IA que usas en los Claygents a escala → `optimizer_tokens_lushows`.
