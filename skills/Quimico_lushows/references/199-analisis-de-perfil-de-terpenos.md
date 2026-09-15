# 199 — Análisis de perfil de terpenos (el dato que más se pierde y más se inventa)

Los terpenos son lo que hace que una variedad huela a limón, a pino o a gasolina, y son el argumento
comercial favorito del cannabis moderno. También son el analito más frágil del panel: **se evaporan durante
el secado, el curado, el almacenamiento, la molienda y hasta durante la preparación de la muestra**. Si el
método no está diseñado para retenerlos, el laboratorio te va a reportar un perfil que no es el de tu
producto sino el de lo que sobrevivió a tu proceso analítico. Y como el perfil se paga, es también donde más
se reintroduce terpeno botánico sin declararlo.

Términos: **monoterpeno (monoterpene)** = 10 carbonos, muy volátil (mirceno, limoneno, pineno).
**Sesquiterpeno (sesquiterpene)** = 15 carbonos, menos volátil (β-cariofileno, humuleno). **Headspace
(espacio de cabeza)** = inyectar el vapor sobre la muestra en vez del líquido. **Terpenos totales (total
terpenes)** = suma del panel, en % p/p o mg/g.

## Por qué se pierden y cuánto

| Etapa | Pérdida reportada en la literatura | Mecanismo |
|---|---|---|
| Secado con calor (> 25 °C) | Alta, sobre todo monoterpenos | Volatilización |
| Curado prolongado | Progresiva | Volatilización + oxidación |
| Molienda a temperatura ambiente | Notoria | Calor de fricción y superficie expuesta |
| Extracción térmica / destilación | Prácticamente total | Los terpenos salen antes que los cannabinoides |
| Almacenamiento en envase permeable | Progresiva | Difusión a través del plástico |

No pongas cifras específicas de pérdida sin tu propio dato: la magnitud depende de la variedad, la
temperatura y el tiempo. Lo que sí es sólido es el **orden**: los monoterpenos se van primero, los
sesquiterpenos aguantan más. Por eso un extracto viejo tiene perfil desplazado hacia cariofileno y humuleno
aunque la flor original fuera dominante en mirceno.

## El método: GC, y con headspace si se puede

| Enfoque | Cómo funciona | Ventaja | Limitación |
|---|---|---|---|
| GC-FID con inyección líquida | Se extrae con solvente y se inyecta | Barato, cuantitativo, robusto | Solvente puede coeluir; no distingue isómeros |
| GC-MS con inyección líquida | Igual, con detector de masas | Identificación por espectro y biblioteca | Más caro |
| HS-GC-MS (static headspace) | Se calienta el vial y se inyecta el vapor | Sin solvente, muy limpia | Sesga hacia lo más volátil |
| HS-SPME-GC-MS | Fibra que adsorbe del espacio de cabeza | Muy sensible | Cuantificación difícil sin estándar interno |
| GCxGC-TOF | Dos dimensiones cromatográficas | Resuelve isómeros de verdad | Equipo y personal caros |

Para un COA comercial, **GC-FID o GC-MS con inyección líquida y estándar interno** es lo estándar. Para
investigación de perfil fino (distinguir enantiómeros de limoneno, por ejemplo) hace falta columna quiral o
GCxGC.

Un detalle que separa métodos serios de los demás: **el estándar interno (internal standard)**. Como los
terpenos se pierden en cada paso, sin estándar interno no puedes corregir la pérdida durante la preparación.
Se usan compuestos que no están en cannabis, por ejemplo n-tridecano o 4-fluorotolueno, añadidos al inicio
(ver `72`).

## El panel: cuántos y cuáles

Un panel comercial típico a agosto de 2026 va de 15 a 40 terpenos. Los que casi siempre están:

`α-pineno · β-pineno · mirceno · limoneno · ocimeno · terpinoleno · linalool · β-cariofileno · α-humuleno ·
α-terpineol · fenchol · borneol · eucaliptol (1,8-cineol) · nerolidol · guaiol · óxido de cariofileno ·
bisabolol · valenceno`

Advertencia de nomenclatura: **el óxido de cariofileno es producto de oxidación**, no un terpeno primario de
la planta fresca. Un perfil con óxido de cariofileno alto respecto al β-cariofileno es señal de material
oxidado o viejo. Es de los indicadores de frescura más útiles que existen y casi nadie lo mira.

## Cómo se mide / cómo se comprueba

Lo que le exiges al laboratorio, punto por punto:

