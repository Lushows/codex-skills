# 241 — Extracción de hongos: agua vs alcohol (por qué el "extracto dual" no es marketing)

Los hongos guardan sus compuestos en dos cajones químicos distintos: los **polisacáridos** (beta-glucanos)
solo salen con agua caliente, y los **triterpenos y compuestos lipofílicos** solo salen con alcohol. Si
extraes con uno solo, dejas la mitad del material adentro — y si tu etiqueta habla del compuesto que no
extrajiste, tu producto no puede sostener lo que dice. Este módulo explica la química detrás de esa
decisión y cómo se comprueba con datos, no con fe.

Términos: **polaridad (polarity)** = qué tan bien un solvente disuelve compuestos con carga o puentes de
hidrógeno. **quitina (chitin)** = polímero rígido de la pared celular fúngica; hay que romperla para
liberar activos. **extracto dual (dual extract)** = combinación de un extracto acuoso y uno alcohólico.
**marc** = el sólido agotado que queda después de extraer.

## La química en una tabla

| Familia | Solubilidad | Sale con | Especies donde importa |
|---|---|---|---|
| Beta-glucanos (β-1,3/1,6) | Alta en agua caliente | Agua 80–100 °C, tiempo largo | Todas las funcionales |
| Triterpenos (ácidos ganodéricos) | Baja en agua, alta en etanol | Etanol 40–96 % | Reishi (Ganoderma) |
| Esteroles (ergosterol) | Insoluble en agua | Etanol/hexano | Marcador de biomasa fúngica |
| Hericenonas | Lipofílicas | Etanol | Melena de león (cuerpo fructífero) |
| Erinacinas | Lipofílicas | Etanol | Melena de león (micelio) |
| Nucleósidos (adenosina, cordicepina) | Solubles en agua | Agua tibia o hidroalcohol | Cordyceps |
| Ergotioneína | Muy soluble en agua | Agua | Varias, alta en Pleurotus |
| Polifenoles de chaga | Parcial en ambos | Hidroalcohol | Chaga (Inonotus) |

Detalle que casi nadie dice: la **quitina de la pared celular es el cuello de botella**. Sin agua caliente
prolongada (o molienda fina previa, o ayuda enzimática/ultrasonido) el solvente no llega al beta-glucano
aunque el beta-glucano sea soluble. Ver `147-ultrasonido-microondas-y-enzimas.md`.

## Cómo se hace un dual, conceptualmente

No es "mezclar agua y alcohol". Es hacer dos extracciones separadas del mismo material y luego combinarlas:

```
Biomasa seca y molida
   ├── Extracción acuosa (80–100 °C, varias horas)  → licor A (polisacáridos)
   └── El marc de A → extracción etanólica (etanol 60–80 %) → licor B (triterpenos, lipofílicos)
Se combinan A + B → se concentra → se seca (aspersión o liofilización) → polvo de extracto dual
```

Si en cambio extraes solo con una mezcla hidroalcohólica al 40 % de una sola pasada, obtienes un producto
intermedio pobre en las dos cosas: el agua no está caliente lo suficiente para los glucanos y el etanol
está muy diluido para los triterpenos.

## Cómo se mide / cómo se comprueba

La discusión "agua vs alcohol" se cierra con tres números, no con opiniones:

| Qué | Método | Unidad | Para qué |
|---|---|---|---|
| Rendimiento de extracto | Masa de extracto seco / masa de biomasa seca | % p/p | Base del ratio (`242`) |
| Beta-glucano en el extracto | Megazyme K-YBGL (enzimático) | % p/p base seca | Prueba que el agua sí funcionó |
| Alfa-glucano | Mismo kit, cálculo por diferencia | % p/p base seca | Delata almidón/grano (`220`) |
| Triterpenos totales | HPLC-DAD, 252 nm, patrón ácido ganodérico A | mg/g base seca | Prueba que el alcohol sí funcionó |
| Etanol residual | GC-headspace | ppm | Cumplimiento ICH Q3C clase 3 |

Y sobre todo: **analiza el marc agotado**. Si el sólido que botas todavía tiene 15 % de beta-glucano, tu
extracción no terminó y estás tirando plata al contenedor.

```
Balance de masa de activo (siempre debe cerrar dentro de ±10 %):
  Activo_entrada = Activo_extracto + Activo_marc + Pérdidas
Si no cierra, o el muestreo está mal, o el método está mal. (66, 06)
```

## Ejemplo aplicado (ILUSTRATIVO)

Reishi (Ganoderma lingzhi), cuerpo fructífero seco molido, 10,0 kg.

```
Ruta 1 — solo agua (95 °C, 4 h × 2):
  Extracto seco: 1,85 kg  → rendimiento 18,5 % p/p
  β-glucano: 32,4 % p/p b.s.   Triterpenos: 4,1 mg/g b.s.  (casi nada)

Ruta 2 — solo etanol 70 % (2 h × 2):
  Extracto seco: 0,72 kg  → rendimiento 7,2 % p/p
  β-glucano: 6,8 % p/p b.s.    Triterpenos: 41,6 mg/g b.s.

Ruta 3 — dual (agua y después etanol sobre el marc):
  Extracto seco combinado: 2,41 kg → rendimiento 24,1 % p/p
  β-glucano: 26,9 % p/p b.s.   Triterpenos: 13,2 mg/g b.s.
```

Lectura correcta: el dual **no** da lo mejor de los dos mundos en concentración — da la suma de los dos
mundos en masa, y por eso cada porcentaje baja al diluirse. Lo que importa no es el porcentaje del
extracto, sino los **mg de activo por porción diaria** del producto terminado (`249`). Si tu cápsula lleva
500 mg de extracto dual al 26,9 %, entrega 134,5 mg de beta-glucano; si llevara extracto acuoso al 32,4 %,
entregaría 162 mg, pero cero triterpenos.

## Errores comunes

- **Creer que "dual" es automáticamente mejor.** Depende de qué activo sostiene tu claim. Para un producto
  que se vende por beta-glucano, el dual puede ser un paso atrás.
- **Extraer con etanol y decir que el producto "tiene beta-glucanos".** Los tiene en una fracción pequeña.
  Es la mentira más común del sector de tinturas.
- **Hervir a fuego abierto sin control de tiempo/temperatura.** No es reproducible entre lotes; tu
  especificación queda imposible de cumplir (`247`).
- **No analizar el marc.** Es la forma más barata de saber si estás perdiendo la mitad del activo.
- **Usar etanol desnaturalizado con metanol o IPA en producto de consumo.** Problema regulatorio y
  toxicológico (`87-solventes-residuales.md`).
- **Reportar "polisacáridos totales" y llamarlos beta-glucanos.** Ese ensayo mide también almidón (`222`).

## Conexión con otros módulos

→ `144-extraccion-acuosa-y-decoccion.md` y `145-extraccion-hidroalcoholica-y-tinturas.md` — el detalle de
cada ruta.
→ `146-extraccion-dual-y-por-que-importa.md` — el dueño del concepto de dual.
→ `242-ratios-de-extraccion-y-etiquetado-honesto.md` — cómo se declara todo esto sin mentir.
→ `221-medir-beta-glucanos-metodo-megazyme.md` y `224-triterpenos-ganodericos-analisis.md` — los métodos.
→ `20-parametros-de-solubilidad-y-eleccion-de-solvente.md` — por qué cada solvente saca lo que saca.
→ `249-dosificacion-de-hongos-funcionales.md` — del porcentaje a los mg por porción.
