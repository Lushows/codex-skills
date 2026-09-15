# 256 — Análisis de psilocibina y psilocina por HPLC y LC-MS/MS (el método, de punta a punta)

Este es un módulo de método analítico serio: cómo se prepara la muestra, qué columna, qué fase móvil, qué
detección, qué patrones, qué se valida y qué trampas tiene esta matriz en particular. La psilocibina es un
analito incómodo — zwitteriónico, muy polar, y con un producto de degradación que es a la vez otro analito —
y por eso los métodos improvisados dan números bajos y nadie se entera.

**Alcance (línea roja):** análisis en laboratorio con licencia para sustancias controladas. Este módulo NO
es una guía de extracción para producción; la preparación de muestra que se describe es analítica (escala de
miligramos, con solvente y estándar interno), y el manejo de patrones certificados exige permiso legal
(`263`, `109`).

Términos: **MRM (multiple reaction monitoring)** = modo de MS/MS donde se sigue una transición
precursor→producto específica. **HILIC (hydrophilic interaction chromatography)** = cromatografía para
compuestos muy polares. **efecto matriz (matrix effect)** = supresión o realce de señal por la matriz.
**isotopólogo deuterado (deuterated isotopologue)** = el mismo compuesto con deuterios; el mejor estándar
interno posible.

## El problema cromatográfico de fondo

La psilocibina es un zwitterión: tiene el fosfato cargado negativo y la amina terciaria protonable. En una
C18 clásica con fase móvil típica **no retiene**: sale con el frente del solvente, coeluye con toda la
matriz y se cuantifica mal o no se cuantifica. La psilocina, en cambio, sí retiene. Cualquier método donde
la psilocibina eluya cerca del volumen muerto está mal.

Tres salidas válidas:

| Estrategia | Cómo funciona | Cuándo usarla |
|---|---|---|
| C18 polar-embedded o AQ | Fase estacionaria que tolera 95–100 % de acuoso | La opción más común y práctica |
| HILIC (amida, sílice) | Retiene por polaridad, con alto orgánico | Excelente para psilocibina, complica la psilocina |
| Par iónico | Aditivo que forma par con el analito | Funciona, pero contamina el MS; evitar en LC-MS |

## Preparación de muestra (analítica)

```
Escala analítica típica:
1. Homogeneizar todo el material del lote (molienda criogénica o molino de cuchillas). Crítico: 254, 67.
2. Pesar 50–100 mg de polvo en tubo, por triplicado.
3. Añadir estándar interno deuterado (psilocibina-d4 y psilocina-d10) ANTES de extraer.
4. Extraer con metanol:agua (75:25) o metanol acidificado, 10–20 mL; ultrasonido 15–30 min a ≤ 40 °C.
5. Centrifugar (p. ej. 4000 g, 10 min) y filtrar 0,22 µm PVDF a vial ámbar.
6. Diluir a rango de curva. Inyectar el MISMO día (255).
Opcional: ácido ascórbico como antioxidante para proteger la psilocina.
```

Dos decisiones que definen la exactitud: **el estándar interno se agrega antes de la extracción** (si se
agrega después, corrige inyección pero no recuperación), y **la muestra se homogeneiza entera** (si no,
mides tu muestreo).

## Condiciones cromatográficas de partida (punto de arranque, hay que optimizar)

| Parámetro | HPLC-DAD (material rico) | LC-MS/MS (traza y confirmación) |
|---|---|---|
| Columna | C18 polar-embedded, 150 × 4,6 mm, 5 µm | C18 fused-core, 100 × 2,1 mm, 2,6 µm |
| Fase A | Buffer fosfato o formiato de amonio 10 mM, pH ~3 | Agua + 0,1 % ácido fórmico (o formiato de amonio 5 mM) |
| Fase B | Acetonitrilo o metanol | Acetonitrilo + 0,1 % ácido fórmico |
| Gradiente | 2 % → 40 % B en 12 min | 2 % → 50 % B en 6 min |
| Flujo | 1,0 mL/min | 0,3–0,4 mL/min |
| Temperatura de columna | 30–35 °C | 35–40 °C |
| Inyección | 10 µL | 2–5 µL |
| Detección | DAD, 267 nm (espectro 200–400 nm para pureza de pico) | ESI+, MRM |

Transiciones MRM habituales (verificar y optimizar en tu equipo):

