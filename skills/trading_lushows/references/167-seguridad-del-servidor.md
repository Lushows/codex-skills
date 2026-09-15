# 167 — Seguridad del servidor: proteger el bot antes de que valga la pena atacarlo

## El principio

Hoy el bot maneja $1.000 simulados; nadie lo va a atacar por deporte. Pero en live tendrá
**API keys que mueven dinero real**, y todo lo expuesto a internet recibe escaneos automáticos
constantes (bots que prueban puertas). La seguridad se instala ANTES de que haya botín.

## Lo que ya está (y por qué)

| Medida | Qué es | Estado |
|---|---|---|
| **Basic auth** | Usuario+contraseña que el navegador pide antes de mostrar el dashboard | ✅ Activo en todo el server (`DASHBOARD_USER`/`DASHBOARD_PASS`) |
| **Secretos en env vars** | Las claves viven en variables de entorno de Render, no en el código | ✅ Nada sensible en el repo de GitHub |
| **`npm audit`** | Comando que revisa si las dependencias tienen vulnerabilidades conocidas | ✅ Parte de la higiene (correrlo con cada actualización) |
| Pocas dependencias | Menos paquetes = menos superficie de ataque (supply chain) | ✅ Decisión de arquitectura (módulo 160) |

Sobre los secretos: la regla es simple — **si está en GitHub, considéralo público**. Una key
subida por error se rota (se genera una nueva y se invalida la vieja), no se "borra del historial".

## Endurecer antes del go-live (checklist Fase 8)

1. **HTTPS only.** Render ya sirve HTTPS, pero hay que asegurar que nada responda por HTTP plano:
   el basic auth viaja en cada request y sin TLS iría legible por la red.
2. **Rate limiting.** Limitar intentos por IP (p. ej. en el login y en la API). Sin esto, un bot
   puede probar contraseñas contra el basic auth toda la noche. Contraseña larga y aleatoria
   ayuda, pero el límite de intentos es la defensa estructural.
3. **API keys de Binance con permisos mínimos.** Al crearlas: habilitar SOLO spot trading,
   **deshabilitar retiros (withdrawals)** — así, incluso robada, la key no puede sacar fondos —
   y restringirla por IP a la IP saliente del servicio de Render Frankfurt.
4. **Separar lectura de acción.** Idealmente el dashboard usa credenciales que no pueden ordenar
   nada; solo el proceso del bot toca la key de trading.
5. **No filtrar secretos por logs ni por `/status`.** Revisar que ningún endpoint devuelva
   variables de entorno o headers sensibles.
6. **Rotación:** cambiar `DASHBOARD_PASS` y las keys si alguna vez se compartió pantalla,
   se pegó en un chat, o "por si acaso" cada tanto.

## Amenazas realistas (sin paranoia de película)

- **Escaneo masivo:** bots que buscan dashboards abiertos. Lo para el basic auth + rate limit.
- **Dependencia comprometida:** un paquete de npm con malware. Lo mitiga tener pocas dependencias
  y `npm audit`.
- **Fuga de key por descuido propio:** históricamente la causa #1 en proyectos pequeños. Lo mitiga
  la disciplina de env vars + permisos mínimos + no-withdrawals.

Lo que NO es amenaza realista a esta escala: hackers dedicados, 0-days a medida. No hay que
diseñar para la NSA; hay que cerrar las puertas que los escáneres automáticos empujan.

## Cómo aplica al AGENTE TRADING

Regla de oro para el go-live: **la key de Binance sin permiso de retiro y atada a la IP de
Frankfurt**. Con eso, el peor escenario de un robo de credenciales es que alguien opere mal con
el saldo (malo), no que lo vacíe hacia su billetera (catastrófico). Rate limiting + HTTPS only
completan el trío mínimo antes del 22-ago-2026.
