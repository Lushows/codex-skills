# 44 — Mecanismos de reacción básicos (predecir qué le va a pasar a tu producto)

Un mecanismo es la película de cómo se rompen y se forman los enlaces, paso a paso. No es teoría de examen:
es la herramienta que te deja **predecir** que un aceite de CBD guardado con trazas de ácido se va a
isomerizar a Δ8, que un extracto con fenoles se va a poner pardo, que la psilocibina se va a defosforilar,
o que un éster de tu formulación se va a hidrolizar y cambiar el olor. Quien entiende cuatro o cinco
mecanismos puede diseñar el envase, el pH y la temperatura de almacenamiento sin esperar 12 meses del
estudio de estabilidad para enterarse.

Términos: **nucleófilo (nucleophile)** = especie rica en electrones que ataca; **electrófilo (electrophile)** =
pobre en electrones, recibe el ataque. **Intermediario (intermediate)** = especie real y aislable en
principio, con vida finita. **Estado de transición (transition state)** = el punto más alto de energía del
camino; no se aísla. **Catálisis ácida/básica (acid/base catalysis)** = el ácido o la base acelera sin
consumirse.

## La regla que resume el 80 %

```
Los electrones van de donde SOBRAN a donde FALTAN.

Sobran electrones (nucleófilos):  OH⁻, H₂O, NH₃/aminas, enolatos, dobles enlaces C=C, fenolatos
Faltan electrones (electrófilos): C del C=O, C unido a buen grupo saliente, H⁺, carbocationes, O₂/radicales
```

Casi toda degradación de producto natural es una de estas cinco películas.

## Los cinco mecanismos que tienes que reconocer

| Mecanismo | Qué pasa | Qué lo acelera | Dónde te lo encuentras |
|---|---|---|---|
| **Sustitución nucleofílica (SN1/SN2)** | Un grupo sale, otro entra | SN1: carbocationes estables, medio polar prótico; SN2: nucleófilo fuerte, sin estorbo | Hidrólisis de ésteres de fosfato; alquilaciones |
| **Adición-eliminación al carbonilo** | El nucleófilo se pega al C=O y luego sale un grupo | Ácido o base, agua, calor | Hidrólisis de ésteres y amidas (`46`) |
| **Eliminación (E1/E2)** | Se forma un doble enlace | Calor, base, ácido (E1) | Deshidratación de alcoholes; isomerizaciones |
| **Adición electrofílica a C=C** | Un electrófilo (H⁺) ataca el doble enlace y forma carbocatión | Ácido, calor | **Isomerización CBD → Δ8/Δ9-THC** (`180`) |
| **Radicalario / oxidación** | Cadena de radicales, con O₂ | Luz UV, metales de transición, calor | **THC → CBN**, rancidez, pardeamiento (`47`) |

## Mecanismo 1 — Adición electrofílica: el que explica el mercado del Δ8

Este es el que hay que saber de memoria si trabajas cannabis.

```
CBD (dos fenoles + un doble enlace terpénico libre)
   ├─ H⁺ (ácido de Lewis o de Brønsted) ataca el doble enlace del anillo terpénico
   ├─ se forma un CARBOCATIÓN terciario (intermediario)
   ├─ un fenol de la misma molécula ataca ese carbocatión → CICLACIÓN → anillo pirano
   └─ pérdida de H⁺ → doble enlace en la posición más estable

Producto termodinámico:  Δ8-THC  (alqueno más sustituido, MÁS ESTABLE)
Producto cinético:       Δ9-THC  (se forma primero, se isomeriza a Δ8 si sigue el ácido/calor)
Subproductos:            iso-THC, Δ4(8)-iso-THC, olivetol, dímeros, clorados si se usó HCl
```

Tres consecuencias de negocio que caen directo de este mecanismo:

1. Por eso el Δ8 comercial casi siempre viene de CBD y no de la planta.
2. Por eso un aceite de CBD con residuo ácido y guardado caliente **se convierte solo** en Δ8/Δ9 con el
   tiempo: puede volverse no conforme sin que nadie haga nada (`204`).
3. Por eso hay que pedir análisis de **subproductos de reacción**, no solo del isómero objetivo: los
   subproductos no tienen datos toxicológicos y casi ningún COA los busca (`180`, `111`).

## Mecanismo 2 — Adición-eliminación al carbonilo: hidrólisis

```
Éster + H₂O  ⇄  ácido + alcohol
  Catálisis ácida:  reversible, hay que desplazar el equilibrio (exceso de agua o quitar producto)
  Catálisis básica: IRREVERSIBLE (el carboxilato formado ya no reacciona) → saponificación (`46`)

Velocidad: v = k[éster][H₂O]  y k depende de pH → curva en "U": mínimo a un pH de máxima estabilidad
```

Ese "pH de máxima estabilidad" es un dato que se busca en el desarrollo de formulación, no se adivina: se
hace un estudio de estabilidad forzada a varios pH y se elige el valle (`164`, `165`).

## Mecanismo 3 — Radicales y oxidación: el que se come tus activos

