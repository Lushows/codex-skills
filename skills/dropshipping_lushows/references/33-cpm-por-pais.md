# CPM por país: la tabla y cómo leerla

> El CPM es el precio de que **mil personas vean** tu anuncio. No es el precio de una venta.
> Todo el mundo elige país mirando esta tabla y la mitad elige mal. Aquí está la tabla y aquí está
> por qué no basta.
>
> Datos: benchmarks Meta 2026, base en USD. Actualizado 14-sep-2026.

## Tabla de CPM y CPC 2026 (Meta, base USD)

| País | CPM base | CPM en Q4 (+20-50%) | CPM semana Black Friday (+50-80%) | CPC |
|---|---|---|---|---|
| **Estados Unidos** | **23,00** | 27,60 - 34,50 | 34,50 - 41,40 | **2,69** |
| Australia | 18,50 | 22,20 - 27,75 | 27,75 - 33,30 | — |
| Canadá | 13,40 | 16,08 - 20,10 | 20,10 - 24,12 | — |
| Reino Unido | 10,31 | 12,37 - 15,47 | 15,47 - 18,56 | — |
| Alemania | 10,05 | 12,06 - 15,08 | 15,08 - 18,09 | — |
| Francia | 8,05 | 9,66 - 12,08 | 12,08 - 14,49 | — |
| Italia | 7,20 | 8,64 - 10,80 | 10,80 - 12,96 | — |
| **España** | **5,80** | 6,96 - 8,70 | 8,70 - 10,44 | **0,85** |
| Polonia | 5,50 | 6,60 - 8,25 | 8,25 - 9,90 | — |
| Chile | 5,20 | 6,24 - 7,80 | 7,80 - 9,36 | 0,60 |
| **México** | **4,50** | **5,40 - 6,75** | 6,75 - 8,10 | **0,45** |
| Brasil | 4,20 | 5,04 - 6,30 | 6,30 - 7,56 | 0,35 |
| Colombia | 4,00 | 4,80 - 6,00 | 6,00 - 7,20 | 0,42 |
| Argentina | 3,80 | 4,56 - 5,70 | 5,70 - 6,84 | — |
| **Perú** | **3,70** | 4,44 - 5,55 | 5,55 - 6,66 | **0,36** |

**EE.UU. cuesta 6,2 veces lo que Perú.** Y aun así hay gente ganando en EE.UU. y perdiendo en Perú.

## El ciclo anual del CPM (referencia global)

| Momento | CPM mediano global | Lectura |
|---|---|---|
| Noviembre 2025 (pico) | **US$25,22** | El techo histórico del año |
| Enero 2026 | **US$15,74** | −38% respecto al pico |

El CPM **no sube porque Meta quiera**: sube porque en Q4 entran a la subasta todas las marcas con
presupuesto anual. En enero se van y el tráfico queda barato. Consecuencia práctica: **validar
producto en enero cuesta casi 40% menos que validarlo en noviembre**. Ver `38`.

## Por qué el CPM barato no gana solo

El CPM es el primer eslabón de cuatro. La cadena completa:

```
CAC real = CPM ÷ (1.000 × CTR × CVR × tasa_de_cobro)
```

| Eslabón | Lo que hace | Quién lo controla |
|---|---|---|
| CPM | Precio de la atención | El país y la temporada |
| CTR | Cuántos hacen clic | **Tu creativo** |
| CVR | Cuántos compran | **Tu página y tu oferta** |
| Tasa de cobro | Cuántos pagan de verdad | **Tu modelo: COD o prepago** (`30`) |

Un CPM de 3,70 con tasa de cobro del 50% es peor que uno de 4,50 con 97%. **El país barato con
COD malo te sale caro.** Ver `31`.

## El número que importa de verdad: CPM ÷ ticket

No compares países por CPM. Compáralos por **cuántas millésimas de tu ticket cuesta la atención**.

| Mercado | CPM base | Ticket típico que aguanta | CPM ÷ ticket ×100 |
|---|---|---|---|
| Estados Unidos | 23,00 | US$49,90 | **46,1** |
| España | 5,80 | US$43,00 | 13,5 |
| Chile | 5,20 | US$40,00 | 13,0 |
| **México (bundle)** | **4,50** | **US$60,05** | **7,5** |
| Colombia | 4,00 | US$30,00 | 13,3 |
| Perú | 3,70 | US$25,00 | 14,8 |

México gana **no por el CPM, sino por la relación**: tráfico barato con ticket que aguanta ser alto
gracias al bundle y a los meses sin intereses. Perú tiene el CPM más barato de la tabla y sale peor
que México, porque el ticket que el mercado paga es más bajo. Ver `34`, `218`.

## Cómo leer un CPM que no encaja con la tabla

| Lo que ves | Causa probable | Qué hacer |
|---|---|---|
| CPM 2-3x arriba de la base | Público diminuto, o creativo con CTR bajísimo | Ampliar público; cambiar creativo |
| CPM sube día a día sin cambiar nada | Fatiga creativa, o entraste a Q4 | Renovar creativo; recalcular techo de CAC |
| CPM bajísimo y cero ventas | Estás comprando atención de mala calidad (posiciones baratas, público frío irrelevante) | Mirar CPC y CVR, no CPM |
| CPM se dispara un día concreto | Evento comercial local o electoral | Consultar `35` |
| CPM bajo en Reels / alto en Feed | Normal. Reels es más barato y convierte distinto | Separar y medir por ubicación |

> **El CPM alto no siempre es malo.** Un público caro suele ser un público con dinero. El CPM es un
> insumo, la utilidad es el resultado.

## Cómo usar la tabla para presupuestar

Para saber cuántas ventas te da un presupuesto:

```
Ventas = (presupuesto ÷ CPM_del_periodo) × 1.000 × CTR × CVR × cobro
```

Ejemplo México, temporada, creativo bueno (CTR 2,2%, CVR 3,0%, cobro 97%):

```
US$300 ÷ 6,75  = 44,4 miles de impresiones
44,4 × 1.000 × 0,022 × 0,030 × 0,97  ≈  28 ventas cobradas
28 × US$20,18 de utilidad  ≈  US$565
```

Ese cálculo, con tus propios números y comparando países, está automatizado en `12`.

## Avisos de uso

1. **Estos son promedios de país, no de nicho.** Seguros, finanzas y salud pagan mucho más; entre­
   tenimiento y compras impulsivas, menos. Usa la tabla para elegir país, no para prometerle un
   número a nadie.
2. **El CPM de tu cuenta depende de tu historial.** Una cuenta nueva paga peor las primeras semanas.
3. **Verifica antes de una decisión grande.** Los benchmarks se mueven trimestre a trimestre; esta
   tabla es del 2026.
4. **TikTok y Google tienen otra estructura de costo.** Compara por CAC final, no por CPM entre
   plataformas distintas.

## La frontera

Cómo bajar el CPM (estructura de campañas, pujas, públicos, Advantage+, ubicaciones, fatiga
creativa) **no es de esta skill**: invoca `facebook_ads_lushows`, `tiktok_ads_lushows` o
`google_ads_lushows` según la plataforma. Aquí decidimos **en qué país y con qué producto** vale la
pena comprar esa atención.

## Relacionados
`10` cómo se elige un país · `11` el techo de CAC · `12` comparador de países · `34` poder
adquisitivo y ticket · `35` calendario comercial global Q4 · `38` estacionalidad · `226` ROAS de
equilibrio
