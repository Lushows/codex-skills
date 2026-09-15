# 139 — Interacciones planta-fármaco (lo que sí está documentado, sin alarmismo y sin promesas)

Este es el módulo que te permite responder bien la pregunta más frecuente y más delicada que le llega a una
marca de productos naturales: *"yo tomo warfarina / losartán / sertralina, ¿puedo tomar esto?"*. Hay dos
maneras de arruinarlo: decir "es natural, no pasa nada" (falso y peligroso) o decir "no, jamás, es
peligrosísimo" (falso también, y además destruye la venta sin motivo). La respuesta correcta es una tercera:
explicar qué se sabe, con qué nivel de evidencia, y remitir la decisión a quien la puede tomar. El error caro
que evita: que tu bot o tu vendedor dé un consejo médico —lo cual, además de riesgoso, te saca del marco
legal de un suplemento en Colombia (`267`, `268`).

Términos: **interacción farmacocinética (pharmacokinetic interaction)** = una sustancia cambia la
concentración de la otra (absorción, metabolismo, transporte, eliminación). **Interacción farmacodinámica
(pharmacodynamic interaction)** = ambas actúan sobre el mismo efecto, sumando o restando, sin cambiar
concentraciones. **Inhibición vs inducción de CYP** = frenar o acelerar la enzima que metaboliza el fármaco.
**Índice terapéutico estrecho (narrow therapeutic index, NTI)** = fármacos donde un cambio pequeño de
concentración importa mucho (warfarina, litio, digoxina, ciclosporina, tacrolimus, levotiroxina, fenitoína).

## Los mecanismos, en orden de importancia práctica

| Mecanismo | Qué hace | Ejemplo canónico |
|---|---|---|
| **Inhibición de CYP450** | Sube la concentración del fármaco: más efecto, más toxicidad | CBD sobre CYP3A4 y CYP2C19 (`124`) |
| **Inducción de CYP450 / P-gp** | Baja la concentración: el fármaco deja de funcionar | Hierba de San Juan (*Hypericum perforatum*) |
| **Transportadores (P-gp, BCRP, OATP)** | Cambian absorción y distribución | Jugo de toronja sobre OATP y CYP3A4 intestinal |
| **Conjugación fase II (UGT, SULT)** | Compite por la eliminación | (`125`) |
| **Absorción física** | Fibra, taninos y cationes quelan o retrasan | Fibra viscosa y levotiroxina: se separan las tomas |
| **Farmacodinámica aditiva** | Mismo efecto, sumado | Antiagregantes + antiagregantes; sedantes + sedantes |

Punto de calibración: **la inducción suele ser más peligrosa que la inhibición** en la vida real, porque el
fallo es silencioso. Si un anticonceptivo o un inmunosupresor pierde efecto, no hay síntoma de aviso: hay
consecuencia.

## Lo que está documentado — con nivel de evidencia honesto

