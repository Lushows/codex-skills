# 34 — Reología y viscosidad (por qué el gotero gotea mal y la bomba no mueve el extracto)

La reología es cómo fluye tu producto, y decide cosas muy concretas: si el gotero entrega 1 mL o 0,6 mL, si
la máquina llena 30 unidades por minuto o 12, si el polvo se apelmaza en la tolva, si la crema se siente
"barata" en la piel, y si el extracto se puede bombear a 20 °C o toca calentarlo. Es una de las pocas
propiedades físicas que el consumidor **percibe directamente**, y una de las que más causa paradas de
línea. También es donde más se miente sin querer: "viscosidad" sin decir a qué temperatura y a qué
velocidad de corte no es un dato.

Términos: **viscosidad (viscosity, η)** = resistencia a fluir; en pascal-segundo (Pa·s) o centipoise (cP);
1 Pa·s = 1 000 cP. **esfuerzo de corte (shear stress)** = fuerza por área aplicada al fluido, en Pa.
**velocidad de corte (shear rate, γ̇)** = gradiente de velocidad, en 1/s. **newtoniano (Newtonian)** =
fluido cuya viscosidad no depende de la velocidad de corte. **pseudoplástico (shear-thinning)** = se
adelgaza al agitar. **tixotrópico (thixotropic)** = se adelgaza con el tiempo de agitación y se recupera al
reposar. **umbral de fluencia (yield stress)** = esfuerzo mínimo para que empiece a fluir.

## Los comportamientos, y dónde los vives

| Comportamiento | Cómo se porta | Ejemplo en tu producto |
|---|---|---|
| Newtoniano | η constante | Agua, etanol, aceite MCT, tinturas diluidas |
| Pseudoplástico (shear-thinning) | Baja η al agitar | Jarabes con goma xantana, geles tópicos |
| Dilatante (shear-thickening) | Sube η al agitar | Suspensiones de polvo muy concentradas; problema de bombeo |
| Con umbral de fluencia (Bingham/Herschel-Bulkley) | No fluye hasta cierto esfuerzo | Cremas, pastas, extracto crudo frío |
| Tixotrópico | Se adelgaza con el tiempo y se recupera | Suspensiones que se agitan antes de usar |
| Viscoelástico | Parte sólido, parte líquido | Gomas (gummies), geles, resinas de cannabis |

Un pseudoplástico bien diseñado es el mejor amigo de una suspensión: **grueso en reposo** (no sedimenta,
Stokes, `32`) y **fino al agitar o al bombear** (llena rápido, se dosifica). Eso es exactamente lo que hace
la goma xantana al 0,1–0,3 % en un jarabe.

## Los números que se usan

```
Ley de Newton:            τ = η · γ̇                τ en Pa, γ̇ en 1/s

Ley de potencia (Ostwald-de Waele):  τ = K · γ̇ⁿ
    n = 1   newtoniano
    n < 1   pseudoplástico   (la mayoría de tus fórmulas espesadas)
    n > 1   dilatante

Herschel-Bulkley (con umbral):  τ = τ0 + K · γ̇ⁿ

Arrhenius para viscosidad:  η = η0 · e^(Ea/(R·T))
    → la viscosidad cae fuerte con la temperatura; por eso el extracto se bombea caliente
```

Órdenes de magnitud útiles: agua a 20 °C ≈ 1 cP; aceite MCT ≈ 25–30 cP; jarabe simple ≈ 150–200 cP; miel ≈
2 000–10 000 cP; extracto crudo de cannabis a temperatura ambiente ≈ 10⁵–10⁷ cP (prácticamente sólido) y a
60 °C baja varios órdenes de magnitud. Esa última es la razón por la que las plantas de extracción tienen
mantas calefactoras en todas las líneas.

## Velocidades de corte de la vida real

| Operación | Velocidad de corte típica (1/s) | Consecuencia |
|---|---|---|
| Sedimentación de una partícula | 10⁻⁶ – 10⁻³ | Aquí importa la viscosidad **a corte muy bajo** |
| Nivelación de una crema | 10⁻² – 10⁻¹ | Determina si se ve pareja |
| Vertido de un frasco | 10 – 100 | Percepción del consumidor |
| Gotero / dosificador | 10² – 10³ | Exactitud de la dosis (`161`) |
| Bombeo y llenado | 10² – 10³ | Velocidad de línea |
| Frotado en la piel | 10³ – 10⁴ | Sensación al aplicar (`196`) |
| Aspersión / atomización | 10⁴ – 10⁵ | Tamaño de gota en secado por aspersión (`150`) |

Aquí está la trampa clásica: se mide la viscosidad **a una sola velocidad** y se usa para predecir todo. En
un pseudoplástico, la viscosidad a 1 1/s y a 1 000 1/s difieren por un factor de 10 o más. Un dato de
viscosidad sin γ̇ declarado es inservible para diseñar (`02`).

## Por qué el gotero es un problema reológico y de cumplimiento

