# 109 — Cadena de custodia y envío de muestras (el resultado empieza mucho antes del instrumento)

El mejor laboratorio del mundo no puede arreglar una mala muestra. La **cadena de custodia (chain of custody,
CoC)** es el registro documentado de quién tuvo la muestra, cuándo, en qué condiciones y qué le hizo, desde
que se tomó hasta que se destruye. Sin ella, el resultado sigue siendo un número, pero deja de ser una
**prueba**: no defiende un lote ante una autoridad, no sostiene una reclamación a un proveedor y no aguanta
una auditoría de cliente. Y hay un detalle que decide más que todo lo anterior: **quién tomó la muestra**. Si
la tomó el proveedor, el COA describe lo que él quiso mandar, no tu lote.

Términos: **cadena de custodia (CoC)** = registro de trazabilidad de la muestra y sus responsables.
**muestra primaria (primary/increment sample)** = cada toma individual del lote. **muestra compuesta
(composite sample)** = mezcla homogénea de varias primarias. **contramuestra (retained/reserve sample)** =
porción idéntica que se guarda para reanálisis o disputa. **precinto (tamper-evident seal)** = sello que se
rompe al abrir. **blanco de terreno (field blank)** = muestra limpia que viaja igual, para detectar
contaminación del transporte.

## La regla que casi nadie cumple: la muestra la tomas tú

| Quién toma la muestra | Qué demuestra el resultado | Uso legítimo |
|---|---|---|
| Tú o un tercero independiente, con CoC | El estado real del lote | Liberación, disputa, exportación |
| El laboratorio (muestreo acreditado, cláusula 7.3 de ISO 17025) | El estado real del lote, con respaldo del acreditador | Lo más defendible; cuesta más |
| El proveedor, y te manda la muestra | Lo que el proveedor decidió mandar | Referencia comercial, nada más |
| Nadie sabe (COA que llegó por WhatsApp) | Nada | Ninguno |

Esto no es paranoia: es la razón por la que un mismo lote puede dar 30 % y 12 % de β-glucano. Un polvo mal
homogeneizado da varios puntos de diferencia entre dos tomas (`66`, `67`), y quien toma la muestra elige,
consciente o inconscientemente, de dónde saca la cucharada.

## Los campos obligatorios de un formato de cadena de custodia

```
FORMATO DE CADENA DE CUSTODIA — [tu empresa]                     CoC No. ______

1. IDENTIFICACION
   Codigo unico de muestra .............. (irrepetible, va en el envase y en el formato)
   Producto / material .................. (descripcion exacta: "polvo de cuerpo fructifero, Ganoderma")
   Lote de produccion ................... (el que aparece en el producto)
   Tamano del lote ...................... (kg o unidades: define cuantas primarias, ver 66)

2. TOMA
   Fecha y hora de toma ................. (dd-mmm-aaaa hh:mm)
   Lugar exacto ......................... (bodega, tanque, punto de uso)
   Quien tomo la muestra ................ (nombre, cargo, firma)
   Plan de muestreo aplicado ............ (No. de primarias, si es compuesta, referencia al SOP)
   Cantidad enviada ..................... (g o mL) y contramuestra retenida (g o mL)

3. CONDICIONES
   Envase ............................... (bolsa de barrera, frasco ambar, vial con septum)
   Preservacion ......................... (ambiente / refrigerado 2-8 C / congelado -20 C / oscuridad)
   Precinto No. ......................... (numero del sello)

4. TRANSFERENCIAS (una linea por cada cambio de manos)
   Entrega: nombre, firma, fecha/hora  |  Recibe: nombre, firma, fecha/hora  |  Estado del precinto

5. RECEPCION EN LABORATORIO
   Fecha/hora de recepcion .............. Temperatura al llegar ....... Precinto integro: SI / NO
   Observaciones de conformidad de la muestra

6. ENSAYOS SOLICITADOS
   Analito | Metodo exigido | Matriz | Base de reporte | Limite/spec | Urgencia
```

El campo 6 es el que más plata ahorra: si no especificas el **método** y la **base de reporte**, el
laboratorio elige, y puede elegir el método barato que no mide lo que crees (ver `91`, `222`).

## Cuánta muestra, en qué envase y cómo viaja

