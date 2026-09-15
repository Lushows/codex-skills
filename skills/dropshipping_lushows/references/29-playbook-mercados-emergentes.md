# Playbook de mercados emergentes

> India, Filipinas, Indonesia, Sudáfrica, Emiratos Árabes y Polonia.
> Vigencia de los datos regulatorios: 14-sep-2026. Los umbrales aduaneros de estos seis países
> cambian sin aviso y con poca cobertura en prensa: **verificar antes de mover plata**.

## La promesa y la trampa

La promesa es real: CPM de uno a cinco dólares, poblaciones enormes, competencia publicitaria
menor que en Occidente. La trampa también: **el CPM barato no es utilidad barata**. El costo de
adquirir a alguien que *paga* depende de tres cosas — CPM, conversión y tasa de cobro — y en estos
mercados las dos últimas se desploman.

```
CAC real = CPM ÷ (1.000 × CTR × CVR × tasa_de_cobro)
```

Un CPM de US$1,20 con tasa de cobro del 55% te deja peor que México a US$4,50 con 97%. Corre `12`
antes de emocionarte.

## Tabla de decisión rápida

| Mercado | CPM aprox. (verificar) | Ticket que aguanta | Pago dominante | Dificultad logística | ¿Entrar con capital chico? |
|---|---|---|---|---|---|
| **India** | US$0,50-1,50 | US$8-25 | COD | Muy alta (RTO brutal) | **No** |
| **Filipinas** | US$1,00-2,50 | US$10-30 | COD / GCash | Alta (archipiélago) | Solo Metro Manila |
| **Indonesia** | US$1,00-2,50 | US$10-30 | Transferencia / COD | Alta | **No** (de minimis casi cero) |
| **Sudáfrica** | US$2,00-4,50 | US$25-70 | Tarjeta / EFT | Media | Tal vez, con socio local |
| **Emiratos (EAU)** | US$6,00-12,00 | **US$60-180** | Tarjeta / COD | **Baja** | Sí, si tienes producto premium |
| **Polonia** | **US$5,50** (dato firme) | US$30-70 | BLIK / lockers | **Baja** | Sí |

**Emiratos y Polonia no son "mercados emergentes pobres"**: son mercados de ticket alto con CPM
todavía razonable. Los otros cuatro son mercados de volumen con fricción de cobro.

## País por país

### India — el cementerio de dropshippers extranjeros

| Factor | Realidad |
|---|---|
| Pago | COD domina; según categoría, 40-60% de los pedidos |
| RTO (devolución al origen) | **25-40%** en COD sin confirmación. Es el número que mata |
| Ticket | Bajísimo. El consumidor compara y espera ₹499-1.999 |
| Importar | Régimen de courier restrictivo para envíos B2C; se espera registro y cumplimiento local |
| Vender como extranjero | Requiere estructura local (GST, entidad). **Invoca `contador_lushows`** |

**Veredicto:** solo si vives allá o tienes socio operativo. Un extranjero sin presencia física
pierde por RTO antes de entender qué pasó. Ver `31`.

### Filipinas — el mercado COD más manejable de Asia

- Inglés funcional en publicidad: **reutilizas creativo en inglés** sin traducir. Eso vale plata.
- COD aceptadísimo culturalmente; GCash y Maya crecen rápido y **suben la tasa de cobro** si logras
  empujar al prepago con descuento.
- Geografía: 7.000+ islas. Metro Manila, Cebú y Davao son manejables; fuera de ahí el flete y los
  días de tránsito destruyen el COD.
- Táctica: **geocercar a las tres áreas metropolitanas** y no salir de ahí hasta tener margen.

### Indonesia — el umbral que lo mata todo

El de minimis indonesio es de aproximadamente **US$3 por envío** (verificar vigencia). En la
práctica: **todo paga impuesto**. Sumado a las restricciones sobre venta directa en redes sociales
de los últimos años, es el mercado más hostil de la lista para un operador externo.

Solo tiene sentido con **stock local e importación por lote formal**, que es un negocio distinto
al que enseña esta skill. Ver `39`.

### Sudáfrica — el más "occidental" de los africanos

