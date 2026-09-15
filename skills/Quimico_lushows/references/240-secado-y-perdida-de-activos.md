# 240 — Secado de hongos y pérdida de activos (dónde se te va la plata sin que lo veas)

El secado es el primer paso donde un lote bueno se vuelve mediocre. Un cuerpo fructífero (fruiting body)
fresco tiene 85–92 % de agua; si lo secás mal, no solo pierdes agua: pierdes compuestos termolábiles,
oxidas triterpenos y polifenoles, y a veces bajas el contenido de beta-glucano medible por daño estructural.
El problema comercial es que nadie lo nota, porque casi nadie mide antes y después. Este módulo te enseña a
tratar el secado como un proceso con parámetros y con datos, no como "poner los hongos al sol".

Términos: **base seca (dry basis)** = el resultado expresado sobre material sin agua. **actividad de agua
(water activity, aw)** = agua disponible para microorganismos, no cantidad total de agua. **termolábil
(heat-labile)** = se degrada con calor. **liofilización (freeze-drying)** = secado por sublimación al vacío.

## Qué se pierde y por qué

| Familia de compuestos | Sensibilidad principal | Qué pasa al secar mal |
|---|---|---|
| Beta-glucanos (β-glucans) | Calor extremo y quemado | Estructura polimérica robusta; se pierden poco hasta ~120 °C, pero el pardeamiento los "enmascara" |
| Triterpenos ganodéricos | Oxidación y luz | Bajan por oxidación prolongada al aire y a la luz |
| Ergotioneína | Oxidación (es un antioxidante) | Se consume oxidándose ella misma |
| Hericenonas / erinacinas | Calor y oxígeno | Familia lipofílica y frágil; poco documentada su cinética real |
| Vitamina D2 (si hubo UV) | Luz UV y oxígeno | Sigue formándose o degradándose según la exposición |
| Nucleósidos (adenosina, cordicepina) | Calor húmedo prolongado | Hidrólisis y pérdida progresiva |

Regla honesta: la **cinética exacta de pérdida por especie y por método casi nunca está publicada**. Lo que
sí puedes hacer es medirla en TU proceso (abajo). Cualquiera que te dé un porcentaje exacto de pérdida sin
haberlo medido en tu lote, te está vendiendo humo.

## Métodos de secado comparados

| Método | Temperatura típica | Tiempo | Costo relativo | Riesgo principal |
|---|---|---|---|---|
| Sol directo | 25–40 °C, UV alto | 1–3 días | Muy bajo | Contaminación, oxidación, humedad residual alta, lluvia |
| Aire forzado / horno de bandejas | 40–60 °C | 8–24 h | Bajo | Sobrecalentar el final del ciclo |
| Deshidratador con control | 45–55 °C | 6–12 h | Medio | Ninguno grave si se controla |
| Liofilización | −40 °C, vacío | 24–48 h | Alto | Costo; textura muy higroscópica después |

Para la mayoría de hongos funcionales, **aire forzado a 45–55 °C hasta humedad ≤ 8 %** es el equilibrio
razonable entre costo, tiempo y conservación. La liofilización preserva mejor los termolábiles y el color,
pero su costo por kilo rara vez se justifica en un suplemento que después se va a extraer con agua caliente.

## Cómo se mide / cómo se comprueba

Se mide el proceso con tres variables y se mide el resultado con tres análisis.

Del proceso: temperatura real del producto (no la del aire), tiempo total y humedad final.

Del resultado, siempre comparando **base seca contra base seca**:

```
Corrección a base seca:
  Valor_base_seca = Valor_medido / (1 − Humedad_fracción)

Ejemplo (ILUSTRATIVO):
  β-glucano medido = 24,0 % p/p en material con 8,0 % de humedad
  Valor_base_seca = 24,0 / (1 − 0,080) = 26,1 % p/p base seca
Verificar con lab-tools/base_seca.py — nunca a mano.
```

| Qué medir | Método | Unidad |
|---|---|---|
| Humedad | Karl Fischer o pérdida por secado 105 °C hasta peso constante | % p/p |
| Actividad de agua | Higrómetro de punto de rocío | aw (adimensional), objetivo ≤ 0,60 |
| Beta-glucano | Megazyme K-YBGL (enzimático) | % p/p base seca |
| Triterpenos totales | HPLC-DAD contra ácido ganodérico A | mg/g base seca |
| Ergotioneína | HPLC-UV o LC-MS/MS | mg/g base seca |

**El diseño del experimento que sí sirve:** parte un lote fresco homogeneizado en tres subunidades, sécalas
por tres rutas distintas, y analiza las tres el mismo día en el mismo laboratorio. Sin ese control, la
diferencia que veas puede ser del laboratorio, no del secado (`287-diseno-de-experimentos-doe.md`).

## Ejemplo aplicado (ILUSTRATIVO)

Lote de melena de león (Hericium erinaceus), 40 kg fresco.

```
Fresco:        40,00 kg, humedad 90,0 %  →  materia seca = 4,00 kg
Secado A (55 °C, 10 h):  humedad final 7,5 %  →  4,32 kg de producto seco
Rendimiento de secado = 4,32 / 40,00 = 10,8 % p/p

β-glucano (Megazyme), base seca:
  Secado A (55 °C):        28,4 % p/p b.s.
  Secado B (75 °C, 5 h):   27,9 % p/p b.s.   → diferencia dentro de la incertidumbre del método
  Secado C (sol, 3 días):  26,1 % p/p b.s.   → más baja Y con recuento microbiano más alto
```

Lectura: en β-glucano el calor moderado no fue el problema; el sol sí, y además metió riesgo
microbiológico. Si el producto se vende por triterpenos u ergotioneína, la conclusión podría ser distinta:
por eso el activo que se mide tiene que ser el que sostiene la etiqueta.

## Errores comunes

- **Medir en base húmeda y comparar con un COA en base seca.** Dos lotes con 6 % y 12 % de humedad no se
  comparan directo; la diferencia aparente puede ser puro agua (`07-base-seca-vs-humeda.md`).
- **Confiar en la temperatura del aire.** El producto húmedo se mantiene frío por evaporación y luego, al
  final del ciclo, se dispara. El daño casi siempre ocurre en la última hora.
- **Secar hasta "que suene seco".** Sin medir humedad ni aw no sabes si quedaste en 12 % (moho asegurado en
  bodega) o en 3 % (frágil, se pulveriza, se oxida más rápido).
- **Secar al sol en clima húmedo colombiano.** En la sabana y en zonas cafeteras la humedad relativa
  nocturna revierte el secado y multiplica el riesgo de hongos contaminantes y micotoxinas (`244`).
- **No guardar contramuestra del fresco.** Sin contramuestra congelada no puedes demostrar después qué
  perdiste en el secado.
- **Asumir que liofilizar siempre es mejor.** Preserva más, pero deja un polvo muy higroscópico que exige
  mejor envase; si tu producto se extrae en agua caliente después, gastaste plata en nada.

## Conexión con otros módulos

→ `07-base-seca-vs-humeda.md` — la corrección que hace comparables dos lotes.
→ `142-secado-y-conservacion-de-biomasa.md` — el proceso general para biomasa vegetal y fúngica.
→ `241-extraccion-de-hongos-agua-vs-alcohol.md` — qué pasa después del secado.
→ `244-micotoxinas-y-contaminacion-en-hongos.md` — el riesgo del secado lento o al aire libre.
→ `35-actividad-de-agua-y-humedad.md` — por qué aw manda más que humedad total.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el método que valida si perdiste activo o no.
