# 105 — Quimiometría: PCA y modelos (cuándo un gráfico bonito significa algo y cuándo no)

La **quimiometría (chemometrics)** es la estadística que convierte una matriz de miles de señales —un
espectro NIR, un cromatograma completo, una corrida de metabolómica— en una decisión: *este lote es el mismo
que el anterior*, *este polvo tiene sustrato de grano*, *este NIR predice la humedad sin destruir la muestra*.
El error caro que evita este módulo es exactamente el contrario: creerle a un gráfico de PCA con seis
muestras y usarlo para acusar a un proveedor o para sostener un claim. En quimiometría, un modelo que no fue
**validado con muestras que nunca vio** no es un resultado; es una ilusión óptica cara.

Términos: **variable latente (latent variable)** = combinación de las señales originales que resume la
información. **PCA (principal component analysis)** = análisis de componentes principales; **no supervisado**:
no le dices los grupos. **PLS-DA / OPLS-DA** = modelos **supervisados** de clasificación: sí les dices los
grupos. **sobreajuste (overfitting)** = el modelo aprendió el ruido de tus muestras, no el fenómeno.
**Q²** = capacidad de predecir muestras que el modelo no vio. **loadings** = qué señales pesan en cada
componente.

## No supervisado vs supervisado (la distinción que define si el resultado vale)

| | No supervisado (PCA, HCA) | Supervisado (PLS-DA, OPLS-DA, PLS, SIMCA) |
|---|---|---|
| Le dices los grupos | No | Sí |
| Para qué sirve | Explorar, ver estructura, detectar atípicos | Clasificar, predecir un valor |
| Riesgo de autoengaño | Bajo | **Alto**: separa incluso datos aleatorios |
| Se valida con | Inspección, varianza explicada | Validación cruzada + permutación + set externo |
| Cuándo lo usas primero | **Siempre primero** | Solo después de que el PCA muestre algo |

Regla de oro del oficio: **si el PCA no muestra ninguna separación, un PLS-DA que sí la muestra es
sospechoso**, no es un hallazgo. El supervisado siempre encuentra una frontera; la pregunta es si esa
frontera sobrevive a datos nuevos.

## Preprocesado: donde se decide el 80 % del resultado

Antes de modelar hay que quitar lo que no es química: deriva de línea base, dispersión de luz, diferencias de
masa de muestra.

| Tratamiento | Qué corrige | Cuándo se usa |
|---|---|---|
| Centrado en la media | Desplazamiento común | Casi siempre |
| Escalado a varianza unitaria (autoescalado) | Que las señales grandes dominen | Cuando las variables tienen escalas distintas |
| Escalado de Pareto | Igual, pero suave | Metabolómica (evita inflar el ruido) |
| Primera/segunda derivada (Savitzky-Golay) | Línea base y solapamiento | NIR, FTIR (ver `92`) |
| SNV / MSC | Dispersión por tamaño de partícula | NIR de polvos (ver `143`) |
| Normalización por suma total o por estándar interno | Diferencias de cantidad inyectada | LC-MS (ver `72`) |

Una advertencia práctica: **el preprocesado se decide con el set de entrenamiento y se aplica igual al set de
prueba**. Si autoescalas usando todas las muestras juntas, ya filtraste información del set de prueba al
modelo y tu validación queda inflada. Es el error silencioso más frecuente.

## Las tres validaciones que hacen honesto un modelo

1. **Validación cruzada (cross-validation).** Se aparta un pedazo de las muestras, se entrena con el resto y
   se predice el pedazo apartado. Repetido por bloques. Da **Q²**. Si R² es alto y Q² es bajo, hay
   sobreajuste: el modelo memorizó.
2. **Prueba de permutación (permutation test).** Se barajan las etiquetas de grupo al azar 100–1.000 veces y
   se reentrena. Si tu modelo real no es claramente mejor que los modelos con etiquetas barajadas, tu
   separación es azar. Es la prueba que más modelos mata, y por eso la que menos se publica.
3. **Set de prueba externo.** Muestras que nunca entraron al entrenamiento, idealmente de otro día, otro
   operario u otro lote. Es la única validación que convence a un auditor.

```
Criterios de lectura rápidos (convención de uso, no norma):
  R2X   = varianza de los datos explicada por el modelo
  R2Y   = varianza de la respuesta/clase explicada     -> siempre alto, no impresiona
  Q2    = varianza predicha en validacion cruzada      -> el numero que importa
  R2Y - Q2 grande (> ~0,3) -> sobreajuste probable
  Permutacion: la nube de Q2 permutados debe quedar CLARAMENTE por debajo del Q2 real
```

