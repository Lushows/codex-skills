# 269 — Registro sanitario en Colombia, paso a paso (y qué te va a frenar)

Sacar el registro sanitario de un suplemento dietario ante el INVIMA no es un trámite de papeles: es
**entregar el expediente técnico de un producto que ya existe, ya se fabricó bajo control y ya se analizó**.
La gente se frena en el paso 1 porque intenta radicar antes de tener química. Este módulo pone el orden
real, lo que cuesta y dónde se cae la gente.

Términos: **registro sanitario (sanitary registration)** = autorización previa del INVIMA para fabricar,
importar y comercializar. · **titular** = quien queda como responsable del registro. · **fabricante /
maquilador (contract manufacturer)** = quien físicamente produce. · **BPM (GMP)** = buenas prácticas de
manufactura. · **requerimiento** = la carta del INVIMA pidiendo que completes o corrijas; para el reloj.

## Antes de radicar: los cuatro prerrequisitos

No se pueden saltar. Si te falta uno, el trámite se cae o se vuelve eterno.

| # | Prerrequisito | Cómo se comprueba |
|---|---|---|
| 1 | Empresa formal con objeto social y RUT | Cámara de comercio + RUT (rutea a `AVIS_lushows`) |
| 2 | Fabricante con capacidad y BPM verificable | Certificado / acta de visita; si maquilas, contrato + documentos del maquilador (`284`) |
| 3 | Producto definido y estable | Fórmula cuali-cuantitativa cerrada, envase definido, lotes piloto hechos |
| 4 | Expediente analítico | Identidad, composición, contaminantes, microbiología, estabilidad (`282`, `286`) |

## El trámite, en orden (a agosto de 2026)

1. **Clasifica la casilla.** Suplemento dietario (Decreto 3249 de 2006) o producto fitoterapéutico
   (Decreto 1156 de 2018). No es una elección de marketing: depende de la composición y del uso previsto.
   Ver `270`. Si dudas, **consulta previa al INVIMA por escrito** y guarda la respuesta.
2. **Verifica cada ingrediente.** Que esté permitido, en la forma química permitida y bajo el nivel máximo
   de ingesta aplicable. Busca conceptos previos en actas de la Sala Especializada.
3. **Cierra la fórmula cuali-cuantitativa** con función de cada componente (activo, excipiente, aditivo) y
   su especificación de materia prima (`141`).
4. **Fabrica lotes piloto** —tres suele ser el mínimo razonable para hablar de especificación— con
   documentación de lote (`168`).
5. **Analiza en laboratorio acreditado ISO/IEC 17025** (`107`, `108`): identidad, contenido del marcador,
   metales pesados, micotoxinas si aplica, microbiología, humedad.
6. **Corre estabilidad** para justificar la vida útil declarada (`164`, `165`). Sin esto, la fecha de
   vencimiento del rótulo es un invento.
7. **Arma el expediente** (`286`) y el arte de etiqueta con las leyendas obligatorias (`272`).
8. **Paga la tarifa y radica** por el sistema en línea del INVIMA.
9. **Responde requerimientos** dentro del plazo. Cada requerimiento reinicia tiempo: por eso el expediente
   completo desde el día uno es lo más barato que puedes hacer.
10. **Radica aparte la publicidad** (art. 24 del Decreto 3249): la pieza publicitaria requiere aprobación
    previa. El registro **no** la incluye.

## Costos y tiempos

Tarifas 2026 para registro sanitario nuevo o renovación de suplemento dietario del Decreto 3249, según el
manual tarifario del INVIMA (`invima.gov.co`, consultado agosto de 2026; **verificar vigencia y código
antes de pagar**):

| Forma farmacéutica | Tarifa (COP) |
|---|---|
| Líquida | 5.553.851 |
| Semisólida | 5.589.477 |
| Sólida | 5.837.164 |

Presupuesto realista del proyecto completo **(ILUSTRATIVO — cotiza tú)**:

