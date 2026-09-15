# 25 — Herramientas de sourcing (bases de datos de contactos)

Las herramientas de sourcing son las **bases de datos de empresas y contactos** con las que sacas listas y correos a escala. En vez de deducir a mano (`23`) o scrapear (`27`), le pides a la base: "dame los Gerentes de Operaciones de restaurantes de 50–200 empleados en Colombia, con su correo y teléfono". Aquí está el mapa de las principales, qué hace cada una, su cobertura en LatAm y precios aproximados 2026 — para que elijas sin gastar de más.

## El principio: cada base es fuerte en algo y floja en otro

Ninguna base tiene todos los datos de todos los países. Se diferencian en: **cobertura geográfica**, **precisión del email/móvil**, **si trae señales/intent** (ver `36`, `131`), **precio** y **si además envía** (secuencias) o solo da datos. La cobertura en **LatAm siempre es menor que en USA**: cualquier proveedor "premium USA" cae 30–50 % de cobertura al sur. Por eso muchos usan **Apollo como base + un waterfall** (`29`, `130`) que rellena huecos con otras.

## Comparativa — las principales

| Herramienta | Qué hace / fuerte en | Cobertura LatAm | Precio aprox. 2026 | Cuándo elegirla |
|---|---|---|---|---|
| **Apollo.io** | Base grande + finder + verificación + **secuencias en la misma app**. Todo-en-uno. | Buena (la mejor relación cobertura/precio para LatAm) | Free limitado; ~$49–99/usuario/mes | **Punto de partida por defecto**, sobre todo con presupuesto ajustado (`100`) |
| **ZoomInfo** | La base más completa y rica en datos B2B (org charts, intent, scoops). Enterprise. | Media (fuerte USA, menos LatAm) | Enterprise, ~US$15k+/año, contrato anual | Equipos grandes con presupuesto y foco USA (`106`) |
| **Lusha** | Datos de contacto directos, sobre todo **móviles**; extensión de LinkedIn simple | Media-buena en móviles | Free 5 créditos; ~$36–79/usuario/mes | Cuando necesitas **teléfonos/móviles** rápido (`24`) |
| **Cognism** | Móviles **verificados** ("Diamond Data"), fuerte compliance GDPR, buena Europa/EMEA | Media (mejor Europa que LatAm) | Enterprise, ~US$15k+/año | Outbound a Europa con foco en llamadas y compliance |
| **RocketReach** | Finder de email + teléfono con base amplia; bueno para casos sueltos | Media | ~$39–99/mes | Búsquedas puntuales, presupuesto medio |
| **Hunter.io** | Especialista en **email por dominio** + patrón + verificador. No es base de personas completa. | Media | Free 25/mes; ~$34–104/mes | Deducir/verificar correos por dominio (`23`) |
| **Clearbit (Breeze Intelligence, HubSpot)** | **Enriquecimiento** de registros existentes + datos de empresa; ahora dentro de HubSpot | Media | Ligado a HubSpot | Enriquecer tu CRM, no prospección desde cero (`29`) |
| **Prospeo / FindThatLead / Dropcontact** | Finders económicos, buenos para waterfall | Media (FindThatLead bueno en ES) | ~$24–49/mes | Rellenar cobertura barato en un waterfall (`130`) |
| **Lead411 / Seamless.ai / UpLead** | Alternativas de base + finder, foco USA | Baja-media LatAm | ~$99+/mes | Foco USA con alternativa a ZoomInfo |

## Cómo elegir (árbol de decisión)

1. **Presupuesto ajustado + LatAm + quieres todo-en-uno (datos + envío):** → **Apollo**. Cubre el 80 % de los casos de esta skill. Empieza aquí.
2. **Necesitas móviles/teléfonos sí o sí:** añade **Lusha** (LatAm) o **Cognism** (Europa) sobre Apollo.
3. **Solo quieres el correo por dominio de pocas cuentas:** **Hunter** o Prospeo, sin pagar una base entera.
4. **Equipo grande, foco USA, presupuesto enterprise, quieres intent y org charts:** **ZoomInfo** (`106`).
5. **Ya tienes CRM y solo quieres rellenar datos faltantes:** enriquecimiento con **Clearbit/HubSpot** o waterfall en **Clay** (`31`, `29`).

Regla de oro: **empieza barato y sube.** No compres ZoomInfo para prospectar 200 restaurantes; Apollo + Maps (`21`) + un verificador (`28`) hacen ese trabajo por una fracción.

## El patrón que usan los buenos: Apollo + waterfall en Clay

La configuración más costo-efectiva 2026 para LatAm:
```
1. Apollo → saca cuentas + contactos + correos (base).
2. Los que Apollo no encuentra → Clay (`31`) corre un WATERFALL:
   intenta Prospeo → si falla Hunter → si falla FindThatLead → ...
   (paga solo por el que acierta; sube cobertura de ~65% a ~85%).
3. Verifica TODO con NeverBounce/MillionVerifier (`28`).
4. Enriquece con señales/personalización (`29`).
```
Esto combina lo mejor: la base barata de Apollo + la cobertura del waterfall + limpieza. Detalle del waterfall en `130`.

## Advertencias sobre datos y legalidad

- **La cobertura LatAm que promete el vendedor es optimista.** Pide prueba gratis y **testea con TUS cuentas reales** antes de pagar anual.
- **Los datos caducan** (~30 % de rotación anual de cargos): un email correcto hoy rebota en 6 meses. Reverifica (`28`, `139`).
- **Legalidad:** que una base te venda el dato no te exime de Habeas Data/GDPR. Debes tener base legítima para contactar y ofrecer opt-out (ver `49`, `181`). ZoomInfo/Cognism dan herramientas de compliance; úsalas.
- **No confundas base con estrategia:** la herramienta da datos; el ICP (`10`) y el mensaje (`50`) los pones tú.

## Errores comunes (qué NO hacer)

- Firmar contrato anual caro sin prueba con tus cuentas reales de LatAm.
- Pagar dos bases que se solapan; mejor una base + waterfall de finders baratos.
- Confiar el email sin verificar (toda base tiene rebotes) → `28`.
- Creer que más créditos = más ventas. Más basura filtrada más rápido, si no cuidas el fit (`20`).

## Siguiente paso

Elige tu base (empieza con Apollo — a fondo en `100`), extrae una tanda con tu ICP (`10`) y tus cuentas de `21`/decisores de `22`. Para exprimir Sales Navigator como fuente de personas → `26`. Para scraping cuando la base no cubre → `27`. Luego verifica (`28`) y enriquece (`29`).
