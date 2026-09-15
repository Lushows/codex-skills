# 24 — Exclusiones y solapamiento

**Solapamiento** (overlap) = cuando dos o más ad groups le apuntan a las mismas personas, y terminas pujando contra ti mismo en la subasta. **Exclusión** = sacar a propósito a un grupo de un ad group (a los compradores, por ejemplo). Lee este módulo cuando tengas varios ad groups corriendo, cuando tu CPA suba sin razón aparente, o cuando sospeches que le pagas dos veces por el mismo ojo. Es el módulo menos sexy y el que más plata salva — la mayoría de cuentas en LatAm sangran aquí sin notarlo.

## Por qué el solapamiento te cuesta plata

TikTok subasta cada impresión. Si dos ad groups tuyos quieren mostrarle a la MISMA persona, **compites contra ti mismo**: subes el precio de tu propia impresión en tu propia subasta. Síntomas:

- CPA que sube sin que cambiaras creativo ni oferta.
- Frecuencia alta concentrada en poca gente (delator silencioso).
- Dos ad groups "buenos" que juntos rinden peor que cualquiera solo.
- Gasto desigual: un ad group se come todo y el otro no entrega (la subasta interna lo asfixia).

En TikTok el riesgo es menor que en Meta porque Smart+ (ver 12) tiende a consolidar la entrega, pero aparece apenas armas estructuras manuales con audiencias que se cruzan: lookalikes solapados (ver 22), retargeting en escalera sin exclusiones (ver 23), o broad + interés del mismo nicho corriendo en paralelo. En 2026, con la plataforma empujando hacia Smart+ y menos ad groups, fragmentar a mano es nadar contra la corriente del propio sistema.

## Las exclusiones obligatorias

| Excluir | De dónde | Por qué |
|---|---|---|
| **Compradores** | Prospección y retargeting (ver 21, 23) | No le pagas a quien ya compró (salvo recompra/recurrente) |
| **Leads ya capturados** | Campañas de lead gen (ver 54) | No pagas por capturar el mismo lead dos veces |
| **Etapas más calientes** | Ad groups de etapas más frías | Que el "carrito abandonado" no compita con "visitó web" |
| **Engagers recientes** (a veces) | Prospección de FRÍO puro | Si quieres medir descubrimiento limpio, saca a los que ya te conocen |

La exclusión de **compradores** es la sagrada. Sin ella, en cada campaña le sigues mostrando a gente que ya pagó. Súbelos como lista de clientes hasheada (ver 28) o usa la audiencia de Shop/GMV de compradores (ver 21), y exclúyela en TODO ad group de adquisición. Excepción: negocios de recompra/recurrencia, donde el comprador es tu mejor audiencia, no exclusión (ver 25).

## Cómo evitar el solapamiento (reglas)

1. **No corras 4 lookalikes de la misma semilla** (1%, 2%, 3%, 5%). Se cruzan masivamente: el 1% está contenido dentro del 3%, que está dentro del 5%. Elige 1-2 (ver 22).
2. **Retargeting en escalera con exclusión descendente** (ver 23): cada ad group más frío excluye a todos los más calientes.
   - Carrito 1-7d → excluye compradores.
   - Visitó web 7-14d → excluye compradores + carrito.
   - Video viewers 95% → excluye compradores + carrito + web.
3. **Separa prospección (frío) de retargeting (tibio/caliente)** en campañas distintas, y excluye los tibios de la prospección si quieres medir descubrimiento puro (algunas cuentas prefieren NO excluirlos y dejar que Smart+ decida; prueba ambas en tu cuenta).
4. **Consolida en vez de fragmentar.** Smart+ rinde mejor con menos ad groups y más presupuesto cada uno que con 12 ad groups peleándose la misma gente. La fragmentación ES la causa más común de solapamiento, y en 2026 también es la que más penaliza la fase de aprendizaje (ver 13): cada ad group necesita ~50 conversiones para salir de aprendizaje, y 12 ad groups hambrientos nunca llegan.

## El test rápido de solapamiento

Si sospechas que dos ad groups se cruzan:

1. ¿Apuntan al mismo geo + edad + idioma? (probable cruce).
2. ¿Comparten semilla o interés? (cruce casi seguro).
3. ¿La suma de sus CPAs empeoró al lanzar el segundo? → solapamiento confirmado.
4. ¿La frecuencia se disparó en ambos al mismo tiempo? → señal clásica.

Solución: fusiona los dos ad groups en uno con presupuesto combinado, o añade exclusiones cruzadas. Casi siempre **fusionar gana** — menos fragmentación, más señal para el algoritmo, salida más rápida de aprendizaje (ver 13).

## No pagar dos veces: la mentalidad

Cada impresión cuesta. Cada vez que dos ad groups tuyos quieren el mismo ojo, encareces tu propia subasta sin darte nada a cambio. La estructura limpia es:

- **Pocos ad groups, bien alimentados** (3-5 creativos cada uno, ver 38) > muchos ad groups hambrientos.
- **Exclusiones explícitas** entre etapas y de compradores, revisadas cada mes.
- **Una semilla, un lookalike** (no cinco).

Esto le da al algoritmo señal concentrada (sale de aprendizaje más rápido, ver 13) y te evita el impuesto del solapamiento.

### Plantilla: matriz de exclusiones para una cuenta típica

| Campaña / AG | Incluye | Excluye |
|---|---|---|
| Prospección Broad | Ciudades + edad + idioma | Compradores (+ engagers si mides frío puro) |
| Prospección LAL | `LAL_compradores_2pct_CO` | Compradores |
| Retarget AG1 (carrito) | Carrito 1-7d | Compradores |
| Retarget AG2 (web) | Web 7-14d | Compradores + carrito |
| Retarget AG3 (VV) | VV 95% 7-30d | Compradores + carrito + web |

Revisa esta matriz cada 30 días: las listas de exclusión deben refrescarse o dejan entrar compradores nuevos a la prospección.

## Errores comunes — blacklist

1. **No excluir compradores de la prospección.** El error más caro y más común: le pagas a quien ya tienes.
2. **Cinco lookalikes solapados de la misma semilla.** Compites contra ti mismo; elige 1-2 (ver 22).
3. **Retargeting en escalera sin exclusión descendente.** El frío y el caliente pujan por la misma persona.
4. **Fragmentar en 12 ad groups creyendo que "controlas más".** Más fragmentación = más solapamiento + menos señal; consolida.
5. **No revisar la frecuencia.** Frecuencia alta concentrada delata solapamiento aunque no lo veas explícito en el panel.
6. **Excluir compradores cuando vendes recompra/recurrente.** La exclusión NO es universal: si tu negocio vive de la recompra, esos compradores son tu mejor audiencia (ver 25).
7. **Olvidar refrescar las listas de exclusión.** Una lista de compradores vieja deja entrar a clientes nuevos a la prospección.
8. **Pelear contra Smart+ con micro-fragmentación.** En 2026 el sistema premia la consolidación; 12 ad groups manuales es remar contra la marea.
