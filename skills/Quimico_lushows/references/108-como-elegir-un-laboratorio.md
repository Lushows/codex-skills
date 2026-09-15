# 108 — Cómo elegir un laboratorio (el proveedor más importante que vas a contratar)

El laboratorio es el proveedor que decide si tu producto se vende o se destruye, y es el único al que le
compras un **número** en vez de una cosa. Elegirlo por precio es el error más caro del oficio: un ensayo
barato con el método equivocado no es más económico, es inútil, y encima te da una falsa tranquilidad que
puede durar hasta que un cliente B2B mande el mismo lote a su propio laboratorio. Este módulo es el proceso
de selección completo: cómo se hace la lista corta, qué se pregunta, cómo se compara una cotización con otra,
y cómo se prueba al laboratorio antes de casarse con él.

Términos: **laboratorio contratado (contract lab / CRO)** = laboratorio externo al que le compras ensayos.
**alcance acreditado (scope)** = ensayo + matriz + método que su acreditación cubre (ver `107`).
**TAT (turnaround time)** = tiempo desde que reciben la muestra hasta que emiten el informe.
**muestra ciega (blind sample)** = muestra que tú conoces y ellos no, para probarlos.
**contramuestra (retained sample)** = porción idéntica que tú guardas (ver `109`).

## Los cuatro tipos de laboratorio y para qué sirve cada uno

| Tipo | Fuerte en | Débil en | Cuándo elegirlo |
|---|---|---|---|
| Universitario (grupo de investigación) | Técnicas exóticas, HRMS, RMN, precio bajo | TAT largo, poca acreditación, informe no comercial | Desarrollo, exploración, caracterización |
| Comercial local acreditado | Rutina acreditada, TAT razonable, cercanía | Puede no tener el método de tu nicho | Control por lote, cumplimiento nacional |
| Comercial internacional (redes grandes) | Alcance amplio, aceptación en exportación | Precio, logística, mínimos de volumen | Exportación, cliente B2B exigente, disputa |
| Especializado de nicho (hongos, cannabis) | El método específico bien hecho | Pocos, a veces sin acreditación en la matriz | β-glucano por K-YBGL, potencia, terpenos |

Para BIO-SETA la realidad es que **el β-glucano por Megazyme K-YBGL lo hacen pocos laboratorios** (ver `91`,
`221`). Cuando el método es raro, el orden de la búsqueda se invierte: primero buscas quién sabe hacerlo, y
después miras acreditación, precio y TAT.

## Las doce preguntas del correo de precalificación

Manda este correo a 4–6 laboratorios. Las respuestas —y la velocidad y calidad con que responden— ya
seleccionan solos.

```
1. Que metodo usan para [analito] en [matriz exacta]? Referencia del metodo (AOAC/USP/kit/SOP).
2. Ese ensayo en ESA matriz esta dentro de su alcance acreditado? Envienme el anexo tecnico.
3. Cual es el LOQ y el LOD del metodo en esa matriz, con unidad? (ver 73)
4. Cual es la incertidumbre expandida (k=2) al nivel de concentracion que me interesa? (ver 76)
5. Participan en ensayos de aptitud para este analito? Ultimo desempeno? (ver 107)
6. Como validaron el metodo para esta matriz? Recuperacion tipica? (ver 74, 75)
7. Cuanta muestra necesitan, en que estado, y como debe llegar? (ver 109)
8. TAT comprometido en dias habiles, y recargo por urgencia.
9. Precio por muestra y precio por panel, con descuento por volumen.
10. Guardan contramuestra? Cuanto tiempo? Puedo pedir reanalisis del mismo extracto?
11. Que politica tienen para resultados fuera de especificacion y para reanalisis? (ver 112)
12. El informe declara metodo, base, unidad, LOQ, incertidumbre y regla de decision?
```

Si un laboratorio no puede responder la 1, la 2, la 3 y la 12, sáquelo de la lista sin importar el precio. No
son preguntas difíciles: son las que el propio sistema de calidad del laboratorio ya tiene contestadas.

## Cómo se comparan dos cotizaciones (no es por precio)

