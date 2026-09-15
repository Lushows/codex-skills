# 20 — Keyword research

Lee este módulo cuando vas a abrir una campaña de Search y no sabes por qué palabras pujar, o cuando tu cuenta gasta pero no vende y sospechas que estás pujando por búsquedas que no compran. El keyword research es el cimiento de Google: aquí no inventas demanda (eso lo hace Meta interrumpiendo el feed → `facebook_ads_lushows`), aquí **capturas** la demanda que ya existe escrita en el buscador. Frame que no debes soltar: **Google captura intención.** La persona ya levantó la mano y escribió lo que quiere; tu trabajo es estar ahí con la oferta correcta. En jun-2026, con AI Overviews comiéndose la parte de arriba del resultado orgánico y AI Max ampliando keywords solo (ver 90), el research dejó de ser "hago una lista una vez" y pasó a ser una disciplina viva alimentada por términos de búsqueda reales (ver 68).

## Las 3 intenciones — y por qué te importan en COP

Cada búsqueda esconde una intención. Pujar sin leerla es quemar plata.

| Intención | Qué busca la persona | Ejemplo (gastronomía) | ¿Pauto en Search? | CPC típico COP 2026 |
|---|---|---|---|---|
| Informacional | Aprender, todavía no compra | "cómo calcular el costo de un plato" | Casi nunca | $300–$700 |
| Comercial | Comparar, está evaluando | "mejor plantilla de costos para restaurante" | Sí, con cuidado | $700–$1.800 |
| Transaccional | Comprar YA | "comprar calculadora de costos gastronómicos" | Sí, prioridad #1 | $1.200–$3.500 |

La transaccional es oro porque la persona ya decidió; solo falta a quién le compra. Tu CPC será más caro ahí, pero la conversión paga. La informacional parece barata pero te llena la cuenta de curiosos que nunca pagan. Regla práctica para presupuestos pequeños (menos de $1.500.000 COP/mes): arranca **solo** transaccional + comercial alta, y deja lo informacional para contenido orgánico o Demand Gen (no es trabajo de Search pago). Si tu producto es de ticket bajo (la calculadora a $10.000 COP), haz la cuenta antes de pujar: si un clic transaccional te cuesta $2.000 y cierras 1 de cada 8 clics, tu CPA es $16.000 — pierdes en cada venta a menos que tengas recompra o ticket promedio mayor. La viabilidad económica la valida `economist_lushows`; el research no arregla un margen roto.

## Modificadores: las palabras que delatan al comprador

Una keyword "raíz" como *calculadora de costos* es ambigua. Los **modificadores** revelan la intención real:

- **De compra:** comprar, precio, cuánto cuesta, oferta, descuento, contratar, "online", "ya".
- **De marca:** tu nombre o el del competidor (ver 39 marca-genérico, 94 auction-insights).
- **Locales:** Bogotá, Medellín, "cerca de mí", "a domicilio", barrio. Decisivos si hay despacho o contraentrega (ver 26 geo).
- **De urgencia/calificación:** "para restaurante", "para dark kitchen", "para cafetería" — afinan a tu cliente real y filtran al consumidor suelto.

Una keyword es **raíz + modificador**. *Calculadora de costos* (raíz) + *para restaurante comprar* (modificadores) = una búsqueda que vale oro y casi nadie más puja. La long-tail (4+ palabras) tiene menos volumen pero CPC más barato y conversión más alta: *plantilla excel costo de recetas para dark kitchen* es más barata que *calculadora* y compra más.

## Construir el research como matriz, no como lista

El método que no falla: **matriz de raíces × modificadores.** En una columna pones tus raíces (calculadora de costos, plantilla de costos, food cost, costeo de recetas, precio de venta plato). En la fila de arriba pones los modificadores (para restaurante, para cafetería, excel, comprar, plantilla, descargar, Colombia). Multiplicas y obtienes decenas de combinaciones reales. De ahí descartas las informacionales y las que no despachas, y agrupas por intención. Plantilla mental:

