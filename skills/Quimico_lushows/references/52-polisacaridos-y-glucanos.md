# 52 — Polisacáridos y glucanos (el módulo que desarma el fraude del micelio en grano)

Este es, probablemente, el módulo más rentable de toda la skill. Todos los glucanos están hechos de la misma
pieza —glucosa— y sin embargo hay tres familias completamente distintas: el **β-(1→3),(1→6)-glucano del
hongo**, el **β-(1→3),(1→4)-glucano del cereal** y el **α-glucano, que es almidón**. Se distinguen solo por
cómo están unidos los ladrillos. Esa diferencia invisible es la que separa un extracto de hongo real de un
saco de arroz molido vendido como suplemento. Si entiendes esta página, puedes desmontar el 80 % del fraude
del mercado de hongos funcionales con una sola pregunta al proveedor.

Términos: **polisacárido (polysaccharide)** = polímero de azúcares. **Enlace glicosídico (glycosidic bond)**
= el enlace que une dos azúcares; se nombra por los carbonos que une y por el anómero (α o β).
**Anómero (anomer)** = configuración del carbono 1 del azúcar; α o β. **Grado de ramificación (degree of
branching, DB)** = cuántas ramas por unidades de cadena principal. **Peso molecular (molecular weight, Mw)**
= tamaño del polímero, en Da o kDa; en polímeros siempre es una distribución, no un número.

## Las tres familias, lado a lado

| | β-glucano fúngico | β-glucano de cereal | α-glucano (almidón/glucógeno) |
|---|---|---|---|
| Enlaces | **β-(1→3)** cadena principal + **β-(1→6)** ramas | **β-(1→3),(1→4)** mixto, **lineal** | **α-(1→4)** + ramas **α-(1→6)** |
| Anómero | β | β | **α** |
| Forma en solución | Triple hélice (algunos) o hélice simple | Cadena flexible, viscosa | Hélice/gránulo |
| Fuente | Hongos, levaduras | Avena, cebada | Arroz, maíz, trigo, papa |
| Digestión humana | No digerible por amilasas | No digerible (fibra soluble) | **Sí, es alimento**: amilasa lo corta |
| Reconocimiento inmune | Descrito para receptor Dectin-1 y CR3 [in vitro/animal] (`130`) | No por Dectin-1 | No |
| Kit Megazyme | **K-YBGL** | **K-BGLU** (lichenasa) | Se mide como α-glucano en K-YBGL |
| Valor en tu producto | Es el marcador de "hongo real" | Otra categoría | **Es el relleno del fraude** |

**Regla de oro:** *"β-glucano" a secas no significa nada. Hay que decir el patrón de enlace y la fuente:*
`β-(1→3),(1→6)-D-glucano de cuerpo fructífero de Ganoderma lucidum` (`41`).

## Por qué la diferencia importa biológicamente

El receptor **Dectin-1** de las células inmunes reconoce estructuras β-(1→3) con ramificaciones β-(1→6) de
cierto tamaño; los β-glucanos de cereal (mixtos 1→3/1→4, lineales) y el almidón (α) **no** presentan esa
estructura. Esto está descrito en literatura [in vitro / animal] (`130`). Nivel de evidencia honesto: hay
mecanismo, hay datos preclínicos, y hay ensayos clínicos de calidad heterogénea; **no** hay base para
afirmar en etiqueta que un producto "fortalece el sistema inmune" en Colombia bajo el Decreto 3249 de 2006
sin el respaldo y el registro correspondientes (`267`, `268`).

Adicionalmente, la actividad reportada depende de **Mw, grado de ramificación y conformación (triple hélice)**.
Dos productos con el mismo "% de β-glucano" pueden ser materialmente distintos. Por eso una especificación
seria incluye —además del %— el rango de Mw si el claim depende de él (`247`).

## La estructura, dibujada

```
β-glucano fúngico (esquema; cada G = glucosa):

   G—β(1→3)—G—β(1→3)—G—β(1→3)—G—β(1→3)—G—β(1→3)—G      ← cadena principal β-(1→3)
                     |β(1→6)              |β(1→6)
                     G                    G—β(1→3)—G     ← ramas β-(1→6)

β-glucano de cereal (avena/cebada): LINEAL, sin ramas
   G—β(1→4)—G—β(1→4)—G—β(1→3)—G—β(1→4)—G—β(1→4)—G—β(1→3)—G

Almidón (amilopectina): TODO alfa
   G—α(1→4)—G—α(1→4)—G—α(1→4)—G
                     |α(1→6)
                     G—α(1→4)—G
```

Otros polisacáridos que aparecen en la misma matriz y hay que saber nombrar:

- **Quitina**: polímero de *N*-acetilglucosamina β-(1→4). Es la pared celular fúngica; aporta nitrógeno y
  por eso el factor de conversión de proteína en hongos es 4,38 y no 6,25 (`48`).
- **Mananos y galactomananos**: presentes en paredes fúngicas; cuentan como "polisacáridos" y no son
  β-glucano.
- **Heteropolisacáridos con proteína** (proteoglicanos): PSK y PSP de cola de pavo son complejos
  polisacárido-proteína, no β-glucano puro (`231`).

