# 10 — ICP: el perfil de cliente ideal (el filtro que todo lo decide)

El **ICP (Ideal Customer Profile)** es la descripción precisa del **tipo de empresa** a la que le vendes mejor: la que más rápido compra, más paga, menos se va y más te refiere. En outbound no es un ejercicio de marketing bonito: es **el filtro operativo** que decide a quién metes en la lista y a quién no. Todo lo demás —los datos, el correo, la cadencia, la herramienta— se construye encima del ICP. Un mensaje perfecto a la empresa equivocada no vende; una lista bien filtrada con un mensaje mediocre igual agenda. Por eso la regla de oro: **ninguna actividad de outbound empieza sin un ICP escrito.**

## Por qué el ICP manda sobre todo lo demás

La matemática es simple. Si tu lista tiene 70% de cuentas que no encajan, el 70% de tu esfuerzo, tus dominios calientes y tu tiempo se queman en gente que nunca iba a comprar. Ese desperdicio no solo cuesta dinero: **quema tu deliverability** (más gente marca como spam lo irrelevante, ver `40`) y **destruye la moral** (respondes menos, ver `04`). Al revés: 300 cuentas que encajan perfecto convierten más que 3.000 al azar, con menos volumen, menos infraestructura y mejor reputación.

**ICP ≠ buyer persona.** El ICP describe la **empresa** (la cuenta: tamaño, sector, tecnología, momento). La buyer persona describe a la **persona** dentro de esa empresa (cargo, dolores, quién decide) — eso vive en `11`. Primero eliges la cuenta correcta; después, dentro de ella, a la persona correcta.

## Cómo construir tu ICP (paso a paso)

No lo inventes en un pizarrón. **Sácalo de tus mejores clientes reales.** Si aún no tienes clientes, usa a los de tu competencia y tu hipótesis, y lo corriges con datos.

1. **Lista tus 10–20 mejores clientes.** "Mejores" = pagaron bien, cerraron rápido, siguen contigo, no dieron problemas. Si no tienes, elige 10 empresas que *deberían* ser tu cliente perfecto.
2. **Busca el patrón.** ¿Qué tienen en común? Sector, tamaño (empleados / facturación), país/ciudad, modelo de negocio, tecnología que usan, cómo llegaron a ti, qué dolor los trajo.
3. **Busca el anti-patrón.** ¿Quiénes fueron tus peores clientes (churn rápido, regatearon, soporte infinito)? Escríbelo: eso son tus **exclusiones** — igual de importantes que las inclusiones.
4. **Escribe los criterios duros (firmographics/technographics)** — los filtros que una herramienta puede aplicar (ver `15`): sector, nº de empleados, geografía, tecnología, señales.
5. **Escribe los criterios blandos** — lo que no se filtra automático pero define encaje: madurez, dolor específico, disposición a cambiar.
6. **Valida con volumen.** ¿Existen suficientes cuentas así para alimentar tu meta? Si tu ICP tiene 40 empresas en todo el país, es demasiado estrecho para outbound puro (ver `13` y `17`).
7. **Itéralo cada mes** con el feedback de qué realmente cierra (`79`).

## Plantilla de ICP rellenable (cópiala)

```
=== ICP — [tu producto] — v1 (fecha) ===

QUÉ VENDO Y QUÉ DOLOR RESUELVO
  Producto/servicio: ____
  Dolor #1 que resuelvo: ____
  Resultado que entrego: ____ (en $ / tiempo / riesgo)

CRITERIOS DUROS (filtrables — ver 15)
  Sector / industria:        ____ (ej. restaurantes, agencias de marketing)
  Tamaño (empleados):        ____ (ej. 10–200)
  Facturación aprox:         ____ (si es filtrable)
  Geografía:                 ____ (país, ciudad, región)
  Modelo de negocio:         ____ (B2B / B2C / e-commerce / SaaS / servicios)
  Tecnología que usan:       ____ (ej. Shopify, HubSpot — ver technographics 15/134)
  Señales/triggers activos:  ____ (contratando, ronda, cargo nuevo — ver 14)

CRITERIOS BLANDOS (encaje cualitativo)
  Madurez / momento:         ____ (ej. ya tienen equipo de ventas pero sin proceso)
  Dolor específico observable: ____
  Disposición a cambiar:     ____

EXCLUSIONES (NO contactar — anti-patrón)
  ____ (ej. > 500 empleados: ciclo muy largo)
  ____ (ej. sector regulado X: no puedo servirlo)
  ____ (ej. freelancers solos: no pagan el ticket)

DECISOR PRINCIPAL (detalle en 11)
  Cargo(s):                  ____
  Champion probable:         ____

TAMAÑO DEL MERCADO (ver 13)
  Cuentas estimadas que cumplen: ____

MENSAJE-MERCADO (ver 18)
  Ángulo que le importa a ESTE ICP: ____
```

## Ejemplo real (LatAm)

```
=== ICP — Software de gestión de costos para restaurantes — v1 ===
QUÉ VENDO: Excel/SaaS que calcula el costo real de cada plato.
  Dolor: no saben cuánto ganan por plato; venden a pérdida sin darse cuenta.

DUROS
  Sector: restaurantes, cafeterías, dark kitchens
  Tamaño: 1–5 sedes / 5–40 empleados
  Geografía: Colombia (Bogotá, Medellín, Cali primero)
  Modelo: food service con carta fija (no eventos)
  Señales: acaban de abrir 2ª sede / contratando chef o admin / publican
           en Rappi con muchos platos

BLANDOS
  Ya tienen POS pero no controlan food cost
  Dueño operativo (mete mano en la cocina y en la plata)

EXCLUSIONES
  Cadenas > 10 sedes (ya tienen ERP)
  Food trucks de 1 persona (no pagan / no lo priorizan)
  Restaurantes de menú degustación que cambian carta a diario

DECISOR: dueño / socio operativo. Champion: administrador o chef ejecutivo.
MERCADO: ~15.000 restaurantes formales objetivo (ver cálculo en 13).
MENSAJE: "cuánto ganas REALMENTE por plato" (no "software de gestión").
```

## Errores comunes

- **ICP demasiado amplio** ("cualquier pyme"): no es un ICP, es un deseo. Sin filtro no hay outbound, hay spam.
- **ICP inventado sin mirar tus clientes reales.** El mercado ya te dijo quién compra; escúchalo.
- **Confundir ICP con persona** y saltarte el nivel cuenta.
- **No escribir exclusiones.** Saber a quién NO contactar ahorra más plata que saber a quién sí.
- **Congelarlo.** El ICP es vivo; se afila con cada trimestre de datos (`79`).

## Frontera y siguiente paso

El **ICP a nivel estrategia de negocio** (si ese segmento sostiene tu CAC/LTV y tu modelo) lo decide **`economist_lushows`**; aquí lo usamos como filtro operativo de la máquina de outbound. Cualquier **cálculo exacto** de tamaño o economía → **`Matematicas_lushows`**.

**Siguiente paso:** rellena la plantilla con tus 10 mejores clientes reales. Luego pasa a `11` (a quién dentro de la cuenta), `13` (cuántas cuentas existen) y `16` (cómo priorizarlas en tiers).
