# 186 — Cosecha, secado y curado (donde se pierde la mitad del aroma sin que nadie lo mida)

El cultivo define el techo químico de la planta; la cosecha, el secado y el curado deciden cuánto de ese
techo llega al frasco. Es el único tramo del proceso donde **pierdes activos sin haber hecho nada**: los
terpenos se evaporan, el THCA se descarboxila y se oxida, y la humedad decide si tienes moho o si tienes
producto. Casi nadie lo mide, y por eso casi nadie sabe que perdió. Este módulo te da las condiciones, lo
que le pasa a cada familia química y cómo comprobarlo con análisis, no con olfato.

Términos:
- **humedad relativa, HR (relative humidity, RH)** = agua en el aire respecto a la saturación, en %.
- **actividad de agua, aw (water activity)** = agua *disponible* para microorganismos, escala 0–1; no es lo
  mismo que humedad total (ver `35`).
- **curado (curing)** = reposo controlado posterior al secado, en recipiente cerrado, que homogeniza la
  humedad y modifica el perfil de volátiles.
- **monoterpeno (monoterpene)** = terpeno de 10 carbonos, volátil y ligero (mirceno, limoneno, pineno).
- **sesquiterpeno (sesquiterpene)** = 15 carbonos, mucho menos volátil (β-cariofileno, humuleno).

## Qué le pasa a cada familia química mientras se seca

| Familia | Qué pasa | Impulsor principal | Consecuencia medible |
|---|---|---|---|
| Monoterpenos | Se evaporan | Temperatura y flujo de aire | Cae el terpeno total, cambia la relación mono/sesqui |
| Sesquiterpenos | Se quedan casi todos | — | Suben en proporción relativa |
| THCA | Se descarboxila lentamente | Temperatura y tiempo | Sube el Δ9-THC "libre" en el COA |
| Δ9-THC | Se oxida a CBN | Oxígeno, luz, calor | Sube el CBN (indicador de maltrato) |
| Clorofila y azúcares | Degradación enzimática | Tiempo, oscuridad, humedad | Menos aspereza al fumar; sin efecto en potencia |
| Hongos y bacterias | Crecen si aw es alta | aw > 0,65 aprox. | Reprueba microbiología (ver `203`) |

La clave química es que **el THC total se conserva mejor que el perfil de terpenos**. Por eso un secado
brutal puede dejarte un COA de potencia decente y un producto que huele a heno: el ensayo de potencia no ve
el daño. Lo ve el ensayo de terpenos (`199`).

## Condiciones de referencia

Estas son las condiciones que la práctica industrial usa como punto de partida. **No son ley**: dependen de
la densidad del cogollo, del cultivar y de tu sala. Ajusta con datos propios.

| Etapa | Temperatura | HR | Duración típica | Objetivo |
|---|---|---|---|---|
| Secado lento | 15–18 °C | 55–62 % | 7–14 días | Bajar humedad sin arrastrar volátiles |
| Secado "rápido" industrial | 20–24 °C | 45–55 % | 3–5 días | Volumen, a costa de monoterpenos |
| Curado | 18–20 °C | 58–62 % | 14–60 días | Homogeneizar y desarrollar aroma |
| Almacenamiento | ≤ 20 °C, oscuridad | 55–62 % | — | Frenar THC → CBN (ver `204`) |

Regla operativa: **el secado va lento y frío; el error se paga en aroma, no en potencia**. Los monoterpenos
empiezan a irse de forma apreciable por encima de ~21 °C, y por encima de 65 % HR el riesgo microbiológico
sube más rápido de lo que el aroma agradece.

Objetivo final de humedad: **10–12 % de humedad en la flor**, medido por pérdida por secado o Karl Fischer
(ver `98`), con `aw` en el rango 0,55–0,65. Por debajo de 55 % HR el material se vuelve quebradizo y pierde
terpenos; por encima de 65 % HR entras en zona de moho.

## La conversión de THCA que ocurre "sola"

La descarboxilación no necesita un horno: necesita tiempo y temperatura. A 20 °C la constante de velocidad
es minúscula, pero un curado de 60 días son 1,44 millones de segundos. Con los parámetros de Arrhenius del
módulo `174` (`Ea ≈ 85 kJ/mol`, `A ≈ 3,7 × 10⁸ s⁻¹`) puedes estimar cuánto THCA se convierte durante el
curado:

```bash
python lab-tools/decarboxilacion.py --temp-c 20 --minutos 86400   # 60 días
python lab-tools/decarboxilacion.py --temp-c 25 --minutos 86400
```

No hagas la cuenta de memoria: ejecútala. La lectura práctica es que en curado frío la conversión es de
unos pocos puntos porcentuales, pero en una bodega a 30 °C durante meses ya es visible en el COA, y viene
acompañada de CBN. Si tu producto es flor y compites por Δ9-THC declarado, esto te afecta el número; si
compites por THC total, no (ver `175`).

## Cómo se mide / cómo se comprueba

No creas en el olor ni en el "crujido del tallo" como control de proceso. Mide:

