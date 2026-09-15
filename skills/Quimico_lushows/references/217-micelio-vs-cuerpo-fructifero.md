
# 217 — Micelio vs cuerpo fructífero (la decisión que define tu producto)

Esta es la primera pregunta que hay que hacerle a cualquier proveedor de hongos, y la que más plata mueve.
"Reishi en polvo" puede ser la seta molida o puede ser arroz colonizado por micelio y secado con el arroz
adentro. Son materiales químicamente distintos, cuestan distinto y no se pueden vender con la misma etiqueta
sin mentir. Este módulo, junto con `218` a `222`, se lee como una unidad: aquí definimos los materiales, en
`218` el fraude, en `219`–`220` la química que lo delata y en `221`–`222` cómo se demuestra con números.

Términos: **cuerpo fructífero (fruiting body)** = la seta. **micelio (mycelium)** = red de hifas.
**micelio sobre grano (mycelium on grain, MOG)** = micelio crecido sobre arroz/avena y secado **junto con el
grano**. **biomasa de fermentación líquida (liquid fermentation biomass)** = micelio filtrado de un tanque,
sin grano. **α-glucano (alpha-glucan)** = familia de glucanos donde vive el almidón.

## Los cuatro materiales que existen en el mercado

| Material | Qué es exactamente | Grano incluido | β-glucano típico | α-glucano típico |
|---|---|---|---|---|
| Cuerpo fructífero seco | Seta cosechada, secada, molida | No | Alto | Muy bajo |
| Extracto de cuerpo fructífero | Seta extraída (agua y/o alcohol) y concentrada | No | Más alto | Muy bajo |
| Micelio de fermentación líquida | Biomasa filtrada del tanque | No | Medio-bajo | Bajo-medio |
| Micelio sobre grano (MOG) | Grano colonizado, secado entero | **Sí** | Muy bajo | **Muy alto** |

Rangos de referencia de la literatura de la industria: Nammex, en su trabajo presentado a la International
Society for Mushroom Science y en su whitepaper *Redefining Medicinal Mushrooms*, reporta β-glucano de
**25–66 % p/p** en muestras comerciales de cuerpo fructífero, y **por debajo de 10 % p/p** de forma
consistente en productos de micelio sobre grano; el α-glucano (almidón) del MOG cae en **30–60 % p/p**,
con casos de 66–72 %, mientras el hongo verdadero tiene apenas **1–5 %** de almidón
(nammex.com, whitepaper y notas técnicas; recogido también por NutraIngredients, marzo de 2017).
Trátalo como orden de magnitud del mercado, no como verdad de tu lote: mídelo.

## Por qué el micelio sobre grano es tan pobre en β-glucano

Sencillo: la mayor parte de la masa que compras **no es hongo, es grano**. El micelio coloniza el arroz pero
no lo consume completo, y como el producto se seca entero (micelio + sustrato residual), el almidón del
arroz entra al polvo final. En un polvo con 60 % de arroz residual, aunque el micelio puro tuviera un
β-glucano decente, el resultado queda diluido por definición.

Segundo motivo: el micelio, incluso puro, tiene una pared más delgada y menos matriz de glucano que el
cuerpo fructífero maduro, cuya estructura mecánica **es** la pared celular. La seta necesita rigidez para
sostenerse; el micelio no.

## Lo que sí tiene el micelio (para ser justos)

No todo micelio es basura. Hay compuestos que el micelio produce y el cuerpo fructífero no:

- **Erinacinas** de *Hericium erinaceus*: son diterpenoides de tipo ciatano que se encuentran en el micelio;
  el tejido de cuerpo fructífero por lo general no produce cantidades detectables (ver `226`).
- **PSK (krestin)** de *Trametes versicolor*: es un polisacárido unido a proteína aislado del **micelio**,
  desarrollado como adyuvante en Japón (ver `231`).
- Cultivos de micelio en medio controlado permiten reproducibilidad y trazabilidad que el silvestre no da.

