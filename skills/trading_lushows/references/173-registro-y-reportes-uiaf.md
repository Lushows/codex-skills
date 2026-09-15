# 173 — Registro y reportes: la UIAF y quién reporta qué

> ⚠️ Las obligaciones de reporte cambian con resoluciones nuevas. Este módulo da el panorama;
> **verificar al día con contador_lushows o fuente oficial (UIAF, DIAN)** antes de asumir nada.

## Qué es la UIAF (en simple)

La **UIAF** (Unidad de Información y Análisis Financiero) es la entidad colombiana que recibe
reportes de operaciones para detectar lavado de activos y financiación del terrorismo. No te
cobra impuestos ni te vigila a ti directamente: recibe información de las **empresas obligadas**
(bancos, y en el ecosistema cripto, los proveedores de servicios de activos virtuales).

**Definición — proveedor de servicios de activos virtuales (VASP):** término técnico para
exchanges y plataformas que custodian o cambian cripto por dinero.

## Quién reporta: el exchange vs el usuario

| Obligación | ¿A quién le toca? |
|---|---|
| Registrarse ante la UIAF y reportar operaciones | Al **exchange/plataforma** (si opera con Colombia) |
| Reportar operaciones sospechosas o de cierto monto | Al **exchange** (por eso el KYC del módulo 171) |
| Declarar impuestos y patrimonio | Al **usuario** (Luis) — módulo 172 |
| Reportar activos en el exterior (si aplica) | Al **usuario**, vía declaración — confirmar con contador |

La idea clave: **como usuario persona natural, tu obligación central es tributaria, no de
reporte a la UIAF.** El reporte antilavado lo hace la plataforma. Pero lo que el exchange
reporta sobre ti debe cuadrar con lo que tú declaras — por eso la coherencia importa.

## Lo que sí te toca a ti (higiene del usuario)

1. **Origen de fondos demostrable**: poder explicar de dónde salió cada peso que entró al
   exchange (nómina, ventas de tu negocio, ahorros declarados).
2. **Trazabilidad**: banco propio → exchange propio → banco propio. Sin atajos por terceros.
3. **Coherencia fiscal**: lo que mueves ≈ lo que declaras. Las alertas nacen de la incoherencia.
4. **Cripto en plataformas del exterior**: puede contar como activo en el exterior para efectos
   de declaración — punto fino, **confirmar con contador_lushows**.

## Anti-humo

- "La UIAF me va a perseguir por hacer trading" — no: hacer trading legal y declarado no es
  operación sospechosa. La sospecha nace de patrones de lavado, no de operar.
- "Mejor uso plataformas sin registro para que nadie reporte" — al revés: esas plataformas son
  las que desaparecen con tu plata o te dejan sin cómo demostrar nada (módulo 174).

## Cómo aplica al AGENTE TRADING

- En paper: nada que reportar, nadie que reporte. Cero exposición.
- En live: elegir exchange que cumpla con el registro colombiano (módulo 174) — que ÉL reporte
  bien es protección para Luis, no amenaza. El diario del bot + extractos bancarios = origen de
  fondos y trazabilidad resueltos por diseño.
