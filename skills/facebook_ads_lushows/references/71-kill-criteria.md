# 71 — Kill criteria: cuándo apagar sin pánico ni piedad

Saber matar es tan importante como saber lanzar. Lee este módulo antes de lanzar cualquier test (los criterios se escriben ANTES, ver 70) y cada lunes en tu revisión semanal. Aquí está el sistema para apagar perdedores sin **pánico** (matar por un mal día) ni **piedad** (mantener vivo un muerto "porque me gusta el creativo"). Las dos son enfermedades caras: el pánico te hace matar futuros ganadores en su día malo; la piedad te hace financiar muertos con la plata del campeón. El kill criteria es la vacuna escrita contra ambas.

## La matemática del kill

Cada peso invertido en un perdedor es un peso que tu ganador no recibió. Eso se llama **costo de oportunidad**: si tienes $100.000 COP/día y el 40% se va a un ad set con CPA al doble del objetivo, no estás "dándole tiempo" — estás financiando la mediocridad con el presupuesto del campeón. Matar rápido lo claramente muerto es la forma más barata de "optimizar".

Regla mental: un perdedor mantenido 1 semana extra "por si acaso" a $30.000/día son $210.000 COP que no compraron ventas. En un año, esos "por si acaso" suman millones. La piedad tiene precio y lo paga tu utilidad.

## El umbral universal: gasto vs CPA

Todo kill criteria sano se ancla en **gasto acumulado medido en múltiplos de tu CPA objetivo**, no en pesos absolutos ni en días sueltos. "Gastó $50.000 sin vender" no dice nada; "gastó 2× su CPA objetivo sin vender" sí. Calibra cada umbral a TU CPA y TU ticket:

- **Ticket bajo / ciclo corto** (producto $20-100k, compra impulsiva): umbrales en el borde bajo (1.5-2× para ads, 3× para ad sets). El sistema decide rápido.
- **Ticket alto / ciclo largo** (cursos, servicios, B2B, $300k+): umbrales en el borde alto (2-3× ads, 4-5× ad sets) y mira métricas blandas antes de matar — una sola venta tarda más en llegar.

## Kill criteria por nivel

### Nivel AD (anuncio individual)
- **Regla base**: gastó 1.5-2× tu CPA objetivo sin UNA sola conversión → pausa.
  - Ejemplo: CPA objetivo $30.000 COP → un ad que gastó $45.000-$60.000 con cero ventas, se pausa.
- **Matiz de volumen y ticket**: en tickets altos o ciclos de compra largos (cursos, servicios, B2B), una conversión puede tardar más. Ahí extiende a 2-3× CPA y mira métricas blandas antes de matar (ver 68): CTR, costo por clic en link, % de video visto, costo por conversación iniciada. Si las blandas son buenas, dale una ventana más; si también son malas, muerte sin apelación.

### Nivel AD SET / campaña de test
- Gastó 3-5× tu CPA objetivo Y su CPA real está >150% del objetivo → mata o re-trabaja (cambia el ángulo/oferta, no solo el color del botón).
- Ejemplo: objetivo $30.000 → gastó $120.000 con CPA de $50.000 (166%) → fuera.
- Si el CPA está entre 100-150% del objetivo: no mates aún; revisa si un solo ad malo está arrastrando el promedio y mata solo ese ad.

### Nivel GANADOR EN DECLIVE (el caso difícil)
Un ex-campeón con CPA >130% de su histórico durante **5-7 días seguidos** (no 1 día, no 2). Antes de matar, diagnostica en este orden (ver 75 para el checklist completo):
1. ¿Fatiga creativa? Frequency subiendo + CTR cayendo (ver 39) → refresca creativo, no mates la campaña. **Es la causa #1 con diferencia.**
2. ¿Temporada? CPMs de toda la cuenta subieron (ver 19, 77) → no es tu anuncio, es el mercado.
3. ¿Competencia? Alguien nuevo pujando fuerte en tu nicho → revisa Auction Insights y Ad Library (ver 94).
4. ¿Tocaste algo? Revisa la bitácora (ver 70).
5. ¿Medición rota? Píxel/CAPI caído reporta CPA infinito con ventas reales sanas (ver 62).

