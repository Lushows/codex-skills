# 148 — CO2 supercrítico (la tecnología que suena premium y casi nunca es tu camino)

La extracción con CO2 supercrítico (SFE) es la niña bonita del marketing de extractos: "sin solventes",
"limpia", "premium". Técnicamente es excelente para ciertas cosas y **completamente inútil** para otras — y
para una pyme colombiana es, salvo excepción, un servicio que se contrata, no un equipo que se compra. Este
módulo existe para que sepas cuándo pedirlo, cuánto pedir y, sobre todo, para que no pagues un sobreprecio por
un CO2 que no te aporta nada en tu producto.

El error caro que evita: pagar maquila de SFE para un extracto de hongos enfocado en β-glucanos. El CO2
supercrítico **no extrae β-glucanos**. Es tirar plata con estilo.

Términos: **fluido supercrítico (supercritical fluid)** = sustancia por encima de su temperatura y presión
críticas; se comporta a la vez como gas (difunde) y como líquido (disuelve). **Punto crítico del CO2** =
31,0 °C y 73,8 bar (7,38 MPa). **Cosolvente / modificador (co-solvent, entrainer)** = pequeño porcentaje de
etanol añadido para subir la polaridad. **Fraccionamiento (fractionation)** = separar en varios separadores a
distintas presiones.

## Por qué el CO2 supercrítico saca unas cosas y no otras

Por encima de su punto crítico, el CO2 tiene una densidad ajustable con presión, y la densidad manda el poder
solvente. Pero el CO2 es **apolar** (momento dipolar cero). Su comportamiento se parece al del hexano.

| Compuesto | ¿Lo extrae CO2 puro? | Con etanol 5–20 % como cosolvente |
|---|---|---|
| Terpenos volátiles | Sí, muy bien (baja presión) | Sí |
| Cannabinoides neutros y ácidos | Sí | Sí, más rápido |
| Ácidos grasos, ceras | Sí (por eso hay que winterizar, `191`) | Sí |
| Ergosterol | Sí | Sí |
| Triterpenos ganodéricos | Parcialmente; mejor con cosolvente | Sí |
| Hericenonas | Parcialmente | Sí |
| Fenoles polares | Poco | Mejor |
| **β-glucanos** | **No** | **No** |
| Proteínas / proteoglicanos | No | No |
| Azúcares, sales | No | No |

La consecuencia es directa: **si tu producto se declara por β-glucano, el CO2 supercrítico no participa.** Como
mucho puede ser un paso previo de desgrasado, no la extracción principal.

## Los parámetros que definen un servicio de SFE

```
Presión        100–400 bar típico (a más presión, más densidad → extrae más y menos selectivo)
Temperatura     35–70 °C (arriba del crítico; suave, ideal para termolábiles)
Flujo de CO2    kg de CO2 por kg de material (relación de solvente); 20–60 es común
Tiempo          1–5 h por carga
Cosolvente      0–20 % v/v de etanol
Separadores     1–3, a presiones decrecientes → fracciona ceras / resina / volátiles
```

Ejemplo de cómo pedirlo bien a un maquilador **(ILUSTRATIVO)**: *"Extracción de 20 kg de flor seca a 250 bar,
50 °C, 40 kg CO2/kg material, sin cosolvente, dos separadores; entregar fracción principal y fracción de
volátiles por separado, con balance de masa y COA de potencia por HPLC."* Si no puedes escribir la solicitud
así, todavía no estás listo para contratar el servicio.

## Ventajas y desventajas honestas

**A favor**
- Sin solvente residual que declarar: el CO2 se evapora completo (`87`). Ventaja regulatoria real.
- Temperatura baja: preserva termolábiles y formas ácidas (menos descarboxilación que un proceso caliente,
  `174`).
- Selectividad ajustable: presión y separadores permiten fraccionar sin cromatografía.
- No inflamable. En términos de seguridad de planta, es más manejable que hidrocarburos (`188`).

**En contra**
- **Costo de capital.** Un equipo de 5–20 L de canasta es una inversión de planta, no de pyme. A esto se suma
  el requisito de recipientes a presión con certificación e inspección periódica.
