# 35 — Actividad de agua y humedad (el número que decide si tu polvo dura un año o tres meses)

Humedad y actividad de agua no son lo mismo, y confundirlas cuesta lotes enteros. La humedad dice **cuánta**
agua hay; la actividad de agua dice cuánta de esa agua está **disponible** para que crezcan hongos y
bacterias, para que se apelmace el polvo y para que se degraden tus activos. Dos polvos de melena de león
con 7 % de humedad pueden tener vida útil muy distinta según su aw. Es el parámetro más barato de medir
—un equipo de mesa, cinco minutos— y el que más gente omite en su especificación de producto terminado.

Términos: **humedad (moisture content)** = masa de agua sobre masa total, en % p/p. **actividad de agua
(water activity, aw)** = presión de vapor de agua del producto dividida por la del agua pura a la misma
temperatura; escala 0–1, adimensional. **humedad relativa de equilibrio (equilibrium relative humidity,
ERH)** = aw × 100, en %. **isoterma de sorción (sorption isotherm)** = curva de humedad vs aw a temperatura
constante. **higroscópico (hygroscopic)** = que absorbe humedad del aire. **temperatura de transición
vítrea (glass transition temperature, Tg)** = temperatura a la que un sólido amorfo pasa de vidrio rígido a
gomoso; por debajo, el polvo se comporta; por encima, se apelmaza.

## El mapa de aw: quién crece y qué pasa

| aw | Qué ocurre | Ejemplo de producto |
|---|---|---|
| > 0,95 | Crecen bacterias Gram negativas, casi todo | Bebidas, decocciones frescas |
| 0,90–0,95 | Crecen la mayoría de bacterias | Extractos líquidos sin conservar |
| 0,86–0,90 | *Staphylococcus aureus* puede crecer y producir toxina | Zona a evitar siempre |
| 0,80–0,86 | Mayoría de levaduras y mohos | Frutas secas, gomas mal formuladas |
| 0,70–0,80 | Mohos xerófilos; **producción de micotoxinas** por *Aspergillus* | Biomasa mal secada (`101`, `244`) |
| 0,60–0,70 | Límite inferior de crecimiento microbiano conocido | Frontera de seguridad |
| 0,40–0,60 | Sin crecimiento; reacciones químicas y enzimáticas activas | Zona de trabajo típica de polvos |
| 0,20–0,40 | **Mínimo de degradación global**; máxima estabilidad | Objetivo para polvo de hongos |
| < 0,20 | Vuelve a subir la oxidación de lípidos (agua monocapa removida) | Sobresecado, contraproducente |

Ese último renglón sorprende a mucha gente: **secar de más también daña**. La capa monomolecular de agua
protege contra la oxidación; al quitarla, el oxígeno accede directo a los sitios reactivos y la oxidación
de lípidos se acelera (`24`, `53`). La curva de estabilidad global tiene forma de U con el mínimo entre
aw 0,2 y 0,4.

## Humedad vs actividad de agua: por qué no son intercambiables

```
Dos polvos, misma humedad, distinta aw (ILUSTRATIVO):

Polvo A — cuerpo fructífero molido, 7,0 % humedad, aw 0,38
Polvo B — extracto con maltodextrina, 7,0 % humedad, aw 0,61

La maltodextrina liga menos el agua a esa concentración: hay más agua "libre".
El polvo B está en zona de riesgo de mohos xerófilos y se apelmazará antes.
La humedad no lo detectó. La aw sí.
```

La relación entre las dos la da la **isoterma de sorción**, y esa isoterma es propia de **cada material**.
Por eso no se puede convertir humedad en aw con una tabla general: se levanta la isoterma del producto
propio, una vez, y sirve para siempre (mientras no cambie la fórmula).

## Cómo se mide

| Qué | Método | Unidad / detalle |
|---|---|---|
| Humedad total | Pérdida por secado en estufa, 105 °C hasta peso constante | % p/p; método simple, incluye volátiles que no son agua |
| Humedad, método de referencia | Karl Fischer (volumétrico o culombimétrico) | % p/p; **específico para agua** (`98`) |
| Humedad rápida en planta | Balanza halógena (termobalanza) | % p/p; se calibra contra Karl Fischer |
| Actividad de agua | Higrómetro de punto de rocío enfriado o de sensor capacitivo | aw adimensional, **con temperatura**: aw 0,42 a 25,0 °C |
| Isoterma de sorción | DVS (sorción dinámica de vapor) o método de sales saturadas | % humedad vs aw, a T fija |
| Tg del polvo | DSC (calorimetría diferencial de barrido) | °C (`99`) |
| Apelmazamiento | Índice de Carr, ángulo de reposo tras condiciones de estrés | % ; grados (`143`) |