| Ensayo | Cantidad típica | Envase | Condición de transporte |
|---|---|---|---|
| Humedad / aW | 20–50 g | Bolsa de barrera sellada, sin aire | Ambiente, sellada de inmediato |
| β/α-glucano (K-YBGL) | 20–50 g de polvo | Bolsa o frasco hermético | Ambiente, seco |
| Cannabinoides / terpenos | 5–15 g | Frasco ámbar, lleno hasta arriba | Fresco y oscuro; terpenos se pierden |
| Metales pesados | 20–50 g | **Envase plástico libre de metales**, no metálico | Ambiente |
| Micotoxinas | 100–500 g (heterogeneidad alta) | Bolsa, muestra bien compuesta | Seco, ambiente |
| Microbiología | 50–100 g, **envase estéril** | Estéril, sin abrir en el camino | 2–8 °C, llegar en 24–48 h |
| Solventes residuales | 2–5 g | Vial de headspace con septum, **lleno** | Frío, mínimo espacio de cabeza |
| Agua | 100 mL–1 L según panel | Según parámetro (estéril para micro) | 2–8 °C, tiempos de retención cortos |

Cantidades **(ILUSTRATIVO)**: cada laboratorio pide lo suyo. La regla que no cambia: manda **al menos el
triple** de lo que el método consume, para que alcance para reanálisis sin volver a muestrear, y **guarda
siempre una contramuestra** del mismo material, sellada y en las mismas condiciones. Sin contramuestra no
hay impugnación posible (ver `112`).

## Los cinco errores de transporte que destruyen el resultado

1. **Calor y luz** en muestras con terpenos, cannabinoides ácidos o psilocibina: se degradan en tránsito y el
   resultado sale bajo sin que nadie haya hecho nada mal en el laboratorio (`204`, `255`).
2. **Espacio de cabeza** en solventes residuales: el volátil migra al aire del vial y "desaparece" (`87`).
3. **Envase equivocado**: bolsa plástica para metales trazas, frasco no estéril para microbiología, plástico
   blando para muestras con aceites.
4. **Muestra caliente y sellada**: condensa, sube la aW y arruina humedad y microbiología (`35`).
5. **Fin de semana en la aduana**: mandar el jueves una muestra microbiológica que necesita llegar en 48 h.

Un **blanco de terreno** —un envase igual, con material limpio, que viaja y se analiza junto con las
muestras— es el detector barato de la contaminación de transporte. Cuesta un ensayo más y resuelve
discusiones enteras.

## Ejemplo aplicado (ILUSTRATIVO)

Lote de 240 kg de polvo de reishi en 12 sacos de 20 kg. Muestreo para liberación:

```
Plan (ver 66): n = raiz(12) redondeado hacia arriba = 4 sacos, elegidos al azar
Toma         : 3 incrementos por saco (arriba, medio, fondo) con calador = 12 primarias x ~150 g
Compuesta    : 1,8 kg homogeneizados y cuarteados (ver 67) -> 4 porciones de ~450 g
Destino de las porciones:
  Porcion 1 -> laboratorio, ensayos del COA (beta/alfa-glucano, humedad, metales)
  Porcion 2 -> CONTRAMUESTRA sellada y precintada, guardada 24 meses en tu bodega
  Porcion 3 -> segundo laboratorio (solo si hay disputa, ver 112)
  Porcion 4 -> retencion para estabilidad / trazabilidad
Precintos    : 4 numeros consecutivos, anotados en el formato de CoC
Envio        : bolsa de barrera + caja rigida + guia; foto del precinto antes de cerrar
```

Costo del ejercicio: unas horas de trabajo y ~1,8 kg de producto que no se vende. Beneficio: si el resultado
sale mal, tienes con qué discutir; si el cliente reclama en ocho meses, tienes el material del lote. Cifras
**(ILUSTRATIVO)**; el cálculo del número de incrementos va a `Matematicas_lushows`.

## Errores comunes

- **No guardar contramuestra.** Sin ella, impugnar es imposible: solo queda pagar otro lote de análisis.
- **Muestra que manda el proveedor.** El resultado describe su elección, no tu lote.
- **Un solo incremento del saco de arriba.** Es la muestra más cómoda y la menos representativa (`66`).
- **No sellar ni precintar.** Cualquiera puede alegar que la muestra se cambió, incluido tú.
- **No anotar fecha y hora de toma.** Después no se puede reconstruir nada.
- **No declararle al laboratorio el método y la base exigidos.** Elige él, y elige barato.
- **Guardar la contramuestra en condiciones distintas** a las de la muestra enviada: ya no son comparables.

## Conexión con otros módulos

→ `66-plan-de-muestreo-y-representatividad.md` — cuántas tomas y de dónde. La base de todo esto.
→ `67-homogeneizacion-y-molienda-de-muestra.md` — cuartear y homogeneizar antes de dividir.
→ `112-como-impugnar-un-resultado.md` — para qué existe realmente la contramuestra.
→ `108-como-elegir-un-laboratorio.md` — a quién le mandas la muestra y qué le exiges por escrito.
→ `168-documentacion-de-lote-y-trazabilidad.md` — cómo se amarra la CoC al expediente del lote.
→ `110-como-leer-un-coa.md` — el campo "quién tomó la muestra" que casi ningún COA trae.
