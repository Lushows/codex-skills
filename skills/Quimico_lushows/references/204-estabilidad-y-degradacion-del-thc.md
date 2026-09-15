# 204 — Estabilidad y degradación del THC (el producto envejece y la etiqueta no)

Un cannabinoide no es una molécula inerte guardada en un frasco: es un fenol con dobles enlaces que se
oxida, se isomeriza y se descarboxila con el tiempo. El THCA se convierte en Δ9-THC; el Δ9-THC se oxida a
CBN; el CBD puede isomerizarse a THC en medio ácido. Esto significa que **el COA que hiciste el día de
producción no describe el producto que el cliente abre 14 meses después**. Y si tu etiqueta dice "10 mg de
THC por porción", esa promesa tiene que sostenerse durante toda la vida útil declarada, no solo el primer día.

Términos: **CBN (cannabinol)** = producto de oxidación del Δ9-THC; marcador de envejecimiento.
**Descarboxilación (decarboxylation)** = pérdida de CO2 que convierte THCA en Δ9-THC. **Isomerización
(isomerization)** = reordenamiento de la molécula sin cambio de fórmula, típicamente catalizado por ácido.
**Estudio acelerado (accelerated stability)** = almacenar a 40 °C / 75 % HR para predecir vida útil.

## Las cuatro rutas de degradación

| Ruta | De → a | Qué la acelera | Cómo se detecta |
|---|---|---|---|
| Descarboxilación | THCA → Δ9-THC + CO2 | Calor, tiempo | Baja THCA, sube Δ9-THC; THC total casi constante |
| Oxidación | Δ9-THC → CBN | Oxígeno, luz, calor | Sube CBN, baja THC total |
| Isomerización | Δ9-THC ↔ Δ8-THC; CBD → THC | Ácido, calor, sílice ácida | Aparece Δ8-THC donde no había |
| Degradación de terpenos | Monoterpenos → óxidos | Oxígeno, luz, calor | Sube óxido de cariofileno; baja el total |

La firma de diagnóstico más útil: **si el THC total baja y el CBN sube, es oxidación**. **Si el THCA baja y
el Δ9-THC sube pero el THC total se mantiene, es descarboxilación** — y eso no es pérdida de valor, es
transformación (ver `174`). Confundir ambas cosas hace que la gente culpe al proveedor de un problema que en
realidad es de temperatura de almacenamiento.

## Los cuatro enemigos, en orden de importancia

1. **Oxígeno.** Es el principal. Envase con espacio de cabeza grande = producto envejecido. Solución: envase
   ajustado al volumen, barrera de oxígeno, y en algunos casos atmósfera modificada.
2. **Luz, especialmente UV.** La literatura clásica sobre estabilidad de cannabis identifica la luz como el
   factor más destructivo del THC. Solución: vidrio ámbar o envase opaco, y almacenamiento en oscuridad.
3. **Temperatura.** Regla práctica de cinética: por cada 10 °C de aumento, la velocidad de degradación
   aproximadamente se duplica (Q10 ≈ 2). Verifica el Q10 real de tu producto con tu propio estudio.
4. **Ácido y superficies activas.** Un pH bajo (gomitas ácidas, bebidas cítricas) favorece isomerización.
   Ojo con los productos "con sabor a limón" y su pH.

## El estudio de estabilidad, hecho como se debe

El marco es **ICH Q1A(R2)** para estabilidad y **ICH Q1E** para extrapolación. Se aplica igual a suplementos
y productos de cannabis aunque no sean medicamentos, porque es el único marco defendible.

| Condición | Temperatura / HR | Duración típica | Para qué |
|---|---|---|---|
| Largo plazo (zona II) | 25 °C ± 2 / 60 % HR ± 5 | 12, 24, 36 meses | Vida útil real |
| Largo plazo (zona IVb, clima Colombia) | 30 °C ± 2 / 75 % HR ± 5 | 12, 24 meses | Condición realista para trópico |
| Intermedia | 30 °C / 65 % HR | 12 meses | Puente |
| Acelerada | 40 °C ± 2 / 75 % HR ± 5 | 6 meses | Predicción y detección temprana |

