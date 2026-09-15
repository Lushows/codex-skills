# 176 — CBD: química y propiedades que gobiernan tu formulación

El CBD es el cannabinoide sobre el que está construido casi todo el mercado legal, y también el más
maltratado por el marketing. Aquí no vamos a hablar de para qué sirve (eso es `206` y `207`, con niveles de
evidencia): vamos a hablar de lo que decide si tu producto funciona como producto — solubilidad, punto de
fusión, estabilidad, isomerización a THC en medio ácido, y cómo se cuantifica sin engañarse. Ese es el
conocimiento que evita el error caro: formular un "agua con CBD" que a los tres meses tiene 30 % del activo
declarado, o un aceite que a pH bajo genera trazas de Δ9-THC.

Términos:
- **CBD (cannabidiol)** = C₂₁H₃₀O₂, **314,47 g/mol**; forma ácida CBDA (C₂₂H₃₀O₄, 358,48 g/mol).
- **aislado (isolate)** = CBD cristalino, típicamente ≥ 98 % de pureza declarada.
- **espectro amplio (broad spectrum)** = extracto con otros cannabinoides pero con THC removido.
- **espectro completo (full spectrum)** = extracto con el perfil de la planta, incluido THC bajo el límite.
- **logP** = coeficiente de reparto octanol/agua; qué tan lipofílica es la molécula (ver `30`).

## Propiedades fisicoquímicas de trabajo

| Propiedad | Valor reportado en literatura | Consecuencia práctica |
|---|---|---|
| Masa molar | 314,47 g/mol | Base del factor 0,877 desde CBDA (`175`) |
| Punto de fusión (cristal) | ~ 66 °C | El aislado se funde en el bolsillo; cuidado en logística |
| logP | ~ 6–7 (muy lipofílico) | Prácticamente insoluble en agua; necesita vehículo lipídico o emulsión |
| Solubilidad en agua | del orden de µg/mL | "Agua con CBD" siempre es una emulsión, nunca una solución |
| Solubilidad en etanol, aceites, MCT | Alta | Base de tinturas y aceites (`156`) |
| Estabilidad a la luz UV y al oxígeno | Baja-media | Envase ámbar, headspace mínimo, antioxidante (`61`, `163`) |
| Estabilidad en medio ácido | **Baja** | Ciclación a THC y otros productos; ver abajo |

Los valores anteriores son órdenes de magnitud reportados en la literatura fisicoquímica del cannabidiol.
**Verifica con tu materia prima y tu proveedor**: un aislado y un destilado se comportan distinto.

## La reacción que hay que vigilar: ciclación en medio ácido

El CBD tiene un anillo abierto. En condiciones ácidas (ácidos fuertes o de Lewis) y con calor, cicla hacia
tetrahidrocannabinoles: principalmente Δ9-THC y Δ8-THC, más una colección de subproductos. Esa reacción es,
literalmente, la base industrial de los "cannabinoides convertidos" (ver `180`).

Para un formulador honesto la lectura es preventiva:

- Bebidas y gomas de pH bajo (frutales, ácido cítrico) son un ambiente potencialmente reactivo.
- Procesos con calor + acidez (pasteurización de una bebida ácida) suman los dos factores.
- Nunca asumas: **mídelo**. Se cuantifica Δ9-THC y Δ8-THC en producto terminado y a lo largo del estudio de
  estabilidad (`164`). Un producto de CBD que gana THC con el tiempo es un problema regulatorio grave.

También hay debate sobre si el CBD ingerido se convierte a THC en el estómago humano. La evidencia en
humanos [clínico] no respalda una conversión relevante; los reportes que la sugieren provienen de modelos de
fluido gástrico simulado [in vitro]. Se dice así, con el nivel de evidencia marcado, y no más.

## Aislado vs espectro: qué cambia químicamente

| | Aislado | Espectro amplio | Espectro completo |
|---|---|---|---|
| CBD declarado | ≥ 98 % | Variable | Variable |
| Otros cannabinoides | Ninguno | CBG, CBC, CBDV, sin THC | Perfil de la planta con THC bajo límite |
| Terpenos | Ninguno | Parciales | Presentes |
| Riesgo de THC | Nulo si el COA lo confirma | Bajo, pero **hay que medirlo** | Real: hay que controlarlo (`175`) |
| Estabilidad | Alta en cristal, sensible fundido | Media | Media-baja (más oxidables) |
| Sabor | Neutro | Vegetal | Vegetal intenso |
| Coartada del "efecto séquito" | No aplica | Discutible | Discutible — ver `183` |

