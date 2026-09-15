# Mentalidad del operador y el ciclo del fracaso

## El ciclo que mata al 95%

```
  Encuentra un producto que le encanta
            ↓
  Monta la tienda en 3 semanas (perfeccionismo)
            ↓
  Gasta $80 en anuncios, 0 ventas
            ↓
  "Le falta tiempo al algoritmo" → gasta $80 más
            ↓
  1 venta. "¡Funciona!" → sube presupuesto
            ↓
  Se acaba la plata. Culpa al producto, al país, a Meta
            ↓
  Se retira, o empieza de cero con otro producto que le encanta
```

Cada paso de ese ciclo es un error de **mentalidad**, no de técnica:

| Paso | El error mental | Lo correcto |
|---|---|---|
| "Un producto que le encanta" | Confunde gusto propio con demanda | Buscar evidencia de que otros ya lo compran (`60`) |
| "3 semanas montando" | Perfeccionismo como forma de evitar el juicio del mercado | Página mínima viable en 2 días (`178`) |
| "Le falta tiempo" | No sabe cuánto presupuesto se necesita para tener señal | Presupuesto de test definido de antemano (`232`) |
| "1 venta, funciona" | Confunde ruido con señal | 3 ventas mínimo, y con economía positiva (`78`) |
| "Culpa al producto" | Atribución externa: impide aprender | Autopsia numérica de cada test (`296`) |

## Las tres tensiones que hay que aguantar

**1. Velocidad contra calidad.** Este negocio premia lanzar rápido y feo por encima de lanzar tarde
y bonito, porque el mercado da la información que ninguna planificación da. Pero hay un piso: una
página sin confianza no convierte por más rápido que salga (`197`).

*Regla práctica:* la primera versión sale en 48 horas. La mejora se hace con datos, no con opinión.

**2. Persistencia contra terquedad.** Son lo mismo visto desde afuera; se distinguen por el criterio
de salida. Persistencia es "sigo porque el CTR subió y el problema está en el checkout". Terquedad es
"sigo porque presiento que va a arrancar".

*Regla práctica:* si no puedes nombrar **qué número** te haría parar, ya estás en terquedad.

**3. Ambición contra supervivencia.** Con capital chico, la decisión correcta casi siempre es la que
te deja seguir jugando mañana, no la que maximiza el retorno de hoy.

*Regla práctica:* nunca pongas en un solo test más del 20% del capital disponible.

## El apego al producto: el error más caro

Es previsible y tiene causa: cuanto más trabajo pones en un producto (fotos, textos, video), más te
cuesta matarlo. Es costo hundido operando como emoción.

**Cómo desactivarlo:**
- Define el criterio de muerte **antes** de lanzar y escríbelo. "Si a los $60 gastados no hay 3
  ventas con CPA menor a X, se cierra."
- Testea siempre 2-3 productos a la vez. El apego se diluye cuando no hay un único candidato.
- Lleva el registro de productos muertos con su autopsia. Convierte la pérdida en biblioteca.

## Qué esperar de verdad, en números

| Hito | Realista | Lo que venden los cursos |
|---|---|---|
| Primera venta | Entre el producto 1 y el 4 | "El primer día" |
| Primer producto rentable | Entre el producto 5 y el 12 | "En la primera semana" |
| Recuperar la inversión inicial | 2-4 meses | "El primer mes" |
| Operación estable | 6-12 meses | "90 días a 6 cifras" |

No es pesimismo: es el rango que permite planear el capital. Quien entra esperando la curva de los
cursos se queda sin plata en la mitad de la curva real.

## Las cinco preguntas del operador disciplinado

Hazlas al cerrar cada semana:

1. ¿Cuántos productos nuevos puse a prueba esta semana? (Si es cero, el negocio está quieto.)
2. ¿Cuál fue el número que me hizo tomar cada decisión? (Si no hay número, fue corazonada.)
3. ¿Qué producto debí matar y no maté? (Y por qué no lo maté.)
4. ¿Cuánto capital me queda y para cuántos tests alcanza? (`233`)
5. ¿Qué aprendí que sirva para el próximo producto, no solo para este?

## Sobre la ansiedad de la temporada

En Q4 la presión es real: el CPM sube, el calendario aprieta, y cada día perdido cuesta más. Esa
presión empuja a dos errores caros:

- **Subir presupuesto demasiado rápido** sobre un producto con señal débil.
- **No matar** lo que no funciona, "porque ya estamos en temporada y no hay tiempo de empezar otro".

La disciplina en temporada alta vale más, no menos. Ver `294`.

## Relacionados
`78` matar a tiempo · `79` el portafolio de tests · `232` presupuesto de test · `294` plan de guerra de temporada · `297` errores que matan tiendas
