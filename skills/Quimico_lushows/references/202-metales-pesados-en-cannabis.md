# 202 — Metales pesados en cannabis (la planta que limpia suelos también los guarda)

El cannabis es un **hiperacumulador (hyperaccumulator)** conocido: se ha estudiado justamente para
fitorremediación, es decir, para sembrarlo en suelos contaminados y que absorba los metales. Eso, que es una
virtud ambiental, es un problema de producto: lo que la planta saca del suelo termina en la flor, y de la
flor pasa al extracto concentrado. A eso se suma una segunda fuente que nadie vigila lo suficiente: **el
envase y el hardware**, sobre todo en cartuchos de vapeo, donde el plomo de una soldadura migra al aceite
durante el almacenamiento.

Términos: **metal pesado (heavy metal)** = en este contexto, los cuatro elementos tóxicos regulados: plomo
(Pb), cadmio (Cd), arsénico (As) y mercurio (Hg). **Elemento traza (trace element)** = presente en niveles de
µg/kg a mg/kg. **ICP-MS** = espectrometría de masas con plasma acoplado inductivamente, la técnica de
referencia. **Digestión (digestion)** = destruir la matriz orgánica con ácido para liberar los metales.

## Los cuatro grandes y de dónde vienen

| Metal | Fuente típica en cannabis | Comportamiento en la planta |
|---|---|---|
| Plomo (Pb) | Suelo contaminado, fertilizantes fosfatados, soldaduras de hardware, pinturas | Se acumula sobre todo en raíz, pero migra a parte aérea |
| Cadmio (Cd) | Fertilizantes fosfatados, suelos ácidos, lodos | Muy móvil; llega a hoja y flor con facilidad |
| Arsénico (As) | Agua de riego, plaguicidas históricos, suelos | Depende mucho de la fuente de agua |
| Mercurio (Hg) | Deposición atmosférica, suelos mineros | Menos frecuente pero crítico en zonas de minería |

En Colombia esto no es teórico: en zonas con historia de minería de oro, el mercurio en suelo y agua es un
riesgo real y hay que preguntarle al cultivador por el **historial del predio**, no solo por su análisis del
último lote.

Cuatro elementos adicionales aparecen en algunas listas por su relación con hardware de vapeo: **cromo (Cr),
níquel (Ni), cobre (Cu) y estaño (Sn)**. Si tu producto es un cartucho, estos importan tanto como los cuatro
clásicos.

## Marco de límites (y por qué no hay uno solo)

**A agosto de 2026 no existe un límite internacional armonizado para metales pesados en cannabis.** Los
marcos que se usan como referencia:

- **USP <232> / ICH Q3D**: impurezas elementales en medicamentos. Fija **PDE (permitted daily exposure)** en
  µg/día por elemento y por vía de administración —oral, parenteral e **inhalatoria**, esta última mucho más
  estricta—. Es el marco técnicamente más sólido porque parte de la dosis diaria, no de la concentración.
- **Listas estatales de EE.UU.**: cada estado con su tabla en µg/g (ppm), y a menudo con límites distintos
  para producto inhalado frente a comestible.
- **Health Canada**: límites para cannabis conforme al Reglamento de Cannabis.
- **Colombia**: para alimentos y suplementos dietarios aplican los límites de la normativa sanitaria de
  alimentos; para derivados de cannabis, la especificación se sustenta en el expediente ante INVIMA
  (ver `210`).

La diferencia conceptual clave: **límite por concentración (ppm) frente a límite por dosis diaria
(µg/día)**. Un aceite muy potente se consume en gotas; un té se consume en gramos. Con el mismo ppm, la
exposición diaria es distinta. El enfoque ICH Q3D es el correcto y el que deberías usar para fijar tu
especificación interna.

```
Exposición diaria (µg/día) =
    concentración (µg/g) × masa de producto consumida al día (g)

Concentración máxima admisible (µg/g) =
    PDE (µg/día) ÷ dosis diaria máxima del producto (g/día)
```

Ejecuta esa conversión con código (`Matematicas_lushows` o `lab-tools/unidades.py`): es exactamente el tipo
de cuenta donde un factor de 1.000 mal puesto se convierte en un retiro de producto.

## Cómo se mide / cómo se comprueba

