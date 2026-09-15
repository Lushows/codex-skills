# 112 — Cómo impugnar un resultado (el procedimiento real, no el berrinche)

Llega un resultado que no cuadra: el β-glucano salió en 18 % cuando el proveedor prometía 30 %, o el plomo
salió por encima del límite en un lote que ya está empacado. La reacción instintiva —llamar al laboratorio a
reclamar, o mandar la muestra a otro laboratorio a ver si sale mejor— es la peor de todas: la primera no
produce nada escrito, y la segunda es **lab shopping** (`113`), que destruye tu posición si la disputa
escala. Impugnar bien es un procedimiento con orden, con documentos y con plazos. Este módulo es ese
procedimiento, y las cláusulas que hay que dejar firmadas **antes** de necesitarlo.

Términos: **OOS (out of specification)** = resultado fuera de especificación. **impugnar (to dispute /
challenge)** = cuestionar formalmente un resultado. **contramuestra (retained sample)** = porción idéntica
guardada por ti (`109`). **reanálisis (retest)** = volver a analizar la **misma** muestra. **remuestreo
(resample)** = tomar una muestra **nueva** del mismo lote. **laboratorio dirimente (referee/umpire lab)** =
tercero acordado de antemano para resolver la discrepancia.

## Regla cero: primero se investiga, después se reclama