## Calibración multivariada: el NIR que predice humedad o β-glucano

El caso de negocio más rentable de la quimiometría en una pyme: usar un **NIR** (barato, no destructivo,
segundos por muestra) para predecir un parámetro que hoy se mide con un método caro y lento.

```
Ciclo de trabajo de una calibracion NIR
1. Reunir 40-100 muestras que CUBRAN el rango real (si tu humedad varia 4-9 %, necesitas
   muestras en todo ese rango, no todas en 6 %).
2. Medir el valor de referencia con el metodo primario (Karl Fischer para humedad, ver 98;
   K-YBGL para beta-glucano, ver 91). El modelo NUNCA sera mejor que su referencia.
3. Construir PLS con preprocesado y numero de variables latentes elegido por validacion cruzada.
4. Reportar SEC (error de calibracion) y SEP (error de prediccion en set externo), con unidad.
5. Definir el rango de aplicabilidad y que hacer con muestras fuera de el (outliers por T2 de
   Hotelling y residual Q).
6. Monitorear en el tiempo: el modelo se degrada con cambios de proveedor, molienda o equipo.
```

Regla dura: **un modelo NIR no reemplaza el método de referencia para un COA ni para una liberación de lote**
mientras no esté validado formalmente y aceptado por quien recibe el resultado. Sirve para control de proceso
y decisiones internas rápidas. Es la diferencia entre "tamizar" y "certificar" (ver `75`, `283`).

## Ejemplo aplicado (ILUSTRATIVO)

Calibración NIR para humedad en polvo de cuerpo fructífero de reishi, BIO-SETA.

```
Muestras            : 62 lotes historicos, humedad por Karl Fischer 3,8-9,6 % p/p
Espectros           : NIR 1.100-2.500 nm, 3 replicas por muestra, promediadas
Preprocesado        : SNV + 1a derivada Savitzky-Golay (ventana 11, polinomio 2)
Modelo              : PLS, 4 variables latentes (elegidas por validacion cruzada por bloques)
R2 calibracion      : 0,981
SEC                 : 0,21 % p/p humedad
Set externo (n=15)  : SEP = 0,28 % p/p humedad
Rango de aplicacion : 3,5-10,0 % p/p; fuera de ahi -> ir a Karl Fischer
Uso aprobado        : control de proceso de secado (ver 142); NO para el COA
```

Lectura: con ±0,3 % p/p de error, el NIR sirve para decidir cuándo apagar el secador, pero no para declarar
la humedad que corrige la base seca del COA, donde ese error se propaga al β-glucano. Cifras **(ILUSTRATIVO)**.
Toda la aritmética de propagación de error va a `Matematicas_lushows` y a `76-incertidumbre-de-medida.md`.

## Errores comunes

- **Presentar un PLS-DA sin prueba de permutación.** Con 5 vs 5 muestras separa cualquier cosa, incluso ruido.
- **Autoescalar con todo el conjunto** y luego "validar": la validación ya está contaminada.
- **Calibrar en un rango estrecho** y usar el modelo fuera de él. Extrapolar en PLS es inventar.
- **Confundir R² con capacidad predictiva.** El número que decide es Q² o el SEP del set externo.
- **Olvidar que el modelo hereda el error de la referencia.** Un NIR calibrado contra un método malo predice
  bien el método malo.
- **No re-validar tras cambiar molienda, proveedor o equipo.** El modelo envejece y nadie le avisa.
- **Usar el gráfico de PCA como prueba de fraude.** El PCA dice dónde mirar; la prueba es el número dirigido
  (ver `104`).

## Conexión con otros módulos

→ `104-metabolomica-y-huella-quimica.md` — el generador de datos que esta estadística interpreta.
→ `92-ftir-y-nir.md` — la técnica donde la calibración multivariada rinde más por peso.
→ `78-estadistica-para-el-laboratorio.md` — la estadística univariada previa, que resuelve el 90 % de los casos.
→ `76-incertidumbre-de-medida.md` — cómo se propaga el error de la referencia al modelo.
→ `287-diseno-de-experimentos-doe.md` — diseñar el experimento antes de modelarlo, no después.
→ `75-validacion-de-metodos-ich-q2-r2.md` — qué hace falta para que un modelo sea aceptable en un COA.
