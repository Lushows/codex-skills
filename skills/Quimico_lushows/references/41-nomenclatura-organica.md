# 41 — Nomenclatura orgánica (hablar el idioma exacto del laboratorio)

Cuando le pides un análisis a un laboratorio o compras un patrón de referencia, el nombre que escribes es
un contrato. "THC" no es un nombre: hay Δ8, Δ9, Δ10, THCA-A, THCA-B, THCV, y dos enantiómeros de cada uno.
"Psilocibina" sí es un nombre único, pero "psilocina" y "psilocibina" se confunden todo el tiempo en
cotizaciones. Un nombre ambiguo te llega como un patrón equivocado de USD 300, un método que no separa lo
que te importa, o un COA que no dice lo que crees. Este módulo te enseña a nombrar sin ambigüedad y a
detectar cuándo el que te escribe no sabe de qué habla.

Términos: **IUPAC** = sistema formal de nomenclatura de la Unión Internacional de Química Pura y Aplicada.
**Nombre trivial (trivial/common name)** = nombre histórico, corto, sin reglas (limoneno, psilocibina).
**CAS RN (CAS Registry Number)** = identificador numérico único de una sustancia; el único que no miente.
**InChIKey** = huella de texto de 27 caracteres derivada de la estructura; ideal para buscar y comparar.
**SMILES** = forma de escribir la estructura en una línea de texto.

## Los cuatro niveles de identidad de una sustancia

| Nivel | Ejemplo (Δ9-THC) | ¿Ambiguo? | Cuándo usarlo |
|---|---|---|---|
| Trivial | THC | Sí, mucho | Nunca en un documento técnico |
| Semisistemático | Δ9-tetrahidrocannabinol | Poco | Conversación técnica |
| IUPAC completo | (6a*R*,10a*R*)-6,6,9-trimetil-3-pentil-6a,7,8,10a-tetrahidro-6*H*-benzo[c]cromen-1-ol | No | Especificación, expediente |
| CAS / InChIKey | CAS 1972-08-3 | No | Compra de patrón, COA, aduana |

**Regla dura del oficio:** en una orden de compra, una especificación o un COA, la sustancia va con **nombre
+ CAS**. Si el proveedor no te da CAS, no sabe qué te está vendiendo.

## Cómo se arma un nombre IUPAC (lo mínimo para leerlo)

```
[estereodescriptores]-[sustituyentes con localizadores]-[cadena o núcleo principal][insaturación][sufijo]
       (6aR,10aR)        6,6,9-trimetil-3-pentil-       benzo[c]cromen         -1-ol

Orden de lectura:
1. Encuentra el NÚCLEO (cadena más larga o sistema de anillos con el grupo principal).
2. El SUFIJO dice el grupo funcional de mayor prioridad (-ol, -ona, -oico, -amina).
3. Los LOCALIZADORES (números) dicen en qué carbono está cada cosa.
4. Los PREFIJOS listan los sustituyentes en orden alfabético (metil, pentil...).
5. Los ESTEREODESCRIPTORES (R/S, E/Z, cis/trans, D/L) van adelante, entre paréntesis (`43`).
```

Prioridad decreciente de grupos para el sufijo (memoriza este orden, resuelve el 90 % de los casos):

```
ácido carboxílico > éster > amida > aldehído > cetona > alcohol > amina > éter/alqueno/alcano
```

## El símbolo Δ: la trampa número uno del cannabis

**Δ (delta)** indica dónde está un doble enlace: `Δ9` = doble enlace entre C9 y C10. Δ8-THC y Δ9-THC tienen
**la misma fórmula molecular (C₂₁H₃₀O₂, masa monoisotópica 314,2246 Da)** y difieren solo en la posición de
ese doble enlace: son **isómeros de posición** (`42`). Consecuencias prácticas, no académicas:

- En MS de baja resolución dan **el mismo ion**: no se distinguen por masa, se distinguen por **tiempo de
  retención cromatográfica**. Un método que no los separe reporta uno por el otro.
- Existen dos sistemas de numeración históricos (monoterpenoide y pirano). El mismo compuesto es
  "Δ1-THC" en el sistema viejo y "Δ9-THC" en el actual. Si un paper de los años 70 dice Δ1, está hablando
  de lo que hoy llamamos Δ9. Verifica siempre el CAS.

| Nombre común | Otro nombre | CAS | Nota |
|---|---|---|---|
| Δ9-THC | Δ1-THC (nomenclatura vieja) | 1972-08-3 | El activo natural mayoritario |
| Δ8-THC | Δ6-THC (nomenclatura vieja) | 5957-75-5 | Isómero de posición, más estable |
| THCA-A | Ácido Δ9-tetrahidrocannabinólico A | 23978-85-0 | Forma ácida dominante en planta |
| CBN | Cannabinol | 521-35-7 | Producto de oxidación del THC (`47`) |
| CBD | Cannabidiol | 13956-29-1 | Estructura abierta, no pirano |

## Nomenclatura en hongos: lo que hay que escribir bien

