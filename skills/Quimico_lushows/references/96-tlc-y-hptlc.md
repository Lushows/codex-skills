# 96 — TLC y HPTLC (la placa: el análisis más barato que sí sirve para identidad)

La cromatografía en capa delgada es una placa de vidrio o aluminio cubierta de sílice, un poco de solvente y
una lámpara UV. Cuesta centavos por muestra y, sin embargo, es un método **oficial** de identidad en
farmacopeas de todo el mundo. Su versión moderna e instrumentada, HPTLC, es la herramienta de referencia
para autenticar material botánico: la American Herbal Pharmacopoeia y la USP publican monografías con
imágenes de placa. Para un emprendedor de hongos o de cannabis, TLC es la forma más barata de responder
"¿esto es lo que dice ser?" antes de gastar en HPLC.

Términos: **fase estacionaria (stationary phase)** = la sílice de la placa. **fase móvil (mobile phase)** =
la mezcla de solventes que sube por capilaridad. **Rf (retention factor)** = distancia que recorrió la
mancha ÷ distancia que recorrió el frente; entre 0 y 1. **derivatización (derivatization)** = rociar un
reactivo que revela manchas invisibles. **HPTLC (High-Performance Thin-Layer Chromatography)** = TLC con
placas de partícula fina, aplicador automático, cámara controlada y densitómetro.

## TLC vs HPTLC vs HPLC

| | TLC clásica | HPTLC | HPLC |
|---|---|---|---|
| Aplicación de muestra | Capilar a mano | Aplicador automático en banda | Inyector |
| Reproducibilidad de Rf | Regular | Buena | N/A (usa tiempo de retención) |
| Cuantificación | No confiable | Sí, por densitometría | Sí, la referencia |
| Muestras por corrida | 5–10 | 15–20 en paralelo | 1 a la vez |
| Costo por muestra | Muy bajo | Bajo | Medio |
| Uso principal | Identidad, seguir reacción | **Identidad y huella de botánicos** | Cuantificación |

La ventaja estructural de la placa: corres **muestra, patrón y referencia botánica lado a lado en la misma
corrida**, bajo exactamente las mismas condiciones. Eso hace la comparación visual mucho más honesta que
comparar dos cromatogramas de HPLC corridos en días distintos.

## Cómo se corre una TLC (procedimiento tipo)

```
1. Prepara la camara: papel de filtro empapado en fase movil, tapa, 20 min de saturacion.
2. Marca la linea de siembra a 1,0 cm del borde inferior (NUNCA sumergida).
3. Aplica 2-10 uL de muestra y de patron en puntos separados >= 1 cm.
4. Introduce la placa; deja subir hasta 1 cm antes del borde superior.
5. Saca, marca el frente INMEDIATAMENTE con lapiz, seca.
6. Revela: UV 254 nm (apagamiento), UV 366 nm (fluorescencia), luego reactivo quimico.
7. Fotografia bajo cada condicion y calcula Rf.

Rf = distancia del centro de la mancha desde la siembra / distancia del frente
```

Rf útil de trabajo: **0,2–0,8**. Fuera de ahí, ajusta la polaridad de la fase móvil: más polar sube más el
compuesto polar.

## Reveladores que te van a servir

| Reactivo | Revela | Uso en lo tuyo |
|---|---|---|
| UV 254 nm | Cromóforos conjugados | Cannabinoides, fenoles |
| UV 366 nm | Fluorescentes | Cumarinas, algunos alcaloides |
| Vainillina-H₂SO₄, calor | Terpenos, esteroles | Triterpenos ganodéricos de reishi |
| Anisaldehído-H₂SO₄ | Terpenos y azúcares | Perfiles de extracto |
| **Fast Blue B / BB salt** | Fenoles | Clásico para **cannabinoides**; separa CBD/THC/CBN |
| Dragendorff | Alcaloides | Psilocibina y relacionados (identidad, no cantidad) |
| Ninhidrina | Aminas y aminoácidos | Psilocibina/psilocina dan color con ninhidrina |
| Naftol-H₂SO₄ | Azúcares | Perfil de polisacáridos crudo |

