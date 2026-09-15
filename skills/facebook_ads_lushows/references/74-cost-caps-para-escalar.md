# 74 — Cost caps y minimum ROAS: escalar con red de seguridad

El cost cap (en la interfaz actual: "cost per result goal") es una estrategia de puja donde le dices a Meta: "tráeme todo el volumen que puedas mientras el costo PROMEDIO por resultado quede en ≤X". Su primo es el **minimum ROAS goal** (ROAS mínimo): "gasta mientras el retorno se mantenga ≥X". Lee este módulo cuando ya conoces tu CPA/ROAS real y quieres subir presupuesto fuerte sin miedo a que el gasto se descontrole. Son las herramientas de escalado PROTEGIDO de 2026 — y las más malentendidas: la mitad de la gente las prueba mal, ve que "no gastan" y las abandona.

## Cost cap vs minimum ROAS: cuál usar

| Usas… | Cuando tu KPI rector es… | Ejemplo |
|---|---|---|
| **Cost cap** (cost per result) | Costo por evento (CPA, costo por conversación, por lead) | "Cada venta ≤$30.000 COP en promedio" |
| **Minimum ROAS** | Retorno sobre inversión (ticket variable, e-com con catálogo) | "Que cada $1 gastado devuelva ≥$3 en ventas" |

Si tu ticket es fijo (un producto, un precio), cost cap es más simple. Si vendes catálogo con tickets muy distintos (un cliente compra $50k, otro $400k), minimum ROAS protege mejor el negocio porque optimiza por valor, no por número de compras. Ambos se calibran y se comportan igual: agresivos donde hay margen, frenan donde no.

## Cómo se comporta (entiéndelo o te frustrará)

- Con **highest volume** (la puja por defecto), Meta gasta TODO tu presupuesto al mejor costo que encuentre — sin techo. Si el día está caro, gasta caro.
- Con **cost cap / min ROAS**, Meta gasta **agresivo cuando encuentra conversiones dentro del objetivo, y FRENA cuando no**. Puede gastar el 100% del presupuesto un día y el 30% al siguiente.
- Punto mental clave: **un cap que no gasta no está "roto" — es el sistema diciéndote que a ese costo no hay volumen disponible**. Es información, no falla. La subasta te está cotizando el mercado.
- Es promedio, no techo absoluto: conversiones individuales pueden costar más de X mientras el promedio del conjunto quede dentro.

## Cuándo migrar de highest volume a cost cap / min ROAS

Las dos condiciones, ambas obligatorias:
1. **Ya conoces tu CPA/ROAS real sostenido** — semanas de datos con highest volume, no el número soñado de tu hoja de cálculo. Cap sin historial = calibrar a ciegas.
2. **Quieres subir presupuesto sin miedo al descontrol** — con cap calibrado puedes poner presupuestos altos porque el sistema solo gasta donde es rentable.

Si estás empezando (cuenta nueva, oferta nueva, sin ~50 conversiones/semana estables, ver 13): quédate en highest volume. El cap necesita señal madura para funcionar. En micro presupuesto (ver 79), olvídate del cap: no tienes el volumen — highest volume y punto.

## Cómo calibrar (la parte donde todos se equivocan)

1. **Arranca 10-20% ARRIBA de tu CPA promedio real.** Si tu CPA real de las últimas 4 semanas es $30.000 COP, el cap inicial es $33.000-$36.000. NO $20.000 "porque eso es lo que quisiera pagar". (Min ROAS: arranca 10-20% por DEBAJO de tu ROAS real — si tu ROAS real es 3.5, pon 2.8-3.0.)
2. **Cap en el sueño = cero entrega.** Es el error #1: poner el CPA deseado, la campaña no gasta nada, y concluir que "cost cap no sirve". El cap se calibra desde la realidad hacia abajo, no desde el deseo.
3. **Baja gradual**: si la campaña gasta su presupuesto completo con holgura varios días, baja el cap 5-10% por semana. Para cuando la entrega empiece a recortarse: ahí encontraste el precio real de tu volumen.
4. Cada movimiento de cap es un cambio significativo: uno por semana máximo, anotado en bitácora (ver 70). Mover el cap a diario persiguiendo la entrega de ayer lo resetea todo.

