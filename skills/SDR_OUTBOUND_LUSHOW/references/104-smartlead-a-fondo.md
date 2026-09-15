# 104 — Smartlead a fondo

Smartlead (smartlead.ai) es el sequencer de cold email preferido por **agencias y operaciones que manejan volumen alto o varios clientes**. Comparte ADN con Instantly (familia 1: cold email a volumen, ver `33`, `103`) pero brilla en tres cosas que Instantly hace más simple: **rotación de buzones a gran escala, un master inbox de nivel operación, y una API abierta que lo vuelve el motor de envío de un sistema automatizado**. Si Instantly es "el más fácil para arrancar", Smartlead es "el que aguanta cuando escalas o le facturas envío a terceros".

## El principio: rotación y aislamiento a escala

Cuando manejas 30, 60 o 200 buzones —o campañas de **varios clientes** que no deben mezclarse— necesitas dos cosas que Smartlead hace mejor:

1. **Rotación inteligente de buzones.** Reparte cada campaña entre muchos buzones (email account rotation) para que ninguno pase su límite diario (~20–40, ver `44`) y la carga se distribuya parejo. A más buzones, más volumen agregado con el mismo riesgo por buzón.
2. **Aislamiento por cliente (multi-cliente).** Cada cliente/proyecto con sus dominios, buzones y reportes separados, sin que el volumen de uno afecte la reputación de otro. Es *la* razón por la que las agencias lo eligen.

## Master inbox (el centro de operaciones)

El **master inbox** de Smartlead unifica las respuestas de **todos** los buzones y clientes en una sola bandeja con categorización:

- Filtra por campaña, cliente, buzón o **categoría de respuesta** (interesado / no ahora / fuera de oficina / no / referido).
- Un equipo puede trabajar respuestas en paralelo sin pisarse.
- Cada respuesta clasificada alimenta la disposición y el CRM (ver `77`, `32`).
- Igual que en Instantly, **la conversación tras la respuesta** —persuadir, manejar objeción, agendar, cerrar— **no vive aquí**: es `ventas_lushows` (ver `64`). El master inbox te organiza el "quién respondió y con qué intención"; el vendedor hace el resto.

## Sub-secuencias y ramificación (más flexible que Instantly)

Smartlead permite **flujos condicionales** dentro de la campaña, no solo una lista lineal de correos:

- **Sub-secuencias por comportamiento/categoría.** Ej.: si el prospecto responde "fuera de oficina", pausa 7 días y reengancha; si abre pero no responde (cuando midas eso), ramifica a otro ángulo.
- **Múltiples variantes por paso** para A/B testing nativo de asunto y cuerpo (ver `65`).
- **Reglas de reengagement** para leads que no respondieron una primera campaña → nueva secuencia con otro ángulo (ver `76`).

Esto le da más músculo de "orquestación" que Instantly, a cambio de una curva un poco mayor.

## La API (lo que lo vuelve un motor, no solo una app)

La **API de Smartlead** es su ventaja para quien automatiza (ver `34`, `107`). Con ella puedes, desde n8n/Make/código:

- **Crear campañas y cargar leads** por programa (ej.: Clay termina de enriquecer → dispara un webhook → Smartlead crea/alimenta la campaña, ver `101`).
- **Leer respuestas y categorías** para escribirlas de vuelta al CRM.
- **Gestionar buzones y warmup** a escala.
- **Sacar métricas** a tu propio dashboard/BI.

Patrón pro: **Clay (datos) → API de Smartlead (envío) → CRM (verdad)**, todo pegado con n8n (ver `107`). Ese es el "producto" que las agencias de outbound-as-a-service venden (ver `95`).

## Ejemplo real: operación multi-cliente

```
Agencia con 3 clientes:
  Cliente A (SaaS):    12 buzones / 4 dominios  → campaña "SaaS-Q1"
  Cliente B (clínicas): 8 buzones / 3 dominios  → campaña "Salud-Q1"
  Cliente C (retail):  10 buzones / 4 dominios  → campaña "Retail-Q1"
Cada cliente:
  - Workspace/cliente aislado (reputación separada)
  - Warmup ON en todos los buzones (ver 43)
  - Daily limit 25/buzón, rotación automática (ver 44)
  - Stop on reply ON · Open tracking OFF (ver 80)
  - Reportes por cliente para enviar el status semanal
Automatización (API):
  Clay enriquece y verifica (ver 28, 101)
    → webhook a n8n (ver 107)
      → API Smartlead: crea/alimenta la campaña del cliente correcto
Respuestas → master inbox → categoriza → CRM del cliente (ver 32)
```

## Smartlead vs. Instantly (cuál eliges)

| Criterio | Instantly (`103`) | Smartlead (`104`) |
|---|---|---|
| Facilidad de arranque | Más simple | Curva un poco mayor |
| Buzones a gran escala | Bien | **Mejor** (rotación, muchos) |
| Multi-cliente / agencia | Limitado | **Su fuerte** |
| API / automatización | Básica | **Potente y abierta** |
| Sub-secuencias / ramificación | Lineal | **Condicional** |
| Master inbox | Unibox | **Master inbox por cliente** |
| Warmup incluido | Sí | Sí |
| Precio 2026 (aprox) | ~$37–97/mes | ~$39–94/mes+ (escala por leads/buzones) |

**Regla:** solista validando → Instantly. Agencia, volumen alto, varios clientes o quieres automatizar por API → Smartlead. Ambos exigen la **misma fontanería de deliverability** del Bloque 4 (`41`–`45`); la herramienta envía, tú montas dominios y DNS.

## Errores comunes

- **Elegir Smartlead siendo solista** que solo quiere validar → pagas complejidad que no usas; empieza en Instantly.
- **Mezclar clientes en un mismo dominio/workspace** → la reputación de uno contamina a otro; aísla siempre.
- **Sin warmup o sin DNS** → spam garantizado, la API no te salva (ver `42`, `43`).
- **Automatizar por API sin verificar leads** → cargas rebotes a escala y quemas buzones de todos los clientes (ver `28`, `45`).
- **Tracking de apertura ON** → penaliza deliverability en 2026 (ver `80`).

## Siguiente paso

Si vas a manejar volumen o clientes, monta un workspace por cliente con dominios y buzones aislados, warmup ON, y prueba la **API** conectando Clay → n8n → Smartlead (ver `101`, `107`). Compara la decisión de herramienta en `33`; la infraestructura obligatoria en `41`–`45`; el modelo de outbound-as-a-service en `95`.
