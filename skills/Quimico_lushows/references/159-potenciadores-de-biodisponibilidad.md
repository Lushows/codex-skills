# 159 — Potenciadores de biodisponibilidad (qué funciona, qué se vende y qué es riesgo)

"Mejora la absorción" es el segundo claim más usado del mercado de suplementos, después de "natural". A veces es
cierto, a veces es marginal y a veces —el caso de la piperina— viene con un riesgo de interacción farmacológica
que casi ninguna marca advierte. Este módulo separa las tres categorías con el criterio del oficio: qué
mecanismo tiene, qué nivel de evidencia lo sostiene, cómo se mide y qué se puede decir legalmente.

Términos: **biodisponibilidad (bioavailability, F)** = fracción de la dosis que llega intacta a circulación
sistémica (`122`). **Efecto de primer paso (first-pass effect)** = metabolismo hepático e intestinal antes de
llegar a circulación. **P-glicoproteína (P-gp)** = bomba de eflujo que devuelve moléculas al intestino.
**CYP3A4** = enzima que metaboliza una fracción enorme de fármacos (`124`). **AUC (area under the curve)** =
exposición total en el tiempo; es el parámetro que mide biodisponibilidad relativa.

## Las cinco estrategias, por mecanismo

| Estrategia | Mecanismo | Ejemplos | Evidencia | ¿Pyme? |
|---|---|---|---|---|
| Aumentar solubilidad | Más disuelto = más absorbible | Nanoemulsión (`157`), ciclodextrina (`158`), dispersión sólida | Sólida en principio, específica por molécula | Maquila o CD |
| Coadministrar grasa | Estimula bilis y vía linfática | Aceite MCT, tomar con comida | Bien documentada para cannabinoides `[clínico]` | **Sí, gratis** |
| Reducir tamaño de partícula | Más superficie de disolución | Micronización, molienda húmeda | Sólida para poco solubles | Parcial (`143`) |
| Inhibir metabolismo/eflujo | Menos primer paso | Piperina, quercetina, naringenina | Real, y por eso mismo **riesgosa** | Sí, pero ojo |
| Cambiar la vía | Evitar el hígado | Sublingual, tópico, inhalado (`123`) | Depende de la vía | Sí |

## La grasa: el potenciador más barato y más ignorado

Para cannabinoides es el caso más claro y mejor documentado. El CBD y el THC son extremadamente lipofílicos
(logP ~6–7). Tomados en ayunas, su absorción es baja y errática; con una comida grasa, la exposición sube de
forma sustancial `[clínico]`. Los mecanismos: solubilización en micelas biliares y transporte parcial por vía
linfática, que **evita el primer paso hepático**.

Consecuencia práctica y gratuita para tu producto: **la instrucción de uso es parte de la formulación.**
"Tomar con una comida que contenga grasa" puede valer más que una tecnología de encapsulación cara. Y ese texto
sí se puede poner en la etiqueta sin problemas regulatorios, porque es un modo de empleo, no un claim de salud.

Para hongos el panorama es distinto: los β-glucanos no se "absorben" en el sentido clásico. Se cree que
interactúan con receptores del tejido linfoide intestinal (dectina-1, receptor de complemento) `[in vitro]`
`[animal]` (`130`). Aplicarles el discurso de biodisponibilidad de una molécula pequeña es un error
conceptual: **la pregunta correcta no es cuánto β-glucano llega a sangre, sino qué estructura y qué peso
molecular tiene el que llega al intestino.** Vender "β-glucano liposomal de alta biodisponibilidad" es, en el
mejor de los casos, confuso.

## Piperina: el caso que hay que mirar de frente

La piperina (del pimiento negro, marca comercial más conocida: BioPerine) inhibe CYP3A4 y P-gp. Eso es
exactamente por lo que "funciona": el activo se metaboliza menos y se elimina menos.

- Tiene evidencia real de aumentar la exposición de algunos compuestos, siendo el caso más estudiado la
  curcumina `[clínico, en esa combinación específica]`.
- **El mismo mecanismo aplica a los medicamentos que la persona esté tomando.** Un inhibidor de CYP3A4 puede
  subir los niveles plasmáticos de fármacos que se metabolizan por esa vía (`124`, `139`).
- Por eso, poner piperina "porque potencia todo" en un producto de consumo general no es neutro. Es una
  decisión farmacológica que debería ir con advertencia de interacciones.

Regla del oficio: **si un potenciador funciona inhibiendo una enzima de metabolismo, hereda el perfil de
interacciones de esa enzima.** No hay atajo. Lo mismo aplica a la quercetina y a la naringenina (toronja).

