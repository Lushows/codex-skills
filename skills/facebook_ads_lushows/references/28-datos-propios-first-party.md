# 28 — Datos propios (first-party data)

**First-party data** = los datos que TUS clientes te dieron directamente: emails, teléfonos, historial de compras. Es el activo publicitario que iOS, las cookies muriendo y los cambios de privacidad NO te pueden quitar — porque vive en tu CRM, no en el navegador de nadie. En la era post-cookie + Andromeda (donde la calidad de señal pesa más que nunca, EMQ piso ~8), tu first-party data dejó de ser "un plus" y pasó a ser la base de la medición y el targeting. Lee este módulo cuando tengas ventas acumuladas y no las estés usando en la pauta, o desde el día 1 para montar el hábito de capturar datos.

## Customer Match / customer list: formato correcto

Una **customer list** (Customer Match) es un archivo (CSV) que subes a Meta (Audiences → Create → Custom audience → Customer list) para que cruce tus clientes con sus usuarios. Cuantas más columnas (identificadores), mejor cruza:

| Columna | Formato | Ejemplo |
|---|---|---|
| email | minúsculas, sin espacios | maria@gmail.com |
| phone | **con código de país**, solo dígitos o con + | +573001234567 |
| fn / ln | nombre / apellido, minúsculas | maria / gomez |
| ct / st / zip | ciudad / depto / código postal | bogota / cundinamarca |
| country | código de 2 letras | co |
| value | valor del cliente (para value-based LAL, ver 22) | 350000 |

El teléfono SIN +57 es el error #1 en Colombia: Meta no sabe que "3001234567" es colombiano y el match falla. En LatAm el **teléfono es el identificador de oro** (más gente tiene WhatsApp verificado que email activo) — priorízalo. Meta publica una plantilla CSV en el flujo de subida — úsala.

**Hashing** (protección del dato): hashear = convertir el dato en una huella irreversible (SHA-256) antes de que viaje. Si subes el CSV por la interfaz, **Meta hashea en tu navegador automáticamente** — no necesitas hacer nada. Si envías por **API** (CAPI o Marketing API, integraciones automáticas ver 96), TÚ debes hashear con SHA-256 (normalizado: minúsculas, sin espacios, teléfono con código de país) antes de enviar. Nunca mandes datos en claro por API.

## Tamaño mínimo y match rate

- **Tamaño útil**: desde unos pocos cientos sirve para exclusiones; para semilla de lookalike o retargeting de lista, ideal **1.000+**. Con 50 contactos no montes nada todavía — sigue capturando.
- **Match rate** (% de tu lista que Meta encuentra): en LatAm espera **40-70%**. ¿Por qué no 100%? Teléfonos sin código de país, emails de la factura que nadie usa en Facebook, datos viejos, números corporativos. Si tu match da < 30%, el problema es formato (revisa el +57) o calidad de captura.

## First-party como columna vertebral de la medición (no solo audiencias)

En 2026 tu first-party data hace DOBLE trabajo: alimenta audiencias Y mejora la medición. Cuando tu CAPI manda los identificadores hasheados del cliente (teléfono, email) junto al evento `Purchase`, sube tu **EMQ** (Event Match Quality) — y el piso práctico subió a **8+** (antes 6). Píxel-solo (EMQ 3-5) ya no compite en la era Andromeda. Es decir: capturar bien el teléfono no solo te da una customer list, te da una señal de conversión que el algoritmo entiende mejor → mejor entrega de TODA la cuenta, no solo del retargeting. En LatAm, mandar el teléfono con +57 hasheado es el upgrade de EMQ más fácil que existe.

## Los 4 usos (con módulo de profundidad)

1. **Exclusiones** (ver 24): compradores fuera del prospecting/retargeting. El uso más rentable por peso invertido — y funciona aun con listas chicas.
2. **Semilla de lookalike value-based** (ver 22): tu lista con columna `value` le dice a Meta "búscame parecidos a mis MEJORES clientes". La mejor semilla que existe.
3. **Retargeting de lista / reactivación**: campaña a clientes que no compran hace 60-180 días ("te extrañamos" + novedad u oferta de regreso). Barata porque ya confían en ti. Para consumibles, sincronízala con el ciclo de recompra.
4. **Existing customers en Advantage+ Sales** (ver 12/24): defines la lista en la configuración y pones el **cap de clientes existentes (25-30%)** para forzar adquisición de gente nueva. Sin lista definida, la campaña no distingue cliente nuevo de viejo y tu ROAS de prospecting es mentira.