Regla dura y muy práctica: **la aw depende de la temperatura**, así que un aw sin temperatura no es un
dato. Y el equipo de aw se verifica cada día con estándares de sales saturadas (por ejemplo, cloruro de
litio, cloruro de magnesio, cloruro de sodio), igual que se calibra un pHmetro (`22`).

Nota importante para tus cálculos: la humedad es la que convierte base húmeda en **base seca**, y todo dato
de potencia sin base seca es incomparable entre lotes (`07`, `04`). El mismo dato de humedad sirve para
dos cosas distintas: corregir la potencia y predecir la estabilidad.

## Ejemplo aplicado — polvo de melena de león: fijar la especificación de aw

Cuerpo fructífero deshidratado y molido a malla 80, almacenado en bolsa con barrera y desecante, 25 °C /
60 % HR **(ILUSTRATIVO)**:

```
aw inicial   Humedad   Recuento de mohos    Apelmazamiento    β-glucano (mg/g b.s.)    Veredicto a 12 meses
             (% p/p)   a 12 m (UFC/g)       a 12 m            0 m → 12 m
   0,68        11,2      1,2 × 10⁴          Bloque duro         268 → 241              Rechazado
   0,55         8,9      3,0 × 10²          Grumos              268 → 258              Marginal
   0,42         6,4      < 10               Fluye bien          268 → 266              Aprobado
   0,31         5,1      < 10               Fluye bien          268 → 265              Aprobado
   0,15         3,2      < 10               Fluye, muy polvoso  268 → 262              Aprobado, pero
                                                                                        índice de peróxidos
                                                                                        más alto (`24`)

β-glucano por K-YBGL (`221`) · mohos por método de recuento en placa (`100`)
```

Especificación que se deriva del experimento: **aw ≤ 0,45 a 25 °C, humedad 4–7 % p/p (Karl Fischer)**, con
control en cada lote y verificación en el estudio de estabilidad. Nótese que el β-glucano casi no se movió
en ningún caso —es un polímero robusto— así que el criterio no lo puso la potencia: lo pusieron la
microbiología y el flujo del polvo. Esa es la lección: la aw se especifica por el modo de falla real del
producto, no por costumbre (`164`, `247`, `282`).

## Envase: la aw se mantiene o se pierde ahí

De nada sirve secar a aw 0,35 si el envase deja pasar humedad. Lo que hay que verificar:

- **WVTR (water vapor transmission rate)** del material, en g/(m²·día) a condiciones declaradas.
- **Sello** real de la máquina (prueba de burbuja o de tinte), no el sello teórico.
- **Desecante** dimensionado: gramos de silica gel según el área del envase, el WVTR y la vida útil
  objetivo — se calcula, no se estima a ojo (`Matematicas_lushows`).
- Verificación: medir aw del producto **a los 0, 3, 6 y 12 meses en el envase real**, no en bolsa de
  laboratorio (`163`, `164`).

## Errores comunes

- Confundir humedad con actividad de agua y especificar solo una. Hacen falta las dos.
- Reportar aw sin temperatura, o sin verificar el equipo con sales patrón ese día.
- Usar estufa a 105 °C en materiales con volátiles (terpenos, alcoholes) y llamar "humedad" a esa pérdida.
  Ahí toca Karl Fischer (`98`).
- Sobresecar "por seguridad". Por debajo de aw 0,2 la oxidación de lípidos repunta.
- Hacer el estudio de estabilidad en un envase distinto al comercial. El resultado no aplica.
- No corregir la potencia a base seca antes de comparar lotes. Es el error de comparación #1 (`07`).
- Suponer que porque el producto "está seco al tacto" está por debajo de aw 0,6. Al tacto no se mide nada.
- Empacar caliente. El producto libera humedad al enfriar dentro del envase y sube la aw local.

## Conexión con otros módulos

→ `07-base-seca-vs-humeda.md` — cómo se corrige la potencia por humedad.
→ `98-karl-fischer-y-humedad.md` — el método de referencia para agua.
→ `164-estabilidad-ich-q1-y-vida-util.md` — el módulo dueño de la vida útil.
→ `142-secado-y-conservacion-de-biomasa.md` — cómo se llega a esa aw.
→ `240-secado-y-perdida-de-activos.md` — qué se pierde en el camino, en hongos.
→ `244-micotoxinas-y-contaminacion-en-hongos.md` — el riesgo que la aw controla.
→ `143-molienda-y-granulometria.md` — apelmazamiento y flujo de polvos.
→ `163-envase-primario-y-compatibilidad.md` — WVTR y desecante.
