# 61 — Diagnóstico por capas

Lee este módulo cuando tu campaña no rinde y no sabes por dónde empezar, cuando el CPA subió y vas a "tocar todo" en pánico, o cuando quieras dejar de adivinar y arreglar la causa raíz. El error #1 del media buyer novato es mirar el CPA (caro) y subir la puja o cambiar el público — cuando casi siempre el problema está en otra capa. Diagnosticar es bajar por el embudo capa por capa y encontrar **exactamente dónde se cae la gente**. Una vez sabes la capa, el fix es obvio. Esto es lo que separa al que "le mueve cosas a ver qué pasa" del que opera con método.

## El embudo tiene 4 capas — revísalas en orden

No mires el CPA y reacciones. Baja por estas cuatro capas de arriba hacia abajo. La primera que esté mal es tu problema. Si arreglas una capa de abajo sin ver una rota arriba, pierdes tiempo y plata.

| # | Capa | Métrica que la delata | Si está mal, el problema es… |
|---|---|---|---|
| 1 | **Entrega / subasta** | CPM alto | Audiencia/subasta caras (público, época, puja) o creativo malo |
| 2 | **Hook (1-3s)** | Thumbstop / hook rate bajo | El **creativo** — el primer segundo no frena el dedo |
| 3 | **Hold (retención)** | 6s view / % visto bajo | El **creativo** — engancha pero aburre y la gente se va |
| 4 | **Conversión** | CTR o CVR baja | Oferta, landing o TikTok Shop |

Mnemónico: **CPM → Hook → Hold → CVR**. Empieza arriba siempre. La razón de bajar en orden es que **cada capa filtra a la siguiente**: si solo frena el 15% (hook roto), no importa cuán buena sea tu landing — casi nadie llega. Arreglar la landing con el hook roto es pintar una pared que se está cayendo.

## Capa por capa: síntoma → causa → fix

**Capa 1 — CPM alto (entrega/subasta).** Tu tarifa de entrada está cara. Causas y fixes:

- Audiencia muy chica o muy competida → amplía a broad (ver 20).
- Época cara (Q4, fechas comerciales) → es estacional, ajusta expectativas (ver 77).
- Creativo no-nativo → ojo: un creativo malo TAMBIÉN sube el CPM porque baja tu calidad/relevancia en la subasta (ver 01). Si el CPM está caro **Y** el thumbstop bajo, el culpable es el creativo, no la audiencia.
- Cuenta nueva / poca señal → dale tiempo de aprendizaje, no toques cada día (ver 13).
- Frequency alta → ya saturaste, el CPM sube porque le insistes a los mismos (ver 39).

**Capa 2 — Thumbstop bajo (hook).** La gente ve impresión pero NO frena. Es 100% creativo, el primer 1-3s.

- Hook débil, lento o genérico → reescribe el hook (ver 37). Prueba 3 hooks por ángulo.
- Primer frame parece "ad" (logo, producto en estudio) → arranca con persona/movimiento/texto-gancho, marca al final (ver 30, 31).
- Fix barato: el mismo video con 3 aperturas distintas suele cambiarlo todo.

**Capa 3 — Hold bajo (retención).** Frenan pero se aburren a los 4-8s. El hook prometió y el cuerpo no entregó.

- El video se desinfla después del gancho → mejora ritmo, cortes, payoff (ver 31, 33).
- Demasiado largo sin razón → recorta; la retención cae con el tiempo muerto.
- Promesa del hook no se cumple → alinea hook y contenido.

**Capa 4 — CTR o CVR baja (conversión).** Ven todo el video pero no actúan o no compran.

- CTR bajo (no hacen clic) → CTA débil o ausente, oferta poco clara. Pide la acción explícito (ver 38).
- CVR baja (clican pero no compran) → el problema NO es TikTok, es lo que pasa después del clic: landing lenta/confusa (rutea `desingweb-lushows`), oferta poco atractiva, fricción de pago, o Shop mal montado. También revisa que el píxel registre bien la conversión (ver 62) — una CVR "baja" puede ser medición rota, no venta perdida.

