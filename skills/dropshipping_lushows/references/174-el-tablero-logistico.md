# El tablero logístico

> Si tu única métrica logística es "cuántos pedidos vendí", estás volando a ciegas. El tablero
> logístico existe para responder tres preguntas todos los días: **¿qué está atascado?, ¿cuánto me
> está costando?, y ¿qué zona o transportadora me está sangrando?**

## Las tres capas

| Capa | Frecuencia | Para qué |
|---|---|---|
| **Operativa** | Diaria, 10 minutos | Apagar incendios antes de que el cliente los vea |
| **Táctica** | Semanal | Decidir transportadora, zona, confirmación |
| **Estratégica** | Mensual | Decidir producto, mercado, modelo de pago |

## Capa 1 — el barrido diario

| Alerta | Umbral | Acción |
|---|---|---|
| Pedidos sin confirmar | > 12 h | Confirmar hoy (`160`) |
| Pedidos confirmados sin despachar | > 24 h | Despachar o explicar |
| Guías creadas sin recolección | > 24 h | Reclamar a la paquetería |
| Sin movimiento en tránsito | > 48-72 h | Abrir caso + avisar al cliente (`171`) |
| Intentos fallidos de ayer | cualquiera | Contactar hoy |
| Fecha prometida vencida | cualquiera | Mensaje nivel 2 (`171`) |
| Sin movimiento | > 7 días | Escalar, posible extravío (`165`) |
| Errores de entrega de WhatsApp | cualquiera | Revisar ventana de 24 h (`162`) |
| Días de stock restante | < 10 | Reponer o planear apagar pauta |

Diez minutos al día. Si te toma más de veinte, automatiza las alertas, no contrates a alguien para
mirar la pantalla.

## Capa 2 — las métricas semanales

| Métrica | Fórmula | Referencia |
|---|---|---|
| Tasa de confirmación | confirmados ÷ pedidos | 60-80% |
| **Tasa de entrega** | entregados ÷ despachados | Ver `159` |
| Tasa efectiva | entregados ÷ pedidos | — |
| **Desperdicio** | (1 − tasa) ÷ tasa | < 0,45 sano |
| Días pedido → despacho | promedio | ≤ 1 |
| Días despacho → entrega | percentil 90 | Es tu promesa real (`157`) |
| Devoluciones | devueltos ÷ entregados | Por categoría (`164`) |
| Extravíos | perdidos ÷ despachados | < 0,5% |
| Costo logístico por entrega | (fletes + retornos + empaque) ÷ entregados | — |
| **Margen por despachado** | Ver `163` | El número honesto |

## El corte que importa: nunca mires el promedio solo

| Cortar por | Qué revela |
|---|---|
| **Transportadora** | Una puede entregar 12 puntos mejor que otra |
| **Ciudad / zona** | Dónde estás perdiendo plata (`173`) |
| **Confirmado vs no confirmado** | La prueba de que confirmar paga (`159`) |
| Anuncio de origen | Un anuncio puede traer compradores de peor calidad |
| Día de la semana | El despacho del viernes entrega peor |
| Semana | Detectar degradación de temporada (`169`) |

El promedio nacional es el número más inútil del tablero. Sirve para el reporte, no para decidir.

## Capa 3 — la revisión mensual

| Pregunta | Dato que la responde |
|---|---|
| ¿El modelo de pago sigue siendo el correcto? | Margen por despachado en COD vs prepago (`30`) |
| ¿Qué zona apago o paso a prepago? | Tabla por zona (`173`) |
| ¿Cambio de transportadora? | Tasa y extravío por operador |
| ¿El proveedor sigue sirviendo? | % de defectuosos y faltantes (`164`, `165`) |
| ¿Cuándo repongo stock? | Velocidad de venta + tiempo de tránsito (`146`) |
| ¿Cuánto me cuesta realmente el producto? | Landed cost actualizado (`152`) |

## La hoja mínima (sin software)

Una hoja de cálculo con una fila por pedido y estas columnas cubre todo lo anterior:

```
fecha_pedido · canal · ciudad · zona_riesgo · transportadora · guía
estado_confirmacion · hora_1er_contacto · intentos · motivo_no
fecha_despacho · fecha_entrega · estado_final · motivo_fallo
precio · costo_producto · flete_ida · flete_retorno · empaque · comision · cac
```

Con eso sacas todas las métricas con tablas dinámicas. No necesitas nada más hasta los 300-500
pedidos al mes. **El que espera a tener software para medir, no mide nunca.**

## Las tres alarmas que no se negocian

| Alarma | Umbral | Por qué |
|---|---|---|
| **Tasa de entrega semanal** cae más de 5 puntos | 5 pts | Algo se rompió: transportadora, zona o confirmación |
| **Días de stock** bajan de 10 | 10 días | Riesgo de vender lo que no tienes |
| **Margen por despachado** se vuelve negativo en alguna zona | 0 | Estás pagando por vender |

Estas tres se revisan aunque no revises nada más.

## La regla del cambio único

> **Un cambio a la vez. Tres días limpios de datos. Mínimo 30-50 pedidos por celda antes de juzgar.**

Cambiar transportadora, guion de confirmación y zona en la misma semana significa que al final no
sabes qué funcionó y vas a repetir el error en el próximo producto.

## Errores de tablero

| Error | Consecuencia |
|---|---|
| Medir entregados ÷ pedidos y llamarlo tasa de entrega | Mezclas dos problemas distintos |
| Mirar solo el promedio nacional | Zonas malas invisibles |
| No registrar el motivo del fallo | No puedes arreglar nada |
| Revisar mensualmente lo que es diario | Te enteras de todo tarde |
| Tablero bonito que nadie mira | Prefiere feo y revisado |
| Confundir horario UTC con el local en los reportes | Los picos de actividad salen corridos |

## Relacionados
`159` tasa de entrega · `163` costo de los rechazos · `173` zonas difíciles · `156` tracking ·
`171` cuando se atrasa · `152` costo puesto en destino · invoca `Matematicas_lushows`
