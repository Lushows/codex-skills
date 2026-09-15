# 00 — El método del contador de élite

Antes de tocar un solo número, conviene entender *cómo piensa* un buen contador. No es alguien que "mete datos en un software": es la persona que traduce todo lo que pasa en tu negocio (una venta, un pago, un préstamo) a un lenguaje exacto, verificable y que cumple la ley. Este módulo te enseña ese método de trabajo para que entiendas qué estamos haciendo y por qué, aunque nunca hayas estudiado contabilidad.

La promesa de esta skill cabe en tres palabras: **CUADRE, CUMPLIMIENTO y AUDITABLE**. Todo lo que sigue existe para sostener esas tres palabras.

## El ciclo de seis pasos

Un contador profesional repite siempre el mismo ciclo. No improvisa.

| Paso | Qué significa | Pregunta que responde |
|---|---|---|
| 1. Entender | Comprender el hecho económico real antes de anotarlo | ¿Qué pasó de verdad en el negocio? |
| 2. Registrar | Anotarlo en partida doble con su soporte | ¿Cómo lo escribo para que cuadre? |
| 3. Conciliar | Cruzar mis libros contra la realidad (banco, inventario) | ¿Mis números coinciden con el mundo real? |
| 4. Reportar | Producir estados financieros legibles | ¿Qué historia cuentan estos números? |
| 5. Cumplir | Declarar y pagar a tiempo y en el formato correcto | ¿La DIAN y la ley quedan satisfechas? |
| 6. Explicar | Traducir todo a lenguaje humano para el dueño | ¿Qué decisión te ayuda a tomar? |

Si te saltas un paso, la cadena se rompe. Por ejemplo: registrar sin conciliar produce estados financieros bonitos pero falsos.

## Principio 1 — Sustancia sobre forma

Lo que importa es **qué pasó de verdad**, no cómo se llamó el papel. Si te "prestaron" plata pero nunca la vas a devolver, eso es un aporte de capital, no un préstamo. El contador mira la realidad económica.

## Principio 2 — Todo registro tiene un soporte

Cada anotación nace de un documento: factura, recibo, extracto bancario, contrato. **Sin soporte no hay registro.** Si la DIAN o un auditor pregunta "¿por qué anotaste esto?", siempre debe haber un papel (o PDF) que lo respalde. Esto es lo que hace tu contabilidad *auditable*.

## Principio 3 — Nunca calcular de cabeza

Esta es una regla de oro de la casa. Un contador serio **no hace cuentas mentales con el dinero del cliente**. Todo cálculo no trivial se ejecuta en código y se verifica dos veces. El dinero se maneja con tipo `decimal` (precisión exacta), **nunca** con `float` (que redondea mal y te puede generar diferencias de centavos que dañan el cuadre). Cuando el cálculo es complejo —liquidar una nómina, una depreciación, un interés— se lo pasamos a la skill hermana **Matematicas_lushows**, que tiene la promesa de error cero.

## Principio 4 — El cuadre es sagrado

En partida doble, la suma de los débitos siempre es igual a la suma de los créditos. Si no cuadra, *algo está mal* y no se avanza hasta arreglarlo. No existe "casi cuadra". Lo veremos a fondo en el módulo 02.

## Principio 5 — Honestidad sobre riesgos

Un buen contador te dice cuándo algo es riesgoso, cuándo una norma no está clara, y cuándo necesitas un profesional titulado que firme. No te vende falsa tranquilidad. Esta skill **no reemplaza** al contador público que pone su firma y su tarjeta profesional en tus declaraciones (ver módulo 09).

## Ejemplo del método en acción (cifras ILUSTRATIVAS / inventadas)

Vendiste un Excel a un cliente por $50.000 y te pagó a la cuenta.

1. **Entender:** entró plata por una venta de servicio digital.
2. **Registrar:** débito a Bancos $50.000, crédito a Ingresos $50.000 (cuadra).
3. **Conciliar:** el extracto del banco muestra ese ingreso de $50.000. ✔️
4. **Reportar:** ese ingreso aparece en el Estado de Resultados del mes.
5. **Cumplir:** ese ingreso se acumula para la futura declaración de IVA/renta.
6. **Explicar:** "vendiste $50.000; tu margen en esto es casi todo ganancia porque el costo del Excel ya estaba pagado".

> Las cifras anteriores son inventadas para enseñar el método. No son datos reales de ningún negocio.

## Errores comunes

- **Empezar a registrar sin entender el hecho.** Anotar rápido produce errores caros que después cuesta deshacer.
- **Confiar en la memoria o en una calculadora mental.** Genera diferencias de centavos que rompen el cuadre.
- **Registrar sin guardar el soporte.** Cuando llega la auditoría, no hay con qué defenderse.
- **Avanzar con los libros descuadrados** "para arreglarlo después". Nunca se arregla; se acumula.
- **Esconder los riesgos al dueño** para que se sienta tranquilo. Eso no es servicio, es negligencia.

## Conexión con otros módulos

- El estándar CUADRE/CUMPLIMIENTO/AUDITABLE se detalla en el módulo **01**.
- La mecánica del cuadre (débito = crédito) está en el módulo **02**.
- Antes de registrar nada, haz el **diagnóstico inicial** del módulo **05**.
- Cuando una decisión sea de negocio (¿subo precios?, ¿es viable?) eso es de **economist_lushows**, no del contador.

## Siguiente paso típico

Lee el módulo **01** para entender a fondo la promesa de la skill, y luego el **05** para hacer el diagnóstico de tu caso antes de registrar el primer asiento.
