# 192 — Destilación de cannabinoides (de crudo a distillate del 85–95 %)

El **distillate** es el commodity central de la industria del cannabis: un aceite dorado, casi transparente,
con 85–95 % de cannabinoides, sin sabor ni olor, que alimenta cartuchos, comestibles y tópicos. Se llega ahí
por **destilación molecular de película raspada (wiped film)** o por **short path**, que es lo mismo a menor
escala. La idea es contraintuitiva: el THC hierve alrededor de 155–180 °C a vacío profundo, cuando a presión
atmosférica se degradaría mucho antes. Todo el arte está en el vacío y en el tiempo de residencia. Este
módulo te da los parámetros publicados, cómo se opera y qué análisis exige el producto.

Términos:
- **destilación molecular / de trayecto corto (molecular / short path distillation)** = destilar a vacío tan
  profundo que la molécula viaja del evaporador al condensador casi sin chocar con nada.
- **película raspada (wiped film, WFE)** = un rotor esparce el aceite en una capa delgadísima sobre la pared
  caliente; el calor entra rápido y el tiempo de exposición es mínimo.
- **tiempo de residencia (residence time)** = cuánto tiempo el aceite está caliente. En wiped film es de
  **1–3 minutos**; en un balón de destilación clásico, horas.
- **micrones / mTorr** = unidad de vacío; 1.000 micrones = 1 Torr ≈ 1,33 mbar.
- **corte (cut / pass)** = cada pasada del aceite por el equipo; cada una separa una fracción distinta.

## Los dos (o tres) cortes

```
Aceite winterizado y descarboxilado
   ↓  PASO 1 — corte de ligeros: terpenos, agua, restos de solvente
Cola de ligeros (se guarda o se descarta)
   ↓  PASO 2 — corte principal: los cannabinoides destilan
DISTILLATE (85–95 % de cannabinoides)
   ↓  residuo pesado: clorofila, ceras que quedaron, sales, material no volátil
Residuo (se descarta o se reprocesa)
```

Muchas plantas hacen un tercer paso para subir pureza. Cada pasada mejora el color y la potencia y **cuesta
rendimiento**, así que hay un punto de retorno decreciente que se determina, no se supone.

## Parámetros publicados

De la literatura, para anclar (no como receta):

| Parámetro | Valor reportado | Fuente |
|---|---|---|
| Temperatura del evaporador (corte principal) | 185 °C (columna); pared interna típica 145 °C | *Industrial Crops and Products* (2023), optimización de wiped-film por RSM |
| Temperatura de condensación interna | 75 °C | Mismo trabajo |
| Recuperación de THC en el destilado | **93,4 %** en condiciones optimizadas | Mismo trabajo |
| Presión de trabajo | 0,001–0,01 mbar (película raspada); 300–600 mTorr en otras configuraciones | Literatura y práctica industrial |
| Vacío típico en short path | 50–150 micrones para la fracción principal | Práctica industrial |
| Temperatura de vapor (short path) | 155–185 °C | Práctica industrial |
| Tiempo de residencia (wiped film) | 1–3 min | Práctica industrial |
| Caudal de alimentación | Bajarlo **sube** rendimiento y recuperación | *Industrial Crops and Products* (2023) |

Ese último dato es el que más se ignora en planta: la tentación es alimentar rápido para producir más
kilos/hora, y es exactamente lo que baja la recuperación.

## La regla que gobierna todo: vacío antes que calor

La presión de vapor manda. A vacío profundo el cannabinoide destila a temperatura mucho menor, y menos
temperatura significa menos degradación de THC hacia CBN (ver `204`) y menos isomerización. Si tu vacío es
malo, la única manera de destilar es subir la temperatura — y ahí empiezas a quemar producto.

Diagnóstico rápido: **si tu distillate sale oscuro, casi siempre el problema es vacío insuficiente o
alimentación mal preparada, no el equipo.** Fugas de vacío, bomba con aceite contaminado, trampa fría
saturada o alimentación con agua/etanol residual son las cuatro causas habituales.

## Lo que tiene que traer la alimentación

| Requisito de la alimentación | Por qué | Módulo |
|---|---|---|
| Descarboxilada | El THCA no destila: se descarboxila en el equipo, libera CO₂ y arruina el vacío | `174` |
| Winterizada | Las ceras espuman, arrastran y ensucian la película | `191` |
| Sin agua ni etanol residual | Cualquier volátil destruye el vacío en el primer minuto | `149` |
| Sin sólidos | Rayan el rotor y ciegan la película | `191` |

En muchas plantas la descarboxilación se hace **en un reactor encamisado justo antes de destilar**, siguiendo
la cinética del módulo `174`: se calienta hasta que deja de burbujear CO₂, con el criterio de parada en el
máximo de Δ9-THC, no en "THCA = 0".

## Lo que la destilación NO hace

- **No separa CBD de THC.** Sus puntos de ebullición son demasiado parecidos. Para eso necesitas
  cromatografía o cristalización (ver `193`, `194`). Un destilado "de CBD" con THC por encima del límite
  **no se arregla destilando otra vez**.
- **No quita pesticidas de forma confiable.** Algunos se van con los ligeros, otros destilan con el
  cannabinoide. Nunca es una estrategia de remediación (`200`).
- **No quita metales pesados**, que quedan en el residuo — pero el arrastre existe, y hay que medirlo (`202`).
- **No devuelve terpenos.** Los perdiste en el corte de ligeros. Si tu producto los necesita, se reintroducen
  después en la formulación (ver `195`, `189`).

