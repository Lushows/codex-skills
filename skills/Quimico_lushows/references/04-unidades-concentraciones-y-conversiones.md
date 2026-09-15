# 04 — Unidades, concentraciones y conversiones (para no perderte entre %, mg/g y ppm)

La mitad de los errores caros de este oficio no son de química: son de unidades. Alguien lee "2 ppm de
plomo" y cree que es mucho; otro lee "25 % de activo" y calcula mal cuántos miligramos quedan en la
cápsula; un tercero compara "mg/mL" con "mg/g" en un gotero y se equivoca por un factor cercano al de
la densidad. Este módulo te da las equivalencias exactas, las trampas típicas y la disciplina de
arrastrar la unidad y la base en cada paso. Regla del oficio: **un número sin unidad no se escribe; y
si es una masa relativa, tampoco se escribe sin base**.

Términos: **p/p (w/w, weight/weight)** = masa de analito por masa de muestra. **p/v (w/v)** = masa por
volumen. **v/v** = volumen por volumen. **ppm (parts per million)** = partes por millón; en sólidos
equivale a mg/kg. **molaridad (molarity, M)** = moles de soluto por litro de solución. **base (basis)**
= sobre qué masa se expresa el porcentaje (húmeda, seca, tal cual).

## Tabla maestra de equivalencias (masa en sólidos)

| Unidad | Equivale a | Ejemplo |
|---|---|---|
| 1 % p/p | 10 mg/g | 25 % p/p = 250 mg/g |
| 1 % p/p | 10.000 ppm (mg/kg) | 0,3 % p/p = 3.000 ppm |
| 1 ppm | 1 mg/kg = 1 µg/g | 2 ppm de Pb = 2 mg por kg de polvo |
| 1 ppb | 1 µg/kg = 1 ng/g | 10 ppb de aflatoxina = 10 µg/kg |
| 1 mg/g | 0,1 % p/p | 12 mg/g = 1,2 % |

En **líquidos**, ppm suele usarse como mg/L, que solo equivale a mg/kg si la densidad es 1,00 g/mL
(agua). Con etanol, aceite MCT o un extracto viscoso, **no lo es**: ahí hay que declarar si es p/p o
p/v. Es una de las trampas más comunes en goteros de cannabis.

## Las conversiones que vas a usar todos los días

```
mg de activo por unidad = masa de la unidad (mg) × (% p/p / 100)
   Ej.: cápsula de 500 mg de extracto al 25 % p/p  ->  500 × 0,25 = 125 mg de activo

% p/p a partir de mg/g:            % = (mg/g) / 10
ppm a partir de %:                 ppm = % × 10.000
mg por porción de N unidades:      mg_unidad × N
Concentración de una solución:     C (mg/mL) = masa (mg) / volumen (mL)
Dilución (C1V1 = C2V2):            V1 = (C2 × V2) / C1
Molaridad:                         M = gramos / (masa molar g/mol × litros)
```

Toda cuenta que sostenga una decisión se **ejecuta**, no se hace de memoria: `lab-tools/unidades.py`
y `lab-tools/diluciones.py`, o se rutea a `Matematicas_lushows`.

## Cómo se comprueba una conversión

Tres verificaciones que atrapan casi todo error:

1. **Análisis dimensional.** Escribe las unidades y cancélalas. Si te queda "mg·kg/g", te equivocaste.
2. **Orden de magnitud.** ¿El resultado es creíble? Una cápsula de 500 mg no puede contener 800 mg de
   activo. 2 ppm en una cápsula de 500 mg son 0,001 mg = 1 µg: cantidades minúsculas.
3. **Camino inverso.** Devuélvete desde el resultado a la entrada. Si no cierra, hay error.

## Concentraciones en líquidos: la trampa del gotero

