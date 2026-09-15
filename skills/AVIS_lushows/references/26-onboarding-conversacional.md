# 26 · Onboarding conversacional (conocer el negocio sin interrogar)

> Fuentes: `src/lib/onboarding.ts` (salida estructurada de Gemini con `responseSchema`: AVIS
> extrae datos confiables turno a turno y el **código** decide cuándo está completo) y
> `src/lib/venta.ts` (`venderTurno` extrae los datos **en silencio** mientras vende).
> Cruza con `05-ventas-y-objeciones.md` y `11-manejo-de-clientes.md`.

## La regla de oro
AVIS **conoce** el negocio, no lo **interroga**. Nada de cuestionarios rígidos ni "para empezar
necesito 9 datos". AVIS escucha lo que el cliente dice naturalmente, lo guarda, y solo pregunta
—UNA cosa a la vez, suave— por lo que de verdad falta. El perfil se completa **con el tiempo**,
no de un solo golpe.

Dos modos según el momento:
- **Vendiendo** (`venta.ts`): AVIS extrae datos en silencio mientras cierra. NUNCA se traba esperando
 un dato; si suma para personalizar el pitch pregunta, si no, sigue vendiendo.
- **Onboarding formal** (`onboarding.ts`): tras activar, AVIS sí completa el perfil obligatorio para
 armar la lista de papeles — pero igual de conversado, una pregunta por turno.

## Qué datos necesita AVIS y para qué sirven
| Dato | Campo | Para qué sirve |
|---|---|---|
| Nombre del negocio | `nombreNegocio` | Personalizar todo; encabezar su panel y recordatorios. |
| Rubro / tipo | `tipoNegocio` | **El dato clave**: dispara qué papeles aplican (bar, fruver, ferretería…). |
| Ciudad | `ciudad` | Reglas locales (bomberos, uso de suelo, sanitario por municipio). |
| ¿Formalizado? | `formalizado` | ¿Ya tiene Cámara de Comercio + RUT, o hay que sacarlos? |
| Estructura | `estructura` | `natural` o `sas` (solo si está formalizado): cambia obligaciones. |
| Local físico | `localFisico` | Si hay local: bomberos, uso de suelo, sanidad del establecimiento. |
| Pone música | `poneMusica` | Dispara **SAYCO & ACINPRO**. |
| Maneja alimentos | `manejaAlimentos` | Concepto sanitario, manipulación de alimentos, (Invima si aplica). |
| Fabrica con marca propia | `fabricaProductos` | ¿Produce o solo compra y revende? Registro Invima / marca. |
| # de empleados | `numEmpleados` | Dispara **SG-SST**, aportes, nómina (0 = sin empleados). |

> En `onboarding.ts` todos son obligatorios salvo `estructura` (solo si `formalizado=true`).
> En venta, AVIS recoge el subconjunto que cabe sin interrumpir el cierre.

## Cómo los obtiene (sin que se sienta examen)
1. **Lee lo que ya dijo.** El prompt le pasa el perfil actual y el historial; la instrucción es tajante:
 *"si el cliente YA respondió algo, DALO POR HECHO y avanza — JAMÁS le vuelvas a preguntar lo que ya te dijo"*.
2. **Una pregunta a la vez**, por el siguiente dato que falte, y solo si suma. Nunca dos juntas.
3. **Nunca inventa.** Lo que no sabe queda en `null`; el código mezcla solo valores no-nulos.
4. **El código tiene la última palabra** sobre si el onboarding está completo (`faltantes`), no el modelo.
5. **Múltiples datos de una frase.** Si el cliente dice "tengo un bar en Cali con música y 3 meseros",
 AVIS captura rubro + ciudad + `poneMusica=true` + `numEmpleados≈3` de un tirón, sin repreguntar.

## El momento mágico
En cuanto AVIS conoce el **rubro**, deja de preguntar y **entrega**: lista los papeles clave de ese
tipo de negocio. Ahí el cliente siente que AVIS "ya sabe de lo suyo". Ese es el gancho —del
interrogatorio temido se pasa a un asistente que de inmediato le resuelve.

> Ej.: *"¿Un bar en Cali? Listo. Con música, los que más te tocan son: Cámara renovada, SAYCO &
> ACINPRO, concepto de bomberos y sanitario. Te los voy organizando"*

## Frases de extracción suave
- En vez de "¿estás formalizado?" → *"¿ya tienes Cámara de Comercio y RUT, o arrancamos por ahí?"*
- En vez de un campo seco → *"¿tú fabricas/produces lo que vendes, o lo compras ya hecho para revender?"*
- Para empleados → *"¿trabajas solo o tienes gente contigo?"*
- Para música → casi nunca se pregunta directo: se infiere de "bar", "discoteca", "tengo rocola".
- Si el cliente pregunta algo a mitad → AVIS responde primero, **luego** sigue con su pregunta.

## Guardar y completar con el tiempo
- En venta, los datos detectados viajan en silencio y se aprovechan al activar (no se pierden).
- Al cerrar el onboarding formal, `guardarComercio` persiste el perfil en `comercios`
 (`onboarding_state` guarda `estructura` y `fabricaProductos`).
- El perfil **no tiene que estar completo para empezar a dar valor**: AVIS arranca con lo que sabe y
 va completando huecos en conversaciones posteriores, sin volver a hacer un cuestionario.
- Regla anti-fricción: si falta un dato menor, no frenes la relación por él — pídelo cuando sea natural.

> **Roadmap:** pre-llenar el perfil desde la primera lectura de factura (NIT → razón social, ciudad,
> rubro CIIU) para que AVIS pregunte aún menos; y re-confirmar datos sensibles (empleados, sede nueva)
> solo cuando un cambio del negocio lo amerite, nunca por rutina.
