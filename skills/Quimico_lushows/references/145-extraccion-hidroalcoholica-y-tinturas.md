# 145 — Extracción hidroalcohólica y tinturas (etanol: la mitad que saca lo lipofílico)

El etanol es el otro solvente del oficio. Saca lo que el agua no toca: triterpenos, esteroles, hericenonas,
resinas, cannabinoides. Y como el etanol y el agua se mezclan en cualquier proporción, el grado alcohólico se
convierte en una **perilla de polaridad** que ajustas según qué quieras sacar. Entender esa perilla es la
diferencia entre una tintura que sí tiene los activos que dices y un frasco de alcohol con color. Además, el
etanol tiene una ventaja regulatoria enorme: es solvente **clase 3** en la clasificación ICH de solventes
residuales, el escalón de menor preocupación toxicológica (`87`), y para una pyme es el único solvente
orgánico que se puede manejar con relativa sencillez.

Términos: **tintura (tincture)** = extracto líquido en mezcla hidroalcohólica, listo para dosificar en gotas.
**Grado alcohólico / ABV (alcohol by volume)** = % v/v de etanol. **Maceración (maceration)** = dejar el
material en reposo con el solvente. **Percolación (percolation)** = pasar solvente fresco a través de una
columna del material. **Menstruo (menstruum)** = el solvente de la tintura. **logP** = medida de lipofilia; a
mayor logP, más afinidad por solventes apolares (`30`).

## La perilla: qué saca cada grado alcohólico

| Etanol (% v/v) | Qué extrae preferentemente | Uso típico |
|---|---|---|
| 20–30 % | Azúcares, taninos, sales, algo de fenoles | Casi nunca solo; conservación de infusiones |
| 40–50 % | Fenoles, glicósidos, alcaloides polares | Tinturas "generales" de material blando |
| 60–70 % | Fenoles + parte de terpenoides; buen compromiso | Melena de león, material vegetal mixto |
| 75–85 % | Triterpenos, esteroles, resinas | **Reishi, chaga: la fracción triterpénica** (`224`) |
| 90–96 % | Resinas, lípidos, cannabinoides, ceras | Cannabis (`187`); también arrastra clorofila y ceras |

Regla mental: **más agua = más polar = más azúcares y sales; más etanol = más apolar = más resinas y ceras.**
Y los β-glucanos, que son muy polares y de alto peso molecular, **precipitan** al subir el etanol: por eso una
tintura de reishi al 80 % prácticamente no tiene β-glucano, y por eso existe la extracción dual (`146`).

## Maceración vs percolación

| Criterio | Maceración | Percolación |
|---|---|---|
| Equipo | Tanque cerrado, agitación ocasional | Percolador cónico de acero o vidrio |
| Tiempo | 7–21 días típico | 24–72 h |
| Consumo de solvente | Alto (queda retenido en el bagazo) | Menor por unidad de activo |
| Agotamiento del material | Parcial (equilibrio) | Casi total (gradiente continuo) |
| Control | Fácil | Requiere pericia (canalización) |
| ¿Pyme? | Sí, es la vía obvia | Sí, con percolador de 20–50 L |

Para una pyme colombiana: **maceración con 2 extracciones sucesivas** rinde casi como percolación y no exige
oficio. Si vas a producción seria, el percolador paga solvente.

## Cuentas que tienes que saber hacer

```
1) RELACIÓN DROGA:MENSTRUO (drug:menstruum ratio)
   1:5 p/v  =  100 g de material seco en 500 mL de menstruo.
   Farmacopeas suelen usar 1:5 para tinturas y 1:10 para material potente.

2) PREPARAR EL MENSTRUO desde alcohol de 96 % v/v
   V(96 %) = V_final × ABV_objetivo / 96
   Ejemplo: 5,00 L al 70 % v/v  →  V(96 %) = 5000 × 70 / 96 = 3646 mL
            agua = 5000 − 3646 = 1354 mL
   (Ojo: etanol + agua CONTRAEN volumen. Mezcla y ajusta a volumen final, no sumes a ciegas.)

3) SÓLIDOS TOTALES DE LA TINTURA
   Evapora 5,00 mL a sequedad, pesa el residuo.
   sólidos (mg/mL) = masa residuo (mg) / 5,00 mL

4) ACTIVO POR GOTA
   1 mL ≈ 20 gotas con gotero estándar — VERIFÍCALO con tu gotero, varía con la viscosidad.
   mg activo/gota = (mg activo/mL) / gotas por mL
```

Toda esta aritmética va a `lab-tools/diluciones.py` y `lab-tools/potencia_formula.py`. Nada de mental.

## Seguridad y cumplimiento del etanol en Colombia