| Combinación | Qué se ha descrito | Nivel de evidencia | Lectura práctica |
|---|---|---|---|
| **CBD + clobazam** | El CBD inhibe CYP2C19; sube el metabolito activo N-desmetilclobazam y aumenta la somnolencia. Está en la ficha técnica del medicamento con CBD purificado | **[clínico, fase 3 y ficha de producto]** — el dato más sólido del bloque | Interacción real y establecida |
| **CBD + valproato** | Elevación de transaminasas al combinarlos | **[clínico fase 3]** | Requiere monitoreo médico |
| **CBD + sustratos de CYP3A4/2C19** (muchos) | Inhibición demostrada in vitro y coherente con los datos clínicos anteriores | **[in vitro]** + extrapolación | Plausible; magnitud depende de la dosis de CBD, que en suplementos es mucho menor que la del medicamento (`206`) |
| **CBD/THC + warfarina** | Reportes de aumento del INR | **[reportes de caso]** | Señal, no prueba. Con un NTI, la prudencia gana |
| **THC + depresores del SNC** (alcohol, benzodiacepinas, opioides) | Sedación aditiva | **[clínico y farmacológico]** | Farmacodinámica pura, previsible (`205`) |
| **Hierba de San Juan + casi todo** | Inductor potente de CYP3A4 y P-gp: reduce anticonceptivos, ciclosporina, antirretrovirales; con ISRS, riesgo serotoninérgico | **[clínico, robusto]** — el ejemplo de libro | Contraindicación conocida y bien establecida |
| **Reishi (*Ganoderma*) + anticoagulantes/antiagregantes** | Actividad antiagregante plaquetaria descrita; algún reporte de caso de sangrado | **[in vitro] / [animal] + [reporte de caso]** — **no hay ensayo de interacción bien diseñado** | Precaución razonable, sobre todo perioperatoria; no es un hecho demostrado en humanos |
| **Cordyceps + inmunosupresores (ciclosporina, tacrolimus)** | Estudios en pacientes trasplantados exploraron *Cordyceps* como ahorrador de ciclosporina; también hay preocupación teórica opuesta por su efecto sobre parámetros inmunitarios | **[clínico, estudios pequeños y de calidad heterogénea]** + **[in vitro]** | Bandera amarilla en trasplantados: es exactamente la población donde no se improvisa |
| **β-glucanos / hongos inmunomoduladores + inmunosupresores** | Preocupación **teórica** por efecto opuesto | **[teórico / in vitro]** (`130`) | Se declara como precaución, no como hecho |
| **PSK / lentinano** | Son productos aprobados como **medicamento** en Japón, usados en ámbito hospitalario | **[clínico, en el marco de un fármaco]** | **No trasladable a un suplemento**: otro producto, otra dosis, otro marco legal (`231`, `233`) |
| **Chaga + función renal / anticoagulantes** | Alto contenido de oxalato; hay reporte de nefropatía por oxalato con consumo alto y prolongado | **[reporte de caso]** | Riesgo propio del chaga, con módulo aparte (`230`) |
| **Melena de león** | Muy pocos datos de interacción publicados | **[insuficiente]** | Decirlo así: "no hay datos suficientes" no es lo mismo que "es seguro" |
| **Ginkgo, ajo, ginseng + anticoagulantes** | Señal de aumento de sangrado, resultados mixtos en ensayos | **[clínico, mixto]** | Precaución perioperatoria estándar |
| **Psilocibina + litio** | Convulsiones y eventos serios reportados en series de casos | **[serie de casos]** | Combinación evitada en investigación clínica (`260`) |
| **Psilocibina + ISRS/IMAO** | Modificación de la respuesta y, con IMAO, preocupación serotoninérgica | **[clínico y farmacológico]** | Criterio de exclusión habitual en estudios (`259`, `260`) |

Cómo leer esta tabla sin exagerar: **la columna de evidencia es la que manda**. Poner "reishi y warfarina" al
mismo nivel que "hierba de San Juan y anticonceptivos" es tan deshonesto como negar el riesgo. Y ojo con la
dosis: casi toda la evidencia fuerte de CBD viene de dosis de medicamento (del orden de mg/kg/día), no de las
dosis de un suplemento (`206`, `208`).

## Cómo se comprueba una interacción (para saber qué le falta a la evidencia)

```
1. IN VITRO — microsomas hepáticos o hepatocitos humanos
   Se mide IC50 / Ki de inhibición sobre cada isoenzima (1A2, 2C9, 2C19, 2D6, 3A4) y la inducción
   vía receptores (PXR, CAR). Barato y rápido. NO prueba relevancia clínica por sí solo.

2. PREDICCIÓN — modelo PBPK
   Se estima la relación [I]/Ki con la concentración plasmática alcanzable en la vida real.
   Si la concentración que se logra con la dosis del suplemento está muy por debajo del Ki,
   la señal in vitro probablemente no se traduce a nada.

3. CLÍNICO — estudio de interacción con fármacos sonda (cocktail)
   Sondas típicas: cafeína (1A2), tolbutamida o flurbiprofeno (2C9), omeprazol (2C19),
   dextrometorfano (2D6), midazolam (3A4), digoxina (P-gp).
   Desenlace: cambio en AUC y Cmax del sonda. ESTE es el dato que decide (`121`).

4. FARMACOVIGILANCIA — reportes en uso real (`138`)
   Detecta lo que ningún estudio con 20 voluntarios sanos iba a ver.
```

