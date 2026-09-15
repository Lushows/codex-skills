# 160 — Excipientes y compatibilidad (lo que no es activo también decide si el producto sirve)

El excipiente es todo lo que acompaña al activo: relleno, deslizante, lubricante, conservante, colorante,
saborizante, cápsula. La gente los trata como "los otros ingredientes" y ahí empiezan los problemas: un
excipiente mal elegido puede reaccionar con tu activo, atraer humedad, retrasar la desintegración, disparar una
alerta de alérgenos o cerrarte un mercado por razones de percepción. En un producto de hongos o cannabis, donde
el activo es sensible y caro, **el excipiente es la mitad del diseño**.

Términos: **excipiente (excipient)** = componente sin actividad terapéutica pretendida. **Incompatibilidad
(incompatibility)** = interacción indeseada activo-excipiente. **Grado (grade)** = calidad especificada de un
material: USP, EP, alimentario, técnico. **c.s. (cantidad suficiente / q.s.)** = lo necesario para completar.
**Estudio de compatibilidad binario (binary compatibility study)** = mezclar activo con cada excipiente y
observar bajo estrés.

## Catálogo funcional

| Función | Materiales típicos | Dosis usual | Nota crítica |
|---|---|---|---|
| Diluyente | Celulosa microcristalina (MCC), fosfato dicálcico, manitol, lactosa, inulina, almidón de arroz | 5–50 % | **Lactosa**: intolerancia. **Almidón/maltodextrina**: suman α-glucano (`220`) |
| Deslizante | Dióxido de silicio coloidal | 0,2–1,0 % | Mejora el flujo del polvo |
| Lubricante | Estearato de magnesio, estearato de calcio, ácido esteárico, behenato de glicerilo | 0,3–1,0 % | En exceso retrasa la desintegración |
| Desintegrante | Croscarmelosa sódica, glicolato sódico de almidón, crospovidona | 2–6 % | Solo relevante en tabletas |
| Aglutinante | Povidona (PVP), HPMC, almidón pregelatinizado | 2–8 % | Puede formar complejos con fenoles |
| Antiapelmazante | Silicato de calcio, dióxido de silicio | 0,5–2 % | Clave en polvos higroscópicos |
| Conservante | Sorbato, benzoato, parabenos | 0,05–0,3 % | Depende del pH (`156`) |
| Antioxidante | Tocoferoles, ácido ascórbico, romero | 0,02–0,5 % | Para aceites y fenoles (`61`) |
| Quelante | EDTA, citrato | 0,01–0,1 % | Secuestra metales que catalizan oxidación |
| Vehículo oleoso | MCT, aceite de oliva, girasol alto oleico | c.s. | MCT es el estándar en cannabis (`195`) |
| Cápsula | Gelatina, HPMC, pullulan | — | HPMC para higroscópicos (`154`) |

## Las incompatibilidades que hay que conocer

| Interacción | Qué pasa | Cómo se detecta | Dónde duele |
|---|---|---|---|
| Aminas + azúcares reductores (lactosa) | Reacción de Maillard: pardeamiento, pérdida de activo | Color, HPLC, DSC | Activos con grupo amino (`62`) |
| Estearato de magnesio en exceso | Película hidrofóbica → desintegración lenta | Ensayo de desintegración | Tabletas y cápsulas |
| Excipientes básicos + activos ácidos | Salificación, cambio de solubilidad | pH de suspensión, HPLC | Formas ácidas (THCA, `173`) |
| Metales traza (Fe, Cu) del excipiente | Catalizan oxidación de fenoles y aceites | Peróxidos, color, ICP-MS | Aceites y extractos fenólicos |
| Higroscópicos juntos (maltodextrina + extracto) | El polvo se apelmaza y se pega | a_w, aspecto a 40 °C/75 % HR | Polvos y cápsulas |
| PVP + polifenoles | Formación de complejos, menor extracción del activo en el ensayo | Recuperación analítica baja | Falsos "bajo contenido" |
| Colorantes migrantes | Moteado, cambio de color en el tiempo | Visual, a 0/3/6 meses | Tabletas y gomitas |

**El caso más frecuente en este sector:** apelmazamiento. Un extracto de hongo secado por aspersión con
maltodextrina, metido en cápsula de gelatina, guardado en Barranquilla, se convierte en un ladrillo. La
solución no es un excipiente milagroso: es HPMC + antiapelmazante + envase con barrera y desecante (`163`).

## Grados: lo que separa un excipiente de un polvo cualquiera

| Grado | Qué garantiza | ¿Sirve para suplemento? |
|---|---|---|
| USP / NF / EP | Cumple monografía farmacopeica, con identidad, pureza y límites | Sí, es el estándar seguro |
| Alimentario (food grade) | Apto para alimentos según la norma local | Sí, con COA |
| Técnico / industrial | Nada aplicable a consumo humano | **No. Nunca.** |

