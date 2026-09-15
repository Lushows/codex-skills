# 224 — Triterpenos ganodéricos: cómo se analizan de verdad

Los triterpenos son la segunda mitad del reishi y el marcador que más se declara mal. Hay dos maneras de
poner un número de "triterpenos" en una ficha: una colorimetría barata e inespecífica, y una cromatografía
con patrones. Dan resultados que pueden diferir en un orden de magnitud, y casi nadie aclara cuál usó. Si
vas a pagar más por un extracto dual "rico en triterpenos", este módulo es el que te dice si estás pagando
por moléculas o por color.

Términos: **triterpeno (triterpene)** = esqueleto de 30 carbonos de la ruta del mevalonato. **ácido
ganodérico (ganoderic acid)** = triterpeno oxigenado de *Ganoderma*, con función ácida; hay decenas
(A, B, C2, D, F, H...). **lucidénico (lucidenic acid)** = serie relacionada, de 27 carbonos.
**HPLC-DAD (diode array detector)** = cromatografía líquida con detector de arreglo de diodos.
**patrón de referencia (reference standard)** = molécula pura certificada contra la cual se cuantifica.

## Los dos métodos que se llaman igual y no son lo mismo

| | Triterpenos totales (colorimétrico) | Ácidos ganodéricos (HPLC/LC-MS) |
|---|---|---|
| Principio | Reacción con vainillina–ácido perclórico o ácido sulfúrico; se lee color | Separación cromatográfica y cuantificación por patrón |
| Se expresa como | "Equivalentes de ácido oleanólico" o de ácido ursólico | Cada ácido ganodérico por su nombre, o suma de los identificados |
| Especificidad | Baja: responden muchos terpenoides y esteroles | Alta |
| Costo | Bajo | Medio-alto |
| Uso legítimo | Seguimiento de proceso, comparación interna | Especificación, control de lote, expediente |

La consecuencia práctica está en los números publicados: un mismo conjunto de materiales de *Ganoderma*
mostró triterpenos totales entre **0,21 % y 10,56 %**, mientras la cuantificación por LC-MS/MS dirigida a
ácidos ganodéricos concretos dio **0,01 % a 0,98 %** (literatura de caracterización de *Ganoderma*
recogida en revisiones de calidad; ver también el trabajo de HPLC-DAD citado abajo). No es que un método
mienta: es que miden cosas distintas. Reportar el 10,56 % como si fueran ácidos ganodéricos sí sería mentir.

## El método cromatográfico de referencia

Existen métodos HPLC-DAD validados para *Ganoderma*. Uno mejorado para comparación cuantitativa de
triterpenos en *G. lucidum* y cinco especies relacionadas de Vietnam cuantifica **14 constituyentes
triterpénicos**: nueve ácidos ganodéricos, cuatro alcoholes triterpénicos y un esterol (ergosterol)
(*Molecules* / PMC6272446, 2015). Otro método HPLC determina **nueve ácidos triterpenoides** de
*G. lucidum* de distintas zonas de producción (*Zhongguo Zhong Yao Za Zhi*, 2013; PubMed 23477148).

Condiciones típicas (orden de magnitud, ajusta con tu laboratorio):

```
Columna:      C18, 4,6 x 250 mm, 5 um  (o C18 sub-2 um en UHPLC)
Fase movil:   A = agua acidificada (acido acetico o formico 0,1 %)
              B = acetonitrilo o metanol
Elucion:      gradiente; los acidos ganodericos son moleculas medianamente polares
Deteccion:    DAD a ~252-257 nm (cromoforo dienona de la serie ganoderica)
Confirmacion: LC-MS/MS en modo negativo [M-H]- para identidad inequivoca
Patrones:     acido ganoderico A como minimo; idealmente A, B, C2, D, F, H
```

**Sin patrón no hay cuantificación, solo estimación** (ver `70`). Los patrones de ácidos ganodéricos son
caros y de disponibilidad limitada; ese es el motivo económico real por el que la industria sigue usando
colorimetría.

## Preparación de muestra

1. Molienda fina y homogénea del material seco (`67`).
2. Extracción con metanol o etanol (frecuentemente con ultrasonido o reflujo); los triterpenos no salen en
   agua (ver `241`).
3. Filtración por 0,22 µm antes de inyectar.
4. Si la matriz es sucia (extracto con excipientes), limpieza por SPE (`69`).
5. Humedad en paralelo para reportar en base seca (`98`, `07`).

## Qué debe decir el informe

| Renglón | Unidad |
|---|---|
| Método (colorimétrico o HPLC/LC-MS) y referencia | texto |
| Patrón usado y su certificado | texto |
| Cada ácido ganodérico cuantificado, o "suma de N identificados" | `mg/g` o `% p/p base seca` |
| Si es colorimétrico: "expresado como equivalentes de ácido oleanólico" | `% p/p base seca` |
| Humedad y base | `% p/p` |
| LOD/LOQ del método | `mg/g` (`73`) |

Un informe que diga solo "triterpenos 4 %" sin decir cuál de los dos métodos usó no sirve para una
especificación.

## Ejemplo aplicado — comparar dos ofertas de extracto dual

**(ILUSTRATIVO)**

```
Oferta 1: "Reishi dual extract, 6 % triterpenos"
   Al pedir el metodo: vainillina-acido perclorico, como equivalentes de acido oleanolico.
   Traduccion: 6 % de "cosas que reaccionan", no 6 % de acidos ganodericos.

Oferta 2: "Reishi dual extract, 1,2 % acidos ganodericos (suma de 6, HPLC-DAD)"
   Traduccion: 1,2 % de moleculas identificadas y cuantificadas contra patron.

La oferta 2 tiene el numero mas bajo y el producto probablemente mejor documentado.
Comparar 6 contra 1,2 es comparar peras con manzanas.
```

Ese es el mismo patrón mental de `222` con los polisacáridos: el número grande e inespecífico gana la
licitación y pierde la auditoría.

## Qué se puede y qué no se puede afirmar

- Se puede declarar: "triterpenos 2,0 % p/p base seca, expresados como ácido ganodérico A por HPLC-DAD".
- Se puede describir el amargor como característica organoléptica asociada a la fracción triterpénica.
- No se puede atribuir a los triterpenos ninguna acción sobre enfermedades. La literatura de ácidos
  ganodéricos es mayoritariamente `[in vitro]`, con algo de `[animal]` y farmacocinética exploratoria
  (por ejemplo, evaluación farmacocinética y de estabilidad de una fracción enriquecida en ácido ganodérico
  H, *Frontiers in Pharmacology* / PMC8876931, 2022). Nada de eso autoriza un claim de enfermedad
  (ver `268`, `276`).

## Errores comunes

- Aceptar "triterpenos totales" como si fueran ácidos ganodéricos.
- Comparar porcentajes de triterpenos entre proveedores sin igualar el método.
- Extraer solo con agua y luego declarar triterpenos: no están ahí (`146`).
- Cuantificar sin patrón, usando el área del pico "más grande" como si fuera ácido ganodérico A.
- No reportar LOD/LOQ: en extractos pobres, "no detectado" puede ser un límite de método alto (`73`).

## Conexión con otros módulos

→ `223-reishi-ganoderma-quimica.md` — el contexto de la especie.
→ `55-esteroles-y-triterpenos.md` — química de la familia.
→ `79-hplc-y-uhplc.md` y `83-lc-ms-ms-y-mrm.md` — las técnicas.
→ `70-patrones-de-referencia-y-trazabilidad.md` — por qué sin patrón no hay número.
→ `146-extraccion-dual-y-por-que-importa.md` — cómo se saca esta fracción.