## Tabla de diagnóstico rápido (memorízala)

| Lo que ves | Capa rota | Acción inmediata |
|---|---|---|
| CPM caro + thumbstop bajo | Creativo (sube CPM) | Re-graba hook nativo (ver 37) |
| CPM caro + thumbstop OK | Subasta/audiencia | Amplía público / revisa época (ver 20, 77) |
| Thumbstop bajo | Hook | 3 hooks nuevos por ángulo (ver 37) |
| Thumbstop OK + hold bajo | Cuerpo del video | Recorta, mejora ritmo (ver 31) |
| Todo OK hasta CTR bajo | CTA/oferta | Pide la acción claro (ver 38) |
| CTR OK + CVR baja | Landing/Shop/oferta o medición | Revisa landing (`desingweb`) y píxel (ver 62) |
| CPA caro sin causa clara | Medición rota | Audita Events Manager primero (ver 62) |
| Todo OK pero ROAS feo | Margen/AOV | No es el ad: el ticket no aguanta (rutea `economist_lushows`) |

Antes de culpar al creativo o a la oferta por una conversión "cara", **confirma que la conversión se está midiendo bien** (ver 62). Muchas campañas "que no convierten" sí convierten — solo que el píxel no lo reporta.

## Ejemplo de triangulación de capas (caso real)

Un cliente de producto digital ($10.000 COP) dice "TikTok no me funciona, el CPA está en $25.000". Diagnóstico en orden:

1. **CPM** = $9.000 → sano, capa 1 OK. No toco audiencia.
2. **Thumbstop** = 41% → excelente, capa 2 OK. El hook no es el problema (no re-grabo).
3. **Hold** = 19% → bueno, capa 3 OK. El video retiene.
4. **CTR** = 2,1% → bueno. Clican.
5. **CVR** = 0,6% → **aquí está la fuga.** De cada 100 que clican, menos de 1 compra.

Conclusión: el creativo es oro, el problema vive después del clic. Antes de culpar la oferta, abro Events Manager (ver 62): el evento `CompletePayment` no aparece en Test Events, solo `PageView`. **La CVR no era 0,6% real — era medición rota.** Arreglado el evento, la CVR sube a 3,2% y el CPA cae a $7.800. Si hubiera reaccionado al CPA "subiendo la puja", habría quemado plata semanas. Esto es por qué se diagnostica antes de tocar.

## La regla de una variable

Cuando ya sabes la capa rota, cambia **una sola cosa** y espera señal (ver 13). Si tocas público + puja + creativo a la vez y el CPA mejora, no sabes cuál lo arregló — y no puedes repetirlo. El diagnóstico por capas solo sirve si después aíslas la variable. Esto se conecta con el aislamiento de pruebas creativas (ver 68) y con no resetear el aprendizaje (ver 13).

## Errores comunes — blacklist

- **Mirar el CPA y subir la puja.** El CPA es síntoma, no causa. Baja por las capas (ver 60).
- **Cambiar el público cuando el problema era el hook.** Tocas la capa equivocada. Diagnostica primero.
- **Tocar varias cosas a la vez.** Si cambias público + puja + creativo, no sabes qué funcionó. Una variable por vez.
- **Asumir que CVR baja = oferta mala.** A veces es el píxel sin medir (ver 62) o la landing lenta (`desingweb-lushows`).
- **Reaccionar diario sin dejar aprendizaje.** Mueves la cuenta antes de tener señal (ver 13).
- **Olvidar que un mal creativo sube el CPM.** Capa 1 y capa 2 se confunden; mira thumbstop para distinguir (ver 01).
- **No triangular la "no conversión".** Si backend SÍ muestra ventas pero TikTok no, es atribución/medición, no falta de ventas (ver 64).
- **Diagnosticar de abajo hacia arriba.** Arreglas la landing con el hook roto. Siempre de la capa 1 a la 4.
