# 43 — Quiralidad y enantiómeros (por qué el activo es el (−)-trans-Δ9-THC y no "el THC")

La quiralidad es la propiedad de una molécula de no ser superponible con su imagen en el espejo, como tu mano
izquierda y la derecha. Tiene una consecuencia que decide productos: el cuerpo es quiral —los receptores y
las enzimas son proteínas quirales— así que **un enantiómero puede ser activo y su imagen especular casi
inerte**. En cannabis, el compuesto natural y activo es el **(−)-trans-Δ9-THC**; su enantiómero
(+)-trans es mucho menos potente en el receptor CB1 [in vitro / animal]. Si compras un "THC sintético" o un
semisintético barato, puedes estar comprando una mezcla racémica: la mitad de tu masa no hace nada, pero sí
cuenta para el límite legal.

Términos: **quiral (chiral)** = no superponible con su imagen especular. **Centro estereogénico (stereocenter)**
= carbono con cuatro sustituyentes distintos. **Enantiómeros (enantiomers)** = par de imágenes especulares.
**Racemato (racemate)** = mezcla 50:50 de ambos enantiómeros; no desvía la luz polarizada. **Exceso
enantiomérico ee (enantiomeric excess)** = qué tanto predomina uno sobre el otro, en %.
**Diastereómero (diastereomer)** = estereoisómero que NO es imagen especular; tiene propiedades físicas
distintas y por eso se separa en columna normal.

## Las dos notaciones que se confunden todo el tiempo

| Notación | Qué describe | Se determina por | Ejemplo |
|---|---|---|---|
| *R* / *S* (Cahn-Ingold-Prelog) | Configuración **absoluta** de cada centro | Estructura (rayos X, RMN, síntesis) | (6a*R*,10a*R*)-Δ9-THC |
| (+) / (−) o *d* / *l* | Sentido en que **desvía la luz** polarizada | Medición: polarímetro | (−)-Δ9-THC |
| *D* / *L* | Convención histórica (azúcares, aminoácidos) | Comparación con gliceraldehído | D-glucosa, L-alanina |

**No hay relación automática entre R/S y (+)/(−).** Una molécula *R* puede ser (+) o (−); hay que medirlo.
Es el error conceptual más repetido en documentos técnicos mal escritos.

## El caso central: (−)-trans-Δ9-THC

El Δ9-THC tiene **dos centros estereogénicos**, C6a y C10a, y por tanto 2² = 4 estereoisómeros posibles:
dos pares de enantiómeros (uno *trans* y uno *cis*).

```
Δ9-THC — los cuatro estereoisómeros
  (6aR,10aR)-trans   → (−)-trans-Δ9-THC  ← EL NATURAL Y EL ACTIVO. Dronabinol.
  (6aS,10aS)-trans   → (+)-trans-Δ9-THC     enantiómero; potencia en CB1 mucho menor [in vitro]
  (6aR,10aS)-cis     → cis-Δ9-THC           diastereómero, minoritario, otra actividad
  (6aS,10aR)-cis     → enantiómero del anterior

Relación entre los pares:
  trans-(R,R)  vs  trans-(S,S)   → ENANTIÓMEROS  → mismas propiedades físicas → NO se separan en C18
  trans-(R,R)  vs  cis-(R,S)     → DIASTERÓMEROS → propiedades distintas      → SÍ se separan en C18
```

Por qué esto importa comercialmente:

1. **La planta hace solo el (−)-trans.** La enzima THCA sintasa es estereoespecífica (`172`). Un cannabinoide
   de origen vegetal, si el análisis de identidad es correcto, viene enantiopuro.
2. **La química de laboratorio no.** Una síntesis o una isomerización no controlada puede dar racemato o
   mezclas. Los semisintéticos tipo HHC son el ejemplo canónico: el HHC se produce como mezcla de epímeros
   9*R* y 9*S* con potencias distintas (`181`).
3. **La ley cuenta masa, no actividad.** Los límites de THC total (`175`) se expresan en % p/p sin distinguir
   enantiómero. Un producto puede tener la mitad de su THC inactivo y aun así ser ilegal.
4. **El dronabinol** —el (−)-trans-Δ9-THC como principio activo farmacéutico— se especifica con su
   estereoquímica explícita en la monografía. Escribir solo "THC" en un expediente es insuficiente (`286`).

## Quiralidad en hongos

- **Psilocibina y psilocina no son quirales**: no tienen centro estereogénico. Eso simplifica su análisis
  —no hace falta columna quiral— y elimina toda discusión de enantiopureza (`251`).
