# 84 — HRMS (Q-TOF y Orbitrap): identificar lo que no sabías que estabas buscando

Hay dos preguntas distintas en análisis: *"¿cuánto hay de esto?"* y *"¿qué diablos es esto?"*. La primera la
responde LC-MS/MS con MRM (`83`), que solo ve lo que le pediste ver. La segunda la responde la
espectrometría de masas de alta resolución (HRMS), que pesa las moléculas con tantos decimales que puede
deducir su **fórmula molecular**. Es la técnica que se usa para cazar adulterantes, para explicar un pico
raro, para demostrar que un extracto tiene lo que dice, y —esto es lo valioso para un negocio— para
**volver a revisar la muestra meses después** buscando algo que en su momento nadie sospechaba.

Términos:
- **HRMS (high-resolution mass spectrometry)** = masas con resolución ≥ 20.000 y exactitud de pocas ppm.
- **Masa exacta / masa monoisotópica (exact mass, monoisotopic mass)** = masa calculada con los isótopos más
  abundantes, con 4+ decimales.
- **Error en ppm** = (masa medida − masa teórica) / masa teórica × 10⁶.
- **Q-TOF (quadrupole time-of-flight)** = cuadrupolo + tubo de vuelo; mide el tiempo que tarda un ion en
  recorrer una distancia.
- **Orbitrap** = trampa electrostática que mide la frecuencia de oscilación de los iones; resolución más
  alta, barrido más lento.
- **Análisis no dirigido (non-targeted / suspect screening)** = buscar sin lista previa, o contra una lista
  amplia de sospechosos.

## Por qué la masa exacta da la fórmula

```
Las masas atomicas exactas no son enteras:
   H = 1,007825   C = 12,000000   N = 14,003074
   O = 15,994915  P = 30,973762   S = 31,972071

Entonces dos moleculas con la MISMA masa nominal pesan distinto de verdad:

   C16H21NO2  ->  259,1572 Da
   C15H17N3O  ->  255,1372 Da
   C12H17N2O4P (psilocibina) -> 284,0926 Da

Con exactitud de 3 ppm a m/z 285, la ventana es +-0,00086 Da. Muy pocas
formulas caben ahi. Si ademas se usa la regla de las 7 reglas de oro (Kind &
Fiehn), el patron isotopico y el numero de insaturaciones, normalmente queda
UNA formula plausible.
```

Ese es el salto: pasar de *"hay algo de masa 285"* a *"es C12H17N2O4P, con error de 1,2 ppm y patrón
isotópico coherente"*. Todavía no es identidad definitiva —dos isómeros comparten fórmula— pero ya se puede
comparar con bases de datos y con patrones.

## Q-TOF vs Orbitrap

| | Q-TOF | Orbitrap |
|---|---|---|
| Resolución típica (FWHM) | 30.000–60.000 | 60.000–500.000 |
| Exactitud de masa | 1–5 ppm | < 3 ppm, típicamente < 1 ppm con lock mass |
| Velocidad de adquisición | Muy rápida (compatible con UHPLC de picos angostos) | Más lenta a alta resolución |
| Rango dinámico | Menor | Mayor |
| Costo (ILUSTRATIVO) | USD 450.000–700.000 | USD 600.000–1.200.000 |
| Fuerte en | Screening rápido, MS/MS de alta velocidad, metabolómica | Identificación fina, proteómica, mezclas complejas |

Para lo que te importa (adulterantes, perfiles de extracto, compuestos raros), **cualquiera de los dos
sirve**. La diferencia real no la hace el equipo sino la base de datos y el analista.

## Los cinco niveles de confianza en la identificación

Es la escala que usa la comunidad de análisis no dirigido (Schymanski et al., 2014) y la que deberías exigir
en cualquier informe que diga "identificamos":

| Nivel | Qué se tiene | Cómo se enuncia honestamente |
|---|---|---|
| **1 — Estructura confirmada** | Patrón de referencia corrido en el mismo método: masa, MS/MS y tR coinciden | "Es X" |
| **2 — Coincidencia probable** | MS/MS coincide con biblioteca o con literatura, sin patrón | "Muy probablemente X" |
| **3 — Candidato tentativo** | Se conoce la clase o hay varios candidatos | "Un compuesto de la familia Y" |
| **4 — Fórmula inequívoca** | Fórmula molecular asignada, estructura desconocida | "C22H33NO4, estructura no determinada" |
| **5 — Masa exacta** | Solo el m/z | "Señal a m/z 384,2537" |

Regla dura para leer informes: **si no corrieron el patrón de referencia, no es nivel 1**. Un informe que
dice "se identificó ergotioneína" sin patrón está en nivel 2 en el mejor de los casos, y hay que escribirlo
así (`03`).

## Para qué la contratarías tú (casos reales del sector)

| Situación | Qué aporta HRMS | Alternativa más barata |
|---|---|---|
| Pico desconocido en un extracto (`80`) | Fórmula molecular y clase de compuesto | Ninguna equivalente |
| Sospecha de adulteración con fármaco (sildenafilo en "potenciadores", esteroides, estimulantes) | Screening contra bases de miles de compuestos | LC-MS/MS dirigida si sospechas cuál |
| Cannabinoides semisintéticos raros (HHC, THCO, Δ10) sin patrón comercial | Detecta e identifica por fórmula y fragmentación | Nada; UV no distingue (`181`) |
| Comprobar que "extracto 10:1" tiene el perfil de la especie declarada | Huella química comparativa (`104`) | HPTLC (`96`) para huella barata |
| Verificar identidad de especie de hongo | Complementa, no reemplaza | **ITS por ADN es mejor y más barato** (`103`, `245`) |
| Revisar retrospectivamente muestras archivadas | Con DIA/all-ions, se busca hoy lo que no se buscaba ayer | Ninguna |

