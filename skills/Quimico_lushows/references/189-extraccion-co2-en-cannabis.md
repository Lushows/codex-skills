# 189 — Extracción con CO₂ en cannabis (la que mejor se vende y peor se entiende)

El CO₂ supercrítico es el método que más aparece en las etiquetas ("extraído con CO₂, sin solventes") y el
que menos gente entiende de verdad. Es limpio, no inflamable, el solvente se va solo al despresurizar y no
deja residuo tóxico — todo eso es cierto. Lo que las etiquetas no dicen es que **es caro, lento, y su
"selectividad ajustable" solo sirve si de verdad ajustas presión y temperatura**. Un CO₂ mal operado da un
crudo peor que un etanol frío bien operado, a diez veces el costo de capital. Este módulo te da la
fisicoquímica, los parámetros reales de la literatura y el criterio para saber si tiene sentido para ti.

Términos:
- **fluido supercrítico (supercritical fluid, SCF)** = por encima de su punto crítico, un fluido con densidad
  de líquido y difusividad de gas. Para el CO₂: **31,1 °C y 73,8 bar**.
- **subcrítico (subcritical)** = por debajo del punto crítico, CO₂ líquido: más suave, más selectivo a
  terpenos, menos rendimiento.
- **cosolvente / modificador (co-solvent, modifier)** = un poco de etanol añadido al CO₂ para subir su
  polaridad y su poder de extracción.
- **fraccionamiento (fractionation)** = separar en varios recipientes a distintas presiones, para obtener
  cortes de terpenos y de cannabinoides por separado.

## La física en una frase

La **densidad del CO₂** es la que extrae. Y la densidad la controlas con presión y temperatura. Más presión
= más densidad = más poder solvente (y menos selectividad). Más temperatura a presión constante = menos
densidad, pero mayor presión de vapor del soluto. Por eso hay ventanas óptimas y no una "receta".

| Régimen | Presión | Temperatura | Qué extrae bien | Costo relativo |
|---|---|---|---|---|
| Subcrítico | 55–75 bar | 10–25 °C | Terpenos, aceites ligeros | Bajo |
| Supercrítico suave | 150–250 bar | 40–55 °C | Cannabinoides, algo de cera | Medio |
| Supercrítico alto | 300–400 bar | 45–70 °C | Todo, incluidas ceras y clorofila ligera | Alto |
| Con cosolvente etanol 5–20 % | 200–350 bar | 40–70 °C | Máximo rendimiento; pierde el argumento "sin solvente" | Alto |

Datos de literatura para anclar: Rovetto y Aieta (*Journal of Supercritical Fluids*, 2017) reportan que
**350 bar y 45 °C** son condiciones adecuadas para alta recuperación de cannabinoides, y que agregar etanol
como cosolvente sube el rendimiento, con un máximo reportado de **30,9 ± 0,8 %** a 70 °C, 300 bar y 10 % de
etanol. Otros trabajos a 170 / 240 / 340 bar y 55 °C con cosolvente obtienen **8–19 % p/p** de cannabinoides,
el máximo a la presión más alta. **Ojo con el detalle incómodo:** los mejores rendimientos publicados usan
etanol. Si tu argumento de marketing es "sin solventes", entonces estás renunciando a esos rendimientos, y
además **si usas etanol tienes que declararlo y medirlo** (ver `201`).

## El fraccionamiento: lo que sí justifica el equipo

La ventaja real y difícil de replicar del CO₂ no es la limpieza, es el **fraccionamiento en línea**:

```
Extractor (alta presión)
   ↓ despresurización parcial
Separador S1 (presión intermedia)  → ceras y cannabinoides pesados
   ↓
Separador S2 (presión baja)        → fracción de cannabinoides
   ↓
Separador S3 (más baja)            → fracción de terpenos, aromática
   ↓
CO₂ recomprimido y reciclado
```

Con esa arquitectura sacas una fracción de terpenos aparte, la guardas y la reintroduces después en tu
formulación (ver `195`). Es la manera más limpia que existe de recuperar **tus propios** terpenos en vez de
comprar terpenos botánicos genéricos. Ese es el argumento técnico honesto del CO₂, no el "sin solventes".

## Las variables que mueven la aguja

1. **Densidad del CO₂** (presión × temperatura). La palanca principal.
2. **Relación masa de CO₂ / masa de biomasa (S/F ratio).** Típicamente 20:1 a 60:1 en masa. Es lo que fija el
   tiempo de ciclo: extraer más completo exige pasar más CO₂, y eso son horas.
3. **Granulometría y empaque del lecho.** Un lecho canalizado deja zonas sin extraer. La molienda uniforme
   (2–3 mm) y el empaque homogéneo valen más que 50 bar de más (ver `143`).
4. **Humedad de la biomasa.** El agua compite y forma hielo/tapones en la despresurización. Biomasa a ≤ 10 %.
5. **Descarboxilación previa.** El THCA es más polar y se extrae peor con CO₂ puro que el THC neutro. Muchas
   operaciones descarboxilan **antes** por eso (ver `174`). Si tu producto necesita forma ácida, esto no es
   una opción y tendrás que aceptar menor rendimiento o usar cosolvente.

## Cómo se mide / cómo se comprueba

