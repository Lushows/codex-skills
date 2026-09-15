# 135 — NOAEL, IDA y límites de exposición (cómo se decide cuánto es demasiado)

Este módulo enseña la cadena que convierte un experimento en animales en un número que aparece en una norma:
NOAEL → factores de incertidumbre → IDA/TDI → límite máximo en el alimento. Entender esa cadena te permite
leer un límite regulatorio sin fe ciega, calcular si tu producto aporta una fracción relevante de la
ingesta tolerable, y responder a un cliente que pregunta "¿pero eso es peligroso?" con un número en vez de
una opinión. El error caro que evita: cumplir un límite legal y aun así aportar una fracción alta de la
ingesta tolerable semanal del consumidor, sin haberlo notado.

Términos: **IDA / ADI (acceptable daily intake)** = cantidad que se puede ingerir a diario toda la vida sin
riesgo apreciable; se usa para aditivos y residuos intencionales. **TDI (tolerable daily intake)** = lo
mismo para contaminantes no intencionales. **PTWI (provisional tolerable weekly intake)** = versión semanal
para contaminantes que se acumulan. **PTMI (provisional tolerable monthly intake)** = versión mensual, para
los de acumulación muy lenta. **Factor de incertidumbre (uncertainty factor, UF)** = divisor de seguridad
aplicado al NOAEL.

## La cadena completa

```
Estudio toxicológico (OECD 408, 90 días)
        │
        ▼
NOAEL o BMDL   (mg/kg pc/día)
        │  ÷ factores de incertidumbre
        ▼
IDA / TDI      (mg/kg pc/día)
        │  × peso corporal de referencia (60 o 70 kg según la agencia)
        ▼
Ingesta tolerable por persona (mg/día)
        │  ÷ consumo estimado del alimento (kg/día)
        ▼
Límite máximo en el alimento (mg/kg)
```

Factores de incertidumbre estándar:

| Factor | Valor por defecto | Por qué |
|---|---|---|
| Extrapolación entre especies (animal → humano) | 10 | El humano podría ser más sensible |
| Variabilidad entre individuos | 10 | Niños, ancianos, polimorfismos |
| **Producto habitual** | **100** | El clásico "factor 100" |
| Uso de LOAEL en vez de NOAEL | ×3 a ×10 adicional | Se partió de una dosis que ya causaba efecto |
| Duración insuficiente (subcrónico → crónico) | ×2 a ×10 adicional | El estudio no cubre la vida entera |
| Datos incompletos | ×2 a ×10 adicional | Falta un endpoint clave |

Nota clave: **BMDL está reemplazando a NOAEL** como punto de partida en las evaluaciones modernas (EFSA lo
usa sistemáticamente), porque el NOAEL depende de qué dosis se eligieron ensayar, mientras que el BMDL sale
de modelar toda la curva dosis-respuesta.

## Cuando no hay umbral: el MOE

Para sustancias genotóxicas y carcinogénicas no se asume umbral seguro, así que no se fija IDA. En su lugar
se usa el **margen de exposición (margin of exposure, MOE)**:

```
MOE  =  BMDL10  /  Exposición estimada
```

Regla de interpretación usada por EFSA: un **MOE ≥ 10.000** para un carcinógeno genotóxico se considera de
baja preocupación desde salud pública. Es el marco que se aplica, por ejemplo, a contaminantes de proceso.

## Valores de referencia para metales pesados (a agosto de 2026)

Esta tabla es de las más útiles del bloque y también de las más malinterpretadas, porque **JECFA y EFSA no
dicen lo mismo** y algunos valores fueron retirados:

