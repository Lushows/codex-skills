# 67 — Reporting ejecutivo

Lee este módulo cuando tengas que reportarle resultados a un cliente o a tu jefe y no sepas qué incluir, cuando tus reportes sean capturas de pantalla de Ads Manager que nadie entiende, o cuando quieras que te paguen más y te renueven (un buen reporte vende tu trabajo). El reporte ejecutivo no es para ti — es para alguien que NO vive en la cuenta y solo quiere saber tres cosas: ¿cuánto gasté, qué obtuve, y qué sigue? Si tu reporte no contesta eso en 30 segundos, sobra. Un media buyer honesto reporta también lo que NO funcionó; eso construye la confianza que renueva contratos (rutea el cierre/relación a `ventas_lushows`).

## A quién le reportas cambia qué reportas

| Audiencia | Qué le importa | Qué NO le importa |
|---|---|---|
| **Cliente / jefe** (no técnico) | Plata invertida vs plata generada, MER, próximos pasos | Thumbstop, CVR, breakdowns |
| **Tú / el equipo** (operativo) | Creativos ganadores, capas rotas (ver 61), CPA por anuncio | El resumen de una línea |

No le tires siglas a un dueño de restaurante. "El thumbstop subió a 38%" no le dice nada; "los videos nuevos enganchan más y bajaron el costo por venta de $12.000 a $8.000" sí. Traduce siempre la jerga al lenguaje de la plata (ver 64 para el MER). Diccionario rápido de traducción:

| Jerga | Cómo decírselo al cliente |
|---|---|
| Thumbstop / hook rate | "Cuánta gente frena a ver el video" |
| CVR baja | "Llegan pero no terminan de comprar" |
| MER | "Por cada peso en pauta, entran X pesos al negocio" |
| Frequency alta | "Le estamos mostrando el anuncio demasiadas veces a los mismos" |
| Iterar el ganador | "Estamos haciendo más versiones del video que más vende" |

## La plantilla semanal/mensual

Una página. Siempre la misma estructura para que el lector aprenda a leerla. Cadencia: **semanal** operativo, **mensual** ejecutivo con tendencia.

```
REPORTE TIKTOK ADS — [Cliente] — [Semana/Mes] — Atribución: 7d-click/1d-view

1. RESUMEN (3 líneas)
   Gastamos $X, generamos $Y (banco), MER Z. [Una frase de qué pasó y por qué.]

2. NÚMEROS CLAVE
   ┌──────────────────┬──────────┬──────────┬─────────┐
   │ Métrica          │ Periodo  │ Anterior │ Δ       │
   ├──────────────────┼──────────┼──────────┼─────────┤
   │ Gasto            │ $X       │ $X-1     │ ±%      │
   │ Conversiones     │ N        │ N-1      │ ±%      │
   │ CPA              │ $        │ $        │ ±%      │
   │ ROAS (plataforma)│ x*       │ x*       │ ±%      │
   │ MER (real)       │ x        │ x        │ ±%      │
   │ GMV / ingreso    │ $        │ $        │ ±%      │
   │ Frequency        │ x        │ x        │ ±%      │
   └──────────────────┴──────────┴──────────┴─────────┘
   *ROAS de plataforma infla; el MER es el real (ver 64).

3. CREATIVOS GANADORES (qué video trajo las ventas) — ver 68
4. APRENDIZAJES (qué probamos, qué funcionó, qué NO)
5. PRÓXIMOS PASOS (3 acciones concretas para la próxima semana)
```

Siempre con **comparación contra el periodo anterior** y el **Δ** (delta = el cambio). Un número solo no dice nada; "$8.000" no significa nada hasta que se sabe que antes era "$12.000". La tendencia es la historia. Pon la **ventana de atribución** en el encabezado (ver 63) para que nadie compare un mes a 7 días con otro a 1 día.

## Plantilla rellena (ejemplo)

