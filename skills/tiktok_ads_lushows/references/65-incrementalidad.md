# 65 — Incrementalidad

Lee este módulo cuando sospeches que tus ventas "atribuidas" ya iban a pasar igual, cuando tu retargeting muestre un ROAS espectacular y quieras saber si es real, o antes de meterle más plata a una campaña que quizás solo le está cobrando crédito a ventas tuyas. La pregunta de la incrementalidad es la más honesta de todo el marketing: **¿esa venta la causó el anuncio, o ya iba a comprar de todas formas?** El ROAS no contesta eso (ver 64). La incrementalidad sí. Y es donde más plata se desperdicia sin que nadie lo note.

## La pregunta de la incrementalidad

**Incremental** = la venta que NO habría ocurrido sin el anuncio. **No incremental** = la venta que igual ibas a tener (alguien que ya te buscaba, un cliente fiel que iba a recomprar). La fórmula conceptual:

```
Lift incremental = ventas del grupo expuesto − ventas del grupo de control (holdout)
ROAS incremental = (ingreso incremental) ÷ gasto
```

El caso clásico: el **retargeting** (anuncios a gente que ya visitó tu web). Le muestras el ad a alguien que ya iba a comprar mañana. Compra hoy. TikTok se acredita la venta. ROAS altísimo. Pero esa venta **no era incremental** — la pagaste sin necesidad. El retargeting siempre se ve bien y a menudo es el menos incremental.

| Tipo de campaña | Suele verse | Incrementalidad real |
|---|---|---|
| Retargeting calientes | ROAS altísimo | Baja (te robas crédito de ventas tuyas) |
| Prospección broad (gente nueva) | ROAS más bajo | Alta (trae clientes que no tenías) |
| Marca / awareness | ROAS feo | Variable (mide con lift, no con ROAS) |

Verdad incómoda: la campaña con el ROAS más bonito (retargeting) suele ser la menos incremental, y la del ROAS más feo (prospección) suele ser la que de verdad crece el negocio. Por eso no se decide solo por ROAS (ver 64). Esto conecta con el frame del bloque: **TikTok es descubrimiento** (ver 60) — su mayor valor está en traer gente nueva, justo donde el ROAS de panel se ve peor.

## Cómo medirla: tres niveles

No necesitas un PhD. Hay versiones caseras y baratas para Colombia/LatAm.

| Método | Qué es | Para quién | Confiabilidad |
|---|---|---|---|
| **Lift test** | TikTok divide la audiencia: a un grupo le muestra el ad, a otro (holdout) no, y compara | Cuentas con volumen | Alta |
| **Holdout casero** | Apagas una campaña/segmento un periodo y ves si las ventas totales caen | Cualquiera | Media |
| **Geo-lift casero** | Pautas en unas ciudades y en otras no; comparas ventas por región | Negocios con varias zonas | Media-alta |

**Lift test (el formal):** TikTok ofrece *conversion lift studies*. Toma un grupo de control (holdout) que NO ve tus ads y compara su tasa de conversión contra los que sí. La diferencia es el lift = lo verdaderamente incremental. Requiere volumen para ser confiable (típicamente miles de conversiones en la ventana).

**Holdout casero (el del día a día):** apaga el retargeting una semana. Mira el negocio TOTAL (no el panel de TikTok): ¿las ventas totales cayeron lo que el panel decía que aportaba el retargeting? Si las ventas casi no se movieron, ese ROAS era humo. Esto se cruza con el MER (ver 64): **si apagas una campaña y el MER no empeora, no era incremental.**

**Geo-lift casero:** enciende TikTok en unas ciudades y mantenlo apagado en otra de mercado parecido. Compara crecimiento de ventas por región (breakdown geográfico, ver 63). Barato y sorprendentemente revelador.

## Ejemplo numérico de holdout

Negocio que gasta $1.000.000/mes en retargeting. El panel dice que ese retargeting "genera" $5.000.000 (ROAS 5x). Pruebas:

| Semana | Retargeting | Ventas totales del negocio (banco) |
|---|---|---|
| 1–2 (con retargeting) | ON | $11.000.000 |
| 3–4 (holdout) | OFF | $10.600.000 |

Diferencia al apagarlo: solo **$400.000** menos de ventas, no los $5.000.000 que el panel atribuía. El ROAS incremental real del retargeting = $400.000 ÷ $500.000 (gasto de 2 semanas) ≈ **0,8x** — ¡estabas perdiendo plata en lo que parecía tu mejor campaña! Esos $5M que el panel se acreditaba eran ventas que pasaban igual. Decisión: bajar el retargeting a un mínimo (recuperar carritos reales) y mover el grueso a prospección.

## Geo-lift: cómo leerlo

| Ciudad | TikTok | Ventas mes anterior | Ventas mes prueba | Δ |
|---|---|---|---|---|
| Medellín | ON | $3.0M | $3.9M | +30% |
| Cali | ON | $2.5M | $3.2M | +28% |
| Barranquilla (control) | OFF | $2.4M | $2.5M | +4% |

El +4% de Barranquilla es el crecimiento "natural" (orgánico, estacional). El lift atribuible a TikTok ≈ 30% − 4% = **~26% incremental**. Eso sí es plata que el ad causó. Requiere mercados parecidos para que la comparación valga.

## Qué hacer con el resultado

1. Si el holdout muestra que el retargeting NO era incremental → bájalo o quítalo, mueve esa plata a prospección (ver 20). No lo elimines a ciegas: un mínimo de retargeting sí recupera carritos reales; busca el punto donde deja de ser incremental.
2. Si la prospección broad SÍ es incremental aunque su ROAS de panel se vea feo → es tu motor de crecimiento, protégela al escalar (ver 72).
3. Lleva la conclusión al modelo de negocio → **rutea a `economist_lushows`** para que el CAC incremental entre en el cálculo de viabilidad y cuánto puedes pagar por cliente. El nCAC honesto (ver 64) usa ventas incrementales, no atribuidas.

Frecuencia sensata: un holdout casero cada 1–2 meses basta para no engañarte. No vivas haciendo tests; hazlos cuando vayas a tomar una decisión grande de presupuesto. La incrementalidad aplica igual cruzando canales — si pautas también en Meta (`facebook_ads_lushows`) o Google (`google_ads_lushows`), el holdout te dice cuál canal de verdad suma y cuál solo se cuelga del crédito de otro.

## Errores comunes — blacklist

- **Tratar el ROAS del retargeting como ganancia real.** Suele ser el menos incremental; te cobras tus propias ventas (ver 64).
- **Escalar prospección o cortarla solo por su ROAS de panel.** Mide su incrementalidad; ahí está el crecimiento real.
- **No hacer nunca un holdout.** Vives sin saber qué pagas de más. Apaga algo una semana y mira el MER.
- **Geo-lift comparando ciudades muy distintas.** Compara mercados parecidos o el dato no sirve.
- **Lift test con poco volumen.** Sin tamaño de muestra, el resultado es ruido. Usa holdout casero si eres chico.
- **Matar TODO el retargeting de golpe.** Algo sí recupera carritos reales; busca el punto incremental, no cero.
- **No descontar el crecimiento orgánico en el geo-lift.** El control te da la línea base; réstala siempre.
- **No llevar el CAC incremental al modelo.** El número honesto va a `economist_lushows`, no se queda en el panel.
