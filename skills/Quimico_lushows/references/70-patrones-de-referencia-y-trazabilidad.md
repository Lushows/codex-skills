# 70 — Patrones de referencia y trazabilidad (sin patrón no hay número, hay estimación)

Un cromatógrafo no mide concentración: mide área de pico. Convertir área en miligramos exige comparar contra
una sustancia de pureza conocida, el **patrón**. Si el patrón está mal —vencido, mal pesado, mal disuelto,
de pureza dudosa— todos tus resultados están mal por el mismo factor, y salen preciosos y consistentes. Es
el error más caro y el más difícil de ver desde afuera, porque no deja huella en el cromatograma. Aquí
aprendes qué patrón exigir, cómo se demuestra su trazabilidad y qué preguntar.

Términos:
- **Patrón de referencia (reference standard)** = sustancia de pureza conocida usada para calibrar.
- **CRM (certified reference material)** = material de referencia certificado, con valor asignado,
  incertidumbre y trazabilidad documentada, emitido por un productor acreditado (ISO 17034).
- **Patrón primario (primary standard)** = de la farmacopea (USP, EP) o de un instituto metrológico (NIST).
- **Patrón secundario / de trabajo (working standard)** = el que se usa a diario, calificado contra el primario.
- **Trazabilidad metrológica (metrological traceability)** = cadena ininterrumpida de comparaciones hasta una
  referencia reconocida, cada eslabón con su incertidumbre.

## La jerarquía de patrones

```
SI (kilogramo, mol)
   └── Institutos metrológicos (NIST SRM, BAM, IRMM) y farmacopeas (USP RS, EP CRS)
          └── CRM comerciales bajo ISO 17034 (Cerilliant, Restek, Sigma, LGC…)
                 └── Patrón de trabajo del laboratorio (calificado contra el CRM)
                        └── Tu resultado
```
Cada eslabón agrega incertidumbre. Un laboratorio serio te puede mostrar la cadena completa; uno flojo te
muestra un frasco.

## Qué debe decir el certificado del patrón

| Dato | Por qué importa |
|---|---|
| Identidad (nombre, CAS, estructura) | Que sea el isómero correcto: Δ9-THC ≠ Δ8-THC (`180`) |
| **Pureza y cómo se determinó** | HPLC-área %, qNMR, balance de masa: dan valores distintos |
| Lote y fecha de emisión | Trazabilidad |
| Fecha de vencimiento / reensayo | Los patrones se degradan, sobre todo en solución |
| Condiciones de almacenamiento | −20 °C, oscuridad, atmósfera inerte |
| Contenido de agua y solventes residuales | Un patrón con 3 % de agua da 3 % de error si no se corrige |
| Incertidumbre del valor asignado | Entra en tu presupuesto de incertidumbre (`76`) |
| Acreditación del productor (ISO 17034) | Es lo que lo convierte en CRM y no en "producto químico" |

Punto técnico que separa a los que saben: la **pureza por área de HPLC no es contenido**. Área % ignora todo
lo que no absorba a esa longitud de onda (agua, sales, solventes). El método que da contenido absoluto sin
necesitar un patrón del mismo compuesto es **qNMR** (`95`); por eso los CRM modernos de cannabinoides y de
alcaloides se certifican cada vez más por qNMR.

## Patrones en el mundo real de cannabis y hongos

| Analito | Disponibilidad de CRM a agosto de 2026 | Comentario |
|---|---|---|
| Δ9-THC, THCA, CBD, CBDA, CBN, CBG, CBC, THCV | Amplia, en solución en metanol/acetonitrilo, bajo licencia | En Colombia requieren trámite de importación de sustancia controlada |
| Δ8-THC, HHC, THCP | Existen, calidad variable según proveedor | Verificar isómero y estereoquímica (`179`, `181`) |
| Terpenos (limoneno, mirceno, pineno…) | Amplia, como mezclas | Ojo con la pureza enantiomérica (`43`) |
| Psilocibina, psilocina, baeocistina | Existen como CRM analíticos bajo control | Importación controlada; en Colombia trámite ante la autoridad competente |
| β-glucano | **No hay patrón de calibración convencional**: el método es enzimático con controles del kit | Por eso el método manda más que el patrón (`221`) |
| Ácidos ganodéricos | Limitada, caros; algunos solo como fracción | Dificulta la cuantificación absoluta (`224`) |
| Hericenonas / erinacinas | Muy limitada | Casi nadie los cuantifica de verdad (`226`) |
| Cordicepina, adenosina | Disponible | Cordicepina relativamente asequible (`228`) |
| Ergotioneína | Disponible | (`235`) |
| Metales (Cd, Pb, As, Hg) | Amplia, soluciones trazables a NIST | Baratos comparados con orgánicos |