```
REPORTE TIKTOK ADS — GastroLatam — Junio 2026 — Atribución: 7d-click/1d-view

1. RESUMEN
   Gastamos $4.0M, el negocio entró $14.3M (banco), MER 2.2x. Bajamos el costo
   por venta de $12.000 a $7.800 cambiando los hooks de los videos.

2. NÚMEROS CLAVE
   Gasto $4.0M (+18%) · Ventas 512 (+34%) · CPA $7.800 (−35%) ·
   ROAS plataforma 4.2x* · MER real 2.2x (+0.3) · GMV $14.3M (+31%) · Freq 2.4

3. CREATIVOS GANADORES
   - "Dolor de costos" (hook3): 210 ventas, CPA $5.000 → lo estamos escalando
   - "Testimonio chef": 130 ventas, CPA $9.000 → haremos más versiones

4. APRENDIZAJES
   - Probamos 3 ángulos nuevos: "dolor" ganó, "identidad" murió (lo matamos),
     "ahorro de tiempo" quedó a prueba una semana más.
   - El píxel no medía la compra hasta el 8 de junio (lo arreglamos): el CPA
     real siempre fue bueno, solo no lo veíamos (ver 62).

5. PRÓXIMOS PASOS
   - Escalar "dolor de costos" +20% de presupuesto.
   - Grabar 3 hooks nuevos sobre el cuerpo del testimonio del chef.
   - Probar TikTok Shop con el producto estrella.
```

## Los cinco bloques, explicados

1. **Resumen de 3 líneas.** Lo único que algunos van a leer. Gasto, resultado (del banco, no del panel), MER, una frase. Que se entienda solo.
2. **Números clave con Δ.** Mete el **MER** (ver 64), no solo el ROAS de plataforma — es lo honesto y te diferencia. CPA, conversiones, gasto, GMV, frequency. Marca el ROAS de panel con asterisco.
3. **Creativos ganadores.** Muestra los 2-3 videos que trajeron las ventas (ver 68). Esto le recuerda al cliente que el creativo es el motor y justifica seguir produciendo (ver 30). Sale del cruce `utm_content` × backend (ver 66).
4. **Aprendizajes — incluye lo que falló.** "Probamos 3 ángulos; el de dolor ganó, el de identidad murió, lo matamos." Reportar lo que NO funcionó **genera confianza**: demuestra rigor y que no escondes nada. El media buyer que solo reporta victorias huele a humo.
5. **Próximos pasos.** Máximo 3 acciones concretas y específicas: "escalar el creativo ganador 20%", "grabar 3 hooks nuevos", "probar TikTok Shop". No "seguir optimizando" (eso no es un plan).

## Cómo presentarlo

- **Formato:** PDF o doc limpio de una página, no capturas de Ads Manager. Si es presentable, genera PDF directo (el cliente no debería tener que procesar un MD).
- **Honestidad con los números:** si el MER bajó, dilo y explica por qué + el plan. Esconderlo se descubre cuando el banco no cuadra y cuesta el contrato.
- **El ROAS con asterisco:** cuando muestres el ROAS de plataforma, aclara que es el de TikTok y que el MER es el real (ver 64). Educas al cliente y te proteges.
- **Frecuencia constante:** mismo día, misma plantilla, siempre. La consistencia construye confianza tanto como los números.
- **Multicanal:** si también corres Meta o Google, reporta el MER **conjunto** (suma de canales, ver 64) y deja el desglose por canal abajo. El dueño piensa en el negocio, no en plataformas (cruza con `facebook_ads_lushows`, `google_ads_lushows`).

## Errores comunes — blacklist

- **Mandar capturas de Ads Manager.** Nadie no-técnico las entiende. Usa la plantilla de una página.
- **Reportar solo el ROAS de plataforma.** Infla; mete el MER o pareces deshonesto cuando el banco no cuadra (ver 64).
- **Solo reportar victorias.** Esconder lo que falló destruye confianza cuando se descubre. Reporta los aprendizajes negativos.
- **Números sin comparación.** "$8.000 de CPA" no dice nada sin el "antes era $12.000". Siempre Δ vs periodo anterior.
- **Tirar siglas a un no-técnico.** Traduce thumbstop/CVR a "engancha más / vende más". Habla de plata.
- **Próximos pasos vagos.** "Seguir optimizando" no es un plan. Da 3 acciones concretas.
- **Cambiar la plantilla cada semana.** El lector tiene que reaprender a leerla. Misma estructura siempre.
- **No declarar la ventana de atribución.** Comparas periodos con vara distinta y "mejoras" que no existen.