## Mantener la lista VIVA

Una lista subida es una foto que envejece: los clientes de hoy no están, los compradores nuevos siguen viendo tu prospecting (exclusión rota). Dos caminos:

- **Manual** (suficiente para empezar): exporta clientes del CRM/Shopify/Excel **una vez al mes**, re-sube reemplazando la lista (Meta permite actualizar la audiencia existente, no crees una nueva cada vez).
- **Automático** (mejor): integración directa tienda→Meta (Shopify/WooCommerce sincronizan compradores solos) o CAPI con datos de cliente, ver 96 y 14. Configúralo cuando el volumen justifique.

## Capturar datos desde el día 1 (LatAm WhatsApp-first)

Si vendes por WhatsApp, tus datos están enterrados en chats — conviértelos en activo:
- Cada venta pide **email "para enviarte la factura/confirmación"**: nadie se niega, y ese email vale pauta futura (exclusiones, LAL, reactivación).
- El teléfono ya lo tienes (es WhatsApp): regístralo CON +57 en tu Excel/CRM, junto a qué compró, cuándo y por cuánto (la columna `value` de mañana).
- Mínimo viable: un Google Sheet con fecha, nombre, teléfono, email, producto, valor. Eso, en 6 meses, es una value-based LAL y una máquina de reactivación.
- Si corres CTWA, captura el **`ctwa_clid`** (click id que llega cuando alguien inicia el chat desde un ad) y dispáralo en tu evento CAPI de `business_messaging` — así Meta atribuye la venta al ad correcto (ver 53). Es first-party data específico de WhatsApp.
- Todo esto requiere autorización de datos del cliente — el aviso y el Habeas Data en el módulo 29. Con la **Data Source Declaration** rodando (Meta exige declarar origen y consentimiento de las audiencias), capturar el consentimiento desde la venta #1 dejó de ser opcional.

## Calendario mínimo del activo de datos

- **Hoy**: Sheet/CRM con +57 en todos los teléfonos y aviso de privacidad que cubra publicidad (ver 29).
- **Cada venta**: registrar email, producto, valor.
- **Mensual**: re-subir/actualizar la customer list en Meta; verificar exclusiones activas y cap de clientes existentes (ver 24).
- **Al llegar a ~500-1.000 compradores**: crear el value-based LAL y testearlo (ver 22).
- **Cuando el volumen lo justifique**: integración automática tienda/CRM → Meta + CAPI con datos de cliente para subir EMQ (ver 96/14).

## Errores comunes — blacklist

- Teléfonos sin +57: match rate por el piso y crees que "las customer lists no sirven".
- Subir la lista una vez en 2025 y nunca actualizarla: exclusiones rotas, LAL aprendiendo de clientes fantasma.
- **Comprar bases de datos**: ilegal (ver 29), match horrible (datos viejos/falsos), y Meta detecta el patrón y te puede tumbar la cuenta (ver 93). Triple pérdida.
- Crear una audiencia NUEVA en cada subida mensual: terminas con 14 listas duplicadas y los ad sets apuntando a la vieja. Actualiza la existente.
- Mandar datos en claro por API "porque hashear es complicado": violación de la política de Meta; la interfaz hashea sola, la API exige SHA-256.
- Guardar las ventas solo en el chat de WhatsApp: a los 6 meses tienes 2.000 ventas y CERO activo de datos. Sheet desde la venta #1.
- Lista sin columna `value`: regalas la posibilidad del value-based LAL, la mejor semilla disponible (ver 22).
- No mandar el teléfono hasheado en el CAPI: dejas tu EMQ en 3-5 y toda la cuenta entrega peor; el teléfono +57 es el upgrade más barato.
- Subir lista sin consentimiento de publicidad: con la Data Source Declaration queda inelegible (ver 29).
