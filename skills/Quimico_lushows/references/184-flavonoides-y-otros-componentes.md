# 184 — Flavonoides y el resto de la planta: lo que hay además de cannabinoides y terpenos

Una flor de cannabis tiene cientos de compuestos que no son ni cannabinoides ni terpenos: flavonoides,
clorofila, ceras, esteroles, azúcares, proteínas, sales minerales, agua. Casi nadie los mide, y sin embargo
son los que explican por qué tu extracto salió verde y amargo, por qué se enturbió en la nevera, por qué la
tintura sabe a pasto y por qué el rendimiento de tu proceso no cuadra con la potencia. Este módulo es el
inventario de "todo lo demás", con especial atención a los **cannflavinas**, el grupo de flavonoides
exclusivo del cannabis que el marketing ya empezó a explotar.

Términos:
- **flavonoide (flavonoid)** = polifenol vegetal de esqueleto C6-C3-C6; pigmento y antioxidante (ver `51`).
- **cannflavina (cannflavin)** = prenilflavona propia del cannabis: cannflavina A, B y C.
- **clorofila (chlorophyll)** = pigmento verde; en extractos aporta color y amargor.
- **cera cuticular (cuticular wax)** = lípidos de la superficie vegetal; causa el enturbiamiento (`191`).
- **fitoesterol (phytosterol)** = esterol vegetal (β-sitosterol, campesterol).

## Inventario aproximado de una flor seca

Composición típica de flor seca de cannabis, órdenes de magnitud reportados en la literatura de composición
vegetal. **Verifica con tu lote:**

| Fracción | Rango orientativo (`% p/p base seca`) | Nota |
|---|---|---|
| Cannabinoides totales | 10–30 | La fracción que se paga |
| Fibra (celulosa, hemicelulosa, lignina) | 30–50 | No extraíble; masa muerta en el proceso |
| Proteínas | 10–20 | Se coagulan y ensucian extractos acuosos |
| Azúcares y almidones | 5–15 | Aportan al amargor y al pardeamiento (`62`) |
| Terpenos totales | 0,5–3 | Ver `182` |
| Clorofilas y carotenoides | 0,1–1 | Color y sabor |
| Ceras y lípidos | 0,5–3 | El problema de la winterización (`191`) |
| Flavonoides totales | 0,1–2,5 | Incluidas cannflavinas en trazas |
| Cenizas / minerales | 5–15 | Base del análisis de metales (`202`) |
| Humedad (flor curada) | 8–13 | La base de todo cálculo (`07`) |

Ese cuadro explica de inmediato un número que confunde a todo el mundo: si tu flor tiene 20 % de
cannabinoides, **el rendimiento máximo teórico de un extracto puro sería 20 %**, y en la práctica un extracto
crudo sale con 60–80 % de cannabinoides porque arrastra ceras, clorofila y lípidos. Ver `187` y balance de
masa en `06`.

## Los flavonoides del cannabis

Los flavonoides habituales son los mismos de muchas plantas: apigenina, luteolina, quercetina, kaempferol,
orientina, vitexina, isovitexina, y sus glicósidos. Lo específico son las **cannflavinas A, B y C**,
prenilflavonas descritas solo en *Cannabis sativa*.

Sobre las cannflavinas, con nivel de evidencia estricto: se han reportado como inhibidoras de la vía de
prostaglandinas en ensayos celulares [in vitro], y se describió su ruta biosintética en 2019, lo que abrió
la puerta a producirlas por biotecnología. **No hay evidencia clínica en humanos** a agosto de 2026. No se
afirma aquí ningún efecto terapéutico ni se sugiere uso para ninguna condición.

Punto práctico importante: los flavonoides son **polares y muchos están glicosilados**. Eso significa que
**no se extraen bien con hidrocarburos ni con CO₂ subcrítico**, y sí pasan parcialmente al etanol y al agua.
Un "extracto full spectrum" hecho con butano contiene esencialmente cero flavonoides glicosilados. Si tu
etiqueta habla de flavonoides, el proceso tiene que poder extraerlos.

## Clorofila, ceras y el aspecto del producto

| Componente | Cuándo entra | Qué causa | Cómo se quita |
|---|---|---|---|
| Clorofila | Etanol tibio o contacto prolongado (`187`) | Color verde, amargor | Etanol frío, carbón activado, cromatografía (`193`) |
| Ceras cuticulares | Cualquier extracción de solvente | Turbidez, aspecto lechoso en frío | Winterización (`191`) |
| Fitoesteroles | Solventes apolares | Cristalización indeseada | Winterización, destilación (`192`) |
| Azúcares y proteínas | Extracción acuosa | Pardeamiento, carga microbiana | Filtración, control de proceso (`100`) |

