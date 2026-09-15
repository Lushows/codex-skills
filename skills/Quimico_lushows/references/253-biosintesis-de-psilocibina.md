# 253 — Biosíntesis de psilocibina (cómo la fabrica el hongo, y por qué importa para el análisis)

Saber la ruta biosintética no es curiosidad académica: explica por qué en el mismo material aparecen
baeocistina y norbaeocistina, por qué el contenido varía tanto entre partes del hongo, y por qué la
industria farmacéutica dejó de depender del hongo para producir psilocibina de grado clínico. Este módulo
describe la ruta **a nivel conceptual y enzimático**, que es lo que hace falta para interpretar un
cromatograma y entender la literatura.

**Alcance (línea roja):** esto es bioquímica descriptiva. **No se entregan condiciones de cultivo, medios,
cepas, parámetros de fermentación, procedimientos de expresión heteróloga ni rutas de síntesis química.**
Lo que sigue sirve para leer papers y diseñar análisis, no para producir.

Términos: **descarboxilasa (decarboxylase)** = enzima que quita un CO₂. **kinasa (kinase)** = enzima que
añade un fosfato. **metiltransferasa (methyltransferase)** = enzima que añade grupos metilo, usando SAM.
**SAM (S-adenosil metionina)** = el donante universal de metilos en biología.

## La ruta, de aminoácido a alcaloide

El punto de partida es el **triptófano**, un aminoácido esencial común a todos los seres vivos. Cuatro
enzimas, identificadas y caracterizadas en *Psilocybe cubensis* (Fricke, Blei y Hoffmeister, 2017,
*Angewandte Chemie*), hacen el resto:

```
L-triptófano
    │  PsiD  (descarboxilasa)              → quita el CO₂
    ▼
Triptamina
    │  PsiH  (monooxigenasa P450)          → hidroxila en la posición 4
    ▼
4-hidroxitriptamina
    │  PsiK  (kinasa)                      → fosforila el hidroxilo en 4
    ▼
Norbaeocistina  (4-fosforiloxi-triptamina)
    │  PsiM  (N-metiltransferasa, usa SAM) → primer metilo
    ▼
Baeocistina    (N-metil)
    │  PsiM   (segundo ciclo)              → segundo metilo
    ▼
PSILOCIBINA   (N,N-dimetil)
```

Tres lecturas prácticas de ese esquema:

1. **Baeocistina y norbaeocistina son intermediarios**, no "compuestos exóticos". Aparecen siempre en
   proporción menor porque la ruta tiende a completarse (`252`).
2. **La psilocina no está en la ruta principal.** En el hongo intacto es sobre todo producto de degradación
   por fosfatasas propias y por el procesamiento del material (`255`).
3. **La aeruginascina (trimetilada)** requiere una metilación adicional, presente en algunas especies como
   *Inocybe aeruginascens*; por eso es rara en *Psilocybe*.

Un detalle elegante: el orden fosforilar-antes-de-metilar no es obvio químicamente, pero tiene sentido
biológico — el hongo protege la 4-hidroxitriptamina (que es inestable y reactiva) convirtiéndola de
inmediato en el éster fosfato. Es la misma lógica de estabilidad que explica `255`.

## Por qué el clínico no usa hongos

Desde 2020 hay literatura publicada sobre manufactura de psilocibina a escala de kilogramos bajo cGMP
(por ejemplo, *ACS Omega*, 2020, sobre fosforilación directa de psilocina para producción cGMP). La razón es
regulatoria, no ideológica: un medicamento necesita **una sustancia definida, con impurezas conocidas,
polimorfismo controlado y lote reproducible**. Un cuerpo fructífero es una mezcla variable de decenas de
compuestos (`254`). Por eso COMP360 (Compass Pathways) es psilocibina sintética en una forma polimórfica
definida, no extracto de hongo (`263`).

| Criterio | Material fúngico | API sintética de grado clínico |
|---|---|---|
| Contenido de psilocibina | Muy variable (`254`) | Especificado, típicamente ≥ 99 % |
| Perfil de impurezas | Desconocido, cambia por lote | Caracterizado y limitado |
| Forma sólida | No aplica | Polimorfo definido y controlado |
| Reproducibilidad | Baja | Alta |
| Aceptable para una NDA | No | Sí |

## Cómo se comprueba (biosíntesis en clave analítica)

No se "mide una ruta": se mide su huella. Lo que un laboratorio puede verificar:

| Qué | Cómo | Qué te dice |
|---|---|---|
| Presencia de intermediarios | LC-MS/MS para norbaeocistina y baeocistina (`256`) | Que la ruta operó y en qué grado se completó |
| Relación baeocistina/psilocibina | Cociente de concentraciones | Huella quimiotaxonómica del material |
| Presencia de genes psiD/psiH/psiK/psiM | PCR sobre ADN fúngico | Identidad genética de la ruta |
| Origen sintético vs biológico | Perfil de impurezas por HRMS; en principio, análisis isotópico ¹³C/²H | Un material sintético tiene impurezas de proceso; uno biológico tiene congéneres |
| Identidad de especie | ITS (`245`, `103`) | Qué organismo es |

Ese último punto —distinguir psilocibina sintética de psilocibina de origen fúngico por su perfil de
impurezas y congéneres— es un problema forense real y una aplicación legítima e interesante de la
metabolómica (`104`).

## Ejemplo aplicado (ILUSTRATIVO) — interpretación de un perfil

```
Muestra A (material de referencia de investigación, origen fúngico declarado):
  psilocibina 6,9 mg/g · baeocistina 0,31 mg/g · norbaeocistina 0,08 mg/g
  Cociente baeocistina/psilocibina = 4,5 %  → coherente con biosíntesis fúngica

Muestra B (declarada como API sintética):
  psilocibina 998 mg/g · baeocistina < LOQ · norbaeocistina < LOQ
  Impurezas de proceso detectadas por HRMS, distintas a los congéneres biológicos
  → coherente con origen sintético
```

Un perfil sin congéneres en un material que dice ser "extracto de hongo" es una contradicción que vale la
pena investigar.

## Errores comunes

- **Llamar a la psilocina un "producto de la ruta".** En el hongo es sobre todo degradación.
- **Suponer que más baeocistina = material más potente.** Suele indicar lo contrario: ruta incompleta.
- **Asumir que todos los *Psilocybe* tienen la misma dotación enzimática.** La expresión varía por especie,
  cepa y condición (`254`).
- **Extrapolar de la ruta a la potencia.** La ruta explica qué compuestos existen, no cuánto hay.
- **Pedirle a este módulo lo que no da.** Aquí no hay ni habrá protocolos de producción.

## Conexión con otros módulos

→ `251-psilocibina-y-psilocina-quimica.md` — las moléculas.
→ `252-baeocistina-y-otros-alcaloides-relacionados.md` — los intermediarios como analitos.
→ `254-variabilidad-de-potencia-entre-especies.md` — por qué el contenido salta tanto.
→ `59-ruta-del-shikimato-y-policetidos.md` — de dónde viene el triptófano.
→ `27-catalisis-y-enzimas.md` y `116-enzimas-y-cinetica-de-michaelis-menten.md`.
→ `263-estado-clinico-y-regulatorio-2026.md` — por qué la industria usa API sintética.