# 67 — Reporting ejecutivo

Lee este módulo cuando tengas que reportarle a un cliente o a tu jefe y no sepas qué incluir, cuando tus reportes generan más preguntas que respuestas, cuando mandas un screenshot del panel de Ads y la otra persona se pierde, o cuando quieras que confíen en ti en vez de dudar cada peso. Un buen reporte no es un volcado de métricas: es una **historia con decisión**. El objetivo es que quien lo lea termine **tranquilo y con claridad**, no abrumado.

Principio: el cliente/jefe no quiere saber cómo funciona el motor; quiere saber si el carro avanza, cuánto gasta de gasolina, y hacia dónde va. Reporta resultado y decisión, no proceso ni jerga. La pauta de Google **captura intención**; tu reporte traduce esa captura a plata y a próximos pasos.

## Qué reportar (y qué callar)

| Incluir SIEMPRE | Dejar fuera |
|---|---|
| Gasto del periodo | Quality Score por keyword |
| Conversiones (leads o ventas) | Capturas crudas del panel |
| CPA y/o ROAS triangulado / MER (ver 64) | Listas de negativos agregados |
| Comparación vs periodo anterior | Detalles técnicos de pujas / Smart Bidding |
| 2–3 aprendizajes concretos | Jerga sin traducir |
| Próximos pasos claros | Métricas de vanidad (impresiones solas) |
| 1 alerta si la hay (competidor, suspensión) | Optiscore / Recommendations internas |

Regla: si una métrica no cambia una **decisión**, no va en el reporte ejecutivo. Va en tu hoja de trabajo, no en la cara del cliente. Las impresiones por sí solas son vanidad; el CPA y el MER deciden (ver 60).

## La plantilla (semanal o mensual)

Cópiala y rellénala. Cabe en una página. Números en COP. Esta es la columna vertebral del módulo:

```
REPORTE GOOGLE ADS — [Negocio] — [Semana/Mes]

1. RESULTADO (los 4 números que importan)
   • Inversión:        $X.XXX.XXX COP   (vs periodo anterior: +/- X%)
   • Conversiones:     XXX leads/ventas (vs anterior: +/- X%)
   • CPA:              $XX.XXX COP      (objetivo: $XX.XXX)
   • ROAS / MER:       X.X              (REAL, triangulado — ver 64)

2. EN UNA FRASE
   "[Vamos bien / hay un freno / probamos algo nuevo]: [explicación humana]."
   Ej: "Bajamos el CPA 18% apagando búsquedas irrelevantes; el cuello
        ahora es la landing móvil."

3. APRENDIZAJES (2–3, concretos)
   • [Qué descubrimos y qué hicimos]
   • Ej: "Las búsquedas genéricas convierten 3x mejor que las amplias;
          movimos presupuesto hacia allá."

4. PRÓXIMOS PASOS (qué haremos + qué necesito de ti)
   • [Acción nuestra]
   • [Lo que necesitamos del cliente: ej. arreglar velocidad de la web]

5. ALERTAS (solo si las hay)
   • Ej: "Un competidor está pujando sobre tu marca, subió el CPC 20%." (ver 94)
```

El bloque 2 ("En una frase") es el más importante y el más olvidado. Es lo que el cliente le repite a su socio. Si no puedes resumir el mes en una frase honesta, no entendiste tu propia cuenta.

## Ejemplo lleno (para que no quede abstracto)

```
REPORTE GOOGLE ADS — Calculadora GastroLatam — Junio 2026

1. RESULTADO
   • Inversión:     $3.200.000 COP   (vs mayo: +14%)
   • Ventas:        412 unidades     (vs mayo: +31%)
   • CPA:           $7.767 COP       (objetivo: $9.000) ✓
   • MER real:      3.1              (triangulado backend, vs mayo 2.6)

2. EN UNA FRASE
   "Subimos ventas 31% gastando solo 14% más: las búsquedas genéricas
    ('cómo costear un plato', 'food cost restaurante') rinden mejor que la
    marca, y movimos plata hacia allá."

3. APRENDIZAJES
   • El genérico trae cliente nuevo a $7.767; la marca traía gente que ya
     nos buscaba (medimos: 70% de esas ventas iban a pasar igual — ver 65).
   • El móvil convierte la mitad que desktop: la landing móvil es el freno.

4. PRÓXIMOS PASOS
   • Nosotros: escalar genérico 20%, abrir 2 grupos nuevos de keywords.
   • Tú: priorizar con tu dev la velocidad de la landing en celular (ver
     desingweb-lushows) — ahí se está fugando ~1 de cada 2 ventas móviles.

5. ALERTAS
   • Ninguna este mes.
```

