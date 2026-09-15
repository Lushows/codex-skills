# 132 — Deanonimización web (identificar quién visita tu sitio)

La **deanonimización web** (website de-anonymization) es identificar **qué empresas —y a veces qué personas— visitan tu sitio aunque no llenen ningún formulario**. El 97–98 % de quien entra a tu web se va sin dejar datos; estas herramientas te dicen quiénes eran. Es el intent data (`36`, `131`) **más barato, más accionable y más ignorado**: alguien que vio tu página de precios y no compró es un lead calientísimo para outbound, porque ya conoce tu producto y mostró interés real. Este módulo cubre las herramientas (RB2B, Vector, Warmly, Leadfeeder) y cómo montar el flujo visita → outbound.

## El principio: la visita es intención pura, y es tuya

El intent de terceros (Bombora) es caro y anónimo a nivel persona. El intent de **tu propia web es first-party** (dato tuyo, gratis o casi), y es la señal de compra más directa que existe: nadie visita tu página de precios "por accidente". La mecánica de identificación es doble:

- **A nivel empresa (IP reverse lookup):** cruzan la IP del visitante contra bases de IPs corporativas y te dan la **empresa**. Funciona en todo el mundo, pero no te da la persona.
- **A nivel persona:** con cookies/píxeles y bases de identidad (sobre todo en US), algunas te dan **nombre + LinkedIn + email** del visitante individual. Cobertura alta en US, baja fuera.

La diferencia legal y de cobertura por región es clave: identificar **personas** en la UE/LatAm choca con privacidad (GDPR/consentimiento); identificar **empresas** por IP es mucho más defendible. Cuida el marco legal → `07`, `27`.

## Las herramientas

| Herramienta | Qué identifica | Región fuerte | Precio aprox. 2026 | Nota |
|---|---|---|---|---|
| **RB2B** | Personas (nombre+LinkedIn) | US (persona), resto solo empresa | Tier **gratis** + pago desde ~$99/mes | El más famoso 2026; empieza gratis (US) |
| **Vector** | Personas + empresas + señales | US fuerte | Desde ~$300/mes | "Signal-based", integra intent |
| **Warmly** | Empresas + personas + orquesta acción | US/global (empresa) | Desde ~$700/mes | Deanonimiza **y dispara** la jugada (Slack, chat, outbound) |
| **Leadfeeder (Dealfront)** | Empresas (por IP) | **Europa fuerte** | Desde ~$99/mes | El mejor para empresa en EU/LatAm, no da persona |
| **Albacross / Clearbit** | Empresas / integrado a HubSpot | Global / HubSpot | Add-on | Clearbit=Breeze si vives en HubSpot (`131`) |

**Para LatAm:** apuesta a identificación **por empresa** (Leadfeeder, o el modo empresa de cualquiera). La identificación de persona funciona sobre todo en US; fuera, esperar poco. Aun así, saber **qué empresa** entró ya te deja encontrar al decisor tú mismo (`22`).

## Cómo montar el flujo visita → outbound, paso a paso

1. **Instala el píxel/script** de la herramienta en tu web (una línea en el `<head>`, o vía Google Tag Manager). Cero código real.
2. **Define páginas de alto intent:** `/precios`, `/demo`, páginas de producto, casos de éxito. Una visita ahí pesa más que al blog.
3. **Filtra por fit (ICP).** La herramienta identificará mucha empresa fuera de tu ICP (proveedores, curiosos, competencia). Cruza con tu ICP (`10`, `137`) — solo las que encajan valen.
4. **Enriquece y encuentra al decisor.** Si solo tienes la empresa, Clay (`31`) + Sales Nav (`26`) encuentran al decisor y su correo (`22`, `23`, waterfall `130`).
5. **Dispara la campaña "visitantes-web"** en tu sequencer (`33`) — cadencia aparte, más caliente y corta que el frío puro.
6. **Actúa rápido.** La visita caduca como toda señal (`37`); contacta en días.

## Ejemplo real: cadencia de visitante-web (sin delatar el tracking)

```
Señal (Leadfeeder): "Franquicia Sabor, 60 empleados, Bogotá,
                     visitó /precios y /casos ayer, no dejó datos"
Fit (Clay): ¿ICP? sí → prioridad A
Acción: Clay halla al Gerente de Operaciones → verifica email (`28`)
         → campaña "visitantes-web" en Smartlead (`33`)

Email 1 (día 0):
  Asunto: {Empresa} + control de costos por sede
  "Hola {nombre}, trabajo con cadenas de restaurantes del tamaño de
   {Empresa} en {ciudad} que quieren ver el costo real por sede sin
   pelear con hojas de cálculo. ¿Tiene sentido una charla de 10 min
   esta semana?"
```

El correo **NUNCA** dice "vi que visitaste nuestra web" — suena a acecho y espanta. La visita es señal **tuya** para priorizar y sincronizar el timing, no un dato para restregar (`36`, `128`).

## Errores comunes

- **Decir "vi que visitaste nuestra página"** → el error #1; da miedo, no confianza.
- **Esperar identificación de persona fuera de US** → arma tu flujo asumiendo solo empresa en LatAm.
- **No filtrar por fit** → la herramienta te llena de proveedores y competencia entrando a tu web.
- **Tratarlo como formulario** → el visitante no pidió contacto; tu outbound debe ganarse la conversación, no asumir interés declarado.
- **Ignorar el consentimiento/privacidad** en EU/LatAm al identificar personas → riesgo legal (`07`).

## Frontera y siguiente paso

Deanonimizar te da **la lista más caliente que existe**; convertirla en reunión y cerrar es `ventas_lushows`. Instala RB2B (gratis, si tienes tráfico US) o Leadfeeder (empresa, EU/LatAm) **esta semana** — es el intent más barato que hay. Cruza con fit (`137`), encuentra al decisor (`22`, `130`) y dispara la cadencia de visitantes (`33`, `34`). Para el resto del intent (G2, Bombora) → `131`; para señales de evento → `133`, `135`.