```
Tarifa INVIMA (forma sólida)                       $  5.837.164
Análisis de producto terminado, 3 lotes            $  ? — cotizar (ver 291)
Estudio de estabilidad (acelerada + natural)       $  ? — cotizar
Asesoría regulatoria / abogado sanitario           $  ? — cotizar
Arte de etiqueta y ajuste de empaque               $  ? — ver directorcreativo_lushows
------------------------------------------------------------------
Total                                              cotizar, no adivinar
```

**Vigencia del registro:** diez (10) años, renovables por períodos iguales (Decreto 3249 de 2006, art. 13;
numeración tomada de compilación normativa, verificar en texto oficial).

**Tiempo de trámite:** el INVIMA publica términos por tipo de trámite en su portal de trámites y servicios.
**No inventes un plazo**: consulta el término legal vigente en `invima.gov.co` → Trámites y servicios, y
súmale el tiempo de tus propios requerimientos, que suele ser el que manda.

## Cómo se comprueba que quedó bien

- El registro aparece en `consultaregistro.invima.gov.co` con el nombre exacto del producto, el titular y
  la forma farmacéutica que fabricas.
- El arte impreso coincide **carácter por carácter** con lo aprobado: nombre, contenido, leyendas.
- Cada lote fabricado tiene su COA contra la especificación registrada (`283`).
- Las piezas publicitarias tienen su radicado de aprobación.

Si alguno de los cuatro falla, tienes registro pero sigues expuesto.

## Ejemplo aplicado — BIO-SETA saliendo del hueco

Situación a agosto de 2026: vende extractos de hongos sin registro. Ruta mínima **(ILUSTRATIVA)**:

| Fase | Qué hace | Bloqueo típico |
|---|---|---|
| 0 | Retirar de inmediato claims de enfermedad de web, redes y guion de WhatsApp (`268`) | Miedo a "perder ventas" |
| 1 | Confirmar identidad de especie por ITS y material (cuerpo fructífero vs. micelio) | El proveedor no sabe qué vende |
| 2 | Medir β-glucano y α-glucano por método enzimático, base seca, 3 lotes | El COA del proveedor dice "polisacáridos" |
| 3 | Metales pesados por ICP-MS y microbiología | Sorpresas en cadmio/plomo en hongos |
| 4 | Especificación de producto terminado (`282`) | Un solo lote no basta |
| 5 | Estabilidad y vida útil | Nadie la corrió nunca |
| 6 | Radicar registro y luego publicidad | Radicar sin expediente |

Mientras dura todo esto, el producto **no debería estar en el mercado**. Esa es la conversación incómoda
que hay que tener con el dueño, y es la conversación que esta skill existe para sostener.

## Errores comunes

- **Radicar con el COA del proveedor como único soporte analítico.** No es de tu producto terminado.
- **Declarar una vida útil sin estudio de estabilidad.** Se cae al primer requerimiento.
- **Cambiar el proveedor de extracto después del registro sin control de cambios.** Cambia el producto
  (`169`).
- **Poner en la etiqueta un contenido de activo que solo cumple un lote.** La especificación necesita rango
  y varios lotes.
- **Olvidar la aprobación previa de publicidad.** Es un trámite distinto, con su propio riesgo.
- **Elegir la casilla por conveniencia.** Registrar como suplemento algo que por composición y uso es
  fitoterapéutico es un problema que aparece en la inspección, no en la radicación.

## Conexión con otros módulos

→ `266-invima-y-suplementos-dietarios.md` — la entidad y la norma.
→ `270-fitoterapeuticos-vs-suplementos.md` — cómo elegir la casilla correcta.
→ `282-especificacion-de-producto-terminado.md` — el corazón del expediente.
→ `286-expediente-tecnico-del-producto.md` — el índice completo de la carpeta.
→ `291-costos-de-analisis-y-presupuesto.md` — cuánto vale medir todo esto.