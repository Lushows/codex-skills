# 92 — FTIR y NIR (identificar materia prima en 30 segundos, sin destruirla)

FTIR y NIR son las dos técnicas de infrarrojo que más plata ahorran en una operación real, y casi nadie las
usa bien. No sirven para decirte "cuánto β-glucano hay" en un material nuevo, pero sí para responder en
menos de un minuto la pregunta que más caro cuesta equivocar: **¿este bulto que me llegó es lo que dice la
etiqueta?** Es la herramienta de identificación de materia prima (identity testing) que exige la GMP de
suplementos en Estados Unidos, y la que permite rechazar un lote en la puerta de la bodega en vez de en la
línea de producción.

Términos: **FTIR (Fourier-Transform Infrared)** = infrarrojo medio, 4000–400 cm⁻¹; mide vibraciones de
enlaces. **NIR (Near-Infrared)** = infrarrojo cercano, ~12000–4000 cm⁻¹; sobretonos, señal débil pero
penetrante. **ATR (Attenuated Total Reflectance)** = accesorio de FTIR donde pones el sólido encima de un
cristal y listo, sin preparar pastilla. **número de onda (wavenumber, cm⁻¹)** = eje x del espectro IR.
**quimiometría (chemometrics)** = matemática que convierte espectros en decisiones (ver `105`).

## FTIR vs NIR: cuál para qué

| | FTIR (medio) | NIR (cercano) |
|---|---|---|
| Qué ve | Grupos funcionales, huella dactilar | Sobretonos de C-H, O-H, N-H |
| Preparación | ATR: nada, o pastilla de KBr | Nada; incluso a través de bolsa |
| Interpretable a ojo | Sí, bastante | No, casi nunca |
| Necesita modelo quimiométrico | Para cuantificar, sí | **Siempre** |
| Uso estrella | Identidad, contaminante, polimorfo | Humedad, contenido, control en línea |
| Costo de equipo | Menor | Mayor si es de proceso |
| Portátil | Sí, hay de mano | Sí, muy usado en bodega |

Regla práctica: **FTIR para identidad, NIR para cantidad rutinaria de algo ya calibrado.**

## Bandas de FTIR que sí vas a usar

| Banda (cm⁻¹) | Enlace | Dónde aparece en lo tuyo |
|---|---|---|
| 3600–3200 (ancha) | O-H | Agua, azúcares, polioles |
| 3000–2800 | C-H alifático | Grasas, ceras, terpenos |
| ~1745 | C=O éster | Aceites, lípidos, acetatos |
| ~1650 y ~1550 | Amida I y II | Proteína, quitina de pared fúngica |
| 1200–900 (huella) | C-O-C, C-O | **Zona de polisacáridos**: glucanos, almidón, celulosa |
| ~890 | Enlace **β** anomérico | Indicio de configuración β |
| ~845 | Enlace **α** anomérico | Indicio de almidón / α-glucano |

Ese par 890 vs 845 cm⁻¹ es la razón por la que FTIR se cita en artículos de hongos para distinguir β de α.
Cuidado: es **cualitativo y sugerente**, no cuantitativo. Un FTIR **no reemplaza** al Megazyme K-YBGL
(ver `91`). Sirve para tamizar rápido y decidir a qué muestras vale la pena pagarles el ensayo caro.

## Cómo se usa de verdad: identidad por comparación

No se "interpreta" el espectro cada vez. Se compara contra un espectro de referencia y se calcula un índice
de similitud.

```
1. Construye la biblioteca: 3-10 lotes de materia prima YA verificada por un
   método ortogonal (ITS/ADN para especie, HPLC para marcador). Ver 103 y 245.
2. Cada lote nuevo: 3 tomas de distintos puntos del bulto (ver 66).
3. Compara: índice de correlación / distancia espectral.
4. Criterio de aceptación: p. ej. correlación >= 0,95 contra la biblioteca (ILUSTRATIVO,
   cada matriz exige su propio umbral, determinado con lotes buenos y lotes malos).
5. Fuera de criterio -> no se rechaza a ciegas: se manda al método de referencia.
```

Un FTIR de identidad sin biblioteca propia no vale nada. La biblioteca **es** el método.

## NIR para humedad y contenido

El NIR mide agua muy bien (banda O-H). Se calibra contra un método primario —Karl Fischer o pérdida por
secado (ver `98`)— con 30–50 muestras que cubran todo el rango, y luego lee en segundos. Es la forma
correcta de controlar la humedad lote a lote sin pagar Karl Fischer cada vez. Lo mismo aplica a contenido de
un activo, **si** ya tienes un método de referencia y suficientes muestras: el modelo NIR nunca es mejor que
el método con el que lo calibraste (ver `105-quimiometria-pca-y-modelos.md`).

## Cómo se comprueba que el FTIR/NIR está diciendo la verdad

- **Verificación diaria del instrumento**: espectro de poliestireno estándar, chequeo de longitud de onda.
- **Muestra control conocida** en cada corrida, igual que en cualquier método (ver `77`).
- **Método ortogonal periódico**: cada N lotes, confirma con HPLC / ADN / Megazyme. Si el NIR se desvía, es
  porque cambió el proveedor, el molino o la humedad ambiente.
- **Rango de validez declarado**: un modelo NIR calibrado entre 4 % y 10 % de humedad **no aplica** a una
  muestra con 18 %. Extrapolar un modelo quimiométrico es inventar.

## Ejemplo aplicado (ILUSTRATIVO)

Llega un bulto de 25 kg rotulado "extracto de cordyceps 10:1". FTIR-ATR, 3 tomas.

```
Correlación contra biblioteca "cordyceps extracto"      : 0,71   -> FUERA de criterio (>= 0,95)
Correlación contra biblioteca "maltodextrina"           : 0,93
Banda anomérica dominante                               : ~845 cm-1 (alfa)
Decisión                                                : cuarentena, no se usa
Confirmación ortogonal pedida                           : alfa-glucano por K-YBGL + cordicepina por HPLC
Resultado de confirmación                               : alfa-glucano 61 % p/p b.s.; cordicepina < LOQ
```

Ese FTIR de 40 segundos evitó meter maltodextrina a un producto terminado. El ensayo confirmatorio costó
plata, pero solo se pagó para el lote sospechoso. (Cifras ilustrativas.)

## Errores comunes

- **Creer que FTIR cuantifica β-glucano.** Da indicios de α vs β; el número sale de `91`.
- **Comparar contra la biblioteca del fabricante del equipo** y no contra tus propios lotes verificados.
- **Muestra húmeda.** La banda ancha de O-H tapa la zona 3600–3200 y arruina la correlación. Seca y controla.
- **Una sola toma del bulto.** Los polvos se segregan; la superficie no representa el interior.
- **Usar un modelo NIR fuera del rango con el que se calibró.**
- **No documentar el criterio de aceptación antes de medir.** Si el umbral se decide después de ver el
  resultado, no es un criterio: es una excusa.

## Conexión con otros módulos

→ `93-espectroscopia-raman.md` — la técnica hermana; complementaria, no redundante.
→ `105-quimiometria-pca-y-modelos.md` — cómo se construye y valida el modelo detrás del NIR.
→ `91-metodos-colorimetricos-y-enzimaticos.md` — el método de referencia que el FTIR nunca reemplaza.
→ `141-especificacion-de-materia-prima.md` — dónde entra la prueba de identidad en la especificación.
→ `103-identidad-por-adn-its-y-barcoding.md` — identidad de **especie**, que el IR no puede dar.
→ `284-auditoria-de-proveedor.md` — el FTIR como herramienta de control de entrada.
