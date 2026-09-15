# 100 — Microbiología de producto (el ensayo que te cierra la planta si sale mal)

De todos los análisis que le vas a pagar a un laboratorio, el microbiológico es el que tiene más
probabilidad de sacarte un lote del mercado. Un metal pesado alto es un problema; una *Salmonella* positiva
es un retiro de producto, una investigación sanitaria y, en Colombia, un expediente con INVIMA. Y es el
ensayo más sensible al **muestreo**: la contaminación no está repartida homogéneamente, está en manchas. Este
módulo te da qué se mide, con qué límites, y por qué la humedad y la actividad de agua deciden el resultado
antes de que la muestra salga de tu bodega.

Términos: **UFC (CFU, Colony Forming Unit)** = una colonia contable en placa; se reporta por gramo o por mL.
**recuento total aerobio (TAMC, Total Aerobic Microbial Count)** = todo lo que crece en condiciones aerobias.
**TYMC (Total Yeast and Mold Count)** = levaduras y mohos. **patógeno (pathogen)** = organismo que se busca
por **ausencia**, no por conteo. **aw (water activity)** = agua disponible; gobierna qué puede crecer.

## Qué se mide y qué se busca

| Ensayo | Se reporta como | Por qué importa |
|---|---|---|
| **TAMC** | UFC/g | Higiene general del proceso |
| **TYMC** | UFC/g | Hongos y levaduras; en producto de hongo el ensayo se hace sobre material inactivado |
| **Enterobacterias / coliformes** | UFC/g | Indicador de contaminación fecal o de manipulación |
| ***E. coli*** | Ausencia en 1 g (o 10 g) | Patógeno indicador |
| ***Salmonella*** spp. | Ausencia en 25 g | Patógeno de retiro inmediato |
| ***Staphylococcus aureus*** | Ausencia en 1 g | Manipulación humana |
| ***Aspergillus*** productores de aflatoxina (*A. flavus*, *A. niger*, *A. fumigatus*, *A. terreus*) | Ausencia | Exigido en varios mercados de cannabis; ligado a micotoxinas (`101`) |
| *Pseudomonas aeruginosa* | Ausencia en 1 g | En productos no orales / tópicos |
| *Bacillus cereus*, *Clostridium* | Según matriz | Esporulados que sobreviven al secado |

Los límites concretos **dependen del mercado y de la categoría de producto**. Las referencias que se usan:
farmacopeas (USP ⟨61⟩, ⟨62⟩, ⟨2021⟩, ⟨2022⟩ para productos de origen natural; Ph. Eur. 5.1.4 / 5.1.8) y la
norma sanitaria de cada país. En Colombia, a agosto de 2026, los suplementos dietarios se rigen por el marco
del Decreto 3249 de 2006 y sus modificaciones, con los requisitos microbiológicos que INVIMA exige en el
registro sanitario; **verifica el texto vigente antes de fijar tu especificación** (ver `266` y `269`).

Órdenes de magnitud que se ven en especificaciones de suplementos en polvo (ILUSTRATIVO, no es una norma):

```
TAMC                : <= 10^4 - 10^5 UFC/g
TYMC                : <= 10^2 - 10^3 UFC/g
Enterobacterias     : <= 10^2 - 10^3 UFC/g
E. coli             : ausencia en 1 g
Salmonella          : ausencia en 25 g
S. aureus           : ausencia en 1 g
```

## La trampa del hongo: TYMC en un producto que ES un hongo

Un polvo de reishi o de melena de león **es** material fúngico. Si el proceso lo dejó viable, el TYMC puede
salir alto sin que haya contaminación externa: son las esporas y el micelio del propio producto. Por eso:

1. El material debe estar **inactivado** (secado y/o tratado térmicamente) antes de envasar.
2. El laboratorio debe saber que la matriz es fúngica, para interpretar y, si aplica, identificar la colonia.
3. Un TYMC alto **siempre** se investiga: se identifica qué creció. Si es *Aspergillus*, es un problema de
   inocuidad; si es la propia especie, es un problema de proceso.

Ver `244-micotoxinas-y-contaminacion-en-hongos.md`.

## Métodos: placa clásica vs métodos rápidos