El carbón activado y las tierras filtrantes limpian el color **pero también retienen cannabinoides y
terpenos**. Toda limpieza cuesta activo. Ese costo se cuantifica con balance de masa antes y después
(`06`, `lab-tools/rendimiento_extraccion.py`).

## Cómo se mide / cómo se comprueba

- **Flavonoides totales:** método colorimétrico con AlCl₃, expresado como equivalentes de quercetina
  (`mg EQ/g`). Es un **método de grupo**: barato, semicuantitativo y no específico (`91`).
- **Flavonoides individuales y cannflavinas:** HPLC-DAD (330–350 nm) o LC-MS/MS con patrones certificados.
  Las cannflavinas están en trazas: necesitas MS (`83`).
- **Clorofila:** absorbancia UV-Vis a ~665 nm y ~649 nm, con las ecuaciones clásicas; útil como control de
  proceso, no como especificación de producto (`90`).
- **Ceras y lípidos:** contenido de materia insaponificable, o simplemente el criterio operativo de la
  winterización (turbidez a −20 °C, `191`).
- **Cenizas y humedad:** métodos gravimétricos de farmacopea (`280`); son la base para expresar todo en base
  seca (`07`).
- **Perfil global / huella:** si quieres comparar lotes o procesos, la herramienta correcta es el
  fingerprint cromatográfico con quimiometría, no medir compuesto por compuesto (`104`, `105`).

## Ejemplo aplicado

Comparación de dos extractos del mismo lote de flor (ILUSTRATIVO):

| Parámetro | Extracto etanólico en frío | Extracto con hidrocarburo |
|---|---|---|
| Rendimiento (`g extracto / 100 g flor`) | 18,4 | 13,9 |
| Cannabinoides totales en el extracto | 62 % p/p | 78 % p/p |
| Terpenos totales | 6,1 mg/g | 9,4 mg/g |
| Flavonoides totales (EQ) | 3,8 mg EQ/g | < 0,3 mg EQ/g |
| Clorofila (Abs 665 nm, 1 mg/mL) | 0,42 | 0,04 |
| Ceras (turbidez a −20 °C) | Alta | Media |

Lectura: el etanólico rinde más masa pero menos pureza, y es el único que trae flavonoides. Si el producto
se va a vender como "espectro completo con flavonoides", el proceso correcto es el etanólico —y luego habrá
que decidir cuánta clorofila se remueve, sabiendo que cada paso de limpieza cuesta cannabinoide.

Recuperación de cannabinoides del proceso completo:

```
Flor: 1.000 g con 20,0 % cannabinoides totales base seca  →  200 g de cannabinoide de partida
Extracto etanólico: 184 g al 62 %                          →  114,1 g recuperados
Recuperación = 114,1 / 200 = 57,1 %
```

Ese 57 % es el número que decide la economía, no el rendimiento en masa. Ejecútalo con
`lab-tools/rendimiento_extraccion.py`.

## Errores comunes

- Vender "rico en flavonoides" un extracto hecho con hidrocarburo o CO₂. No los tiene.
- Reportar flavonoides totales por colorimetría como si fuera un dato específico. Es un método de grupo.
- Ignorar la clorofila hasta que el cliente devuelve el producto por sabor.
- Descontar la clorofila con carbón sin medir cuánto cannabinoide se llevó el carbón.
- Confundir rendimiento en masa con recuperación de activo. Son dos números distintos y solo uno paga.
- Hablar de cannflavinas con lenguaje terapéutico. La evidencia es [in vitro] y punto.
- Olvidar que la fracción de cenizas es donde viven los metales pesados que te van a medir (`202`).

## Conexión con otros módulos

→ `51-polifenoles-y-flavonoides.md` — la química general de la familia.
→ `182-terpenos-del-cannabis.md` — la otra fracción menor que sí se paga.
→ `187-extraccion-con-etanol.md` — el proceso que sí los arrastra.
→ `191-winterizacion-y-desceramiento.md` — cómo se quitan las ceras.
→ `06-estequiometria-y-balance-de-masa.md` — rendimiento vs recuperación.
→ `104-metabolomica-y-huella-quimica.md` — cómo se compara "todo lo demás" entre lotes.
