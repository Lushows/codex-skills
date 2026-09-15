# 46 — Demand Gen para LatAm

Lee este módulo cuando vendas en Colombia o LatAm con destino **WhatsApp, lead o llamada** y quieras usar Demand Gen como tu motor visual dentro de Google, o cuando dudes si Demand Gen reemplaza o complementa a tu pauta de Meta. La frase clave del oficio: **Google captura demanda, Meta la genera** (`facebook_ads_lushows`). Demand Gen es el punto medio — genera demanda visual *pero dentro de Google*, aprovechando señales de intención que Meta no tiene. Para el comprador latino, móvil-primero y WhatsApp-primero, esto cambia cómo armas la campaña. Cómo se construye Demand Gen por dentro está en 41; aquí va su uso específico para el mercado de la región.

## El destino manda: WhatsApp, lead o llamada

En LatAm la venta rara vez termina en un checkout web frío; termina en una conversación. Demand Gen te deja apuntar a los destinos que de verdad funcionan aquí:

| Destino | Cuándo es el mejor | Qué medir |
|---|---|---|
| WhatsApp (clic-a-chat) | Producto que necesita conversar/cerrar a mano; ticket medio-alto | Chats iniciados → ventas |
| Lead form nativo | Volumen, captura rápida sin landing (ver 52) | Leads → cierre (ver 53) |
| Llamada | Servicios urgentes, público mayor, alto ticket | Llamadas válidas (>60s) |
| Landing web | Producto digital de compra directa (ver 33, 48) | Conversiones en sitio |

Regla práctica Colombia: si tu venta se cierra hablando, **manda el clic a WhatsApp**. Cada paso de fricción entre el video y el chat pierde gente; el latino que se interesa quiere escribir ahora, no llenar tres campos y esperar correo. El cierre de esa conversación es oficio de `ventas_lushows`. A jun-2026 el destino de mensajería de Demand Gen está disponible directo en varios mercados LatAm; donde no, usa una landing-puente con botón WhatsApp gigante arriba (ver 48).

### Benchmarks Colombia (jun-2026, órdenes de magnitud)

| Métrica | Rango típico |
|---|---|
| CPM Demand Gen | $6.000–$20.000 COP |
| CPV video | $25–$120 COP |
| CPA chat WhatsApp iniciado | $3.000–$15.000 COP según nicho/ticket |
| CPL lead form nativo | $2.000–$10.000 COP (ojo: lead barato ≠ lead bueno, ver 52) |
| % tráfico móvil | 80–90% |

Si tu CPA por chat se dispara a $30.000+ en un producto de ticket bajo, revisa creativo (hook, ver 42), audiencia-semilla y congruencia del destino (ver 48), no subas la puja a ciegas.

## Cómo armar la Demand Gen para que rinda en la región

1. **Audiencias-semilla locales.** Sube tu lista de clientes (Customer Match, ver 25) y tu remarketing (ver 24); Google genera **segmentos similares** (su versión de lookalike). En LatAm la lista propia rinde más que los intereses genéricos: tus clientes reales son el mejor molde. Semilla mínima útil ~1.000 contactos (ver 41).
2. **Creativo móvil y vertical.** El 80–90% del tráfico es celular de gama media. Video **9:16** para Shorts, **subtítulos quemados** (arranca mudo), texto grande, zona segura (ver 42). El look se dirige en `directorcreativo_lushows`.
3. **Localiza el mensaje** (ver 47): español que suene del país, no traducción de gringo. Precio en **COP**, modismos que convierten ("de una", "sin enredos"), **tú/usted** según público.
4. **Empieza amplio, deja aprender.** Demand Gen necesita 1–2 semanas y volumen (~$30–50k COP/día) para que los segmentos similares calienten. No la apagues a las 48 horas por pánico (ver 13 smart-bidding, 61 diagnóstico).
5. **Conecta el cierre offline (OCI, ver 53):** en LatAm el lead cierra por WhatsApp días después; si no devuelves esa venta a Google, optimiza por leads baratos, no por compradores.

## Cuándo complementa a Meta — y cuándo no

| Situación | Demand Gen | Meta |
|---|---|---|
| Generar demanda fría masiva y barata | Sirve, pero Meta suele ganar en volumen frío | Fuerte |
| Generar demanda con señales de intención de Google | **Demand Gen gana** (lo que Meta no tiene) | Limitado |
| Capturar al que ya busca "comprar X" | No — eso es Search | No |
| Reforzar a quien ya te vio/buscó (remarketing visual) | Muy bueno | Bueno |
| Diversificar para no depender solo de Meta | **Sí, esa es la jugada** | — |
| Reactivar tu lista de clientes con video | Muy bueno (Customer Match + similares) | Bueno |

