# 28 — Datos propios (first-party)

**First-party data** (datos propios) = la información que TÚ recolectas directamente de tus clientes: correos, teléfonos, compras, de tu CRM o tu tienda. **Hashear** = convertir esos datos en un código irreversible (SHA-256) antes de subirlos, para que TikTok los cruce con sus usuarios sin ver el dato real. Lee este módulo cuando quieras subir tu lista de clientes a TikTok para excluirlos, retenerlos o crear lookalikes. En el mundo **post-cookie** (sin rastreo de terceros), tus datos propios son el activo de pauta más valioso que tienes — y casi nadie en LatAm lo usa, lo que te da ventaja.

## Por qué los datos propios son el activo post-cookie

Las cookies de terceros (que rastreaban al usuario por toda la web) ya están muriendo por privacidad y regulación (ver 29), y en 2026 el rastreo cross-site es cada vez más limitado por navegadores y sistemas operativos. El Pixel sigue, pero **pierde señal** por bloqueadores, restricciones de iOS y falta de consentimiento. Lo que NO depende de cookies es lo que el cliente te dio directo: su correo y teléfono cuando compró. Eso es first-party, es tuyo, y TikTok lo cruza con sus usuarios vía **Customer Match / Customer File** (lista de clientes, ver 21).

Quien tiene una base limpia de clientes con consentimiento tiene una ventaja que el competidor sin CRM **no puede comprar a ningún precio**. Esa base alimenta exclusiones, lookalikes y retención, y resiste el deterioro del Pixel. Es, literalmente, el único dato de targeting que mejora con el tiempo mientras todo lo demás se degrada.

## Los tres usos (en orden de valor)

| Uso | Qué hace | Valor |
|---|---|---|
| **Exclusión** | Saca a tus compradores de la prospección (ver 24) | Alto e inmediato: dejas de pagarle a quien ya compró |
| **Lookalike** | Semilla de tus mejores clientes para encontrar similares (ver 22) | Alto: la semilla más fuerte que existe son compradores reales |
| **Retención / recompra** | Audiencia directa para upsell, recompra, fidelidad (ver 25) | Alto si tu negocio es recurrente; nulo si es pago único sin recompra |

Para GastroLatam (calculadora pago único, ver CLAUDE.md): el comprador no recompra el mismo producto, así que los usos clave son **exclusión** (no pautarle al que ya pagó) y **lookalike** (semilla premium para encontrar más dueños de restaurante parecidos). La retención entra en juego solo si GastroLatam saca un segundo producto.

## Tamaños mínimos y calidad

- **Tamaño mínimo útil**: ~1.000 registros que hagan match para que TikTok active la audiencia. Listas más chicas no entregan o entregan caro.
- **Tasa de match**: no todos tus correos/teléfonos están en TikTok con el mismo dato (alguien se registró con otro correo, otro teléfono). Espera que solo un % haga match — a veces 40-70%. Por eso necesitas volumen: para tener 1.000 en match quizás debas subir 2.000.
- **Calidad > cantidad**: para lookalike, sube tus MEJORES clientes (top por gasto/recompra), no todos. Una semilla de 1.000 compradores premium vence a 10.000 mezclados con curiosos y devoluciones.
- **Formato**: teléfonos en E.164 (+57300...), correos en minúscula sin espacios. TikTok hashea al subir; aun así, sube limpio para maximizar el match. Un teléfono sin código de país o un correo con mayúsculas baja tu tasa de match.

## Cómo subir la lista (acciones exactas)

1. Exporta de tu CRM/tienda: correos y teléfonos de compradores (separa "premium" / top por gasto en un archivo aparte si tu CRM lo permite).
2. Limpia: minúsculas, sin espacios, teléfonos con +57 y código de país en E.164. Un Excel con `=MINUSC()` y formato de texto basta.
3. Tools → Audiences → Create audience → **Customer file**.
4. Sube el CSV. TikTok lo hashea (SHA-256) en el navegador — el dato crudo no viaja en claro si usas el flujo oficial.
5. Nombra claro: `clientes_compradores_CO_2026` / `clientes_premium_CO`.
6. Espera a que procese y muestre tamaño/match. Si el match sale muy bajo (< 20%), revisa formato antes de culpar a la lista.
7. Úsala: como **exclusión** en prospección (ver 24) y como **semilla** de lookalike (ver 22).
8. **Refresca cada 1-3 meses** subiendo lista nueva; las viejas dejan entrar clientes recientes a la prospección y degradan los lookalikes.

### Plantilla: columnas mínimas del CSV

| email | phone |
|---|---|
| juan.perez@gmail.com | +573004183337 |
| maria@hotmail.com | +573159876543 |

Una columna de email, una de teléfono. Más datos no hacen falta para Customer Match. Cada fila, un cliente con consentimiento.

## El requisito que NO es opcional: consentimiento

Subir datos de personas a una plataforma publicitaria está regulado. En Colombia aplica **Habeas Data** (Ley 1581 de 2012, vigila la SIC); en Brasil, **LGPD** (vigila la ANPD); en México, la LFPDPPP (ver 29 para el detalle). Antes de subir:

- Debes tener **autorización** del titular para tratar sus datos con fines de marketing (la casilla/aviso al momento de la compra o registro, NO pre-marcada).
- No subas datos **sensibles** (salud, orientación, religión, datos de menores).
- Documenta de dónde salió el consentimiento (sabes qué cliente autorizó y cuándo).

Cumplir esto no es burocracia: una multa de la SIC en Colombia o una queja te cuesta más que toda la campaña. Y subir datos sin consentimiento puede costarte la **cuenta publicitaria** completa. Hazlo bien desde el día uno (ver 29). Si dudas del encuadre legal de cómo capturas datos, valida viabilidad con `economist_lushows` y, para temas legales finos, un abogado real.

## Errores comunes — blacklist

1. **No tener CRM ni capturar datos.** Sin base propia no tienes el activo post-cookie; empieza a capturar correo/teléfono en cada venta YA.
2. **Subir una lista de 80 personas.** Por debajo de ~1.000 con match, TikTok no activa la audiencia.
3. **Subir todos los clientes para lookalike.** La semilla premium (top por gasto) vence a la lista completa mezclada.
4. **Formato sucio.** Teléfonos sin +57, mayúsculas, espacios → match bajo → audiencia inútil.
5. **No refrescar.** Listas viejas dejan entrar compradores recientes a la prospección y degradan los lookalikes (ver 22).
6. **Subir sin consentimiento Habeas Data/LGPD.** Riesgo legal real y riesgo de perder la cuenta (ver 29).
7. **Subir datos sensibles.** Prohibido y peligroso; solo correo y teléfono de marketing autorizado.
8. **Asumir 100% de match.** Solo un % de tus contactos hace match; sube con volumen suficiente para que el match útil llegue a ~1.000.
