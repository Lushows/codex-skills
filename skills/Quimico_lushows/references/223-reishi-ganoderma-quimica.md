# 223 — Reishi (*Ganoderma*): química completa de la especie estrella

El reishi es el hongo más vendido y el más malinterpretado. Tiene **dos familias de activos que se extraen
con solventes distintos**: β-glucanos, que salen en agua caliente, y triterpenos ganodéricos, que salen en
alcohol. Quien vende "extracto de reishi" sin decir cuál extracción hizo está vendiendo la mitad del hongo y
cobrando por el entero. Este módulo te da la composición, los rangos publicados y qué medir en cada caso.

Términos: **cuerpo fructífero (fruiting body)** = el conk leñoso. **triterpeno (triterpene)** = molécula de
30 carbonos derivada de la ruta del mevalonato; en reishi son los ácidos ganodéricos. **esporas
(spores)** = polvo reproductivo, con pared muy dura. **extracción dual (dual extraction)** = agua caliente
+ alcohol, combinadas.

## Identidad: el lío del nombre

| Nombre que verás | Situación taxonómica a agosto de 2026 |
|---|---|
| *Ganoderma lucidum* | Nombre histórico; estrictamente corresponde a material europeo |
| *Ganoderma lingzhi* | Nombre correcto para el reishi asiático cultivado (Cao et al., 2012) |
| *Ganoderma sichuanense* | Sinónimo usado en parte de la literatura china |
| *Ganoderma applanatum* | Otra especie (artist's conk). No es reishi |

Un COA que dice *G. lucidum* no es fraude por sí mismo: es la costumbre. Pero si mandas identidad por ITS
(ver `245`) y vuelve *G. lingzhi*, no es un hallazgo, es lo esperable. Lo que sí es problema es que vuelva
otra especie del género o un *Ganoderma* silvestre no identificado.

## Familias de compuestos y dónde viven

| Familia | Ejemplos | Parte donde abunda | Solubilidad |
|---|---|---|---|
| β-glucanos | β-(1→3)/(1→6), algunos ligados a proteína | Cuerpo fructífero | Agua caliente |
| Triterpenos ganodéricos | Ácidos ganodéricos A, B, C2, D, F, H; ganoderoles; lucidenicos | Cuerpo fructífero (más en el sombrero y la capa externa) | Etanol / metanol |
| Esteroles | Ergosterol y derivados | Todo el hongo | Alcohol / lipídico |
| Proteínas y péptidos | LZ-8 (Ling Zhi-8), inmunomodulina | Cuerpo fructífero, micelio | Acuosa, termolábil |
| Nucleósidos | Adenosina, guanosina | Todo el hongo | Agua |
| Minerales y metales | Germanio, y también Pb/Cd si el sustrato estaba contaminado | Todo | — |

El amargor del reishi es en buena parte triterpénico. No es prueba analítica, pero un "extracto de reishi"
que no amarga nada difícilmente tiene triterpenos relevantes.

## Rangos reportados en la literatura

**β-glucanos.** En muestras comerciales de cuerpo fructífero de hongos funcionales medidas por Megazyme
K-YBGL se reportan **25–66 % p/p base seca**, frente a <10 % en micelio sobre grano (Nammex, whitepaper
*Redefining Medicinal Mushrooms*, nammex.com). Para *Ganoderma lucidum* específicamente, un extracto
enzimático de cuerpo fructífero tipo "antler" reportó **40,57 % de β-glucano** y 7,47 % de proteína
(*Journal of Fungi* / MDPI, 2022; PMC9573635). El contenido en cuerpo fructífero depende de la cepa y del
sustrato de madera (Sánchez-Hernández et al., *Journal of Fungi*, 2020; PMC7587577).

**Triterpenos.** Un trabajo con LC-MS/MS y determinación de triterpenos totales sobre productos y materiales
de *Ganoderma* reportó triterpenos totales entre **0,21 % y 10,56 %**, mientras la cuantificación dirigida
a ácidos ganodéricos concretos por LC-MS/MS dio **0,01 % a 0,98 %**. Esa brecha entre "totales" y "ácidos
ganodéricos identificados" es exactamente el mismo problema que "polisacáridos" vs β-glucano (ver `224`,
`222`). En polvo de esporas amargo se reportan triterpenos totales de 6,3–7,4 % con procesos específicos
frente a ~1,7 % con rotura de pared convencional (documentación de patente, US 11,083,763).

