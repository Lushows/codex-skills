# Pruebas A/B en la página

> Vigencia: 14-sep-2026. Significancia estadística y tamaño de muestra: invoca
> `Matematicas_lushows`. Pruebas de creativos publicitarios: invoca `facebook_ads_lushows`.

## La verdad incómoda primero

Con el tráfico de una tienda que arranca, **casi ninguna prueba A/B te va a dar un resultado
concluyente**. Para detectar una mejora del 15% sobre una conversión del 3% necesitas miles de
sesiones por variante. Si haces 300 sesiones al día, esa prueba tarda semanas — y para entonces el
producto, la temporada y los creativos ya cambiaron.

Conclusión operativa: **antes de tener volumen, no hagas pruebas A/B. Haz cambios grandes y mide el
antes y el después.**

## Cuándo sí y cuándo no

| Tu volumen diario | Qué hacer |
|---|---|
| Menos de 300 sesiones/día | **Nada de A/B.** Cambia cosas grandes, compara semana contra semana |
| 300-1.000 sesiones/día | A/B solo de cambios grandes (encabezado entero, oferta entera) |
| Más de 1.000 sesiones/día | A/B en serio, una prueba a la vez |
| Más de 5.000 sesiones/día | Puedes probar detalles |

## Lo que sí debes probar, en orden de impacto

| # | Qué | Rango de efecto observado |
|---|---|---|
| 1 | **La oferta completa** (bundle, precio, qué incluye) | Enorme. Es la diferencia entre USD 2,63 y USD 20,18 de utilidad. `195` |
| 2 | **La promesa del encabezado** | Grande. `181` |
| 3 | **El precio** | Grande y contraintuitivo: subir precio a veces sube utilidad |
| 4 | **El video de demostración** | Grande. `186` |
| 5 | **La garantía** (30 vs 90 días, con o sin devolución) | Medio-grande. `188` |
| 6 | La primera imagen de la galería | Medio. `182` |
| 7 | El texto del botón | Pequeño |
| 8 | El color del botón | Casi siempre ruido |

**Nunca empieces por el color del botón.** Es el ejemplo clásico de prueba que consume tráfico y no
enseña nada.

## Las seis reglas

1. **Una variable a la vez.** Si cambias promesa y precio juntos, no sabes qué funcionó.
2. **Define el ganador antes de empezar.** Conversión, ticket, o utilidad por sesión: elígelo
   primero, no después de ver los datos.
3. **Corre semanas completas.** El martes no se comporta como el sábado.
4. **No pares al ver una ventaja.** La ventaja del día 2 desaparece el día 6 casi siempre.
5. **No pruebes durante Buen Fin ni Navidad.** El comportamiento es anómalo y contamina la lectura.
   `205`.
6. **Documenta todo.** Fecha, hipótesis, variantes, resultado, decisión. Sin bitácora, repetirás
   pruebas.

## La métrica correcta: utilidad por sesión

La conversión sola engaña. Si bajas el precio, la conversión sube y la utilidad baja.

| Variante | Conversión | Ticket (USD) | Utilidad/venta | **Utilidad por 1.000 sesiones** |
|---|---|---|---|---|
| A: producto suelto 699 MXN | 3,6% | 38,00 | 2,63 | **USD 94,68** |
| B: bundle 1.099 MXN con MSI | 3,0% | 60,05 | 20,18 | **USD 605,40** |

La variante A "gana" en conversión y pierde por goleada en dinero. **Siempre mide utilidad por
sesión.** Para calcularlo bien, invoca `Matematicas_lushows`.

## El formato de bitácora

| Campo | Ejemplo |
|---|---|
| Fecha inicio / fin | 21-sep → 5-oct 2026 |
| Hipótesis | "Poner la mensualidad de MSI junto al precio sube la conversión" |
| Variante A | Solo `$1,099 MXN` |
| Variante B | `$1,099 MXN` + `o 12 pagos de $91.58 sin intereses` |
| Métrica ganadora | Utilidad por sesión |
| Sesiones por variante | 4.100 / 4.050 |
| Resultado | B: +18% utilidad por sesión |
| ¿Concluyente? | Sí / No / Sin datos suficientes |
| Decisión | Se adopta B |

## El método para quien tiene poco tráfico

Como no puedes hacer A/B estadístico, usa el **cambio grande medido contra el periodo anterior**:

1. Deja la página estable 7 días. Anota conversión, ticket y utilidad por sesión.
2. Haz **un** cambio grande (la oferta, la promesa, el video).
3. Deja 7 días más, con el mismo gasto y los mismos creativos.
4. Compara.
5. Si la diferencia es menor al 20%, considérala ruido y sigue adelante.

Solo funciona si mantienes constante todo lo demás: mismo creativo, mismo presupuesto, mismo
público. Si cambias el anuncio a la vez, no aprendiste nada.

## Las trampas

| Trampa | Qué pasa |
|---|---|
| Parar la prueba al ver el resultado que querías | Confirmas tu sesgo, no la realidad |
| Probar durante una promoción | El comportamiento cambia por completo |
| Probar con dos creativos distintos corriendo | No sabes si movió la página o el anuncio |
| Herramienta de A/B que ralentiza la página | Pierdes más por velocidad de lo que ganas. `196` |
| Parpadeo de la variante (se ve A y luego B) | Arruina la prueba y la confianza |
| Probar 5 cosas a la vez con poco tráfico | Ruido puro |
| Concluir con 40 conversiones | No hay significancia |

## Qué probar en el proyecto de México (diciembre 2026)

Con capital bajo USD 500, el volumen será bajo. Prioridad:

| Semana | Qué cambiar | Por qué |
|---|---|---|
| 1-2 | Línea base con la mejor página que sepas hacer | No pruebes, construye bien |
| 3 | La promesa del encabezado | El de mayor impacto. `181` |
| 4 | La composición del bundle | Decide la utilidad. `195` |
| 5 | La mensualidad de MSI junto al precio | Barato y suele mover mucho |
| **13-17 nov** | **Nada.** Solo operar | No se prueba en temporada. `205` |
| Después | Lo que la bitácora diga | |

## Relacionados
`199` analítica · `203` conversión esperada · `204` diagnóstico · `195` MSI · `205` temporada alta
