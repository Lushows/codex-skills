# Cómo medir competencia por nicho

"Hay mucha competencia" no es un dato, es una sensación. Esto se cuenta. En 45 minutos puedes tener un número que te dice si el nicho es entrable, y ese número se puede volver a medir dentro de 30 días para ver hacia dónde va.

## El método de las 3 mediciones

### Medición 1 — Anunciantes activos (30 min)

Biblioteca de Anuncios de Meta. Filtro: país = México, categoría = todos, estado = activos.

Busca por: nombre genérico del producto (3 variantes), nombre de marca de los competidores conocidos, palabra del nicho.

Registra en tabla:

| Anunciante | Anuncios activos | Fecha del más antiguo | Días corriendo | Nº de creativos distintos | ¿Sitio propio o marketplace? |
|---|---|---|---|---|---|
| | | | | | |

Descarta del conteo: marketplaces grandes (Amazon, MercadoLibre, Temu) — esos son fondo del mercado, no competidores directos. Cuéntalos aparte, importan para precio.

**Índice de competencia (IC):**

```
IC = (anunciantes con +30 días corriendo) × 1,0
   + (anunciantes con 7-30 días) × 0,5
   + (anunciantes con <7 días) × 0,2
```

| IC | Lectura | Acción |
|---|---|---|
| 0-2 | Vacío. O es fase 1, o no hay mercado | Verificar demanda (`60`) antes de emocionarte |
| 3-8 | Corredor ideal | Entra con ángulo |
| 9-20 | Competido pero vivo | Solo con diferenciación fuerte (`65`) |
| +20 | Saturado | Ver `61`, considera otro mercado |

### Medición 2 — Inversión estimada de los competidores (10 min)

No hay dato público de gasto en Meta para anunciantes comerciales. Lo que sí se puede estimar, con honestidad sobre el error:

```
Gasto diario estimado ≈ (nº de creativos activos distintos) × (USD 15-40 por creativo)
```

Esa horquilla viene de que nadie mantiene creativos activos sin presupuesto mínimo. **Es una estimación gruesa, verificar**; sirve para ordenar competidores de grande a chico, no para decir "gasta USD 1.237/día".

| Creativos activos | Escala del competidor | Qué significa para ti |
|---|---|---|
| 1-3 | Está testeando | Puede morir en 2 semanas, no te intimides |
| 4-10 | Encontró algo | Es competencia real |
| 11-30 | Está escalando | Tiene mejor costo que tú; necesitas ángulo distinto |
| +30 | Operación grande | No compitas de frente; nicho lateral o mercado distinto |

### Medición 3 — Precio de mercado (5 min)

Toma 8 precios: 3 de anunciantes directos, 3 de MercadoLibre México, 1 de Amazon MX, 1 de Temu.

| Fuente | Precio MXN | Envío | Días de entrega |
|---|---|---|---|
| | | | |

Calcula: mediana, mínimo y el múltiplo que te permite tu costo.

```
Múltiplo disponible = mediana de mercado / tu costo puesto en bodega
```

Compara contra el mínimo de México: 3,74x conservador / 3,00x creativo bueno / 2,70x ganador real. Si el múltiplo disponible es 2,4x, el nicho no paga tu operación aunque el IC sea bajo. Para el cálculo exacto de márgenes invoca `Matematicas_lushows`.

## La tabla de veredicto (las 3 juntas)

| IC | Múltiplo disponible | Veredicto |
|---|---|---|
| 0-2 | >3,5x | Sospechoso: verifica que exista demanda (`60`) |
| 3-8 | >3,0x | 🟢 Entrar |
| 3-8 | 2,5-3,0x | 🟡 Entrar solo con bundle (`65`) |
| 9-20 | >3,0x | 🟡 Entrar solo con ángulo nuevo (`63`) |
| 9-20 | <3,0x | 🔴 No |
| +20 | cualquiera | 🔴 No, salvo mercado distinto |

## Medir el nicho, no solo el producto

Para un nicho completo (mascotas, cocina, belleza), repite la medición 1 con 5 productos representativos y promedia el IC. Un nicho con IC promedio de 25 es un nicho donde vas a pelear todo el tiempo; uno con IC promedio de 6 tiene aire. Esto importa porque el nicho es donde vas a construir la lista de clientes y el segundo producto, no el producto suelto.

## Errores de medición frecuentes

| Error | Consecuencia |
|---|---|
| Medir sin filtrar país | Ves 300 anunciantes de EE.UU. y descartas un nicho vacío en México |
| Contar anuncios en vez de anunciantes | Un solo competidor con 40 variantes parece 40 competidores |
| Incluir Temu/Amazon en el IC | Inflas el número; van aparte, en precio |
| Medir una sola vez | El dato que importa es la tendencia: mide hoy y dentro de 30 días |
| Ignorar TikTok | En 2026 los ganadores nacen ahí. Revisa también el Centro Creativo de TikTok |

## Frecuencia recomendada

| Situación | Cada cuánto medir |
|---|---|
| Antes de testear | Una vez, completo |
| Producto en test | Semanal, solo medición 1 |
| Producto escalando | Quincenal, las 3 |
| Temporada alta (Buen Fin, diciembre) | Semanal: todo se mueve rápido |

La mecánica fina de la Biblioteca de Anuncios y del Centro Creativo la maneja `facebook_ads_lushows` y `tiktok_ads_lushows`; aquí solo se usa para decidir qué anunciar.

## Relacionados

`60` demanda real · `61` saturación · `62` ciclo de vida · `63` temprano vs tarde · `65` diferenciación · `76` scorecard
