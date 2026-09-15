# Diagnóstico inicial del proyecto

> **Carga este módulo SIEMPRE antes de recomendar cualquier cosa.** Sin estas respuestas, cualquier
> consejo es genérico y probablemente equivocado.

## Las siete preguntas, una a la vez

Nunca las dispares juntas. Pregunta, escucha, y usa la respuesta para afinar la siguiente.

### 1. ¿A qué país le vas a vender?
Define arancel, medio de pago, CPM, ticket que aguanta y logística. Es la variable más pesada.
Si no lo sabe: **no elijas por él; corre el comparador** de `12` con sus restricciones.

### 2. ¿Cuánto capital tienes de verdad para esto?
No "cuánto tengo", sino **cuánto puedo perder sin que me afecte la vida**. Esta es la variable que
más cambia la recomendación.

| Capital | Lo que cambia |
|---|---|
| < $500 | La pregunta es cuántos tiros alcanzas, no cuánto ganas por venta. Prepago obligatorio por velocidad de caja. Ver `233`, `32` |
| $500 - $1.500 | Puedes testear 4-8 productos y escalar uno. Escenario estándar |
| $1.500 - $5.000 | Tests en paralelo, negociación por volumen, aguantas el CPM de Black Friday |
| > $5.000 | Stock adelantado, agente con bodega, línea DDP propia. Cambia el modelo |

### 3. ¿Tienes fecha límite?
Una temporada, un evento, un plazo personal. Define si hay tiempo para envío desde China o hay que
usar stock local. Corre el calendario de `35` y las fechas de corte de `170`.

### 4. ¿Ya tienes producto, o partimos de cero?
- **Tiene producto** → salta a validación: `41`, `76`, `42`. No asumas que sirve.
- **No tiene** → investigación: `50`, `52`, `59`.

### 5. ¿Ya tienes tienda?
- **Sí** → auditoría antes que tráfico. `204`, `208`. Escalar una página rota multiplica pérdidas.
- **No** → `178`, `175`.

### 6. ¿Qué canal de tráfico dominas o puedes aprender rápido?
Meta, TikTok, Google u orgánico. No es lo mismo: el canal define el tipo de producto que funciona.
Un producto que necesita demostración visual muere en búsqueda; uno que se busca por nombre
desperdicia el video. Ver `241`.

### 7. ¿Puedes grabar video tú mismo?
Determina si los creativos salen gratis o hay que pagarlos. Con capital chico, grabar con el celular
no es opcional: es la diferencia entre tener 8 ángulos o tener 1. Ver `253`.

## Preguntas de segundo nivel (solo si aplica)

- **¿Tienes empresa constituida?** Afecta pasarelas de pago y el IOSS si vendes a la UE. `237`, `192`.
- **¿Hablas el idioma del mercado?** Si no, el costo de los creativos se multiplica.
- **¿Tienes alguien que ayude?** La atención al cliente en temporada alta consume más de lo que se
  cree. `288`.
- **¿Has tenido cuentas publicitarias bloqueadas?** Cambia la estrategia de lanzamiento. `291`.
- **¿Tienes infraestructura reutilizable?** Bots de WhatsApp, dominios, pasarelas ya aprobadas, una
  lista de clientes. Todo eso es capital que no aparece en el banco.

## El resumen del diagnóstico

Antes de pasar a recomendar, devuélvele al usuario el diagnóstico en cinco líneas para que confirme:

```
País:        México (prepago, stock local)
Capital:     USD 500  →  ~5 tests escalonados (costo esperado USD 85 c/u)
Fecha tope:  Buen Fin 13-nov; Reyes 6-ene
Producto:    desde cero
Canal:       Meta (domina), TikTok (aprender)
```

Si algo de esas cinco líneas está mal, todo lo que viene después estará mal.

## Señales de alarma en el diagnóstico

| Señal | Qué significa | Qué hacer |
|---|---|---|
| "Todo el dinero que tengo" | Riesgo personal inaceptable | Frena. Sugiere reducir a un monto perdible |
| "Necesito que dé en 2 semanas" | Expectativa irreal | Muestra los plazos de `04` |
| "Ya compré 300 unidades" | Inventario antes de validar | Cambia el plan: hay que vender ese stock, no testear |
| "Un amigo me dijo que este producto es buenísimo" | Cero evidencia | Llévalo al scorecard `76` |
| "Quiero vender a Estados Unidos" | Probablemente no ha visto el arancel | `14`, `23` |

## Relacionados
`10` cómo se elige un país · `12` comparador de países · `233` cuántos tiros da tu capital · `241` Meta vs TikTok vs Google · `298` el plan de 90 días