Cuando alguien te diga "está demostrado que X interactúa con Y", la pregunta correcta es: *¿en qué escalón de
esa lista está el dato?* La mayoría de las afirmaciones que circulan sobre hongos están en el escalón 1.

## Ejemplo aplicado — la pregunta de un cliente real

Cliente de BIO-SETA: *"tengo 62 años, tomo warfarina hace tres años, ¿puedo tomar el extracto de reishi?"*.

Lo que **no** se responde: "sí, tranquilo, es natural" · "no, eso le puede causar una hemorragia" ·
cualquier frase que ajuste, sugiera o reemplace un tratamiento.

Respuesta correcta, en el tono de la marca:

> "Gracias por decírmelo, es justo lo que hay que preguntar. Le cuento lo que sabemos con honestidad: se ha
> descrito en estudios de laboratorio y en animales que el reishi puede afectar la agregación plaquetaria, y
> existen reportes aislados en personas; **no hay estudios clínicos buenos** que midan la interacción con
> warfarina. La warfarina es un medicamento de margen estrecho, donde cambios pequeños importan. Por eso, en
> su caso, la decisión la debe tomar su médico o su anticoagulóloga: llévele el nombre exacto del producto,
> la dosis por porción y el certificado de análisis —se los envío en PDF— y que ellos decidan. Si le dan luz
> verde, aquí estamos."

Por qué esta respuesta funciona: es honesta con el nivel de evidencia, no promete nada, no prohíbe nada, no
da consejo médico, entrega documentación técnica (que además te posiciona como marca seria) y deja la puerta
abierta. Es exactamente el estilo que `ventas_lushows` y `293` recomiendan para temas de salud.

Para el bot o el equipo comercial, la regla operativa se escribe así:

```
SI el cliente menciona: medicamento con receta · embarazo o lactancia · trasplante ·
   anticoagulante · inmunosupresor · litio, ISRS o IMAO · cirugía próxima · condición médica
ENTONCES: no se afirma seguridad, no se afirma peligro, se remite a profesional de salud
          y se ofrece la ficha técnica y el COA del lote.
```

## Errores comunes

- Decir "es natural, no interactúa". La hierba de San Juan es natural y es el inductor enzimático más famoso
  de la farmacología.
- Presentar una señal in vitro como un hecho clínico. Es el pecado más común de las fichas de proveedor.
- El error contrario: alarmar con "cuidado, interactúa con todo". Espanta clientes y no se sostiene.
- Extrapolar la dosis de medicamento a la de suplemento. El CBD de un ensayo clínico está a otro orden de
  magnitud que el de un gotero (`208`).
- No preguntar por la medicación concomitante cuando el cliente ya la mencionó. Es el dato más importante que
  te van a dar gratis.
- Dar instrucciones de "suspenda su medicamento" o "baje la dosis". Eso es ejercicio médico, y no es tu papel.
- No dejar registro. Si alguien reporta algo tras esa conversación, el registro es tu defensa (`138`).
- Poner en la etiqueta advertencias inventadas o, peor, omitir las que la norma sí exige (`272`).
- Olvidar que "no hay datos" ≠ "es seguro". La ausencia de estudios es ausencia de información (`12`, `03`).

## Conexión con otros módulos

→ `124-citocromo-p450-e-interacciones.md` — el módulo dueño del mecanismo enzimático.
→ `125-metabolismo-de-fase-ii.md` — conjugación y competencia por la eliminación.
→ `121-farmacocinetica-adme.md` — AUC, Cmax y por qué un cambio de concentración importa.
→ `206-farmacologia-del-cbd.md` y `205-farmacologia-del-thc.md` — el detalle de cannabis.
→ `209-seguridad-interacciones-y-contraindicaciones.md` — el listado operativo en cannabis.
→ `250-seguridad-e-interacciones-de-hongos.md` — el listado operativo en hongos.
→ `260-screening-de-seguridad-y-contraindicaciones.md` — cómo se hace el tamizaje en investigación clínica.
→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — el riesgo propio del chaga.
→ `12-niveles-de-evidencia.md` — la escala que sostiene toda la tabla de este módulo.
→ `293-como-comunicar-ciencia-sin-mentir.md` — cómo se dice todo esto sin prometer ni asustar.
