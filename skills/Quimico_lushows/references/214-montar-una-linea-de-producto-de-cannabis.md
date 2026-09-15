# 214 — Montar una línea de producto de cannabis (del cultivo al producto registrado)

Este es el módulo de cierre del bloque de cannabis: la ruta completa, en orden, desde la materia prima hasta
un producto que se puede vender sin que te lo retiren del mercado. No es un plan de negocio —para eso está
`economist_lushows`— sino el **plan técnico y de cumplimiento**: qué decisiones se toman en qué orden, qué
análisis hay que pagar en cada etapa, y dónde están los costos que la gente olvida presupuestar. La lección
central es contraintuitiva: **la primera decisión no es qué producto hacer, sino en qué país y en qué
categoría regulatoria va a vivir**, porque eso determina todo lo demás.

Términos: **maquilador (contract manufacturer)** = tercero que fabrica por ti bajo su licencia. **Expediente
técnico (technical dossier)** = el conjunto de documentos que sustentan el producto ante la autoridad.
**Especificación (specification)** = la tabla de ensayo, método, límite y unidad que define si un lote pasa
o no. **Plan analítico (testing plan)** = qué se analiza, en qué punto y con qué frecuencia.

## El orden correcto de las decisiones

```
1. Mercado de destino        → determina el límite de THC y la unidad (% o mg/envase)
2. Categoría regulatoria     → alimento, suplemento, fitoterapéutico, cosmético o medicamento
3. Claim sostenible          → lo que la evidencia y la ley permiten decir
4. Formato y dosis           → derivado de la categoría y del claim
5. Materia prima             → espectro completo, amplio o aislado
6. Fabricación               → propia con licencia, o maquila
7. Especificación            → los números que definen un lote conforme
8. Plan analítico            → qué se mide y cuándo
9. Estabilidad               → para declarar vida útil
10. Expediente y radicación  → ante la autoridad
11. Etiqueta y empaque       → lo último, no lo primero
```

El error que arruina proyectos es hacer esto al revés: diseñar el empaque, imprimir 5.000 etiquetas, y
descubrir en el paso 2 que el claim impreso convierte el producto en medicamento.

## Paso 1–2: el mapa de límites, resumido (a agosto de 2026)

| Destino | Límite de THC | Base | Categoría de CBD | Verificar en |
|---|---|---|---|---|
| Colombia | < 1 % THC (incluidas formas ácidas) para "no psicoactivo" | **Peso seco** | Suplemento dietario o fitoterapéutico vía INVIMA | normograma.invima.gov.co; Decreto 811 de 2021 |
| EE.UU. (nueva definición) | **0,4 mg de THC total por envase** | Producto final | CBD **excluido** de suplemento dietario por la FDA | congress.gov (Sec. 781, P.L. 119-37); fda.gov |
| UE | 3,0 mg/kg (semilla y derivados secos); 7,5 mg/kg (aceite de semilla) | Producto | CBD **no** está en la lista de la Unión | EUR-Lex Reg. (UE) 2022/1393; food.ec.europa.eu |

En EE.UU., el aplazamiento de la nueva definición hasta el 11 de diciembre de 2026 fue aprobado por el
Senado el 8 de agosto de 2026 y **a mediados de agosto de 2026 seguía pendiente en la Cámara**; la fecha
vigente sin ese cambio es el 12 de noviembre de 2026 (ver `211`). Confirma el estado el día que decidas.

## Paso 5–6: fabricar o maquilar

| Criterio | Fabricación propia | Maquila |
|---|---|---|
| Licencia | La necesitas tú (INVIMA, en Colombia) | La tiene el maquilador |
| Inversión inicial | Alta (planta, equipos, BPM) | Baja |
| Control de calidad | Total | Depende de la auditoría que le hagas |
| Tiempo hasta el primer lote | Largo | Corto |
| Confidencialidad de fórmula | Alta | Requiere acuerdo |
| Costo por unidad a volumen bajo | Alto | Menor |

Para casi todo el que empieza, **maquilar es la respuesta correcta**, con una condición: auditar al
maquilador de verdad (licencia vigente, BPM, historial de análisis, manejo de desviaciones) y no solo por
teléfono (ver `284`, `292`).

## Paso 7: la especificación, que es el corazón del asunto

Una especificación es una tabla, no una promesa. Este es el esqueleto para un aceite con CBD:

| Ensayo | Método | Unidad y base | Límite | Frecuencia |
|---|---|---|---|---|
| CBD total | HPLC-DAD | mg/mL | 90–110 % del declarado | Cada lote |
| THC total | HPLC-DAD o LC-MS/MS | mg/mL y mg/envase | Según destino | Cada lote |
| Perfil de cannabinoides | HPLC-DAD | mg/mL | Informativo | Cada lote |
| Identidad del aceite portador | FTIR o perfil de ácidos grasos | — | Coincide con patrón | Cada lote de materia prima |
| Metales pesados | ICP-MS | mg/kg | Según destino | Cada lote de materia prima; periódico en terminado |
| Pesticidas | LC-MS/MS + GC-MS/MS | µg/kg | Según destino | Cada lote de materia prima |
| Solventes residuales | GC-MS headspace | ppm | Según destino | Cada lote de extracto |
| Micotoxinas | LC-MS/MS | µg/kg | Según destino | Cada lote de materia prima |
| Microbiología | Según norma de la categoría | UFC/g, ausencia/25 g | Según destino | Cada lote |
| Índice de peróxidos | AOCS | meq O2/kg | Según especificación | Periódico |
| Llenado / contenido neto | Gravimetría | mL o g | Según norma metrológica | Cada lote |