| Factor | Nota |
|---|---|
| Pago | Tarjeta y EFT instantáneo dominan; COD es marginal → **tasa de cobro alta** |
| Ticket | Aguanta US$25-70 en Gauteng y Western Cape |
| Aduana | De minimis bajo (orden de ZAR 500) y **régimen endurecido para textiles**: verificar |
| Riesgo | Volatilidad del rand: tu margen en USD se mueve solo |

Es un mercado de prepago con CPM medio. Si tu producto es no-textil y de ticket medio, es más
sensato que India o Indonesia.

### Emiratos Árabes — ticket alto, logística de primer mundo

- Poder adquisitivo alto y **tolerancia a precio premium**: el mismo producto que en México va a
  1.099 MXN aquí va a AED 199-299 sin resistencia.
- Entrega en 24-48 h dentro de Dubái y Abu Dabi. El COD funciona aquí **porque es rápido** — que es
  exactamente el punto de `31`.
- Contra: CPM más caro, mercado chico (≈10 M personas), y publicidad sujeta a normas de contenido
  más estrictas. Revisa políticas antes de producir creativo.

### Polonia — la puerta barata a la Unión Europea

| Factor | Dato |
|---|---|
| CPM | **US$5,50** — de los más baratos de la UE, contra 10,05 en Alemania |
| Aduana | Régimen UE: **€150 eliminado el 1-jul-2026**, ahora €3 por línea de declaración. Ver `15` |
| Entrega | Lockers (paczkomaty) con densidad enorme: entrega barata y sin fallo de "no estaba en casa" |
| Pago | BLIK es el método local dominante; sin BLIK pierdes conversión |
| Idioma | Obligatorio traducir. El inglés no vende en Polonia |

**Polonia es el mejor experimento europeo para capital chico**: costo de tráfico de mercado
emergente con infraestructura de mercado desarrollado. Ver `26`.

## Las tres preguntas antes de entrar a cualquiera

1. **¿Cuál es la tasa de cobro real?** No la del blog: pide el dato a un operador local o a la
   plataforma de COD. Si no lo consigues, asume el peor caso de `159`.
2. **¿Puedo cobrar sin ser residente?** Pasarela, cuenta bancaria y factura. Si la respuesta es
   "con una empresa local", ya no es un test barato. **Invoca `contador_lushows`**.
3. **¿El ticket que aguanta el mercado cubre mi flete?** Método en `34`. Un flete de US$5 sobre un
   ticket de US$12 no deja negocio por mucho que el CPM sea de un dólar.

## Comparación honesta contra el mercado del proyecto

| | México (proyecto activo) | Mejor emergente (Polonia) | Emergente de volumen (Filipinas) |
|---|---|---|---|
| CPM base | US$4,50 | US$5,50 | ~US$1,50 (verificar) |
| Ticket objetivo | US$60,05 | US$35-60 | US$15-25 |
| Tasa de cobro | 97% prepago | ~95% prepago | 55-75% COD |
| Calendario Q4 | **55 días seguidos** | Navidad | Doble-doble (11.11, 12.12) |
| Complejidad de entrada | Baja | Media (idioma, BLIK, IVA UE) | Media-alta |

**Para el proyecto de diciembre 2026 la respuesta es no**: ninguno de estos seis compite con
México cuando tienes menos de US$500, ~5 tests disponibles y una ventana comercial que ya empezó a
contar. Los emergentes son la **segunda tienda**, no la primera. Ver `39`.

## Cuándo sí valen la pena

- Cuando ya tienes un ganador validado y el creativo está amortizado (`39`).
- Cuando tu producto es **estacionalmente inverso** al mercado principal — Sudáfrica tiene verano en
  diciembre. Ver `38`.
- Cuando tu margen unitario en USD es tan alto que aguanta una tasa de cobro del 60%.

## Cuándo no, sin discusión

- Si es tu primer país.
- Si dependes de COD **y** proveedor lejano al mismo tiempo. Ver `31`.
- Si no puedes leer los anuncios de la competencia en el idioma local.
- Si tu capital total es menor a US$1.000: el costo de aprender el mercado se come los tests.

## Relacionados
`12` comparador de países · `26` playbook Unión Europea · `31` COD y China son incompatibles ·
`34` poder adquisitivo y ticket · `39` expandir de un país a otro · `159` tasas de entrega