| Criterio | Peso sugerido | Cómo se puntúa |
|---|---|---|
| Método correcto para la matriz | 30 % | Enzimático específico vs colorimétrico: no son comparables (`91`) |
| Alcance acreditado que cubre tu ensayo + matriz | 20 % | Cubre / no cubre / reporta fuera de alcance |
| LOQ suficientemente bajo frente al límite | 15 % | LOQ debe ser 5–10 veces menor que el límite aplicable |
| Desempeño en ensayos de aptitud | 10 % | Satisfactorio documentado / sin evidencia |
| TAT y cumplimiento del TAT | 10 % | Comprometido por escrito |
| Calidad del informe | 10 % | ¿Trae método, base, LOQ, incertidumbre? |
| Precio | 5 % | Solo desempata entre los que ya pasaron |

El precio pesa poco a propósito. La razón es aritmética: un ensayo de β-glucano cuesta el orden de cientos de
dólares, y un lote mal liberado cuesta el lote entero más la relación con el cliente. Lleva la comparación de
plata a `economist_lushows` si el volumen anual es grande, y el presupuesto a `291`.

## La prueba antes del matrimonio: muestras ciegas

Antes de darle todo tu volumen a un laboratorio, pruébalo. Cuesta poco y te dice más que cualquier brochure.

```
PRUEBA DE 3 MUESTRAS (misma remesa, codigos distintos, sin decirle nada al laboratorio)
  Muestra A: material de referencia certificado o muestra de valor conocido
             -> mide EXACTITUD (sesgo frente al valor verdadero, ver 74)
  Muestra B: duplicado exacto de A, con otro codigo
             -> mide REPETIBILIDAD (dos numeros del mismo material)
  Muestra C: tu material real de un lote representativo
             -> mide si el metodo aguanta TU matriz

Lectura:
  A lejos del valor certificado          -> sesgo: no lo contrates para cumplimiento
  A y B distintos entre si (mas que su U)-> baja precision: el numero no decide nada
  C con recuperacion pobre o interferencia -> el metodo no esta validado para tu matriz
```

Repite una versión reducida de esta prueba **una vez al año** con el laboratorio ya contratado. No es
desconfianza: es lo mismo que el laboratorio hace con sus propios controles (ver `77`).

## Ejemplo aplicado (ILUSTRATIVO)

BIO-SETA busca laboratorio para β-glucano en polvo de cuerpo fructífero.

| | Lab A (comercial local) | Lab B (universitario) | Lab C (especializado, exterior) |
|---|---|---|---|
| Método | Fenol-sulfúrico ("polisacáridos totales") | Megazyme K-YBGL, versión 2025 | Megazyme K-YBGL, versión 2025 |
| Acreditado para la matriz | Sí, para "azúcares totales" | No | Sí |
| Reporta α-glucano por separado | No | Sí | Sí |
| Precio por muestra | USD 45 | USD 150 | USD 210 |
| TAT | 5 días | 20 días | 12 días |

Veredicto: **Lab A queda descartado aunque sea el más barato y el único acreditado**, porque su método no mide
β-glucano (`222`). Entre B y C: B para desarrollo y control interno, C para el COA que va al cliente B2B y a
exportación. Es normal y sano tener dos laboratorios con roles distintos. Cifras **(ILUSTRATIVO)**.

## Errores comunes

- **Elegir por precio sin comparar el método.** Es el error que financia el fraude del sector.
- **No pedir el anexo técnico del alcance.** El logo no es la acreditación (`107`).
- **No preguntar el LOQ.** Un LOQ más alto que el límite legal convierte "no detectado" en nada (`73`).
- **Mandarle la muestra que el proveedor te dio** en vez de tomarla tú. El COA describe lo que él quiso (`109`).
- **Un solo laboratorio para todo, sin plan B.** Cuando se cae el equipo, tu producción se detiene.
- **No probar con muestras ciegas** y descubrir el sesgo el día de una disputa.
- **Aceptar un informe que no declara base ni método.** Ese papel no defiende nada (`111`).

## Conexión con otros módulos

→ `107-iso-17025-y-acreditacion.md` — cómo se verifica el alcance que aquí se exige.
→ `109-cadena-de-custodia-y-envio-de-muestras.md` — cómo llega la muestra sin arruinar el resultado.
→ `114-costos-y-tiempos-de-analisis.md` — órdenes de magnitud para negociar con datos.
→ `292-negociar-con-laboratorios-y-maquiladores.md` — la negociación comercial, sin bajar calidad.
→ `284-auditoria-de-proveedor.md` — la calificación formal del laboratorio como proveedor crítico.
→ `65-el-metodo-analitico-de-punta-a-punta.md` — qué le vas a pedir exactamente y por qué.
→ `112-como-impugnar-un-resultado.md` — lo que debe quedar pactado por contrato antes de necesitarlo.
