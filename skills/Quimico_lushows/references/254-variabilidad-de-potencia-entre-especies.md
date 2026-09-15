# 254 — Variabilidad de potencia entre especies y lotes (el dato que hace inviable dosificar con material natural)

Si hay un solo argumento científico para que la medicina de psilocibina use sustancia sintética y no hongos,
es este: **la variabilidad de contenido es enorme y no es controlable en la práctica**. Entre especies varía
por un factor grande; entre cepas de la misma especie también; entre el sombrero y el estípite del mismo
ejemplar hay diferencias de dos veces; y entre cosechas sucesivas del mismo cultivo, también. Este módulo
pone números a esa afirmación y explica cómo se mide la variabilidad, que es distinto de medir un promedio.

**Alcance (línea roja):** esto es química analítica y estadística de material biológico. No hay guías de
cultivo, ni de selección de cepas, ni de manejo del material.

Términos: **RSD (relative standard deviation)** = desviación estándar dividida por la media, en %; mide
dispersión. **flush** = cada tanda de cuerpos fructíferos que produce un mismo cultivo. **intra-lote
(within-batch)** = variación dentro del mismo lote. **inter-lote (between-batch)** = entre lotes.

## Qué tan variable es

Datos de literatura revisada por pares. Todos son **rangos reportados, no valores garantizados**, y están en
base seca:

| Fuente de variación | Magnitud reportada | Referencia |
|---|---|---|
| Entre cepas de *P. cubensis* | Psilocibina ~0,2 – 5,3 mg/g | Gotvaldová et al., 2021; estudios de cepas en *J. Fungi*, 2025 |
| Entre especies del género | Varía por más de un orden de magnitud | Literatura de quimiotaxonomía |
| Sombrero vs estípite | Sombrero ~1,03 % vs estípite ~0,52 % (p/p, alcaloides totales) | Gotvaldová et al., 2021 |
| Basidiosporas | Sin triptaminas detectadas | Gotvaldová et al., 2021 |
| Entre flushes del mismo cultivo | Diferencias sustanciales entre cosechas sucesivas | Bigwood & Beug, 1982 |
| Dentro de la misma cepa (intra-strain) | Diferencias notables incluso en condiciones controladas | *J. Fungi*, 2026 (14 cepas) |
| Por almacenamiento | Ver `255` | Gotvaldová et al., 2021 |

El estudio de 2026 sobre 14 cepas cultivadas bajo condiciones controladas es el más contundente: incluso
**controlando el ambiente, la variación intra-cepa sigue siendo alta**. Es decir, la variabilidad no es solo
un problema de manejo; es intrínseca al material biológico.

## Qué significa eso en dosis

```
(ILUSTRATIVO — cálculo de exposición para mostrar la magnitud del problema)

Si un material tiene 5,0 mg/g de psilocibina y otro 1,0 mg/g, la misma masa de 2,0 g entrega:
  Material A: 2,0 g × 5,0 mg/g = 10,0 mg de psilocibina
  Material B: 2,0 g × 1,0 mg/g =  2,0 mg de psilocibina
Un factor de 5 en la misma "dosis" aparente.

En comparación, una tableta farmacéutica debe cumplir uniformidad de contenido USP <905>,
típicamente dentro de ±15 % del valor declarado. La diferencia de rigor es abismal.
```

Ese contraste es exactamente la razón por la que los ensayos clínicos (`259`) usan sustancia sintética con
dosis fija en miligramos, y por la que ningún regulador aceptaría material fúngico como forma farmacéutica
sin un control de contenido que hoy no existe.

## Cómo se mide la variabilidad (no el promedio)

Medir un promedio es fácil y engañoso. Lo que hay que caracterizar es la **dispersión**:

| Nivel | Diseño de muestreo | Qué se calcula |
|---|---|---|
| Intra-unidad | 3 submuestras del mismo ejemplar molido | RSD de homogeneización |
| Intra-lote | 10 unidades al azar del lote | RSD intra-lote |
| Inter-lote | 5 lotes distintos | RSD inter-lote |
| Por parte anatómica | Sombrero y estípite por separado | Cociente sombrero/estípite |
| Por flush | Cada cosecha por separado | Tendencia entre flushes |

```
Ejemplo de reporte (ILUSTRATIVO), 10 unidades de un mismo lote:
  Psilocibina (mg/g b.s.): 6,1 / 7,8 / 5,2 / 9,4 / 6,7 / 8,1 / 4,9 / 7,2 / 10,3 / 6,4
  media = 7,21 ; s = 1,66 ; RSD = 23,0 %
  mínimo/máximo = 4,9 / 10,3  → factor 2,1 dentro del MISMO lote

Un RSD de 23 % es inaceptable para cualquier producto farmacéutico.
Ejecuta la estadística en código (Matematicas_lushows), nunca a ojo.
```

El paso de homogeneización es crítico: si no mueles todo el lote y muestreas del polvo homogéneo, estás
midiendo tu muestreo, no el material (`66`, `67`).

## Ejemplo aplicado — por qué esto es un argumento de seguridad

La conclusión de la literatura sobre variabilidad (Gotvaldová 2021 lo dice explícitamente) es que las
concentraciones de triptaminas en hongos son extremadamente variables y eso **representa un riesgo real de
sobreexposición** para quien consume material natural asumiendo una potencia constante. No es un argumento
moral; es un argumento de control de calidad: no se puede dosificar lo que no se puede medir por adelantado.

Traducido a lo que esta skill sí hace: si alguien te pregunta "¿cuántos gramos equivalen a 25 mg?", la
respuesta técnica correcta es **"no se puede saber sin analizar ese material específico"** — y aun
analizándolo, la variación entre unidades del mismo lote hace la estimación poco confiable.

## Errores comunes

- **Usar un valor promedio de internet como si aplicara a un material concreto.** No aplica.
- **Medir una sola unidad y llamarlo "la potencia del lote".** Un solo dato no describe una distribución.
- **No homogeneizar antes de muestrear.** El sombrero y el estípite tienen contenidos distintos.
- **Comparar valores en bases distintas.** Fresco vs seco cambia el número por un factor cercano a 10.
- **Ignorar la degradación durante el almacenamiento** al comparar análisis separados en el tiempo (`255`).
- **Confundir variabilidad con error analítico.** Un método con RSD de 3 % midiendo material con RSD de 23 %
  te está mostrando el material, no el método.

## Conexión con otros módulos

→ `251-psilocibina-y-psilocina-quimica.md` y `252-baeocistina-y-otros-alcaloides-relacionados.md`.
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — la variación que agrega el tiempo.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — cómo se mide bien.
→ `66-plan-de-muestreo-y-representatividad.md` y `67-homogeneizacion-y-molienda-de-muestra.md`.
→ `78-estadistica-para-el-laboratorio.md` — RSD, dispersión, intervalos.
→ `259-dosis-en-investigacion-clinica.md` — por qué la clínica usa dosis fijas de sustancia sintética.