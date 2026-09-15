# 15 — Pujas (bidding)

Cada vez que alguien abre Facebook/Instagram, hay una subasta en milisegundos entre anunciantes que quieren mostrarle algo. La **estrategia de puja** define cómo compite tu plata en esa subasta. Lee este módulo cuando vayas a escalar, cuando tu CPA se descontrole, o cuando alguien te diga "ponle bid cap" sin explicarte qué es.

## Cómo se gana una subasta (el contexto)

Meta no le da el espacio al que más puja: ordena por **total value = puja × tasa de acción estimada + relevancia/calidad del anuncio**. Por eso un anuncio brutal con buena tasa de conversión gana espacio pujando menos que uno mediocre. La estrategia de puja es solo la parte "puja" de esa ecuación; el resto lo decide tu creativo (ver 30) y tu oferta (ver 41). Esto explica por qué "subir la puja" rara vez arregla una campaña mala.

## Las estrategias en 2026

| Estrategia | Qué hace | Riesgo principal |
|---|---|---|
| **Highest volume** (mayor volumen — default) | Gasta TODO el presupuesto buscando los resultados más baratos disponibles | El CPA sube al escalar: paga lo que cueste con tal de gastar |
| **Cost per result goal** (cost cap) | Mantiene tu CPA **promedio** ≤ X que defines | Si no encuentra conversiones a ese costo, **no gasta** (entrega frenada) |
| **Bid cap** (límite de puja) | Techo de lo que pujas en CADA subasta individual (no promedio) | Herramienta de experto: mal calibrado = entrega cero |
| **ROAS Goal** | Para value optimization (ver 14): apunta a un retorno objetivo sobre el gasto | Necesita valores de compra limpios; riesgo de no-entrega |
| **Minimum ROAS** (refinado 2026) | Pone un **piso** de ROAS: Meta no gasta por debajo de ese retorno, pero busca volumen por encima | Piso muy alto = no entrega; necesita señal de valor confiable |

> 🔁 **Novedad 2026 (ver `actualizacion-2026-06`):** el stack de valor se modernizó. Hoy combinas **Minimum ROAS / ROAS Goal** + **Value Rules** (reglas de valor: le dices a Meta que cierto cliente vale más — ej. nuevos 1.3×, clientes de cierta ciudad 1.2×) + **atribución incremental** (cuenta solo conversiones causadas, ver 16). Juntos, dejan de optimizar "ventas baratas" y empiezan a optimizar "ventas que valen e incrementales".

## Cuándo usar cada una

- **Empezar SIEMPRE con highest volume.** Necesitas descubrir tu CPA real antes de poder ponerle techo a nada. Mínimo 2-4 semanas y 50+ conversiones de historia.
- **Cost cap cuando**: ya conoces tu CPA tolerable (calcúlalo desde margen y LTV — ver 64 y economist_lushows) y quieres **escalar protegido**: subir presupuesto fuerte sabiendo que Meta no gastará en conversiones carísimas. Detalle de escalado con cost cap en 72.
- **ROAS Goal / Minimum ROAS**: solo con value optimization activa y señal de valor confiable (tickets dispares, ≥50 compras/sem con valor correcto). Minimum ROAS es más "amigable" que ROAS Goal duro porque pone piso sin matar volumen.
- **Bid cap**: solo si entiendes subastas a fondo y tienes una razón específica (ej. arbitraje de inventario barato). Para el 95% de cuentas: ignóralo.

## Cómo calibrar un cost cap (receta)

1. Saca tu **CPA real de los últimos 30 días** (backend, no solo Ads Manager — ver 16). Ej: $38.000 COP.
2. Pon el cap **10-20% POR ENCIMA**: $42.000-$46.000. Sí, encima. El cap se calibra sobre tu realidad, **no sobre tu deseo**: si tu CPA real es $38k y pones cap de $25k porque "eso quisiera pagar", Meta simplemente no gastará.
3. Déjalo correr 5-7 días sin tocar. Evalúa: ¿gastó el presupuesto completo? ¿CPA promedio respetó el cap?
4. Ajusta en pasos de 5-10%, máximo cada 3-4 días. Bajando el cap poco a poco puedes "exprimir" eficiencia; demasiado y se apaga la entrega.

## Cómo calibrar un ROAS Goal / Minimum ROAS (receta)

1. Saca tu **ROAS real de plataforma** de los últimos 30 días (ej. 2.4) y tu ROAS de **breakeven** (1 ÷ margen; si margen 40%, breakeven ROAS = 2.5 — ver 64).
2. Pon el objetivo **ligeramente por debajo de tu ROAS real actual** (ej. 2.2), no por encima de tu deseo. Igual que el cost cap: el algoritmo no entrega contra fantasías.
3. Activa **Value Rules** si quieres sesgar a clientes nuevos o de mayor valor (crecimiento vs cosecha).
4. Déjalo 5-7 días, evalúa entrega y ROAS contra backend. Sube/baja en pasos de ~0.2.

## Diagnóstico: síntomas de cap/objetivo mal puesto

| Síntoma | Diagnóstico | Acción |
|---|---|---|
| Gasta <70-80% del presupuesto diario | Cap muy agresivo / ROAS goal muy alto | Suelta 10-15% o vuelve a highest volume |
| Gasta todo y el CPA quedó muy por debajo del cap | Cap muy suelto (no protege nada) | Baja 5-10% gradual, o déjalo: protección barata |
| Gasta a borbotones (días de todo, días de nada) | Cap/objetivo al filo de lo viable | Aflójalo un poco; la entrega intermitente daña el aprendizaje (ver 13) |
| No gasta NADA | Cap absurdo vs realidad, o evento sin volumen | Revisa CPA real; quizá el problema es el evento (ver 14) |

## Lo que la puja NO arregla

La puja administra el costo, no lo crea. Si tu CPA es caro, la causa casi siempre está en: oferta floja (ver 41), creativos fatigados (ver 39), evento de optimización equivocado (ver 14), señal CAPI sucia con EMQ bajo (ver 22) o landing que no convierte (desingweb-lushows). Ponerle cost cap a una campaña mala solo hace que la campaña mala no gaste.

## Errores comunes — blacklist

- Lanzar cuenta nueva directo con cost cap o ROAS goal: no conoces tu CPA/ROAS real; estás adivinando y la campaña no entregará.
- Poner el cap en tu CPA *deseado* en vez de tu CPA *real*: el wishful thinking no puja en subastas.
- Poner un ROAS Goal por encima de tu ROAS real "para ganar más": Meta deja de entregar y crees que "se dañó".
- Cambiar la estrategia de puja en un ad set activo: edición significativa, resetea el aprendizaje (ver 13). Crea una campaña nueva.
- Ajustar el cap/objetivo todos los días persiguiendo el número de ayer: dale 72h mínimo entre ajustes.
- Usar bid cap "porque un gurú dijo": sin modelo de subasta propio, es la forma más rápida de pagar CPMs raros o no entregar.
- Creer que cost cap garantiza el CPA por conversión individual: es PROMEDIO; verás conversiones sueltas por encima del cap y es normal.
- Activar ROAS Goal / Minimum ROAS sin valores de compra limpios en el píxel/CAPI: optimizas contra números inventados.
