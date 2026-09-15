# 60 — Quimiotaxonomía y marcadores (confirmar la especie por su química, y dónde se acaba el truco)

La quimiotaxonomía es clasificar organismos por los compuestos que producen: si esta muestra tiene ácidos
ganodéricos, es muy probable que sea *Ganoderma*; si no tiene ergosterol, probablemente ni siquiera es un
hongo. Te sirve para tres cosas concretas: confirmar que el proveedor te mandó lo que dijo, detectar mezclas
y adulteraciones, y sostener la identidad del ingrediente en un expediente técnico. El error caro que evita
es el más común del sector: aceptar la identidad de una materia prima porque lo dice la bolsa. Pero también
tiene un techo duro, y este módulo lo dice sin adornos: **la química sugiere la especie; el ADN la confirma.**

Términos: **marcador quimiotaxonómico (chemotaxonomic marker)** = metabolito cuya presencia/ausencia o
proporción es característica de un taxón. **Quimiotipo (chemotype)** = variante de una misma especie que
difiere en su perfil químico (el caso clásico es cannabis). **Huella química (chemical fingerprint)** =
patrón cromatográfico completo usado como un todo, no un solo pico. **Marcador de identidad vs marcador de
actividad** = uno prueba qué es; el otro prueba cuánto activo tiene. **No son el mismo número.**

## Qué hace bueno a un marcador

| Criterio | Qué significa | Contraejemplo típico |
|---|---|---|
| Específico del taxón | No lo produce medio reino | "Polisacáridos": los tiene hasta el arroz (`222`) |
| Estable al proceso | Sobrevive secado, extracción y almacenamiento | Terpenos volátiles: se van con el secado (`61`) |
| Medible con método común | HPLC-UV, LC-MS/MS, GC-MS | Un marcador que solo se ve por RMN de 800 MHz no sirve en rutina |
| Con patrón de referencia disponible | Se puede cuantificar de verdad | Muchas erinacinas no tienen estándar comercial barato (`70`) |
| Difícil de falsificar barato | Añadirlo cuesta más que el fraude | Adulterar con cafeína o con almidón es barato (`246`) |

Un marcador que falla el primer criterio no es marcador: es decoración del COA.

## Los marcadores que de verdad se usan