Esa penúltima fila importa: para saber **qué especie es**, el método correcto es secuenciación de la región
ITS del ADN, no masas. HRMS te dice qué moléculas hay, no de qué organismo vinieron.

## Ejemplo aplicado — screening de adulterantes en un "extracto de cordyceps"

```
Contexto: proveedor asiatico ofrece extracto de Cordyceps militaris con
"cordicepina 5 % p/p". La cordicepina real a ese nivel es cara y rara (228).
Sospecha razonable: adulteracion con adenosina (mas barata) o con un farmaco.

Plan (ILUSTRATIVO):
  1. HPLC-DAD para cuantificar cordicepina y adenosina .... COP 350.000
  2. HRMS Q-TOF, full scan + DDA, ESI +/-, screening contra
     base de adulterantes farmaceuticos y de productos naturales
     ................................................. COP 1.200.000-2.000.000
  3. Si aparece un candidato, confirmar con PATRON de referencia
     corrido en el mismo metodo (nivel 1) ............ COP 300.000-800.000

Hallazgo tipico del sector: la "cordicepina" declarada resulta ser
principalmente adenosina (masa exacta 267,0968 vs cordicepina 251,1018;
un cuadrupolo de baja resolucion las distingue por 16 Da, pero un metodo
UV mal desarrollado las puede coeluir y sumar — 80).

Decision de negocio: con nivel 1 en la mano, se rechaza el lote y se cobra
el analisis al proveedor segun el contrato (284, 292).
```

## Lo que HRMS NO hace

- **No cuantifica mejor que un triple cuadrupolo.** Para cuantificación de trazas, MRM sigue mandando (`83`).
- **No distingue isómeros por sí sola.** Δ8 y Δ9-THC tienen la misma fórmula y masa exacta idénticas; se
  separan por cromatografía (`81`) o por fragmentación cuidadosa e ion mobility.
- **No convierte un espectro en una estructura.** Para estructura definitiva de un compuesto nuevo hace falta
  RMN (`94`).
- **No sustituye la identidad biológica.** Especie = ADN (`103`).
- **No sirve sin base de datos y sin criterio.** El 70 % del valor está en la biblioteca y en el analista.

## Costo, tiempo y quién lo hace en Colombia

| Servicio | Costo (ILUSTRATIVO) | Tiempo |
|---|---|---|
| Screening no dirigido de adulterantes, 1 muestra | COP 1,2–2,5 millones | 2–4 semanas |
| Confirmación de identidad nivel 1 con patrón | COP 0,3–0,8 millones adicionales | 1–2 semanas |
| Perfil metabolómico comparativo (n=10 muestras) | COP 8–20 millones | 6–12 semanas |

A agosto de 2026, la capacidad de HRMS en Colombia está concentrada en universidades (grupos de
investigación con Q-TOF/Orbitrap) y en unos pocos laboratorios de servicio; muchos proyectos se envían a
Estados Unidos o Europa. Confirma antes de prometerle un plazo a un cliente, y ten en cuenta permisos de
exportación de muestras (`109`, `285`).

## Qué preguntarle al laboratorio

1. ¿Qué **nivel de confianza** (1–5) van a poder darme, y con qué patrón?
2. ¿Contra qué **base de datos** hacen el screening y cuántos compuestos tiene?
3. ¿Adquieren en **DDA o DIA**? ¿Guardan los datos crudos para reanálisis futuro?
4. ¿Cuál es el **error de masa** típico de su equipo y usan **lock mass**?
5. ¿Corren blanco de método y blanco de solvente? (En HRMS aparecen plastificantes y ftalatos por todas
   partes; sin blanco, "descubres" contaminantes de tu propio laboratorio.)
6. ¿El informe va a distinguir claramente entre **detectado**, **tentativo** y **confirmado**?

## Errores comunes

- **Leer "identificado" como "confirmado".** Sin patrón, no hay nivel 1.
- **Pedir HRMS cuando lo que necesitas es un ITS de ADN** (identidad de especie) o un Megazyme (β-glucanos).
- **Creer que resolución alta arregla mala cromatografía.** Los isómeros siguen sin separarse.
- **Interpretar el hallazgo de un ftalato o de un siloxano como adulteración**: suelen venir del vial, el
  septum o la manguera. Por eso el blanco.
- **No archivar los datos crudos.** El mayor valor de HRMS es poder volver a mirar.
- **Publicar un hallazgo de nivel 3 como si fuera un descubrimiento.** Cuesta reputación (`03`, `293`).

## Conexión con otros módulos

→ `82-espectrometria-de-masas-fundamentos.md` — fuentes, aductos y resolución.
→ `83-lc-ms-ms-y-mrm.md` — la técnica hermana, para cuantificar.
→ `94-rmn-fundamentos.md` y `95-qnmr-cuantificacion-absoluta.md` — cuando hace falta estructura o pureza absoluta.
→ `103-identidad-por-adn-its-y-barcoding.md` y `245-identidad-de-especie-por-its.md` — identidad biológica.
→ `104-metabolomica-y-huella-quimica.md` — comparar materiales completos.
→ `181-hhc-thco-y-semisinteticos.md` y `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — los fraudes que esto destapa.
→ `284-auditoria-de-proveedor.md` — cómo se usa el hallazgo en la relación comercial.
