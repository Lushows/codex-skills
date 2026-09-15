# 22 — Lookalikes en TikTok

Un **lookalike** (público similar) es una audiencia que TikTok arma buscando gente parecida a una **semilla** tuya (tus compradores, por ejemplo). Lee este módulo cuando quieras escalar prospección con algo más dirigido que broad puro, o cuando tu semilla sea lo bastante buena para valer la pena. La verdad incómoda primero: en la era **Smart+** (ver 12), un buen creativo sobre broad (ver 20) suele igualar o ganarle al lookalike. El lookalike no es magia; es una **semilla buena multiplicada** — y si la semilla es basura, multiplicas basura a escala. Entra a este módulo sabiendo que el lookalike es una herramienta, no un atajo.

## Cuándo el lookalike SÍ aporta

| Situación | ¿Lookalike? | Por qué |
|---|---|---|
| Tienes ≥ 1.000 compradores reales como semilla | Sí, vale probarlo | Semilla fuerte = el algoritmo aprende un patrón nítido |
| Producto de nicho donde broad trae mucha basura | Sí | El lookalike acota sin que apiles intereses a mano |
| Apenas tienes 50 visitantes y 0 compras | No | Semilla pobre; broad + creativo rinde más |
| Ya escalaste broad y quieres otra fuente paralela | Sí, como ad group adicional | Diversificar de dónde sale el volumen reduce riesgo |
| Tienes lista de clientes premium (top por gasto) | Sí, prioritario | La mejor semilla que existe para ticket alto |

Regla 2026: **el lookalike compite contra broad, no lo reemplaza.** Córrelos en paralelo, mismos creativos, y deja que el CPA decida. Con Smart+ empujando el targeting amplio, muchas cuentas descubren que el lookalike apenas empata broad — y si empata, broad gana por simplicidad (menos mantenimiento, menos solapamiento, ver 24).

## Calidad de semilla: la jerarquía que importa

El resultado del lookalike depende casi 100% de la semilla. De mejor a peor:

1. **Compradores** (Shop/GMV o lista de clientes, ver 21, 28) — la mejor. Gente que pagó plata real.
2. **Clientes de alto valor** (top 25% por gasto, si tu CRM lo permite) — semilla premium para ticket alto o para encontrar a los que más gastan.
3. **Leads que convirtieron** (no todos los leads: los que compraron después; un lookalike de leads basura te trae más leads basura).
4. **Add-to-cart / iniciaron checkout** — intención fuerte aunque no compraron; buena semilla si aún no acumulas compras.
5. **Video viewers 95-100%** — tibios; semilla aceptable de arranque si no tienes compras todavía.
6. **Visitantes de web genéricos / todos los engagers** — la más débil; casi broad disfrazado, no esperes magia.

Nunca uses como semilla "todos los que vieron 2 segundos de un video": es ruido puro. Mínimo de semilla útil: ~1.000 personas que hagan match; por debajo, el patrón es inestable y el lookalike sale errático. Si solo tienes 200 compradores, no fuerces el lookalike — sigue con broad hasta acumular semilla.

## Porcentaje según tamaño de mercado

El lookalike se define por amplitud: 1% (más parecido, más chico) hasta 10% (más amplio, más lejano de la semilla). Ajusta al tamaño del mercado:

| Mercado | % sugerido | Razón |
|---|---|---|
| Colombia / Perú / Chile (país completo) | 1-3% | Población suficiente para que 1-2% ya dé volumen |
| Una sola ciudad (Bogotá, Lima, Medellín) | 3-5% | El pool es chico; 1% se queda sin gente para entregar |
| LatAm multipaís | 1-2% | Mucho pool; quédate cerca de la semilla |
| Nicho B2B en un país (ver 27) | 5-10% o mejor broad+creativo | Tan pocos que el % alto o el broad rinden más |

Empieza estrecho (1-2%) si tienes semilla fuerte; amplía solo si te quedas sin entrega o el CPA aguanta al subir el %. Subir de 1% a 5% sin razón solo diluye la semilla hacia algo cada vez más parecido a broad — si vas a terminar en broad, ahórrate el lookalike.

## Mantenimiento: refrescar la semilla

Una semilla envejece. "Compradores de hace 8 meses" ya no refleja a tu cliente de hoy si cambiaste producto, precio u oferta. Reglas:

- **Refresca la semilla cada 1-3 meses** subiendo lista nueva o dejando que Shop/GMV la actualice solo (esas se mantienen vivas sin que toques nada).
- Si cambiaste de oferta o subiste el precio, **rehaz la semilla** con compradores de la oferta nueva: el cliente que compró a $10.000 COP no es idéntico al que compra a $50.000.
- No acumules 5 lookalikes solapados (1%, 2%, 3% de la misma semilla compitiendo entre sí); te canibalizan la subasta (ver 24). Elige 1-2 y déjalos correr con presupuesto decente.

## Cómo crearlo (acciones exactas)

1. Tools → Audiences → Create audience → **Lookalike audience**.
2. Source: elige tu semilla (compradores > add-to-cart > video viewers, ver arriba).
3. Location: el país/región donde entregas (ver 26). Un lookalike "global" sobre semilla colombiana no tiene sentido si solo despachas en Colombia.
4. Audience size: empieza en 1-2% para Colombia; sube si necesitas volumen.
5. Nómbralo claro: `LAL_compradores_2pct_CO`.
6. Úsalo en un ad group de prospección SEPARADO de tu broad, con los mismos 3-5 mejores creativos (ver 38), para que el A/B sea limpio (misma creatividad, distinta fuente de audiencia).
7. **Excluye compradores también del lookalike** (ver 24): un lookalike incluye, por construcción, gente que ya te compró si no la sacas — terminarías pagando por volverle a vender.

### Plantilla: test broad vs. lookalike

| AG | Fuente | Creativos | Presupuesto/día | Juzga a los |
|---|---|---|---|---|
| AG-Broad | Ciudades + edad + idioma | 5 ángulos | $40.000 COP | 7-14 días / 50 conv |
| AG-LAL-2% | `LAL_compradores_2pct_CO` (excl. compradores) | mismos 5 ángulos | $40.000 COP | 7-14 días / 50 conv |

Mismos creativos, misma plata, mismo periodo. Gana el del CPA/ROAS mejor; si empatan, quédate con broad por simplicidad.

## Errores comunes — blacklist

1. **Semilla de "todos los que vieron 2s".** Ruido multiplicado; el lookalike sale tan malo como su semilla.
2. **Esperar que el lookalike le gane a broad porque "es más avanzado".** En Smart+ broad+creativo suele empatar o ganar. Compite, no reemplaza.
3. **Usar 1% en una sola ciudad.** Te quedas sin gente para entregar; sube a 3-5% en mercados chicos.
4. **Crear 5 lookalikes solapados de la misma semilla.** Se canibalizan en la subasta; elige 1-2 (ver 24).
5. **No refrescar la semilla.** Compradores de hace un año ya no representan a tu cliente actual.
6. **No excluir compradores del lookalike.** Le vuelves a vender a quien ya pagó.
7. **Hacer lookalike con 50 personas de semilla.** Patrón inestable; necesitas ~1.000 mínimo. Sin eso, usa broad.
8. **Probar lookalike con creativos distintos a los del broad.** Entonces no sabes si ganó la audiencia o el video; iguala la creatividad para un A/B limpio.
