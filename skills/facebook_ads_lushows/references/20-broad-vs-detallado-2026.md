# 20 — Broad vs. detallado en 2026

"Targeting" es a quién le muestras tus anuncios. **Broad** = solo defines geografía y edad, y dejas que Meta encuentre al comprador. **Detallado** = tú eliges intereses, comportamientos y demografía a mano. Lee este módulo cuando estés decidiendo cómo segmentar una campaña nueva o cuando vengas de la escuela vieja de "apilar intereses" y tus CPAs ya no cuadren. La respuesta corta de jun-2026: **broad gana en la mayoría de las cuentas**, y aquí está el porqué, los números y las pocas excepciones reales.

## Por qué cambió la era

Antes (2017-2021) el media buyer ganaba eligiendo intereses precisos. Hoy el sistema de Meta —con **Andromeda** (motor de retrieval, rollout global terminado ~oct-2025) y **GEM** encima (Generative Ads Recommendation Model, paper nov-2025, ver 92)— predice quién va a comprar usando dos señales mucho más ricas que tus intereses manuales:

1. **El creativo**: Meta analiza tu video/imagen/texto y lo muestra primero a gente parecida a la que reaccionó a anuncios similares. Tu anuncio ES tu targeting.
2. **La señal de conversión** (Dataset = píxel + CAPI, ver 14/28): cada compra que reporta tu sitio o tu CRM le dice al sistema "más gente como esta". Con EMQ 8+ esta señal pesa más que cualquier interés.

Resultado: los intereses manuales ("yoga", "emprendimiento") son una foto borrosa de 2015 del usuario; la señal de conversión es su comportamiento real de ayer. GEM además evalúa el anuncio dentro del **journey completo** del cliente, no aislado — micro-segmentar por intereses no solo es inútil, es contraproducente porque le quitas datos al modelo. Por eso el **detailed targeting es cada vez más residual** en el producto: Meta lo va arrinconando versión tras versión.

## Advantage+ audience: tu targeting es una sugerencia

Tras el overhaul de creación de campañas (~feb-2026) ya **no eliges "Manual vs Advantage+"**: hay un solo flujo con toggles Advantage+ **encendidos por default** por sección, y haces **opt-out** si quieres control (ver 90). En audiencia eso significa **Advantage+ audience** por defecto: lo que configuras NO es un límite duro sino una **sugerencia**. Meta arranca mostrando a tu audiencia sugerida y se **expande** fuera de ella si encuentra conversiones más baratas afuera. Solo geografía y edad mínima son restricciones reales (la edad mínima según el modo/categoría).

Implicaciones prácticas:
- Poner 10 intereses en Advantage+ audience ≈ ponerle un punto de partida, no una cerca. No te asustes si el breakdown muestra gente "fuera" de tu interés — es el diseño.
- Si NECESITAS una cerca dura (caso raro: categorías especiales HEC/financiero que prohíben lookalikes y radio, ver actualizacion-2026 §10), el sistema te obliga a la audiencia original/manual y te quita features. No es tu decisión: es regulatoria.

## Cuándo el detallado AÚN sirve

| Caso | Por qué | Cómo |
|---|---|---|
| Nicho muy específico + presupuesto chico (< $40-60k COP/día) | Con poca plata, broad puede tardar semanas en encontrar la señal | 1 ad set con 1-3 intereses gruesos del nicho como sugerencia |
| B2B pyme (ver 27) | El comprador es el 0.5% de la población; el creativo filtra, pero un empujón de intereses de industria acelera | Intereses de herramientas/industria (Alegra, Siigo, Fenalco) + creativo que auto-filtra |
| Forzar exploración de un segmento | Quieres validar si "mamás 25-34" responde a un ángulo concreto | Ad set ABO temporal con ese segmento, presupuesto fijo, 1-2 semanas, luego se consolida |
| Categoría con restricción legal real (licores, financiero) | Obligación, no optimización | Edad mínima + exclusiones requeridas; financiero pierde radio y lookalikes |

Fuera de eso: broad. En LatAm con e-com de ticket medio, leads a WhatsApp o servicios locales, broad + buen creativo gana el A/B contra intereses en la mayoría de cuentas (no en el 100% — pruébalo en TU cuenta, sección de testing más abajo).

## Cómo migrar de detallado a broad sin sustos

NUNCA apagues lo que funciona para "cambiarte a broad" de un día para otro. Receta:

