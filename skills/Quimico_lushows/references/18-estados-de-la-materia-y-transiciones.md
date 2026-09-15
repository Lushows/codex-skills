# 18 — Estados de la materia y transiciones (por qué el extracto se apelmaza y el destilado cristaliza)

Los problemas físicos de un producto natural —el polvo que se vuelve piedra en el frasco, el aceite de CBD
que se enturbia en la nevera, el destilado que cristaliza, la cápsula que se ablanda— son transiciones de
fase, no fallas de calidad química. Un lote puede tener el activo perfecto y aun así ser invendible porque
nadie miró la temperatura de transición vítrea ni la humedad de equilibrio. Este módulo te da el
vocabulario para diagnosticar esos fracasos y para pedir el ensayo correcto (DSC, TGA, isoterma de
sorción) en vez de repetir el HPLC que ya salió bien.

Términos: **transición de fase (phase transition)** = cambio entre sólido, líquido y gas o entre formas
sólidas. **transición vítrea (glass transition, Tg)** = temperatura a la que un sólido amorfo pasa de
vidrio rígido a gomoso; en °C. **polimorfismo (polymorphism)** = misma molécula, distintas redes
cristalinas, con distinta solubilidad y punto de fusión. **amorfo (amorphous)** = sólido sin orden
cristalino; más soluble, menos estable. **sublimación (sublimation)** = sólido a gas sin pasar por
líquido; base de la liofilización.

## Los estados que te importan (y uno que casi nadie nombra)

| Estado | Rasgo | Dónde aparece en tu operación |
|---|---|---|
| Cristalino | Red ordenada, punto de fusión definido | CBD aislado, cafeína, cristales de THCA |
| Amorfo | Sin orden, ablanda en un rango (Tg) | Extractos secados por aspersión, resinas de cannabis |
| Gomoso (rubbery) | Amorfo por encima de Tg | El polvo que se apelmaza en climas húmedos |
| Líquido viscoso | Fluye, sin orden | Destilado de cannabinoides, oleorresinas |
| Emulsión / coloide | Dos fases dispersas | Bebidas y nanoemulsiones de CBD (`32`, `157`) |
| Gas / vapor | — | Solventes residuales en headspace (`86`, `87`) |

La mayoría de los extractos naturales son **amorfos**, no cristalinos. Eso significa que no tienen punto de
fusión: tienen Tg. Y la Tg baja cuando entra agua, porque el agua es plastificante. Ahí está la explicación
completa del polvo que se convierte en ladrillo.

## Transición vítrea: el concepto que salva productos en polvo

```
Tg_seco (extracto rico en azúcares/glucanos)   ≈ 40–80 °C   (ILUSTRATIVO, medir por DSC)
Cada +1 % de humedad puede bajar Tg varias decenas de °C  (efecto plastificante del agua)
Si T_almacenamiento > Tg  →  el polvo fluye, se pega, se apelmaza (caking) e irreversiblemente
                              cambia de aspecto aunque el activo siga intacto
```

Regla operativa: un extracto en polvo debe almacenarse con su Tg **al menos 20 °C por encima** de la
temperatura ambiente esperada. En Bogotá (~19 °C) tienes margen; en Barranquilla o en un contenedor a
45 °C, no. Se corrige bajando la actividad de agua (`35`), añadiendo un portador de Tg alta
(maltodextrina de bajo DE, sílice) o cambiando el envase.

## Diagrama de fases, en cristiano

| Concepto | Qué significa para ti |
|---|---|
| Punto triple | Coexisten sólido, líquido y gas; base de la liofilización |
| Punto crítico | Por encima, no hay distinción líquido/gas: es el CO2 supercrítico (`148`) |
| Curva de presión de vapor | Bajar presión baja el punto de ebullición: destilación al vacío (`29`) |
| Eutéctico | Mezcla que congela a T menor que sus componentes; importa en congelado previo a liofilizar |

La liofilización (freeze-drying) funciona exactamente por el punto triple del agua (0,01 °C, 611 Pa):
congelas, bajas presión por debajo de 611 Pa y el hielo sublima sin pasar por líquido. Por eso conserva
estructuras frágiles y por eso es cara (`150`).

