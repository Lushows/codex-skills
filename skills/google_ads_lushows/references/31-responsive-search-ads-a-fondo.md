# 31 — Responsive Search Ads a fondo

Lee este módulo cuando vayas a crear o reescribir un anuncio de Search, te aparezca "Ad Strength: Bajo/Medio" y no sepas qué tocar, o no entiendas por qué tu anuncio a veces se ve distinto cada vez que buscas.

El **RSA (Responsive Search Ad)** es HOY, en 2026, el único formato de texto que existe en Search. Los viejos Expanded Text Ads (donde tú elegías el orden exacto de 3 títulos) murieron — Google los eliminó hace años. Hoy tú entregas muchas piezas y Google las arma como un Lego: para cada búsqueda elige la combinación que cree que dará más clics. Esto te da alcance, pero te quita control. Este módulo es cómo recuperar el control que importa sin pelear con la máquina. Es el corazón del bloque de Search: aquí se escribe lo que el usuario lee, y todo lo demás (Quality Score 36, ángulos 38, match 37) se apoya en hacerlo bien.

## Cómo funciona el RSA (la materia prima)

| Componente | Cuántos puedes dar | Cuántos muestra Google | Límite por pieza |
|---|---|---|---|
| Títulos (headlines) | hasta 15 | normalmente 2-3 | 30 caracteres |
| Descripciones | hasta 4 | normalmente 2 | 90 caracteres |
| Paths de URL | 2 | 2 | 15 caracteres c/u |

Google mezcla y rota: prueba combinaciones, mide cuáles convierten y va favoreciendo las ganadoras. Por eso ves el anuncio "distinto" — es la misma materia prima recombinada. No le des solo 3 títulos: dale 12-15 reales y variados para que tenga con qué experimentar. 15 títulos casi idénticos no sirven; quieres 15 ángulos distintos (ver 38). La regla mental: cada título es una carta de la baraja; Google reparte la mejor mano para cada búsqueda, pero solo puede jugar con las cartas que le diste.

### Los 15 títulos completos (ejemplo real, calculadora gastronómica)

Reparto recomendado, listo para copiar y adaptar. Cada uno cabe en 30 caracteres:

| # | Título | Ángulo |
|---|---|---|
| 1 | Calculadora de Costos Gastro | keyword exacta |
| 2 | Calculadora Costos Restaurante | keyword + segmento |
| 3 | Costos para tu Cocina | keyword variante |
| 4 | Sabe Cuánto Ganas por Plato | beneficio |
| 5 | Deja de Perder Plata | beneficio (dolor) |
| 6 | Fija Precios sin Adivinar | beneficio |
| 7 | Controla tu Food Cost Real | beneficio (jerga) |
| 8 | Descárgala Hoy Mismo | CTA + urgencia |
| 9 | Pruébala Ya, Es Inmediata | CTA |
| 10 | Pago Único $10.000 COP | precio/oferta |
| 11 | Sin Mensualidad, para Siempre | precio (anti-suscripción) |
| 12 | +2.000 Negocios la Usan | confianza/prueba |
| 13 | Hecha en Colombia | local/confianza |
| 14 | Funciona en Excel, Sin Instalar | diferenciador técnico |
| 15 | Acceso Digital Inmediato | beneficio operativo |

> **Food cost** = el costo de los ingredientes de un plato como % de su precio de venta; es la métrica madre de un restaurante. Explicarla así dentro del anuncio (título 7) capta justo al dueño que sufre con eso.

Así Google siempre tiene una keyword + un beneficio + un cierre + una prueba para combinar, gane lo que gane su algoritmo. Reparto resumido: 3-4 con keyword exacta (reconocimiento, ver 30), 3-4 con beneficio, 2-3 con CTA, 2-3 con confianza/prueba, 2 con precio/oferta.

### Las 4 descripciones

Tienes 90 caracteres por descripción. Escribe las 4 distintas:

1. "Calcula el costo real de cada plato y fija precios con margen. Pago único, sin mensualidad."
2. "Funciona en Excel, sin instalar nada. Acceso digital inmediato por solo $10.000 COP."
3. "Más de 2.000 restaurantes, cafeterías y dark kitchens en Colombia ya la usan."
4. "Deja de perder plata por no saber cuánto te cuesta cada plato. Descárgala hoy mismo."

## Ad Strength y pinning (control con criterio)