1. **Semana 0**: deja tus ad sets de intereses corriendo igual.
2. **Crea en paralelo** 1 ad set broad (solo país/ciudades + edad 22-55 o la tuya) con tus 4-6 MEJORES creativos probados (no creativos nuevos: estarías testeando dos cosas a la vez).
3. **Presupuesto**: dale al broad el 30-40% del total, sin tocar lo demás (sube el total temporalmente si hace falta).
4. **Espera 7-14 días** o ~50 conversiones en el broad (fase de aprendizaje, ver 13). No juzgues al día 2.
5. **Compara CPA/ROAS** del mismo periodo, con la **misma ventana de atribución** (estándar 7d-click/1d-view; recuerda que Meta quitó el view-through de 7/28d del API el 12-ene-2026, ver 16). Si broad gana o empata: mueve presupuesto gradualmente (20% cada 3-4 días) hasta que los de intereses queden vacíos y los apagas. Si broad pierde claro tras 2 semanas y gasto decente: revisa creativos (casi siempre es eso) antes de culpar al targeting.

## El requisito del broad: diversidad creativa REAL

Broad funciona porque cada creativo distinto "pesca" en un estanque distinto. Un video de testimonio atrae a un perfil; un demo de producto a otro; un meme a otro. Si le das al ad set broad **2 anuncios genéricos**, Meta solo tiene una caña de pescar: encuentra UN bolsillo de audiencia, lo agota, y el CPA sube. Eso no es que "broad no sirve": es broad mal alimentado = quemar plata.

Mínimo honesto: 4-6 creativos con **ángulos distintos** (no 6 colores del mismo banner). Y ojo con el **Entity ID** de 2026: Meta colapsa creativos casi-iguales en una sola entidad que compite consigo misma, así que apunta a **10-15 creativos CONCEPTUALMENTE distintos** por cuenta activa, no 100 casi-duplicados. La vida útil de un ad bajó a ~2-4 semanas (antes 6-8), así que necesitas un pipeline de refresco (ver 30, 38, 39 para el sistema de ángulos y volumen creativo). Si no puedes producir esa variedad todavía, resuelve eso primero — es mejor inversión que cualquier ajuste de targeting.

## Test honesto broad vs. detallado (plantilla)

No discutas de fe, mide en TU cuenta:

| | Ad set A | Ad set B |
|---|---|---|
| Audiencia | Broad (geo + edad) | Detallado (3-5 intereses del nicho) |
| Creativos | LOS MISMOS 5 en ambos | LOS MISMOS 5 |
| Presupuesto | Idéntico (ABO, ej. $50k COP/día c/u) | Idéntico |
| Duración | 7-14 días o ~50 conv/ad set | igual |
| Veredicto | gana el de mejor **CPA/ROAS**, NO el de mejor CTR/CPM | igual |

Veredicto típico jun-2026: broad gana o empata en la mayoría de cuentas con señal decente. Re-testea cada trimestre — la ventaja de broad crece a medida que tu Dataset acumula señal.

## Checklist de configuración broad (copiar y pegar)

1. Ubicación: país o ciudades donde ENTREGAS (la única cerca sagrada, ver 26).
2. Edad: mínima realista para tu ticket (22-25 si el producto cuesta > $100k COP); máxima abierta salvo razón fuerte.
3. Género: todos, salvo producto inequívocamente de uno (y aun así, prueba abierto: el que regala también compra).
4. Detailed targeting: vacío, o 1-3 intereses gruesos como sugerencia si el nicho es raro.
5. Placements: Advantage+ (automáticos). Incluye Threads (placement default a escala, CPMs bajos) y WhatsApp Status; no los recortes a mano el primer mes (ver 02/33).
6. Creativos: 4-6 ángulos distintos desde el día 1 (ver 30).
7. Evento de optimización: el más profundo que genere ~50/semana (Purchase si alcanza; si no, sube un nivel, ver 14).

Para cerrar las conversaciones que el broad te traiga a WhatsApp → **ventas_lushows**. Para saber si tu CAC con broad cierra contra tu LTV → **economist_lushows**.

## Errores comunes — blacklist

- Cambiar de intereses a broad de golpe apagando todo: pierdes el aprendizaje acumulado y entras en pánico al día 3. Migra en paralelo.
- Juzgar broad con 2 anuncios mediocres: el veredicto es sobre tus creativos, no sobre el targeting.
- Apilar 15 intereses "para afinar" dentro de Advantage+ audience: el sistema los trata como sugerencia y se expande igual; solo te engañas a ti mismo.
- Broad con edad 18-65+ vendiendo un producto de $800k COP: los de 18-21 clickean barato y no compran; pon edad mínima realista.
- Pelear contra la expansión de Advantage+ con exclusiones infinitas: si necesitas tanto control, tu problema es de oferta o creativo, no de audiencia.
- Subir 80 creativos casi-iguales creyendo que "más variantes = mejor": el Entity ID los colapsa y compiten entre sí. 10-15 conceptos distintos.
- Concluir "broad no funciona en mi nicho" tras 3 días y $200k COP de gasto: con ese volumen no aprendió nadie. Mínimo 7-14 días o ~50 conversiones.