Un gotero de 1 mL dosifica por volumen, pero el usuario cuenta **gotas**. El volumen de gota depende de la
tensión superficial y de la viscosidad, no solo del orificio. Cambiar el aceite portador de MCT a aceite de
oliva, o subir la concentración del extracto, cambia el tamaño de gota — y con él, los miligramos por gota
que declaras en la etiqueta.

```
Verificación obligatoria (ILUSTRATIVO):
  Gotas por mL, medidas en triplicado con el gotero real, a 20 °C
  MCT + extracto 5 %:   n = 28 gotas/mL  →  1,79 mg de CBD por gota si la base es 50 mg/mL
  MCT + extracto 20 %:  n = 24 gotas/mL  →  contenido por gota distinto, aunque el frasco diga lo mismo

Si la etiqueta declara "X mg por gota", ese número debe verificarse con el envase final (`163`, `272`).
```

## Cómo se mide

| Pregunta | Método | Unidad / requisito |
|---|---|---|
| ¿Cuál es la viscosidad? | Viscosímetro rotacional (Brookfield) con aguja y rpm declaradas | cP a T y rpm específicas |
| ¿Cómo se comporta con el corte? | Reómetro rotacional: curva de flujo η vs γ̇ | Pa·s vs 1/s; ajustar ley de potencia (n, K) |
| ¿Tiene umbral de fluencia? | Barrido de esfuerzo en reómetro | τ0 en Pa |
| ¿Es viscoelástico? | Barrido oscilatorio: G' (elástico) y G'' (viscoso) | Pa; G' > G'' = comportamiento tipo gel |
| ¿Es tixotrópico? | Rampa arriba/abajo, área del ciclo de histéresis | Pa/s; tiempo de recuperación |
| ¿Cuántas gotas por mL? | Conteo gravimétrico con el gotero real, triplicado | gotas/mL y mg/gota |
| ¿Fluye el polvo? | Ángulo de reposo, índice de Carr, celda de corte | grados; % ; función de flujo (`143`) |

Regla dura: reportar `viscosidad 3 500 cP` sin decir instrumento, aguja, rpm y temperatura es un dato que
nadie puede reproducir. La especificación correcta dice: *3 500 ± 500 cP (Brookfield LV, aguja 4, 20 rpm,
25,0 ± 0,5 °C)* (`282`).

## Ejemplo aplicado — jarabe de hongos que se sedimenta o no se puede llenar

Jarabe con extracto de melena de león en suspensión, 250 mL, se prueban tres niveles de goma xantana
**(ILUSTRATIVO)**:

```
Xantana (% p/p)   η a 0,1 1/s   η a 500 1/s   n     Sedimento a 3 meses   Velocidad de llenado
     0,00             12 cP         11 cP     1,00   Capa de 8 mm            48 unidades/min
     0,10          1 800 cP         95 cP     0,52   Capa de 2 mm            44 unidades/min
     0,20          6 400 cP        180 cP     0,41   Sin sedimento           38 unidades/min
     0,35         21 000 cP        410 cP     0,33   Sin sedimento           19 unidades/min

Uniformidad de contenido de β-glucano entre primera y última dosis del frasco (K-YBGL):
     0,00 % xantana → diferencia de 41 %      0,20 % xantana → diferencia de 4 %
```

La decisión: 0,20 % de xantana. Detiene la sedimentación, mantiene la línea a 38 unidades/min, y —lo que
de verdad importa— hace que la primera y la última cucharada tengan la misma dosis. Esa uniformidad no es
un capricho: es el atributo que sostiene el contenido declarado en la etiqueta durante toda la vida útil
(`161`, `282`). A 0,35 % la línea cae a menos de la mitad y el producto se siente pastoso; se paga mucho
por un beneficio que ya se había conseguido.

## Errores comunes

- Reportar viscosidad sin temperatura, sin instrumento y sin velocidad de corte.
- Medir a una sola velocidad un fluido pseudoplástico y extrapolar.
- Cambiar el aceite portador o la concentración y no volver a verificar mg por gota (`161`).
- Espesar hasta que "se vea rico" sin medir el impacto en la velocidad de línea y en el costo.
- Ignorar la reología del polvo. La mitad de los problemas de encapsulado son de flujo, no de fórmula (`143`, `154`).
- Suponer que si no se ve sedimento, la dosis es uniforme. Se comprueba analizando primera y última dosis.
- Bombear extracto crudo frío y quemar la bomba. La viscosidad cae exponencialmente con la temperatura.

## Conexión con otros módulos

→ `32-coloides-emulsiones-y-espumas.md` — la viscosidad como freno del cremado (Stokes).
→ `33-tensioactivos-y-hlb.md` — la otra palanca de estabilidad de una emulsión.
→ `143-molienda-y-granulometria.md` — flujo de polvos y su medición.
→ `156-liquidos-goteros-y-jarabes.md` — la forma farmacéutica donde esto se decide.
→ `161-dosis-y-tamano-de-porcion.md` — mg por gota y uniformidad de contenido.
→ `196-topicos-y-transdermicos.md` — reología y sensación en la piel.
→ `282-especificacion-de-producto-terminado.md` — cómo se escribe una especificación de viscosidad.