```
RAÍZ            ×  MODIFICADOR        =  KEYWORD CANDIDATA
costeo recetas  ×  para restaurante   =  costeo de recetas para restaurante
plantilla costos × excel comprar      =  comprar plantilla de costos excel
food cost       ×  dark kitchen       =  control de food cost dark kitchen
```

## Herramientas — y el truco del Planner

El **Keyword Planner** (gratis dentro de Google Ads) es tu base. Dos modos:

1. **"Descubre nuevas keywords":** mete tu producto o la URL de tu landing y te escupe ideas con volumen y puja estimada.
2. **"Obtén volumen y pronósticos":** pega una lista y te dice búsquedas/mes y CPC estimado en COP.

Tres advertencias honestas:
- Los rangos de volumen son **amplios** (ej. "100–1.000"). Trátalos como dirección, no como verdad.
- Las pujas estimadas suelen quedar **cortas** frente a la subasta real. Súmales 30–50% al planear tu presupuesto.
- El Planner está sesgado a comercial. La long-tail real sale mejor del **reporte de términos de búsqueda** una vez prendes campañas (ver 68): ahí ves lo que la gente escribe DE VERDAD.

Complementa gratis con: autocompletar de Google (escribe tu keyword y mira las sugerencias), "Búsquedas relacionadas" al pie del resultado, "People also ask", y Google Trends para ver estacionalidad (las búsquedas gastro suben en apertura de negocios a inicio de año y antes de temporada alta). Para entender qué responde la gente con sus propias palabras, lee reseñas, grupos de Facebook de dueños de restaurante y comentarios — ahí está el lenguaje real del mercado.

## Mapear keyword → etapa del embudo

No todas las keywords van a la misma campaña ni al mismo anuncio. Mapéalas:

| Etapa | Keyword tipo | Adónde la mando |
|---|---|---|
| Descubrimiento | informacional | Orgánico / Demand Gen (ver 41) |
| Consideración | comercial ("mejor", "vs", "opiniones") | Search, anuncio que compara y educa |
| Decisión | transaccional ("comprar", "precio") | Search, anuncio directo + landing de cierre (ver 33) |
| Recompra/marca | tu nombre | Campaña de marca aparte (ver 39) |

Cada grupo de keywords con la misma intención = un grupo de anuncios con su propio RSA (ver 10 estructura, 30 RSA). Si mezclas "cómo calcular costos" con "comprar calculadora" en el mismo grupo, el anuncio no le habla a ninguno, baja tu relevancia y tu Quality Score (ver 36) cae — pagas más por cada clic. Una vez la landing convierte el clic, el cierre conversacional (WhatsApp, DM) lo trabaja `ventas_lushows`; la calidad de la landing, `desingweb-lushows`.

## Errores comunes — blacklist

1. **Pujar por informacional con presupuesto chico.** Gastas en curiosos. Empieza por transaccional; la educación que la haga el contenido orgánico.
2. **Tomar el volumen del Planner como exacto.** Son rangos, y la puja estimada casi siempre se queda corta — planea con 30–50% más.
3. **Una sola keyword raíz sin modificadores.** *Calculadora* sola trae de todo (de embarazo, de IMC, de calorías). Sin modificador + sin negativos (ver 22) es un hueco de plata.
4. **No separar marca de genérico.** Mezclar tu nombre con keywords genéricas infla tu CTR y te engaña: parece que el genérico funciona cuando es la marca la que convierte (ver 39).
5. **Investigar una vez y nunca más.** El lenguaje del mercado cambia. El reporte de términos de búsqueda semanal (ver 68) es tu research vivo.
6. **Ignorar el modificador local con producto físico/contraentrega.** Sin geo-keywords pagas clics de ciudades donde ni despachas (ver 26).
7. **Copiar la lista del competidor sin entender su intención.** Tú no sabes qué les convierte; puede estar quemando plata igual que tú.
8. **No hacer la cuenta de CPC × tasa de cierre antes de pujar.** Si el CPA proyectado supera tu margen, ninguna keyword te salva — revisa el negocio antes (ver `economist_lushows`).
