# 39 — Química computacional para no especialistas (qué se puede predecir sin laboratorio, y qué no)

Hay una capa de herramientas de software que predicen propiedades moleculares en minutos y gratis: logP,
pKa, solubilidad, espectros, incluso posibles interacciones con una proteína. Bien usadas te ahorran meses
y plata: te dicen qué solvente probar primero, qué pH esperar, si una molécula va a cruzar membranas.
Mal usadas producen el peor tipo de dato — uno que parece medido y no lo es. La regla de esta skill es
tajante: **un valor calculado se marca como calculado, siempre, y nunca entra a un expediente técnico ni a
una etiqueta como si fuera experimental**.

Términos: **in silico** = hecho por computador (por analogía con *in vitro* e *in vivo*). **QSAR
(quantitative structure-activity relationship)** = modelo estadístico que relaciona estructura con una
propiedad o actividad. **docking molecular (molecular docking)** = simulación de cómo una molécula encaja
en el sitio de unión de una proteína. **DFT (density functional theory)** = método de mecánica cuántica
para calcular energías y geometrías. **descriptor (descriptor)** = número que resume un rasgo de la
molécula (peso molecular, área polar, número de donantes de puente de hidrógeno). **SMILES** = forma de
escribir una estructura molecular como texto.

## Qué se predice bien, qué se predice mal

| Propiedad | Confianza del cálculo | Cuándo se puede usar | Qué se hace igual |
|---|---|---|---|
| Peso molecular, fórmula, masa exacta | Exacta (es aritmética) | Siempre | Nada, es un hecho |
| logP | Buena para moléculas comunes; peor en extremos (logP > 6) | Para elegir solvente y orientar | Medir por shake-flask si va al expediente (`30`) |
| pKa | Buena en grupos clásicos; regular en policíclicos raros | Para diseñar el pH de extracción | Titulación potenciométrica (`22`) |
| Solubilidad acuosa | Regular; errores de 1–2 órdenes de magnitud | Como orden de magnitud | Shake-flask + HPLC (`19`) |
| Espectro UV | Cualitativa (dónde cae el máximo) | Elegir longitud de onda de detección | Barrido con DAD (`90`) |
| Fragmentación en MS | Buena para orientar | Interpretar un espectro desconocido | Estándar de referencia (`84`) |
| Desplazamientos de RMN | Buena para confirmar una estructura propuesta | Elucidación estructural | El espectro real (`94`) |
| Afinidad por un receptor (docking) | **Débil como número absoluto** | Generar hipótesis, priorizar ensayos | Ensayo de unión real `[in vitro]` (`120`) |
| Actividad biológica / efecto | **No se predice de forma confiable** | Nunca como evidencia | Ensayo, y luego clínico (`12`) |
| Toxicidad (modelos QSAR regulatorios) | Aceptada en algunos marcos para impurezas | Evaluación preliminar; ICH M7 la contempla | Estudios toxicológicos (`134`) |

La fila más importante es la penúltima. Un docking que "muestra que el compuesto X se une al receptor Y"
es una **hipótesis generada por computador**, no una prueba de nada. En el marketing de suplementos esa
confusión es epidémica: se publica una figura bonita de una molécula encajando en una proteína y se
comunica como si fuera un mecanismo demostrado. En términos de esta skill, eso es un dato sin método y sin
nivel de evidencia (`02`, `12`), y si se usa para insinuar un efecto en salud, es un claim de riesgo
regulatorio (`267`, `268`).

## Las herramientas que de verdad vas a usar

| Herramienta | Para qué | Costo |
|---|---|---|
| PubChem | Estructura, SMILES, propiedades calculadas y experimentales recopiladas, sinónimos, CAS | Gratis |
| ChemSpider | Igual, con enlaces a fuentes | Gratis |
| SwissADME | Predicción de logP, solubilidad, absorción, reglas de Lipinski | Gratis |
| RDKit (Python) | Calcular descriptores en lote, dibujar estructuras, buscar subestructuras | Gratis, open source |
| Avogadro / ChemDraw / MarvinSketch | Dibujar y limpiar estructuras; nomenclatura | Gratis / licencia |
| mzCloud, MassBank, GNPS | Bibliotecas de espectros de masas reales | Gratis / registro |
| AutoDock Vina, PyMOL | Docking y visualización | Gratis |
| Reglas de Lipinski / Veber | Filtro rápido de "drug-likeness" oral | Concepto, no software |

```
Ejemplo con RDKit — descriptores de CBD en cuatro líneas:

  from rdkit import Chem
  from rdkit.Chem import Descriptors, Crippen
  m = Chem.MolFromSmiles("CCCCCc1cc(O)c(C2CC(C)=CCC2C(C)=C)c(O)c1")
  print(Descriptors.MolWt(m), Crippen.MolLogP(m), Descriptors.TPSA(m))

Lo que devuelve es un logP CALCULADO (método de Crippen). Se anota como
"logP calculado (Crippen/RDKit)", nunca como "logP = X".
```