Regla de oro: **un solo lote no es una especificación**. Los límites se fijan con al menos tres lotes y un
rango, no con el resultado del primero (ver `282`).

## Paso 8: el plan analítico y su costo

Órdenes de magnitud **(ILUSTRATIVO)** para Colombia, en pesos colombianos, para dimensionar la conversación.
Cotiza con tu laboratorio; los precios varían mucho por matriz y por volumen:

| Ensayo | Orden de magnitud por muestra |
|---|---|
| Perfil de cannabinoides (HPLC-DAD) | cientos de miles de COP |
| Terpenos (GC-MS) | cientos de miles de COP |
| Metales pesados (ICP-MS, 4 elementos) | cientos de miles de COP |
| Pesticidas multiresiduo (panel amplio) | del orden de un millón de COP o más |
| Solventes residuales | cientos de miles de COP |
| Microbiología completa | cientos de miles de COP |
| Micotoxinas | cientos de miles de COP |
| **Panel completo por lote** | **suma de los anteriores; suele ser el mayor costo variable oculto del producto** |
| Estudio de estabilidad (3 lotes, 5 puntos) | decenas de millones de COP en total |

Este es el renglón que casi nadie presupuesta y el que más proyectos hunde: si tu lote es de 200 unidades y
el panel completo cuesta 3 millones de COP, estás cargando 15.000 COP de análisis por unidad. **El tamaño de
lote se decide, en parte, por el costo del análisis**. Modela esto con `Matematicas_lushows` y
`economist_lushows`, y contabilízalo como costo de producción con `contador_lushows`.

## Paso 9–11: estabilidad, expediente y etiqueta

- **Estabilidad**: ICH Q1, condición de zona climática IVb para Colombia (30 °C / 75 % HR), tres lotes,
  puntos a 0-3-6-9-12-18-24 meses. Sin esto, la fecha de vencimiento es inventada (ver `204`).
- **Expediente técnico**: fórmula cuali-cuantitativa, especificaciones de materia prima y producto terminado,
  métodos analíticos y su validación, estudios de estabilidad, descripción del proceso, controles en proceso,
  información de envase, y la etiqueta proyectada (ver `286`).
- **Etiqueta**: se diseña **al final**, cuando ya sabes qué puedes decir. Debe llevar el porcentaje de THC en
  el caso colombiano, la porción, las advertencias de seguridad (embarazo, conducción, interacciones,
  ver `209`) y ningún claim de enfermedad (ver `268`, `272`). Para el arte, rutea a
  `directorcreativo_lushows`; para cómo se comunica al cliente, a `ventas_lushows`.

## Ejemplo aplicado (ILUSTRATIVO)

Proyecto: aceite de CBD para venta en Colombia, categoría suplemento dietario, lotes de 1.000 frascos de
30 mL a 300 mg de CBD.

| Etapa | Decisión | Dato clave |
|---|---|---|
| Mercado | Colombia | Límite THC < 1 % en peso seco (Decreto 811, art. 2.8.11.1.3) |
| Categoría | Suplemento dietario | Ingrediente debe estar en las referencias o ir a Sala Especializada de la Comisión Revisora |
| Claim | Solo composición: "cada mL aporta 10 mg de CBD" | Verificable por HPLC-DAD, lote a lote |
| Materia prima | Extracto de espectro amplio, THC total 0,15 % p/p | Proveedor con licencia de derivados no psicoactivos |
| Fabricación | Maquila con tercero licenciado | Auditoría previa documentada |
| Especificación de CBD | 9,0–11,0 mg/mL | 90–110 % del declarado |
| Vida útil | A determinar por estudio | Provisional 12 meses hasta tener datos de 24 |
| Costo analítico por lote | ~3.000.000 COP en panel completo | 3.000 COP por frasco |

Cifras **(ILUSTRATIVO)**. Lo que este ejercicio deja claro: el claim más defendible del mercado colombiano
hoy **no es un beneficio de salud, es la verificabilidad**. En un sector donde muchos productos no contienen
lo que dicen, "esto tiene exactamente lo que dice y aquí está el COA del lote" es un diferenciador real y
sostenible (ver `293`).

## Errores comunes

- **Empezar por el empaque.** Imprimir etiquetas antes de saber la categoría regulatoria es quemar plata.
- **No presupuestar el costo analítico por lote.** Es el costo oculto que define el tamaño mínimo de lote.
- **Copiar la especificación de otro producto.** La especificación es tuya y se construye con tus lotes.
- **Confiar en el COA del proveedor como único control.** Se verifica por muestreo propio (ver `283`).
- **Declarar vida útil sin estudio de estabilidad**, y en la condición climática equivocada.
- **Diseñar el producto sin mirar el límite del mercado de destino.** Un envase grande puede volverte ilegal
  en EE.UU. aunque la concentración sea baja (ver `211`).
- **Olvidar que el marco cambia.** Todo dato regulatorio de este módulo está fechado a agosto de 2026;
  verifícalo antes de decidir.

## Conexión con otros módulos

→ `140-de-la-materia-prima-al-producto.md` — el arco general de desarrollo.
→ `210-cannabis-medicinal-en-colombia.md` — licencias y registro en Colombia.
→ `211-hemp-y-cbd-en-estados-unidos-2026.md` y `212-cannabis-y-cbd-en-europa.md` — los otros mercados.
→ `282-especificacion-de-producto-terminado.md` y `283-plan-de-control-de-calidad-por-lote.md` — el corazón.
→ `286-expediente-tecnico-del-producto.md` — el paquete que se radica.
→ `291-costos-de-analisis-y-presupuesto.md` y `292-negociar-con-laboratorios-y-maquiladores.md` — la plata.
→ `213-como-leer-un-coa-de-cannabis.md` — la herramienta diaria de control.