| Metal | JECFA | EFSA | Comentario crítico |
|---|---|---|---|
| Cadmio | **PTMI 25 µg/kg pc/mes** (73ª reunión, 2011; reemplazó al PTWI de 7 µg/kg pc) | **TWI 2,5 µg/kg pc/semana** (CONTAM, 2009), basado en efectos renales | EFSA es más estricta: 2,5/semana ≈ 10,7/mes vs 25/mes de JECFA |
| Plomo | **PTWI de 25 µg/kg pc RETIRADO** (2010): no se pudo establecer un nivel sin efecto | Sin umbral seguro; se usan BMDL y MOE | **No existe una "ingesta tolerable de plomo"**. Quien cite un PTWI de plomo está usando un valor derogado |
| Arsénico inorgánico | **PTWI de 15 µg/kg pc RETIRADO** (2010) por no ser suficientemente protector | Se maneja con BMDL y MOE | Igual que el plomo: el valor viejo circula todavía en fichas comerciales |
| Mercurio inorgánico | PTWI 4 µg/kg pc | TWI 4 µg/kg pc | Coinciden |
| Metilmercurio | PTWI 1,6 µg/kg pc | **TWI 1,3 µg/kg pc** | EFSA algo más estricta |

Verificar siempre la vigencia antes de usarlos en un expediente: estas evaluaciones se revisan y la fecha
de este módulo es agosto de 2026.

## Cómo se comprueba en tu producto

El cálculo que hay que saber hacer, y que casi nadie hace, es **cuánta fracción de la ingesta tolerable
aporta tu porción diaria**:

```
Aporte diario (µg) = concentración en producto (mg/kg) × porción diaria (kg) × 1.000
Fracción del TWI   = (Aporte diario × 7) / (TWI × peso corporal)
```

Ese porcentaje es el número honesto. Cumplir el límite legal del alimento y aportar el 40 % del TWI
semanal de una persona son dos hechos compatibles y muy distintos.

## Ejemplo aplicado — cadmio en un extracto de hongo

Supuesto **(ILUSTRATIVO)**: extracto de reishi con cadmio 0,30 mg/kg por ICP-MS (`88`); porción diaria de
1,5 g; persona de 70 kg; se usa el TWI de EFSA de 2,5 µg/kg pc/semana.

```
Aporte diario  = 0,30 mg/kg × 0,0015 kg × 1.000 = 0,45 µg/día
Aporte semanal = 0,45 × 7 = 3,15 µg/semana
TWI de la persona = 2,5 × 70 = 175 µg/semana
Fracción = 3,15 / 175 = 1,8 % del TWI
```

Lectura: el aporte del suplemento es pequeño **por sí solo**. Pero el TWI se llena con la dieta completa
(cereales, hortalizas, mariscos), así que el suplemento se suma a una base que ya existe. Por eso la
pregunta correcta no es "¿cumplo el límite?" sino "¿cuánto contribuyo al total?".

Y el matiz que decide un lanzamiento: si el extracto es 10:1, el cadmio se concentra junto con todo lo
demás. Un cuerpo fructífero conforme puede dar un extracto no conforme (ver `136`, `151`).

**Ejecutar estos cálculos en código** con `lab-tools/unidades.py` o `Matematicas_lushows`. Un error de
factor 1.000 entre mg y µg aquí es un error regulatorio.

## Errores comunes

- Citar el PTWI de plomo o de arsénico inorgánico. Ambos fueron retirados; usarlos es citar norma muerta.
- Mezclar JECFA y EFSA sin decir cuál se está usando. Dan números distintos para cadmio.
- Comparar un TWI (semanal) con un aporte diario sin convertir. Error de factor 7.
- Aplicar el límite del alimento fresco a un extracto concentrado. El factor de concentración cambia todo.
- Olvidar el peso corporal: el límite es por kg de persona, y un niño tiene mucho menos margen.
- Cumplir el límite legal y creer que la conversación terminó, sin calcular la fracción del TWI.

## Conexión con otros módulos

→ `134-toxicologia-basica-dosis-y-riesgo.md` — de dónde sale el NOAEL.
→ `136-toxicidad-de-metales-pesados.md` — los metales, uno por uno.
→ `88-icp-ms-y-metales-pesados.md` — cómo se mide.
→ `151-relacion-planta-extracto-y-ratios.md` — por qué concentrar concentra también los contaminantes.
→ `282-especificacion-de-producto-terminado.md` — cómo se fija el límite propio.