## Cómo se mide — y por qué "polisacáridos totales" es una trampa

| Método | Qué mide | ¿Distingue α de β? | Veredicto |
|---|---|---|---|
| **Fenol-sulfúrico** ("polisacáridos totales") | Todos los azúcares tras hidrólisis | **No** | Inútil para el claim; mide el almidón como si fuera activo |
| Antrona | Igual | No | Igual |
| **Megazyme K-YBGL** | Glucano total, α-glucano, β por diferencia | **Sí** | **El estándar del sector** |
| Megazyme K-BGLU | β-glucano mixto de cereal (lichenasa) | Es otro analito | Solo para avena/cebada. Usarlo en hongo es un error |
| Metilación + GC-MS (linkage analysis) | Patrón exacto de enlaces | Sí, en detalle | Confirmatorio; caro |
| RMN ¹³C / ¹H | Anómeros α/β y tipo de enlace | Sí | Confirmatorio |
| SEC-MALS | Distribución de Mw | No aplica | Complementa el % |

```
Principio del K-YBGL (yeast & mushroom beta-glucan), en cristiano:
  A) GLUCANO TOTAL: hidrólisis con H₂SO₄ concentrado (~12 M, frío) y luego diluido (~1,3 M, 100 °C)
     → todo el glucano se rompe a glucosa → se mide glucosa con GOPOD (glucosa oxidasa/peroxidasa).
  B) α-GLUCANO: digestión con amiloglucosidasa + invertasa (solo cortan α)
     → glucosa liberada = α-glucano (almidón, glucógeno) + sacarosa libre.
  C) β-GLUCANO = GLUCANO TOTAL − α-GLUCANO

  Unidad de reporte: % p/p BASE SECA. Sin la humedad, el número no es comparable (`07`).
```

Ese "por diferencia" es la clave del oficio: **el método te entrega gratis el dato del fraude**. Si el
α-glucano es alto, hay almidón; si hay almidón en un producto que dice ser "extracto de cuerpo fructífero",
alguien está vendiendo el sustrato (`218`, `220`).

## Ejemplo aplicado — dos COA del mismo "reishi"

```
COA A (ILUSTRATIVO)                        COA B (ILUSTRATIVO)
  Polisacáridos totales: 35,0 %              Glucano total:  31,8 % p/p base seca
  β-glucano: no reportado                    α-glucano:       3,4 % p/p base seca
  α-glucano: no reportado                    β-glucano:      28,4 % p/p base seca
  Humedad: no reportada                      Humedad (KF):    5,2 %
  Método: "colorimétrico"                    Método: Megazyme K-YBGL, lab acreditado ISO 17025
  Parte: "reishi"                            Parte: cuerpo fructífero; ITS confirmó G. lucidum

Diagnóstico:
  · COA A no permite saber si esos 35 % son almidón de arroz. Es un número sin significado (`222`).
  · COA B es auditable: dice método, base, α, β, humedad, parte y especie.
Señal de alarma universal: α-glucano alto (indicativo de sustrato) + β-glucano bajo + "polisacáridos" alto.
Con micelio crecido en grano, es común encontrar α-glucano muy por encima del β-glucano (`218`).
```

## Errores comunes

- Aceptar "polisacáridos ≥ 30 %" como sinónimo de β-glucano. Es el fraude, no un descuido.
- Usar el kit de cereal (K-BGLU) en una muestra de hongo: mide un analito que en hongo prácticamente no
  existe, y da valores absurdamente bajos que confunden a todo el mundo.
- Reportar β-glucano sin humedad, o en base húmeda: no comparable entre lotes ni proveedores (`07`).
- Creer que un β-glucano alto por sí solo prueba que es cuerpo fructífero. Las levaduras también tienen
  β-(1→3),(1→6). Hay que cerrar identidad con **ITS** (`245`) y coherencia con otros marcadores (`60`).
- Comprar por % de β-glucano sin mirar Mw ni conformación cuando el claim depende de la estructura.
- Confundir "fibra dietaria" con β-glucano: la fibra incluye quitina, celulosa y todo lo no digerible.
- Extrapolar de un lote. La especificación necesita varios lotes y un rango (`282`).

## Las tres preguntas que desarman a cualquier proveedor

1. *¿Cuál es el **α-glucano** de este lote, en % p/p base seca, por Megazyme K-YBGL?*
2. *¿La materia prima es **cuerpo fructífero** o micelio, y sobre qué sustrato creció?* (`217`, `239`)
3. *¿Me envía el **informe del laboratorio** —no la ficha comercial— con lote, fecha y acreditación?* (`110`)

Si no contesta las tres por escrito, la decisión ya está tomada.

## Conexión con otros módulos

→ `219-beta-glucanos-quimica-y-estructura.md` — el módulo dueño del detalle estructural en hongos.
→ `220-alfa-glucanos-y-almidon-el-confusor.md` — el confusor, en detalle.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el método paso a paso.
→ `222-polisacaridos-totales-por-que-no-sirve.md` — la demolición del método inespecífico.
→ `218-el-fraude-del-micelio-en-grano.md` — el caso comercial completo.
→ `130-inmunomodulacion-y-beta-glucanos.md` — qué dice la evidencia, con niveles marcados.