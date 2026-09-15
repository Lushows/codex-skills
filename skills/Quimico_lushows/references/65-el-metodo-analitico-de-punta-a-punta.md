# 65 — El método analítico de punta a punta (de la bodega al número del COA)

Cuando el laboratorio te entrega "28,4 % de beta-glucano", ese número no nació en el instrumento: nació
en la bodega, cuando alguien metió la mano en un saco. El instrumento es el último 10 % de la cadena y casi
nunca es el que se equivoca. Este módulo te da el mapa completo de las ocho etapas por las que pasa una
muestra, dónde se pierde de verdad la exactitud, cuánto cuesta y demora cada tramo, y qué preguntar en cada
punto. Si contratas laboratorios y no operas los equipos, este es el módulo que más plata te ahorra: te
enseña a auditar el proceso, no el cromatograma.

Términos:
- **Analito (analyte)** = la sustancia que se quiere medir (β-glucano, Δ9-THC, plomo, psilocibina).
- **Matriz (matrix)** = todo lo demás de la muestra (fibra, almidón, grasa, resina) que estorba la medida.
- **Alícuota (aliquot)** = la porción que realmente entra al análisis, típicamente 0,1–2 g de un lote de 200 kg.
- **Trazabilidad (traceability)** = poder rastrear el número hasta un patrón certificado y hasta el saco físico.
- **Cadena de custodia (chain of custody)** = el registro firmado de quién tuvo la muestra y cuándo.

## Las ocho etapas y dónde se pierde la exactitud

| # | Etapa | Qué pasa | Error típico si se hace mal | Quién lo controla |
|---|---|---|---|---|
| 1 | Definir la pregunta | ¿Liberas lote, registras producto, auditas proveedor? | Pides el ensayo equivocado y pagas dos veces | Tú |
| 2 | Muestreo (sampling) | Tomar incrementos del lote | El más grande de todos: 20–200 % de sesgo | Tú o el lab |
| 3 | Reducción y homogeneización | Cuarteo, molienda, tamizado | 10–50 % si el material está segregado | Lab (o tú) |
| 4 | Preparación (sample prep) | Pesada, secado, digestión, extracción | 5–30 %; recuperación incompleta | Lab |
| 5 | Separación | HPLC, GC, o ninguna | Coelución = sobreestimación | Lab |
| 6 | Detección | UV-DAD, MS, FID, ICP-MS | Interferencia, saturación | Lab |
| 7 | Cuantificación | Curva de calibración, patrón, factor | Patrón malo = todo el número malo | Lab |
| 8 | Reporte | Unidad, base, LOQ, incertidumbre | Base húmeda vs seca: 5–15 % de diferencia | Ambos |

La lección dura: **la varianza total del resultado es la suma de las varianzas de cada etapa**, y en materiales
sólidos heterogéneos (flor de cannabis, polvo de hongos, granel) el muestreo suele aportar más varianza que
todo el instrumento junto.

```
s²_total = s²_muestreo + s²_preparación + s²_análisis

Presupuesto de varianza (ILUSTRATIVO) para flor de cannabis:
  muestreo       s = 12 %  →  s² = 144
  preparación    s =  4 %  →  s² =  16
  análisis HPLC  s =  2 %  →  s² =   4
  ------------------------------------------
  s_total = raíz(164) = 12,8 %

Comprar un HPLC "mejor" (s de 2 % a 1 %) baja el total a 12,7 %.
Duplicar los incrementos de muestreo (s de 12 % a 8,5 %) lo baja a 9,4 %.
```
Es decir: pagar por un instrumento más fino cuando el muestreo es malo es tirar la plata.

## Costo y tiempo, en orden de magnitud

Precios de laboratorio privado en Colombia, **(ILUSTRATIVO)** — pide siempre cotización, varían por volumen,
acreditación y si es lote de rutina o desarrollo:

| Ensayo | Técnica | Unidad que reporta | Costo aprox. COP | Tiempo típico |
|---|---|---|---|---|
| Potencia cannabinoides (10–16 analitos) | HPLC-DAD | % p/p base seca | 250.000–500.000 | 3–7 días |
| β-glucano / α-glucano | Enzimático Megazyme | % p/p base seca | 300.000–600.000 | 5–10 días |
| Metales pesados (Cd, Pb, As, Hg) | ICP-MS | mg/kg (ppm) | 250.000–600.000 | 5–10 días |
| Pesticidas multiresiduo | LC-MS/MS + GC-MS/MS | mg/kg (ppm) | 700.000–1.800.000 | 7–15 días |
| Solventes residuales | HS-GC-FID/MS | ppm (µg/g) | 300.000–700.000 | 5–10 días |
| Micotoxinas (aflatoxinas, OTA) | LC-MS/MS | µg/kg (ppb) | 300.000–700.000 | 5–10 días |
| Humedad | Gravimetría / Karl Fischer | % p/p | 60.000–150.000 | 2–4 días |
| Identidad de especie | PCR/ITS sequencing | especie + % identidad | 400.000–900.000 | 10–20 días |

