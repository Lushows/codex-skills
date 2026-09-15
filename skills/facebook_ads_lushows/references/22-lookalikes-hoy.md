# 22 — Lookalikes hoy

Un **lookalike** (LAL, "público similar") es una audiencia que Meta construye buscando gente parecida a una **semilla** que tú le das (ej: tus compradores). Se crea en Audiences → Create → Lookalike audience. Lee este módulo cuando te preguntes si vale la pena montar LALs en jun-2026 — la respuesta honesta: **menos central que antes, pero no muerto**, y con casos donde sigue siendo el atajo correcto.

## Su rol HOY (jun-2026)

En la era Andromeda + GEM + Advantage+ audience (ver 20, 92), el broad ya hace internamente lo que el LAL hacía a mano: el sistema usa tu señal de Dataset/CAPI para encontrar gente parecida a tus compradores, sin que crees nada. Por eso en cuentas grandes con buena señal (EMQ 8+, ver 14), el LAL suele empatar o perder contra broad — es trabajo duplicado.

Dónde SÍ sigue siendo útil:
- **Cuentas medianas** ($1M-12M COP/mes ≈ $300-3.000 USD) con señal decente pero no enorme: el LAL le da al sistema un atajo.
- **Países/ciudades pequeños**: en mercados chicos el broad explora menos eficiente; un LAL 1% acota bien.
- **Arrancar señal**: cuenta nueva con Dataset virgen pero una customer list de cientos de compradores (ver 28) — el LAL traduce ese activo en targeting desde el día 1. Es el caso más claro: convierte tu activo de datos en pauta antes de que el píxel acumule historia.
- **Cuentas que vienen de un ban o reseteo** y necesitan reconstruir señal rápido (ver 93).
- **Post-cookie / first-party**: con cookies muriendo, tu **Customer Match** (lista hasheada) se vuelve la semilla más confiable que tienes — vale más en 2026 que en 2022 precisamente porque no depende del navegador (ver 28).

## Semillas: las que funcionan y las que no

En orden de potencia (la regla: la semilla debe parecerse a la ACCIÓN que quieres, no a la atención):

1. **Compradores con valor (value-based LAL)**: subes la lista o usas el evento Purchase con valor; Meta pondera por cuánto gastó cada uno. Busca parecidos a tus MEJORES clientes, no al promedio. La mejor semilla que existe si tienes 100+ compradores con valor.
2. **Compradores** (evento Purchase 180d o customer list de clientes).
3. **Leads calificados** (no todos los leads: los que agendaron, respondieron en WhatsApp o pasaron tu filtro).
4. **Top 25% por tiempo en sitio** (website custom audience por percentil) — sorprendentemente buena cuando no tienes compras suficientes.

Semillas flojas (evítalas): page likes (incluye bots y familiares), engagers genéricos (likes baratos ≠ compradores), video viewers de 3s, listas compradas (además ilegal y patrón de baneo, ver 29). Garbage in, garbage out: un LAL de gente que NO compra te trae más gente que no compra, con precisión quirúrgica.

Tamaño de semilla: mínimo técnico ~100 personas del mismo país; útil de verdad desde 500-1.000. Con menos, el parecido es ruido. Y un detalle 2026: la semilla también necesita **consentimiento demostrable** (Data Source Declaration, ver 29) — una customer list sin autorización de publicidad puede quedar inelegible como semilla.

## Porcentajes: qué significa 1% vs 10%

El % es qué tan parecida es la audiencia: **1% = el 1% de la población del país más parecido a tu semilla** (máxima precisión), 10% = el 10% más parecido (máximo alcance, menos precisión).

- En **Colombia** (≈ 35-40M usuarios de Meta en 2026): 1% ≈ 350-400 mil personas — cientos de miles, suficiente para campañas chicas y medianas.
- En **México** (≈ 90M+): 1% ≈ ~900k — alcance enorme con precisión alta; ahí el LAL 1% rinde mucho.
- Usa **1-3%** cuando buscas precisión (presupuesto chico, producto nicho).
- Usa **5-10%** cuando buscas alcance (escalando, ciudad/país pequeño donde el 1% se agota rápido).

| País | Usuarios Meta aprox | 1% ≈ | Cuándo subir de % |
|---|---|---|---|
| Colombia | 35-40M | 350-400k | al escalar o en ciudad sola |
| México | 90M+ | ~900k | rara vez; 1-2% basta mucho tiempo |
| Perú | 24M | ~240k | antes (mercado más chico) |
| Chile | 14M | ~140k | pronto; usa 2-5% |

**Stacking de LALs**: en vez de un ad set por porcentaje (anti-patrón de fragmentación, ver 10), agrupa 1% + 2% + 5% (o 1-10%) EN EL MISMO ad set. Consolidas conversiones, el sistema decide dentro del rango, y no compites contra ti mismo en la subasta.

