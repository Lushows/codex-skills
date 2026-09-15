# Mapa aduanero 2026 (el módulo que hay que verificar siempre)

> **Vigencia: 14 de septiembre de 2026.** Este es el módulo que más rápido envejece de toda la skill.
> Antes de recomendar un país, **verifica en web** que el régimen siga igual. Un decreto puede
> cambiar el margen de un negocio entero de un día para otro.

## La tabla maestra

| Mercado | Umbral de minimis | Qué paga un paquete de origen chino | Desde | Fuente a verificar |
|---|---|---|---|---|
| 🇺🇸 **EE.UU.** | **Eliminado** | ~**54%** de arancel (30% vía courier comercial) | China may-2025 · resto ago-2025 · regulación 24-jun-2026 | CBP |
| 🇪🇺 **Unión Europea** | **Eliminado** (era €150) | **€3 fijos por línea** de declaración + IVA del país | 1-jul-2026 | Comisión Europea, DG TAXUD |
| 🇲🇽 **México** | Régimen simplificado | **33,5%** global (países sin TLC) | 1-ene-2026, sin caducidad | DOF, ANAM |
| 🇨🇴 **Colombia** | **US$200 FOB** (restaurado por Sentencia C-079 de 2026) | Bajo $200 de origen sin TLC: **IVA 19% + arancel courier ~10%** | Vigente | DIAN |
| 🇬🇧 **Reino Unido** | £135, **vigente hasta al menos 31-dic-2026** | Sin arancel bajo el umbral (por ahora); IVA sí | Retiro previsto hasta mar-2029 | HMRC |
| 🇧🇷 **Brasil** | Tributación sobre compras internacionales bajo US$50 | Impuesto de importación + ICMS | Vigente | Receita Federal |
| 🇨🇱 **Chile** | US$41 | IVA 19% + arancel | Vigente | Aduana de Chile |
| 🇵🇪 **Perú** | US$200 | IGV 18% + arancel | Vigente | SUNAT |

## Los tres tipos de régimen y por qué importa la diferencia

### Régimen proporcional (el peor para ti)
El impuesto es un porcentaje del valor. EE.UU. (54%), México (33,5%), Chile, Perú.

**Consecuencia:** el impuesto crece cuando sube tu costo. No puedes diluirlo. Si el producto te
cuesta $13,50 puesto, pagas $7,29 en México y $7,29 más por cada $13,50 adicionales.

### Régimen plano (el mejor para ti)
El impuesto es una cantidad fija por pedido o por línea. UE (€3 por línea).

**Consecuencia:** el impuesto **se diluye** cuando subes el ticket. Sobre €35 son 8,6%; sobre €70
son 4,3%. Por eso la UE castiga menos al que vende caro y bien. Es la razón técnica por la que España
salía con el múltiplo mínimo más bajo en el estudio comparativo.

### Régimen con umbral vivo
Todavía existe un valor bajo el cual no pagas arancel. Reino Unido (£135, por ahora), Colombia
(US$200 con condiciones), Perú (US$200).

**Consecuencia:** hay una ventana, pero es la que todos los gobiernos están cerrando. No construyas
un negocio que dependa de ella sin plan B.

## La regla operativa que se deriva de esto

```
Si el régimen es PROPORCIONAL y alto (>25%)
   → el envío directo desde China no es viable
   → necesitas stock local o proveedor local

Si el régimen es PLANO
   → el envío directo desde China es viable
   → y mejora cuanto más alto sea tu ticket

Si el régimen tiene UMBRAL VIVO
   → viable mientras dure; ten plan B documentado
```

## Cómo se calcula el costo puesto en destino

```
valor declarado = costo del producto + flete internacional
impuesto        = valor declarado × tasa   (proporcional)
                  o  cantidad fija         (plano)
costo puesto    = valor declarado + impuesto + manejo del courier
```

El **manejo del courier** (despacho, gestión aduanera) se olvida siempre y va de $2 a $8 por envío.
Ver `152` para el cálculo completo.

## Errores que salen caros

| Error | Realidad |
|---|---|
| "Declaro $5 y no pagan nada" | Fraude aduanero. Con el fin del de minimis hay control documental y consistencia exigida entre factura, valor y cobro. Ver `150` |
| "El courier se encarga" | Solo si contrataste DDP. En DDU el arancel lo cobran **a tu cliente en la puerta**, y ahí pierdes la venta. Ver `149` |
| "Es igual para todos los productos" | No: la fracción arancelaria cambia la tasa. Electrónica, textil y cosmético pagan distinto |
| "El de minimis de EE.UU. va a volver" | La suspensión es indefinida por regulación y hay derogación legal prevista para jul-2027 |
| "En la UE son solo €3, es barato" | €3 **por línea de declaración**, no por paquete. Un bundle de 3 productos distintos puede ser 3 líneas |

## Productos con régimen especial (verifica siempre)

Estos no siguen la tabla general y pueden requerir permisos, certificados o pagar tasas mucho más
altas:

- Cosmética y cuidado personal (registro sanitario en varios países)
- Suplementos y cualquier cosa ingerible
- Dispositivos médicos, incluso los de apariencia inocente
- Electrónica con batería de litio (restricción de transporte aéreo)
- Juguetes (certificaciones de seguridad)
- Textiles (cuotas y aranceles específicos)
- Cualquier cosa con marca registrada ajena

Ver `143`.

## Qué vigilar en los próximos meses

1. **Tasa de gestión de la UE** — propuesta para el **1-nov-2026**, en plena temporada. Si entra,
   recalcula España y toda Europa.
2. **Derogación legal en EE.UU.** — prevista jul-2027.
3. **Reino Unido** — consulta cerrada mar-2026; el umbral cae antes de mar-2029.
4. **Nuevas fracciones mexicanas** — ya hubo una ampliación en abr-2026; puede haber más.

## Relacionados
`14` EE.UU. · `15` Unión Europea · `16` México · `17` Colombia · `18` Sudamérica · `19` Reino Unido ·
`149` DDP y DDU · `150` declarar valor · `152` costo puesto en destino
