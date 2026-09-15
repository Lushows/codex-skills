# 196 — Tópicos y transdérmicos (lo que se queda en la piel y lo que la atraviesa)

Una crema con CBD y un parche transdérmico con cannabinoides son productos **distintos en objetivo,
regulación y química**. El tópico busca actuar en la piel o justo debajo, sin pasar a sangre en cantidades
relevantes. El transdérmico busca exactamente lo contrario: atravesar la piel y llegar a circulación
sistémica. Confundirlos cuesta caro: un producto vendido como cosmético que en realidad entrega
cannabinoide a sangre deja de ser cosmético a los ojos de cualquier agencia sanitaria, y ahí el expediente
cambia por completo.

Términos: **estrato córneo (stratum corneum)** = la capa muerta y lipídica de la superficie de la piel; es
la barrera real. **Tópico (topical)** = acción local. **Transdérmico (transdermal)** = paso a circulación
sistémica. **Potenciador de penetración (penetration enhancer)** = sustancia que abre transitoriamente la
barrera. **Flujo (flux, J)** = masa que atraviesa la piel por unidad de área y tiempo, en µg/cm²/h.

## Por qué la piel es tan mala puerta para los cannabinoides

El estrato córneo se comporta como una pared de lípidos ordenados. Para atravesarla, una molécula necesita
un equilibrio: suficientemente lipofílica para entrar en los lípidos, suficientemente hidrofílica para salir
al otro lado (epidermis viable, que es acuosa).

Los cannabinoides fallan en la segunda mitad. Su **logP** (coeficiente de reparto octanol/agua, ver `30`)
está reportado en la literatura en el rango aproximado de 6–7 para Δ9-THC y CBD. La ventana clásica de buena
penetración pasiva es logP entre 1 y 3. Consecuencia práctica: **un cannabinoide aplicado en la piel tiende a
quedarse atrapado en el estrato córneo**, lo cual es bueno para un tópico local y malo para un transdérmico.

| Propiedad | Δ9-THC / CBD | Qué implica |
|---|---|---|
| logP (literatura) | ~6–7 | Se acumula en estrato córneo, mala difusión a dermis |
| Masa molar | 314,5 g/mol (ambos, C21H30O2) | Aceptable (< 500 g/mol) |
| Solubilidad en agua | Muy baja (orden de µg/mL) | Necesita vehículo lipídico o solubilizado |
| Punto de fusión CBD | ~66 °C | Sólido; se disuelve en la fase oleosa |

Verifica siempre estos valores con la fuente que uses (los logP reportados varían según el método de
determinación); el orden de magnitud es lo que sostiene la decisión de formulación.

## Formas farmacéuticas y qué resuelve cada una

| Forma | Base | Ventaja | Riesgo típico |
|---|---|---|---|
| Ungüento (ointment) | Anhidra, vaselina/ceras | Oclusivo, alta retención | Sensación grasosa; poca penetración |
| Crema (cream) | Emulsión O/W o W/O | Cosméticamente aceptable | Estabilidad de la emulsión, conservación |
| Gel | Hidrofílico + solubilizante | Fresco, se absorbe rápido | Solubilizar el cannabinoide es el reto |
| Bálsamo (balm) | Ceras + aceites | Muy estable, sin agua → sin conservante | Difusión lenta |
| Parche transdérmico | Matriz adhesiva o reservorio | Dosis controlada en el tiempo | Es un medicamento en casi toda jurisdicción |
| Roll-on / linimento | Alcohólico | Evaporación rápida, sensación fría | Irritación, inflamabilidad |

## Potenciadores de penetración: la palanca y su precio

Los potenciadores más citados en la literatura de formulación son etanol, propilenglicol, transcutol,
ácido oleico, terpenos (limoneno, mentol, cineol) y ésteres como el miristato de isopropilo. Todos funcionan
por el mismo mecanismo general: **desordenan los lípidos del estrato córneo o aumentan la solubilidad del
activo en la barrera**.

El precio: lo que abre la barrera para tu activo la abre para todo lo demás, incluidos conservantes,
fragancias e impurezas. Por eso un tópico con potenciadores exige **más control de contaminantes**, no
menos: metales pesados, pesticidas y solventes residuales del extracto (ver `200`, `201`, `202`).

## Cómo se mide / cómo se comprueba

Aquí está lo que separa un producto serio de una crema con historia:

1. **Potencia del producto terminado.** HPLC-DAD sobre la crema, extrayendo el activo de la matriz.
   Unidad: mg de CBD por gramo de producto, y mg por envase. Extraer cannabinoides de una emulsión
   requiere validación de recuperación (ver `74`).