## Testing honesto: LAL vs broad

No asumas — mide en tu cuenta:

1. Misma campaña o dos ad sets ABO con presupuesto idéntico: **Ad set A = broad** (solo geo+edad), **Ad set B = LAL stack** (1-5% de compradores). MISMOS creativos en ambos.
2. Corre 7-14 días o hasta ~50 conversiones por ad set, con **ventana 7d-click/1d-view** (recuerda: view-through fuera del API desde 12-ene-2026, ver 16).
3. Gana el de mejor **CPA/ROAS**, no el de mejor CTR ni CPM. Un LAL con CPM 30% más caro puede igual perder aunque "se sienta más preciso".
4. Veredicto típico jun-2026: broad gana o empata en la mayoría; si tu LAL gana claro, quédatelo y re-testea cada 2-3 meses (la ventaja se erosiona a medida que tu Dataset acumula señal).

Mantenimiento: los LAL de customer list NO se actualizan solos — re-sube la lista mensual o conecta el CRM (ver 96). Los LAL de eventos del Dataset sí se refrescan automáticamente.

## Receta: value-based LAL paso a paso

1. Exporta tus compradores con columna `value` (total gastado por cliente, en COP) — formato en 28.
2. Audiences → Create → Custom audience → Customer list → marca "incluye una columna de valor de cliente".
3. Sube el CSV, mapea las columnas (email, phone con +57, value), espera el match (horas). Espera match rate 40-70% en LatAm (ver 28).
4. Audiences → Create → Lookalike → fuente: esa lista value-based → país: Colombia → tamaño: 1% (o rango 1-5% para stacking).
5. Métela al test contra broad (sección anterior). No la declares ganadora por fe.

Alternativa sin CSV: si tu Dataset/CAPI ya manda `Purchase` con `value` (ver 14), puedes crear el LAL value-based directo desde el evento — se actualiza solo, mejor a largo plazo.

Conexión con Minimum ROAS / ROAS Goal (ver 15): si vas a optimizar por valor con la puja de ROAS, una semilla value-based alinea targeting y puja hacia tus clientes rentables, no hacia el comprador promedio.

## Árbol de decisión: ¿uso LAL o no?

Decide rápido sin teología:

1. ¿Tienes 500+ compradores con valor en lista o evento? **No** → usa broad, sigue capturando datos (ver 28). **Sí** → paso 2.
2. ¿Tu Dataset ya manda 50+ Purchases/semana con EMQ 8+? **Sí** → el broad probablemente ya replica al LAL; testéalo pero no esperes milagro. **No** → paso 3.
3. ¿Cuenta nueva / post-ban / mercado chico / arrancando señal? **Sí** → el LAL es tu atajo, móntalo value-based 1-3% y stackea. **No** → testéalo contra broad y que gane el CPA.

Regla de bolsillo jun-2026: **el LAL es un puente, no un destino**. Sirve mientras tu señal de conversión madura; cuando el Dataset tiene historia, el broad lo alcanza. Por eso lo re-testeas cada trimestre en vez de dejarlo encendido por fe.

## Tabla resumen: semilla → calidad → uso

| Semilla | Calidad | Cuándo usarla |
|---|---|---|
| Compradores con valor | ★★★★★ | siempre que tengas 100+; mejor a largo plazo desde evento |
| Compradores (sin valor) | ★★★★ | si no tienes columna `value` aún |
| Leads calificados | ★★★ | servicios/B2B con filtro real (ver 27) |
| Top 25% tiempo en sitio | ★★★ | sin compras suficientes todavía |
| Engagers/likes/video 3s | ★ | evítalas: clones de curiosos |

## Errores comunes — blacklist

- LAL de page likes o engagers de sorteos: clones de curiosos, no de compradores.
- 5 ad sets: LAL1%, LAL2%, LAL3%, LAL5%, intereses — fragmentación pura; consolida en 1-2 (ver 10 y 24).
- Semilla de 60 personas: matemáticamente válido para Meta, estadísticamente ruido. Junta más datos primero (usa broad mientras).
- Excluir la semilla del LAL y de paso olvidar excluir compradores en prospecting: son dos exclusiones distintas (ver 24).
- Declarar "los LAL ya no sirven" o "los LAL son lo mejor" sin haber corrido el test en TU cuenta este trimestre.
- LAL internacional con semilla colombiana para "expandir a México": el parecido cruza mal entre países; haz semilla y LAL por país (ver 26).
- Semilla de customer list sin consentimiento de publicidad: inelegible bajo la Data Source Declaration (ver 29).
- Olvidar re-subir la lista: a los 3 meses tu LAL aprende de clientes fantasma y nuevos compradores no entran a la semilla.
