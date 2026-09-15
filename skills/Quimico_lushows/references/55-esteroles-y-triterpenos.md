# 55 — Esteroles y triterpenos (ácidos ganodéricos y ergosterol: los dos números serios del reishi)

Si el β-glucano prueba que hay hongo, los **triterpenos** prueban qué hongo y qué tan bien se extrajo. En
reishi (*Ganoderma lucidum*) la fracción amarga —los **ácidos ganodéricos**— es soluble en alcohol y no en
agua: por eso existe la extracción dual y por eso un extracto solo acuoso no puede declarar triterpenos. El
**ergosterol**, por su parte, es el esterol de la membrana fúngica y funciona como marcador de biomasa
real de hongo y como precursor de vitamina D2 bajo UV. Estos dos analitos son los que separan una
especificación de reishi seria de una hoja de folleto.

Términos: **triterpeno (triterpene)** = terpeno de 30 carbonos (`49`). **Lanostano (lanostane)** = esqueleto
tetracíclico C30 del que derivan los ácidos ganodéricos. **Esterol (sterol)** = triterpeno modificado, con
esqueleto de ciclopentanoperhidrofenantreno y OH en C3. **Insaponificable (unsaponifiable)** = fracción del
lípido que no se hidroliza con base; ahí viven los esteroles. **Aglicona / forma libre vs esterificada** =
el esterol puede estar libre o unido a un ácido graso.

## Ergosterol: el esterol de los hongos

| Propiedad | Valor |
|---|---|
| Nombre químico | (22*E*)-ergosta-5,7,22-trien-3β-ol |
| CAS | 57-87-4 |
| Fórmula / M | C₂₈H₄₄O / 396,65 g/mol |
| λ máx UV | ~282 nm (con hombros a ~271 y ~293 nm — patrón del dieno conjugado 5,7) |
| Estabilidad | Fotolábil y oxidable: proteger de luz y O₂ (`47`) |
| Rol biológico | Esterol de membrana fúngica; equivalente al colesterol animal |
| Uso analítico | **Marcador de biomasa fúngica real** y de vitamina D2 potencial |

Dos usos que valen dinero:

1. **Marcador de biomasa fúngica.** Los cereales y el sustrato **no** tienen ergosterol. Medir ergosterol en
   un polvo permite estimar cuánta masa fúngica hay de verdad, y cruzarlo con el α-glucano (que delata el
   grano) da una imagen muy difícil de falsificar (`238`, `218`, `220`).
2. **Precursor de vitamina D2.** Bajo luz UV-B, el anillo B del ergosterol se abre fotoquímicamente a
   previtamina D2 y esta isomeriza térmicamente a **ergocalciferol (vitamina D2)**. Es la base del
   tratamiento UV de hongos. El proceso se declara y se mide; no se asume (`236`, `57`).

## Ácidos ganodéricos: la fracción amarga del reishi

Son triterpenoides de tipo **lanostano** altamente oxigenados (cetonas, hidroxilos, un -COOH). Se han
descrito más de un centenar de estructuras en *Ganoderma*; el de referencia comercial es el **ácido
ganodérico A** (C₃₀H₄₄O₇, 516,67 g/mol, CAS 81907-62-2).

| Característica | Consecuencia práctica |
|---|---|
| Muy oxigenados, con -COOH | Solubles en etanol; poco solubles en agua fría |
| Cetona conjugada en el anillo | Absorben UV a **~245–255 nm** → cuantificables por HPLC-DAD |
| Sabor muy amargo | El amargor es un indicador cualitativo (no cuantitativo) de su presencia |
| Perfil muy variable | Depende de cepa, sustrato, madurez y parte (`239`) |
| Ausentes en micelio joven en grano | Otro discriminante frente al fraude |

**La consecuencia de negocio, dicha claro:** una extracción **solo acuosa** (decocción) rinde β-glucanos y
casi nada de triterpenos; una extracción **solo alcohólica** rinde triterpenos y casi nada de β-glucanos.
Por eso existe la **extracción dual** y por eso un producto que declare ambos debe demostrar ambos por
método analítico, no por narrativa (`146`, `241`).

## Cómo se miden

