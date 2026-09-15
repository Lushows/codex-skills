# 23 — Buffers y control de pH (cómo evitar que tu producto se mueva solo)

Medir el pH es la mitad del trabajo; la otra mitad es que se quede quieto. Un extracto sin capacidad
buffer cambia de pH cuando le agregas un excipiente, cuando el CO₂ del aire se disuelve, o cuando un
componente se degrada y libera ácido. Ese movimiento silencioso es la causa de la mitad de las
"inestabilidades misteriosas" en producto terminado: el activo no se degradó porque sí, se degradó porque
el pH se corrió a la zona donde se degrada. En el laboratorio, además, el buffer es lo que hace que un
método de HPLC dé el mismo tiempo de retención hoy y en seis meses.

Términos: **buffer / solución amortiguadora (buffer)** = mezcla de un ácido débil y su base conjugada que
resiste cambios de pH. **capacidad buffer (buffer capacity, β)** = mol de ácido o base fuerte que hay que
agregar por litro para mover el pH una unidad; mayor cerca del pKa. **fuerza iónica (ionic strength)** =
medida de la concentración total de iones; afecta actividad, solubilidad y separación cromatográfica.
**buffer volátil (volatile buffer)** = el que se evapora en la fuente de un espectrómetro de masas
(formiato, acetato de amonio) y por eso es el único compatible con LC-MS.

## Cómo se elige un buffer, en cuatro decisiones

```
1. pH objetivo        →  elige un buffer con pKa dentro de ±1 unidad del pH objetivo
2. Concentración      →  10–50 mM en análisis; 5–50 mM en producto; más = más capacidad y más problemas
3. Compatibilidad     →  ¿MS? volátil. ¿Oral? aceptado en farmacopea. ¿Metales? sin fosfato con Ca²⁺
4. Etiqueta y sabor   →  citrato sabe, fosfato no; ambos deben declararse (`272`)

Capacidad máxima cuando pH = pKa. A pH = pKa ± 1 ya perdiste ~2/3 de la capacidad.
```

## Los buffers que de verdad vas a usar

| Buffer | pKa útiles | Rango de trabajo | Volátil (MS) | Dónde lo usas |
|---|---|---|---|---|
| Ácido fórmico / formiato de amonio | 3,75 | 2,5–4,8 | Sí | LC-MS/MS de cannabinoides y psilocibina (`83`, `256`) |
| Ácido acético / acetato de amonio | 4,76 | 3,8–5,8 | Sí | LC-MS, extracción QuEChERS (`69`) |
| Citrato (3 pKa: 3,13 / 4,76 / 6,40) | 3,1–6,4 | 2,5–7 | No | Bebidas, gomas, jarabes; también quelante suave |
| Fosfato (2,15 / 7,20 / 12,3) | 2,1 / 7,2 | 5,8–8,0 | No | HPLC-UV clásico, medios biológicos; precipita con Ca²⁺ y Mg²⁺ |
| Ácido tartárico / tartrato | 3,0 / 4,4 | 2,5–5 | No | Alimentos, efervescentes |
| Bicarbonato / carbonato | 6,35 / 10,33 | 6–7 y 9–11 | Parcial | Extracción ácido-base suave (`22`) |
| Tris | 8,06 | 7,0–9,0 | No | Bioquímica y ensayos enzimáticos (`91`) |
| Acetato de sodio + ácido acético | 4,76 | 3,8–5,8 | No | Ensayos enzimáticos de β-glucano (K-YBGL usa acetato y MOPS) (`221`) |

## Cómo se prepara y cómo se documenta

```
Ejemplo: 1 L de buffer acetato 50 mM, pH 4,80
  1. Pesar 4,10 g de acetato de sodio anhidro (PM 82,03) → 50 mmol
  2. Disolver en ~900 mL de agua tipo II
  3. Ajustar a pH 4,80 con ácido acético glacial, con el electrodo calibrado ese día
  4. Aforar a 1 000 mL a 20 °C. Filtrar 0,45 µm si va a HPLC.
  5. Registrar: reactivo, lote, pureza, pesada real, pH final, temperatura, analista, fecha, caducidad

Regla: el buffer de fase móvil se prepara fresco (≤ 7 días refrigerado, ≤ 48 h a temperatura ambiente si
no lleva conservante). El crecimiento microbiano en fosfato es real y tapa columnas.
```

Documentarlo así no es burocracia: si un método falla, la primera pregunta del auditor es "muéstrame la
preparación del buffer" (`168`, `107`).

## Control de pH en producto, no solo en el laboratorio

