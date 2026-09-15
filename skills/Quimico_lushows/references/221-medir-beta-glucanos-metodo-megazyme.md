# 221 — Medir beta-glucanos: el método Megazyme K-YBGL, paso a paso

Este es el módulo operativo del bloque: el ensayo concreto que convierte una discusión de marketing en un
número defendible. El kit **Megazyme K-YBGL (β-Glucan Assay Kit, Yeast & Mushroom)** es el estándar de facto
de la industria de hongos, y su lógica es simple: mide **glucano total**, mide **α-glucano**, y el
β-glucano es **la resta**. Si sales de aquí sabiendo pedirlo bien y leerlo bien, ya no te venden arroz.

Términos: **GOPOD (glucose oxidase/peroxidase reagent)** = reactivo que convierte glucosa en color medible
por absorbancia. **amiloglucosidasa (amyloglucosidase, AMG)** = enzima que corta α-glucanos a glucosa.
**invertasa (invertase)** = enzima que corta sacarosa. **exo-1,3-β-glucanasa + β-glucosidasa** = par
enzimático que corta β-glucano a glucosa en la variante enzimática. **base seca (dry basis)** = resultado
corregido por humedad.

## La ecuación que gobierna todo

```
beta-glucano  =  glucano total  -  alfa-glucano

donde:
  glucano total : hidrolisis acida controlada (H2SO4 concentrado en frio,
                  luego diluido y calentado) que rompe TODO glucano a glucosa.
                  Incluye tambien glucosa libre y la glucosa de la sacarosa.
  alfa-glucano  : hidrolisis ENZIMATICA especifica con amiloglucosidasa
                  (almidon y glucogeno) + invertasa (sacarosa).
                  Incluye igualmente glucosa libre.

En ambas ramas la glucosa liberada se mide con GOPOD por absorbancia a 510 nm
frente a un estandar de D-glucosa.
```

Como la glucosa libre y la sacarosa entran en **las dos** ramas, se cancelan en la resta. Ese es el truco
elegante del método. Documentación: Megazyme, kit K-YBGL (megazyme.com y support.megazyme.com); la
determinación por diferencia para hongos y productos miceliales está publicada en *Journal of AOAC
International* (McCleary y Draga, 2016).

## El procedimiento, en el orden en que ocurre

1. **Muestreo y molienda.** Muestra representativa, molida a paso de malla fina y homogénea. Un producto mal
   molido da resultados dispersos; este es el error operativo más frecuente (ver `66`, `67`).
2. **Humedad en paralelo.** Se determina humedad (Karl Fischer o pérdida por secado) sobre la misma muestra
   para poder reportar en base seca (ver `98`, `07`).
3. **Rama de glucano total.** Alícuota (del orden de 100 mg) + H₂SO₄ concentrado en frío para hinchar y
   solubilizar; se diluye y se calienta para completar la hidrólisis; se neutraliza; se toma alícuota.
4. **Rama de α-glucano.** Otra alícuota se trata con KOH para solubilizar el almidón/glucógeno, se
   neutraliza con buffer y se incuba con **amiloglucosidasa + invertasa**.
5. **Cuantificación con GOPOD.** Ambas alícuotas se incuban con el reactivo GOPOD; se lee absorbancia a
   510 nm contra estándar de D-glucosa y contra blanco de reactivo.
6. **Control del kit.** El kit incluye un control (material de referencia) para verificar que la hidrólisis
   y el GOPOD funcionaron. **Exige que el laboratorio lo corra y lo reporte**; sin control, el número no
   está respaldado.
7. **Cálculo.** Cada rama se expresa como glucosa × factor de conversión a polímero (0,90, porque al
   hidrolizar se suma agua) y se resta. El resultado se corrige a base seca.

```
% glucano (p/p) = (A_muestra / A_estandar) x (concentracion estandar) x F x 0,90 x (V/m) x 100
% en base seca  = % en base humeda / (1 - humedad/100)
```

No hagas esa cuenta de memoria: pásala a `lab-tools/base_seca.py` o a `Matematicas_lushows`.

## Qué reporta y en qué unidad

| Renglón que debe aparecer en el informe | Unidad |
|---|---|
| Glucano total | `% p/p base seca` |
| α-glucano | `% p/p base seca` |
| β-glucano (por diferencia) | `% p/p base seca` |
| Humedad de la muestra y método | `% p/p` |
| Método y referencia (Megazyme K-YBGL / AOAC) | texto |
| Lote, fecha de recepción, fecha de análisis | texto |
| Resultado del control del kit | `%` de recuperación |

