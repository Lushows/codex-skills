# 20 — Fundamentos de list building

Construir la lista (list building = armar el listado de empresas y personas a contactar) es la fase que más decide el resultado de todo tu outbound, y la que casi todos hacen a la carrera. Antes de escribir una sola palabra de correo, antes de elegir herramienta, antes de calentar un dominio: está la lista. Un mensaje perfecto a la persona equivocada no vende nada; un mensaje mediocre a la persona correcta en el momento correcto agenda. Este módulo fija la mentalidad y el estándar de calidad; los siguientes (`21`–`29`) son el cómo operativo de cada pieza.

## El principio: la lista es la mitad del resultado

Tu tasa de respuesta positiva es, en la práctica, `calidad_de_la_lista × relevancia_del_mensaje × deliverability`. Si la lista vale 3/10, ni el mejor copy ni la mejor infraestructura la salvan: multiplicas por 0,3. Los números lo confirman: una lista bien filtrada de 200 contactos que **encajan de verdad** con tu ICP (perfil de cliente ideal, ver `10`) rinde más reuniones que 3.000 correos comprados al azar — y no te quema el dominio (ver `40`). **30 cuentas que encajan > 3.000 al azar.**

Regla operativa: **calidad > cantidad, siempre.** Es preferible enviar menos y a mejor gente. El volumen es un medio para llegar a tu meta de reuniones (ver `05` la ecuación del pipeline y `17` cuántos contactos necesitas), no un fin. Enviar más basura solo acelera el día en que Gmail te manda a spam.

## Qué es una lista "buena" — los 5 criterios de calidad

Una fila de tu lista sirve solo si cumple los cinco:

| Criterio | Qué significa | Cómo lo verificas |
|---|---|---|
| **Fit (encaje)** | La empresa cumple tu ICP: sector, tamaño, país, madurez (ver `15` firmographics) | Filtro explícito, no "me suena" |
| **Decisor correcto** | Es la persona con dolor + poder o influencia sobre la compra (ver `11`, `22`) | Cargo/función, no solo nombre bonito |
| **Dato de contacto válido** | Correo que existe y no rebota; teléfono/WhatsApp/LinkedIn reales (ver `23`, `24`) | Verificado (ver `28`) |
| **Señal / timing** | Idealmente hay un disparador (contrataron, levantaron ronda, cambio de cargo) (ver `14`, `37`) | Columna de trigger cuando exista |
| **Ángulo de personalización** | Tienes al menos 1 dato para una primera línea relevante (ver `29`, `52`) | Campo lleno, no vacío |

Si una fila no tiene fit + decisor + dato válido, **no va a la campaña.** Punto.

## El proceso paso a paso (el flujo canónico de sourcing)

1. **Parte del ICP escrito** (ver `10`). Sin filtro no hay lista, hay ruido. Define: sector/nicho, tamaño (empleados/ingresos), país/ciudad, y el cargo objetivo.
2. **Encuentra las CUENTAS** (empresas) que encajan → módulo `21` (LinkedIn, directorios, Cámaras de Comercio, Google Maps, Crunchbase, marketplaces, gremios).
3. **Encuentra al DECISOR** dentro de cada cuenta → módulo `22` (por cargo/función).
4. **Consigue el CORREO** de esa persona → módulo `23` (patrones + herramientas + verificación).
5. **Consigue teléfono/WhatsApp/social** si tu canal lo pide → módulo `24`.
6. **Verifica y limpia** (quita rebotes, catch-all, duplicados) → módulo `28`.
7. **Enriquece** con los datos que personalizan el mensaje → módulo `29`.
8. **Prioriza** en tiers A/B/C (ver `16`) para gastar tu mejor tiempo en las mejores cuentas.

Este es el corazón de "conseguir clientes/correos por nicho". Los módulos `21`–`29` desarrollan cada paso con herramientas exactas.

## La estructura mínima de tu lista (columnas)

Trabaja en una hoja (Google Sheets, Airtable o Clay — ver `31`). Columnas mínimas:

```
empresa | sitio_web | sector | tamaño_empleados | ciudad/pais |
nombre | apellido | cargo | linkedin_url |
email | email_status(valid/catch-all/invalid) |
telefono | whatsapp |
trigger/señal | angulo_personalizacion | tier(A/B/C) | fuente
```

La columna `fuente` (de dónde salió cada fila) es oro: te dice qué canal de sourcing te da mejores leads para doblar la apuesta.

## Cuánto necesitas construir (dimensiona desde la meta)

No construyas "muchos" — construye **los que tu meta exige**. Ejemplo con números defendibles 2026 para cold email B2B:

- Meta: 10 reuniones/mes.
- Reply rate positivo típico bien hecho: ~2–4 % de los contactados.
- Contactado→reunión: ~30–40 % de las respuestas positivas agendan.
- Entonces por reunión necesitas ~70–120 contactos buenos. Para 10 reuniones: **~900–1.200 contactos/mes** de calidad.

Ese cálculo exacto (con tus propios ratios) hazlo en `17` y verifícalo con `Matematicas_lushows`. El punto: la lista se dimensiona con matemática, no con intuición.

## Errores comunes (qué NO hacer)

- **Comprar listas prehechas.** Están quemadas (todo el mundo les escribió), llenas de rebotes y muchas veces son ilegales (ver `49`). Rebotan, te mandan a spam y arruinan tu dominio.
- **Priorizar volumen sobre fit.** "Metí 5.000 correos" no es un logro; es deuda de deliverability.
- **Saltarte la verificación** (ver `28`). Un 5 % de rebote y ya empiezas a caer en spam.
- **Una sola fuente.** Cruza LinkedIn + directorio + Maps para cubrir más y validar (ver `21`, `130`).
- **Personalizar el nombre y creer que personalizaste.** "Hola {nombre}" no es relevancia (ver `52`).

## Siguiente paso

Ten el ICP escrito (`10`) y abre `21` para sacar la primera tanda de cuentas por tu nicho. Cuando tengas 50 empresas, sigue con `22` (decisor) y `23` (correo). Recuerda la frontera: esta skill **consigue y agenda**; convencer y **cerrar** la conversación vive en `ventas_lushows`.