```
Iniciación:   R-H + (luz UV, calor, Fe²⁺/Cu²⁺)  →  R• + H•
Propagación:  R• + O₂ → ROO•        ROO• + R'-H → ROOH + R'•     ← se AUTOALIMENTA
Terminación:  R• + R• → R-R         o antioxidante: ROO• + AH → ROOH + A•

Puntos débiles preferidos: H alílico (junto a C=C), H bencílico, fenoles, dobles enlaces de poliinsaturados
```

Por eso: envase opaco, cabeza de aire mínima o nitrógeno, quelante de metales (EDTA o ácido cítrico) y
antioxidante. No son adornos de formulación: cada uno corta un paso del mecanismo (`61`, `133`).

## Mecanismo 4 — Descarboxilación: no es hidrólisis, es térmica

El THCA pierde CO₂ por un mecanismo intramolecular (estado de transición cíclico de seis miembros, ayudado
por el fenol vecino). No hace falta ácido ni base añadidos: solo calor.

```
THCA  --Δ-->  Δ9-THC + CO₂         (misma lógica para CBDA → CBD)
Cinética aproximadamente de primer orden: ln([THCA]t/[THCA]0) = −k·t
k depende de T por Arrhenius: k = A·exp(−Ea/RT)
→ Calcular tiempo y temperatura con `lab-tools/decarboxilacion.py`, nunca a ojo (`174`).
```

## Mecanismo 5 — Enzimático: catálisis biológica

En hongos y plantas, muchas transformaciones son enzimáticas. Lo relevante para producto:

- **Fosfatasas** desfosforilan la psilocibina a psilocina; ocurre en el organismo y también en el material
  mal secado, donde las enzimas del propio hongo siguen activas (`251`, `255`).
- **Polifenol oxidasa (PPO)** oxida fenoles a quinonas: es el pardeamiento enzimático del hongo cortado
  (`62`).
- **THCA sintasa** es una oxidociclasa dependiente de FAD; su estereoespecificidad explica el (−)-trans (`43`, `172`).

Cortar la vía es simple y se llama **blanqueado/inactivación térmica o secado rápido**: la enzima es una
proteína, se desnaturaliza (`142`, `240`).

## Cómo se comprueba qué mecanismo está actuando

1. **Estabilidad forzada (forced degradation, ICH Q1A/Q1B):** somete la muestra por separado a ácido, base,
   oxidante (H₂O₂), calor seco y luz UV. Cada estrés genera un perfil de degradación distinto.
2. **Perfil de picos nuevos en HPLC-DAD:** si aparece un pico con el espectro UV del CBN, es oxidación; si
   aparece a un tiempo de retención de Δ8, es isomerización ácida.
3. **Cinética:** mide a 3–5 tiempos y ajusta orden 0, 1 y 2. El orden que linealiza te dice el tipo de
   proceso (`26`).
4. **Balance de masa:** lo que se pierde del activo debe aparecer como degradantes. Si no aparece, hay
   pérdida física (adsorción, volatilización) y no química (`06`).

## Ejemplo aplicado — decidir el envase de una tintura de melena de león

```
Formulación (ILUSTRATIVO): tintura hidroalcohólica 40 % v/v etanol, pH medido 4,8, con
  fenoles del extracto y ésteres del vehículo.
Riesgos por mecanismo:
  Radicalario/oxidación → fenoles + O₂ + luz → color pardo, pérdida de aroma.
     Control: vidrio ámbar, llenado al tope, cierre hermético, ácido ascórbico 0,05 % p/v.
  Hidrólisis de ésteres → pH 4,8 está cerca del mínimo de la curva en U para muchos ésteres.
     Control: no bajar más el pH; verificar con estabilidad forzada.
  Enzimático → ya inactivado por el etanol y el secado previo. Riesgo bajo.
Plan: estabilidad acelerada 40 °C / 75 % HR, 6 meses, con seguimiento de color (L*a*b*),
  fenoles totales y perfil HPLC (`164`, `165`). Nada de esto se declara hasta tener el dato.
```

## Errores comunes

- Llamar "hidrólisis" a la descarboxilación del THCA. Son mecanismos distintos y se controlan distinto.
- Añadir un antioxidante sin quelante cuando el problema real es el hierro del agua: no corta la iniciación.
- Ajustar el pH "porque suena estable" sin hacer el perfil pH-estabilidad. El valle se mide.
- Pensar que un producto seco no se degrada. La fotooxidación y la oxidación por O₂ no necesitan agua (`35`).
- Buscar solo el analito principal en estabilidad. Los degradantes son los que cuentan la historia y los que
  pregunta el regulador (`164`).

## Conexión con otros módulos

→ `26-cinetica-de-reaccion.md` — órdenes de reacción y constantes.
→ `45-reacciones-de-sintesis-frecuentes.md` — las mismas películas, usadas a propósito.
→ `47-oxidacion-y-degradacion-de-productos-naturales.md` — el mecanismo radicalario en detalle.
→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — cómo se traduce a envase y almacenamiento.
→ `174-descarboxilacion-cinetica-y-calculo.md` — el cálculo completo con herramienta.