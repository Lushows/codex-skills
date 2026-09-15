# 170 — Regulación cripto en Colombia (panorama)

## Lo básico, sin humo

- **Poseer y operar cripto es legal en Colombia.** Comprar, vender y tener bitcoin o ether
  no es delito ni está prohibido para personas naturales.
- **Cripto NO es moneda de curso legal.** Nadie está obligado a aceptarla como pago, y el
  peso colombiano sigue siendo la única moneda oficial. Para el Estado, la cripto se parece
  más a un *activo* (algo que tienes y que vale plata) que a *dinero*.
- **No hay una "licencia cripto" plena todavía.** Colombia ha discutido proyectos de ley para
  regular a los exchanges (las plataformas donde se compra/vende), pero el marco sigue en
  evolución. Lo que hoy es cierto puede cambiar en meses.

## Quién dice qué (los actores)

| Actor | Qué le importa |
|---|---|
| **Banco de la República** | La cripto no es moneda legal; los bancos no pueden operarla directamente como divisa |
| **Superintendencia Financiera** | Vigila el sistema financiero; ha corrido pilotos con exchanges y bancos |
| **DIAN** | Que declares: la cripto es patrimonio y las ganancias pagan impuestos (ver módulo 172) |
| **UIAF** | Lavado de activos: los exchanges reportan operaciones (ver módulo 173) |

**Definición rápida — exchange:** la plataforma (Binance, etc.) donde cambias pesos por cripto
y viceversa. Es una empresa privada, no un banco, y no tiene seguro de depósitos.

## Lo que esto significa en la práctica

1. Puedes operar tranquilo como persona natural, **pero** debes declarar (módulo 172).
2. Los bancos colombianos a veces son ariscos con transferencias hacia/desde exchanges:
   pueden pedir explicaciones o, en casos raros, cerrar cuentas. No es ilegal — es política
   interna de riesgo de cada banco.
3. Nadie te va a "rescatar" si un exchange quiebra. No hay Fogafín para cripto.
4. La regulación **cambia rápido**. Antes de cualquier decisión legal o fiscal importante:
   **verificar al día con contador_lushows o fuente oficial (DIAN, Superfinanciera)**.
   Este módulo da el mapa, no la letra chica vigente.

## Lo que NO es cierto (mitos)

- "La cripto es ilegal en Colombia" — falso.
- "Como no está regulada, no se declara" — falso y caro: la DIAN sí la considera patrimonio.
- "Binance está prohibido" — falso a la fecha de este módulo; opera con usuarios colombianos.
- "Ya que es anónimo, nadie se entera" — falso: los exchanges hacen KYC (módulo 171) y reportan.

## Cómo aplica al AGENTE TRADING

- El bot opera **paper trading** (dinero simulado): cero implicación legal o fiscal mientras
  no toque dinero real.
- Al pasar a live (post 22-ago-2026, con capital real chico): las ganancias reales entran al
  mundo DIAN → ruta obligada por **contador_lushows** antes del primer peso real.
- Diseño defensivo: el sistema asume que las reglas pueden cambiar (módulo 179) y por eso
  mantiene capital chico en exchange y todo documentado.