Nota cómo cada número viene con su comparación, la frase resume sin jerga, y los próximos pasos reparten responsabilidad. Eso es lo que conserva clientes.

## Cómo construir confianza (no confusión)

Lo que separa al que conserva clientes del que los pierde:

- **Reporta el ROAS/MER real, no el del panel.** Si dices "ROAS 6" basado en el panel y el banco del cliente no lo siente, pierdes credibilidad para siempre. Triangula y reporta el número honesto (ver 64). Mejor "MER 2.5 real y creciendo" que "ROAS 6" que nadie ve.
- **Sé dueño de las malas noticias.** "Este mes el CPA subió 15% porque entró un competidor nuevo; esto es lo que estamos haciendo." Esconder un mal mes destruye la relación cuando se descubre.
- **Cierra siempre con una decisión.** Un reporte sin "próximo paso" deja al cliente sin saber qué sigue. Siempre termina diciendo qué vas a hacer y qué necesitas de él.
- **Mismo formato cada vez.** La consistencia genera confianza; cambiar el reporte cada mes parece que ocultas algo.
- **Distingue lo medido de lo estimado.** Si una cifra es modelada (Consent Mode) o triangulada, dilo. La honestidad sobre la incertidumbre genera más confianza que falsa precisión.
- **Si el cuello está fuera de Ads, dilo y rutea.** Si la landing es el problema, escríbelo y sugiere arreglarla (ver `desingweb-lushows`). Si la duda es de viabilidad/precio/margen, eso es `economist_lushows`. Si lo que falta es cerrar los leads que ya entran, es `ventas_lushows`. Si conviene complementar con generación de demanda, `facebook_ads_lushows` / `tiktok_ads_lushows`. No cargues con culpas que no son de la pauta.

## De dónde sacas los datos del reporte

El reporte se llena con tu mesa de trabajo (ver 63), tu triangulación (ver 64) y, si lo automatizaste, tu dashboard (ver 69). El flujo sano:
1. Mesa de trabajo en Google Ads (columnas + segmentos, ver 63) → ves qué pasó.
2. Triangulación con backend/banco (ver 64) → sabes qué fue real.
3. Dashboard de Looker Studio (ver 69) → el cliente ve los números vivos.
4. **Este reporte** → tú pones la frase, el aprendizaje y la decisión que el dashboard no da.

El dashboard muestra **qué pasó**; el reporte ejecutivo explica **qué significa y qué sigue**. No son lo mismo y el segundo no se automatiza.

## Frecuencia

| Cuándo | Para quién | Profundidad |
|---|---|---|
| **Semanal** | Cuentas activas, lanzamientos, presupuestos grandes | Corto: los 4 números + 1 frase + alertas |
| **Mensual** | Estándar para la mayoría | La plantilla completa |
| **Tiempo real** | Solo si hay un incendio (cuenta suspendida, gasto disparado) | Mensaje directo, no reporte formal |

No reportes diario salvo lanzamiento crítico: genera ansiedad y el ruido del día a día confunde más que ayuda (ver 61 sobre no reaccionar al ruido de pocos días).

## Errores comunes — blacklist

1. **Mandar un screenshot del panel como reporte.** Genera confusión, no confianza. Traduce a la plantilla con decisión incluida.
2. **Reportar el ROAS del panel como si fuera real.** Cuando el banco no lo confirma, pierdes credibilidad. Reporta el número triangulado (ver 64).
3. **Llenar el reporte de métricas que no cambian ninguna decisión.** Impresiones, Quality Score por keyword: eso es tu hoja de trabajo, no el reporte del cliente.
4. **Esconder un mal mes.** Se descubre y destruye la relación. Sé dueño de las malas noticias con un plan al lado.
5. **No cerrar con próximos pasos.** Un reporte sin decisión deja al cliente sin saber qué sigue ni qué necesitas de él.
6. **Cambiar el formato cada vez.** La inconsistencia parece que ocultas algo. Misma plantilla, siempre.
7. **Cargar con culpas que no son de Ads.** Si el problema es landing, oferta o cierre, dilo y rutea (`desingweb-lushows`, `economist_lushows`, `ventas_lushows`) en vez de inventar excusas dentro de la pauta.
8. **Presentar cifras modeladas/estimadas como hechos exactos.** Distingue lo medido de lo estimado; la falsa precisión cuesta credibilidad cuando no cuadra con el banco.
