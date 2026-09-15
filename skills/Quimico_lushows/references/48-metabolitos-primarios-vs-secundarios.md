# 48 — Metabolitos primarios vs secundarios (qué de tu materia prima es "activo" y qué es relleno)

Un hongo o una planta fabrican dos clases de moléculas: las que necesitan para vivir (metabolitos primarios:
azúcares, proteínas, lípidos, ácidos nucleicos) y las que fabrican para defenderse, competir o comunicarse
(metabolitos secundarios: cannabinoides, terpenos, alcaloides, triterpenos, polifenoles). Casi todo lo que
vale dinero en tu producto es secundario, y casi todo lo que pesa es primario. Confundirlos es exactamente
el mecanismo del fraude del micelio en grano: te venden almidón —metabolito primario del arroz— y lo cobran
como si fuera β-glucano de hongo.

Términos: **metabolito primario (primary metabolite)** = esencial para crecer y reproducirse; universal.
**Metabolito secundario (secondary metabolite / specialized metabolite)** = no esencial para el crecimiento;
específico de taxón; suele ser el activo. **Rendimiento metabólico (metabolic yield)** = cuánto secundario
produce el organismo por unidad de biomasa. **Elicitor** = estímulo (estrés, luz, herida) que dispara la
producción de secundarios.

## La diferencia, en tabla

| Criterio | Primarios | Secundarios |
|---|---|---|
| Función | Sobrevivir, crecer | Defensa, competencia, señal |
| Distribución | En todos los seres vivos | Específicos de género/especie |
| Cantidad | % altos: 20–80 % p/p de la biomasa | Trazas a pocos %: mg/g a decenas de mg/g |
| Variabilidad | Baja | **Alta**: cambia con sustrato, luz, estrés, etapa |
| Valor comercial | Bajo (relleno, calorías) | Alto (el "activo") |
| Ejemplos en hongo | Almidón, quitina, proteína, β-glucano estructural | Ácidos ganodéricos, hericenonas, cordicepina, psilocibina |
| Ejemplos en cannabis | Celulosa, almidón, proteína, aceites de semilla | Cannabinoides, terpenos, flavonoides |
| Uso analítico | Composición proximal | Potencia y quimiotaxonomía (`60`) |

Matiz importante y honesto: **el β-glucano fúngico está en la frontera**. Es estructural de la pared
celular —o sea, primario— pero su estructura β-(1→3),(1→6) es característica del reino Fungi y es lo que se
usa como marcador de "hongo real". Se comporta como marcador de identidad más que como activo raro (`52`).

## Composición típica de una biomasa fúngica seca

Órdenes de magnitud reportados en la literatura para cuerpo fructífero seco; **verificar con tu lote**:

```
Carbohidratos totales      ~ 40–60 % p/p base seca   (primarios; incluye glucanos y quitina)
  de los cuales β-glucano  ~ 10–40 % p/p             (según especie, parte y método, `221`)
Proteína (N × 4,38*)       ~ 15–35 % p/p
Fibra                      ~ 5–20 % p/p
Lípidos                    ~ 1–8 % p/p
Cenizas (minerales)        ~ 5–12 % p/p
Metabolitos secundarios    ~ 0,1–5 % p/p             ← el ACTIVO por el que pagas

*Nota: en hongos se usa factor 4,38 y no 6,25 porque parte del nitrógeno viene de la quitina,
 no de proteína. Usar 6,25 SOBREESTIMA la proteína. Es un error clásico en fichas técnicas.
```

Lectura del negocio: si te venden "extracto de reishi" por su contenido de carbohidratos, te están cobrando
el relleno. Si te lo venden por ácidos ganodéricos cuantificados por HPLC-DAD con patrón, te están cobrando
el activo (`224`).

## Por qué los secundarios varían tanto (y qué hacer con eso)

Los secundarios responden al ambiente. Esto no es una molestia: es la palanca de control del proceso.

| Factor | Efecto reportado | Módulo |
|---|---|---|
| Sustrato de cultivo | Cambia el perfil completo; grano deja almidón residual | `239`, `218` |
| Parte usada (micelio vs fructífero) | Perfiles distintos: erinacinas en micelio, hericenonas en fructífero | `217`, `226` |
| Etapa de cosecha | Cannabinoides y terpenos cambian con la madurez | `186` |
| Luz/UV | Aumenta fenoles; convierte ergosterol en vitamina D2 | `236` |
| Estrés hídrico o térmico | Puede subir secundarios de defensa | `185` |
| Secado y curado | Pérdidas de volátiles y descarboxilación | `186`, `240` |

