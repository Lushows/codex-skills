# 79 — HPLC y UHPLC: el caballo de batalla de todo análisis de potencia

Si vendes un producto natural y alguna vez vas a poner un número de activo en la etiqueta, ese número casi
seguro va a salir de un HPLC. Es la técnica que cuantifica cannabinoides, triterpenos ganodéricos,
psilocibina, cordicepina, hericenonas, vitaminas y prácticamente todo compuesto orgánico que sea soluble y
no volátil. No necesitas operarla; necesitas entender qué hace, qué la daña y qué preguntarle al
laboratorio, porque el 90 % de las peleas por potencia se resuelven mirando el cromatograma, no el COA.

Términos:
- **HPLC (high-performance liquid chromatography)** = cromatografía líquida de alta resolución: se empuja la
  muestra disuelta a través de una columna empacada y cada compuesto sale a un tiempo distinto.
- **UHPLC / UPLC (ultra-high-performance liquid chromatography)** = lo mismo con partículas más pequeñas
  (< 2 µm) y presiones más altas; corre más rápido y separa mejor.
- **Fase móvil (mobile phase)** = el líquido que arrastra. **Fase estacionaria (stationary phase)** = lo que
  está pegado a la columna y retiene.
- **Tiempo de retención (retention time, tR)** = cuánto tarda un compuesto en salir. Es la "identidad" del
  pico en un HPLC simple.
- **Gradiente (gradient)** = la mezcla de solventes cambia durante la corrida. **Isocrático (isocratic)** =
  no cambia.
- **Fase reversa (reversed phase, RP)** = fase estacionaria apolar (C18) y móvil polar (agua/acetonitrilo).
  Lo apolar se retiene más. Es el 80 % de todo lo que se hace.

## Cómo funciona, en cristiano

La bomba empuja la fase móvil a 100–600 bar. El inyector mete 1–20 µL de tu extracto. En la columna, cada
molécula reparte su tiempo entre quedarse pegada a la fase estacionaria y viajar con la fase móvil. Las que
se quedan pegadas más tiempo salen después. El detector (casi siempre UV-DAD, ver `80`) mide cuánta luz
absorbe lo que va saliendo y dibuja el cromatograma. **El área del pico es proporcional a la cantidad**, y
esa proporción se establece con una curva de calibración de patrones (`70`, `71`).

## HPLC vs UHPLC — qué cambia para ti

| | HPLC clásico | UHPLC |
|---|---|---|
| Tamaño de partícula | 3–5 µm | 1,3–2 µm (o core-shell 2,6 µm en HPLC) |
| Presión de trabajo | 100–400 bar | 600–1300 bar |
| Corrida típica de cannabinoides | 15–25 min | 4–9 min |
| Solvente consumido por muestra | 20–35 mL | 4–10 mL |
| Costo del equipo (ILUSTRATIVO) | USD 35.000–70.000 | USD 80.000–150.000 |
| Riesgo | Menor resolución en pares difíciles | Se tapa con muestras sucias; exige mejor filtrado |

Para ti, lo que importa: **UHPLC no es "más exacto", es más rápido y más eficiente**. Un laboratorio con
HPLC clásico y método bien desarrollado te da un resultado igual de defendible. Si te cobran más "porque es
UPLC", el argumento correcto es el tiempo de entrega, no la calidad del dato.

## El método real de cannabinoides por HPLC-DAD

Este es el método que corre casi todo laboratorio de cannabis del mundo, en su forma genérica. Sirve para
que hables de igual a igual cuando pidas cotización.

