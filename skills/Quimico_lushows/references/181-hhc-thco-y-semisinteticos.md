# 181 — HHC, THC-O y semisintéticos: qué son químicamente y por qué no los tocaría

Después del Δ8 vino una ola de moléculas con nombres de laboratorio: HHC, HHC-O, HHC-P, THC-O acetato,
H4CBD, THCJD. Ninguna es un producto de la planta. Todas se obtienen modificando químicamente un
cannabinoide de partida, y todas comparten el mismo problema: **se venden para consumo humano sin base
toxicológica y con un estatus legal que cambia cada mes**. Este módulo describe la química con rigor para
que puedas identificar, analizar y rechazar estos materiales. **No incluye rutas ni condiciones de síntesis.**

Términos:
- **semisintético (semi-synthetic)** = obtenido modificando químicamente una molécula natural de partida.
- **hidrogenación (hydrogenation)** = adicionar H₂ a un doble enlace, con catalizador metálico.
- **acetilación (acetylation)** = formar un éster acetato sobre un grupo hidroxilo.
- **epímero (epimer)** = estereoisómero que difiere en un solo centro quiral.
- **ceteno (ketene)** = producto de pirólisis de acetatos; gas altamente tóxico.

## El catálogo, con su química

| Compuesto | Fórmula | M (g/mol) | Se obtiene de | Qué le hicieron |
|---|---|---|---|---|
| HHC (hexahidrocannabinol) | C₂₁H₃₂O₂ | 316,48 | Δ8/Δ9-THC | Hidrogenación del doble enlace del anillo |
| HHC-O (acetato de HHC) | C₂₃H₃₄O₃ | 358,52 | HHC | Acetilación del fenol |
| HHC-P | C₂₃H₃₆O₂ | 344,54 | THCP o análogo | Hidrogenación de un homólogo heptilo |
| THC-O acetato (Δ8 o Δ9) | C₂₃H₃₂O₃ | 356,50 | Δ8/Δ9-THC | Acetilación del fenol (con anhídrido acético) |
| H4CBD | C₂₁H₃₄O₂ | 318,50 | CBD | Hidrogenación de los dos dobles enlaces |
| Δ8-THC | C₂₁H₃₀O₂ | 314,47 | CBD | Isomerización ácida (ver `180`) |

Un detalle que casi nadie menciona: **el HHC no es una molécula, son dos**. La hidrogenación crea un nuevo
centro quiral en C9, dando los epímeros **9R-HHC** y **9S-HHC**. Estudios de unión reportan que el 9R es
bastante más activo en CB1 que el 9S [in vitro] — un trabajo publicado en 2025 comparó la activación in
vitro de CB1 por HHC, HHC-O y HHC-P. Un producto "HHC" comercial es una **mezcla de epímeros en proporción
desconocida**, así que la potencia real varía de lote a lote incluso con el mismo porcentaje declarado.

## Los tres riesgos que hay que decir en voz alta

**1. Riesgo toxicológico: no hay datos.** No existe para estos compuestos nada parecido al cuerpo de datos
de seguridad del Δ9-THC. No hay estudios de toxicidad crónica, no hay farmacocinética humana publicada
robusta, no hay datos de metabolitos. La ausencia de reportes de daño **no es evidencia de seguridad**: es
ausencia de estudio (`134`, `135`).

**2. Riesgo específico de los acetatos: el ceteno.** Los ésteres acetato calentados a alta temperatura —como
en un vaporizador— pueden pirolizar y liberar **ceteno**, un gas de toxicidad pulmonar aguda bien
documentada en toxicología industrial. Es un mecanismo plausible y reconocido en la literatura de riesgo del
vapeo; combinado con el precedente del EVALI (`197`), es razón suficiente para no formular con acetatos.

**3. Riesgo de impurezas de proceso.** Hidrogenar exige catalizador metálico (paladio, platino, níquel).
Acetilar exige anhídrido acético, precursor controlado en muchos países. Ambos dejan residuos que hay que
medir por ICP-MS y GC-headspace, y que casi nunca aparecen en los COA comerciales (`88`, `87`).

## Estatus regulatorio — a agosto de 2026, verifícalo antes de decidir

