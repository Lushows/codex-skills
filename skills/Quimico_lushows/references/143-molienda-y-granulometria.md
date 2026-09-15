# 143 — Molienda y granulometría (el tamaño de partícula decide tu rendimiento)

Moler no es "hacer polvo". El tamaño de partícula controla cuánta superficie ve el solvente y, por lo tanto,
cuánto activo sale y en cuánto tiempo. También controla si el polvo fluye en la encapsuladora, si se apelmaza
en el frasco y si el análisis del laboratorio es representativo. Es un paso barato de hacer bien y carísimo de
hacer mal: la mitad de los "el extracto rindió poco" del mundo real son en realidad "la materia prima estaba
mal molida" o "no estaba tamizada y cada muestra era distinta".

Términos: **granulometría (particle size distribution, PSD)** = cómo se reparten los tamaños de partícula.
**Malla / mesh** = número de aberturas por pulgada lineal de un tamiz; a mayor número, abertura más pequeña.
**d50 (median particle size)** = tamaño por debajo del cual está el 50 % de la masa. **Finos (fines)** =
fracción muy pequeña que vuela, se apelmaza y ensucia. **Bagazo / marc** = sólido agotado después de extraer.

## La tabla que necesitas pegada al molino

Equivalencias estándar de tamiz (serie ASTM/US mesh), útiles para escribir especificaciones:

| Malla (mesh) | Abertura (µm) | Aspecto | Uso típico |
|---|---|---|---|
| 10 | 2000 | Trozos gruesos | Pre-molienda, decocción larga |
| 20 | 850 | Granulado | Percolación, tinturas |
| 40 | 425 | Polvo grueso | Extracción acuosa con agitación |
| 60 | 250 | Polvo medio | Extracción hidroalcohólica |
| 80 | 180 | Polvo fino | Encapsulado, extracción rápida |
| 100 | 150 | Muy fino | Análisis, mezclas homogéneas |
| 200 | 75 | Impalpable | Muestra analítica (`67`) |
| 325 | 45 | Micronizado | Suspensiones, formulaciones especiales |

Especificación bien escrita **(ILUSTRATIVO)**: *"≥ 95 % p/p pasa malla 80 (180 µm); ≤ 5 % p/p pasa malla 200
(75 µm)"*. Fíjate que tiene **dos** criterios: uno de finura mínima y uno de límite de finos.

## Por qué el tamaño cambia el rendimiento

La velocidad de extracción está gobernada por difusión: el solvente tiene que entrar a la partícula, disolver
y salir. Al reducir el diámetro, la superficie por gramo sube y el camino de difusión baja.

```
Aproximación útil (partículas esféricas, mismo material):
  Área específica  ∝ 1 / d
  Tiempo característico de difusión  t ∝ d² / D

  Reducir d a la mitad  →  el doble de área y ~4 veces menos tiempo de difusión.

Ejemplo (ILUSTRATIVO) — extracción acuosa de β-glucano de reishi, 90 °C, 2 h, 1:15 p/v:
  d50 ≈ 800 µm (malla 20)   rendimiento de sólidos  6,1 % p/p b.s.
  d50 ≈ 300 µm (malla 50)   rendimiento de sólidos  9,4 % p/p b.s.
  d50 ≈ 150 µm (malla 100)  rendimiento de sólidos 10,2 % p/p b.s.  ← ganancia marginal, filtrado lento
```

Traducción: hay un punto donde moler más ya no te da activo y sí te da un problema de filtración, porque el
polvo ultrafino tapona la tela y forma una torta impermeable. **El óptimo casi nunca es "lo más fino posible".**

## Molinos: qué compra una pyme y qué se manda a maquilar

| Tipo de molino | Principio | Rango típico | Costo relativo | Notas |
|---|---|---|---|---|
| Cuchillas (blade) | Corte | 500–2000 µm | Muy bajo | Sirve para pre-moler; calienta |
| Martillos (hammer mill) | Impacto | 150–1000 µm | Bajo–medio | **El caballo de batalla de la pyme** |
| Discos / pin mill | Cizalla | 75–300 µm | Medio | Buen control, más caro |
| Molino de bolas | Fricción | 20–100 µm | Medio | Lento, calienta, batch pequeño |
| Chorro de aire (jet mill) | Colisión | 1–20 µm | Alto | Sin calor; maquila |
| Criogénico (con N₂ líquido) | Fragilización | Variable | Alto | Para termolábiles y resinas; maquila |