Nota de honestidad: la superioridad del espectro completo sobre el aislado se argumenta con el efecto
séquito, cuyo soporte clínico controlado es limitado. Ver `183` antes de escribirlo en una etiqueta.

## Cómo se mide / cómo se comprueba

- **Potencia:** HPLC-DAD (típicamente 220–230 nm), estándar de referencia certificado de CBD y CBDA, curva
  de calibración de al menos 5 puntos con R² ≥ 0,995 (`71`). Reporta `% p/p` o `mg/g` con base declarada.
- **CBD total:** `CBD total = CBD + 0,877 × CBDA` — mismo factor, mismas masas molares (`175`).
- **Identidad del aislado:** punto de fusión, FTIR contra patrón (`92`) y, si hay dudas de estructura,
  RMN ¹H/¹³C (`94`). La cuantificación absoluta sin patrón se hace por qNMR (`95`).
- **Pureza real:** cromatograma completo con detección de impurezas relacionadas; "98 %" por área no es lo
  mismo que 98 % p/p si no hay estándar (`80`).
- **Contaminantes obligatorios en producto terminado:** solventes residuales (`201`), metales pesados
  (`202`), pesticidas (`200`), micotoxinas y microbiología (`203`).
- **Estabilidad:** ICH Q1 con puntos a 0, 3, 6, 9, 12 meses; analitos CBD, CBDA, Δ9-THC, Δ8-THC, CBN
  y aspecto/pH (`164`).

## Ejemplo aplicado

Aceite de CBD 1.000 mg / 30 mL en MCT (ILUSTRATIVO):

```
Objetivo: 1.000 mg de CBD por frasco de 30 mL  →  33,33 mg/mL
Aislado disponible: COA declara 99,1 % p/p de CBD (HPLC-DAD, qNMR de respaldo)

Masa de aislado requerida = 1.000 mg / 0,991 = 1.009,1 mg por frasco
Sobredosificación de proceso (overage) por pérdidas: +3 %  →  1.039,4 mg
```

Al mes 6 del estudio de estabilidad, el frasco en ámbar a 25 °C/60 % HR marca `31,9 mg/mL` (−4,3 %) y el
frasco en transparente a 40 °C marca `27,4 mg/mL` (−17,8 %), con CBN medible. Conclusión: envase ámbar
obligatorio y vida útil declarada según el estudio, no según la costumbre. La cuenta de sobredosificación se
ejecuta con `lab-tools/potencia_formula.py`.

## Errores comunes

- Decir "soluble en agua" de un producto que es una nanoemulsión. Químicamente es otra cosa y se estabiliza
  distinto (`157`).
- Declarar mg de CBD sin decir si incluye CBDA convertido. Declara el analito exacto.
- Formular bebidas ácidas sin medir Δ9-THC y Δ8-THC en estabilidad.
- Comprar aislado "99 %" sin COA con método, laboratorio acreditado y cromatograma (`110`, `111`).
- Guardar aislado fundido y re-solidificado sin revalidar potencia y aspecto.
- Usar "espectro completo" como argumento de eficacia sin decir qué nivel de evidencia lo soporta (`183`).
- Olvidar que el aceite portador (MCT, oliva, girasol) tiene su propia estabilidad oxidativa y aporta al
  vencimiento del producto (`53`).

## Conexión con otros módulos

→ `173-formas-acidas-thca-y-cbda.md` — CBDA y el factor 0,877.
→ `180-delta8-delta10-e-isomerizacion.md` — la ciclación del CBD, en detalle y con advertencias.
→ `183-efecto-sequito-que-dice-la-evidencia.md` — antes de justificar espectro completo.
→ `195-formulacion-de-aceites-y-comestibles.md` — cómo se formula de verdad.
→ `206-farmacologia-del-cbd.md` — mecanismos, con nivel de evidencia.
→ `164-estabilidad-ich-q1-y-vida-util.md` — el estudio que sostiene la fecha de vencimiento.
