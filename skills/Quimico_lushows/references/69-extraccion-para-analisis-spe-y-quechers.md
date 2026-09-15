# 69 — Extracción y limpieza para análisis: SPE y QuEChERS (cuando la matriz estorba)

Extraer no basta. En un extracto de flor de cannabis o de polvo de hongo, el analito que buscas puede ser el
0,001 % de lo que hay en el vial: lo demás es clorofila, ceras, azúcares, resina. Esa matriz tapa señales,
ensucia el instrumento y suprime la respuesta del detector de masas. La **limpieza (cleanup)** es la etapa
que separa un método que funciona el primer día de uno que funciona el lote 300. Si te cotizan pesticidas
"baratos", casi siempre es porque están recortando esta etapa.

Términos:
- **SPE (solid-phase extraction)** = extracción en fase sólida: el extracto pasa por un cartucho con
  sorbente que retiene selectivamente el analito o la basura.
- **QuEChERS** = *Quick, Easy, Cheap, Effective, Rugged, Safe*; protocolo de extracción con acetonitrilo,
  sales y limpieza dispersiva, estándar mundial para pesticidas multiresiduo.
- **dSPE (dispersive SPE)** = limpieza dispersiva: se agrega el sorbente suelto al extracto, se agita y se
  centrifuga; no hay cartucho.
- **Supresión iónica (ion suppression)** = la matriz roba carga en la fuente del espectrómetro de masas y la
  señal del analito baja aunque el analito esté.
- **Efecto de matriz (matrix effect, ME)** = cuantifica esa distorsión: `ME % = (señal en matriz / señal en solvente) x 100`.

## QuEChERS: el caballo de batalla de pesticidas

Nació para frutas y verduras (métodos AOAC 2007.01 y EN 15662, ambos vigentes y ampliamente usados a agosto
de 2026) y se adaptó a cannabis y a hongos. El flujo:

```
1. Pesar 5-15 g de muestra homogeneizada (+ agua si la matriz es seca: hidratar es obligatorio)
2. Agregar acetonitrilo (típicamente 10-15 mL) + patrones internos
3. Agregar sales de partición:
     - versión AOAC 2007.01 : acetato de sodio + MgSO4 (medio tamponado con acetato)
     - versión EN 15662     : citrato + MgSO4 + NaCl (medio tamponado con citrato)
   Agitar fuerte, centrifugar → dos fases; el analito sube al acetonitrilo
4. Tomar alícuota del sobrenadante y limpiar por dSPE:
     - PSA (primary secondary amine): quita ácidos orgánicos y azúcares
     - C18: quita grasas y ceras  → CLAVE en cannabis y hongos grasos
     - GCB (graphitized carbon black): quita clorofila y pigmentos → CLAVE en flor verde
       (ojo: GCB también retiene pesticidas planares como el clorotalonil; se pierde recuperación)
5. Centrifugar, acidificar si aplica, filtrar e inyectar en LC-MS/MS y GC-MS/MS
```
El punto delicado en cannabis es que la matriz es resinosa y muy pigmentada: sin C18 + GCB el instrumento se
ensucia en pocas corridas; con demasiado GCB pierdes analitos. Ese ajuste fino es lo que distingue a un
laboratorio bueno de uno que "también hace cannabis".

## SPE: cuándo sí y cuándo no

| Modo de SPE | Sorbente | Retiene | Uso típico en este oficio |
|---|---|---|---|
| Fase reversa | C18, C8 | Compuestos apolares | Limpiar extractos acuosos; concentrar cannabinoides |
| Fase normal | Sílica, florisil, alúmina | Polares | Separar pigmentos de aceites |
| Intercambio catiónico | SCX, MCX | Bases protonadas | **Psilocibina/psilocina y alcaloides** (`251`, `256`) |
| Intercambio aniónico | SAX, MAX | Ácidos | Ácidos orgánicos, algunos metabolitos |
| Polimérico mixto | HLB (hydrophilic-lipophilic balance) | Amplio rango | Multiresiduo, micotoxinas |
| Inmunoafinidad (IAC) | Anticuerpo específico | Solo el analito | **Aflatoxinas y ocratoxina A** (`101`) |

Los cartuchos de inmunoafinidad son caros (varios dólares por muestra) pero dan la limpieza más selectiva que
existe; por eso los métodos oficiales de micotoxinas los usan.

```
Secuencia estándar de un cartucho SPE:
  acondicionar (metanol) → equilibrar (agua o buffer) → cargar la muestra
  → lavar (quita interferencias, no el analito) → eluir (recupera el analito)
El error clásico: lavar con un solvente demasiado fuerte y eluir el analito en el lavado.
Se detecta recogiendo y analizando la fracción de lavado.
```