La disciplina farmacéutica ya resolvió cómo se hace, y sirve igual para un suplemento. La guía de la FDA para
investigar resultados fuera de especificación separa el trabajo en dos fases: **Fase I** determina si hubo
error de laboratorio; **Fase II** —solo si la Fase I no encontró un error confirmado— investiga producción y
materiales, y puede incluir reanálisis de la muestra original y remuestreo del lote
([FDA, *Investigating Out-of-Specification (OOS) Test Results for Pharmaceutical Production*, revisión nivel 2,
consultada a agosto de 2026](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/investigating-out-specification-oos-test-results-pharmaceutical-production-level-2-revision)).
La misma guía es tajante en algo que conviene grabarse: **repetir el ensayo hasta que dé bien ("testing into
compliance") nunca es aceptable**, y si la investigación confirma error de laboratorio, el resultado de
reanálisis sustituye al original pero **el dato original se conserva** con la explicación registrada.

Traducción para una pyme: un resultado malo no se borra. Se investiga, se documenta y se decide.

## El procedimiento en seis pasos

```
PASO 1 - CONGELAR (dia 0)
  Bloquea el lote (cuarentena fisica y en el sistema). No despachar, no reprocesar.
  Localiza la CONTRAMUESTRA sellada y verifica su precinto.
  Reune: COA, cadena de custodia, orden de servicio, correos, foto del precinto.

PASO 2 - AUDITAR EL PAPEL (dia 0-1, gratis)
  Pasa el COA por la lista de 111. Muchas impugnaciones terminan aqui:
  base no declarada, metodo equivocado, LOQ mayor que el limite, unidad mal transcrita.
  Rehaz TODAS las cuentas del certificado (restas, sumas, conversiones de base).

PASO 3 - PEDIR LOS DATOS CRUDOS AL LABORATORIO (dia 1-5)
  Por escrito, sin acusar. Lo que se pide:
    - cromatogramas / espectros / hojas de calculo del ensayo
    - curva de calibracion del dia, con R2 y rango
    - resultados de los controles de calidad de esa corrida (blancos, spikes, CRM) (ver 77)
    - peso de muestra, dilucion, factor de calculo
    - recuperacion (spike/recovery) en tu matriz (ver 74)
    - incertidumbre expandida y regla de decision aplicada
  Un laboratorio serio manda esto sin drama. La negativa es, en si misma, informacion.

PASO 4 - REANALISIS DE LA MISMA MUESTRA (dia 5-12)
  El laboratorio reanaliza la porcion original retenida por ellos, de preferencia con otro
  analista. Objetivo: descartar error de laboratorio (Fase I).
  Prohibido: reanalizar hasta que salga bien. Se define de antemano CUANTAS replicas y
  como se promedia.

PASO 5 - SEGUNDO LABORATORIO CON LA CONTRAMUESTRA (dia 10-25)
  Solo si el paso 4 no explica nada. Se manda TU contramuestra sellada al laboratorio
  dirimente, exigiendo el MISMO metodo, la MISMA base y la MISMA matriz declarada.
  Se le informa que es un analisis dirimente; no se le dice el resultado anterior
  (para no sesgarlo) pero si el metodo exacto.

PASO 6 - DECIDIR Y DOCUMENTAR (dia 25-35)
  Con los tres datos (original, reanalisis, dirimente) se concluye causa raiz y destino
  del lote: liberar, reprocesar, rechazar o destruir. Todo entra al expediente (168).
```

## Cómo se lee el resultado del laboratorio dirimente

| Escenario | Interpretación | Acción |
|---|---|---|
| Dirimente coincide con el original (dentro de sus U combinadas) | El resultado es real | El problema es del lote o del proveedor, no del laboratorio |
| Dirimente coincide con tu expectativa y difiere del original | Posible error del primer laboratorio | Exigir investigación formal y nota de corrección |
| Los tres valores dispersos | Muestra **heterogénea** o método no robusto en tu matriz | El problema es el muestreo (`66`) o el método (`75`), no la mala fe |
| Diferencia grande pero métodos distintos | No hay disputa: no midieron lo mismo | Repetir con método idéntico (`91`) |

La comparación no se hace "a ojo": dos resultados difieren de verdad cuando la diferencia supera la
incertidumbre combinada de ambos. Esa cuenta se ejecuta (`76`) y se rutea a `Matematicas_lushows`.

## La carta formal de impugnación (esqueleto)

```
Asunto: Impugnacion formal de resultado — Informe No. [XXX], lote [YYY]

1. Identificacion: informe, fecha, lote, ensayo y resultado impugnado (con unidad y base).
2. Hecho: cual es el resultado y por que se cuestiona (dato objetivo, no adjetivos).
   Ej.: "el informe reporta beta-glucano 18,2 % p/p sin declarar la base ni el alfa-glucano".
3. Fundamento tecnico: metodo esperado vs metodo usado; base; LOQ vs limite; incoherencias
   aritmeticas; ausencia de incertidumbre o de regla de decision (citando 107, 110, 111).
4. Peticion concreta y numerada:
   a) entrega de datos crudos y controles de calidad de la corrida;
   b) reanalisis de la porcion retenida por el laboratorio, con [N] replicas;
   c) informe de investigacion de causa raiz;
   d) plazo de respuesta: [10] dias habiles.
5. Reserva: se conserva contramuestra sellada No. [precinto] para analisis dirimente.
6. Firma del responsable tecnico y copia al responsable comercial.
```

Frente al **proveedor** (no al laboratorio) la carta cambia de eje: cita la orden de compra, la especificación
acordada, el resultado propio con su COA completo, y pide una de tres cosas concretas —reposición del lote,
nota crédito o devolución— con plazo. Lo comercial de esa negociación se prepara con `ventas_lushows` y
`economist_lushows`; lo contable y tributario de una nota crédito, con `contador_lushows`.

## Lo que hay que exigir POR CONTRATO (antes de necesitarlo)

| Cláusula | Qué debe decir |
|---|---|
| Especificación acordada | Analito, método exacto, unidad, **base**, límite y tolerancia. Sin esto no hay incumplimiento demostrable |
| Muestreo | Quién muestrea, con qué plan, y derecho del comprador a muestrear en origen o en destino |
| Contramuestra | El proveedor retiene una y **tú retienes otra**, selladas, por [24] meses |
| Laboratorio dirimente | **Nombrado de antemano** por acuerdo de las dos partes, con el método definido |
| Quién paga el dirimente | La parte que resulte equivocada. Es la cláusula que más disuade el fraude |
| Plazo de reclamación | Días desde la recepción para reclamar (30–60 típico) |
| Remedio | Reposición, nota crédito o devolución, y quién paga el flete de retorno |
| Confidencialidad de datos crudos | Que puedas exigirlos sin que te opongan "propiedad del método" |

La cláusula del **dirimente nombrado de antemano** es la más barata y la más poderosa: elimina de raíz la
discusión de "tu laboratorio es malo" y hace que nadie tenga incentivo para mandar la muestra al laboratorio
más complaciente.

## Ejemplo aplicado (ILUSTRATIVO)

Lote GL-2608 de reishi. Especificación: β-glucano ≥ 25,0 % p/p base seca por K-YBGL. Resultado: 18,2 %.

```
Paso 2 (auditoria del papel): el COA no reporta alfa-glucano ni base, y el metodo dice
        "polisacaridos por metodo interno". -> El ensayo NO fue K-YBGL: no hay comparacion posible.
Paso 3: el laboratorio confirma por escrito que uso fenol-sulfurico.
Paso 5: contramuestra sellada -> laboratorio dirimente, K-YBGL v2025.
        Glucano total 33,9 ; alfa-glucano 4,3 ; beta-glucano 29,6 % p/p base seca. Cumple.
Conclusion: no hubo lote malo ni proveedor mentiroso: hubo METODO EQUIVOCADO en el pedido.
Causa raiz: la orden de servicio no especificaba el metodo (falla propia, ver 109 campo 6).
Accion correctiva: formato de solicitud con metodo obligatorio; lote liberado.
Costo del error: 1 ensayo dirimente + 18 dias de lote bloqueado.
```

Cifras **(ILUSTRATIVO)**. La moraleja incomoda a propósito: la impugnación más frecuente termina demostrando
un error propio en cómo se pidió el análisis, no una trampa del otro.

## Errores comunes

- **Mandar la muestra a otro laboratorio "a ver si sale mejor"** sin investigar primero. Eso es lab shopping y
  te deja sin argumento (`113`).
- **Reanalizar hasta que dé bien.** "Testing into compliance" es una falta grave, no una estrategia.
- **No tener contramuestra.** Sin ella no hay disputa posible; solo queda aceptar (`109`).
- **Reclamar por teléfono o por WhatsApp.** Lo que no está escrito no existe en una disputa.
- **Comparar dos resultados de métodos distintos** y llamarlo discrepancia. No midieron lo mismo.
- **No pactar el dirimente en el contrato** y tener que negociarlo justo cuando ya hay conflicto.
- **Borrar el resultado original** al reemplazarlo. Se conserva, siempre, con la justificación.
- **Olvidar el análisis de impacto**: si el lote ya se vendió, hay que evaluar retiro y notificación (`169`).

## Conexión con otros módulos

→ `111-banderas-rojas-en-un-coa.md` — el paso 2, que resuelve la mitad de las impugnaciones gratis.
→ `109-cadena-de-custodia-y-envio-de-muestras.md` — la contramuestra, sin la cual nada de esto funciona.
→ `113-lab-shopping-e-inflacion-de-potencia.md` — la frontera entre impugnar y hacer trampa.
→ `76-incertidumbre-de-medida.md` — cuándo dos números difieren de verdad.
→ `77-control-de-calidad-analitico-y-cartas-control.md` — los controles de la corrida que vas a pedir.
→ `169-control-de-cambios-y-desviaciones.md` — cómo se documenta la desviación y su acción correctiva.
→ `292-negociar-con-laboratorios-y-maquiladores.md` — las cláusulas en la mesa de negociación.