2. **Permeación in vitro (IVPT, in vitro permeation test).** **Celda de Franz (Franz diffusion cell)**: un
   compartimiento donador con el producto, una membrana (piel humana de banco de tejidos, piel porcina o
   membrana sintética), y un compartimiento receptor que se muestrea en el tiempo. Resultado: perfil de
   cantidad acumulada (µg/cm²) frente a tiempo, y flujo J en µg/cm²/h. Es la prueba que **distingue
   objetivamente un tópico de un transdérmico**.
3. **Distribución en capas (skin retention).** Tras el ensayo, se separan estrato córneo (por *tape
   stripping*), epidermis y dermis, y se cuantifica cada uno. Un buen tópico deja mucho en piel y poco en el
   receptor.
4. **Estabilidad física y microbiológica.** pH, viscosidad, separación de fases, y ensayo de eficacia de
   conservante (challenge test) si la fórmula tiene agua.
5. **Irritación y sensibilización.** Ensayos in vitro validados (por ejemplo métodos OECD para irritación
   cutánea) antes de cualquier prueba en personas, y con comité de ética si hay personas (ver `289`).

## Qué se puede afirmar y qué no

- Que el CBD tiene actividad antiinflamatoria en modelos celulares y animales es una afirmación con nivel
  `[in vitro]` y `[animal]`, y así se debe decir.
- La evidencia **clínica** de tópicos con cannabinoides es limitada; existen ensayos pequeños y estudios
  abiertos, pero no un cuerpo robusto que sostenga afirmaciones terapéuticas `[clínico fase 2, muestras
  pequeñas]`. Ver `207`.
- **Nunca** se escribe que la crema trata, cura o previene artritis, psoriasis, dolor neuropático ni ninguna
  otra enfermedad. Eso convierte un cosmético en un medicamento sin registro (ver `267`, `268`, `276`).
- Lo que sí se puede describir, según el marco de cada país: características cosméticas del producto
  (hidratación, sensación, aroma) y su composición cuantificada.

## Ejemplo aplicado (ILUSTRATIVO)

Crema O/W al 1,0 % p/p de CBD, envase de 60 g. Contenido total = 600 mg de CBD.

Ensayo en celda de Franz, piel porcina, 24 h, área 1,77 cm², n = 6:

- Cantidad acumulada en receptor: 3,1 ± 1,4 µg/cm² a las 24 h → flujo promedio ~0,13 µg/cm²/h.
- Retenido en estrato córneo: 128 ± 41 µg/cm².
- Retenido en epidermis + dermis: 22 ± 9 µg/cm².

Interpretación: más del 80 % de lo que penetró se quedó en el estrato córneo y menos del 2 % llegó al
receptor. Este producto se comporta como **tópico**, no como transdérmico. Cifras **(ILUSTRATIVO)** — el
resultado real depende de la fórmula, la membrana y el medio receptor, y hay que generarlo con tu producto.

## Errores comunes

- **Declarar mg de CBD "por envase" y que el consumidor entienda "por aplicación".** La etiqueta debe dar
  ambos datos, con la cantidad de producto por aplicación.
- **Formular un gel acuoso sin solubilizar el cannabinoide.** Termina en un producto turbio con el activo
  separado en la superficie y una potencia que cambia según de dónde saques la muestra.
- **Suponer que "no pasa a sangre" sin haberlo medido.** Sin IVPT, esa afirmación no tiene sustento; y en
  productos con potenciadores fuertes puede ser falsa.
- **Meter potenciadores potentes en un producto cosmético** y quedarse con la clasificación de cosmético.
  El grado de penetración es parte de lo que define la categoría regulatoria.
- **Olvidar el conservante y su validación.** Una emulsión sin sistema conservante probado es un cultivo con
  aroma a lavanda.
- **Copiar la fórmula de un competidor sin su COA de materia prima.** El mismo porcentaje con un extracto
  distinto da otro producto y otro perfil de contaminantes.

## Conexión con otros módulos

→ `30-extraccion-liquido-liquido-y-logp.md` — por qué el logP manda en la penetración.
→ `123-vias-de-administracion.md` — comparación con oral, sublingual e inhalada.
→ `157-emulsiones-y-nanoemulsiones.md` — cómo estabilizar la base.
→ `160-excipientes-y-compatibilidad.md` — potenciadores, conservantes y sus conflictos.
→ `206-farmacologia-del-cbd.md` — qué hace el CBD y con qué nivel de evidencia.
→ `268-claims-prohibidos-el-caso-bioseta.md` — el límite de lo que se puede decir en la etiqueta.