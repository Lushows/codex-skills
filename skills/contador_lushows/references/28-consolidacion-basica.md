# 28 — Consolidación Básica de Estados Financieros

A veces un dueño no tiene un negocio, sino varios, y uno controla a los otros. Por ejemplo, "Inversiones La Sazón S.A.S." es dueña del 80% del "Restaurante La Sazón" y del 100% de una "Comercializadora". Para saber cómo le va al **grupo completo** como si fuera una sola empresa, se hacen **estados financieros consolidados**.

Este módulo da la **visión básica**: cuándo toca consolidar, quién es quién, y qué se elimina. La consolidación es técnica y la firma siempre un **contador titulado**; aquí entiendes el concepto para no perderte.

## Cuándo se consolida

La regla central es el **control**: si una empresa controla a otra, debe consolidar.

| Concepto | Significa |
|---|---|
| **Matriz (o controlante)** | La empresa que controla a otra(s) |
| **Subordinada (subsidiaria)** | La empresa controlada por la matriz |
| **Control** | Poder de dirigir las decisiones (normalmente >50% de los votos, pero también por acuerdos) |
| **Participación no controladora (interés minoritario)** | La parte de la subordinada que NO es de la matriz |

> Cuando hay control, la matriz presenta **dos juegos**: sus estados **individuales** (solo ella) y los **consolidados** (ella + sus subordinadas como un todo). Los umbrales y excepciones exactos los define la norma colombiana vigente — no se inventan.

## La idea de consolidar: sumar y luego eliminar

Consolidar **no** es solo sumar las dos contabilidades. Eso contaría cosas dos veces. El proceso tiene dos pasos:

1. **Sumar** línea por línea los estados de la matriz y las subordinadas.
2. **Eliminar** las operaciones *entre* empresas del grupo (intercompañía), porque para el grupo "no existen": es plata moviéndose de un bolsillo a otro del mismo dueño.

### Qué se elimina
| Eliminación | Por qué |
|---|---|
| La inversión de la matriz en la subordinada vs. el patrimonio de esta | Si no, se contaría el patrimonio dos veces |
| Ventas y compras entre empresas del grupo | El grupo no se vende a sí mismo |
| Cuentas por cobrar/pagar entre el grupo | El grupo no se debe a sí mismo |
| Utilidades por ventas internas aún no realizadas afuera | No hay ganancia real hasta vender a un tercero |

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

**Grupo La Sazón — Consolidación simplificada de ventas (COP)**

| Concepto | Matriz | Subordinada | Suma simple | Eliminación | **Consolidado** |
|---|---:|---:|---:|---:|---:|
| Ventas a terceros | 50.000.000 | 120.000.000 | 170.000.000 | — | 170.000.000 |
| Venta de la matriz a la subordinada | 20.000.000 | — | 20.000.000 | (20.000.000) | 0 |
| **Total ventas** | **70.000.000** | **120.000.000** | **190.000.000** | **(20.000.000)** | **170.000.000** |

Sin eliminar, el grupo "vendería" $190 M, pero $20 M fueron de un bolsillo a otro: las ventas reales al mundo son $170 M. La participación no controladora (el 20% del restaurante que no es de la matriz) se muestra por separado dentro del patrimonio consolidado. Las sumas y eliminaciones se ejecutan en código vía Matematicas_lushows.

## Cómo leer estados consolidados en 30 segundos
1. Mira las **ventas a terceros** consolidadas: es el tamaño real del grupo frente al mundo.
2. Busca la **participación no controladora** en el patrimonio: parte de la utilidad no es de la matriz.
3. Compara individuales vs. consolidados: si difieren mucho, hay mucha operación intragrupo.

## Errores comunes
- **Sumar sin eliminar:** infla ventas, activos y deudas con operaciones internas.
- **Olvidar el interés minoritario:** no toda la subordinada es de la matriz.
- **Consolidar sin control real:** tener acciones no siempre es control; depende de los votos/acuerdos.
- **Confundir consolidado con individual al declarar impuestos:** los impuestos suelen ir sobre los individuales.
- **Inventar umbrales de control:** se confirman con la norma vigente.

## Conexión con otros módulos
- **Módulos 20–23:** se consolidan los cuatro estados, no solo el de resultados.
- **Módulo 24 (Notas):** la base de consolidación y las eliminaciones se revelan en notas.
- **Módulo 25 (Presentación NIIF):** los consolidados también exigen comparativos y juego completo.
- **economist_lushows:** estructurar un grupo empresarial (holding) es una decisión que orienta economist.

## Siguiente paso típico
Pasa al **módulo 29 (Leer estados para decidir)**: con todo armado (individual o consolidado), el dueño aprende a sacar conclusiones, sin invadir el terreno de la decisión, que es de economist.