| Forma de declarar | Qué significa | Riesgo |
|---|---|---|
| "10 % CBD" en aceite | Ambiguo: ¿p/p o p/v? | Diferencia real del orden del 5–10 % según densidad |
| "1000 mg por frasco de 30 mL" | Total, no concentración | El cliente no sabe cuánto hay por gota |
| "33,3 mg/mL" | Concentración clara | Correcto, y permite calcular la gota |
| "1,7 mg por gota" | Dosis por unidad de uso | Depende del gotero; hay que verificarlo pesando |

Una gota no es una unidad de medida legal: su volumen depende de la viscosidad, la temperatura y el
gotero. Si vas a etiquetar por gota, tienes que **pesar 20 gotas** y calcular la masa media, y aun así
declarar mg/mL como referencia principal (ver `156`).

## Ejemplo aplicado (BIO-SETA)

Quieres etiquetar "aporta 200 mg de β-glucanos por porción" en un frasco de cápsulas.

Datos **(ILUSTRATIVO)**: extracto con β-glucano 24,6 % p/p base seca (Megazyme K-YBGL); cápsula
cargada con 450 mg de extracto; porción = 2 cápsulas.

```
Por cápsula:  450 mg × 0,246            = 110,7 mg de β-glucano
Por porción:  110,7 × 2                 = 221,4 mg de β-glucano
```

221,4 mg supera los 200 mg declarados, con margen del 10,7 %. Ese margen no es un lujo: es lo que te
protege de la variabilidad entre lotes y de la incertidumbre del método (ver `05`, `76`). Ahora la
pregunta correcta: ¿ese 24,6 % es el promedio de cuántos lotes? Con un solo lote no se fija una
especificación (ver `282`).

Y el mismo cálculo para un contaminante: si el límite de plomo es 2 ppm en el polvo y tu porción son
900 mg de extracto, la exposición por porción es `0,9 g × 2 µg/g = 1,8 µg de Pb`. Ese número, y no el
ppm, es el que se compara contra un límite de exposición diaria (ver `135`).

## Unidades que confunden y hay que traducir siempre

- **UI (unidades internacionales)** — solo existen para sustancias con actividad biológica definida
  (vitaminas A, D, E). No hay UI de β-glucanos ni de cannabinoides; si alguien las usa, es invento.
- **"Ratio 10:1"** — es masa de material de partida por masa de extracto, no potencia (ver `151`, `242`).
- **"Equivalente a X mg de planta"** — depende del ratio declarado; sin el ratio no significa nada.
- **%RSD** — desviación estándar relativa, mide dispersión, no cantidad (ver `05`).
- **mg/kg de peso corporal** — unidad de toxicología y de dosis animal; nunca es la dosis del producto.

## Errores comunes

- **Mezclar p/p con p/v** en un líquido y errar por el factor de densidad.
- **Confundir ppm con %**: un factor de 10.000. Reportar 0,3 ppm cuando era 0,3 % es una diferencia
  entre "trazas" e "ilegal".
- **Calcular mg por cápsula sobre el peso total de la cápsula** (incluyendo la cubierta y excipientes)
  en vez de sobre el extracto cargado.
- **Sumar porcentajes de bases distintas.** Un 20 % base seca y un 15 % base húmeda no se suman.
- **Declarar por gota** sin haber pesado las gotas.
- **Redondear antes de terminar la cadena de cálculo**, y perder por el camino lo que después reclamas
  como margen (ver `05`).

## Conexión con otros módulos

→ `05-cifras-significativas-e-incertidumbre.md` — cuántos decimales tienes derecho a escribir.
→ `06-estequiometria-y-balance-de-masa.md` — cuando la conversión implica una reacción.
→ `07-base-seca-vs-humeda.md` — la base, que va pegada a todo porcentaje.
→ `73-lod-loq-y-rango-lineal.md` — el piso por debajo del cual la unidad ya no significa nada.
→ `161-dosis-y-tamano-de-porcion.md` — de mg/g a la porción que ve el cliente.
→ `175-thc-total-y-el-factor-0877.md` — la conversión más consecuencial del cannabis.