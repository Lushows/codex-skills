# 219 — Beta-glucanos: química y estructura (qué es el activo del que todos hablan)

"Beta-glucanos" es la palabra que sostiene todo el mercado de hongos funcionales, y casi nadie que la usa
sabe qué es. Es una familia de polímeros de glucosa, no una molécula única: el β-glucano de la avena, el de
la levadura y el del reishi son químicamente distintos y no se comportan igual. Entender la estructura te
permite tres cosas prácticas: saber qué método los mide, saber por qué el almidón se confunde con ellos, y
saber por qué no puedes copiar la evidencia de un β-glucano a otro.

Términos: **glucano (glucan)** = polímero de glucosa. **enlace glucosídico (glycosidic bond)** = unión entre
azúcares; su configuración α o β define la familia. **β-(1→3)** = enlace beta entre el carbono 1 de una
glucosa y el 3 de la siguiente. **ramificación (branching)** = cadena lateral, en hongos típicamente
β-(1→6). **grado de ramificación (degree of branching, DB)** = ramas por unidad de cadena principal.
**peso molecular (molecular weight, MW)** = tamaño del polímero.

## α o β: una diferencia de geometría con consecuencias enormes

La glucosa cierra su anillo y el hidroxilo del carbono 1 queda "abajo" (α) o "arriba" (β). Ese detalle
estereoquímico define todo:

| | α-glucano | β-glucano |
|---|---|---|
| Ejemplos | Almidón, glucógeno | Celulosa (β-1,4), β-glucano fúngico (β-1,3/1,6) |
| Geometría de la cadena | Helicoidal, compacta | Extendida, rígida (β-1,3 forma triple hélice) |
| Enzimas humanas que lo digieren | Amilasas: sí | No hay β-1,3-glucanasa humana |
| Rol | Reserva de energía | Estructura de pared celular |
| Reconocimiento inmune innato | No relevante | Sí, vía Dectin-1 y otros `[in vitro]` |

Por eso el almidón es alimento y el β-glucano fúngico es fibra que llega intacta al intestino. Y por eso
medirlos juntos como "polisacáridos" no informa nada (ver `222`).

## Los β-glucanos no son todos iguales

| Origen | Estructura dominante | Nota |
|---|---|---|
| Hongos (basidiomicetos) | β-(1→3) con ramas β-(1→6) | Es el que interesa en reishi, melena, cola de pavo |
| Levadura *Saccharomyces* | β-(1→3) con ramas β-(1→6), muy ramificado | Base de muchos suplementos "beta-glucan 1,3/1,6" |
| Avena y cebada | β-(1→3),(1→4) mixto, soluble | Otro mundo: relacionado con colesterol, evidencia y claims propios |
| Bacterias (curdlano) | β-(1→3) lineal | Uso alimentario como gelificante |

**Consecuencia dura:** la evidencia clínica del β-glucano de avena no se puede usar para tu reishi, ni la de
la levadura, ni la de un β-glucano de otra especie fúngica. Cada preparación es su propio ingrediente
(ver `248`, `293`).

## Ejemplos con nombre propio en hongos

- **Lentinano (lentinan)**, de *Lentinula edodes*: esqueleto β-(1→3) con ramas β-(1→6) (ver `233`).
- **Grifolano / fracción D y MD (D-fraction, MD-fraction)**, de *Grifola frondosa* (ver `232`).
- **PSK (krestin) y PSP**, de *Trametes versicolor*: β-glucanos **unidos a proteína**; el PSK se describe con
  cadena principal β-(1→4) y ramas β-(1→3) y β-(1→6) (ver `231`).
- **Pleurano**, de *Pleurotus ostreatus*.

Que estén "unidos a proteína" no es un detalle menor: cambia la solubilidad, el método de extracción y
cómo se cuantifica.

## Lo que determina la actividad biológica (y lo que no sabemos)

Los factores que la literatura asocia a actividad inmunomoduladora `[in vitro]` `[animal]`:

- Configuración β-(1→3) en la cadena principal.
- Presencia y grado de ramificación β-(1→6).
- Peso molecular y capacidad de formar triple hélice.
- Solubilidad: la fracción soluble en agua se comporta distinto a la insoluble.
- Pureza: proteínas y pigmentos acompañantes pueden aportar o interferir.

Lo honesto: el **porcentaje de β-glucano no predice la actividad**. Dos extractos con 30 % pueden diferir en
peso molecular y solubilidad. El porcentaje es un control de identidad y de que compraste hongo, no una
medida de eficacia. Quien te venda "30 % = más potente" está simplificando de más.

## Cómo se mide / cómo se comprueba

| Qué quieres | Método | Unidad | Comentario |
|---|---|---|---|
| Contenido de β-glucano | Megazyme K-YBGL (enzimático, por diferencia) | `% p/p base seca` | Estándar de la industria (ver `221`) |
| Distinguir de almidón | El mismo kit: α-glucano aparte | `% p/p base seca` | Es la clave del asunto (ver `220`) |
| Tipo de enlace | RMN de ¹³C y ¹H; FTIR como apoyo | Cualitativo/semicuant. | Confirma β-(1→3)/(1→6) (ver `94`, `92`) |
| Peso molecular | SEC-MALS (cromatografía de exclusión) | `kDa` | Poco frecuente en rutina comercial |
| Triple hélice | Dicroísmo circular, rojo Congo | Cualitativo | Investigación, no rutina |
| Solo β-1,3/1,6 sin α | Kits enzimáticos específicos | `% p/p base seca` | Alternativa; verifica la validación |

## Ejemplo aplicado — traducir el porcentaje a la etiqueta

**(ILUSTRATIVO)** Extracto de reishi con β-glucano 28,4 % p/p base seca; cápsula de 500 mg de extracto;
porción diaria de 2 cápsulas.

```
por capsula: 500 mg x 0,284 = 142 mg de beta-glucano
por porcion: 142 x 2        = 284 mg de beta-glucano/dia
```

Ese cálculo va a código, siempre (`lab-tools/betaglucano_dosis.py` o `Matematicas_lushows`), y en la
etiqueta se declara con el método: "β-glucanos 284 mg por porción (Megazyme K-YBGL, base seca)".

Lo que **no** puede decir esa etiqueta: que los β-glucanos "estimulan las defensas para prevenir
enfermedades". La inmunomodulación descrita es mayormente `[in vitro]` y `[animal]`; convertirla en promesa
de prevención es un claim de enfermedad (ver `130`, `267`, `268`).

## Errores comunes

- Tratar "β-glucano" como si fuera una molécula única y comparar avena con reishi.
- Reportar β-glucano sin base: en base húmeda el número baja con la humedad del día (ver `07`).
- Suponer que más porcentaje = más eficacia. No está demostrado así.
- Aceptar un porcentaje calculado "por diferencia con todo lo demás" en vez de medido enzimáticamente.
- Extrapolar dosis de un ensayo clínico hecho con lentinano inyectable a un polvo oral. No es el mismo
  producto ni la misma vía (ver `123`).

## Conexión con otros módulos

→ `52-polisacaridos-y-glucanos.md` — la química general de polisacáridos.
→ `220-alfa-glucanos-y-almidon-el-confusor.md` — el otro lado de la moneda.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el ensayo, paso a paso.
→ `130-inmunomodulacion-y-beta-glucanos.md` — qué dice la farmacología, con nivel de evidencia.
→ `231-cola-de-pavo-trametes-psk-y-psp.md` — el caso de β-glucanos unidos a proteína.