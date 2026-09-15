# 110 — Arquitectura multi-dominio

Este es el módulo raíz del Bloque 11 (deliverability avanzada). Cuando pasas de "mando 100 correos al día" a "necesito 1.000+ al día sostenidos", ya no basta con comprar un par de dominios secundarios (ver `41`): necesitas **arquitectura** — un diseño deliberado de cuántos dominios, cuántos buzones por dominio, cómo aíslas el riesgo y cómo lo escalas sin que un dominio podrido se lleve a los demás. La regla física del correo frío no cambió (ver `44`): **el volumen se construye con muchos buzones pequeños, no con pocos grandes.** Lo que cambia a escala es que ahora administras una *flota*, y la flota necesita estructura, nomenclatura y aislamiento. Este módulo te da los números y el plano.

## El principio: aislar el riesgo, no concentrarlo

En correo frío todo dominio es desechable y todo dominio puede caer. La pregunta de arquitectura no es "cómo evito que caiga uno" (caerán), sino **"cuando uno caiga, ¿cuánto de mi operación se lleva?"**. La respuesta es: reparte. Muchos dominios chicos, pocos buzones cada uno, cada dominio como un compartimento estanco. Si un dominio entra en blacklist (ver `114`) o se quema (ver `117`), lo jubilas y pierdes el 5–10% de tu capacidad, no el 100%.

Los tres números de la arquitectura:

| Número | Rango sano 2026 | Por qué |
|---|---|---|
| **Buzones por dominio** | 2–3 (máx. 3) | Más de 3–4 buzones enviando en un dominio concentra riesgo: si Google marca el dominio, caen todos juntos |
| **Correos por buzón/día** | 20–40 (ver `44`) | Imita humano; por encima de ~50 el patrón grita spam |
| **Capacidad por dominio/día** | ~60–120 | = buzones × límite. Un dominio "vale" ~100 correos/día sanos |

## La matemática: cuántos dominios y buzones para tu volumen

Todo se deriva de tu meta de reuniones hacia atrás (la ecuación completa está en `05`; para números exactos usa `Matematicas_lushows`). La fórmula:

```
Dominios necesarios = correos/día objetivo ÷ (buzones por dominio × correos por buzón/día)
Buzones totales      = correos/día objetivo ÷ correos por buzón/día
```

Tabla de referencia (a 3 buzones/dominio, 35 correos/buzón/día):

| Meta correos/día | Buzones | Dominios | Capacidad prospectos/mes (~22 días) |
|---|---|---|---|
| 300 | 9 | 3 | ~6.600 |
| 600 | 18 | 6 | ~13.200 |
| 1.000 | ~30 | 10 | ~22.000 |
| 2.000 | ~58 | 20 | ~44.000 |
| 5.000 | ~145 | 48 | ~110.000 |

**A gran volumen conviene bajar el límite por buzón** (a 25–30) y sumar más buzones: más margen de seguridad, menos exposición por buzón. Prefiere 60 buzones a 30 que 40 buzones a 45.

## El plano: cómo se estructura la flota

```
CUENTA MADRE (Google Workspace u Outlook 365) — factura y administración
│
├── DOMINIO 1  (variante de tu marca; ver 41)
│    ├── luis@dominio1.com
│    ├── l.castillo@dominio1.com
│    └── ventas@dominio1.com
├── DOMINIO 2
│    ├── ... (2-3 buzones)
└── DOMINIO N ...
```

Decisiones de arquitectura a esta escala:

- **Proveedor de buzones:** Google Workspace da la mejor reputación (~$6–7/buzón/mes) pero limita cuentas por dominio y verifica pagos. Microsoft 365 es más barato en volumen. Los revendedores de infraestructura (**Maildoso, Mailreef, Hypertide, Premium Inbox, Superwave, Zapmail**) venciendo 2025–2026 te montan decenas de buzones ya autenticados en minutos (~$1.5–4/buzón/mes) — clave para escalar sin hacer DNS a mano dominio por dominio.
- **Mezcla de proveedores:** a gran volumen, no pongas toda la flota en un solo proveedor. Reparte entre Google + Microsoft + revendedor. Aísla el riesgo de que un proveedor te suspenda en bloque.
- **Nomenclatura de dominios:** variantes limpias de tu marca real (`getgastrolatam.com`, `gastrolatam.co`, `trygastrolatam.com`), nunca palabras raras ni con guiones o números. El prospecto debe reconocer la marca. (Detalle en `41`.)
- **Redirección:** cada dominio de envío redirige (301) a tu web principal, para que si alguien lo teclea, exista un sitio real. Suma legitimidad.

## Escalar la flota sin quemarte

1. **Nunca enciendas toda la flota de golpe.** Compra e integra dominios en oleadas; cada buzón nuevo pasa por warmup 2–4 semanas (ver `43`, y warmup avanzado `112`) antes de un solo correo real.
2. **Ten siempre un colchón calentándose.** Mantén ~15–20% de buzones en warmup de reserva. Cuando uno se degrade (ver `113`), lo jubilas y ya tienes reemplazo caliente.
3. **Segmenta la flota por función:** dedica dominios/buzones a tu campaña de mayor volumen y otros a cuentas tier-1 de alto valor (ABM; ver `94`). Así una campaña masiva que se degrade no toca los buzones con los que le escribes a tus mejores cuentas.
4. **Documenta la flota** en una hoja: dominio, buzones, fecha de compra, fecha fin de warmup, proveedor, estado de reputación. A 30 dominios, sin registro, vuelas ciego.

## Errores comunes (qué NO hacer)

- Meter 8–10 buzones en un dominio para "ahorrar dominios". Concentras todo el riesgo; un mal día se lleva la operación.
- Toda la flota en un solo proveedor y una sola cuenta madre: si te suspenden la cuenta, mueres entero.
- Escalar dominios sin escalar warmup ni monitoreo (ver `112`, `113`). Volumen sin vigilancia = caída masiva silenciosa.
- Dominios con nombres basura (guiones, números, palabras spam): nacen con sospecha.
- No jubilar buzones degradados: un buzón podrido contamina la reputación de su dominio y arrastra a sus vecinos.

## Siguiente paso

Con la flota diseñada, blíndala: `111` (DMARC estricto, BIMI y reputación de dominio), luego `112` (warmup avanzado y rampa de volumen para toda la flota). Para vigilar la reputación real de cada dominio ver `113` (Google Postmaster). Para la matemática exacta de buzones a tu volumen objetivo, `Matematicas_lushows`. Los fundamentos (por qué dominios secundarios, autenticación básica) están en el Bloque 4: `40`–`49`.