```
ERGOSTEROL — esquema (ILUSTRATIVO; validar en tu matriz, `75`)
  1. Muestra seca, molida, humedad conocida (`07`, `67`)
  2. SAPONIFICAR (imprescindible: parte está esterificada, `46`):
     KOH metanólico ~1 M, 70–80 °C, 30–60 min, con BHT y bajo N₂, protegido de la luz
  3. Extraer el insaponificable con hexano (3 ciclos)
  4. Evaporar suave, reconstituir en metanol, filtrar 0,22 µm
  5. HPLC-UV/DAD 282 nm, C18, metanol ~100 % isocrático; patrón de ergosterol certificado
  6. Curva de 5 puntos, control de recuperación con adición de patrón (`74`)
  Reporte: mg/g base seca. Órdenes de magnitud reportados en literatura: décimas a unidades de mg/g.

ÁCIDOS GANODÉRICOS — dos niveles de rigor
  A) "Triterpenos totales" por colorimetría (vainillina-ácido perclórico), expresado como equivalentes de
     ácido oleanólico → BARATO e INESPECÍFICO. Sirve para control interno, NO para etiqueta.
  B) HPLC-DAD 245–255 nm con patrón de ácido ganodérico A (y B, C2, D si los tienes) →
     cuantificación específica, reporte en mg/g o % p/p base seca, "expresado como ácido ganodérico A".
  Confirmación de identidad: LC-MS/MS o HRMS (`83`, `84`).
```

Regla de reporte: siempre **"expresado como <patrón>"**. Sin esa frase, el número de "triterpenos totales"
no es interpretable ni comparable entre proveedores.

## Otros triterpenos y esteroles del portafolio

| Compuesto | Fuente | Rol |
|---|---|---|
| Ácidos lucidénicos | *Ganoderma* | Familia hermana de los ganodéricos |
| **Betulina / ácido betulínico** | Chaga sobre abedul | Vienen del árbol, no del hongo: marcador de sustrato (`229`, `60`) |
| Inotodiol, lanosterol | Chaga | Triterpenos propios |
| β-sitosterol, campesterol | Plantas, cannabis | Fitoesteroles; sirven como marcadores de origen vegetal |
| Ácido oleanólico / ursólico | Plantas | Patrón usado como "equivalente" en colorimetría |

## Ejemplo aplicado — especificación de un extracto dual de reishi

```
ESPECIFICACIÓN (ILUSTRATIVO — los rangos se fijan con ≥3 lotes reales, `282`)
  Identidad de especie      : Ganoderma lucidum confirmado por ITS (`245`)
  Parte                     : cuerpo fructífero (declarado y verificable)
  Humedad (Karl Fischer)    : ≤ 7,0 % p/p
  β-glucano (K-YBGL)        : ≥ 25,0 % p/p base seca
  α-glucano (K-YBGL)        : ≤ 5,0 % p/p base seca   ← control anti-sustrato (`220`)
  Ácidos ganodéricos totales: ≥ 2,0 % p/p base seca, expresado como ácido ganodérico A, HPLC-DAD 254 nm
  Ergosterol                : reportar, mg/g base seca, HPLC-UV 282 nm tras saponificación
  Metales pesados           : Pb, Cd, As, Hg dentro de límites aplicables (`243`)
  Microbiología             : según la especificación de producto (`100`)
  Solventes residuales      : etanol dentro de ICH Q3C clase 3 (`87`)

Lo que este documento logra: cualquier lote se acepta o se rechaza con datos, no con confianza.
Lo que NO incluye: ninguna afirmación sobre efectos en salud (`268`).
```

## Errores comunes

- Medir ergosterol sin saponificar y subestimarlo, porque parte estaba esterificada (`46`).
- Declarar "triterpenos 30 %" por colorimetría de vainillina. Ese método sobreestima y no es específico;
  además nunca dice contra qué patrón se expresó.
- Prometer triterpenos en un extracto acuoso. Químicamente no pueden estar en cantidad relevante.
- Confundir betulina de chaga con un triterpeno fúngico: viene del abedul, y su presencia dice cosas sobre el
  origen, no sobre la calidad del hongo (`60`).
- Exponer los extractos de ergosterol a la luz durante la preparación y perder analito antes de inyectar.
- Comparar "triterpenos totales" entre proveedores con métodos distintos. No son el mismo número.
- Suponer que amargor alto = triterpenos altos. Es una pista sensorial, no una medición.

## Conexión con otros módulos

→ `238-ergosterol-como-marcador.md` — el módulo dueño del ergosterol como marcador.
→ `224-triterpenos-ganodericos-analisis.md` — el método completo para reishi.
→ `236-vitamina-d2-y-tratamiento-uv.md` — la conversión fotoquímica y cómo se declara.
→ `146-extraccion-dual-y-por-que-importa.md` — por qué hacen falta agua y alcohol.
→ `58-rutas-biosinteticas-mevalonato-y-mep.md` — de dónde vienen todos los triterpenos.