- **Costo operativo**: CO2 grado alimentario, compresores, mantenimiento de sellos.
- **No sirve para lo polar.** Punto final.
- **Productividad**: cargas discretas, tiempos largos, canastas relativamente pequeñas.
- En Colombia, a agosto de 2026, la oferta de maquila de SFE es limitada y concentrada; verifica capacidad real,
  certificación BPM de la planta y quién responde por el producto (`292`).

## Cómo se comprueba un extracto por SFE

| Atributo | Método | Por qué |
|---|---|---|
| Potencia del analito | HPLC-DAD / LC-MS/MS según el caso | Es lo que compras |
| Perfil de terpenos | GC-MS headspace (`86`, `199`) | Los volátiles se pierden fácil |
| Ceras y lípidos | Gravimetría tras winterización (`191`) | Definen si hay que refinar |
| Solventes residuales | GC-headspace (`87`) | Solo si hubo cosolvente etanólico |
| Metales pesados | ICP-MS (`88`) | El CO2 no los extrae, pero el equipo puede aportar |
| Balance de masa | Pesadas de entrada/salida/bagazo | Detecta pérdidas y sobreestimaciones |

Regla: exige **balance de masa** al maquilador. Entrada, extracto, bagazo. Si los números no cierran dentro de
un margen razonable, hay algo que no te están contando.

## Ejemplo aplicado — dos decisiones opuestas

```
CASO 1 — BIO-SETA, extracto de reishi declarado por β-glucano
  Analito: β-glucano (polar, alto PM)
  ¿SFE? NO. El CO2 no lo extrae. La ruta es agua caliente + etanol (`146`).
  Uso posible marginal: desgrasar la biomasa antes de la decocción. Rara vez lo justifica el costo.

CASO 2 — línea de cannabis, extracto para aceite sublingual
  Analitos: CBD/THC y terpenos (apolares)
  ¿SFE? SÍ, es una opción técnicamente sólida frente a etanol (`187`) e hidrocarburos (`188`).
  Preguntas antes de firmar la maquila:
    - ¿me entregan la fracción de terpenos aparte?
    - ¿cuánta cera trae? ¿incluyen winterización? (`191`)
    - ¿qué grado de descarboxilación tiene el extracto entregado? (`174`)
    - ¿COA por laboratorio independiente o del propio maquilador? (`108`, `113`)
```

Números de proceso **(ILUSTRATIVOS)** para el caso 2: 20 kg de flor a 250 bar / 50 °C rindiendo 12–18 % p/p de
crudo. Ese rango depende brutalmente del material; pídelo como compromiso escrito al maquilador y verifícalo
con el balance de masa del primer lote.

## Errores comunes

- Pagar sobreprecio por "extraído con CO2" en un producto cuyo activo es polar. No aporta nada.
- Creer que "sin solventes" significa "sin nada que analizar": ceras, metales y potencia siguen midiéndose.
- Ignorar el cosolvente: si usaron etanol, hay solvente residual y hay que medirlo.
- Contratar SFE sin especificar presión, temperatura, relación de CO2 y fracciones. Te entregan lo que a ellos
  les resulte cómodo.
- Comprar un equipo pequeño de segunda sin certificación de recipiente a presión. Es un riesgo de seguridad y
  un problema legal.
- Suponer que baja temperatura significa cero degradación: el tiempo y el oxígeno residual siguen actuando
  (`61`, `204`).

## Conexión con otros módulos

→ `189-extraccion-co2-en-cannabis.md` — el detalle del caso donde sí tiene sentido.
→ `146-extraccion-dual-y-por-que-importa.md` — por qué en hongos la ruta es otra.
→ `20-parametros-de-solubilidad-y-eleccion-de-solvente.md` — la teoría de qué disuelve qué.
→ `292-negociar-con-laboratorios-y-maquiladores.md` — cómo se contrata este servicio sin quedar mal parado.
→ `191-winterizacion-y-desceramiento.md` — el paso que casi siempre viene después.