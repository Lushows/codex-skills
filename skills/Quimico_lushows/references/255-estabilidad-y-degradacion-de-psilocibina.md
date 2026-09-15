# 255 — Estabilidad y degradación de psilocibina (el resultado contraintuitivo: el congelador es peor que el cajón)

La psilocibina se degrada por dos caminos: pierde el fosfato y se convierte en psilocina (hidrólisis o acción
enzimática), y la psilocina se oxida hasta compuestos azules sin actividad. Lo interesante es que la
literatura publicada trae un resultado que contradice la intuición de todo el mundo: **el material seco
guardado en oscuridad a temperatura ambiente se conservó mejor que el material fresco congelado a −80 °C.**
Este módulo explica por qué y cómo se diseña un estudio de estabilidad serio para estos analitos.

**Alcance (línea roja):** estabilidad química y diseño de estudio analítico. Nada de esto es una guía de
conservación de material ilícito; es lo que un laboratorio necesita saber para que sus resultados sean
válidos y lo que un desarrollador farmacéutico necesita para su ICH Q1.

Términos: **desfosforilación (dephosphorylation)** = pérdida del grupo fosfato. **quinoide (quinoid)** =
producto de oxidación de un fenol; aquí, el pigmento azul. **ICH Q1A** = guía internacional de estudios de
estabilidad. **condición acelerada (accelerated condition)** = 40 °C / 75 % HR, para estimar vida útil.

## Las dos rutas de degradación

```
PSILOCIBINA  ──(fosfatasa fúngica / hidrólisis por calor y humedad)──►  PSILOCINA
                                                                          │
                                                       (O₂, luz, pH alto, lacasas)
                                                                          ▼
                                          Especies quinoides azules → oligómeros (sin actividad)
```

El grupo fosfato es literalmente un escudo: mientras esté puesto, el fenol no se oxida. Por eso el material
seco pierde poco, y por eso todo lo que favorezca la hidrólisis (agua líquida, calor, enzimas activas,
descongelado) acelera la pérdida total.

## Datos publicados de estabilidad

| Condición | Observación | Fuente |
|---|---|---|
| Biomasa seca, oscuridad, temperatura ambiente | La **menor** degradación de todas las condiciones ensayadas | Gotvaldová et al., *Drug Test. Anal.*, 2021 |
| Material fresco a −80 °C | La **mayor** degradación observada; se asocia a conversión de psilocibina a psilocina | Gotvaldová et al., 2021 |
| Solución acuosa, 90 °C | ~17 % de hidrólisis a psilocina en 1 h | Literatura de manufactura cGMP (*ACS Omega*, 2020) |
| Solución acuosa, 70 °C | ~3–4 % de hidrólisis por hora | Ídem |
| Solución acuosa, 60 °C | Degradación lenta y sostenida; psilocina como impureza principal | Ídem |
| Soluciones patrón acuosas | Inestabilidad temporal documentada por HPLC | *J. Forensic Sci.* / literatura analítica |

La explicación del resultado del congelador: la congelación y descongelación **rompen células y liberan
fosfatasas**, que actúan sobre la psilocibina; y la psilocina liberada se oxida rápido. Es un caso de libro
de por qué "más frío" no siempre es "más estable" en matrices biológicas vivas.

## Consecuencias directas para el laboratorio

Esto no es teoría: cambia cómo se manejan las muestras y los patrones.

| Elemento | Práctica correcta | Motivo |
|---|---|---|
| Muestra sólida | Secar, moler y guardar en oscuridad, seca, temperatura ambiente | Menor degradación reportada |
| Muestra fresca | Analizar de inmediato o secar antes de guardar | Fosfatasas activas |
| Extracto en solución | Analizar el mismo día; refrigerar y proteger de la luz | Hidrólisis y oxidación |
| Patrones acuosos | Preparar fresco; verificar estabilidad antes de usar viales viejos | Inestabilidad documentada |
| Antioxidante | Puede añadirse ácido ascórbico al extracto | Frena la oxidación de psilocina |
| pH | Extraer en medio ligeramente ácido | La oxidación se acelera a pH alcalino |
| Vial | Vidrio ámbar | La luz acelera la ruta oxidativa |
| Estabilidad de la muestra procesada | **Validarla explícitamente** (ICH Q2, `75`) | Sin este dato, tus resultados no son defendibles |

## Cómo se comprueba: un estudio de estabilidad bien diseñado

```
Diseño mínimo (ICH Q1A adaptado a material de investigación):
  Condiciones: 25 °C/60 % HR (largo plazo) · 40 °C/75 % HR (acelerada) · 5 °C · luz (ICH Q1B)
  Tiempos:     0, 1, 3, 6, 9, 12, 18, 24 meses (acelerada: 0, 1, 2, 3, 6 meses)
  Analitos:    psilocibina, psilocina y suma como psilocibina equivalente (251)
  Método:      LC-MS/MS o HPLC-DAD validado, indicativo de estabilidad (256)
  n:           3 réplicas independientes por punto
  Criterio:    ≥ 90 % del valor inicial y balance de masa que cierre

Balance de masa obligatorio:
  Si la psilocibina baja 1,00 mg/g, la psilocina debería subir ~0,72 mg/g (factor 0,7186).
  Si NO sube, hay una segunda ruta de pérdida (oxidación) y hay que buscar los productos.
```

Esa verificación del balance es lo que distingue un estudio de estabilidad real de una tabla de números: si
lo que se pierde no aparece en otro lado, el método no está viendo todo lo que pasa.

## Ejemplo aplicado (ILUSTRATIVO)

```
Material seco de investigación, 25 °C/60 % HR, oscuridad, envase de vidrio ámbar

Mes  Psilocibina  Psilocina  Psilocibina equiv.  % del inicial
 0     7,42        0,31        7,85               100,0 %
 3     7,18        0,45        7,81                99,5 %
 6     6,95        0,58        7,76                98,9 %
12     6,51        0,74        7,54                96,1 %
24     5,88        0,92        7,16                91,2 %

Lectura: la psilocibina cae, la psilocina sube, y la suma (psilocibina equivalente) cae poco.
Es decir: la mayor parte de la pérdida es CONVERSIÓN, no destrucción — hasta el mes 24.
La diferencia entre lo que cae la suma (8,8 %) y lo que caería solo por conversión es
lo que se fue por oxidación.
```

## Errores comunes

- **Congelar material fresco creyendo que se conserva.** La literatura publicada muestra lo contrario.
- **Reportar solo psilocibina.** Sin psilocina no ves la conversión y crees que perdiste todo.
- **No validar la estabilidad de la muestra ya extraída.** Si la solución se degrada entre la preparación y
  la inyección, todos tus resultados son bajos y no lo sabes.
- **Guardar patrones acuosos por meses.** Se degradan; tu curva de calibración queda sesgada.
- **Trabajar con luz directa y viales transparentes.** La ruta oxidativa se acelera.
- **No hacer el balance de masa.** Sin él no distingues conversión de destrucción.

## Conexión con otros módulos

→ `251-psilocibina-y-psilocina-quimica.md` — el factor 0,7186 y el papel del fosfato.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — método indicativo de estabilidad.
→ `164-estabilidad-ich-q1-y-vida-util.md` y `165-estudios-acelerados-y-arrhenius.md`.
→ `47-oxidacion-y-degradacion-de-productos-naturales.md` y `61-estabilidad-quimica-luz-calor-oxigeno.md`.
→ `75-validacion-de-metodos-ich-q2-r2.md` — dónde se demuestra la estabilidad de la muestra.
→ `254-variabilidad-de-potencia-entre-especies.md` — la otra fuente de dispersión.