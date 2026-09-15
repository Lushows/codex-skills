# Audiencias en 2026

> **Frontera**: la mecánica de públicos —cómo se crean, sincronizan, excluyen, qué señales usa el
> sistema, ventanas y tamaños mínimos— pertenece a la plataforma. **Para el detalle de configuración,
> invoca `facebook_ads_lushows`** o `tiktok_ads_lushows`. Aquí se decide **a quién le habla tu video**,
> que es una decisión de producto y de mensaje, no de checkbox.

## Lo que cambió

Durante una década la ventaja competitiva fue encontrar el interés secreto. En 2026 eso se acabó: con
entrega automatizada (Advantage+ y equivalentes) la máquina encuentra al comprador mejor que tú, y lo
hace leyendo **quién reacciona a tu creativo**. La segmentación se mudó adentro del video.

| Antes (2018-2022) | Ahora (2026) |
|---|---|
| 15 conjuntos, 15 intereses | 1 conjunto amplio |
| El ganador era una audiencia | El ganador es un ángulo |
| Creativo: 3 por mes | Creativo: 8-15 por semana (`262`) |
| Se optimizaba segmentación | Se optimiza mensaje |

## La audiencia sigue existiendo, pero vive en el guion

Tú no la eliges en el panel: la eliges cuando decides **para quién escribes**. Un mismo producto le
habla a públicos distintos según el ángulo.

Ejemplo, bundle organizador de cocina ~1.099 MXN:

| A quién le hablas | Dolor | Primera línea del guion |
|---|---|---|
| Mamá con cocina chica | Desorden que no cede | "Mi alacena era un desastre y no podía comprar otra casa" |
| Recién independizado | Cocina improvisada | "Me mudé solo y mi cocina parecía bodega" |
| Quien busca regalo de diciembre | No sabe qué regalar | "Si no sabes qué regalarle a tu mamá, ve esto" |
| Quien cocina mucho | Perder tiempo buscando | "Perdía 10 minutos buscando la tapa correcta" |

Son cuatro audiencias reales. Ninguna se seleccionó en un menú. Ver `250`.

## Cuándo la segmentación SÍ importa todavía

| Caso | Por qué |
|---|---|
| País y ciudad | Envío, moneda, aduana, CPM (`10`, `20`) |
| Idioma | Obvio y muy mal hecho: español de España en México mata el CVR |
| Edad, cuando el producto es legalmente restringido | Cumplimiento |
| Edad, cuando el público real es 55+ | El sistema tarda en encontrarlos; ayuda acotar |
| Retargeting | Ahí la lista **es** la audiencia (`271`) |
| Mercados muy chicos | Con población pequeña, "amplio" ya está acotado |

Fuera de esta lista, en 2026 acotar suele subir el CPM sin subir el CVR.

## Amplio vs acotado: la comparación honesta

| | Amplio | Acotado por intereses |
|---|---|---|
| CPM | Menor | 15-40% mayor |
| Tiempo de aprendizaje | Más rápido (más señal) | Más lento |
| Techo de escala | Alto | Bajo: se satura |
| Depende de | Tu creativo | Tu hipótesis, que suele ser mala |
| Recomendación 2026 | **Por defecto** | Solo con razón explícita |

## Los públicos que sí construyes tú

Estos no los inventa el algoritmo; salen de tu operación y son tu activo:

| Público | Cómo se llena | Valor |
|---|---|---|
| Visitantes del sitio | Píxel, desde el día 1 | Base del retargeting (`271`) |
| Añadieron al carrito | Píxel | La lista más rentable |
| Compradores | Píxel + pedidos | Excluir de frío; usar para recompra |
| Lista de correo / WhatsApp | Captura propia (`272`) | Independiente de la plataforma |
| Vieron 50%+ de tus videos | Plataforma | Alimenta retargeting barato |

**Instala el píxel antes del primer peso de pauta.** Un mes de tráfico sin píxel es un mes de
audiencias perdidas que no se recuperan. Configuración: `facebook_ads_lushows`.

## Exclusiones: la única "segmentación" que siempre vale

| Excluir de | A quién | Por qué |
|---|---|---|
| Campañas de frío | Compradores últimos 30-60 días | No pagar por quien ya compró |
| Retargeting de carrito | Quienes ya compraron | Evitar el anuncio molesto y el gasto muerto |
| Todo | Tu propio equipo y tus dispositivos | Limpiar datos |

## Cuando el resultado es malo, ¿es la audiencia?

Casi nunca. Árbol corto (completo en `267`):

| Síntoma | Culpable probable | Audiencia culpable si... |
|---|---|---|
| CTR < 1% | Creativo / hook | ...estás vendiendo bastones a los 18 años |
| CTR alto, CVR bajo | Página u oferta | ...el país o el idioma están mal |
| CPA alto con todo bien | CPM caro o AOV bajo | ...estás en un país con CPM 23 y ticket de 15 |

## El caso México dic-2026

| Decisión | Elección | Razón |
|---|---|---|
| País | México, nacional | Stock local, envío interno |
| Ciudades | Nacional, con exclusión de zonas sin cobertura de paquetería | Evitar pedidos que no puedes entregar |
| Edad | 18-65 en el test; acotar solo si los datos lo piden | Dejar que aprenda |
| Interés | Ninguno al arrancar | Amplio + 3-4 ángulos (`250`) |
| Idioma | Español de México, con modismos naturales | "Alacena", "chamba", "sale", no "vale" ni "coger" |

## Errores

1. **Apilar 20 intereses** creyendo que suma: el sistema los promedia y tú pagas más.
2. **Excluir demasiado** hasta dejar una audiencia de 40.000 personas: se satura en días.
3. **Creer que el lookalike reemplaza el creativo**: sin 100+ conversiones de base no vale nada.
4. **Testear audiencias antes que ángulos**: gastar el capital buscando 10% con 400% al lado (`247`).
5. **No poner el píxel el día 1**.

## Relacionados
`246` Advantage+ · `247` el creativo es la segmentación · `250` generar ángulos · `267` diagnóstico · `271` retargeting · `272` canal propio
