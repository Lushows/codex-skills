# 149 — Concentración y evaporación (quitar agua sin cocinar el producto)

Después de extraer tienes 60 litros de líquido con 2 % de sólidos. Nadie vende eso. Hay que quitarle el agua
(o el etanol) hasta un concentrado manejable, y ese es el paso donde más activo se pierde por calor y donde más
tiempo se pierde por hacerlo mal. La clave física es simple y salvadora: **al bajar la presión, baja la
temperatura de ebullición**. Evaporar a 45 °C en vez de 100 °C es la diferencia entre conservar los triterpenos
y entregar un caramelo pardo.

Términos: **evaporación al vacío (vacuum evaporation)** = hervir a presión reducida para bajar la temperatura.
**Rotavapor (rotary evaporator)** = evaporador de laboratorio con matraz giratorio y baño térmico. **°Brix
(°Bx)** = % de sólidos solubles aproximado, medido por refractómetro. **Factor de concentración** = volumen
inicial / volumen final. **Ósmosis inversa (reverse osmosis, RO)** y **nanofiltración (NF)** = concentrar por
membrana, sin calor.

## Presión de vapor: la tabla que justifica el vacío

Temperatura de ebullición del agua según presión absoluta (valores de tablas fisicoquímicas estándar):

| Presión absoluta (mbar) | Ebullición del agua (°C) |
|---|---|
| 1013 (atmosférica) | 100 |
| 500 | ~81 |
| 200 | ~60 |
| 100 | ~46 |
| 72 | ~40 |
| 47 | ~32 |
| 24 | ~20 |

Para el etanol, a la misma presión, la ebullición es bastante más baja (a 1013 mbar hierve a ~78 °C). Por eso en
una mezcla hidroalcohólica **primero se va el etanol** y el concentrado se va volviendo más acuoso: útil para
recuperar solvente, pero cambia la polaridad del medio y puede precipitar resinas en el balón.

Regla de trabajo: **si tu activo es termolábil, evapora por debajo de 50 °C.** El vacío no es un lujo, es lo
que hace posible ese número.

## Métodos de concentración

| Método | Temperatura típica | Costo entrada | Escala | ¿Pyme? |
|---|---|---|---|---|
| Marmita abierta a fuego | 95–100 °C | Muy bajo | Cualquiera | Técnicamente sí, químicamente pésimo |
| Rotavapor 5 L | 35–55 °C con vacío | Medio | 1–5 L/h de agua | **Sí, la entrada realista** |
| Rotavapor 20–50 L | 35–55 °C | Alto para pyme | 5–20 L/h | Solo con volumen que lo justifique |
| Evaporador de película descendente | 45–70 °C | Muy alto | 100+ L/h | Maquila |
| Ósmosis inversa / nanofiltración | Ambiente | Medio–alto | Variable | Interesante, poco usado en este sector |
| Congelación fraccionada (freeze concentration) | < 0 °C | Bajo–medio | Pequeña | Artesanal, viable para pilotos |

Dato práctico muy poco conocido en el sector: la **nanofiltración** concentra el licor acuoso sin calor y
retiene bien las moléculas grandes (los β-glucanos son enormes, se retienen fácil) dejando pasar agua y sales.
Para un producto declarado por β-glucano puede ser mejor que evaporar. Es una inversión intermedia y merece al
menos una cotización antes de comprar rotavapor grande.

## Cómo se controla la operación

Se controla con **tres** números medidos, no con "hasta que se vea espeso":

```
1) °Brix por refractómetro — barato, instantáneo, suficiente para control de proceso
   Objetivo típico de concentrado antes de secar: 20–40 °Bx
   OJO: °Bx mide sólidos SOLUBLES totales; incluye azúcares, sales y soporte. No es potencia.

2) Sólidos totales por gravimetría — la referencia real
   Pesa 5,00 mL, seca a 105 °C hasta peso constante, pesa el residuo.
   sólidos (% p/v) = masa residuo (g) / 5,00 mL × 100

3) Factor de concentración
   FC = volumen inicial / volumen final
   Ejemplo: 62,0 L → 6,2 L  →  FC = 10,0

Y el control que decide si el paso fue bueno:
4) BALANCE DE ACTIVO antes y después
   mg de activo en el licor inicial vs mg en el concentrado.
   Si perdiste activo aquí, fue calor, oxidación o precipitación en las paredes.
```