## Reglas de Lipinski y por qué los cannabinoides las rozan

La "regla de 5" de Lipinski describe qué tan probable es que una molécula se absorba bien por vía oral:
peso molecular ≤ 500, logP ≤ 5, donantes de puente de hidrógeno ≤ 5, aceptores ≤ 10. Es una regla empírica
sobre fármacos, no una ley.

El CBD (PM 314, logP ~6,3, 2 donantes, 2 aceptores) **incumple el criterio de logP**. Y eso predice
exactamente lo que la práctica confirma: absorción oral errática, fuerte efecto de la comida, y
biodisponibilidad oral baja reportada en la literatura clínica. La predicción in silico acertó en la
dirección — y aun así, el número real de biodisponibilidad solo se obtiene con un estudio farmacocinético
en humanos (`122`, `206`). Eso resume la utilidad honesta de estas herramientas: **orientan la decisión,
no reemplazan la medición**.

## Cómo se documenta un dato calculado

| Elemento del registro | Ejemplo |
|---|---|
| Valor y unidad | logP = 6,33 |
| Marca de origen | **Calculado**, no medido |
| Método y versión | Crippen (RDKit 2024.03.5) |
| Entrada usada | SMILES exacto, con estereoquímica si aplica |
| Fecha | 11 de agosto de 2026 |
| Qué medición lo reemplazaría | Shake-flask OECD 107 (`30`) |

Sin esas seis líneas, el número es irrastreable y en una auditoría se cae solo (`03`, `168`, `286`).

## Ejemplo aplicado — priorizar solventes antes de gastar en laboratorio

Se quiere fraccionar un extracto de reishi y decidir con qué probar primero, sin quemar 20 corridas
**(ILUSTRATIVO — todos los valores son CALCULADOS, no medidos)**:

```
Compuesto              logP calc.   pKa calc.   TPSA (Å²)   Predicción de fase a pH 3 / pH 8
Ácido ganodérico A         2,9         4,5          104      pH 3: orgánica · pH 8: acuosa
Ergosterol                 7,6          —            20      Orgánica siempre
Adenosina                 −1,1        3,5/12,5      140      Acuosa siempre
Ergotioneína              −3,0       zwitterión     130      Acuosa siempre
Δ9-THC (referencia)        6,8         9,3           29      Orgánica siempre

Diseño derivado: partición acetato de etilo / agua a pH 3 y a pH 8 (2 experimentos, no 20).
Verificación experimental: HPLC de ambas fases + balance de masa (`06`, `30`).
Resultado experimental esperado en la práctica: coincide en dirección, no necesariamente en magnitud.
```

Ese es el uso correcto: la predicción **redujo el espacio de búsqueda de 20 experimentos a 2**, y después
el laboratorio produjo el dato real. Lo que no se puede hacer es saltarse el segundo paso y poner los
números calculados en la ficha técnica del producto.

## Errores comunes

- Presentar un valor calculado como experimental. Es el pecado capital de este módulo.
- Usar un docking como prueba de mecanismo o —peor— como base de un mensaje de salud (`268`, `293`).
- Predecir solubilidad y comprar 200 L de solvente sin una prueba de 50 mL antes.
- Calcular propiedades de una estructura mal dibujada. Un SMILES con un enlace equivocado da todo mal;
  se verifica contra PubChem y contra el CAS.
- Ignorar la estereoquímica. Los enantiómeros tienen el mismo logP calculado y actividad biológica
  distinta (`43`).
- Aplicar modelos entrenados con fármacos a polímeros o a mezclas. Un β-glucano no tiene logP (`219`).
- Creer que "gratis y rápido" significa "sin responsabilidad". Un dato mal marcado en un expediente es un
  problema de cumplimiento, no un error académico.

## Conexión con otros módulos

→ `30-extraccion-liquido-liquido-y-logp.md` — el logP medido de verdad.
→ `22-acidos-bases-y-ph.md` — el pKa medido de verdad.
→ `12-niveles-de-evidencia.md` — dónde cae "in silico" en la jerarquía (abajo).
→ `03-honestidad-cientifica-y-fuentes.md` — cómo se marca un dato según su origen.
→ `84-hrms-qtof-orbitrap-e-identificacion.md` — donde el cálculo sí ayuda a identificar.
→ `104-metabolomica-y-huella-quimica.md` — análisis de datos a gran escala.
→ `105-quimiometria-pca-y-modelos.md` — modelos estadísticos sobre datos reales.
→ `287-diseno-de-experimentos-doe.md` — la otra forma de reducir el número de experimentos.