- **Los azúcares sí.** La glucosa de los glucanos es **D-glucosa**, y los enlaces son **β**. Ese "β" es
  estereoquímica del carbono anomérico C1 y es exactamente lo que decide que una enzima humana o de
  levadura pueda o no cortar el polímero. El α-glucano (almidón) tiene el otro anómero y por eso se digiere
  distinto (`52`, `220`).
- **Los aminoácidos** de las proteínas fúngicas son **L**. Detectar D-aminoácidos en un hidrolizado sugiere
  racemización por proceso térmico agresivo o adulteración (`54`).
- **Ergotioneína** se presenta como **L-ergotioneína**; el transportador OCTN1 es estereoselectivo [in vitro] (`235`).

## Cómo se mide la quiralidad

| Objetivo | Técnica | Unidad / criterio | Costo relativo |
|---|---|---|---|
| ¿Es racemato o enantiopuro? | Polarimetría (rotación específica [α]D) | grados·mL/(g·dm), con λ, T, solvente, c | Bajo |
| Cuantificar ee | **HPLC quiral** (fase de amilosa/celulosa) | ee (%) = (mayor − menor)/(mayor + menor) × 100 | Medio |
| Cuantificar ee volátiles | GC quiral (ciclodextrina) | Igual | Medio |
| Configuración absoluta | Difracción de rayos X de monocristal | Asignación *R*/*S* inequívoca | Alto |
| Confirmación por espectro | Dicroísmo circular (CD/ECD) o VCD | Comparación con calculado | Alto |

```
Cálculo del exceso enantiomérico a partir de áreas de HPLC quiral (ILUSTRATIVO):
  A(−) = 982 341    A(+) = 17 659    (misma respuesta del detector, factor 1:1)
  ee = (982341 − 17659) / (982341 + 17659) × 100 = 96,47 %
  Interpretación: 98,23 % del enantiómero (−) y 1,77 % del (+).
  → Verificar la cuenta con `Matematicas_lushows` o `lab-tools/`; no confiar en la aritmética mental.
```

Advertencia dura: **una columna C18 normal NO separa enantiómeros**. Si el COA no dice "columna quiral",
no hay dato de enantiopureza, punto. Y el polarímetro solo te dice si hay desviación neta: un racemato da 0°
y también da 0° una muestra donde no hay nada.

## Ejemplo aplicado — comprar destilado y no comprar la mitad de aire

Un proveedor ofrece "destilado de Δ9-THC 92 %" a mitad de precio del mercado (ILUSTRATIVO).

```
Lo que dice el COA         : Δ9-THC 92,1 % p/p por HPLC-DAD, columna C18.
Lo que NO dice             : nada de enantiopureza ni de origen (extraído vs sintetizado/isomerizado).
Pregunta clave             : ¿[α]D del material? ¿ee por HPLC quiral?
Escenario A (natural)      : ee > 99 % → 92,1 % de THC activo.
Escenario B (racémico)     : ee ~ 0 %  → ~46 % activo, ~46 % enantiómero de baja potencia,
                             pero 92,1 % contando para el límite legal de THC total.
Diferencia de valor real   : ~2x en activo por peso, con el mismo riesgo regulatorio.
```

La prueba cuesta una fracción del lote. No pedirla es regalar el margen.

## Errores comunes

- Escribir "THC" en una especificación sin el descriptor `(−)-trans` ni el CAS: el documento no define la
  sustancia (`41`).
- Suponer que R = (+). No hay tal correspondencia; se mide.
- Pedir "análisis quiral" sin especificar la columna y el patrón del enantiómero minoritario: sin ese patrón
  no se puede reportar ee con trazabilidad (`70`).
- Confundir enantiómeros con diastereómeros y pedir columna quiral cuando bastaba una C18 (o al revés,
  gastar en C18 esperando separar enantiómeros).
- Aplicar la lógica de quiralidad a psilocibina: no es quiral, ese gasto no aplica.
- Olvidar que un proceso térmico o ácido puede **racemizar o epimerizar** un centro con el tiempo: la
  enantiopureza es un atributo de estabilidad, no solo de fabricación (`61`).

## Conexión con otros módulos

→ `42-isomeria-y-estereoquimica.md` — el mapa completo de tipos de isomería.
→ `181-hhc-thco-y-semisinteticos.md` — epímeros 9R/9S y el problema de los semisintéticos.
→ `205-farmacologia-del-thc.md` — por qué el receptor distingue enantiómeros.
→ `70-patrones-de-referencia-y-trazabilidad.md` — patrones enantiopuros y su certificado.
→ `52-polisacaridos-y-glucanos.md` — el anómero α/β y por qué decide todo en hongos.