## Cómo se mide

| Propiedad | Técnica | Unidad | Qué decides con eso |
|---|---|---|---|
| Tg | DSC (calorimetría diferencial de barrido) | °C | Condiciones de almacenamiento y envase (`99`) |
| Punto de fusión / polimorfo | DSC + difracción de rayos X en polvo | °C / patrón | Si tu aislado va a cristalizar en el aceite |
| Pérdida por secado y descomposición | TGA (termogravimetría) | % p/p vs °C | Humedad, solventes ocupluidos, estabilidad térmica |
| Humedad exacta | Karl Fischer | % p/p | Base seca y riesgo de caking (`98`) |
| Actividad de agua | Higrómetro de punto de rocío | aw, 0–1 | Vida útil microbiológica y física (`35`) |
| Comportamiento de flujo del polvo | Ángulo de reposo, índice de Carr | ° / % | Encapsulado sin atascos (`143`, `154`) |

Orden de magnitud: para polvo de hongo estable se apunta a humedad baja y aw por debajo de 0,6; el valor
exacto se fija con tu propio estudio, no copiándolo (`164`).

## Ejemplo aplicado

Un lote de extracto de melena de león secado por aspersión llega bien y a las 6 semanas en bodega el
cliente reclama "piedras" **(ILUSTRATIVO)**:

```
Al empaque:   humedad 4,2 % (KF)   aw 0,32   Tg (DSC) 52 °C   aspecto: polvo suelto
A 6 semanas:  humedad 8,9 % (KF)   aw 0,61   Tg (DSC) 29 °C   aspecto: torta compacta
Bodega:       28–34 °C, HR 70–80 % (Cali, sin control)
Envase:       bolsa de polietileno simple, sin barrera de vapor ni desecante
Potencia:     β-glucano 30,1 % → 29,8 % p/p b.s. (sin cambio significativo)
```

Diagnóstico: la química no falló, la física sí. El polietileno simple deja pasar vapor; el extracto ganó
agua, la Tg cayó por debajo de la temperatura de bodega y el polvo entró en estado gomoso. La solución no
es cambiar el extracto: es envase multicapa con barrera (aluminio/EVOH), desecante, y una especificación de
aw máxima en la orden de compra (`163`, `247`). Verifica el cálculo de vida útil y las condiciones con
`165` y ejecuta las cuentas en código (`Matematicas_lushows`).

## Errores comunes

- Diagnosticar un apelmazamiento repitiendo el análisis de potencia. El activo casi siempre está intacto;
  el problema es humedad y Tg.
- Especificar solo "humedad ≤ X %" sin especificar actividad de agua. Dos matrices con la misma humedad
  pueden tener aw muy distinta (`35`).
- Guardar destilado de cannabinoides en frío esperando que "se conserve mejor" y encontrarlo cristalizado
  y separado: la nucleación aumenta al bajar temperatura.
- Liofilizar sin congelar bien primero. Si la muestra se funde parcialmente en la cámara, colapsa y
  pierdes la estructura porosa que justificaba el costo (`150`).
- Asumir que un extracto amorfo tiene punto de fusión. No lo tiene; pedir "punto de fusión" a un
  laboratorio para un extracto es pedir un dato que no existe.
- Cambiar de envase por costo sin repetir el estudio de estabilidad. El envase es parte de la
  especificación (`164`).

## Conexión con otros módulos

→ `28-gases-y-presion-de-vapor.md` — la curva que gobierna secado y destilación.
→ `35-actividad-de-agua-y-humedad.md` — aw, isotermas y vida útil del polvo de hongo.
→ `99-analisis-termico-dsc-y-tga.md` — cómo se corren esos ensayos y qué se lee.
→ `150-secado-por-aspersion-y-liofilizacion.md` — las dos rutas para llegar a polvo.
→ `163-envase-primario-y-compatibilidad.md` — barrera de vapor y compatibilidad.
→ `164-estabilidad-ich-q1-y-vida-util.md` — cómo se demuestra la vida útil con datos.