```
Psilocibina  [M+H]+ m/z 285,1 → 205,1 (cuantificador) ;  285,1 → 58,1 (calificador)
Psilocina    [M+H]+ m/z 205,1 → 58,1  (cuantificador) ;  205,1 → 160,1 (calificador)
Psilocibina-d4 y psilocina-d10 como estándares internos, sus transiciones correspondientes.
Criterio de identificación: tiempo de retención ±2,5 % del patrón + relación
cuantificador/calificador dentro de ±20–30 % del patrón (criterio tipo SANTE/forense).
```

## Sensibilidad esperable

| Técnica | LOD/LOQ reportados | Fuente |
|---|---|---|
| LC-MS/MS | LOD ~1 ppb psilocibina, ~0,1 ppb psilocina | Nota de aplicación SCIEX, matriz hongo |
| HPLC-DAD | LOD 1,58 mg/L y LOQ 4,78 mg/L (psilocibina); LOD 1,70 y LOQ 5,17 mg/L (psilocina) | *ACS Omega*, 2025 |

Traducción práctica: para material con miligramos por gramo, **HPLC-DAD alcanza y es mucho más barato**.
Para congéneres en traza (`252`), fluidos biológicos o confirmación forense, hace falta LC-MS/MS.

## Validación mínima (ICH Q2(R2))

| Parámetro | Criterio típico |
|---|---|
| Especificidad | Separación de psilocibina, psilocina y congéneres; pureza de pico por DAD o razón de iones |
| Linealidad | r² ≥ 0,995 en al menos 5 niveles, cubriendo 50–150 % del nivel esperado |
| Exactitud (recuperación) | 95–105 % en material rico; 80–120 % en traza |
| Precisión (repetibilidad) | RSD ≤ 3 % en material rico; ≤ 15 % en traza |
| Precisión intermedia | Otro día, otro analista, otra columna |
| LOD/LOQ | S/N ≥ 3 y ≥ 10, o desde la curva (`73`) |
| Robustez | ± pH, ± temperatura, ± % orgánico |
| **Estabilidad de la muestra** | Obligatoria en este analito: en autosampler, en refrigeración y congelada (`255`) |
| Efecto matriz (LC-MS) | Evaluado por post-column infusion o comparación de pendientes |

## Ejemplo aplicado (ILUSTRATIVO) — reporte final

```
Muestra PSY-2026-011 · material fúngico seco homogeneizado · humedad 6,2 %
Método: HPLC-DAD 267 nm, C18 polar-embedded, IS psilocibina-d4; validado ICH Q2(R2)
Curva: 5 niveles, 2–100 µg/mL, r² = 0,9993 · Recuperación 98,4 % · RSD 2,7 % (n=6)

  Psilocibina             7,42 mg/g base seca
  Psilocina               0,88 mg/g base seca
  Psilocibina equivalente 8,64 mg/g base seca (factor 0,7186, ver 251)
  Baeocistina             < LOQ por DAD → se remite a LC-MS/MS
```

## Errores comunes

- **Usar C18 estándar y no ver la psilocibina.** Sale en el frente; el resultado es falso bajo.
- **Agregar el estándar interno después de extraer.** No corrige la recuperación.
- **No homogeneizar el material completo.** Con RSD del material de 20 %+ (`254`), el muestreo domina el error.
- **Guardar los extractos para el día siguiente.** Se degradan (`255`).
- **Reportar sin base ni convención.** "0,9 %" sin base seca y sin decir si incluye psilocina no significa nada.
- **Cuantificar congéneres sin patrón.** Es estimación, y hay que decirlo (`70`, `252`).
- **Trabajar con patrones sin licencia.** Riesgo legal grave para el laboratorio (`263`).

## Conexión con otros módulos

→ `79-hplc-y-uhplc.md`, `81-columnas-fases-y-desarrollo-de-metodo-lc.md`, `83-lc-ms-ms-y-mrm.md`.
→ `75-validacion-de-metodos-ich-q2-r2.md` y `73-lod-loq-y-rango-lineal.md`.
→ `70-patrones-de-referencia-y-trazabilidad.md` y `72-estandar-interno-y-adicion-de-estandar.md`.
→ `251`, `252`, `254`, `255` — los analitos, la variabilidad y la estabilidad.
→ `109-cadena-de-custodia-y-envio-de-muestras.md` — obligatorio con sustancias controladas.