| Ensayo | Técnica | Unidad | Por qué en esta ruta |
|---|---|---|---|
| Potencia y perfil | HPLC-DAD (`198`) | % p/p base seca | Recuperación real; ojo THCA vs. neutro |
| Terpenos | GC-MS / GC-FID headspace (`199`) | mg/g | Valorar la fracción aromática del fraccionamiento |
| Solventes residuales | GC-MS headspace (`201`) | ppm | **Obligatorio si usaste cosolvente etanol**; el CO₂ en sí no deja residuo |
| Metales pesados | ICP-MS (`202`) | µg/kg | Se concentran igual que el activo |
| Pesticidas | LC-MS/MS y GC-MS/MS (`200`) | µg/kg | El CO₂ extrae muy bien los pesticidas apolares |
| Biomasa agotada | HPLC-DAD | % p/p base seca | El único modo de saber si el ciclo terminó |

Ese último es el control de proceso propio del CO₂: **cuándo parar**. Como el ciclo es largo y el CO₂ es
caro de recomprimir, la pregunta económica es en qué minuto el gramo adicional ya no paga la energía. Se
responde con una curva de extracción (masa acumulada de extracto vs. masa de CO₂ pasada) y análisis de la
torta. Ejecuta la curva y el punto de corte con `lab-tools/rendimiento_extraccion.py` y rutea el
óptimo económico a `economist_lushows`. **Nada de eso se decide de memoria.**

## Ejemplo aplicado (ILUSTRATIVO)

Extractor de 20 L, 5,0 kg de flor descarboxilada con 17,5 % p/p de THC total (HPLC-DAD, base seca).
300 bar, 50 °C, S/F 40:1, tres separadores. Cifras **(ILUSTRATIVO)**:

| Fracción | Masa | Cannabinoides totales | Terpenos totales | Destino |
|---|---|---|---|---|
| S1 (ceras/pesados) | 0,18 kg | 22 % p/p | 0,3 % | Reproceso o descarte |
| S2 (cannabinoides) | 0,74 kg | 71 % p/p | 1,1 % | Winterización → destilación |
| S3 (aromática) | 0,04 kg | 9 % p/p | 48 % p/p | Reintroducir en formulación |
| Biomasa agotada | 4,0 kg | 1,9 % p/p base seca | — | Analizar |

THC total que entró = 5,0 × 0,175 = 0,875 kg. En S2 ≈ 0,74 × 0,68 = 0,503 kg. Recuperación en la fracción
principal ≈ **57 %** — y ese es justo el punto: **casi 2 % de cannabinoides quedaron en la torta**, que sobre
4 kg son unos 76 g de activo. Si tu ciclo se corta temprano para ahorrar energía, ese es el costo escondido.
Todas las cifras son ilustrativas: hay que levantar la curva con tu equipo y tu material.

## Equipo modesto vs. maquila

| Actividad | Con equipo modesto | Exige maquila / planta |
|---|---|---|
| Extracción CO₂ a cualquier escala | No: es equipo a 300–400 bar, con certificación de recipientes a presión | **Sí** |
| Preparación de biomasa (secado, molienda) | Sí (`186`, `143`) | — |
| Descarboxilación previa | Sí, con horno y datalogger (`174`) | Reactor para lotes grandes |
| Formulación con la fracción aromática | Sí (`195`) | — |
| Winterización del S2 | Sí (`191`) | — |
| Todos los análisis | No | Sí — laboratorio acreditado (`107`, `108`) |

Realismo económico: un equipo de CO₂ de escala productiva cuesta un orden de magnitud más que una línea de
etanol de capacidad equivalente, y su productividad por hora es menor. **Solo tiene sentido si vendes el
fraccionamiento o si tu mercado paga la narrativa "CO₂".** Corre esa cuenta con `economist_lushows` antes de
comprar.

Nota de seguridad: el CO₂ no es inflamable, pero **es asfixiante y trabaja a 300–400 bar**. El riesgo aquí no
es fuego, es **descompresión explosiva de un recipiente a presión y desplazamiento de oxígeno en sala
cerrada**. Exige recipientes certificados, válvulas de alivio, detector de CO₂ en ambiente y ventilación
(ver `08`).

## Errores comunes

- **Decir "sin solventes" y usar etanol como cosolvente.** Es publicidad falsa y, si el COA de solventes
  residuales lo detecta, es un problema regulatorio, no de marketing (`267`, `293`).
- **Operar con "la receta" del fabricante sin levantar la curva propia.** Cada cultivar y cada molienda
  cambia el punto de corte.
- **No descarboxilar cuando el producto lo permite** y luego culpar al equipo del bajo rendimiento del THCA.
- **Empacar el lecho a la brava.** El canalizado deja bolsas sin extraer y arruina la reproducibilidad.
- **No analizar la biomasa agotada.** Sin ese número no sabes si el ciclo fue completo o si botaste plata.
- **Comprar CO₂ de soldadura.** Exige grado alimenticio o superior, con COA del lote.
- **Comparar rendimientos de CO₂ contra hidrocarburo sin fijar base ni definir qué se cuenta como extracto.**

## Conexión con otros módulos

→ `148-co2-supercritico.md` — la fisicoquímica general del método, fuera del cannabis.
→ `28-gases-y-presion-de-vapor.md` — por qué existe un punto crítico.
→ `187-extraccion-con-etanol.md` y `188-extraccion-con-hidrocarburos.md` — las alternativas y su trade-off.
→ `191-winterizacion-y-desceramiento.md` — qué hacer con las ceras del S1 y del S2.
→ `192-destilacion-de-cannabinoides.md` — el paso siguiente del corte principal.
→ `199-analisis-de-perfil-de-terpenos.md` — cómo se valora la fracción aromática.
→ `201-solventes-residuales-en-cannabis.md` — obligatorio si hubo cosolvente.
→ `195-formulacion-de-aceites-y-comestibles.md` — dónde se reintroducen tus propios terpenos.
