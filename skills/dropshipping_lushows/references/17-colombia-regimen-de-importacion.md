# Colombia: régimen de importación y courier

> Vigencia: septiembre 2026. Verifica en la DIAN antes de recomendar.

## El estado actual

| Concepto | Situación |
|---|---|
| **Umbral de minimis** | **US$200 FOB**, restaurado tras la **Sentencia C-079 de 2026**, que tumbó el Decreto 1474 de 2025 |
| **Sobre US$200** | IVA 19% + arancel único de courier (normalmente 10%) |
| **Bajo US$200, origen CON TLC** | Excluido de IVA; paga arancel courier |
| **Bajo US$200, origen SIN TLC (China)** | **Gravado con IVA 19%** + arancel courier |
| **Uso comercial** | Gravado aunque esté bajo el umbral |
| **Medidas especiales** | Decreto 0264 de 2026: 35% al acero de China, Rusia, India y Turquía |

La lectura práctica: **China no tiene TLC con Colombia**, así que un paquete chino para reventa paga
del orden de **19% de IVA + ~10% de arancel courier ≈ 29%** sobre el valor declarado.

## El impacto en el modelo

Producto de US$8 FOB + US$5,50 de flete = US$13,50 puesto.

```
Valor declarado                  13,50
IVA 19% + arancel courier 10%     3,92
Flete de última milla             2,80
Comisión de plataforma (5%)       1,50
                                ──────
Costo por pedido                 21,72
```

Con ticket de US$30 el margen bruto es **US$8,28**. Pero igual que en México, el problema real es el
**tránsito**: 12-22 días desde China por aire. Con contraentrega, eso hunde la tasa de entrega.

## Lo que hace único a Colombia

**Es el mercado de contraentrega más maduro de LatAm.** 52 millones de habitantes, ecommerce
creciendo por encima del 25% anual, y ~70% del ecommerce físico se paga al recibir.

**Tasas de entrega reales:**
- Con confirmación previa (WhatsApp o voz IA): **65-78%**
- Sin confirmación: **50-60%**
- Zonas urbanas con confirmación: **70-85%**

**Infraestructura:** cuatro transportadoras con recaudo integrado — Interrapidísimo (líder en
cobertura nacional), Servientrega (urbano premium), Coordinadora (urbano principal), Envía Colvanes
(cobertura rural amplia). Ver `154`.

**Stack estándar 2026:** Shopify + Dropi Colombia + formulario COD + confirmación por IA + pauta en
Meta/TikTok.

## El CPM más barato de la región

**US$4,00** de base, US$5,80 en Q4. CPC de US$0,42. Es el mercado hispanohablante donde el clic es
más barato, lo que lo convierte en el mejor **laboratorio de pruebas**: puedes validar un producto
con US$16-17 de inversión.

## La temporada colombiana

El evento de consumo es la **prima de servicios**: por ley, la segunda cuota se paga **antes del 20
de diciembre**. Equivale a 30 días de salario al año en dos cuotas. Con el salario mínimo en
$1.750.905 (alza del 23% decretada en dic-2025), la base de cálculo de un trabajador de mínimo parte
de ~$2.000.000.

Otras fechas: el **8 de diciembre** (Día de las Velitas) abre la Navidad colombiana. Ver `37`.

## Cuándo Colombia es la decisión correcta

- Capital chico y hay que **validar barato**: el CAC más bajo de todos los mercados comparados.
- El operador está en Colombia: conoce el modismo, la objeción local y puede recibir devoluciones.
- Producto de impulso con ticket de $80.000-$150.000 COP.
- Se puede usar catálogo local (Dropi) sin inmovilizar capital.

## Cuándo no

- Se quiere vender desde China directo: el tránsito mata el COD. Ver `31`.
- Se necesita ticket alto: el mercado colombiano aguanta menos que el mexicano o el español.
- Se necesita cobrar rápido: la liquidación de billetera es de 2-7 días hábiles **después** de la
  entrega efectiva, lo que da un ciclo de caja de ~12 días. Ver `32`.

## Errores frecuentes

| Error | Realidad |
|---|---|
| "Bajo US$200 no paga nada" | Solo si el origen tiene TLC y no es uso comercial |
| "El COD es plata fácil" | Sin confirmación previa entregas 52%: pierdes en cada venta |
| "Mando por Interrapidísimo y ya" | La transportadora importa menos que la confirmación |
| "Puedo vender lo mismo que en México" | El ticket que aguanta el mercado es menor |

## Relacionados
`13` mapa aduanero · `21` playbook Colombia · `129` proveedores en Colombia · `132` Dropi ·
`154` paqueterías de Colombia · `37` primas y aguinaldos · `159` subir la tasa de entrega
