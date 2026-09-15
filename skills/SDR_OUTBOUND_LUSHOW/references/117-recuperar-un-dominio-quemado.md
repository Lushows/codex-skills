# 117 — Recuperar un dominio quemado

Tarde o temprano un dominio de tu flota se quema: la reputación cae a "Baja/Mala" en Postmaster (ver `113`), el spam rate se dispara, el placement se va a spam (ver `116`), quizá entra a una blacklist (ver `114`). Un **dominio quemado** es uno cuya reputación está tan dañada que sus correos caen en spam por defecto, sin importar el copy. Este módulo es el protocolo de crisis: **cómo diagnosticas la gravedad, cuándo vale la pena recuperarlo (descansar, desintoxicar, reconstruir) y cuándo simplemente lo jubilas y sigues.** La decisión no es emocional: los dominios de outbound son desechables por diseño (ver `41`, `110`), y a veces reconstruir cuesta más que empezar limpio. Lo único que casi siempre se pelea a muerte es tu **dominio principal** — ese sí es irreemplazable.

## Primero: ¿está quemado, o solo tropezó?

No todo bajón es "quemado". Diagnostica la gravedad antes de actuar:

| Señal | Tropezón (recuperable fácil) | Quemado (crisis) |
|---|---|---|
| Domain Reputation (Postmaster) | Bajó de Alta a Media | Baja o Mala sostenida (semanas) |
| Spam Rate | Subió a 0.2–0.3% puntual | > 0.3% sostenido |
| Placement (seed test) | Algo más de Promociones | Mayoría en spam en varios proveedores |
| Bounce rate | Pico aislado | Alto y persistente |
| Blacklist | Limpio o lista menor | En Spamhaus, reincidente |
| Reply rate | Bajó un poco | Se secó por completo |

Un tropezón se arregla bajando volumen, limpiando lista y reforzando warmup (ver `112`, `28`) sin drama. Un dominio quemado necesita el protocolo completo o jubilación.

## El protocolo de recuperación (si decides pelearlo)

Recuperar un dominio quemado es **lento** (semanas a meses) y no siempre funciona. Vale la pena solo si el dominio tiene valor (antigüedad, es tu principal, o la causa fue un error puntual y corregible). Pasos:

```
1. PARA TODO. Cero outbound desde ese dominio. Seguir enviando quemado
   solo profundiza el pozo. Esto es innegociable.

2. DIAGNOSTICA LA CAUSA (no reinicies sin saberla):
   - ¿Lista sucia / spam-traps? (ver 28, 114)  → la causa nº1
   - ¿Volumen brusco sin rampa? (ver 112)
   - ¿Copy que generó quejas? (ver 45, 40)
   - ¿Autenticación rota? (ver 42, 111)
   - ¿En blacklist? → delisting primero (ver 114)

3. DESCANSA el dominio 2-4 semanas (o más) en silencio total.
   La reputación decae con el tiempo, pero también se "enfría" el mal historial.
   El descanso deja que Google/Microsoft olviden el mal comportamiento reciente.

4. ARREGLA la causa raíz mientras descansa:
   - Limpia TODA la base con verificador; borra hard bounces y dudosos (ver 28)
   - Revisa/repara SPF, DKIM, DMARC (ver 42, 111)
   - Reescribe copy si generó quejas (texto plano, relevante; ver 45)
   - Sal de blacklists (ver 114)

5. RE-WARMUP desde cero, lento. Trátalo como dominio nuevo:
   warmup 3-4 semanas, arranque a 5/día, rampa mínima (ver 112).

6. REINICIA con volumen bajísimo y lista limpísima, SOLO a contactos de alta
   probabilidad de respuesta positiva (tus mejores segmentos; ver 10, 16).
   El objetivo es generar engagement positivo que reconstruya reputación.

7. VIGILA a diario la primera semana: Postmaster, placement (seed test),
   blacklist. Si a las 2-3 semanas la reputación no sube, ve al paso de jubilar.
```

**Realidad honesta:** un dominio que cayó a "Mala" en Postmaster a menudo **no se recupera** aunque hagas todo bien, o tarda meses. Por eso el descanso + re-warmup es una apuesta, no una garantía.

## Cuándo jubilar (y por qué casi siempre es lo correcto para la flota)

Para un dominio **secundario de outbound**, la matemática suele favorecer jubilar:

| Recuperar | Jubilar y reemplazar |
|---|---|
| 4–8 semanas de descanso + re-warmup, sin garantía | ~$10–15 dominio nuevo + 3–4 semanas warmup, resultado predecible |
| Riesgo de recaída (historial marcado) | Empieza limpio, sin lastre |
| Solo vale si el dominio tiene antigüedad/valor | Ideal si es un dominio joven y desechable |

**Regla de flota:** si tienes colchón de buzones calentándose (ver `112`), jubilar un dominio quemado casi no duele — activas el reemplazo y sigues. Guarda el esfuerzo de recuperación para casos con valor real.

Cómo jubilar bien:
- Pausa y no borres de golpe: deja que las conversaciones abiertas terminen por otros buzones.
- Compra el reemplazo (variante limpia; ver `41`), autentícalo (ver `42`, `111`), caliéntalo.
- Documenta la baja en tu hoja de flota (ver `110`): fecha y causa, para no repetir el error.

## Caso especial: tu dominio PRINCIPAL se quemó

Aquí no se jubila — se pelea. Tu dominio principal maneja tu correo real (clientes, proveedores, recepción). Si lo quemaste (típico: alguien mandó outbound frío desde él, el error que `40` y `41` te advierten evitar):

1. **Deja de mandar CUALQUIER cosa masiva desde él inmediatamente.** El principal es solo para 1-a-1 y transaccional.
2. Sigue el protocolo de recuperación con paciencia extra (puede tomar meses).
3. Considera **BIMI + DMARC reject** para blindarlo hacia adelante (ver `111`).
4. **Nunca** vuelvas a mandar outbound frío desde él. Para eso están los secundarios (ver `41`, `110`).

## Errores comunes (qué NO hacer)

- Seguir enviando desde el dominio quemado "a ver si se recupera solo". Lo entierras más.
- Reiniciar sin descanso ni arreglar la causa: recaes en días.
- Re-warmup rápido para "recuperar el tiempo perdido": lo vuelves a quemar.
- Pelear a muerte por un dominio secundario desechable cuando jubilar es más barato y seguro.
- Jubilar el dominio principal (¡es irreemplazable!) en vez de recuperarlo.
- No documentar la causa: repites el mismo error con el dominio nuevo.
- Mandar outbound frío desde el principal "solo esta vez": así se quema el activo irreemplazable.

## Siguiente paso

La mejor recuperación es no quemarse: revisa que tu volumen a escala respete la matemática de buzones para no forzar dominios — ve a `118` (cold email a volumen seguro). Para el warmup lento del re-inicio, `112`. Para salir de blacklists, `114`. Para verificar el placement tras reconstruir, `116`. Los fundamentos de por qué usar secundarios y no el principal están en `41`.