## Cómo se comprueba que un potenciador funcionó

Solo hay una manera honesta, y no es in vitro:

```
ESTUDIO DE BIODISPONIBILIDAD RELATIVA (diseño mínimo)

  Diseño: cruzado (crossover), aleatorizado, con período de lavado (washout)
  n:      12–24 sujetos sanos es el rango típico de un estudio piloto
  Brazos: A = formulación estándar   |   B = formulación con potenciador
  Muestreo: sangre a 0; 0,25; 0,5; 1; 1,5; 2; 3; 4; 6; 8; 12; 24 h
  Bioanálisis: LC-MS/MS validado para el activo y sus metabolitos (`83`, `75`)
  Parámetros: Cmax, Tmax, AUC0-t, AUC0-∞, t½
  Resultado:  F_relativa = AUC_B / AUC_A × 100

  Requisitos NO negociables: comité de ética, consentimiento informado,
  registro del estudio. Ver `289`.
```

Costo realista: un estudio así no es de pyme. La alternativa honesta es **no hacer el claim**. Un producto puede
estar bien formulado y decirlo en términos de composición ("con aceite MCT") sin afirmar un múltiplo de
absorción que no midió.

## Cuando el proveedor te muestra un "5× más biodisponible"

```
LAS CUATRO PREGUNTAS QUE DESARMAN CUALQUIER MÚLTIPLO

  1. ¿Contra qué comparador?         → si es "polvo puro" o "activo cristalino", el múltiplo está inflado
  2. ¿En qué especie?                → rata ≠ humano
  3. ¿Qué parámetro?                 → Cmax sube fácil; AUC es el que importa
  4. ¿Publicado y revisado?          → un póster interno no es evidencia (`11`, `12`)

Ejemplo de lectura (ILUSTRATIVO):
  "22× más biodisponible" contra CBD en polvo puro  →  cierto y casi irrelevante:
  nadie vende CBD en polvo puro. Contra un aceite MCT bien formulado,
  la diferencia real es mucho menor.
```

## Ejemplo aplicado — dos decisiones para BIO-SETA y para una línea de cannabis

```
CASO 1 — cápsula de extracto de hongos
  ¿Piperina?  NO.
    Razón 1: el mecanismo (inhibir CYP3A4) no aplica al β-glucano, que no se absorbe como molécula pequeña.
    Razón 2: agrega un riesgo de interacción farmacológica sin beneficio demostrado para este activo.
  ¿Qué sí?    Estructura y peso molecular del glucano; dosis correcta (`161`); tomar con o sin comida
              según tolerancia digestiva.

CASO 2 — aceite sublingual de CBD
  ¿Nanoemulsión?  Tal vez, pero es maquila cara y frágil (`157`).
  ¿Qué primero?   Aceite MCT + instrucción "tomar con comida grasa" + retención sublingual 60–90 s.
                  Es gratis, tiene soporte clínico y no compromete estabilidad.
  Medir:          si un día quieres el claim, se mide con el estudio de arriba. Mientras tanto, no se afirma.
```

## Errores comunes

- Poner piperina "por si acaso" y crear un riesgo de interacción no advertido.
- Repetir el múltiplo del proveedor sin conocer el comparador.
- Aplicar el marco de biodisponibilidad de molécula pequeña a los β-glucanos.
- Confundir Cmax con AUC: un pico alto y corto no es más exposición total.
- Usar in vitro (Caco-2, disolución) como si fuera prueba de biodisponibilidad humana `[in vitro]` ≠
  `[clínico]` (`12`).
- Hacer un claim de absorción en la etiqueta sin haberlo medido en tu formulación. En Colombia, cualquier
  afirmación debe poder sostenerse (`267`, `268`).
- Olvidar que aumentar biodisponibilidad también aumenta la exposición a lo indeseado: si el extracto trae
  contaminantes, también se absorben mejor.

## Conexión con otros módulos

→ `122-biodisponibilidad-y-efecto-de-primer-paso.md` — la farmacocinética que sostiene todo el módulo.
→ `124-citocromo-p450-e-interacciones.md` — por qué la piperina es un arma de doble filo.
→ `157-emulsiones-y-nanoemulsiones.md` y `158-liposomas-y-ciclodextrinas.md` — las tecnologías de solubilidad.
→ `130-inmunomodulacion-y-beta-glucanos.md` — por qué los glucanos juegan otro juego.
→ `139-interacciones-planta-farmaco.md` — el mapa de interacciones que hay que advertir.