```
COLUMNA        C18 de fase reversa, 150 x 4,6 mm, 2,6-3 um (core-shell) o
               100 x 2,1 mm, 1,7 um si es UHPLC.
FASE MOVIL     A: agua + 0,1 % acido formico
               B: acetonitrilo + 0,1 % acido formico
               (algunos metodos usan 0,05 % TFA o buffer de formiato de amonio 5 mM;
                si se va a acoplar a MS, formiato de amonio, nunca TFA — ver 83)
GRADIENTE      Ejemplo (ILUSTRATIVO): 65 % B a 0 min -> 75 % B a 10 min ->
               95 % B a 12-14 min (lavado) -> 65 % B, reequilibrio 3 min.
               Varios metodos de potencia corren ISOCRATICO ~ 25:75 agua:acetonitrilo
               con acido, lo cual es mas robusto pero mas lento.
FLUJO          1,0-1,5 mL/min (4,6 mm) ; 0,4-0,6 mL/min (2,1 mm)
TEMPERATURA    30-40 C, CONTROLADA. El par CBD/CBG y el par CBC/THC se mueven
               con la temperatura: sin horno de columna el metodo no es robusto.
DETECCION      DAD. Cuantificacion a 220-228 nm (banda principal de cannabinoides).
               Se registra tambien 270-280 nm para CBN y para pureza de pico (80).
INYECCION      5-10 uL de extracto diluido en metanol o metanol:agua.
CORRIDA        9-25 min segun cuantos cannabinoides se separen (6, 11 o 16).

POR QUE ACIDO FORMICO: los cannabinoides acidos (THCA, CBDA) tienen un grupo
carboxilo. A pH bajo quedan neutros y eluyen como picos simetricos con
retencion estable. Sin acido, el THCA sale ancho, con cola y con el tiempo de
retencion moviendose. El acido es lo que hace cuantificable la forma acida.

POR QUE 220-228 nm: alli los cannabinoides absorben fuerte. A 280 nm la senal
cae para varios, aunque se conserva para CBN, que por eso va en el segundo
canal (204).
```

## Por qué NO se usa GC para cannabinoides ácidos

Este punto vale plata literal, y es el malentendido más caro del sector.

En cromatografía de gases (`85`) la muestra se vaporiza en un inyector a 250–280 °C. A esa temperatura el
**THCA se descarboxila** casi por completo y se convierte en Δ9-THC dentro del inyector (`174`). Resultado:

```
Muestra real de flor fresca:
    THCA .... 18,0 % p/p base seca
    D9-THC ... 0,6 % p/p base seca

Reporte por HPLC (sin calor):
    THCA 18,0 %  |  D9-THC 0,6 %  |  THC total = 0,6 + 18,0*0,877 = 16,39 % p/p

Reporte por GC sin derivatizar:
    THCA "no detectado"  |  D9-THC ~ 16,4 %   <- todo junto, ya convertido

Los dos numeros son "verdad", pero responden preguntas distintas.
```

Consecuencias prácticas:

1. **Pierdes la información de la forma ácida.** No puedes saber si el material está fresco (predomina THCA)
   o ya descarboxilado. Para hemp legal y para producto crudo, esa distinción es el producto, y un producto
   que se vende como "no psicoactivo por estar en forma ácida" no se puede sustentar con GC.
2. **La conversión en el inyector nunca es 100 %.** Es 70–95 % según inyector, temperatura y matriz, así que
   el "THC total" por GC tiene un sesgo variable e incontrolable. Por eso se pide HPLC, o GC **con
   derivatización** (sililación con BSTFA/TMS, ver `64`), que protege el carboxilo y separa THCA de THC.
3. **Si te van a medir el 0,3 % p/p de THC total**, el método importa más que la planta. Un GC mal usado te
   puede volver ilegal un lote legal, o al revés (`175`, `198`).

Regla corta para cotizar: **potencia de cannabinoides = HPLC-DAD. Terpenos = GC (`199`). Solventes
residuales = headspace-GC (`87`). Metales = ICP-MS (`88`).**

## Qué le pasa a un HPLC y cómo te afecta

