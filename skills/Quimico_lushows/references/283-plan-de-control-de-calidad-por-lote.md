# 283 — Plan de control de calidad por lote (qué se ensaya, cuándo y con qué criterio)

La especificación (`282`) dice *qué debe cumplir* tu producto. El plan de control dice *cómo lo compruebas
en la vida real, lote tras lote, sin quebrarte*. Es una tabla de una página que responde cuatro cosas por
cada ensayo: qué se mide, con qué método, cada cuánto, y qué pasa si sale fuera. Sin este plan ocurre el
error caro más frecuente de una marca pequeña: se analiza el primer lote a fondo, se publica ese COA en la
página web como si fuera el de todos, y tres lotes después llega un cliente B2B (o el INVIMA) pidiendo el
COA del lote que efectivamente le vendieron — que nunca existió.

Términos: **lote (batch/lot)** = cantidad producida bajo condiciones uniformes e identificada con un código
único. **ensayo (test)** = una determinación analítica concreta. **criterio de aceptación (acceptance
criterion)** = el límite numérico que separa "libera" de "no libera". **liberación de lote (batch release)**
= la decisión firmada de que ese lote puede venderse. **skip-lot** = ensayar solo 1 de cada N lotes, con
justificación documentada. **OOS (out of specification)** = resultado fuera de especificación.

## Los tres puntos de control

Todo plan tiene tres columnas de la vida del producto. Si te falta una, tienes un hueco.

```
MATERIA PRIMA  →  [PROCESO: controles en línea]  →  PRODUCTO TERMINADO  →  ESTABILIDAD (en el tiempo)
   ¿entra bien?        ¿se está haciendo bien?          ¿salió bien?          ¿sigue bien a los 12 meses?
```

## Tabla 1 — Control de materia prima (entrada)

Ejemplo para un extracto de hongo comprado a un proveedor **(ILUSTRATIVO — ajusta a tu producto)**:

| Qué se ensaya | Método | Frecuencia | Criterio de aceptación | Si falla |
|---|---|---|---|---|
| Identidad de especie | ITS / ADN barcoding (`103`, `245`) | 1er lote de cada proveedor + cambio de origen | Coincidencia ≥ 99 % con la especie declarada | Rechazo total, no negociable |
| Identidad organoléptica | Inspección visual, olor, color vs muestra patrón | 100 % de los lotes | Conforme a patrón de referencia retenido | Cuarentena + ensayo instrumental |
| β-glucano | Enzimático Megazyme K-YBGL (`221`) | 100 % de los lotes (año 1); skip-lot 1 de 3 tras 6 lotes conformes | ≥ 20 % p/p base seca **(ILUSTRATIVO)** | Devolución o renegociación de precio |
| α-glucano | Mismo kit, misma corrida (`220`) | Junto con β-glucano | ≤ 15 % p/p base seca **(ILUSTRATIVO)** | Sospecha de micelio en grano (`218`) |
| Humedad | Gravimetría 105 °C o Karl Fischer (`98`) | 100 % de los lotes | ≤ 8,0 % p/p | Ajuste de base seca o rechazo |
| Metales pesados (Pb, Cd, As, Hg) | ICP-MS (`88`) | 1 de cada 3 lotes + cambio de origen | Dentro del límite de la norma vigente (`243`) | Rechazo, no se "promedia" |
| Micotoxinas (aflatoxinas B1/total, OTA) | LC-MS/MS (`101`) | 1 de cada 3 lotes | Bajo límite normativo vigente | Rechazo |
| Microbiología (aerobios, hongos/levaduras, *E. coli*, *Salmonella*) | Métodos oficiales (`100`) | 100 % de los lotes | Según especificación | Rechazo |
| COA del proveedor completo | Revisión documental (`110`, `111`) | 100 % de los lotes | Con método, lote, fecha y firma | No se recibe la mercancía |

Regla dura: **el COA del proveedor no reemplaza tu verificación**. Se acepta como soporte, pero al menos
un ensayo confirmatorio propio por proveedor y por año (típicamente identidad + activo) es lo mínimo
defendible. Si el proveedor está calificado formalmente (`284`), puedes reducir — no eliminar.

## Tabla 2 — Controles en proceso (in-process controls)

| Etapa | Qué se controla | Método | Frecuencia | Criterio |
|---|---|---|---|---|
| Molienda | Granulometría | Tamizado (`143`) | Cada lote | ≥ 90 % pasa malla 80 **(ILUSTRATIVO)** |
| Extracción | Temperatura y tiempo | Registro del equipo | Continuo | Dentro de ±3 °C y ±10 min del maestro |
| Concentración | Sólidos totales / °Brix | Refractómetro o gravimetría | Cada 30 min | Rango definido en el maestro |
| Secado | Humedad del polvo a la salida | Balanza halógena | Cada tanda | ≤ 6,0 % p/p |
| Mezclado | Uniformidad de mezcla | 10 tomas del mezclador, ensayo del activo | Validación + cada cambio de escala | RSD ≤ 5 % |
| Encapsulado | Peso individual | Balanza analítica, 20 cápsulas cada 30 min | Continuo | ±5 % del peso objetivo |
| Envasado | Sellado / hermeticidad | Prueba de vacío o inmersión | Inicio, medio y fin de lote | Sin fugas |

Los controles en proceso son los baratos y los que de verdad salvan el lote: detectan el problema cuando
todavía se puede corregir. El ensayo de producto terminado solo te dice si hay que botar todo.