| Jurisdicción | Situación | Verificar en |
|---|---|---|
| EE.UU. federal | La DEA ha sostenido que HHC es un cannabinoide sintético fuera de la definición de cáñamo, y en febrero de 2023 declaró que los ésteres acetato Δ8-THCO y Δ9-THCO son sustancias de Lista I, no cáñamo. | DEA, texto legal vigente |
| Unión Europea | Más de 20 países han adoptado controles. HHC está prohibido en Francia, Irlanda, Bélgica, Austria, Polonia, Estonia, Finlandia, Bulgaria y otros. La República Checa lo controló tras hospitalizaciones pediátricas por comestibles con HHC. Francia (ANSM) ha prohibido además THCP, H4CBD y HHCPO. | Autoridad nacional, EUDA |
| Colombia | El marco de fiscalización cubre THC "y sus isómeros, sales y formas ácidas". Un semisintético psicoactivo no encaja como derivado no psicoactivo. | Minsalud, FNE |

La regla operativa para un negocio serio: **si el estatus legal de tu ingrediente cambia cada trimestre en
media docena de países, no es un ingrediente, es un pasivo.**

## Cómo se mide / cómo se comprueba

- **Detección dirigida por LC-MS/MS.** Cada semisintético tiene su masa y sus transiciones MRM. Un panel de
  screening debe incluir al menos: Δ8-THC, Δ10-THC, HHC (ambos epímeros), HHC-O, THC-O acetato, H4CBD,
  THCP (`83`).
- **Separación de epímeros de HHC:** requiere método cromatográfico específico; si el COA reporta "HHC
  total" sin desglosar 9R/9S, la potencia declarada no es interpretable.
- **HRMS** para asignar fórmula elemental de picos desconocidos (`84`).
- **RMN** cuando hay que probar estructura o proporción de epímeros (`94`).
- **Residuos de proceso:** ICP-MS para Pd/Pt/Ni (`88`), GC-headspace para solventes y anhídrido/ácido acético
  (`87`).
- **En producto de terceros:** el screening de semisintéticos debe ser parte de tu control de entrada si
  compras destilado o aislado a terceros. Se han encontrado en materiales vendidos como "CBD" o "THC"
  convencionales.

## Ejemplo aplicado

Una marca colombiana quiere lanzar un vape "HHC premium" para exportar (ILUSTRATIVO). Análisis del material
ofrecido por el proveedor, LC-MS/MS + ICP-MS:

| Analito | Resultado | Lectura |
|---|---|---|
| HHC (suma de epímeros) | 82,3 % p/p | Sin desglose 9R/9S → potencia impredecible |
| Δ9-THC | 1,7 % p/p | Suficiente para ilegalidad en destino |
| HHC-O | 0,9 % p/p | No declarado en la ficha |
| Paladio | 3,2 mg/kg | Residuo de catalizador; sin límite establecido para inhalación |
| Solventes residuales | No analizado | Inaceptable |

Recomendación técnica: **no lanzar**. No hay especificación defendible, no hay datos de seguridad por
inhalación, hay un catalizador metálico presente, y el mercado de destino puede prohibir el ingrediente
mientras el contenedor está en el barco. Si la marca quiere un producto potente y exportable, el camino es
cannabis legal con THC declarado bajo el marco del país de destino (`210`, `211`, `212`).

## Errores comunes

- Vender "HHC natural". No existe HHC natural en cantidad relevante; es un producto de hidrogenación.
- Tratar la ausencia de reportes de daño como evidencia de seguridad.
- Formular acetatos para vapeo. El riesgo de ceteno es conocido y evitable.
- Comprar sin screening de semisintéticos: pueden aparecer sin estar declarados.
- Aceptar "HHC 90 %" sin proporción de epímeros: el mismo número puede ser dos productos distintos.
- Diseñar un negocio sobre un vacío legal. El vacío se cierra, y el inventario queda.
- Pensar que porque el país de origen lo permite, el de destino lo permitirá. Se verifica destino por destino
  y a la fecha del embarque (`285`).

## Conexión con otros módulos

→ `180-delta8-delta10-e-isomerizacion.md` — el primer eslabón de esta familia.
→ `179-thcp-cbdp-y-homologos.md` — los homólogos que se combinan con estas modificaciones.
→ `197-vapeo-quimica-y-riesgos.md` — por qué la inhalación cambia todo el análisis de riesgo.
→ `134-toxicologia-basica-dosis-y-riesgo.md` · `135-noael-ida-y-limites-de-exposicion.md` — qué falta.
→ `83-lc-ms-ms-y-mrm.md` — cómo se hace el screening.
→ `202-metales-pesados-en-cannabis.md` — los residuos de catalizador.
→ `265-mapa-regulatorio-global.md` — dónde verificar el estatus vigente.