A agosto de 2026, para operar con etanol en Colombia hay tres frentes que verificar antes de comprar el primer
tambor (confirma el estado vigente con la autoridad correspondiente, esto cambia):

- **Alcohol potable vs desnaturalizado.** Para producto de consumo humano necesitas etanol de grado alimentario
  o farmacéutico, con COA y ficha técnica. El desnaturalizado **no** sirve: el desnaturalizante es tóxico y
  queda en el extracto.
- **Control de licores / impuesto al consumo.** La compra de alcohol etílico potable en volumen está regulada
  y suele exigir permisos y trazabilidad; revisa con la secretaría de hacienda departamental y el proveedor.
- **Seguridad industrial.** El etanol es inflamable (punto de inflamación ~13 °C para el absoluto). Área
  ventilada, sin fuentes de ignición, extintores, y SDS del solvente a la mano (`08`, `09`).

Y el frente analítico: si vendes un extracto **seco**, hay que demostrar que el etanol se fue. Se mide por
GC-headspace y se compara contra el límite de solventes clase 3 (`87`, `201`).

## Cómo se comprueba una tintura

| Atributo | Método | Unidad | Por qué importa |
|---|---|---|---|
| Grado alcohólico | Densimetría / alcoholímetro corregido a 20 °C | % v/v | Conservación y polaridad declarada |
| Sólidos totales | Evaporación a sequedad, gravimetría | mg/mL | Cuánto extracto hay realmente |
| Activo marcador | HPLC-DAD (triterpenos, `224`) o LC-MS/MS | mg/mL | Lo único que sostiene la etiqueta |
| Densidad | Picnómetro / densímetro | g/mL | Convertir mg/mL ↔ mg/g |
| Metanol | GC-headspace | ppm | Riesgo si el alcohol no es de grado |
| Microbiología | Recuento y patógenos (`100`) | UFC/mL | Menos crítica sobre ~25 % v/v, no nula |

Un ABV ≥ ~20–25 % v/v en el producto final suele bastar como sistema autoconservante; por debajo, hay que
pensar en conservantes y en microbiología en serio.

## Ejemplo aplicado — tintura de reishi estandarizada por triterpenos

```
Material: 500 g de cuerpo fructífero seco de Ganoderma lucidum, malla 40, humedad 7,2 %
Menstruo: 2,50 L al 80 % v/v (relación 1:5 p/v)
Proceso: maceración 14 días, 22 °C, agitación diaria, frasco ámbar cerrado
         → prensado del bagazo → 2ª maceración con 1,25 L al 80 %, 7 días
         → combinar, reposar 48 h en frío, filtrar 1 µm, ajustar a 3,50 L con menstruo

Controles (ILUSTRATIVO):
  ABV final                    78,4 % v/v
  Sólidos totales              41,2 mg/mL
  Ácidos triterpénicos totales  3,10 mg/mL  (HPLC-DAD 252 nm, como ácido ganodérico A)
  β-glucano                     < LOQ  ← ESPERADO: el etanol alto no lo extrae

Etiqueta honesta posible: "cada 1 mL aporta 3,1 mg de ácidos triterpénicos totales
(expresados como ácido ganodérico A, por HPLC-DAD)".
Etiqueta deshonesta: "extracto de reishi de espectro completo".  ← le falta la mitad (`146`)
```

## Errores comunes

- Vender una tintura alcohólica de reishi o cola de pavo hablando de β-glucanos: en ese menstruo no están.
- Usar alcohol antiséptico o desnaturalizado del supermercado. No es apto para consumo.
- Preparar el menstruo sumando volúmenes sin ajustar a volumen final: la contracción etanol-agua te deja fuera
  del grado que declaraste.
- Guardar tinturas en frasco transparente: fotodegradación de fenoles y triterpenos (`61`).
- No prensar el bagazo: se queda con un tercio del líquido cargado.
- Declarar "extracto 1:5" como si fuera potencia. Es una relación de masa/volumen, no un contenido de activo
  (`151`).
- Secar la tintura en casa con calor directo: pierdes activo y no eliminas el etanol de forma controlada.

## Conexión con otros módulos

→ `146-extraccion-dual-y-por-que-importa.md` — cómo se combinan agua y etanol sin engañar a nadie.
→ `20-parametros-de-solubilidad-y-eleccion-de-solvente.md` — la teoría de por qué el grado alcohólico manda.
→ `87-solventes-residuales.md` — cómo se demuestra que el etanol se fue.
→ `156-liquidos-goteros-y-jarabes.md` — convertir la tintura en producto dosificable.
→ `187-extraccion-con-etanol.md` — el mismo solvente aplicado a cannabis, con otras reglas.