## El combo escalador

**Presupuesto alto + cap calibrado = el sistema gasta hasta donde es rentable y para solo.**

Con highest volume, presupuesto alto = riesgo de gastar caro. Con cap calibrado puedes poner 2-3× tu presupuesto normal: Meta lo usará solo si encuentra conversiones dentro del cap. El presupuesto deja de ser "lo que vas a gastar" y se vuelve "el máximo que autorizas si hay volumen rentable". Por eso el cap es la red del escalado vertical agresivo (ver 72): te deja escalar sin vigilar a diario, porque el piso de rentabilidad está cableado en la puja.

## Monitoreo

- **Si la entrega cae a <70% del presupuesto por 3+ días**: o subes el cap 5-10%, o mejoras los creativos. Mejor creativo = más gente convierte barato = más volumen cabe dentro del mismo cap. **El cap no arregla creativos malos** — solo te protege de pagarlos caro (ver 39).
- Revisa el CPA real vs cap semanalmente: si el real queda muy por debajo del cap consistentemente, hay espacio para bajar el cap o subir presupuesto.
- Entrega errática día a día es NORMAL con cap. Evalúa por semana, no por día.

| Síntoma | Diagnóstico | Acción |
|---|---|---|
| Cap nuevo no gasta nada | Cap puesto en el sueño | Subir cap a 10-20% sobre CPA real |
| Entrega <70% por 3+ días | Mercado no da volumen a ese precio | Subir cap 5-10% O mejorar creativo |
| CPA real muy bajo el cap | Hay holgura | Bajar cap 5-10% o subir presupuesto |
| Entrega errática día a día | Normal con cap | Nada, evaluar por semana |

## Bid cap vs cost cap

- **Cost cap**: controla el costo PROMEDIO por resultado. Meta puja flexible por ti. Para el 95% de los casos.
- **Bid cap**: techo máximo por subasta individual — control fino, pero exige saber cuánto vale cada impresión para ti y se sub-entrega brutalmente si calculas mal. Herramienta de avanzados con modelos de LTV; si estás leyendo esto para aprender, usa cost cap.

## Ejemplo numérico: calibración en 3 semanas

Pyme con CPA real $28.000 COP (4 semanas de historial en highest volume), presupuesto $150.000/día que quiere subir.

- **Semana 1**: activa cost cap en $33.000 (+18%). Sube presupuesto a $250.000/día. Resultado: gasta ~$230.000/día, CPA $30.500. Entrega sana (92%).
- **Semana 2**: baja cap a $30.000 (-9%). Resultado: gasta ~$200.000/día (80%), CPA $28.800. Sigue sano.
- **Semana 3**: baja cap a $27.000. Resultado: gasto cae a $120.000/día (48%) — el mercado no da volumen a ese precio. **Decisión**: volver a $30.000 y dejar ahí. Precio real del volumen encontrado: ~$29-30k. Para crecer más desde aquí: mejores creativos (ver 38, 39), no más presión al cap.

## Errores comunes — blacklist

- Poner el cap en el CPA soñado y concluir que "no gasta, cost cap no funciona".
- Activar cost cap en cuenta/oferta nueva sin historial de CPA real.
- Mover el cap todos los días persiguiendo la entrega de ayer.
- Entrar en pánico porque el lunes gastó 40% del presupuesto (el freno ES la funcionalidad).
- Usar bid cap "porque suena más pro" sin saber valuar una impresión.
- Esperar que el cap salve una oferta o creativos mediocres.
- Subir el cap 40% de un golpe en vez de 5-10% gradual.
- Usar min ROAS con tickets fijos donde cost cap era más simple (o al revés).
- No anotar los movimientos de cap en la bitácora (ver 70) y perder la lectura.