| Método | Tiempo | Nota |
|---|---|---|
| Siembra en placa (referencia) | 3–5 días TAMC; 5–7 días TYMC; ~5 días Salmonella | El método aceptado por defecto |
| Petrifilm y equivalentes | Igual tiempo, menos trabajo | Validado por AOAC para muchas matrices |
| **qPCR** | 24–48 h | Detecta ADN: puede dar positivo con células **muertas**; exige confirmación por cultivo |
| Citometría / bioluminiscencia | Horas | Tamiz interno, no resultado de liberación |

En el mercado de cannabis de EE. UU. la discusión qPCR vs cultivo es constante justamente porque qPCR
detecta ADN de organismos ya inactivados y puede rechazar producto seguro, o al revés, no distinguir
viabilidad. A agosto de 2026 la práctica defendible es: tamiz rápido interno, **liberación por el método de
referencia** del regulador de tu mercado.

## Cómo se comprueba

- **Plan de muestreo escrito**: número de tomas, puntos, tamaño de la muestra compuesta (ver `66`).
- **Muestra tomada asépticamente**, en bolsa estéril, con cadena de frío si aplica (ver `109`).
- **Controles del laboratorio**: control positivo, control negativo, control de medio, y **prueba de
  idoneidad del método** (method suitability / neutralización) para demostrar que tu matriz no inhibe el
  crecimiento. Sin ese control, un "ausencia de Salmonella" puede ser un falso negativo por un extracto
  antimicrobiano.
- **Tiempo entre muestreo y análisis** declarado: la flora cambia. En polvos secos es tolerante, en líquidos
  no.

## Ejemplo aplicado (ILUSTRATIVO)

Lote de cápsulas de melena de león, HE-2604, 30.000 unidades.

```
Muestreo   : 10 tomas de puntos distintos del lote, compuesto de 100 g, bolsa esteril
aw producto: 0,44         Humedad: 5,1 % p/p (KF, ver 98)
TAMC       : 1,2 x 10^3 UFC/g        Especificacion <= 10^4        CONFORME
TYMC       : 4,0 x 10^2 UFC/g        Especificacion <= 10^3        CONFORME
Enterobact.: < 10 UFC/g                                            CONFORME
E. coli    : ausencia en 1 g                                       CONFORME
Salmonella : ausencia en 25 g                                      CONFORME
Idoneidad del metodo: recuperacion del control positivo 78 %  -> valida
Laboratorio: acreditado ISO/IEC 17025 con el ensayo EN el alcance (ver 107)
```

Con aw 0,44 el producto es microbiológicamente estable: por debajo de 0,60 prácticamente nada crece. El
riesgo real ya no es crecimiento, es la carga que **traía** la materia prima. (Cifras ilustrativas.)

## Errores comunes

- **Analizar producto terminado y no materia prima.** El microbio entra con la materia prima; ahí es más
  barato encontrarlo.
- **Una sola toma del lote.** La contaminación es en manchas; una toma no representa nada.
- **No pedir prueba de idoneidad del método** en matrices con actividad antimicrobiana (extractos, aceites
  esenciales, alcohol).
- **Confiar en un qPCR positivo sin confirmar por cultivo**, o al revés, liberar con qPCR donde el regulador
  exige cultivo.
- **Ignorar la aw.** Controlar aw ≤ 0,60 hace más por la inocuidad que repetir el ensayo.
- **Muestra tomada por el proveedor.** Igual que en potencia: la muestra la tomas tú (ver `109`, `113`).
- **No fechar el muestreo aparte del análisis.** Si pasaron 20 días, el resultado ya no describe el lote.

## Conexión con otros módulos

→ `101-analisis-de-micotoxinas.md` — el mohito que crece hoy es la aflatoxina de mañana.
→ `35-actividad-de-agua-y-humedad.md` y `98-karl-fischer-y-humedad.md` — lo que decide si algo crece.
→ `66-plan-de-muestreo-y-representatividad.md` — el ensayo más dependiente del muestreo de todos.
→ `203-micotoxinas-y-microbiologia-en-cannabis.md` — el caso cannabis y el debate qPCR.
→ `244-micotoxinas-y-contaminacion-en-hongos.md` — el caso hongos.
→ `266-invima-y-suplementos-dietarios.md` — el marco colombiano y sus requisitos.