Regla de bolsillo: un panel completo de liberación de lote para un suplemento anda en **1,5–3 millones COP**
y **2–3 semanas**. Presupuéstalo por lote, no por año (ver `291-costos-de-analisis-y-presupuesto.md`).

## Cómo se comprueba que la cadena está sana

No puedes ver el HPLC, pero sí puedes exigir evidencia documental de cada etapa:

1. **Muestreo:** protocolo escrito con número de incrementos, masa total y método de reducción (`66`).
2. **Recepción:** acta de recepción con masa recibida, estado y temperatura; cadena de custodia firmada (`109`).
3. **Preparación:** que el COA diga si se secó, a qué temperatura, y en qué base reporta (`07`, `68`).
4. **Calibración:** patrón certificado (CRM) con lote, proveedor y vigencia; curva con R² y número de puntos (`70`, `71`).
5. **Control de calidad de la corrida:** blanco, muestra fortificada (spike) con % de recuperación, duplicado (`77`).
6. **Reporte:** unidad, base, LOQ del método, incertidumbre expandida, alcance acreditado ISO 17025 (`107`, `110`).

Si el laboratorio no te puede mostrar 4, 5 y 6, no tienes un resultado analítico: tienes una opinión con membrete.

## Ejemplo aplicado — un lote de polvo de melena de león para BIO-SETA

Lote de 120 kg en 6 bultos de 20 kg. Decisión que depende del resultado: liberar o no liberar para encapsular.

```
Etapa 1  Pregunta: ¿cumple la especificación de β-glucano >= 20 % p/p base seca
         y Cd <= límite de la norma aplicable?
Etapa 2  Muestreo: 6 bultos, 3 incrementos por bulto (superior/medio/fondo) = 18 incrementos
         de ~50 g → muestra compuesta 900 g
Etapa 3  Reducción: molienda a malla 40 y cuarteo hasta 100 g → muestra de laboratorio
Etapa 4  Envío: 2 frascos ámbar de 50 g, sellados, con acta de custodia; se guarda una
         contramuestra de 100 g en la empresa (esto es lo que te salva si hay disputa, ver 112)
Etapa 5  Ensayos: β-glucano (Megazyme K-YBGL), humedad, Cd/Pb/As/Hg (ICP-MS)
Etapa 6  Reporte esperado: "β-glucano 24,1 % p/p base seca; humedad 6,8 % p/p;
         Cd 0,08 mg/kg base seca (LOQ 0,01)"   (ILUSTRATIVO)
Etapa 7  Decisión: comparar contra la especificación escrita del producto (282)
```
Sin la contramuestra y sin el acta, si el número sale mal no puedes discutir nada: el proveedor dirá que el
problema fue tuyo y tendrá razón formalmente.

## Errores comunes

- **Pedir "análisis de hongos" sin decir el analito.** El lab cotiza lo más barato (polisacáridos totales) y
  te entrega un número que no sirve para tu etiqueta. Especifica analito, método y base (`222`).
- **Muestrear con la mano por la boca del saco.** El fino se asienta al fondo y el grueso sube; la boca del
  saco no representa nada. Sesgo de decenas de por ciento (`66`).
- **Comparar dos COA con humedades distintas.** 8 % vs 3 % de humedad ya son ~5 % de diferencia relativa
  antes de tocar el analito (`07`).
- **No pedir el LOQ.** "No detectado" sin LOQ es una frase vacía: no sabes si el método detecta 0,01 o
  10 mg/kg (`73`).
- **Cambiar de laboratorio para conseguir el número que quieres.** Eso es lab shopping y es rastreable; te
  hunde en una auditoría (`113`).
- **No guardar contramuestra.** Sin ella no hay impugnación posible (`112`).

## Conexión con otros módulos

→ `66-plan-de-muestreo-y-representatividad.md` — la etapa que más error aporta, en detalle.
→ `68-preparacion-de-muestra-solidos.md` — pesada, secado y digestión.
→ `75-validacion-de-metodos-ich-q2-r2.md` — cómo se demuestra que el método sirve.
→ `108-como-elegir-un-laboratorio.md` — a quién le entregas la cadena.
→ `110-como-leer-un-coa.md` — cómo se audita el papel que te devuelven.
→ `114-costos-y-tiempos-de-analisis.md` — presupuesto y planeación.