La conclusión honesta no es "micelio malo", es: **micelio puro con su marcador medido, sí; micelio con grano
vendido como si fuera hongo, no.**

## Cómo se mide / cómo se comprueba

El par que resuelve la discusión en un solo ensayo es **β-glucano + α-glucano por Megazyme K-YBGL**, sobre
`% p/p base seca` (ver `221`). Regla de lectura práctica:

```
alfa-glucano alto (>10 % p/p b.s.)  +  beta-glucano bajo (<10 % p/p b.s.)
        =>  hay grano/almidon en el producto. Pide explicacion por escrito.

beta-glucano alto  +  alfa-glucano bajo (<5 % p/p b.s.)
        =>  consistente con cuerpo fructifero o su extracto.
```

Confirmaciones complementarias:

| Pregunta | Método | Qué esperarías |
|---|---|---|
| ¿Hay biomasa fúngica real? | Ergosterol por HPLC-UV 282 nm (`238`) | Bajo en producto con mucho grano |
| ¿Es la especie declarada? | Secuenciación ITS (`245`) | Coincidencia con la especie de la etiqueta |
| ¿Cuánto almidón exactamente? | Método de almidón AOAC en paralelo (`220`) | Coherente con el α-glucano |
| ¿Hay proteína de grano? | Nitrógeno total / Kjeldahl o Dumas | Perfil distinto al fúngico |

## Ejemplo aplicado — dos cotizaciones de "reishi" para BIO-SETA

**(ILUSTRATIVO)**

```
Proveedor A — "Reishi extract 30% polysaccharides, 4:1"   USD 38/kg
   beta-glucano   7,9 % p/p b.s.   (Megazyme K-YBGL)
   alfa-glucano  41,2 % p/p b.s.
   Lectura: micelio sobre grano. El "30 % de polisacaridos" es casi todo almidon.
   Costo real por gramo de beta-glucano: 38 / (0,079 x 1000) = USD 0,48/g

Proveedor B — "Reishi fruiting body extract"              USD 95/kg
   beta-glucano  29,6 % p/p b.s.
   alfa-glucano   2,4 % p/p b.s.
   Costo real por gramo de beta-glucano: 95 / (0,296 x 1000) = USD 0,32/g
```

El proveedor "barato" es 50 % más caro por gramo de activo. Ese cálculo hazlo siempre en código, no de
memoria (`Matematicas_lushows`, o `lab-tools/betaglucano_dosis.py`).

## Qué se puede y qué no se puede afirmar

- Se puede decir: "elaborado 100 % con cuerpo fructífero", si tienes el respaldo documental y analítico.
- Se puede decir: "contiene X mg de β-glucanos por porción, medidos por Megazyme K-YBGL".
- No se puede decir que el material "fortalece las defensas contra enfermedades" ni nada equivalente: eso
  es claim de enfermedad (ver `267`, `268`).
- La evidencia de inmunomodulación por β-glucanos es mayoritariamente `[in vitro]` y `[animal]`, con
  clínicos limitados y específicos de preparaciones concretas (ver `130`, `248`).

## Errores comunes

- Aceptar "mycelial biomass" en la ficha sin preguntar si viene con grano. Casi siempre viene con grano.
- Leer "polisacáridos 30 %" como si fuera β-glucano (ver `222`).
- Pensar que "full spectrum" garantiza cuerpo fructífero: es un término de mercadeo sin definición analítica.
- Comparar precio por kilo en vez de precio por gramo de activo medido.
- Traducir "mycelium" como "raíz del hongo" en el material de venta: es falso y te deja expuesto.

## Conexión con otros módulos

→ `218-el-fraude-del-micelio-en-grano.md` — cómo opera el engaño y qué cifras lo delatan.
→ `220-alfa-glucanos-y-almidon-el-confusor.md` — la molécula que hace el disfraz.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el ensayo paso a paso.
→ `238-ergosterol-como-marcador.md` — confirmación independiente de biomasa fúngica.
→ `242-ratios-de-extraccion-y-etiquetado-honesto.md` — por qué "4:1" no dice nada de potencia.