Exige siempre: **COA del lote + ficha técnica + declaración de alérgenos + país de origen**. Y guarda todo en
el expediente (`286`). Un excipiente sin COA es un ingrediente sin identidad y hace inauditable todo tu
producto.

## Cómo se comprueba la compatibilidad

Se comprueba antes de fabricar, con un estudio binario que cuesta poco y ahorra lotes:

```
ESTUDIO DE COMPATIBILIDAD BINARIA (protocolo de pyme)

  1. Prepara mezclas 1:1 p/p de activo con CADA excipiente candidato.
     Incluye un vial con activo solo (control).
  2. Dos condiciones:
       - seco, 40 °C / 75 % HR, viales abiertos y cerrados
       - con 5 % de agua añadida (estrés de humedad), viales cerrados
  3. Tiempos: 0, 2 y 4 semanas.
  4. Se observa/mide en cada punto:
       - aspecto y color (foto en condiciones fijas)
       - contenido de activo por HPLC (% respecto a t=0)
       - aparición de picos nuevos (productos de degradación)
       - opcional: DSC del binario vs los componentes (`99`)
  5. Criterio: se descarta el excipiente que produzca pérdida de activo
     significativamente mayor que el control, o picos nuevos.

Costo: unas pocas decenas de análisis. Comparado con perder un lote de producción, es nada.
```

## Excipientes y percepción de marca

Aquí hay una capa que no es química pero decide ventas, y conviene decirla sin condescendencia:

- El **estearato de magnesio** es seguro a las dosis usadas, y aun así una parte del mercado natural lo
  rechaza. Es una decisión de posicionamiento; si lo quitas, asume peor flujo y más variación de llenado.
- El **dióxido de titanio** como opacificante está bajo revisión y restricción en varias jurisdicciones; a
  agosto de 2026 verifica su estatus en Colombia y en los mercados a los que quieras exportar antes de usarlo.
- **"Sin rellenos" / "100 % puro"** es un claim que te obliga: si escribes eso, no puedes tener diluyente. Y sin
  diluyente, el llenado de la cápsula es más difícil de controlar.
- **Alérgenos** (lactosa, soya en la lecitina, gluten en algunos almidones) son declaración obligatoria y un
  riesgo real de retiro de producto.

La conversación de cómo se comunica esto al cliente es de `directorcreativo_lushows` y `ventas_lushows`; la
decisión técnica de qué se puede sostener es de aquí.

## Ejemplo aplicado — reformular una cápsula que se apelmaza

```
Síntoma: a los 4 meses, las cápsulas están pegadas entre sí y el polvo forma terrones.

Diagnóstico (ILUSTRATIVO)
  a_w del polvo al envasar: 0,52  →  ya alto
  Soporte del extracto: maltodextrina 40 % (muy higroscópica, `150`)
  Cápsula: gelatina (13–16 % de humedad de equilibrio, cede agua al polvo)
  Envase: frasco PET sin desecante, tapa sin sello de inducción

Reformulación
  1. Cambiar el soporte de secado a fibra de acacia o celulosa   → menos higroscópico y sin α-glucano
  2. Agregar dióxido de silicio 0,8 % como antiapelmazante
  3. Cambiar a cápsula HPMC (humedad de equilibrio 4–6 %)
  4. Envasar a HR ambiente ≤ 40 % y meter desecante de sílica
  5. Frasco HDPE opaco con sello de inducción (`163`)
  6. Reverificar a 40 °C/75 % HR durante 3 meses antes de relanzar (`165`)
```

## Errores comunes

- Copiar la fórmula de otro producto sin verificar compatibilidad con **tu** activo.
- Comprar excipiente sin COA ni grado declarado.
- Sobredosificar el lubricante y obtener un producto que no se desintegra.
- Usar lactosa con un activo que tenga grupo amino: Maillard asegurado en el tiempo (`62`).
- No declarar alérgenos derivados de excipientes (soya de la lecitina es el más olvidado).
- Cambiar de proveedor del "mismo" excipiente sin revalidar: distinto grado, distinta granulometría, distinto
  comportamiento (`169`).
- Poner un antioxidante sin quelante cuando la oxidación la cataliza un metal: se resuelve a medias.
- Olvidar que los excipientes entran a la cuenta de costo y al espacio de la cápsula. Cada mg de relleno es un
  mg que no es activo.

## Conexión con otros módulos

→ `154-capsulas-y-encapsulado.md` y `155-tabletas-y-compresion.md` — dónde se usan estos materiales.
→ `62-maillard-y-pardeamiento.md` — la incompatibilidad clásica, en química.
→ `164-estabilidad-ich-q1-y-vida-util.md` — donde se paga el excipiente mal elegido.
→ `163-envase-primario-y-compatibilidad.md` — la otra mitad del problema de humedad.
→ `137-alergenos-e-hipersensibilidad.md` — qué hay que declarar y por qué.
