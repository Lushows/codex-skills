# 87 — Playbook inmobiliaria y vehículos

Lee este módulo cuando vendes **propiedades o vehículos** — inmobiliaria (venta/arriendo de casas, apartamentos, lotes, proyectos sobre planos), concesionarios, venta de usados, motos, maquinaria. Estas verticales comparten dos rasgos que mandan toda la estrategia: **alta intención + altísimo ticket**, y un **ciclo largo con decisión muy meditada**. Nadie compra un apartamento de $400 millones ni un carro de $80 millones desde un clic — pero SÍ empieza el camino buscando en Google. Aquí Google **captura** al comprador serio que ya investiga; tu trabajo es traer **leads calificados**, no curiosos, porque a este ticket un lead bueno justifica un costo alto. El cierre largo y consultivo es `ventas_lushows`; los números de margen/comisión/financiación, `economist_lushows`. Para GENERAR demanda (un proyecto nuevo, una promo de cuota inicial) Meta complementa (`facebook_ads_lushows`).

## Estructura: alta intención + leads con fricción

El ticket alto cambia la lógica: no buscas volumen de leads baratos, buscas **pocos leads muy calificados**. Y la forma de calificar es poner **fricción buena** en la captura (un formulario que el curioso no llena pero el interesado real sí).

| Campaña | Tipo | Puja | Presupuesto arranque COP | Rol |
|---|---|---|---|---|
| Marca / proyecto | Search | tCPA bajo | $8.000–18.000/día | "[Proyecto] apartamentos", "[concesionario]" |
| Alta intención | Search | tCPA (valor de lead) | $40.000–100.000/día | "apartamentos venta [zona]", "Mazda CX-30 precio" |
| Feed (vehículos/propiedades) | PMax con feed o Vehicle ads | tCPA/tROAS | $30.000–70.000/día | Listados con foto + precio (ver abajo) |
| Lead form | Search + lead form | tCPA | $15.000–35.000/día | Capturar interesado calificado (ver 52) |

- **Keywords con marco de compra:** "venta", "precio", "cuota inicial", "financiación", "[modelo] 2026", "[barrio] apartamentos", "test drive", "crédito hipotecario". Estas delatan intención de compra real, no de curiosear. Benchmark COP: el CPC de estas keywords corre alto ($3.000–12.000) porque el ticket lo aguanta y la competencia es feroz — pero una comisión de $15M justifica leads costosos.
- **Separa venta de arriendo / nuevo de usado:** tienen tickets, márgenes y compradores distintos; mézclalos y no sabes qué rinde ni puedes pujar bien.
- **Fricción buena en el lead:** un formulario que pide presupuesto, zona, tiempo de compra o que requiere agendar visita FILTRA al que solo mira. En ticket alto, un lead que costó $40.000 pero quiere comprar vale más que 20 leads de $2.000 que solo preguntan (ver 58 high-ticket). Con **AI Max / broad** en 2026, los negativos a nivel cuenta son críticos para no comprar tráfico de "ver casas bonitas" o "carros de lujo" sin intención (ver actualizacion, 22).

## Feeds de vehículos y propiedades

Google tiene formatos específicos para estos catálogos:

- **Vehicle ads (anuncios de vehículos):** muestran el carro con foto, precio, kilometraje, año — directo en el buscador. Viven de un feed en Merchant Center con cada vehículo del inventario. Ideal para concesionarios y venta de usados con muchas unidades. **Verifica disponibilidad en Colombia** antes de prometerlo — los formatos de vehículos tienen despliegue por país (ver 50 para la lógica de "verificar antes de vender").
- **Inmobiliaria:** Google no tiene un "real estate ads" universal como portales especializados; lo común es **PMax con feed de propiedades** (vía Merchant Center con custom labels o feed de páginas) o Search a landings de cada proyecto. Los portales (Metrocuadrado, Fincaraíz) capturan mucha búsqueda — decide si compites en Google directo o también listas allí; muchas veces conviene Google a TU landing del proyecto para quedarte el lead completo.
- **El feed debe tener** foto buena (en inmuebles/carros la foto ES la decisión), precio real, ubicación, características clave (área, habitaciones / año, km). Listado sin foto o con precio "consultar" rinde pésimo — el comprador de ticket alto descarta lo que no muestra precio.