**Colombia está en zona climática IVb** (caliente y muy húmeda) en la clasificación ICH/OMS para estudios de
estabilidad. Usar la condición de zona II (25 °C / 60 %) para un producto que se va a distribuir en
Barranquilla es subestimar el estrés real. Verifica la zona asignada en la guía vigente de la OMS o en la
resolución del INVIMA que aplique a tu categoría.

Puntos de muestreo típicos: 0, 3, 6, 9, 12, 18, 24, 36 meses para largo plazo; 0, 3, 6 para acelerado.
Mínimo tres lotes. Ensayos en cada punto: potencia de cannabinoides, perfil completo (para ver CBN y Δ8),
apariencia, pH si aplica, aW si aplica, microbiología, y para líquidos también peróxidos.

## Cómo se mide / cómo se comprueba

El criterio de aceptación se fija antes de empezar. Lo habitual, prestado de farmacia: **el activo debe
permanecer entre 90 % y 110 % del valor declarado** durante toda la vida útil. Con eso se calcula la
sobrecarga de formulación (ver `195`).

```
Cinética de primer orden:
    ln(C_t) = ln(C_0) − k·t

Vida útil hasta el 90 % del valor inicial:
    t_90 = 0,1054 / k

Arrhenius (para extrapolar de 40 °C a 25 °C):
    k = A · exp(−Ea / (R·T))
    ln(k2/k1) = −(Ea/R) · (1/T2 − 1/T1)      con T en kelvin
```

Nunca hagas esta extrapolación de cabeza. Usa `lab-tools/vida_util_arrhenius.py` o rutea a
`Matematicas_lushows`. Y recuerda la limitación honesta: **Arrhenius solo vale si el mecanismo de
degradación es el mismo a las dos temperaturas**. Si a 40 °C aparece una ruta que a 25 °C no existe, la
extrapolación miente. Por eso el estudio acelerado orienta pero **no reemplaza** el de largo plazo.

## Ejemplo aplicado (ILUSTRATIVO)

Aceite de espectro completo, envase ámbar de 30 mL, condición 30 °C / 75 % HR:

| Mes | Δ9-THC (mg/mL) | CBN (mg/mL) | THC total (mg/mL) | % del valor inicial |
|---|---|---|---|---|
| 0 | 10,2 | 0,08 | 10,3 | 100 % |
| 3 | 10,0 | 0,21 | 10,1 | 98 % |
| 6 | 9,7 | 0,44 | 9,8 | 95 % |
| 12 | 9,2 | 0,88 | 9,3 | 90 % |
| 18 | 8,6 | 1,35 | 8,7 | 84 % |

Cifras **(ILUSTRATIVO)**. Lectura: el producto cruza el umbral del 90 % alrededor del mes 12. Vida útil
defendible: **12 meses**, no los 24 que dice la etiqueta que ya se imprimió. Y el CBN subiendo casi en
proporción a lo que baja el THC confirma que la ruta es oxidación, es decir, el problema es **oxígeno en el
envase**, no la formulación. La corrección es de empaque, no de fórmula.

## Errores comunes

- **Declarar vida útil sin estudio.** "24 meses porque todos ponen 24 meses" no es dato, es copia.
- **Usar condición de zona II para producto tropical.** Colombia es zona IVb; el estrés real es mayor.
- **Analizar solo THC y no el panel completo.** Sin CBN ni Δ8 no puedes diagnosticar la ruta de degradación.
- **Confundir descarboxilación con pérdida.** Si el THC total se mantiene, no perdiste activo, se transformó.
- **Extrapolar de acelerado sin verificar el mecanismo.** Arrhenius con mecanismo cambiado da números
  bonitos y falsos.
- **Guardar la contramuestra en condiciones distintas al producto comercial.** Entonces tu referencia no
  representa nada.
- **Envasar en frasco grande con mucho aire.** El espacio de cabeza es el reactor donde ocurre la oxidación.

## Conexión con otros módulos

→ `174-descarboxilacion-cinetica-y-calculo.md` — la transformación que no es pérdida.
→ `177-cbg-cbc-y-cbn.md` — qué es el CBN y qué significa encontrarlo.
→ `164-estabilidad-ich-q1-y-vida-util.md` — el marco general de estabilidad.
→ `165-estudios-acelerados-y-arrhenius.md` — las matemáticas de la extrapolación.
→ `163-envase-primario-y-compatibilidad.md` — la solución real cuando la ruta es oxidación.
→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — la química de fondo.
