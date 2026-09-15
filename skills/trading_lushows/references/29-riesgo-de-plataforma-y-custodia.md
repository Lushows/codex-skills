# 29 — Riesgo de plataforma y custodia

Hay un riesgo que ningún stop, sizing ni disciplina cubre: que la plataforma donde vive el
dinero falle, congele retiros o desaparezca. **Riesgo de contraparte** = el riesgo de que
quien te guarda los fondos no te los devuelva. Se puede hacer todo bien en el trading y
perderlo todo por dónde estaba guardado.

## FTX: la lección que no se olvida

En noviembre de 2022, FTX — uno de los exchanges más grandes y "confiables" del mundo, con
auditorías, celebridades y estadios con su nombre — colapsó en días. Usó fondos de clientes
para tapar huecos de su empresa hermana; cuando se supo, hubo corrida, congeló retiros y
quebró. Millones de usuarios quedaron atrapados años en un proceso de quiebra (detalles y
cifras de recuperación: verificar, el proceso siguió evolucionando). Las lecciones:

1. El tamaño y la fama del exchange NO son garantía.
2. Cuando hay pánico, los retiros se congelan ANTES de que el usuario promedio reaccione.
3. El dinero en un exchange no es "tuyo guardado allá": es un pasivo que el exchange te debe.

No fue el único caso (Mt. Gox, Celsius, BlockFi...) — es un patrón del sector, no una
anécdota.

## "Not your keys, not your coins"

En cripto, quien controla las **llaves privadas** (la clave criptográfica que mueve los
fondos) controla el dinero. En un exchange, las llaves las tiene el exchange: tú tienes una
promesa. **Custodia propia** = guardar cripto en una billetera cuyas llaves solo tienes tú.

| Opción | Llaves | Riesgo principal |
|---|---|---|
| Exchange | Del exchange | Contraparte (quiebra, congelación, hackeo) |
| Billetera caliente (app/software) | Tuyas | Malware, phishing en tu dispositivo |
| **Billetera fría (hardware, offline)** | Tuyas | Perder el dispositivo Y la frase semilla |

La custodia propia traslada el riesgo: de confiar en terceros a tu propia disciplina
(guardar la frase semilla en papel, en sitio seguro, jamás en foto/nube). Para la mayoría,
ese trade vale la pena para el capital que NO se está operando.

## Cuánto dejar en el exchange

Regla práctica: en el exchange solo lo que el sistema NECESITA para operar — capital activo
más un colchón. Todo lo demás, custodia fría. La ganancia acumulada se "cosecha"
periódicamente (ej. mensual) hacia la billetera fría: así el riesgo de contraparte queda
acotado al capital operativo, nunca al patrimonio.

Complementos de higiene: exchange grande y regulado (menos malo ≠ seguro), 2FA con app (no
SMS), y whitelist de direcciones de retiro.

## API keys: el riesgo específico de un bot

Un bot opera con **API keys** (credenciales que permiten a un programa dar órdenes en tu
cuenta). Si se filtran — código subido a GitHub, servidor comprometido, .env expuesto — un
atacante opera tu cuenta. Mitigación no negociable: keys con permiso de **solo trading,
JAMÁS de retiro** (así el ladrón no puede sacar fondos), whitelist de IP del servidor,
secretos solo en variables de entorno (nunca en el repo), y rotación si hay cualquier duda.

## Cómo aplica al AGENTE TRADING

Hoy el riesgo es cero: paper trading, no hay dinero real en ningún exchange. Para el
go-live (22-ago-2026), checklist de custodia ANTES del primer trade real: (1) capital
inicial $200-500 en el exchange — solo lo operativo, regla de la quiebra del módulo 07;
(2) API keys sin permiso de retiro + whitelist de IP de Render; (3) .env fuera del repo,
verificado; (4) 2FA por app en la cuenta; (5) si el capital crece, cosecha mensual de
ganancias a custodia fría. El riesgo de plataforma no se elimina — se acota a un monto que
no cambia nada si se pierde.