**Concesionario vs inmobiliaria — dos calendarios distintos.** El concesionario vive de modelos y promociones ("[modelo] 2026", "plan de financiación", "salón del automóvil"), con picos en lanzamientos y fin de mes/año (cuotas de venta, descuentos). La inmobiliaria vive del proyecto y la etapa de obra ("sobre planos", "entrega inmediata", "subsidio de vivienda"), con un ciclo aún más largo y un comprador que compara financiación durante meses. No copies la estructura de uno al otro: el carro se decide en semanas, el apartamento en meses, y eso cambia la ventana de conversión, el presupuesto y la paciencia que necesitas.

## OCI por etapa: medir el lead largo

El ciclo es largo y por etapas; medir solo "lead capturado" hace que Google optimice a volumen de gente que pide info y nunca compra. Hay que medir por **etapa del pipeline** con OCI (ver 53):

| Etapa | Qué subir a Google |
|---|---|
| Lead capturado | Conversión micro (volumen, no objetivo principal) |
| Visita agendada / test drive | Conversión de más valor |
| Negociación / separación | Alto valor |
| Venta cerrada | Valor real de la operación |

- Guarda el **GCLID** cuando entra el lead; muévelo por el CRM; sube cada etapa con su valor. Así Google aprende a traer leads que se parecen a los que LLEGAN a visita y cierran, no a los que solo preguntan. Activa **Enhanced Conversions for leads** como base de señal first-party (ver actualizacion-2026-06).
- **Ventana de conversión larga:** una compra inmobiliaria puede tardar meses. No evalúes la campaña con ventana de 30 días; usa la ventana larga y juzga por leads calificados que avanzan, no por venta inmediata (ver 60, 64).

**Llamada y respuesta inmediata.** En ticket alto el lead que llama o agenda quiere atención YA: un asesor que responde en minutos cierra mucho más que uno que devuelve la llamada al otro día. Usa **asset de llamada / call ads** además del formulario (ver 51) y ten quién conteste en horario comercial extendido — el lead de un apartamento de $400M que llamó y nadie atendió se fue al proyecto vecino. La velocidad de respuesta es parte de la pauta, no del "después".

**Geo y presupuesto:** segmenta por la zona donde está la propiedad o donde compra el cliente del concesionario (ver 26). El presupuesto debe aguantar el ciclo largo — no esperes ROAS en la semana 1. Calcula tu costo por lead máximo desde el margen de UNA venta: si un apartamento te deja $15 millones de comisión y cierras 1 de cada 30 leads calificados, puedes pagar hasta ~$500.000 por lead calificado y seguir ganando. Ese cálculo es `economist_lushows`, no "se siente caro".

## Errores comunes — blacklist

1. **Buscar leads baratos en ticket alto.** A este precio quieres pocos leads calificados, no muchos curiosos. Pon fricción buena en la captura (ver 58).
2. **Optimizar a "lead capturado".** Te llenas de gente que pide info y no compra. Mide por etapa con OCI (visita, negociación, venta) — ver 53.
3. **Mezclar venta con arriendo / nuevo con usado.** Tickets y compradores distintos; no sabrás qué rinde ni pujar bien. Sepáralos en campañas.
4. **Listados sin foto o con precio "consultar".** En inmuebles y carros la foto y el precio son la decisión; sin ellos el feed rinde pésimo.
5. **Ventana de conversión corta.** El ciclo dura meses; evaluar a 30 días entierra campañas que iban a cerrar. Usa ventana larga (ver 64).
6. **Prometer vehicle ads sin verificar Colombia.** Formatos de vehículos tienen despliegue por país; confírmalo en la cuenta antes de venderlo (ver 50).
7. **No calcular el costo por lead máximo desde el margen.** "Se siente caro" no es análisis; una comisión de $15M aguanta un lead costoso. Calcula desde la venta (ver `economist_lushows`).
8. **No filtrar el tráfico amplio de AI Max.** Sin negativos a nivel cuenta, compras "casas bonitas" y "carros de lujo" sin intención. Negativos agresivos (ver 22, actualizacion).