## Tabla 3 — Producto terminado (liberación de lote)

| Qué se ensaya | Método | Frecuencia | Criterio de aceptación |
|---|---|---|---|
| Descripción y aspecto | Visual vs patrón | 100 % de los lotes | Conforme |
| Peso o volumen de llenado | Gravimetría, n = 20 | 100 % de los lotes | Promedio ≥ declarado; ninguna unidad < −5 % |
| Contenido de activo (label claim) | HPLC-UV o enzimático validado (`75`) | 100 % de los lotes | 90–120 % de lo declarado **(ILUSTRATIVO; fija tu rango y susténtalo)** |
| Humedad / actividad de agua | KF o a_w (`35`, `98`) | 100 % de los lotes | a_w ≤ 0,60 |
| Microbiología completa | Métodos oficiales (`100`) | 100 % de los lotes | Según especificación |
| Metales pesados | ICP-MS | 1 de cada 5 lotes si materia prima ya se controló | Límite normativo |
| Disgregación (cápsulas) | Farmacopea USP/EP (`280`) | 1 de cada 3 lotes | ≤ 30 min |
| Estabilidad de seguimiento | Plan de estabilidad (`164`) | 1 lote por año | Cumple hasta el vencimiento declarado |

## Cómo se decide la frecuencia (y cómo se justifica bajarla)

No se baja "porque sale caro". Se baja **con datos**. El argumento defendible es este:

```
Regla práctica de reducción (documéntala en el plan):
1. Ensayo al 100 % de los lotes durante los primeros 6 lotes o 12 meses (lo que sea mayor).
2. Si los 6 resultados están dentro de especificación Y dentro de ±1/3 del ancho de la especificación
   (proceso capaz, ver carta de control en `77`), se pasa a skip-lot 1 de cada 3.
3. Cualquier OOS, cambio de proveedor, de sustrato, de escala o de equipo → se vuelve al 100 %.
4. Los ensayos de SEGURIDAD que dependen del origen (metales, micotoxinas, pesticidas, patógenos)
   nunca bajan de 1 de cada 3, y vuelven al 100 % si cambia el origen geográfico.
```

## Qué hacer cuando un resultado sale fuera (OOS)

El error de principiante es repetir el análisis hasta que dé bien. Eso se llama *testing into compliance*
y es exactamente lo que un auditor busca. El procedimiento correcto:

1. **No repitas todavía.** Primero investiga si hubo error de laboratorio documentable (dilución mal
   registrada, patrón vencido, columna fuera de control). Sin causa asignable, el resultado vale.
2. **Registra la investigación** con fecha, responsable y hallazgo (`169`).
3. Si hay causa asignable: se repite el ensayo original según el procedimiento, y **se reportan ambos**.
4. Si no hay causa asignable: el lote **no se libera**. Se decide destrucción, reproceso o degradación de
   uso, y queda escrito.
5. Si el lote ya estaba en el mercado: evalúa retiro y avisa. Aquí entra `AVIS_lushows` para la parte
   operativa y de comunicación con autoridad.

## Ejemplo aplicado (BIO-SETA)

Marca con 2 referencias (cápsulas de reishi y de melena de león), 6 lotes al año de 3.000 unidades cada uno.
Plan mínimo defendible **(ILUSTRATIVO)**:

- Materia prima: identidad ITS en el primer lote de cada proveedor; β/α-glucano y humedad en cada lote;
  metales y micotoxinas 1 de cada 3.
- En proceso: humedad a la salida del secado y peso de cápsula en cada lote.
- Terminado: aspecto, peso, β-glucano, a_w y microbiología en cada lote; metales 1 de cada 5.
- Estabilidad: 1 lote/año en tiempo real a 30 °C / 75 % HR (`164`).

Conteo anual de ensayos: 12 β-glucano de materia prima + 12 de terminado + 4 paquetes de metales +
4 de micotoxinas + 12 microbiologías + 1 estudio de estabilidad. El costo de todo eso y cómo presupuestarlo
está en `291`; cómo negociar el paquete completo con un solo laboratorio, en `292`.

## Errores comunes

- **Publicar un COA sin lote.** Un COA sin código de lote no certifica nada y es una bandera roja para
  cualquier comprador B2B.
- **Analizar solo el activo y ninguna seguridad.** El activo te da la etiqueta; los metales y la
  microbiología te dan el permiso de existir.
- **Muestrear del envase de arriba.** Sin plan de muestreo (`66`) el resultado no representa el lote.
- **No guardar contramuestra.** Sin material retenido del mismo lote no puedes impugnar nada (`112`).
- **Repetir hasta que dé.** Testing into compliance: si el auditor lo ve, todo tu sistema pierde credibilidad.
- **Copiar el plan de otra empresa** sin ajustar la frecuencia a tu propio historial de datos.

## Conexión con otros módulos

→ `282-especificacion-de-producto-terminado.md` — los criterios que este plan verifica.
→ `284-auditoria-de-proveedor.md` — cómo justificar reducir ensayos de entrada.
→ `77-control-de-calidad-analitico-y-cartas-control.md` — la evidencia estadística para bajar la frecuencia.
→ `168-documentacion-de-lote-y-trazabilidad.md` — dónde vive el registro del lote.
→ `291-costos-de-analisis-y-presupuesto.md` — cuánto cuesta este plan al año.
→ `298-plantillas-y-formatos.md` — el formato de registro de lote listo para usar.