## Cuándo la placa alcanza y cuándo no

**Alcanza para:** confirmar que una materia prima corresponde al perfil de referencia; detectar la ausencia
de un marcador esperado; ver si hay un pico gigante que no debería estar; seguir fracciones en una
purificación; tamizar 20 lotes y decidir cuáles mandar a HPLC.

**No alcanza para:** un número de cumplimiento. Ni potencia de THC declarada en etiqueta, ni contenido de
β-glucano, ni pesticidas, ni metales. Los kits caseros de "mide tu THC con una placa" dan órdenes de
magnitud, no valores reportables (ver `198-analisis-de-potencia-metodo.md`).

**Nunca da identidad de especie.** Dos especies de *Ganoderma* pueden dar placas parecidísimas. La especie
se resuelve por ADN (ver `103` y `245`).

## Cómo se comprueba

- **Patrón en la misma placa**, siempre. Un Rf sin patrón simultáneo no vale: el Rf cambia con humedad
  ambiente, saturación de cámara, lote de placa y temperatura.
- **Referencia botánica auténtica** (authenticated botanical reference material) cuando el objetivo es
  identidad de planta u hongo, no solo un compuesto puro.
- **Imagen documentada** bajo las tres condiciones (254, 366, revelado), archivada con el lote.
- **Criterio escrito**: qué bandas deben estar, en qué Rf ± tolerancia, y qué se hace si falta una.
- Para HPTLC cuantitativa: curva de calibración en la misma placa, típicamente no lineal
  (se ajusta por polinomio), con `71` y `73` aplicando igual que en cualquier método.

## Ejemplo aplicado (ILUSTRATIVO)

Verificación de identidad de un lote de extracto de reishi antes de mandarlo a Megazyme.

```
Placa       : silica gel 60 F254, HPTLC 10 x 10 cm
Fase movil  : tolueno : acetato de etilo : acido formico  (60 : 40 : 2, v/v/v)
Aplicacion  : 5 uL de extracto 10 mg/mL en metanol
Revelado    : UV 366 nm, luego vainillina-H2SO4 + 105 C, 5 min
Referencia  : material botanico autenticado de Ganoderma lucidum

Bandas del patron autentico : Rf 0,28 (violeta) ; 0,41 (violeta) ; 0,55 (rosa) ; 0,68 (violeta)
Bandas del lote GL-2608     : Rf 0,28 ; 0,41 ; 0,55 ; 0,68  -> coincide, 4 de 4
Banda extra en el lote      : ninguna
Conclusion                  : perfil compatible; pasa a cuantificacion de beta-glucano (91)
                              y a confirmacion de especie por ITS (103) una vez al ano
```

(Cifras y Rf ilustrativos; los valores reales dependen de tu placa, tu cámara y tu lote de sílice.)

## Errores comunes

- **Sumergir la línea de siembra** en la fase móvil: la muestra se disuelve hacia la cámara y no sube nada.
- **No saturar la cámara**: los Rf se corren y las bandas se deforman.
- **Comparar el Rf de hoy con el Rf de un artículo publicado.** Solo se comparan corridas simultáneas.
- **Sobrecargar la placa**: manchas en cometa y colas; aplica menos volumen o diluye.
- **Reportar cuantificación desde una TLC clásica a ojo.** Eso no es un número.
- **Creer que la placa identifica la especie.** Identifica el perfil químico, que puede compartirse.
- **No fotografiar.** La placa se degrada en horas; sin imagen, el registro se perdió.

## Conexión con otros módulos

→ `31-principio-de-la-cromatografia.md` — por qué las cosas se separan.
→ `79-hplc-y-uhplc.md` — el paso siguiente cuando necesitas el número.
→ `103-identidad-por-adn-its-y-barcoding.md` — la identidad que la placa no puede dar.
→ `104-metabolomica-y-huella-quimica.md` — la placa como huella de bajo costo.
→ `224-triterpenos-ganodericos-analisis.md` — perfiles de reishi en placa y en HPLC.
→ `284-auditoria-de-proveedor.md` — TLC como filtro de entrada barato y repetible.