Si el informe dice solo "β-glucano 30 %" sin base, sin método y sin lote, no es un resultado: es una
afirmación (ver `110`, `111`).

## Costo y tiempo (orden de magnitud)

**(ILUSTRATIVO — verifica con tu laboratorio; los precios cambian y varían por país):**

| Ítem | Orden de magnitud |
|---|---|
| Ensayo β/α-glucano en laboratorio comercial | decenas a bajas centenas de USD por muestra |
| Tiempo de respuesta típico | del orden de 1 a 3 semanas |
| Kit K-YBGL completo (si lo corre una universidad) | centenas de USD, rinde ~100 ensayos |
| Ensayo adicional de humedad | costo menor, súmalo siempre |

En Colombia, esto se puede correr en laboratorios universitarios (la UDCA entre ellos) o enviarse fuera.
Si el laboratorio no tiene el kit, cotiza el kit tú y negocia el tiempo de equipo (ver `292`).

## Qué pedirle exactamente al laboratorio

Copia y pega esto en el correo de cotización:

```
Solicito determinacion de beta-glucano y alfa-glucano por metodo enzimatico
Megazyme K-YBGL (beta-glucano = glucano total - alfa-glucano), en muestra de
[extracto de hongo / polvo de cuerpo fructifero].

Necesito que el informe reporte:
  - glucano total, alfa-glucano y beta-glucano, cada uno en % p/p BASE SECA
  - humedad de la muestra con el metodo usado
  - referencia del metodo y del kit, y numero de lote del kit
  - resultado del control incluido en el kit
  - identificacion de mi lote, fechas de recepcion y de analisis
  - nombre y firma del responsable tecnico

Analisis por duplicado. Indicar si el laboratorio esta acreditado ISO 17025
para este ensayo o si es un ensayo fuera de alcance de acreditacion.
```

Ese último punto importa: muchos laboratorios corren el ensayo bien pero **fuera del alcance acreditado**.
No es un problema si lo sabes y lo dejas escrito (ver `107`).

## Ejemplo aplicado — leer un resultado real de BIO-SETA

**(ILUSTRATIVO)**

```
Muestra: Extracto de reishi, lote BS-R-2026-07
   glucano total   31,8 % p/p base seca
   alfa-glucano     3,4 % p/p base seca
   beta-glucano    28,4 % p/p base seca
   humedad          4,2 % (Karl Fischer)
   control del kit  recuperacion 98,6 %

Lectura: alfa bajo -> consistente con cuerpo fructifero, sin grano.
Beta 28,4 % -> dentro del rango que la literatura reporta para material
autentico (25-66 % segun Nammex). Se acepta el lote.
```

## Limitaciones honestas del método

- **No dice qué especie es.** Un β-glucano de levadura da un número parecido. La identidad se resuelve con
  ITS (ver `245`).
- **No mide peso molecular ni solubilidad**, que probablemente importan más para la actividad (ver `219`).
- Muestras con mucha azúcar añadida o con polisacáridos no glucánicos pueden complicar la interpretación.
- La hidrólisis ácida incompleta subestima el glucano total: por eso el control del kit no es opcional.
- Es un método de diferencia: un error en cualquiera de las dos ramas se traslada íntegro al resultado.

## Errores comunes

- Pedir "beta-glucano" y aceptar que el laboratorio te dé "polisacáridos" (ver `222`).
- No pedir el α-glucano. Te quedas sin la señal de fraude.
- Recibir el resultado en base húmeda y compararlo con uno en base seca.
- Analizar la materia prima y no el producto terminado: la cápsula lleva excipientes y el número cambia.
- Un solo lote como especificación. Se necesitan varios lotes y un rango (ver `282`).

## Conexión con otros módulos

→ `220-alfa-glucanos-y-almidon-el-confusor.md` — la química que sostiene la resta.
→ `222-polisacaridos-totales-por-que-no-sirve.md` — el método que hay que dejar de aceptar.
→ `07-base-seca-vs-humeda.md` — la corrección sin la cual nada es comparable.
→ `110-como-leer-un-coa.md` y `111-banderas-rojas-en-un-coa.md` — cómo auditar el informe.
→ `114-costos-y-tiempos-de-analisis.md` — presupuesto del plan analítico.
→ `247-especificacion-de-producto-de-hongos.md` — cómo se vuelve especificación.