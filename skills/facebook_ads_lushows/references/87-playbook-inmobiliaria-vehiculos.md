# 87 — Playbook: Inmobiliaria y vehículos (special ad categories + alto ticket)

Venta/arriendo de inmuebles, proyectos de constructora, concesionarios, carros usados, motos. Dos realidades definen el vertical: (1) vivienda es **special ad category** en Meta — categoría especial con targeting restringido por reglas anti-discriminación — y (2) es alto ticket: **nadie compra una casa o un carro por un anuncio**; el anuncio vende la VISITA. Quien entiende esas dos cosas gana; quien no, colecciona leads basura o baneos.

## Special ad categories: la restricción (enforcement más duro en 2026)

Meta obliga a declarar la categoría **Vivienda** (también Crédito/finanzas y Empleo) al crear la campaña. Al marcarla:

- Sin targeting por **edad** ni **género** (queda 18-65+ todos).
- Sin **zip/códigos postales finos**; geo con radio mínimo de ~15 km.
- Audiencias limitadas: sin lookalikes clásicos (Meta da "audiencia especial" similar sin atributos sensibles), intereses recortados.

**Declárala SIEMPRE**: arriendo, venta, crédito hipotecario, todo lo que sea acceso a vivienda. No declararla "para targetear mejor" = rechazo y, reincidiendo, baneo (ver 08/93). En 2026 el **enforcement de HEC (vivienda/empleo/crédito) con detección automática** es más agresivo: correr una categoría que debía marcarse es causa común de restricción de cuenta (ver `actualizacion-2026-06`). Además hay nueva categoría especial **"Financial Products and Services"** (aplica a targeting US/US-targeted; si pautas a residentes de EE.UU. revísala). Vehículos NO es special category, salvo que pautes el crédito/financiación como producto financiero — ahí declara Crédito.

## Cómo ganar igual: el creativo segmenta

Lo que el targeting ya no puede, el creativo sí (ver 30/37): **el ad se auto-filtra**.

- "Apartamentos desde **$280 millones** en **Sabaneta** — separa con $5M" → el precio filtra presupuesto, la zona filtra geografía, el "separa con" filtra seriedad. Tres filtros en una línea.
- "¿Pagas más de $1.5M de arriendo en Bogotá? Esta cuota inicial te alcanza" → auto-selección por capacidad.
- **Ocultar el precio = leads basura.** El "escríbenos para info" sin precio trae 200 curiosos que preguntan el precio y desaparecen. El dato duro visible (precio, ubicación, financiación) es tu mejor filtro y tu mejor argumento.

## El funnel de ticket gigante

```
Ad (vende la visita, no el inmueble) → lead form con filtros o CTWA con bot calificador
  → contacto en MINUTOS → visita/test drive agendada → venta consultiva (meses)
```

- **Lead form** (ver 52) con preguntas obligatorias: presupuesto (rangos), ¿para cuándo buscas?, ¿crédito aprobado/pre-aprobado? — cada pregunta baja volumen y sube calidad: en alto ticket, calidad gana siempre. **Advantage+ Leads + verificación/calificación con IA** (2026) ayuda a limpiar la basura (ver `actualizacion-2026-06`).
- **CTWA con calificación de bot** (ver 50): el bot pregunta presupuesto/zona/tiempos y agenda con el asesor solo si califica. WhatsApp es donde el colombiano pregunta por finca raíz.
- **Velocidad de contacto BRUTAL**: un lead de un inmueble de $500M COP contactado en **5 minutos** convierte varias veces más que a las 24 horas (ver 52/96) — y ese lead costó caro. Alarma al asesor en tiempo real, no reporte diario.

## La cuenta concreta

| Campaña | Tipo | Objetivo | Creativos | Medición | % presup. |
|---|---|---|---|---|---|
| **Captación** | Advantage+ Leads (cat. Vivienda declarada) o CTWA | lead calificado | recorrido en video · dato duro en pantalla · cuota mensual | costo por **visita realizada** | 70-80% |
| **Retargeting largo** | Leads / tráfico, 90-180 días | visita | avance de obra · testimonio de comprador · inventario nuevo | costo por visita | 15-25% |
| **Catálogo (concesionario)** | Advantage+ catalog / DPA (ver 56) | lead / test drive | el carro que miró + similares | costo por test drive | si hay inventario |

## Creativos del vertical

