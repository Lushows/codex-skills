# 95 — qNMR: cuantificación absoluta (pureza sin patrón del mismo compuesto)

qNMR resuelve el problema del huevo y la gallina de la química analítica. Para cuantificar por HPLC
necesitas un patrón puro de tu compuesto; pero ¿quién le midió la pureza al patrón? La respuesta correcta,
en la cadena metrológica moderna, es **qNMR**. La señal de RMN es proporcional al número de núcleos, sin
factor de respuesta que dependa del compuesto: eso convierte a qNMR en un **método primario de razón**
(primary ratio method) reconocido por el BIPM, capaz de asignar pureza másica a un material usando un patrón
**distinto** al analito. Si vendes o compras aislados, extractos estandarizados o estándares de referencia,
esto define cuánto vale realmente lo que tienes.

Términos: **método primario de razón (primary ratio method)** = método cuyo resultado se deriva de
constantes y de una razón medida, sin necesidad de un patrón del mismo analito. **estándar interno
(internal standard)** = compuesto puro certificado que se pesa junto con la muestra. **T1 (spin-lattice
relaxation)** = tiempo que tarda el núcleo en volver al equilibrio; manda el tiempo de espera entre pulsos.
**d1 (relaxation delay)** = ese tiempo de espera. **CRM (Certified Reference Material)** = material con
pureza certificada y trazabilidad al SI.

## Por qué qNMR es primario

