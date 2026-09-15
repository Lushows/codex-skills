# 06 — Estequiometría y balance de masa (la materia no aparece ni desaparece)

La estequiometría suena a examen de bachillerato, pero es la herramienta más práctica que tiene un
dueño de producto: te dice cuánto activo **puede** haber, como máximo, y te permite detectar mentiras
sin pisar un laboratorio. Si entran 10 kg de hongo seco con 30 % de β-glucano y sale un extracto que
pesa 2,5 kg, no puede haber más de 3 kg de β-glucano en ese extracto, pase lo que pase. Cuando un
proveedor te ofrece cifras que rompen el balance de masa, no necesitas discutir de química: le
muestras la cuenta. Y en cannabis la estequiometría es directamente la ley: el famoso factor 0,877
sale de aquí.

Términos: **estequiometría (stoichiometry)** = relación cuantitativa entre lo que entra y lo que sale
de una reacción. **masa molar (molar mass)** = masa de un mol, en g/mol. **balance de masa (mass
balance)** = contabilidad de toda la materia que entra, sale y se pierde en un proceso. **rendimiento
(yield)** = fracción de lo posible que realmente obtuviste. **recuperación (recovery)** = fracción del
analito que sobrevive al proceso y aparece en el producto.

## La contabilidad básica

```
BALANCE DE MASA TOTAL
  masa que entra = masa que sale + masa que se pierde (+ acumulación)

BALANCE DE UN COMPONENTE
  masa de analito en la entrada = masa en el producto + masa en el residuo + degradado

RENDIMIENTO DE PROCESO (%)
  = 100 × masa de producto obtenida / masa de material de partida

RECUPERACIÓN DEL ACTIVO (%)
  = 100 × (masa de activo en el producto) / (masa de activo en la entrada)
```

Estas cuatro líneas resuelven casi todas las discusiones con maquiladores. Si el balance no cierra, o
falta medir algo o alguien está adivinando.

## Estequiometría cuando hay reacción: el caso THCA → THC

La descarboxilación (decarboxylation) del ácido tetrahidrocannabinólico pierde una molécula de CO2:

| Especie | Masa molar (g/mol) |
|---|---|
| THCA (C22H30O4) | 358,47 |
| CO2 | 44,01 |
| Δ9-THC (C21H30O2) | 314,46 |

```
358,47 − 44,01 = 314,46
factor = 314,46 / 358,47 = 0,8772  ->  se usa 0,877
THC total = Δ9-THC + (THCA × 0,877)
```

Ese 0,877 no es una convención regulatoria arbitraria: es aritmética de masas molares. Aplicarlo mal
—olvidarlo, o aplicarlo dos veces— convierte un producto legal en ilegal o al revés (ver `174`, `175`).
Para calcularlo, `lab-tools/thc_total.py` y `lab-tools/decarboxilacion.py`.

## Cómo se comprueba un balance de masa en tu propia planta

Procedimiento que puedes hacer con una balanza y un COA por etapa:

1. **Pesa la entrada** de material seco y mídele humedad (todo en base seca, ver `07`).
2. **Mide el analito en la entrada** por el método definitivo, no por uno "aproximado".
3. **Pesa cada salida**: producto, torta de residuo, solvente recuperado, mermas.
4. **Mide el analito en el producto y en el residuo.**
5. **Cierra la cuenta.** Un cierre del 90–105 % es normal; por fuera de ahí, investiga.
6. **Documenta** el balance por lote: es lo que después sostiene tu ratio y tu rendimiento (ver `168`).

Un balance que "cierra" en 130 % no es un proceso milagroso: es un error de medición, de humedad o de
método. La materia no se multiplica.

## Ejemplo aplicado (BIO-SETA)

Lote piloto de extracto acuoso de reishi, todo **(ILUSTRATIVO)**:

```
ENTRADA
  cuerpo fructífero seco:        10,00 kg (humedad 8 %  ->  9,20 kg base seca)
  β-glucano en la entrada:       28,0 % p/p base seca  ->  9,20 × 0,280 = 2,576 kg

SALIDA
  extracto en polvo:              2,30 kg (humedad 4 %  ->  2,208 kg base seca)
  β-glucano en el extracto:      45,0 % p/p base seca  ->  2,208 × 0,450 = 0,9936 kg

INDICADORES
  rendimiento de proceso:        100 × 2,30 / 10,00           = 23,0 %
  ratio planta:extracto:         10,00 / 2,30                 = 4,3 : 1
  recuperación de β-glucano:     100 × 0,9936 / 2,576         = 38,6 %
  factor de concentración:       45,0 / 28,0                  = 1,61 veces
```

Lectura del químico: el extracto está 1,61 veces más concentrado que la materia prima, pero **se perdió
el 61 % del β-glucano** en la torta y el agua madre. Ese es el dato que decide si vale la pena
optimizar la extracción (más tiempo, más ciclos, molienda más fina) o si el proceso está bien y el
material de partida era pobre. Sin balance de masa, esa conversación es imposible.

Y una alerta comercial: si otro proveedor te ofrece un extracto "10:1 con 70 % de β-glucano", pídele
el balance. Con una materia prima de 28 % base seca, un 10:1 tendría que recuperar más β-glucano del
que existía. La cuenta lo desmiente sin necesidad de análisis.

## Órdenes de magnitud útiles (verificar con tu proceso)

| Proceso | Rendimiento típico reportado | Comentario |
|---|---|---|
| Extracción acuosa de hongo seco | 15–30 % p/p | Depende de tiempo, temperatura y molienda |
| Extracción hidroalcohólica de hongo | 5–15 % p/p | Saca triterpenos, no β-glucanos |
| Extracción dual (agua + alcohol combinadas) | 20–35 % p/p | Ver `146` |
| Etanol sobre biomasa de cannabis | 10–20 % p/p de crudo | Antes de winterización |

Rangos orientativos de literatura y práctica industrial; **mide el tuyo**, porque cambia con especie,
sustrato, secado y equipo.

## Errores comunes

- **Mezclar bases.** Calcular el balance con entradas en base húmeda y salidas en base seca; el número
  sale mal y nadie se da cuenta.
- **Olvidar el residuo.** Sin medir la torta no sabes si perdiste el activo o nunca estuvo.
- **Confundir rendimiento con recuperación.** Puedes tener 30 % de rendimiento y 10 % de recuperación:
  sacaste mucha masa, pero poco de lo que importa.
- **Vender el ratio como potencia.** Un 10:1 con activo bajo es peor que un 4:1 con activo alto (ver `151`).
- **Aplicar 0,877 a un resultado que ya venía descarboxilado** (típico de GC), y reportar THC total
  inflado o deflactado (ver `198`).
- **Hacer la cuenta de memoria.** Todo esto va a `lab-tools/` o a `Matematicas_lushows`.

## Conexión con otros módulos

→ `04-unidades-concentraciones-y-conversiones.md` — las unidades con las que se arma el balance.
→ `07-base-seca-vs-humeda.md` — sin esto, el balance nunca cierra.
→ `151-relacion-planta-extracto-y-ratios.md` — cómo se declara honestamente un ratio.
→ `174-descarboxilacion-cinetica-y-calculo.md` — la reacción detrás del factor 0,877.
→ `175-thc-total-y-el-factor-0877.md` — su uso regulatorio.
→ `166-escalado-de-lote.md` — qué cambia del balance cuando subes de escala.