**Ad Strength** ("Eficacia del anuncio": Baja → Media → Buena → Excelente) es un medidor que Google muestra mientras escribes. Mide variedad y cantidad, NO si vendes. Es una guía, no una garantía: he visto anuncios "Buena" rendir mejor que "Excelente". Apunta a Buena/Excelente porque suele correlacionar con más alcance, pero **nunca sacrifiques un buen mensaje por subir la barrita**. Si para llegar a "Excelente" tienes que meter títulos genéricos que no dicen nada, no lo hagas. La barrita no paga la nómina; las conversiones sí.

**Pinning (fijar/anclar)**: forzar que un título o descripción aparezca siempre, y en una posición fija (1, 2 o 3). Fijar BAJA el Ad Strength porque le quitas combinaciones a Google. Úsalo con criterio:

| Cuándo SÍ fijar | Cuándo NO fijar |
|---|---|
| Marca obligatoria en posición 1 | El resto de los títulos |
| Texto legal/regulatorio que debe salir igual | "Porque quiero controlar todo" |
| Disclaimers de precio | Beneficios y CTAs (déjalos rotar y competir) |
| Cumplir una política (ej. "resultados no garantizados") | Por inseguridad de soltar el control |

Regla práctica: fija lo que LEGALMENTE o por MARCA no puede faltar, y deja todo lo demás rotando para que Google encuentre al ganador. Truco avanzado: si fijas 2-3 títulos en la MISMA posición, Google rota entre ESOS para esa posición — útil para variantes de marca o para garantizar que la posición 1 siempre tenga keyword sin matar del todo la rotación.

## Cuántos RSA por grupo de anuncios

**1, máximo 2 RSA por grupo de anuncios.** No 5. Razón: cada grupo tiene un presupuesto de impresiones; si metes 5 anuncios, cada uno recibe pocos datos y Google tarda muchísimo en saber cuál gana. Con 1-2 anuncios bien hechos, los datos se concentran y aprende rápido. Si quieres probar dos enfoques distintos, mete 2 RSA y deja correr 2-3 semanas con tráfico real antes de juzgar (ver 60 para métricas, ver 61 para diagnóstico, ver 17 para framework de testing).

Cada grupo de anuncios debe ser de UN solo tema, con sus keywords de ese tema, su RSA de ese tema y su landing de ese tema. Eso es lo que sube el Quality Score (ver 36, 37). Un RSA "para todo" diluye el match y te sale caro. La estructura correcta — un grupo, un tema, un anuncio, una landing — está a fondo en el módulo 37, que es la columna vertebral de toda la sección.

## Una nota sobre DSA y RSA con IA (2026)

Existen las **DSA (Dynamic Search Ads)**, donde Google genera el título automáticamente leyendo tu web y tú solo escribes la descripción — útiles para catálogos grandes o para descubrir keywords que no se te ocurrieron (ver 56). No reemplazan al RSA bien hecho; son complemento. En 2026 Google también empuja sugerencias de títulos generadas por IA dentro del editor del RSA: úsalas como punto de partida, nunca tal cual. La IA no conoce tu ángulo dominante ni las objeciones de tu cliente; tú sí (ver 38, y `ventas_lushows`).

## Errores comunes — blacklist

- **Dar solo 3-4 títulos**: le quitas a Google la materia prima para optimizar; subutilizas el formato. Dale 12-15 ángulos reales.
- **15 títulos que dicen lo mismo**: variedad de longitud sí, pero también de ÁNGULO (keyword, beneficio, CTA, confianza, precio). Repetir no es variar (ver 38).
- **Fijar (pin) todo para "controlar"**: matas la optimización de Google y bajas el alcance; fija solo marca/legal.
- **Perseguir "Excelente" a costa del mensaje**: Ad Strength es guía, no garantía de ventas; un mensaje claro vale más que la barrita verde.
- **Meter 5 RSA por grupo**: fragmentas los datos, ninguno aprende; usa 1-2.
- **Un RSA genérico para todos los grupos**: rompe el match keyword→anuncio→landing y baja el Quality Score (ver 37). Un grupo, un tema, un anuncio.
- **Juzgar el anuncio en 3 días**: sin volumen suficiente (clics/conversiones) la comparación es ruido. Espera datos reales (ver 60).
- **Aceptar los títulos de IA de Google tal cual**: son genéricos, no conocen tu ángulo; edítalos o reemplázalos (ver 38).