Ejecuta las cuentas con `lab-tools/rendimiento_extraccion.py`; para decisiones que muevan plata, rutea a
`Matematicas_lushows`.

## Los cuatro problemas prácticos del rotavapor

1. **Espuma (foaming).** El licor de hongos y de plantas trae proteínas y saponinas: espuma que sube al
   condensador y contamina el destilado. Soluciones: bajar el vacío gradualmente, subir la velocidad de
   rotación, usar balón más grande (nunca más de 1/2 de llenado), antiespumante alimentario si toca declararlo.
2. **Bumping (golpe de ebullición).** Sobrecalentamiento súbito. Se controla con rotación constante y vacío
   progresivo.
3. **Costra en la pared.** Un extracto que se pega y se quema es activo perdido y limpieza de horas. Baja
   temperatura del baño y no llegues a sequedad en el rotavapor.
4. **Aumento de viscosidad.** Por encima de ~40 °Bx el concentrado se vuelve melaza y la transferencia de calor
   colapsa. Ese es el punto donde debes pasar al secado (`150`), no insistir.

## Recuperación del etanol

Si evaporaste una fracción hidroalcohólica, el condensado **es etanol recuperable**, y eso es dinero:

- Se recoge, se mide el grado con alcoholímetro corregido a 20 °C y se reutiliza para la etapa de maceración,
  **si tu sistema de calidad permite el reúso y lo documentas** (`169`).
- No se reutiliza para producto de consumo si arrastró aromas o si no puedes demostrar su composición.
- El etanol recuperado nunca vuelve limpio: cada ciclo arrastra volátiles. Analízalo o degrádalo a limpieza.

## Ejemplo aplicado — concentrar el licor de reishi

Números **(ILUSTRATIVOS)** para el proceso del módulo `144`:

```
Entrada:  62,0 L de licor acuoso combinado, 2,1 % p/v de sólidos, β-glucano 0,84 g/L
          → sólidos totales = 1 302 g   |   β-glucano total = 52,1 g

Operación: rotavapor 20 L, baño 48 °C, vacío 90 mbar (ebullición ~44 °C),
           condensador a 8 °C, 6 cargas sucesivas, ~9 h totales

Salida:   6,05 L de concentrado, 20,8 % p/v de sólidos, β-glucano 8,32 g/L
          → sólidos = 1 258 g   |   β-glucano = 50,3 g
          FC = 10,2   |   recuperación de sólidos = 96,6 %   |   de β-glucano = 96,5 %

Lectura: el β-glucano aguantó (es un polímero robusto). Si hubiéramos concentrado
a fuego abierto a 100 °C, la pérdida esperable habría estado en la fracción termolábil
(triterpenos y color), no en el glucano — razón más para medir AMBOS analitos.
```

## Errores comunes

- Concentrar a fuego abierto para ahorrar el rotavapor y destruir la fracción termolábil que ibas a declarar.
- Llevar el rotavapor a sequedad: el residuo se quema, se pega y se pierde. El secado es otro equipo (`150`).
- Reportar °Bx como si fuera potencia. El refractómetro no distingue activo de maltodextrina.
- No refrigerar el concentrado: un jarabe a 20 °Bx a temperatura ambiente es un medio de cultivo (`100`).
- Reutilizar etanol recuperado sin analizarlo ni documentarlo. Es un hallazgo de auditoría seguro (`169`).
- Sobrellenar el balón y perder producto por arrastre al condensador.
- Olvidar que al evaporar se concentran también los **contaminantes**: metales pesados y micotoxinas suben en
  proporción al factor de concentración. Un material limítrofe en la materia prima puede salirse de límite en
  el extracto (`243`, `244`).

## Conexión con otros módulos

→ `28-gases-y-presion-de-vapor.md` — la física del vacío y la ebullición.
→ `150-secado-por-aspersion-y-liofilizacion.md` — qué hacer con el concentrado.
→ `144-extraccion-acuosa-y-decoccion.md` — de dónde viene el licor.
→ `34-reologia-y-viscosidad.md` — por qué el concentrado deja de fluir.
→ `243-metales-pesados-en-hongos.md` — por qué concentrar también concentra lo malo.