| Compuesto | Nombre químico correcto | CAS | Error típico |
|---|---|---|---|
| Psilocibina | 4-fosforiloxi-*N*,*N*-dimetiltriptamina | 520-52-5 | Escribir "psilocybin" con y en español y confundirla con psilocina |
| Psilocina | 4-hidroxi-*N*,*N*-dimetiltriptamina | 520-53-6 | Pedir "psilocibina" y recibir psilocina |
| Baeocistina | 4-fosforiloxi-*N*-metiltriptamina | 21420-58-6 | Confundirla con norbaeocistina |
| Ergosterol | (22*E*)-ergosta-5,7,22-trien-3β-ol | 57-87-4 | Escribirlo "ergosterina" |
| Ergotioneína | 2-mercapto-L-histidina betaína | 497-30-3 | Confundir con ergosterol por parecido de nombre |
| Cordicepina | 3'-desoxiadenosina | 73-03-0 | Pedir "cordyceps extract" en vez del analito |

Para los β-glucanos **no hay un CAS útil**: son polímeros, no una sustancia única. Se especifican por
**tipo de enlace y fuente**: `β-(1→3),(1→6)-D-glucano de cuerpo fructífero de Ganoderma lucidum`. Ese detalle
es exactamente lo que separa el producto real del fraude (`52`, `218`).

## Nomenclatura biológica (que también te cobran caro)

El nombre de la especie va en cursiva, con género en mayúscula y epíteto en minúscula, y **con autoridad**
cuando es un documento formal: *Hericium erinaceus* (Bull.) Pers. Reglas de supervivencia:

- La especie **no es una fuente química suficiente**: hay que decir además el **órgano** (cuerpo fructífero,
  micelio) y el **sustrato** (`217`, `239`).
- Los sinónimos taxonómicos cambian: *Cordyceps sinensis* hoy es *Ophiocordyceps sinensis*, y casi todo lo
  que se vende como "cordyceps" es *Cordyceps militaris*, que es otra química (`227`).
- "Cannabis sativa L." cubre legalmente tanto cáñamo como marihuana en muchos marcos: la diferencia es
  química (contenido de THC total), no botánica (`170`).

## Cómo se comprueba que el nombre corresponde a la sustancia

1. Busca el **CAS** en la ficha del proveedor y contrástalo con PubChem/ChemSpider.
2. Compara el **InChIKey**: los primeros 14 caracteres son el esqueleto; los siguientes 10 codifican
   estereoquímica y protonación. Dos enantiómeros comparten el primer bloque y difieren en el segundo.
3. Pide el **certificado del patrón (CoA del estándar)**: pureza en % p/p, método (qNMR o HPLC), lote y
   fecha de vencimiento (`70`).
4. Verifica la **sal o forma**: "clorhidrato de X" pesa más que la base libre. Si compras 10 mg de clorhidrato
   y calculas como base libre, tu curva de calibración queda sesgada — el factor de corrección es la razón
   de masas molares (`04`, `06`).

## Ejemplo aplicado — una orden de compra que no se puede malinterpretar

```
SOLICITADO (ILUSTRATIVO):
  1. Δ9-tetrahidrocannabinol (Δ9-THC), CAS 1972-08-3, solución 1,0 mg/mL en metanol,
     1 mL, certificado con pureza por qNMR, trazable a material de referencia certificado.
  2. Ácido Δ9-tetrahidrocannabinólico A (THCA-A), CAS 23978-85-0, mismas condiciones.
  3. Cannabinol (CBN), CAS 521-35-7, mismas condiciones.
Requisito: los tres deben resolverse (Rs > 1,5) del Δ8-THC (CAS 5957-75-5) en el método propuesto.
```

Compara con lo que suele mandar la gente: *"cotícenme patrón de THC"*. Ese correo puede terminar en un
patrón de Δ8 y en un método que no separa isómeros.

## Errores comunes

- Escribir solo el nombre trivial en una especificación y descubrir en el COA que midieron otra cosa.
- Ignorar el estereodescriptor: sin `(−)-trans` el nombre "THC" cubre cuatro estereoisómeros (`43`).
- Pedir un patrón "de hongo" en vez del analito específico. Un extracto no es un patrón de referencia (`70`).
- Confundir sal con base libre en la preparación del estándar y sesgar toda la cuantificación.
- Usar sinónimos taxonómicos viejos en documentos de importación y que aduana no reconozca la especie (`285`).

## Conexión con otros módulos

→ `40-grupos-funcionales.md` — qué significa cada sufijo en términos de comportamiento.
→ `42-isomeria-y-estereoquimica.md` — por qué Δ8 y Δ9 son cosas distintas.
→ `70-patrones-de-referencia-y-trazabilidad.md` — cómo se compra un patrón sin equivocarse.
→ `103-identidad-por-adn-its-y-barcoding.md` — cuando el nombre de la especie hay que probarlo.
→ `180-delta8-delta10-e-isomerizacion.md` — el problema comercial completo de los isómeros.