| Material | Marcador de identidad | Técnica | Orden de magnitud reportado | Qué NO prueba |
|---|---|---|---|---|
| Cualquier hongo | **Ergosterol** (esterol de membrana fúngica) | HPLC-UV 282 nm o GC-MS con sililación (`64`) | Cientos de mg/kg a unos pocos mg/g, según especie y parte (`238`) | No distingue especies entre sí |
| *Ganoderma lucidum* / *sinense* | **Ácidos ganodéricos** (triterpenos) y su patrón | HPLC-DAD 245–254 nm, LC-MS/MS | Muy variable por parte y cepa (`224`) | No distingue *G. lucidum* de otros *Ganoderma* con seguridad |
| *Cordyceps militaris* | **Cordicepina** (3'-desoxiadenosina) | HPLC-UV 260 nm / LC-MS/MS (`228`) | Presente en *C. militaris*; en *O. sinensis* es baja o ausente | Cordicepina alta no prueba especie: se sintetiza y se puede añadir |
| *Hericium erinaceus* | Hericenonas (fructífero) / erinacinas (micelio) | LC-MS/MS (`226`) | Trazas; muy dependiente de parte y cepa | Ausencia no prueba fraude: el proceso las destruye |
| *Inonotus obliquus* (chaga) | Complejo de melanina + betulina/ácido betulínico (del abedul) | UV-Vis, HPLC (`229`) | Variable | Betulina viene del árbol, no del hongo |
| *Trametes versicolor* | Proteoglicanos PSK/PSP | Cromatografía + proteína (`231`) | — | No es β-glucano puro |
| Hongos comestibles | **Ergotioneína** | LC-MS/MS o HILIC-UV (`235`) | Reportado en el rango de cientos de mg/kg base seca según especie | Marcador de grupo, no de especie |
| *Cannabis sativa* | **Perfil de cannabinoides** = quimiotipo I/II/III | HPLC-DAD (`198`) | Relación THC/CBD define el tipo (`170`) | No distingue variedades ni origen geográfico |
| Cannabis, afinar | Perfil de terpenos (huella) | GC-MS/FID headspace (`199`) | — | Cambia con secado y curado (`186`) |
| Sustrato (fraude) | **α-glucano alto** = grano | Megazyme K-YBGL (`221`) | — | Marcador *negativo*: delata, no identifica |

Regla de lectura: **un marcador presente confirma poco; un marcador ausente cuando debería estar presente
es una bandera roja fuerte.** La ausencia de ergosterol en algo vendido como "extracto de hongo" es
prácticamente diagnóstica de que ahí no hay hongo (`238`).

## El límite frente al ADN — dilo siempre

La química mide **fenotipo**: lo que el organismo expresó bajo ese sustrato, esa temperatura y ese proceso.
El ADN mide **genotipo**: lo que el organismo es. Por eso:

```
Lo que la QUÍMICA puede decir            Lo que solo el ADN (ITS) puede decir
─────────────────────────────            ────────────────────────────────────
"Hay triterpenos tipo ganodérico"        "Es Ganoderma lingzhi y no G. applanatum"
"Hay ergosterol → material fúngico"      "El género y la especie, con % de identidad"
"El α-glucano es 42 % → hay grano"       "Hay ADN de Oryza sativa en la muestra"
"El perfil no cuadra con la especie"     "Hay dos especies mezcladas en el lote"
```

Tres razones por las que la química sola no cierra identidad:

1. **Convergencia:** especies distintas comparten metabolitos. Los ácidos triterpénicos aparecen en varios
   *Ganoderma*; el perfil se solapa.
2. **Plasticidad:** la misma cepa cambia su perfil según sustrato, luz, temperatura y edad (`239`, `185`).
   Un lote "sin marcador" puede ser la especie correcta mal cultivada.
3. **Adición deliberada:** un marcador barato se puede agregar. La cordicepina y la cafeína son ejemplos de
   compuestos que se compran sintéticos (`246`).

Y al revés: el ADN tampoco cierra el negocio, porque **el ADN no te dice cuánto activo hay**, y a veces
sobrevive al proceso aunque el activo no (o al contrario, se degrada en un extracto y no amplifica). La
respuesta profesional es **doble**: ITS para identidad (`245`, `103`) + marcador químico para potencia,
más el perfil de α/β-glucano para detectar sustrato (`221`).

## Cómo se mide — la huella completa, no un pico

Cuando ningún marcador único basta, se usa la **huella química**: se corre el cromatograma en condiciones
fijas y se compara el patrón completo contra un material de referencia auténtico.

```
Protocolo típico de huella (HPLC-DAD o HPTLC):
  1. Material de referencia AUTÉNTICO (voucher botánico/fúngico identificado por ADN)  ← sin esto no hay huella
  2. Método fijo: columna, gradiente, temperatura, longitud de onda, todo congelado
  3. Marcador de sistema (system suitability): tiempo de retención relativo (RRT) y resolución
  4. Comparación: RRT de 6–12 picos característicos + relación de áreas entre picos clave
  5. Criterio de aceptación numérico y escrito, no "se parece"
  6. Quimiometría si hay muchos lotes: PCA / SIMCA para ver el lote que se sale (`105`)
```

HPTLC (`96`) es la versión barata y visual: sirve para identidad rutinaria de entrada de materia prima y es
la que aceptan muchas monografías de farmacopea (`280`). LC-MS de alta resolución (`84`) y metabolómica no
dirigida (`104`) son la artillería pesada cuando hay que probar adulteración.

## Ejemplo aplicado — un lote de "reishi" que huele raro

Datos **(ILUSTRATIVO)** de un lote de extracto recibido:

```
Ergosterol (HPLC-UV 282 nm)      : 0,04 mg/g base seca     ← muy bajo para material fúngico
Triterpenos totales (HPLC-DAD)   : 0,9 % p/p base seca     ← bajo para reishi de fructífero
Perfil de ácidos ganodéricos     : 2 picos de 9 esperados  ← la huella no cuadra
β-glucano (K-YBGL)               : 11,2 % p/p base seca
α-glucano (K-YBGL)               : 38,6 % p/p base seca    ← bandera roja: grano (`218`)
ITS (`245`)                      : no solicitado
```

Diagnóstico: la química ya dice "esto es mayoritariamente sustrato con algo de material fúngico". Lo que la
química **no** puede decir es si el poco hongo que hay es *Ganoderma lucidum*. Decisión: rechazar el lote
por especificación de α/β-glucano (`247`) y pedir ITS solo si se va a discutir identidad con el proveedor.
Rechazar por el dato que ya tienes es más rápido y más barato que ganar la discusión taxonómica.

## Errores comunes

- Usar un marcador de identidad como si fuera de potencia (o al revés). Ergosterol confirma que hay hongo;
  no dice cuánto β-glucano hay.
- Comparar huellas corridas con métodos distintos. Sin el método congelado, la huella no significa nada (`81`).
- Aceptar "análisis organoléptico" o "verificado por experto" como identidad. No es trazable ni auditable.
- Concluir fraude por ausencia de un marcador frágil (hericenonas, terpenos) que el proceso destruye (`61`).
- No tener material de referencia auténtico. Sin el patrón de comparación, la huella es un dibujo bonito (`70`).
- Pedir ITS a un extracto muy procesado sin preguntar antes si hay ADN amplificable: se paga por un "no
  detectado" que no prueba nada (`103`).
- Aceptar un solo lote como prueba del perfil de un proveedor. El perfil se establece con varios (`282`).

## Conexión con otros módulos

→ `103-identidad-por-adn-its-y-barcoding.md` — cómo funciona el barcoding y qué resuelve de verdad.
→ `245-identidad-de-especie-por-its.md` — el módulo dueño de la identidad en hongos.
→ `238-ergosterol-como-marcador.md` — el marcador fúngico universal, en detalle.
→ `224-triterpenos-ganodericos-analisis.md` y `228-cordicepina-y-adenosina-analisis.md` — los métodos.
→ `104-metabolomica-y-huella-quimica.md` y `105-quimiometria-pca-y-modelos.md` — la huella a escala.
→ `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — qué se falsifica y cómo se detecta.
→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — por qué un marcador desaparece sin que haya fraude.