| Síntoma en el cromatograma | Causa típica | Efecto en tu resultado |
|---|---|---|
| Picos con cola (tailing) | Silanoles libres, columna vieja, pH mal | Integración ambigua, resultado bajo o inflado |
| Tiempos de retención que se corren | Temperatura sin control, fase móvil mal preparada, columna equilibrándose | Identificación errónea de cannabinoide menor |
| Presión subiendo corrida a corrida | Filtro/columna tapándose por matriz sucia | Corte de corrida, resultados perdidos |
| Línea base con ondas | Burbujas, mezcla mal desgasificada, lámpara vieja | Integración inestable en trazas |
| Picos fantasma en el blanco | Arrastre (carryover) de la muestra anterior | Falso positivo de THC en producto CBD |
| Pico saturado (plano arriba) | Muestra muy concentrada, fuera de rango lineal | **Subestimación** de potencia, típico en concentrados |

Esa última fila es la que más veces termina en pleito: un extracto al 80 % inyectado sin diluir satura el
detector y sale "62 %". Pide siempre que el resultado caiga **dentro del rango de la curva** (`73`).

## Costo y tiempo (orden de magnitud, ILUSTRATIVO)

| Servicio | Precio típico Colombia | Tiempo |
|---|---|---|
| Potencia de cannabinoides (6–11 analitos), HPLC-DAD | COP 180.000–450.000 por muestra | 3–8 días hábiles |
| Cuantificación de 1 marcador por HPLC en matriz vegetal | COP 150.000–350.000 | 5–10 días |
| Desarrollo de método nuevo HPLC | COP 4–12 millones | 3–8 semanas |
| Validación completa del método (`75`) | COP 8–25 millones | 4–10 semanas |

Son órdenes de magnitud para presupuestar, no cotizaciones. Verifica con `114` y con tres laboratorios (`108`).

## Qué preguntarle al laboratorio

1. ¿Qué **columna** exacta (marca, química, dimensiones, tamaño de partícula) y qué **fase móvil**?
2. ¿Corren **gradiente o isocrático**, y con **horno de columna** a qué temperatura?
3. ¿A qué **longitud de onda** cuantifican y cuál usan de confirmación? (`80`)
4. ¿Cuántos cannabinoides/marcadores separan y con qué **resolución en el par crítico**?
5. ¿El resultado de mi muestra cayó **dentro de la curva** o extrapolaron?
6. ¿Corren **blanco entre muestras** para descartar arrastre?
7. ¿Me mandan el **cromatograma**, no solo la tabla? (Si se niegan, bandera roja — `111`.)

## Errores comunes

- **Pedir "potencia" sin decir qué analitos.** Seis cannabinoides y dieciséis cuestan y significan cosas
  distintas.
- **Comparar un COA de HPLC con uno de GC** y concluir que un proveedor miente.
- **Aceptar resultados de concentrados sin dilución adecuada** (pico saturado).
- **Creer que el tiempo de retención identifica**. Identifica solo dentro de ese método y con patrón; para
  identidad real hace falta DAD con espectro o MS (`80`, `84`).
- **No filtrar la muestra** y luego reclamar porque el laboratorio cobró cambio de columna.
- **Ignorar la estabilidad en el vial**: el THCA descarboxila si el automuestreador se calienta (`255`).

## Conexión con otros módulos

→ `31-principio-de-la-cromatografia.md` — la física detrás de la separación.
→ `80-deteccion-uv-dad-y-pureza-de-pico.md` — el detector y cómo se demuestra que el pico es puro.
→ `81-columnas-fases-y-desarrollo-de-metodo-lc.md` — cómo se elige columna y se desarrolla el método.
→ `83-lc-ms-ms-y-mrm.md` — cuando UV no alcanza y hay que ir a trazas.
→ `85-cromatografia-de-gases.md` — la técnica hermana y sus dominios propios.
→ `174-descarboxilacion-cinetica-y-calculo.md` y `175-thc-total-y-el-factor-0877.md` — el fondo del problema THCA/THC.
→ `198-analisis-de-potencia-metodo.md` — el método de potencia aplicado a cannabis, punta a punta.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — el mismo instrumento en hongos psilocibios.
