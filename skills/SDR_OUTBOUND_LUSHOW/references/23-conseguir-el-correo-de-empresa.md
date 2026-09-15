# 23 — Conseguir el correo de empresa

Este es el módulo que la gente busca cuando dice "necesito los correos". Ya tienes la empresa (`21`) y la persona decisora (`22`); ahora hay que conseguir su **correo corporativo** — el que existe, recibe y no rebota. El email finding (encontrar el correo) tiene dos caminos que se combinan: **deducir** el patrón del dominio y **buscar/verificar** con herramientas. Hacer esto bien es la diferencia entre una campaña que llega a la bandeja y una que te manda a spam por rebotes (ver `28`, `40`).

## El principio: casi todas las empresas usan un patrón

Una organización configura sus correos con **una plantilla fija** sobre su dominio. Si descubres el patrón de UNA persona, deduces el de TODAS las de esa empresa. Los patrones más comunes (frecuencia real aproximada en B2B):

| Patrón | Ejemplo (Juan Pérez, @acme.com) | Frecuencia aprox. |
|---|---|---|
| `nombre.apellido@` | juan.perez@acme.com | ~35 % |
| `nombre@` | juan@acme.com | ~15 % |
| `inicial+apellido@` | jperez@acme.com | ~15 % |
| `nombreapellido@` | juanperez@acme.com | ~10 % |
| `apellido.nombre@` | perez.juan@acme.com | ~5 % |
| `nombre.inicial@` / `inicial.apellido@` | juan.p@ / j.perez@ | resto |

En LatAm ojo con el **segundo apellido** y con las tildes/ñ: `perez` no `pérez`, `nunez` no `nuñez`. Un buen finder ya lo normaliza.

## Los dos caminos (úsalos juntos)

### Camino A — Deducir + verificar (barato, para pocos)
1. Descubre el patrón de la empresa: busca en Google `"@dominio.com" email`, mira la firma en algún correo público, o usa Hunter (te dice el patrón dominante del dominio).
2. Genera el correo del decisor aplicando el patrón.
3. **Verifícalo** (obligatorio) — sin verificar no lo envías (ver `28`).

### Camino B — Herramienta de email finding (a escala)
Le das nombre + apellido + dominio (o el `linkedin_url`) y te devuelve el correo ya con un score de confianza. Es el camino para volumen.

| Herramienta | Qué hace | Cobertura LatAm | Precio aprox. 2026 |
|---|---|---|---|
| **Apollo.io** | Finder + verificación + base propia + secuencias | Buena | Free 5k/mes limitado; pago ~$49–99/mes (ver `25`, `100`) |
| **Hunter.io** | Patrón del dominio + finder + verificador | Media | Free 25/mes; ~$34–104/mes |
| **Prospeo** | Finder + LinkedIn email + waterfall barato | Media-buena | ~$39/mes, créditos generosos |
| **FindThatLead** | Finder por dominio/nombre + verificador (creado en España, bueno para ES) | Buena en España/LatAm | ~$49/mes |
| **Dropcontact** | Finder + enriquecimiento GDPR-friendly (Europa) | Media | ~€24/mes |
| **RocketReach / Lusha / Cognism** | Finders con base propia grande | Variable (ver `25`) | Ver `25` |

**Recomendación práctica LatAm 2026:** Apollo como base (finder + verificación + secuencias en uno), y un waterfall (ver `29`, `130`) que encadene Prospeo/Hunter/FindThatLead para las que Apollo no encuentra. La cobertura LatAm siempre es menor que en USA: espera encontrar el email de ~60–80 % de tus decisores, no del 100 %.

## Deducir a mano (cuando la herramienta falla)

Para PYMES locales sin datos en las bases, muchas veces el correo está a la vista:
- Web de la empresa → página **Contacto** (a veces `gerencia@`, `ventas@` — genéricos, sirven para PYME).
- Firma en redes, pie de página, WHOIS del dominio.
- Google: `"nombre apellido" "@dominio.com"` o `site:dominio.com correo`.
- Si solo tienes genérico (`info@`, `contacto@`): sirve para PYME de dueño único (`22`), pero el correo nominal al decisor convierte más.

## Verificación: el paso que NO te puedes saltar

Un correo deducido **no está confirmado hasta verificarlo**. Enviar sin verificar sube el bounce (rebote) y quema tu dominio (ver `40`). Estados que te devuelve un verificador (ver `28` a fondo):

| Estado | Qué es | ¿Enviar? |
|---|---|---|
| **Valid / deliverable** | Existe y acepta correo | Sí |
| **Catch-all / accept-all** | El servidor acepta todo, no confirma si existe | Con cautela (riesgo medio) |
| **Invalid / undeliverable** | No existe o rebota | No — descártalo |
| **Risky / unknown** | No se pudo confirmar | No, o verifica con otro proveedor |

Verificadores dedicados: **NeverBounce, ZeroBounce, MillionVerifier, Bouncer** (ver `28`). Regla: mantén el **bounce < 2–3 %** por campaña o Gmail/Outlook empiezan a mandarte a spam.

## Ejemplo real: de nombre a correo verificado

```
Decisor: María Gómez Ruiz — Gerente de Operaciones — Grupo Sabores S.A.S
Dominio: grupossabores.com (de la web / Maps)

1. Hunter → patrón del dominio = {nombre.apellido}@ → maria.gomez@grupossabores.com
2. Ojo 2º apellido: probar también maria.gomez.ruiz@ y mgomez@
3. Verificar los candidatos en NeverBounce:
   maria.gomez@grupossabores.com → VALID  ✅  (usar este)
   mgomez@grupossabores.com      → INVALID ❌
4. Guardar: email + email_status=VALID + fuente=Hunter+NeverBounce
```

## Errores comunes (qué NO hacer)

- **Enviar correos deducidos sin verificar.** Es la causa #1 de caer en spam.
- **Comprar listas con correos "ya listos".** Rebotan y son ilegales (ver `49`).
- **Ignorar tildes/ñ/segundo apellido** en LatAm — genera correos inválidos.
- **Confiar en el finder sin cruzar** — usa waterfall (`130`) para subir cobertura y precisión.
- **Guardar catch-all como "válido".** Márcalos aparte y envíales con más cuidado.

## Frontera y siguiente paso

Conseguir y verificar el correo = esta skill. Qué **escribirle** en ese correo → copy y cold email en `50`–`56`; la **conversación de venta** que sigue a la respuesta → `ventas_lushows`. Con el email verificado, pasa a `24` (teléfono/WhatsApp para multicanal), luego `28` (limpieza masiva de toda la lista) y `29` (enriquecer para personalizar).
