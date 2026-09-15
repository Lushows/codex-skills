# Plataformas COD de LatAm

> Vigencia: septiembre 2026. Verifica cobertura, comisiones y transportadoras en cada plataforma.

Las plataformas COD son la infraestructura que hace posible el ecommerce en países con baja
bancarización y baja confianza en el pago en línea. Resuelven tres cosas a la vez: **catálogo con
stock local, integración con transportadoras, y recaudo del efectivo**.

Sin ellas, vender contraentrega en LatAm exige contratos propios con transportadoras, conciliación
manual de recaudos y capital de inventario. Con ellas, arrancas hoy sin plata.

## El panorama

| Plataforma | Cobertura | Perfil |
|---|---|---|
| **Dropi** | 12 países: CO, MX, EC, PE, CL, ES, AR, PA, PY, VE, GT, CR | **El líder.** Catálogo + logística + billetera. Ver `132` |
| **Mastershop** | LatAm | Competidor directo, catálogo y logística propia |
| **Aliddy** | México | Enfoque mexicano |
| Plataformas locales menores | Por país | Aparecen y desaparecen. Verifica antigüedad |

Además existe la vía sin plataforma: contrato directo con transportadora + proveedor mayorista. Mejor
margen, mucho más trabajo operativo. Ver `128`, `129`.

## Qué resuelve cada capa (y qué no)

| Capa | Lo resuelve la plataforma | Sigue siendo tuyo |
|---|---|---|
| Catálogo con stock local | Sí | Elegir el producto correcto |
| Contrato con transportadora | Sí | Elegir cuál usar por zona |
| Generación de guías | Sí | Confirmar dirección |
| Recaudo del efectivo | Sí | El desfase de caja |
| Conciliación | Sí | Verificar que cuadre |
| Gestión de novedades | Da la herramienta | **Gestionarlas tú, a diario** |
| Calidad del producto | **No** | Tuya. Pide muestra |
| Tasa de entrega | **No** | Tuya: confirmación, oferta, producto |
| Servicio al cliente | No | Tuyo |

## Cómo comparar plataformas: las 12 preguntas

1. ¿Cuál es la **comisión** y sobre qué base (precio de venta o costo)?
2. ¿Cuál es el **plazo de liquidación** tras entrega efectiva, en días hábiles?
3. ¿Qué **transportadoras** integra y cuáles cubren mis ciudades objetivo?
4. ¿Cuál es el **flete** por rango de peso y por zona?
5. ¿Quién paga el **flete de la devolución**?
6. ¿Qué pasa si el producto llega dañado? ¿Quién repone?
7. ¿El **stock del catálogo es en tiempo real**?
8. ¿Puedo **pedir muestra** a mi casa fácilmente?
9. ¿Puedo meter **inserto o empaque propio**?
10. ¿Tiene **integración** con Shopify/Woo, o solo carga manual/CSV?
11. ¿Puedo usarla en **prepago**, o solo COD?
12. ¿Puedo subir **mi propio inventario** a su bodega (modelo híbrido)? Ver `136`.

Las preguntas 5, 9, 11 y 12 son las que casi nadie hace y las que más definen si podrás escalar.

## La economía del COD: los tres números que mandan

```
1. TASA DE ENTREGA EFECTIVA    (entregados / despachados)
2. FLETE REAL POR ENTREGA      (incluye el flete de las devoluciones)
3. DÍAS DE CICLO DE CAJA       (venta → plata en tu banco)
```

Rangos observados en operaciones COD de LatAm (verifica los tuyos, varían mucho):

| Escenario | Tasa de entrega orientativa |
|---|---|
| Sin confirmación, producto de impulso, ticket alto | Baja |
| Con confirmación por WhatsApp | Notablemente mayor |
| Con stock local y entrega en 2-4 días | Mayor aún |
| Con tránsito desde China de 10-20 días | **Se derrumba** |

**La confirmación por WhatsApp antes de despachar es la palanca más barata y más potente del COD.**
Cuesta un mensaje y mueve la entrega en dos dígitos. Para el guion de confirmación invoca
`ventas_lushows`.

## El ciclo de caja: lo que quiebra operaciones rentables

```
Día 0   Pagas la pauta y vendes
Día 1   Se despacha
Día 3-6 Se entrega (o no)
Día 5-13 Liquidación a tu banco (2-7 días hábiles tras entrega)

Desfase real: 5-15 días entre pagar la pauta y recibir la plata.
```

Si escalas la pauta 3× de un día para otro, necesitas financiar 3× ese desfase con caja propia. Es la
razón por la que operaciones con margen positivo se quedan sin plata escalando. Ver `138`.

**Prepago rompe este problema.** Cobras al momento, la pasarela liquida en días, y no pagas flete de
devoluciones fantasma. Por eso, cuando el mercado lo tolera, prepago gana. Ver `30`.

## Cuándo la plataforma deja de convenir

| Señal | Qué hacer |
|---|---|
| Vendes 300+ unidades/mes del mismo SKU | Compra el lote y usa 3PL. Ver `134`, `137` |
| La comisión mensual supera lo que costaría tu propia bodega | Calcula el punto de cruce |
| El proveedor se queda sin stock recurrentemente | Compra tú el inventario |
| Quieres empaque y marca propios | La plataforma limita. Ver `125`, `126` |
| Necesitas mejor precio para bajar el CAC objetivo | Solo el lote propio te lo da |

El punto de cruce típico: cuando el ahorro mensual de comprar directo supera el costo fijo del 3PL más
el costo financiero del inventario. Invoca `Matematicas_lushows` para calcularlo con tus números.

## Riesgos de depender de una plataforma

| Riesgo | Mitigación |
|---|---|
| Cambian la comisión | Ten modelado el escenario con comisión mayor |
| Suspenden tu cuenta | Ten cuenta en una segunda plataforma, aunque sea inactiva |
| El proveedor del catálogo desaparece | Producto B siempre. Ver `144` |
| Retraso en la liquidación | No comprometas pauta contra plata que no está en tu banco |
| Tus datos de cliente viven en su sistema | Exporta tus clientes periódicamente. Es tu activo |

El último punto es el más subestimado: **la base de clientes es lo único que se acumula.** Si toda tu
relación con el cliente vive dentro de la plataforma, no estás construyendo marca. Ver `127`.

## Errores frecuentes

| Error | Realidad |
|---|---|
| Creer que la plataforma garantiza calidad | El proveedor es un tercero |
| No gestionar novedades | Es la tarea más rentable del COD |
| Modelar sin flete de devolución | El flete real es 40-80% mayor que el nominal |
| Escalar pauta sin financiar el desfase de caja | Rentable en papel, quebrado en banco |
| Quedarse en la plataforma para siempre | Techo de margen bajo. Ver `136` |
| No exportar la base de clientes | Regalas el único activo acumulable |

## Para el proyecto activo (México, diciembre 2026)

Dropi MX en modalidad **prepago** es la configuración correcta: obtienes el stock local (que resuelve
el 33,5% y el tiempo de tránsito, ver `16`) sin heredar el problema de caja ni las devoluciones del
COD.

Ten cuenta abierta también en una segunda plataforma mexicana aunque no la uses. Diciembre es el mes
de los quiebres de stock y de las suspensiones por volumen inusual: la redundancia cuesta cero y
salva la campaña.

## Relacionados
Ver `128`, `129`, `132`, `134`, `136`, `137`, `138`, `144`, `30`, `16`, `20`.