El punto crítico que casi nadie mira: **el calor de molienda**. Un molino de martillos puede subir el material
20–40 °C en pocos minutos. Si tu activo es termolábil o tu material es resinoso (cannabis, chaga, reishi con
mucho triterpeno), la molienda continua lo cocina o lo embadurna. Solución de pyme: moler en tandas cortas,
dejar enfriar, y medir la temperatura del polvo a la salida con termómetro infrarrojo.

## Cómo se comprueba la granulometría

```
MÉTODO DE TAMIZADO POR VIBRACIÓN (el que puedes hacer tú)

1. Pesa 100,0 g de muestra seca (registra humedad; el material húmedo se aglomera).
2. Apila tamices de mayor a menor abertura: 40 / 60 / 80 / 100 / 200 + fondo.
3. Vibra 10 min (tamizadora) o agita manualmente 10 min de forma reproducible.
4. Pesa la retención de cada tamiz.
5. Reporta:
     % retenido por malla  y  % acumulado que pasa
     d50 = interpolación donde el acumulado que pasa cruza 50 %

Ejemplo de reporte (ILUSTRATIVO):
   Malla 40  retenido  1,2 %     acumulado pasa 98,8 %
   Malla 60  retenido  9,8 %     acumulado pasa 89,0 %
   Malla 80  retenido 32,4 %     acumulado pasa 56,6 %
   Malla100  retenido 30,1 %     acumulado pasa 26,5 %
   Malla200  retenido 22,0 %     acumulado pasa  4,5 %
   Fondo               4,5 %
   d50 ≈ 175 µm    finos <75 µm = 4,5 %   →  CONFORME con la spec del ejemplo
```

Métodos instrumentales (difracción láser) dan la distribución completa y son mejores, pero para una pyme el
juego de tamices resuelve, cuesta una fracción y es defendible en un expediente.

## Ejemplo aplicado — por qué el laboratorio te dio dos números distintos

Mandas la misma "muestra" de polvo de melena de león a dos laboratorios y te dan 18,2 % y 26,7 % de β-glucano.
Antes de acusar a nadie de `lab shopping` (`113`), revisa esto:

```
Causa probable: SEGREGACIÓN. El polvo sin tamizar se separa por tamaño al transportarse
(los finos bajan, los gruesos suben). Si la parte fina es más rica en pared celular
(donde vive el β-glucano) y la gruesa arrastra material menos activo, cada laboratorio
midió un material distinto — y ambos tienen razón.

Arreglo:
  1. Moler todo a pasar malla 100 antes de muestrear.
  2. Homogeneizar y cuartear (`67`).
  3. Enviar la MISMA muestra homogeneizada a ambos, con contramuestra sellada.
```

Esto es más frecuente que el fraude. Antes de pelear, homogeniza.

## Errores comunes

- Moler sin secar. El material húmedo se apelmaza, tapa el molino y sube la temperatura.
- Especificar "polvo fino" sin malla ni µm: no es una especificación, es un adjetivo.
- Moler todo a 200 mesh "por si acaso": filtración lenta, más finos en suspensión, extracto turbio y pérdidas
  en el filtro.
- No controlar la temperatura de salida y perder terpenos o triterpenos en el propio molino.
- Muestrear del saco sin homogeneizar: garantiza resultados irreproducibles y peleas con el laboratorio.
- Ignorar el riesgo de explosión de polvo y de inhalación: polvo orgánico fino en ambiente cerrado es un
  peligro real; EPP y ventilación no son opcionales (`08`).
- Limpiar mal entre lotes: la contaminación cruzada de especies arruina la identidad que pagaste por verificar.

## Conexión con otros módulos

→ `67-homogeneizacion-y-molienda-de-muestra.md` — la versión analítica: moler para medir, no para producir.
→ `144-extraccion-acuosa-y-decoccion.md` — el paso al que alimenta esta molienda.
→ `154-capsulas-y-encapsulado.md` — por qué el tamaño y la fluidez deciden el llenado de la cápsula.
→ `66-plan-de-muestreo-y-representatividad.md` — segregación y cómo se toma una muestra que represente el lote.
→ `08-seguridad-de-laboratorio-y-epp.md` — polvo, ruido y protección respiratoria.