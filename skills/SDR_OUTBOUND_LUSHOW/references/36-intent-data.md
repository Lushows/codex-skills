# 36 — Intent data (datos de intención)

El "intent data" (datos de intención) son señales de que una empresa está **investigando activamente** una solución como la tuya, aunque todavía no te haya contactado. Ejemplo: 8 personas de una empresa leyeron esta semana artículos sobre "software de facturación" y compararon proveedores en G2. Esa empresa está en el mercado **ahora**. Contactarla vale muchísimo más que contactar a una idéntica que no muestra ninguna señal. Este módulo explica qué es, de dónde sale y cómo usarlo sin gastar de más. Es primo hermano de las señales de evento (`37`) y del intent avanzado (`131`).

## El principio: timing multiplica todo lo demás

En outbound, el mensaje correcto a la persona correcta **en el momento equivocado** no vende. El intent data ataca justo el timing —la variable más difícil de conseguir—. La mecánica: la mayoría de tu mercado no está comprando en cualquier momento dado; una fracción pequeña **sí** lo está esta semana. El intent data te dice cuál es esa fracción. Contactar a los "in-market" (en mercado ahora) sube tus tasas de respuesta y reunión de forma dramática frente al frío puro (ver `14`, `137`).

Distinción clave:
- **Fit (encaje):** ¿esta empresa es de mi ICP? (tamaño, industria) — ver `10`, `15`.
- **Intent (intención):** ¿está buscando ahora? — este módulo.
- **El oro está en la intersección:** buen encaje **+** intención activa = tu lista prioritaria (ver `137`).

## Los tres tipos de intent data

| Tipo | Qué es | De dónde sale | Ejemplo |
|---|---|---|---|
| **Third-party (de terceros)** | Consumo de contenido en la web abierta, agregado por proveedores | Bombora, 6sense | "Empresa X consume contenido sobre 'CRM' arriba de su base" |
| **Review-site / marketplace** | Actividad en sitios de comparación de software | G2, Capterra intent | "Alguien de Empresa X vio tu perfil y el de 2 competidores en G2" |
| **First-party (propia)** | Actividad en TUS propios activos | tu web (deanonimización), emails, demos | "3 personas de Empresa X visitaron tu página de precios" |

### Third-party: Bombora
Bombora rastrea el consumo de contenido en miles de sitios B2B y detecta cuando una empresa "sube" (surge) su interés en un tema frente a su comportamiento normal. Te entrega un "Surge score" por cuenta y tema. Es amplio pero anónimo a nivel empresa (no persona). Fuerte para priorizar cuentas; caro, suele venir en contratos (a menudo dentro de 6sense/ZoomInfo). Detalle en `131`.

### Review-site: G2
G2 Buyer Intent te dice qué empresas están **mirando tu categoría y a tus competidores** en G2 justo ahora. Es señal altísima porque comparar en G2 es acto de compra tardío. Si vendes software y estás en G2, es de los intent data con mejor ROI.

### First-party: tu propia web
El intent más barato y más ignorado. Herramientas de **deanonimización web** (RB2B, Warmly, Vector) te dicen **qué empresas —a veces qué personas— visitaron tu sitio** aunque no llenaran nada. Alguien que visitó tu página de precios y no compró es un lead calientísimo para outbound. Detalle en `132`. Empieza por aquí: es lo más accionable y barato (RB2B tiene tier gratis para US).

## Cómo usarlo, paso a paso

1. **Empieza por first-party** (tu web). Instala RB2B/Warmly. Cuesta poco/nada y las cuentas que ya te visitaron son tu mejor lista fría (ver `132`).
2. **Si vendes software, activa G2 Buyer Intent.** Las cuentas mirando tu categoría van directo a una campaña priorizada.
3. **Third-party (Bombora/6sense) solo a escala.** Es caro; se justifica cuando tienes equipo y un TAM grande que priorizar. No lo compres para validar.
4. **Cruza intent con fit.** Una cuenta con surge pero fuera de ICP no vale; una con surge **y** dentro de ICP es prioridad #1. Haz este cruce en Clay (ver `31`, `137`).
5. **Dispara outbound específico por el intent.** El mensaje debe reflejar (sutilmente) la señal, sin decir "sé que nos estás espiando" (ver `128`). Ej.: si consume contenido de "seguridad", tu ángulo es seguridad.

## Ejemplo: campaña disparada por intent de web

```
Señal (RB2B): "Restaurante Brasa, 40 empleados, visitó /precios ayer,
               no dejó datos"
Cruce (Clay): ¿encaja ICP? sí → prioridad A
Acción:       Clay encuentra al dueño/gerente → verifica email → 
              a campaña "visitantes-web" en Smartlead
Opener (sin delatar el tracking):
   "Hola {nombre}, trabajo con restaurantes del tamaño de {empresa}
    en {ciudad} que buscan ordenar sus costos. ¿Tiene sentido una
    charla corta de 10 min esta semana?"
```
El correo **no** dice "vi que visitaste nuestra web" —suena a acecho—. Usa la señal para **priorizar y sincronizar el timing**, no como amenaza.

## Errores comunes

- **Comprar Bombora para validar.** Es caro y amplio; empieza por tu propia web (first-party).
- **Delatar el tracking.** "Vi que visitaste nuestra página" espanta. La señal es tuya, no del prospecto.
- **Intent sin fit.** Una empresa "in-market" que no es de tu ICP igual no compra; cruza siempre (ver `137`).
- **Tratar intent anónimo (empresa) como si fuera una persona.** Bombora te da la cuenta, no el contacto; todavía tienes que encontrar al decisor (ver `22`).

## Siguiente paso

Instala una herramienta de deanonimización web (first-party) esta semana: es el intent más barato y accionable. Si vendes software, activa G2 Buyer Intent. Cruza intent con fit en Clay (`31`, `137`) y dispara la campaña con automatización (`34`, `128`). Para las señales de **evento** (cambió de cargo, levantó ronda, está contratando), que son otra familia de timing → `37`. Intent avanzado a fondo → `131`.