Consecuencia comercial directa: cuando un proveedor te ofrece "extracto estandarizado al 40 % de
triterpenos", pregúntale **contra qué patrón**. Si la respuesta es "ácido ursólico" o "equivalentes de ácido
oleanólico", te está dando un valor equivalente, no un contenido de ácidos ganodéricos. No es fraude si lo
declara; es fraude si no lo declara.

## Cómo se comprueba

1. **Pide el certificado del patrón (CoA del standard)**, no solo la marca. Debe venir con lote y vencimiento.
2. **Verifica que el laboratorio califique su patrón de trabajo** contra un CRM al menos una vez al año o por
   lote nuevo.
3. **Verificación independiente de la curva**: se prepara un patrón de una fuente distinta (second source
   verification) y se analiza como muestra. Criterio típico: recuperación 97–103 % para analitos mayores.
4. **Corrección por pureza**, siempre:
   ```
   Masa efectiva del analito = masa pesada x pureza (fracción) x (1 - humedad) x (1 - solventes)

   Ejemplo (ILUSTRATIVO): se pesan 25,0 mg de CBD "98,2 % HPLC", con 0,8 % de agua
     25,0 x 0,982 x 0,992 = 24,36 mg de CBD real
     Ignorar la corrección = +2,6 % de error sistemático en TODOS los resultados
   ```
5. **Registro de preparación de soluciones**: fecha, masa, volumen, analista, vigencia asignada.

## Ejemplo aplicado — por qué dos laboratorios difieren 6 % de forma constante

```
Lab A calibra con CRM de Δ9-THC en metanol, pureza certificada por qNMR 99,3 %, corregida.
Lab B calibra con un "estándar analítico" 98 % área HPLC, sin corregir por agua ni solvente.
Sesgo esperado: ~2-4 % (ILUSTRATIVO), sistemático, siempre en el mismo sentido.

Súmale una diferencia de base (uno reporta base seca y otro tal cual, 6 % de humedad)
y tienes 8-10 % de diferencia sin que ningún instrumento haya fallado.
```
Cuando dos COA no cuadran, la primera hipótesis no es "alguien miente": es **patrón y base**.

## Qué preguntarle al laboratorio

1. ¿De qué proveedor son sus patrones y son CRM bajo ISO 17034?
2. ¿Corrigen por pureza, agua y solventes residuales del patrón?
3. ¿Cada cuánto verifican con un patrón de segunda fuente y cuál fue el último resultado?
4. ¿Cómo almacenan y con qué vigencia usan las soluciones de trabajo?
5. Para β-glucano o triterpenos: ¿contra qué se está expresando el resultado (equivalentes de qué)?
6. ¿Tienen licencia vigente para tener patrones de sustancias controladas? (En Colombia, cannabinoides y
   psilocibina la requieren; sin ella el laboratorio no puede cuantificar legalmente.)

## Errores comunes

- **Aceptar "estándar" sin certificado.** Un frasco con etiqueta no es trazabilidad.
- **Usar patrones vencidos**, sobre todo en solución: los cannabinoides ácidos se descarboxilan y la psilocina
  se oxida dentro del vial.
- **No corregir por pureza.** Error sistemático de 1–5 %, invisible y permanente.
- **Confundir "% área HPLC" con contenido.** No es lo mismo (`95`).
- **Cuantificar un analito contra el patrón de otro** sin declararlo ("equivalentes de"). Legítimo si se
  declara, engañoso si no.
- **Guardar patrones en la nevera del almuerzo.** Sin control de temperatura registrado, se cae la
  trazabilidad completa en auditoría.

## Conexión con otros módulos

→ `71-curva-de-calibracion.md` — qué se hace con el patrón.
→ `76-incertidumbre-de-medida.md` — cómo entra el patrón en la incertidumbre.
→ `95-qnmr-cuantificacion-absoluta.md` — cómo se certifica pureza sin patrón del mismo compuesto.
→ `107-iso-17025-y-acreditacion.md` — qué exige la norma sobre trazabilidad.
→ `111-banderas-rojas-en-un-coa.md` — cuando el COA no dice contra qué se calibró.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el caso sin patrón convencional.
