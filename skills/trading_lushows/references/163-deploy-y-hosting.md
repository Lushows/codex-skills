# 163 — Deploy y hosting: dónde vive el bot y por qué

## Qué significa "deploy"

Deploy = poner el código a correr en un servidor que no se apaga (a diferencia del PC de Luis).
Un bot de trading 24/7 necesita: proceso siempre encendido, disco que sobreviva reinicios,
y — detalle que casi nadie cuenta — **una IP en el país correcto**.

## La configuración actual: Render.com

| Pieza | Valor | Nota |
|---|---|---|
| Plan | Starter (pago) | El free tier "duerme" el servicio sin tráfico — inservible para un bot 24/7 |
| Disco | Persistente, montado en `data/` | Sin él, cada redeploy borra portafolio y memoria |
| Deploy | Auto-deploy desde GitHub `main` | Push → Render reconstruye y reinicia solo |
| Región | US (Oregon) — ⚠️ a migrar | Ver geo-bloqueo abajo |

Costos: el plan Starter cuesta del orden de pocos USD/mes y el disco se cobra aparte por GB —
**verificar precios al día en render.com/pricing**, cambian con el tiempo.

## Por qué la región importa: el geo-bloqueo

Binance **bloquea el trading desde IPs de Estados Unidos** (por regulación: en USA solo opera
Binance.US, otra empresa). Consecuencias reales para el bot:

- Los **datos** de mercado sí llegan (vía el mirror de solo lectura `data-api.binance.vision`).
- Las **órdenes** (crear, cancelar, OCO) desde una IP de USA serían rechazadas.
- Por eso el paper trading funcionó 44 días en Oregon, pero el **go-live exige mudarse**.

Plan Fase 8: recrear el servicio en **Render Frankfurt** (región UE, sin bloqueo de Binance).
Ojo: en Render no se "mueve" un servicio de región con un clic — se crea uno nuevo en Frankfurt,
se copia el contenido de `data/`, se apunta el auto-deploy y se apaga el viejo.

## Alternativas evaluadas (honesto)

| Opción | A favor | En contra |
|---|---|---|
| **Render** (actual) | Auto-deploy desde GitHub, disco fácil, cero administración de servidor | Menos control; el disco no tiene backups automáticos hacia afuera |
| **VPS** (Hetzner, DigitalOcean...) | Más barato por potencia, control total, eliges país exacto | Tú eres el sysadmin: actualizaciones, firewall, reinicios, seguridad — mal trato para no técnicos |
| **Fly.io** | Regiones muy flexibles, buena latencia | Más fricción de configuración (CLI, volúmenes); curva más técnica |

Para el perfil de Luis, Render sigue siendo la elección correcta: lo que se paga de más se
recupera en no-administrar-servidores. Un VPS solo se justificaría si el costo mensual doliera
o se necesitara algo que Render no ofrece.

## Cómo aplica al AGENTE TRADING

Checklist de la migración a Frankfurt (antes del go-live 22-ago-2026): ① crear servicio en
Frankfurt con disco persistente, ② copiar variables de entorno (incluidas `DASHBOARD_USER/PASS`
y las API keys), ③ transplantar `data/`, ④ verificar `/status` y que las órdenes de testnet
pasen desde la IP nueva, ⑤ apagar el servicio de US. Nada de esto es urgente para paper,
pero es **bloqueante** para live: sin IP fuera de USA no hay órdenes reales.