El BIPM lo lista como técnica del área de análisis orgánico precisamente por esta propiedad: la intensidad
integrada de una señal es proporcional al número de núcleos que la producen, sin corrección empírica
([BIPM, Quantitative NMR, consultado a agosto de 2026](https://www.bipm.org/en/organic-analysis/qnmr)).
Un detector UV, en cambio, responde según la absortividad de cada molécula: dos compuestos a la misma
concentración dan áreas distintas. Por eso "99 % de área por HPLC-UV" **no es** 99 % de pureza másica.

```
Ecuacion fundamental de qNMR con estandar interno:

           I_x     N_std     M_x      m_std
P_x  =  ------- x ------- x ------ x -------- x  P_std
           I_std    N_x      M_std     m_x

P_x   = pureza masica del analito (% p/p)
I     = integral de la senal elegida
N     = numero de nucleos que originan esa senal
M     = masa molar (g/mol)
m     = masa pesada (mg)
P_std = pureza certificada del estandar interno (% p/p)
```

Todo lo demás son masas molares (constantes) y dos pesadas. Por eso el resultado es absoluto. Cualquier
cuenta de estas va a código: rutea a `Matematicas_lushows` o ejecútala con `decimal`.

## Los CRM que se usan como estándar interno

| Estándar interno típico | Núcleo | Nota |
|---|---|---|
| Ácido benzoico (NIST PS1) | ¹H | Primario, calibrante definitivo de qNMR |
| Maleato de dimetilo, ftalato de dimetilo | ¹H | Señales limpias, sin acoplar |
| Ácido 3,5-dinitrobenzoico | ¹H | Solubles en DMSO-d₆ |
| 4-fluorobenzoico / trifluorotolueno | ¹⁹F | Espectros vacíos, muy limpios |
| Trifenilfosfato | ³¹P | Para fosforados |

NIST emitió un material de referencia de ácido benzoico ultrapuro (PS1) como calibrante primario de qNMR, y
proveedores como Merck comercializan kits de estándares qNMR trazables a NIST o a NMIJ (Japón)
([Sigma-Aldrich / Merck, documentación técnica de CRM para qNMR, consultada a agosto de 2026](https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/analytical-chemistry/calibration-qualification-and-validation/the-international-system-of-units);
[J. AOAC Int. 100(5):1365, CRM para ¹H, ³¹P y ¹⁹F qNMR con trazabilidad al SI](https://academic.oup.com/jaoac/article/100/5/1365/5654283)).

## Cómo se hace bien (los parámetros que no se negocian)

1. **Pesada analítica** de muestra y estándar interno en la misma balanza calibrada, ~5–20 mg cada uno,
   registrando 4 decimales. La pesada es la principal fuente de incertidumbre.
2. **Solvente deuterado** que disuelva ambos por completo. Nada de suspensiones.
3. **d1 ≥ 5 × T1** del protón más lento involucrado (típicamente 30–60 s en ¹H). Este es **el** error
   clásico: un d1 de 2 s da integrales sesgadas hacia abajo para las señales lentas.
4. **Ángulo de pulso 90°** calibrado, o pulso reducido con d1 ajustado en consecuencia.
5. **Sin desacoplamiento NOE** en ¹³C cuantitativo (el NOE distorsiona intensidades); en ¹H no aplica.
6. **Señales elegidas**: aisladas, sin solapamiento, sin protones intercambiables (OH, NH, COOH — se
   intercambian con el agua y su integral no es confiable).
7. **Procesado consistente**: mismo apodizado, corrección de fase manual, línea base plana, integrales con
   límites amplios y simétricos.
8. **Réplicas**: mínimo 3 preparaciones independientes; se reporta media y desviación.

Incertidumbre típica bien hecha: **0,3–1,5 % relativo** (orden de magnitud, ILUSTRATIVO); la mejor
literatura metrológica llega por debajo de 0,3 % en condiciones controladas.

## Quién ofrece qNMR (a agosto de 2026)

- **Institutos nacionales de metrología**: NIST (EE. UU.), NMIJ (Japón), BAM (Alemania), LGC (Reino Unido).
  Son la fuente de los CRM primarios; no hacen servicio de rutina para una pyme.
- **Farmacopeas y organismos**: USP mantiene trabajo publicado sobre qNMR para asignación de valor a sus
  estándares de referencia ([USP, Stimuli article on qNMR](https://www.usp.org/sites/default/files/usp/document/workshops/stimuli-article-qnmr.pdf)).
- **Proveedores de estándares analíticos** (Sigma-Aldrich/Merck TraceCERT, Cerilliant, LGC Standards,
  Restek, Cayman Chemical): usan qNMR internamente para asignar pureza a lo que venden. Ese dato debe
  aparecer en el certificado del patrón: si dice "pureza asignada por qNMR", vas bien.
- **Laboratorios de servicio y universidades con RMN de 400–600 MHz**: en Colombia hay equipos de RMN en
  universidades (Universidad Nacional, Universidad de Antioquia, entre otras). El equipo existe; lo que hay
  que verificar es si el laboratorio corre **qNMR validado** o solo RMN estructural. Confirma alcance y
  acreditación en el directorio de ONAC antes de contratar (ver `107` y `108`).
- **Servicios comerciales de qNMR en el exterior** (Europa, EE. UU., Canadá) con reporte trazable al SI.

## Ejemplo aplicado (ILUSTRATIVO)

Aislado de CBD comprado como "99,2 % por HPLC-UV". Se corre ¹H qNMR con maleato de dimetilo como estándar
interno, DMSO-d₆, 400 MHz, d1 = 60 s, 32 scans, 3 réplicas.

```
m_muestra = 10,214 mg      m_std = 8,047 mg      P_std = 99,7 % p/p
Senal analito : 6,22 ppm, N = 2 H      M_CBD  = 314,46 g/mol
Senal std     : 6,80 ppm, N = 2 H      M_std  = 144,13 g/mol
Razon de integrales I_x / I_std = 0,3546

Pureza masica calculada (3 replicas) : 92,4 % p/p ; DE 0,4
Diferencia contra el COA del proveedor: -6,8 puntos porcentuales
Hipotesis del faltante: solvente residual + agua + un isomero coeluyente
Siguiente paso: Karl Fischer (98), GC headspace (86, 87), LC-HRMS (84)
```

Si le pagas ese material a precio de 99 %, estás pagando ~7 % de más por kilo. En una compra de 5 kg eso es
plata real; el qNMR costó una fracción. (Cifras ilustrativas, no corresponden a ningún proveedor.)

## Errores comunes

- **Confundir pureza cromatográfica de área con pureza másica.** El error más caro del módulo.
- **d1 corto.** Subestima sistemáticamente; el resultado se ve "profesional" y está mal.
- **Integrar señales de OH/NH.** Intercambiables: integral no cuantitativa.
- **Un solo pesaje.** Sin réplicas no hay desviación, y sin desviación no hay resultado defendible.
- **Estándar interno no certificado** o sin pureza declarada: toda la trazabilidad se cae ahí.
- **Solapamiento de señales** ignorado; siempre verifica en el espectro ampliado, no en el reporte.
- **Pedir qNMR para trazas.** No es su oficio: es para el componente mayoritario.

## Conexión con otros módulos

→ `94-rmn-fundamentos.md` — la base que hay que entender antes de cuantificar.
→ `70-patrones-de-referencia-y-trazabilidad.md` — por qué la pureza del patrón define toda la cadena.
→ `80-deteccion-uv-dad-y-pureza-de-pico.md` — por qué el "99 % de área" engaña.
→ `76-incertidumbre-de-medida.md` — cómo se reporta el ± de un resultado primario.
→ `193-cromatografia-preparativa-y-aislados.md` — dónde importa de verdad la pureza de un aislado.
→ `111-banderas-rojas-en-un-coa.md` — "pureza 99 %" sin método declarado es bandera roja.