En una formulación tienes tres herramientas, en este orden de preferencia:

1. **Elegir un pH donde el activo sea estable** — lo determina el estudio de estabilidad forzada (`164`).
2. **Poner un sistema buffer** que sostenga ese pH contra las perturbaciones esperadas.
3. **Ajustar con ácido o base** al final, solo si 1 y 2 no bastan. Un ajuste sin buffer no dura.

Cuidado con la interacción buffer–activo: el citrato quela hierro y cobre, y eso **frena** oxidaciones
catalizadas por metales (útil, `133`); el fosfato precipita calcio y puede enturbiar una bebida
fortificada; el acetato tiene olor a bajas concentraciones y se percibe en un gotero.

## Cómo se mide y se comprueba

| Pregunta | Método | Unidad / criterio |
|---|---|---|
| ¿El pH quedó donde debía? | Potenciometría con electrodo calibrado el día, con ATC | pH ± 0,05 a T declarada (`22`) |
| ¿Tiene capacidad buffer suficiente? | Titular una alícuota con HCl 0,1 N y NaOH 0,1 N | mmol/L por unidad de pH; reportar β |
| ¿Se mueve el pH en almacenamiento? | Medir pH en cada punto del estudio de estabilidad (0, 3, 6, 12 meses) | Deriva ≤ 0,3 unidades es manejable |
| ¿El buffer afecta la separación? | Inyectar el mismo estándar con 10, 25 y 50 mM | Cambio de tR y de forma de pico (`81`) |
| ¿Hay precipitación con excipientes? | Prueba de compatibilidad 1:1, 40 °C, 14 días, inspección visual + HPLC | Turbidez NTU y % de activo (`160`) |
| ¿El buffer es compatible con MS? | Solo volátiles; nada de fosfato ni de detergentes | Supresión iónica medible (`83`) |

## Ejemplo aplicado — bebida de melena de león que se pone turbia

Bebida lista para tomar, 250 mL, extracto acuoso de *Hericium* al 2 % p/v, pH inicial 6,4 sin buffer
**(ILUSTRATIVO)**:

```
Tiempo (meses, 30 °C)   pH     Turbidez (NTU)   β-glucano (mg/porción, K-YBGL)
        0               6,40         12               210
        3               5,85         34               204
        6               5,31         96               189
       12               4,92        210               171

Reformulación con citrato 20 mM, pH ajustado a 4,20:
        0               4,20         10               209
        6               4,18         14               205
       12               4,15         18               201
```

Lectura: el pH bajaba solo (CO₂ disuelto + acidez generada por degradación de azúcares) y arrastraba la
solubilidad del polisacárido hacia la turbidez. No era el activo: era el pH sin control. Además, bajar a
pH 4,2 mete la bebida en el rango donde el riesgo microbiológico cae fuerte (`100`). Dos problemas
resueltos con 20 mM de citrato. El número de β-glucano por porción se sigue midiendo por K-YBGL sobre la
bebida completa, no se calcula del extracto de entrada (`221`, `242`).

## Errores comunes

- Ajustar el pH con NaOH y creer que quedó "bufferado". Ajustar no es amortiguar; sin par conjugado no hay β.
- Usar fosfato en un método que después se quiere pasar a LC-MS. Toca rehacer el método completo (`83`).
- Preparar el buffer "por receta" sin verificar el pH final. Los reactivos hidratados cambian de peso con
  la humedad y la pesada nominal no da el pH nominal.
- No refrigerar ni descartar buffers viejos. Fosfato a temperatura ambiente cría microorganismos en días.
- Poner más buffer del necesario "por si acaso": sube fuerza iónica, cambia la separación, puede salar el
  activo y aporta sabor y sodio a la etiqueta.
- Olvidar que el buffer entra a la lista de ingredientes y a los cálculos de sodio en el rotulado (`272`).
- Medir pH en un producto no acuoso (aceite, polvo seco) y ponerlo en la especificación (`22`).

## Conexión con otros módulos

→ `22-acidos-bases-y-ph.md` — la base teórica y los pKa de tus activos.
→ `164-estabilidad-ich-q1-y-vida-util.md` — donde el pH se vuelve un atributo crítico de calidad.
→ `81-columnas-fases-y-desarrollo-de-metodo-lc.md` — el buffer como parte de la fase móvil.
→ `160-excipientes-y-compatibilidad.md` — cómo el buffer interactúa con lo demás de la fórmula.
→ `100-microbiologia-de-producto.md` — el pH como barrera microbiológica.
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — pH y degradación, con datos.
