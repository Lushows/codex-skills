# 113 — Lab shopping e inflación de potencia (el fraude que el mercado premia)

**Lab shopping** es mandar la misma muestra a varios laboratorios y publicar solo el resultado que más
conviene. **Inflación de potencia (potency inflation)** es el efecto agregado: un mercado donde los números
publicados suben año tras año sin que el producto mejore, porque el laboratorio que reporta más alto gana los
clientes. Es el fraude más estudiado en cannabis, pero la mecánica es idéntica en hongos —donde el analito
inflado se llama "polisacáridos"— y en cualquier categoría donde el comprador pague por un número. Este
módulo explica por qué el mercado lo premia, cómo se detecta desde afuera y cómo se blinda un negocio que no
quiere jugar ese juego.

Términos: **lab shopping** = elegir el laboratorio por su resultado, no por su competencia. **inflación de
potencia** = sesgo sistemático al alza de los valores reportados. **sesgo de selección (selection bias)** = el
sesgo de publicar solo lo favorable. **auditoría de potencia (potency audit)** = el regulador compra el
producto en tienda y lo reanaliza. **muestra ciega (blind sample)** = muestra de valor conocido enviada sin
avisar (`108`).

## Por qué el mercado lo premia (la economía del número)

```
El consumidor asocia numero alto con calidad y paga mas por el.
        v
El productor necesita numero alto para vender.
        v
El laboratorio compite por clientes, y su producto es un numero.
        v
El laboratorio que reporta mas alto consigue mas clientes.
        v
Los laboratorios rigurosos pierden mercado o se ajustan.
        v
Todo el mercado sube sin que ningun producto haya mejorado.
```

Es una carrera hacia arriba donde el rigor es una desventaja competitiva. Por eso no se corrige sola: se
corrige con auditoría del comprador y con regulación. Y por eso el punto de apalancamiento de una marca
honesta es el comprador B2B, no el consumidor final: el B2B sí reanaliza.

## Qué tan grande es el problema (evidencia con fuente)

- Un estudio revisado por pares en **PLOS ONE (12 de abril de 2023, Schwabe, Johnson, Harrelson y McGlaughlin)**
  compró 23 muestras de flor de cannabis de 12 variedades en 10 dispensarios de Colorado y las midió por HPLC:
  la potencia media observada (14,98 % de THC) fue **23,1 % menor** que el mínimo declarado en la etiqueta y
  **35,6 % menor** que el máximo declarado; alrededor del **70 %** de las muestras estuvo más de un 15 % por
  debajo del mínimo etiquetado, y **solo una** cayó dentro del rango de la etiqueta
  ([PLOS ONE, consultado a agosto de 2026](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0282396)).