La verdad honesta: **Demand Gen no reemplaza a Meta para demanda fría masiva** — Meta sigue siendo el rey de generar interés en quien no te conocía. Pero Demand Gen **complementa** porque (a) usa señales de intención de Google que Meta no posee, (b) te diversifica para no depender de una sola plataforma —si Meta te banea la cuenta mañana, no te quedas en cero—, y (c) reactiva visualmente a quien ya tuvo contacto contigo. Si solo tienes plata para una y necesitas captura caliente, primero **Search**; si necesitas generación fría barata, primero **Meta**; Demand Gen entra a complementar, no a sustituir.

## Plantilla de campaña Demand Gen LatAm

```
PAÍS/CIUDAD: Colombia / [Bogotá, Medellín…]  (geo: ver 26)
DESTINO: WhatsApp directo  (fallback: landing-puente con botón WA arriba, 48)
CREATIVO: video 9:16 con hook 5s + subtítulos quemados (42)
          + imágenes 1:1 / 4:5
TONO: usted (dueños de negocio adultos) — colombiano práctico (47)
PRECIO EN COPY: "$10.000 COP — pago único — hoy"
AUDIENCIA: Customer Match (lista) + similares + remarketing (24)
           + intereses gastronomía/restaurantes
PUJA: Max conversiones → tCPA $______ COP   PRESUPUESTO: $______/día
MEDICIÓN: chats iniciados (14) + OCI venta (53)
CIERRE: pasar lead a ventas_lushows en <5 min
```

## El stack de pauta LatAm: dónde encaja Demand Gen

Para un negocio colombiano con presupuesto limitado, el orden de prioridad de canales suele ser:

| Prioridad | Canal | Trabajo que hace |
|---|---|---|
| 1 | **Search** (Google) | Captura al que ya busca "comprar X" — intención caliente |
| 2 | **Meta** (FB/IG) | Genera demanda fría masiva y barata (`facebook_ads_lushows`) |
| 3 | **Demand Gen** (Google) | Genera demanda visual con señales de intención + reactiva tu lista + diversifica |
| 4 | **Remarketing** (Display/Demand Gen) | Recuerda a quien ya te vio (ver 24, 43) |
| 5 | **TikTok** | Demanda fría joven/viral (`tiktok_ads_lushows`) |

Demand Gen no pelea con Search ni con Meta: ocupa el espacio que ninguno de los dos cubre — demanda visual con intención, dentro de Google. Si ya tienes Search + Meta corriendo y una lista de clientes, Demand Gen es tu siguiente movimiento natural. La estrategia de mezcla de canales y unit economics la valida `economist_lushows`.

## Por qué WhatsApp gana en LatAm (y cómo no desperdiciarlo)

El comprador latino confía en la conversación, no en el checkout frío. Pero un chat iniciado no es una venta:

- **Responde en <5 minutos.** El lead que escribe y no recibe respuesta en minutos se va a la competencia. Automatiza el primer mensaje (un bot tipo "Luis" de GastroLatam) y que un humano cierre.
- **No abuses del bot:** el latino detecta el robot frío. El bot califica y agenda; el cierre fino es de `ventas_lushows`.
- **Mide el embudo completo:** chats iniciados → conversaciones reales → ventas. Un canal que trae 100 chats basura pierde contra uno que trae 20 que cierran (ver 49, 53).

## Errores comunes — blacklist

1. **Mandar el clic a una landing fría cuando el público quiere conversar.** En LatAm WhatsApp cierra mejor; cada paso de fricción pierde gente.
2. **Creer que Demand Gen reemplaza a Meta para demanda fría.** No lo hace — complementa. Meta sigue ganando en volumen frío masivo.
3. **Usar creativo horizontal de escritorio.** El público es móvil vertical; sin 9:16 y sin subtítulos quemados, lo saltan (ver 42).
4. **Arrancar sin audiencias-semilla locales (o con <1.000 contactos).** Sin tu lista, los similares van a ciegas. Sube Customer Match primero (ver 25).
5. **Apagar la campaña a las 48 horas.** Demand Gen necesita aprender; el pánico temprano mata campañas que iban a rendir (ver 13).
6. **Traducir literal el mensaje gringo.** El latino huele la traducción y desconfía. Localiza de verdad (ver 47).
7. **Capturar leads y no cerrarlos rápido.** El lead latino se enfría en minutos; pásalo al cierre de `ventas_lushows` de inmediato (ver 53, 54).
8. **No subir las ventas offline.** Sin OCI, Google te trae leads baratos que no compran, no clientes (ver 53).