## Cómo se mide / cómo se comprueba

| Ensayo | Técnica | Unidad | Criterio típico de un distillate |
|---|---|---|---|
| Potencia y perfil | HPLC-DAD contra patrón certificado (`198`) | % p/p | 85–95 % de cannabinoides totales |
| **CBN** | HPLC-DAD, dentro del panel | % p/p | Marcador de exceso de calor: si sube lote a lote, revisa vacío |
| Terpenos | GC-MS / GC-FID headspace (`199`) | mg/g | Prácticamente ausentes; si aparecen, el corte de ligeros falló |
| Solventes residuales | GC-MS headspace (`201`) | ppm | El destilado suele salir limpio: es su ventaja frente al crudo |
| Metales pesados | ICP-MS (`202`) | µg/kg | Por lote; el equipo también puede aportar |
| Isómeros (Δ8, Δ10) | HPLC-DAD o LC-MS (`180`) | % p/p | Su aparición delata acidez y sobrecalentamiento |
| Agua | Karl Fischer (`98`) | % p/p | Cierra el balance de la pureza |

Y la regla de oro del COA de un destilado: **el balance de masa debe cerrar**. Si el reporte dice 92 % de
cannabinoides, ese 8 % restante tiene que estar buscado (agua, terpenos, otros cannabinoides, no volátiles).
Un COA que declara pureza y no reporta nada más está afirmando algo que no midió (ver `111`).

## Ejemplo aplicado (ILUSTRATIVO)

10,0 kg de aceite winterizado y descarboxilado, con 74,0 % p/p de cannabinoides totales (HPLC-DAD), en un
wiped film de 6" con dos pasadas. Cifras **(ILUSTRATIVO)**:

| Corriente | Masa | Cannabinoides | Cannabinoides absolutos |
|---|---|---|---|
| Alimentación | 10,00 kg | 74,0 % | 7,400 kg |
| Corte de ligeros | 0,45 kg | 12 % | 0,054 kg |
| **Distillate** | 7,60 kg | 91,5 % | 6,954 kg |
| Residuo pesado | 1,80 kg | 18 % | 0,324 kg |
| No contabilizado | 0,15 kg | — | 0,068 kg |

Recuperación de cannabinoides en el distillate = 6,954 / 7,400 = **94,0 %**, consistente con el 93,4 %
reportado en la literatura para condiciones optimizadas. El renglón que importa es el **residuo pesado**:
324 g de cannabinoides atrapados en 1,8 kg de material. Reprocesarlo o venderlo como grado inferior es una
decisión de negocio, pero **botarlo sin analizarlo es tirar plata**.

## Equipo modesto vs. maquila

| Actividad | Con equipo modesto | Exige maquila / planta |
|---|---|---|
| Preparar alimentación (descarbo, winterización) | **Sí** (`174`, `191`) | — |
| Short path de 2–5 L | Posible: manto, bomba de difusión o de dos etapas, trampa fría. Curva de aprendizaje alta y rendimiento irregular | Recomendable maquilar mientras aprendes |
| Wiped film de producción (kg/h) | No: equipo de decenas de miles de USD + chiller + bombas de vacío serias | **Sí** |
| Alcanzar > 90 % de forma reproducible | Difícil sin wiped film | Sí |
| Formulación con el distillate | Sí (`195`) | — |
| Potencia, CBN, isómeros, metales | No | **Sí** — laboratorio acreditado (`107`, `108`) |

Criterio honesto: **si procesas menos de unos pocos kilos de crudo al mes, maquilar la destilación es más
barato que comprar el equipo**, y te ahorra la curva de aprendizaje que se paga en producto quemado. Corre
el punto de equilibrio con `economist_lushows`, no a ojo.

## Errores comunes

- **Destilar sin descarboxilar.** El CO₂ liberado destruye el vacío y arruina la corrida.
- **Destilar sin winterizar.** Espuma, arrastre y una limpieza de tres horas.
- **Subir temperatura en vez de arreglar el vacío.** Es la causa raíz de casi todo distillate oscuro.
- **Alimentar rápido para producir más.** Baja la recuperación; está documentado.
- **Creer que destilar quita pesticidas o separa CBD de THC.** No y no.
- **Botar el residuo pesado sin analizarlo.** Suele traer 15–25 % de cannabinoides.
- **No seguir el CBN lote a lote.** Es tu carta de control del proceso térmico (`77`, `204`).
- **Comprar distillate "99 %" sin exigir método, patrón y balance de masa.** Pureza por área de pico no es
  pureza p/p contra patrón certificado (`70`, `111`).

## Conexión con otros módulos

→ `29-destilacion-y-equilibrio-liquido-vapor.md` — la teoría general de la destilación.
→ `28-gases-y-presion-de-vapor.md` — por qué el vacío baja el punto de ebullición.
→ `174-descarboxilacion-cinetica-y-calculo.md` — el paso obligatorio antes de destilar.
→ `191-winterizacion-y-desceramiento.md` — la otra condición de la alimentación.
→ `193-cromatografia-preparativa-y-aislados.md` — lo que sí separa molécula por molécula.
→ `194-remediacion-de-thc.md` — por qué destilar no baja el THC de un espectro amplio.
→ `204-estabilidad-y-degradacion-del-thc.md` — el CBN como marcador de exceso térmico.
→ `198-analisis-de-potencia-metodo.md`, `201-solventes-residuales-en-cannabis.md`,
  `202-metales-pesados-en-cannabis.md` — el panel que libera el lote.