| Qué | Método | Unidad | Cuándo |
|---|---|---|---|
| Humedad | Pérdida por secado (105 °C) o Karl Fischer (`98`) | % p/p | Diario durante el secado |
| Actividad de agua | Higrómetro de punto de rocío (aw meter) | adimensional | Al cerrar el secado |
| Potencia (THCA, Δ9-THC, CBN) | HPLC-DAD, **nunca GC** (ver `173`, `198`) | % p/p base seca | Día 0, fin de secado, fin de curado |
| Perfil de terpenos | GC-MS o GC-FID headspace (ver `199`) | mg/g o % p/p | Día 0 y fin de curado |
| Microbiología y micotoxinas | Cultivo/qPCR y LC-MS/MS (ver `203`) | UFC/g y µg/kg | Liberación de lote |
| Metales pesados | ICP-MS (ver `202`) | µg/kg | Por lote de cultivo, no por secado |
| Solventes residuales | No aplica en flor seca (ver `201`) | — | — |

**Sin base seca no hay comparación posible.** Durante el secado pierdes 70–80 % del peso en agua, así que la
potencia "sube" sola. Si comparas el día 0 en base húmeda contra el día 12, estás midiendo evaporación, no
química. Corrige siempre con `lab-tools/base_seca.py` (ver `07`).

## Ejemplo aplicado (ILUSTRATIVO)

Lote de 40 kg de flor fresca, secado a 17 °C y 58 % HR durante 11 días, curado 21 días en recipiente
cerrado. Cifras **(ILUSTRATIVO)**, HPLC-DAD para cannabinoides y GC-MS headspace para terpenos, todo en
`% p/p base seca`:

| Punto | Humedad | THCA | Δ9-THC | CBN | THC total | Terpenos totales |
|---|---|---|---|---|---|---|
| Cosecha | 76 % | 22,1 | 0,4 | 0,02 | 19,79 | 2,45 |
| Fin de secado (día 11) | 11,5 % | 21,3 | 1,1 | 0,04 | 19,78 | 1,62 |
| Fin de curado (día 32) | 10,8 % | 20,6 | 1,6 | 0,07 | 19,67 | 1,48 |

Lectura: el **THC total prácticamente no se movió** (19,79 → 19,67, dentro de la incertidumbre del método,
ver `76`), pero los **terpenos cayeron 40 %** entre cosecha y producto final. Ese 40 % es el margen que se
juega tu producto en el mercado premium, y no aparece en el ensayo de potencia. Si tu comprador paga por
aroma, este es el número que tienes que defender, no el THC.

## Equipo modesto vs. maquila

| Actividad | Con equipo modesto | Exige maquila / servicio externo |
|---|---|---|
| Control de T y HR | Sí: deshumidificador, termohigrómetro con registro | — |
| Humedad de la flor | Sí: balanza de humedad (~USD 800–2.000) | Karl Fischer si necesitas exactitud de expediente |
| Actividad de agua | Medidor aw de mesa, inversión media | — |
| Potencia por HPLC | No | Sí — laboratorio con patrón certificado (`70`, `108`) |
| Terpenos por GC-MS | No | Sí — el ensayo que justifica el secado lento (`199`) |
| Microbiología y micotoxinas | No | Sí — laboratorio acreditado (`203`) |
| Metales pesados | No | Sí — ICP-MS (`202`) |

## Errores comunes

- **Secar rápido y caliente para rotar la sala.** Ganas días y pierdes el aroma, que es lo que diferencia el
  producto. El COA de potencia no te va a delatar; el cliente sí.
- **Usar el "test del tallo" como especificación.** No es medible, no es reproducible y no entra en un
  expediente técnico (`286`).
- **Comparar COAs de humedades distintas.** Sin base seca, dos lotes idénticos parecen diferentes (`07`).
- **Curar en frascos sin abrir ("burping") con humedad alta.** Es exactamente la receta del moho anaerobio.
- **Ignorar el CBN.** Es tu marcador de exceso de calor, luz y tiempo. Si sube lote a lote, tu bodega está
  cocinando el inventario (`204`).
- **Medir potencia por GC.** El GC descarboxila en el inyector y te borra la distinción THCA / Δ9-THC, que es
  justamente lo que quieres seguir durante el curado (`173`).
- **No registrar T y HR con datalogger.** Sin registro no hay causa raíz cuando un lote sale mal, y sin causa
  raíz no hay desviación cerrable (`169`).

## Conexión con otros módulos

→ `185-cultivo-y-perfil-quimico.md` — el techo químico que traes de la sala de cultivo.
→ `174-descarboxilacion-cinetica-y-calculo.md` — la matemática de la conversión THCA → THC.
→ `204-estabilidad-y-degradacion-del-thc.md` — qué le sigue pasando al producto en bodega.
→ `199-analisis-de-perfil-de-terpenos.md` — el ensayo que sí ve el daño del secado.
→ `98-karl-fischer-y-humedad.md` y `35-actividad-de-agua-y-humedad.md` — cómo se mide el agua de verdad.
→ `142-secado-y-conservacion-de-biomasa.md` — la versión general del secado para otras biomasas.
→ `203-micotoxinas-y-microbiologia-en-cannabis.md` — el riesgo del otro lado de la humedad.