- **Recorrido en video** del inmueble/proyecto (ver 34): vertical, 30-60s, estabilizado, recorrido natural puerta→espacios→vista. El formato rey.
- **Render vs real honesto**: si es sobre planos, dilo ("entrega dic 2027, imágenes de referencia") — el lead engañado se cae en la visita y quema al asesor.
- **El dato duro en pantalla**: precio, m², habitaciones, zona, cuota. Estática de ficha técnica funciona (ver 35).
- **Vehículos**: el carro andando + interior + el dato (modelo, km, precio, cuota). **Test drive como conversión**. Concesionario con inventario: catálogo + DPA (ver 56) — el retargeting muestra EL carro que miró.

## Financiación: el ángulo madre LatAm

"**Cuota desde $1.890.000/mes**" > "Apartamento de $310 millones" (ver 41). El comprador LatAm piensa en cuota mensual, no en precio total. Lo mismo en vehículos: "estrena moto desde $350.000/mes". Requisito: que la cuota sea real y defendible (tasa, plazo, cuota inicial en el disclaimer) — cuota engañosa = lead furioso + riesgo de policy y de Superintendencia. Si pautas el crédito como tal, declara categoría Crédito.

## Ofertas tipo del vertical

- **Separa con $X** (cuota inicial baja) — reduce la barrera de entrada del inmueble.
- **Cuota mensual desde $X** (con disclaimer) — el ángulo que más convierte.
- **Test drive a domicilio** / **valoración gratis de tu usado** — conversión de bajo costo.
- **Bono de estreno / electrodomésticos incluidos** (constructora) — diferenciador sin bajar precio.

## Nurturing de meses

El ciclo es de 3-18 meses: el lead que "por ahora solo está mirando" compra el año entrante — con quien le hizo seguimiento. Secuencia larga (ver 96): novedades del proyecto, avance de obra, cambios de tasas, inventario nuevo. Retargeting de 90-180 días con contenido, no con el mismo ad. El cierre consultivo de alto ticket → ventas_lushows 58.

## Presupuesto y benchmarks honestos (Colombia)

- Proyecto inmobiliario: **$100.000-$500.000+ COP/día** sostenidos; lead calificado **$15.000-$80.000 COP** (sin calificar puede ser $5.000 — y no servir). Vehículo usado/concesionario: lead $8.000-$40.000. CPM inmobiliario $9.000-$25.000.
- La métrica real: costo por **visita realizada** y por **venta** (lead→visita 10-30% con buen filtro y contacto rápido; visita→venta es oficio del asesor). Caveat: ciudad, estrato y tasa de interés del momento mueven todo.

## La velocidad de respuesta: el multiplicador #1 del vertical

En alto ticket, el lead se valora distinto: no por cuántos llegan sino por **qué tan rápido los tocas**. Estudios clásicos de lead response (y la experiencia de cualquier asesor serio) coinciden en que contactar en los primeros 5 minutos puede multiplicar varias veces la conversión a visita frente a hacerlo en una hora — y se cae a casi nada después de 24h. El lead inmobiliario o de vehículo costó $15.000-$80.000 COP: dejarlo enfriar es tirar esa plata. Sistema mínimo: el lead form o el CTWA disparan una **alerta en tiempo real** al asesor (no un correo que ve al día siguiente), un bot saluda y agenda en el primer minuto mientras el humano se conecta, y la visita queda en calendario antes de que el prospecto siga mirando otros tres proyectos. El bot calificador hace doble trabajo: responde en 0 segundos (gana la carrera de velocidad) y filtra por presupuesto/zona/tiempos (protege la agenda del asesor). En finca raíz y carros, quien contesta primero suele cerrar — la pauta solo entrega el balón; la velocidad anota.

## Ruteo a skills hermanas

Cierre consultivo, visita, objeciones y negociación de alto ticket → ventas_lushows. Ficha de proyecto/inventario con simulador de cuota y agendamiento → desingweb-lushows 66/72. Render, recorrido y marca del proyecto → directorcreativo_lushows. Viabilidad del proyecto y simulación de financiación → economist_lushows. Búsquedas "apartamentos en [zona]" / "[modelo] usado" → google_ads (intención altísima aquí); recorridos nativos → tiktok_ads.

## Errores comunes — blacklist

- No declarar special ad category de vivienda "para poder segmentar": camino directo al baneo (enforcement 2026 más duro).
- Ocultar el precio para "generar conversaciones": generas curiosos, no compradores.
- Contactar leads al día siguiente: en alto ticket el lead caro se enfría igual de rápido.
- Render vendido como entregado: la mentira se cae en la visita.
- Lead form sin filtros para presumir volumen: el equipo comercial muere tramitando basura.
- Evaluar la pauta a la semana cuando el ciclo es de meses: mide leads calificados y visitas, no ventas inmediatas.
- Cuota mensual inventada sin tasa ni plazo: problema legal, no solo de conversión.