Todos esos son rangos de literatura: **verifica con tu lote**. La variabilidad entre cepas, sustratos y
partes del hongo es enorme.

## Cómo se mide / cómo se comprueba

| Marcador | Método | Unidad y base |
|---|---|---|
| β-glucano y α-glucano | Megazyme K-YBGL, enzimático por diferencia | `% p/p base seca` (`221`) |
| Triterpenos totales | Colorimétrico con ácido vanillina-perclórico, vs ácido oleanólico | `% p/p base seca`, ojo: inespecífico (`224`) |
| Ácidos ganodéricos individuales | HPLC-DAD ~252/254 nm o LC-MS/MS con patrones | `% p/p base seca` o `mg/g` (`224`) |
| Ergosterol | HPLC-UV 282 nm | `mg/g base seca` (`238`) |
| Identidad de especie | Secuenciación ITS | % identidad (`245`) |
| Metales pesados | ICP-MS | `mg/kg base seca` (`243`) |
| Humedad | Karl Fischer o pérdida por secado | `% p/p` (`98`) |

## Ejemplo aplicado — especificación de entrada para BIO-SETA

**(ILUSTRATIVO — construye la tuya con al menos 3 lotes, ver `282`):**

```
Materia prima: Extracto de reishi, cuerpo fructifero, extraccion dual
Identidad          Ganoderma lingzhi por ITS, >= 99 % identidad
beta-glucano       >= 25,0 % p/p base seca   (Megazyme K-YBGL)
alfa-glucano       <=  5,0 % p/p base seca   (Megazyme K-YBGL)
Triterpenos        >=  2,0 % p/p base seca   (HPLC-DAD, como acido ganoderico A)
Humedad            <=  6,0 % p/p             (Karl Fischer)
Pb / Cd / As / Hg  segun limite regulatorio vigente (ICP-MS, ver 243 y 272)
Microbiologia      segun 100 y la norma aplicable
```

## Qué se puede y qué no se puede afirmar

- **Se puede** declarar composición medida: "aporta X mg de β-glucanos y Y mg de triterpenos por porción,
  con método y base".
- **Se puede** mencionar uso tradicional marcándolo: "usado tradicionalmente en la medicina de Asia
  oriental" `[tradicional]`.
- **No se puede** decir que el reishi trata, cura o previene ninguna enfermedad, ni con eufemismos.
  La literatura de *Ganoderma* está llena de estudios `[in vitro]` y `[animal]`; hay clínicos, pero pequeños
  y heterogéneos (ver `248`).
- Cuidado especial: la palabra "anticancerígeno" y variantes son claim de enfermedad y ya generaron un
  problema real en BIO-SETA (ver `268`).

## Errores comunes

- Vender extracto acuoso y hablar de triterpenos: si extrajiste solo con agua, los triterpenos casi no
  están (ver `241`, `146`).
- Reportar "triterpenos totales" por colorimetría y presentarlos como ácidos ganodéricos (ver `224`).
- Usar esporas sin romper la pared: la pared de la espora es muy resistente y sin rotura la extracción es
  pobre.
- Comprar reishi silvestre sin ICP-MS: el conk acumula lo que haya en el árbol y el ambiente (ver `243`).
- Comparar un producto de cuerpo fructífero con uno de micelio como si fueran el mismo reishi (ver `217`).

## Conexión con otros módulos

→ `224-triterpenos-ganodericos-analisis.md` — cómo se mide de verdad la fracción amarga.
→ `146-extraccion-dual-y-por-que-importa.md` — por qué el reishi necesita agua y alcohol.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el ensayo del otro activo.
→ `55-esteroles-y-triterpenos.md` — la química de fondo de la familia.
→ `268-claims-prohibidos-el-caso-bioseta.md` — la frontera de lo que puedes decir.