Solo después del diagnóstico decides: refrescar creativo, reducir presupuesto al último nivel rentable, o matar. Matar un ganador histórico sin autopsia es tirar un activo a la basura.

## Lo que NO es kill criteria

- **Un mal día.** La varianza diaria es ruido (ver 70). Nunca mates por 24 horas.
- **CTR bajo con CPA bueno.** ¿A quién le importa el CTR si vende rentable? Las métricas blandas son diagnóstico, no sentencia.
- **Corazonadas.** "Siento que no va a funcionar" no es un dato. Si gastó menos del umbral, espera.
- **Que a ti no te guste el anuncio.** El feo que vende le gana al bonito que no (ver 32).
- **Una subida de CPA explicada por el mercado.** Si todo el nicho subió de CPM, matar tus ads no baja el CPM (ver 76).

## Autopsia del muerto (30 segundos, obligatoria)

Antes de pasar página, responde: **¿qué capa falló?** (ver 61)
- ¿No lo vieron? (CPM altísimo, poca entrega) → problema de subasta/calidad de la cuenta o del creativo (relevancia baja).
- ¿Lo vieron y no hicieron clic? (CTR <0.5-1%) → el gancho/creativo no conecta (ver 37).
- ¿Hicieron clic y no convirtieron? (clics buenos, cero ventas) → landing u oferta (ver 41, 48; desingweb-lushows para la landing).

Anota la conclusión en tu archivo de learnings (ver 17). Un muerto sin autopsia es plata perdida dos veces: la que gastaste y la lección que botaste. Tres autopsias que dicen "clic bueno, cero venta" = tu problema no es la pauta, es la oferta o la página (ver 41).

## Reglas automáticas: tu red nocturna

En Ads Manager → Reglas automáticas, configura como **seguro contra desastres**, no como piloto automático:

- **Regla anti-sangría (ad)**: SI gasto del ad > 2× CPA objetivo Y compras = 0 (ventana: últimos 3 días) → pausar anuncio + notificarme por email. Evaluación: cada hora.
- **Regla de gasto loco (campaña)**: SI gasto de la campaña hoy > 150% del presupuesto diario esperado → notificarme (solo avisa, no pauses campañas enteras en automático).
- **Regla de CPA roto (ad set, opcional)**: SI CPA últimos 3 días > 200% objetivo Y gasto > 4× CPA → pausar ad set + avisar.

La regla te protege mientras duermes; las decisiones de verdad las tomas tú el lunes con datos de 7 días. NUNCA dejes una regla que pause campañas enteras en automático y la olvides: un día de ruido puede apagarte el negocio a las 3am.

## Tabla resumen

| Situación | Umbral | Acción |
|---|---|---|
| Ad sin conversiones | Gastó 1.5-2× CPA objetivo | Pausar (2-3× si ticket alto: mira blandas antes) |
| Ad set/test caro | Gastó 3-5× CPA y CPA >150% objetivo | Matar o re-trabajar ángulo/oferta |
| Ad set tibio | CPA 100-150% del objetivo | No matar; buscar el ad podrido y matar solo ese |
| Ganador en declive | CPA >130% histórico por 5-7 días | Diagnóstico (fatiga/temporada/competencia/medición) → luego decidir |
| Un mal día | Cualquier métrica fea de 24h | NADA. Esperar. |
| CPA roto por mercado | CPM de toda la cuenta arriba | Aguantar/ajustar oferta, NO matar (ver 76) |
| Madrugada | Gasto >2× CPA sin conversión | Regla automática pausa + te avisa |

## Errores comunes — blacklist

- Matar a las 12 horas porque "no ha vendido nada" con $15.000 COP gastados.
- Mantener un perdedor 2 semanas "porque el creativo me encanta".
- Matar un ganador histórico por UN día malo, sin diagnóstico.
- Usar CTR como criterio de muerte ignorando que el CPA es rentable.
- No hacer autopsia: matar y lanzar lo siguiente sin aprender nada.
- Anclar umbrales en pesos absolutos en vez de múltiplos de tu CPA.
- Dejar reglas automáticas que pausan campañas enteras y olvidar que existen.
- No pre-escribir los umbrales y decidir "según cómo lo vea" cada noche.
- Matar ads sanos cuando el verdadero muerto es el píxel (ver 75 paso 2).