- A **agosto de 2026**, el lab shopping está bajo escrutinio regulatorio activo en Norteamérica: se reportan
  auditorías de potencia en las que la autoridad retira producto del anaquel y lo reanaliza en laboratorios de
  referencia, y estados como California y Colorado han introducido requisitos de trazabilidad que dificultan
  esconder ensayos fallidos ([resumen sectorial 2026, consultado a agosto de 2026](https://www.cannabisregulations.ai/cannabis-and-hemp-regulations-compliance-ai-blog/cannabis-lab-testing-standards-2026-potency-audits-iso-17025)).
  Ese mismo panorama señala la acreditación **ISO/IEC 17025** como requisito de entrada para los laboratorios
  del sector (`107`).

El dato clave para un no técnico: el problema **no es que un laboratorio se equivoque**, es que el error tiene
una **dirección constante**. Un error aleatorio se cancela entre lotes; un sesgo sistemático no.

## Las seis palancas técnicas con las que se infla un número

| Palanca | Cómo se ve en el COA | Cómo se detecta |
|---|---|---|
| **Muestreo dirigido** | El proveedor manda la mejor porción | El COA no dice quién muestreó (`109`, `111` #11) |
| **Método que mide de más** | "Polisacáridos totales", "azúcares totales" | El método está en el certificado: léelo (`91`, `222`) |
| **Base conveniente** | Reportar base seca sin decirlo, o al revés | Falta humedad o falta la palabra "base" (`07`) |
| **Curva de calibración forzada** | Rango mal ajustado, R² bajo, extrapolación | Pedir la curva del día y los controles (`71`, `112`) |
| **Redondeo y cifras** | Resultados redondos, decimales inventados | Cifras significativas incoherentes con el LOQ (`05`) |
| **Selección del resultado** | Solo aparece el COA "bueno" | Pedir **todos** los análisis del lote, por escrito |

En hongos, la palanca dominante es la segunda: no hace falta manipular nada si el ensayo que se cobra ya mide
almidón junto con β-glucano. El fraude está en la elección del método, no en el instrumento (`218`).

## Cómo se blinda un comprador (seis defensas, de la más barata a la más cara)

1. **Exigir el método en la orden de servicio.** Gratis. Elimina la palanca #2 de un plumazo.
2. **Muestrear tú o exigir muestreo del laboratorio.** Costo bajo. Elimina la palanca #1 (`109`).
3. **Pedir todos los análisis del lote, no el mejor.** Gratis, y la reacción del proveedor ya es un dato.
4. **Muestras ciegas y duplicados con otro código.** Costo: un ensayo extra. Mide sesgo y repetibilidad (`108`).
5. **Verificación por lote en tu propio laboratorio de confianza.** Es el control de calidad real (`283`).
6. **Laboratorio dirimente pactado por contrato**, pagado por quien resulte equivocado (`112`).

## La frontera: qué es legítimo y qué no

| Situación | ¿Legítimo? |
|---|---|
| Comparar cotizaciones de varios laboratorios antes de contratar | Sí — eso es elegir proveedor (`108`) |
| Enviar la misma muestra a dos laboratorios y **publicar ambos** | Sí — es verificación |
| Impugnar un resultado siguiendo el procedimiento documentado | Sí (`112`) |
| Enviar a cinco y publicar el más alto | **No** — lab shopping |
| Repetir el ensayo hasta que dé bien | **No** — "testing into compliance" (`112`) |
| Analizar el mejor lote y usar ese COA para todos | **No** — es el fraude que rompe la relación B2B |

La prueba de fuego es simple: **¿podrías publicar todos los resultados que obtuviste?** Si la respuesta es no,
lo que estás haciendo es lab shopping, se llame como se llame.

## Ejemplo aplicado (ILUSTRATIVO)

Dos proveedores de polvo de reishi ofrecen a BIO-SETA, mismo precio por kilo:

```
Proveedor A: "beta-glucano 45 %"   COA de 1 pagina, sin lote, metodo "interno",
                                    sin alfa-glucano, sin base, sin humedad.
Proveedor B: "beta-glucano 30,7 %" COA de 2 paginas, lote, K-YBGL v2025, alfa-glucano 4,1 %,
                                    base seca, humedad 5,0 % Karl Fischer, laboratorio acreditado,
                                    muestreo por el laboratorio.

Prueba de verificacion (una muestra ciega de cada uno al mismo laboratorio dirimente, K-YBGL):
  Proveedor A -> glucano total 41,2 ; alfa-glucano 33,8 ; beta-glucano  7,4 % p/p b.s.
  Proveedor B -> glucano total 33,9 ; alfa-glucano  4,3 ; beta-glucano 29,6 % p/p b.s.

Costo de la verificacion: 2 ensayos.
Lectura: el alfa-glucano de 33,8 % en A es sustrato de grano (218). Su "45 %" era polisacaridos
totales, no beta-glucano. Comprarle a A a "mismo precio" era pagar 4 veces mas por kilo de activo.
```

Cifras **(ILUSTRATIVO)**. El cálculo del costo por kilo de activo —que es el único precio que importa— se
ejecuta con `Matematicas_lushows` y se lleva al margen con `economist_lushows`.

## Errores comunes

- **Comparar proveedores por el porcentaje** en vez de por el costo por kilo de activo verificado.
- **Creer que el número alto es un problema del proveedor.** El número alto lo pide el mercado; el proveedor
  responde al incentivo.
- **Impugnar mandando la muestra a otro laboratorio sin procedimiento.** Eso es el mismo lab shopping, con
  otro signo (`112`).
- **Confiar en que la acreditación resuelve el sesgo.** Ayuda mucho, pero no cubre el muestreo ni la elección
  del método por parte del cliente.
- **No pedir todos los análisis del lote.** La pregunta cuesta un correo y desarma la palanca principal.
- **Publicar el mejor COA propio en la web** y guardar los demás. Es la versión doméstica del mismo fraude, y
  cuando un cliente B2B lo descubre, no hay vuelta (`293`).

## Conexión con otros módulos

→ `112-como-impugnar-un-resultado.md` — cómo se cuestiona un número sin caer en esto.
→ `111-banderas-rojas-en-un-coa.md` — las señales que delatan un COA seleccionado.
→ `108-como-elegir-un-laboratorio.md` — elegir por competencia, incluida la prueba con muestras ciegas.
→ `218-el-fraude-del-micelio-en-grano.md` y `222-polisacaridos-totales-por-que-no-sirve.md` — la versión hongos.
→ `213-como-leer-un-coa-de-cannabis.md` — la versión cannabis, con su bandera roja #10.
→ `293-como-comunicar-ciencia-sin-mentir.md` — cómo se cuenta un número honesto sin perder la venta.
→ `283-plan-de-control-de-calidad-por-lote.md` — la verificación propia que vuelve irrelevante el COA ajeno.