1. **Técnica y modo de inyección** (líquida o headspace) y temperatura del inyector.
2. **Lista completa del panel** con LOQ individual en % p/p o mg/g, no solo los que "salieron".
3. **Estándar interno usado** y recuperación demostrada.
4. **Cómo se preparó la muestra**: si molieron la flor a temperatura ambiente, ya perdiste monoterpenos antes
   de inyectar. Lo correcto es molienda criogénica o pesar la flor entera en el vial.
5. **Base del resultado** y humedad (ver `07`).
6. **Suma de terpenos totales** y coherencia: la suma de los individuales debe dar el total reportado.

Y una comprobación de sentido común que detecta muchos reportes malos: **si el mismo COA reporta terpenos
altos en un destilado**, algo no cuadra, porque la destilación se los lleva. Si están, fueron
reintroducidos — lo cual es legítimo, pero debe declararse (ver `194`).

## Distinguir terpeno de cannabis de terpeno botánico

Esta es la pregunta comercial cara: ¿los terpenos de este producto vienen de la planta o los compraron?

- **Relación de isómeros / enantiómeros.** El limoneno del cannabis es predominantemente el enantiómero
  (R)-(+); el de fuentes cítricas industriales también, así que este marcador por sí solo no cierra el caso,
  pero una mezcla racémica sí delata origen sintético. Requiere columna quiral.
- **Presencia de marcadores exclusivos.** Terpenos poco frecuentes en fuentes botánicas comerciales que sí
  aparecen en cannabis apoyan el origen natural.
- **Coherencia con el perfil de cannabinoides.** Un producto con terpenos "de flor" y cero cannabinoides
  menores es sospechoso.
- **Análisis isotópico (IRMS, isotope ratio mass spectrometry).** El método más contundente para origen
  natural frente a sintético, pero caro y con pocos laboratorios que lo ofrezcan.

## Ejemplo aplicado (ILUSTRATIVO)

Misma variedad, dos momentos:

| Terpeno | Flor recién curada (mg/g) | Misma flor a 9 meses (mg/g) |
|---|---|---|
| Mirceno | 6,8 | 2,1 |
| Limoneno | 3,2 | 1,0 |
| α-Pineno | 1,4 | 0,3 |
| β-Cariofileno | 4,1 | 3,4 |
| α-Humuleno | 1,5 | 1,3 |
| Óxido de cariofileno | 0,3 | 1,6 |
| **Total** | **17,3** | **9,7** |

Cifras **(ILUSTRATIVO)**. Dos lecturas: (1) perdió 44 % de terpenos totales, casi todo de la fracción
monoterpénica; (2) la relación óxido de cariofileno / β-cariofileno pasó de 0,07 a 0,47, que es la firma
química de la oxidación. Si tu etiqueta declara "3 % de terpenos totales", este producto ya no la cumple —
y eso es una discrepancia de etiqueta, no una opinión sobre el olor.

## Errores comunes

- **Declarar en la etiqueta el perfil del análisis inicial** y no revalidarlo a fin de vida útil. Los
  terpenos se van; el número declarado tiene que ser sostenible durante la vida útil.
- **Analizar terpenos por el mismo método que la potencia.** Son técnicas distintas: HPLC para cannabinoides,
  GC para terpenos.
- **Moler la muestra en caliente antes de analizar** y culpar al cultivo del resultado bajo.
- **Reintroducir terpenos botánicos y no declararlo.** Es adulteración, y además un tema de alérgenos:
  linalool y limoneno son alérgenos de declaración obligatoria en cosméticos en la UE.
- **Reportar solo los terpenos detectados.** Sin el panel completo con sus LOQ no se sabe qué se buscó y no
  se encontró.
- **Confundir "terpenos totales" del COA de flor con el del extracto.** Bases y matrices distintas.

## Conexión con otros módulos

→ `182-terpenos-del-cannabis.md` — quiénes son y qué se sabe de cada uno.
→ `183-efecto-sequito-que-dice-la-evidencia.md` — qué sostiene la evidencia sobre la sinergia.
→ `85-cromatografia-de-gases.md` y `86-gc-ms-y-headspace.md` — el instrumento.
→ `72-estandar-interno-y-adicion-de-estandar.md` — por qué sin estándar interno el dato se cae.
→ `186-cosecha-secado-y-curado.md` — dónde se pierden en el proceso.
→ `213-como-leer-un-coa-de-cannabis.md` — cómo se lee la sección de terpenos del certificado.