## Cómo se comprueba que la limpieza funciona

Tres números que debes pedir en el informe de validación (`75`):

1. **Recuperación (recovery)** por nivel de fortificación. Para pesticidas y micotoxinas, los criterios
   habituales en guías de residuos son 70–120 % con RSD <= 20 % (verifica el criterio exacto de la guía que
   aplique a tu jurisdicción y matriz).
2. **Efecto de matriz (ME)**: se compara la señal del patrón en solvente contra la del patrón preparado en
   extracto de matriz blanca.
   ```
   ME = 100 x (pendiente en matriz / pendiente en solvente)   (ILUSTRATIVO)
     ME = 100 %   → sin efecto
     ME = 62 %    → supresión del 38 % : subestimarías si calibras en solvente
     ME = 145 %   → aumento de señal (enhancement) : sobreestimarías
   ```
   La solución no es siempre limpiar más: se usa **calibración con matriz emparejada (matrix-matched
   calibration)** o **estándar interno marcado isotópicamente** (`72`, `83`).
3. **Blanco de matriz** libre del analito, para demostrar que lo que ves viene de la muestra y no del proceso.

## Ejemplo aplicado — pesticidas en flor de cannabis colombiana

Panel exigido: depende del país. A agosto de 2026, California está en pleno cambio regulatorio (expediente
DCC-2025-03-R, texto de 15 días publicado el 11 de febrero de 2026 y aviso público de abril de 2026), que
sube el panel de 66 a 80 pesticidas y reemplaza límites basados en LOQ por límites de acción basados en
salud para varias categorías; Colorado exige más de 100 activos; Canadá tiene su propia lista obligatoria de
Health Canada. **Verifica el texto vigente antes de cotizar**, porque el panel define el precio.

```
Escenario (ILUSTRATIVO):
  Muestra: 15 g de flor seca molida, hidratada con 10 mL de agua 30 min
  QuEChERS EN 15662 + dSPE con PSA/C18/GCB
  Inyección en LC-MS/MS (analitos polares) y GC-MS/MS (organoclorados, PGRs volátiles)
  Recuperaciones obtenidas: 78-112 % ; RSD 4-14 % ; ME entre 61 % y 118 %
  → se calibra con matriz emparejada porque el ME de varios analitos está fuera de 80-120 %
  Costo del panel completo: 700.000-1.800.000 COP ; 7-15 días hábiles
```

## Qué preguntarle al laboratorio

1. ¿Qué protocolo usan: AOAC 2007.01, EN 15662 o uno propio? ¿Está validado en **mi** matriz?
2. ¿Calibran en solvente o con matriz emparejada? Si es en solvente, ¿cómo corrigen el efecto de matriz?
3. ¿Usan patrones internos marcados isotópicamente? ¿Para cuántos analitos del panel?
4. ¿Cuál es el LOQ por analito y cómo se compara con el límite regulatorio que me aplica?
5. ¿Cuántos analitos del panel tienen recuperación fuera de 70–120 % y cómo lo reportan?
6. ¿Con qué frecuencia corren blancos y fortificados dentro de la secuencia de rutina?

## Errores comunes

- **No hidratar la matriz seca antes de QuEChERS.** Sin agua, la partición no funciona y las recuperaciones
  se desploman para los analitos polares.
- **Abusar del GCB en flor verde.** Queda un extracto precioso y sin varios pesticidas planares.
- **Calibrar en solvente puro en LC-MS/MS.** Con supresión del 40 %, reportas un producto "conforme" que no
  lo es.
- **Reusar cartuchos SPE.** Nunca; el arrastre es real.
- **Pedir "el panel de pesticidas" sin decir cuál.** Cada jurisdicción tiene su lista; un panel de 30 no
  sirve para cumplir uno de 80.
- **Ignorar los reguladores de crecimiento (PGRs)** como daminozida y paclobutrazol: no siempre están en el
  panel básico y son de los hallazgos más frecuentes en cannabis (`200`).

## Conexión con otros módulos

→ `68-preparacion-de-muestra-solidos.md` — lo que pasa antes de limpiar.
→ `72-estandar-interno-y-adicion-de-estandar.md` — cómo se corrige el efecto de matriz.
→ `83-lc-ms-ms-y-mrm.md` — el detector donde el efecto de matriz duele más.
→ `101-analisis-de-micotoxinas.md` — inmunoafinidad y límites.
→ `102-pesticidas-multiresiduo.md` — el panel y su lectura regulatoria.
→ `200-pesticidas-en-cannabis.md` — los activos que aparecen de verdad en cannabis.
