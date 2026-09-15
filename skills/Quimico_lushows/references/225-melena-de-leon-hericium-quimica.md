# 225 — Melena de león (*Hericium erinaceus*): química de la especie

La melena de león es el hongo con el marketing más peligroso del mercado, porque casi todo lo que se dice
de él roza o cruza la línea del claim de enfermedad. Químicamente es interesante por un motivo real: es el
único de la lista donde **el micelio y el cuerpo fructífero producen familias de moléculas distintas** —
erinacinas en el micelio, hericenonas en la seta. Eso hace que la pregunta "¿qué parte usaste?" no sea
retórica: cambia el marcador que se puede medir.

Términos: **cuerpo fructífero (fruiting body)** = la seta blanca en cascada. **hericenona (hericenone)** =
compuesto aromático (meroterpenoide) del cuerpo fructífero. **erinacina (erinacine)** = diterpenoide de tipo
ciatano del micelio, frecuentemente como xilósido. **hericeno (hericene)** = serie relacionada de compuestos
aromáticos. **NGF (nerve growth factor)** = factor de crecimiento nervioso, proteína usada como desenlace en
estudios `[in vitro]`.

## Composición por parte del hongo

| Familia | Dónde está | Solubilidad | Se mide por |
|---|---|---|---|
| β-glucanos | Cuerpo fructífero (pared celular) | Agua caliente | Megazyme K-YBGL (`221`) |
| Hericenonas y hericenos | Cuerpo fructífero | Alcohol / solventes orgánicos | UHPLC-UV, LC-MS (`226`) |
| Erinacinas | **Micelio** | Alcohol | UHPLC-UV, LC-MS (`226`) |
| Ergosterol | Ambos | Alcohol | HPLC-UV 282 nm (`238`) |
| α-glucano (almidón) | Solo si hay grano del sustrato | — | Megazyme K-YBGL (`220`) |

El dato clave, publicado: **las hericenonas se aíslan del cuerpo fructífero y las erinacinas del micelio**;
el tejido de cuerpo fructífero por lo general **no produce cantidades detectables de erinacinas** (Kawagishi
y colaboradores, revisión en *Mycology*, 2010, tandfonline.com; y estudio de sustrato y tipo de tejido sobre
producción de erinacinas y expresión de genes biosintéticos, *Journal of Fungi* / PMC11969743, 2025).

Esto tiene una consecuencia comercial incómoda: si tu producto es 100 % cuerpo fructífero —lo correcto
para β-glucanos— **no tiene erinacinas**, y no puedes citar la literatura de erinacinas para venderlo.
Y si es micelio, probablemente viene con grano y tu β-glucano será bajo (ver `218`).

## Rangos: lo que hay y lo que no hay

- **β-glucano.** Fuentes de la industria mencionan que un extracto auténtico de cuerpo fructífero de melena
  de león suele caer del orden de **30–40 % p/p base seca**, y advierten que valores muy altos (por encima
  de ~80 %) suelen indicar adición de polisacáridos baratos más que calidad excepcional (análisis de mercado
  de suplementos de hongos, 2026). Trátalo como referencia de mercado y **mide tu lote**.
- **Hericenonas y erinacinas.** No hay un rango de consenso publicado que sirva como especificación
  universal: la variabilidad por cepa, sustrato y etapa es muy alta, y hasta hace poco no existía un método
  único que las midiera juntas. En 2026 se publicó un método UHPLC-UV validado para determinar
  simultáneamente hericenonas, hericenos, erinacinas y ergosterol en materias primas y productos, con
  corrida de ~38 minutos (*Molecules* / PMC12899107). Ese es hoy el punto de partida técnico (ver `226`).

Si alguien te ofrece "Lion's mane 0,5 % hericenonas" pídele el método, el patrón y el cromatograma. Los
patrones de hericenonas son escasos y caros; esa cifra rara vez está bien sustentada.

## Cómo se mide / cómo se comprueba

| Marcador | Método | Unidad y base |
|---|---|---|
| β-glucano / α-glucano | Megazyme K-YBGL | `% p/p base seca` |
| Hericenonas, hericenos, erinacinas, ergosterol | UHPLC-UV (método simultáneo, 2026) o LC-MS/MS | `mg/g base seca` |
| Identidad de especie | Secuenciación ITS | % de identidad |
| Presencia de grano | α-glucano y microscopía de almidón | `% p/p base seca` |
| Metales pesados | ICP-MS | `mg/kg base seca` |
| Humedad | Karl Fischer | `% p/p` |

## Ejemplo aplicado — decidir qué material comprar para BIO-SETA

**(ILUSTRATIVO)**

```
Opcion A: cuerpo fructifero, extracto acuoso 8:1
   beta-glucano  32,5 % p/p b.s.
   alfa-glucano   2,8 % p/p b.s.
   erinacinas     no aplica (no las produce el cuerpo fructifero)
   hericenonas    a medir por UHPLC-UV; declarar solo si se mide

Opcion B: micelio sobre arroz, "rico en erinacinas"
   beta-glucano   5,9 % p/p b.s.
   alfa-glucano  38,4 % p/p b.s.
   erinacinas     el proveedor no aporta metodo ni patron
   Lectura: se paga arroz y se compra una promesa sin analitica.

Decision: opcion A, y si mas adelante se quiere hablar de hericenonas,
se paga el ensayo UHPLC-UV y se declara con metodo y unidad.
```

## Qué se puede y qué no se puede afirmar

Esta es la especie donde hay que ser más estricto, porque la literatura invita a exagerar:

- **Se puede** declarar composición medida: β-glucanos por porción, con método y base.
- **Se puede** decir que hericenonas y erinacinas **han sido estudiadas** por su efecto sobre la biosíntesis
  de NGF en cultivos de astrocitos de roedor `[in vitro]` (Kawagishi et al., *Mycology*, 2010). Eso es
  describir el estado de la investigación, no prometer un efecto.
- **No se puede** decir que "mejora la memoria", "regenera nervios", "previene enfermedades
  neurológicas" ni nada equivalente. Esa última frase es literalmente una de las que le costó caro a
  BIO-SETA (ver `268`). Un resultado `[in vitro]` sobre NGF **no** es un efecto cognitivo en personas.
- **No se puede** trasladar evidencia de erinacinas a un producto de cuerpo fructífero que no las contiene.

## Errores comunes

- Vender cuerpo fructífero y citar estudios de erinacinas. Es el error químico y legal más frecuente de la
  especie.
- Aceptar "hericenonas 1 %" sin método, patrón ni cromatograma.
- Comprar micelio en grano por el argumento de las erinacinas y terminar con 6 % de β-glucano.
- Traducir "NGF" al lenguaje del consumidor como "regeneración del cerebro".
- No medir metales: la melena de león se cultiva sobre aserrín suplementado y el sustrato importa (`239`).

## Conexión con otros módulos

→ `226-hericenonas-y-erinacinas-analisis.md` — el detalle analítico de los dos marcadores.
→ `217-micelio-vs-cuerpo-fructifero.md` — por qué aquí la parte usada decide la química.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el otro activo, medible y defendible.
→ `12-niveles-de-evidencia.md` — cómo no convertir un `[in vitro]` en una promesa.
→ `268-claims-prohibidos-el-caso-bioseta.md` — el caso concreto y las frases a retirar.