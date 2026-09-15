# 94 — RMN, fundamentos (la técnica que sí dice "esta molécula es esta")

La resonancia magnética nuclear (RMN) es la única técnica de rutina que te da la **estructura** de una
molécula, átomo por átomo, sin destruirla. Cromatografía te dice "salió a 7,2 minutos"; masas te dice "pesa
314 Da"; RMN te dice "es este esqueleto, con este sustituyente en esta posición". Para quien desarrolla un
producto natural, RMN es la técnica que cierra discusiones: confirma la identidad de un estándar, revela un
adulterante que nadie estaba buscando y —en su versión cuantitativa— entrega pureza sin necesidad de un
patrón del mismo compuesto (ver `95-qnmr-cuantificacion-absoluta.md`).

Términos: **RMN (NMR, Nuclear Magnetic Resonance)** = espectroscopía basada en el espín de núcleos como ¹H,
¹³C, ³¹P, ¹⁹F en un campo magnético. **desplazamiento químico (chemical shift, δ)** = posición de la señal
en ppm; depende del entorno electrónico. **integral (integral)** = área de la señal, proporcional al número
de núcleos. **acoplamiento (coupling, J)** = cómo se parten las señales por los vecinos, en Hz.
**deuterado (deuterated solvent)** = solvente con D en vez de H (CDCl₃, DMSO-d₆, D₂O) para no tapar la
muestra.

## Qué se lee en un espectro de ¹H

Cuatro datos por señal, y cada uno cuenta algo distinto:

| Dato | Qué te dice | Ejemplo |
|---|---|---|
| **δ (ppm)** | Entorno químico | CH₃ alifático ~0,9; olefínico 5–6; aromático 6,5–8; aldehído ~9,8 |
| **Integral** | Cuántos H hay | Integral 3 = un metilo |
| **Multiplicidad** | Cuántos vecinos | Regla n+1: un triplete tiene 2 vecinos |
| **J (Hz)** | Geometría y distancia | J trans ~15 Hz vs J cis ~10 Hz en un doble enlace |

En ¹³C la escala llega a ~220 ppm y normalmente se corre desacoplado: una línea por carbono químicamente
distinto. Cuenta carbonos, no protones.

## Los experimentos que de verdad se piden

| Experimento | Para qué sirve |
|---|---|
| ¹H 1D | Todo: pureza aparente, identidad rápida, solventes residuales |
| ¹³C / DEPT-135 | Contar carbonos y clasificar CH₃ / CH₂ / CH / cuaternario |
| **COSY** | Qué H está acoplado con qué H (conectividad H-H) |
| **HSQC** | Qué H está pegado a qué C (un enlace) |
| **HMBC** | Qué H "ve" a qué C a 2–3 enlaces: **arma el esqueleto** |
| **NOESY / ROESY** | Cercanía en el espacio: estereoquímica relativa |
| DOSY | Separa por tamaño; útil en mezclas |

Para una estructura nueva no negocies: **¹H + ¹³C + COSY + HSQC + HMBC**, y NOESY si hay estereoquímica.
Con menos que eso, la asignación es una hipótesis, no una estructura.

## Campo, sensibilidad y cuánta muestra hace falta

El "tamaño" del equipo se dice en MHz de la frecuencia de ¹H: 300, 400, 600, 800 MHz. Más campo = mejor
dispersión de señales y mejor sensibilidad. Órdenes de magnitud prácticos (ILUSTRATIVO, dependen de equipo,
sonda y compuesto):

```
1H 1D, 400 MHz, sonda estandar : 1-5 mg de muestra, minutos
13C 1D, 400 MHz                : 10-30 mg, 30 min a varias horas (13C es 1,1 % natural)
HSQC/HMBC, 400-600 MHz         : 3-10 mg, 1-12 h
Criosonda (cryoprobe)          : baja los requisitos ~4x, y el precio por hora sube
```

RMN es **poco sensible** comparada con masas: se mide en miligramos, no en nanogramos. Por eso no es técnica
de trazas ni de contaminantes; es técnica de estructura y de componentes mayoritarios.

## Cómo se comprueba que el espectro es confiable

- **Referencia interna** correcta: TMS a 0,00 ppm, o la señal residual del solvente (CDCl₃ 7,26; DMSO-d₆
  2,50; D₂O 4,79 aproximadamente).
- **Shimming y forma de línea**: picos anchos o asimétricos = campo mal ajustado, integrales no confiables.
- **Tiempo de relajación**: para integrar bien hace falta esperar suficiente entre pulsos (d1 ≥ 5·T1). Este
  punto es negociable en un ¹H de identidad y **no negociable** en qNMR (ver `95`).
- **Relación señal-ruido** declarada y suficiente para lo que vas a afirmar.
- **Los datos crudos (FID)**: pide siempre los archivos, no solo el PDF. Un espectro sin FID no es auditable.

## Ejemplo aplicado (ILUSTRATIVO)

Un proveedor vende "aislado de CBD 99 %". Llega el material y se corre ¹H en CDCl₃, 400 MHz.

```
Senales esperadas de CBD : 6,20-6,25 (2H, aromaticos); 5,55 (1H); 4,55 y 4,65 (2H, =CH2);
                           1,79 (3H, CH3 vinilico); 0,88 (3H, t, CH3 del pentilo)
Hallazgo adicional       : singulete a 2,10 ppm, integral equivalente a ~2 % molar
Interpretacion           : posible acetona o acetato residual -> confirmar con GC headspace (86, 87)
Segundo hallazgo         : sistema aromatico extra a 6,3-6,4 no asignable a CBD
Accion                   : HMBC + LC-HRMS para identificar; sospecha de CBDV o de un isomero
```

El COA decía "99,2 % por HPLC-UV". HPLC-UV mide **área relativa a 220 nm**, no masa: si el acompañante
absorbe parecido, el 99,2 % puede ser real como área y falso como pureza másica. Ahí es donde entra qNMR.
(Cifras ilustrativas.)

## Errores comunes

- **Confundir "pureza por HPLC-UV" con pureza másica.** Son cosas distintas; ver `95` y `80`.
- **Integrar sin haber esperado la relajación.** Las integrales quedan sesgadas y nadie lo ve en el PDF.
- **Agua en el solvente deuterado** tapando señales entre 1,5 y 3,3 ppm según el solvente.
- **Asignar estructura solo con ¹H.** Sin HMBC no tienes conectividad: tienes una corazonada.
- **Pedir RMN para buscar trazas.** Para 10 ppm de un pesticida, RMN no es la técnica.
- **Quedarse con el PDF.** Sin FID no puedes reprocesar, ni verificar, ni impugnar (ver `112`).

## Conexión con otros módulos

→ `95-qnmr-cuantificacion-absoluta.md` — la versión cuantitativa: pureza sin patrón del mismo compuesto.
→ `82-espectrometria-de-masas-fundamentos.md` y `84-hrms-qtof-orbitrap-e-identificacion.md` — la otra mitad
   de la identificación estructural.
→ `70-patrones-de-referencia-y-trazabilidad.md` — por qué la pureza del patrón define todo lo demás.
→ `224-triterpenos-ganodericos-analisis.md` — donde RMN resuelve isómeros que la cromatografía no separa.
→ `104-metabolomica-y-huella-quimica.md` — RMN como huella de autenticidad de un material.