Consecuencia dura para especificaciones: **un solo lote no define un rango**. Se necesitan varios lotes
(idealmente ≥ 3, mejor 6) para construir una especificación defendible (`282`).

## Cómo se mide cada cosa

| Fracción | Método | Unidad | Comentario |
|---|---|---|---|
| Humedad | Karl Fischer o estufa 105 °C | % p/p | Base para todo lo demás (`07`, `98`) |
| Proteína | Kjeldahl o Dumas × 4,38 (hongos) | % p/p base seca | El factor importa |
| Grasa | Soxhlet / hidrólisis ácida | % p/p base seca | |
| Cenizas | Calcinación 550 °C | % p/p base seca | Alta = mucho sustrato mineral |
| Fibra dietaria | AOAC 991.43 / 2009.01 | % p/p base seca | |
| **β-glucano** | Megazyme K-YBGL (enzimático) | % p/p base seca | Total − α (`221`) |
| **α-glucano (almidón)** | Incluido en K-YBGL | % p/p base seca | **La bandera del fraude** (`220`) |
| Triterpenos ganodéricos | HPLC-DAD ~245–255 nm | mg/g o % p/p | Con patrón (`224`) |
| Cannabinoides | HPLC-DAD con patrones | % p/p base seca | (`198`) |
| Terpenos | GC-MS / GC-FID headspace | mg/g o ppm | (`199`) |
| Alcaloides indólicos | HPLC-UV o LC-MS/MS | mg/g base seca | (`256`) |

## Ejemplo aplicado — leer una ficha técnica de "extracto de melena de león"

```
Ficha del proveedor (ILUSTRATIVO):
  "Polisacáridos ≥ 30 %"   ·   "Proteína 22 %"   ·   "Extracto 10:1"   ·   Precio bajo

Traducción química:
  · "Polisacáridos 30 %" mide PRIMARIOS y no distingue almidón de β-glucano (`222`).
  · Proteína 22 % calculada probablemente con factor 6,25 → sobreestimada para hongo.
  · "10:1" es una relación de MASA de proceso, no de potencia (`151`, `242`).
  · No hay un solo metabolito SECUNDARIO cuantificado.

Lo que hay que exigir para poder comparar:
  1. β-glucano y α-glucano por Megazyme K-YBGL, en % p/p base seca, con el informe del laboratorio.
  2. Identidad de especie por ITS (`245`), y declaración de PARTE usada (fructífero vs micelio, `217`).
  3. Hericenonas por HPLC (fructífero) o erinacinas (micelio), en mg/g base seca (`226`).
  4. Humedad, para poder pasar todo a base seca y comparar entre proveedores (`07`).
Sin esos cuatro datos, dos ofertas no son comparables ni por precio ni por calidad.
```

## Errores comunes

- Comprar por "% de polisacáridos" y creer que se compró actividad. Es el error más caro del sector (`222`).
- Usar el factor 6,25 para calcular proteína en hongos e inflar el valor nutricional en la etiqueta.
- Tratar la variabilidad de secundarios como defecto del laboratorio en vez de biología: se controla con
  especificación por rango y muestreo correcto (`66`, `282`).
- Comparar valores entre proveedores sin llevar todo a base seca.
- Suponer que más biomasa = más activo. Un cultivo rápido en grano da mucha masa y pocos secundarios (`218`).
- Declarar en etiqueta un metabolito secundario que no se mide por lote. Si no se mide, no se declara (`283`).

## Conexión con otros módulos

→ `52-polisacaridos-y-glucanos.md` — el detalle estructural que separa hongo de cereal y de almidón.
→ `49-terpenos-y-terpenoides.md` y `50-alcaloides.md` — las dos grandes familias de secundarios.
→ `58-rutas-biosinteticas-mevalonato-y-mep.md` — de dónde salen los secundarios.
→ `60-quimiotaxonomia-y-marcadores.md` — usar secundarios para probar identidad.
→ `218-el-fraude-del-micelio-en-grano.md` — el caso completo del fraude.