| Etapa | Qué se hace | Qué puede salir mal |
|---|---|---|
| Muestreo | Compuesto y representativo | Los metales se distribuyen heterogéneamente |
| Digestión | Microondas cerrada con HNO3 (± H2O2, ± HCl) | Digestión incompleta subestima; recipientes sucios contaminan |
| Medición | ICP-MS (preferido), ICP-OES o AAS | Interferencias poliatómicas si no se usa celda de colisión |
| Control | Blanco de reactivo, material de referencia certificado, duplicado, spike | Sin blanco no se detecta contaminación del laboratorio |

Lo que le exiges al informe:

1. **Los elementos analizados** y su LOD/LOQ individual en **µg/kg** o µg/g. Un LOQ de 0,5 µg/g no sirve para
   sostener un límite de 0,1 µg/g.
2. **La técnica exacta**: ICP-MS con celda de colisión/reacción resuelve interferencias que ICP-OES no.
3. **Recuperación con material de referencia certificado** de matriz vegetal.
4. **Acreditación ISO/IEC 17025 con metales en la matriz correspondiente** (ver `107`).
5. **Base del resultado**: base seca o tal cual (ver `07`).

## Ejemplo aplicado (ILUSTRATIVO)

Flor con plomo a 0,35 µg/g (base seca). Se extrae con etanol, rendimiento del 15 % en masa. Suponiendo que
el metal se transfiere completo (supuesto conservador; en la práctica la transferencia depende de la
especiación y del solvente):

```
Pb en 1.000 g de flor        = 0,35 µg/g × 1.000 g = 350 µg
Extracto obtenido            = 150 g
Concentración en el extracto = 350 µg / 150 g = 2,33 µg/g
Factor de concentración      = 6,7×
```

Si ese extracto va a un aceite de 30 mL con dosis diaria máxima de 1 mL (≈ 0,92 g), y el aceite lleva 10 % de
extracto:

```
Pb en el aceite       = 2,33 µg/g × 0,10 = 0,233 µg/g
Exposición diaria     = 0,233 µg/g × 0,92 g = 0,21 µg Pb/día
```

Cifras **(ILUSTRATIVO)**. La lectura importante: la flor "conforme" produjo un extracto 6,7 veces más
cargado, pero la exposición diaria del producto final es baja porque la dosis es pequeña. **Sin la cuenta de
dosis diaria no se puede juzgar el riesgo**, solo el número del COA.

## Estrategia de control

- **Analiza el suelo y el agua antes de sembrar**, no la flor después de cosechar (ver `106`). Es mucho más
  barato.
- **Pide el historial del predio**: minería, industria, botaderos, uso previo de plaguicidas arsenicales.
- **Cualifica fertilizantes y enmiendas.** Los fosfatados son fuente conocida de cadmio; pide COA con metales.
- **Ensayo de migración del envase** para cartuchos y cualquier envase metálico: llenar, almacenar y medir a
  0, 30, 90 días (ver `197`, `163`).
- **Controla el agua de riego** con la misma seriedad que el sustrato.

## Errores comunes

- **Analizar solo la flor y no el extracto.** El extracto concentra.
- **Comparar ppm contra ppm entre productos con dosis distintas.** El riesgo se mide en µg/día.
- **Usar límites de alimentos para productos inhalados.** ICH Q3D es mucho más estricto por vía inhalatoria,
  con razón fisiológica.
- **Olvidar el envase.** Un extracto limpio en un cartucho barato deja de estar limpio en tres meses.
- **Aceptar AAS cuando el límite exige ICP-MS.** La técnica debe tener el LOQ que el límite requiere.
- **Confiar en un solo análisis de suelo de hace tres años.** Los metales no se degradan, pero la
  distribución en el lote cambia con el manejo.

## Conexión con otros módulos

→ `88-icp-ms-y-metales-pesados.md` — la técnica por dentro.
→ `136-toxicidad-de-metales-pesados.md` — por qué son tóxicos y a qué dosis.
→ `106-analisis-de-agua-y-materias-primas.md` — controlar la entrada.
→ `197-vapeo-quimica-y-riesgos.md` — la migración desde el hardware.
→ `243-metales-pesados-en-hongos.md` — el mismo problema en la otra materia prima de la casa.
→ `213-como-leer-un-coa-de-cannabis.md` — cómo se lee la sección de metales.
