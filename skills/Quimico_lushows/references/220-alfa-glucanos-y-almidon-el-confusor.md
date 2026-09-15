# 220 — Alfa-glucanos y almidón: el confusor (la molécula que hace posible el fraude)

El α-glucano es el personaje que nadie menciona en el marketing y que decide todo. Es la familia donde vive
el almidón, y como también está hecho de glucosa, cualquier método que solo mida "azúcares totales" lo
cuenta como si fuera activo. Ese es el mecanismo químico exacto por el cual el arroz molido puede venderse
como extracto de hongo con "30 % de polisacáridos". Si entiendes este módulo, entiendes por qué el par
β/α es la única lectura que sirve.

Términos: **α-glucano (alpha-glucan)** = polímero de glucosa con enlaces α; incluye almidón y glucógeno.
**amilosa (amylose)** = fracción lineal α-(1→4) del almidón. **amilopectina (amylopectin)** = fracción
ramificada α-(1→4) con puntos α-(1→6). **glucógeno (glycogen)** = reserva de glucosa; en hongos existe, en
poca cantidad. **amiloglucosidasa (amyloglucosidase, AMG)** = enzima que corta α-glucanos hasta glucosa.

## Qué α-glucanos aparecen en un producto de hongos

| α-glucano | De dónde viene | Cuánto esperar |
|---|---|---|
| Almidón de arroz/avena | Sustrato de cultivo residual | Alto si es micelio en grano |
| Glucógeno fúngico | Reserva propia del hongo | Bajo |
| Maltodextrina | Excipiente/soporte de secado por aspersión | Depende de la formulación; **declárala** |
| Almidón añadido | Carga barata deliberada | Es adulteración (ver `246`) |

Ojo con la maltodextrina: no es fraude si está declarada como soporte de secado, pero **sube el α-glucano**
y puede confundir la lectura. Cuando audites un COA, pregunta primero por la formulación antes de acusar.

## Cifras de referencia

De la literatura de la industria (Nammex, *Redefining Medicinal Mushrooms*, nammex.com; recogido por
NutraIngredients, marzo de 2017), medido con Megazyme K-YBGL más el ensayo de almidón AOAC en paralelo:

- Cuerpo fructífero auténtico: **almidón ~1–5 % p/p base seca**.
- Micelio sobre grano: **α-glucano 30–60 % p/p base seca**, con casos de 66–72 %, y β-glucano 1–3 %.

De literatura académica, para calibrar lo que es normal en una seta: en sombrero de *Lentinula edodes* se
reporta glucano total ~20,5 g/100 g base seca, del cual ~96,3 % es β-glucano (19,8 g/100 g) y solo ~3,7 %
es α-glucano (0,7 g/100 g) (estudio de aislamiento y comparación de α- y β-D-glucanos de shiitake,
*Carbohydrate Polymers*, 2020). Esa proporción —β dominante, α marginal— es la firma del hongo real.

## Por qué el método enzimático puede separarlos

Porque hay enzimas específicas para cada configuración. El kit Megazyme K-YBGL aprovecha exactamente eso:

```
GLUCANO TOTAL  = hidrolisis acida controlada (H2SO4) de TODO glucano -> glucosa
                 medida con glucosa oxidasa/peroxidasa (GOPOD)

ALFA-GLUCANO   = hidrolisis ENZIMATICA especifica (amiloglucosidasa + invertasa)
                 que solo ataca almidon/glucogeno y sacarosa -> glucosa
                 medida con el mismo GOPOD

BETA-GLUCANO   = GLUCANO TOTAL  -  ALFA-GLUCANO
```

La química es honesta porque el ácido no discrimina (rompe todo) y la enzima sí (solo α). La resta es la
que da el β. Ese es el fundamento de la determinación "por diferencia" descrita en *Journal of AOAC
International* para hongos y productos miceliales (McCleary y Draga, 2016) y documentada por Megazyme para
el kit K-YBGL (megazyme.com, documentación K-YBGL). El detalle operativo está en `221`.

## Cómo se mide / cómo se comprueba

| Objetivo | Método | Unidad |
|---|---|---|
| α-glucano en el mismo ensayo del β | Megazyme K-YBGL, rama enzimática | `% p/p base seca` |
| Almidón como tal, confirmación independiente | Método de almidón total AOAC (amilasa termoestable + AMG) | `% p/p base seca` |
| Identificar el grano de origen | Microscopía de gránulos de almidón; ADN de la planta | Cualitativo |
| Maltodextrina añadida | Perfil de dextrosa equivalente / HPAEC-PAD | `% p/p` |

Un dato útil: los gránulos de almidón de arroz son poliédricos y muy pequeños (aprox. 3–8 µm) y se ven al
microscopio con tinción de yodo. No es cuantitativo, pero en 20 minutos te dice si hay grano. Sirve como
tamiz rápido antes de pagar un ensayo (ver `67`).

## Ejemplo aplicado — el cálculo de "cuánto arroz estoy comprando"

**(ILUSTRATIVO)** Un polvo con α-glucano 44,9 % p/p base seca. Si el arroz integral tiene del orden de
70–75 % de almidón en base seca, una estimación gruesa del contenido de grano es:

```
fraccion de grano ~= 44,9 / 72  =  0,62   ->  ~62 % del polvo seria arroz
```

Es una estimación, no una medida: asume que todo el α-glucano viene del arroz e ignora el glucógeno fúngico
y cualquier maltodextrina. Sirve para la conversación con el proveedor, no para el expediente. Y hazla en
código (`Matematicas_lushows`), no de memoria.

## Qué se puede y qué no se puede afirmar

- Puedes afirmar: "α-glucano 3,1 % p/p base seca (Megazyme K-YBGL)" — es un dato medido.
- Puedes afirmar que un α-glucano alto es **inconsistente** con cuerpo fructífero puro.
- No puedes afirmar que el almidón "no sirve para nada": sí es alimento; lo que no es, es β-glucano fúngico.
- No conviertas el hallazgo en un ataque público sin segunda medición y sin cadena de custodia (ver `109`,
  `112`).

## Errores comunes

- Pedir solo β-glucano y no pedir α-glucano. Sin el α no tienes la historia completa ni la señal de fraude.
- Olvidar que el kit también captura glucosa libre y sacarosa: si el producto tiene azúcar añadida, hay que
  interpretar con cuidado y correr el control del kit (ver `221`).
- Confundir "fibra dietaria total" con β-glucano: la fibra incluye quitina, celulosa y más.
- Aceptar un α-glucano alto porque "es que el extracto lleva maltodextrina" sin que la maltodextrina esté en
  la ficha de formulación firmada.
- Reportar el α-glucano en base húmeda y compararlo con un β-glucano en base seca. Nunca mezcles bases
  (ver `07`).

## Conexión con otros módulos

→ `219-beta-glucanos-quimica-y-estructura.md` — la otra mitad de la historia.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el procedimiento completo.
→ `222-polisacaridos-totales-por-que-no-sirve.md` — el método que mete todo en la misma bolsa.
→ `218-el-fraude-del-micelio-en-grano.md` — el fraude que este confusor hace posible.
→ `52-polisacaridos-y-glucanos.md` — química general de la familia.
