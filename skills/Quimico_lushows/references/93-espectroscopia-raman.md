# 93 — Espectroscopía Raman (identificar sin abrir el frasco, y sus límites reales)

Raman es la técnica que más impresiona en una demo y la que más se sobrevende. Ilumina la muestra con un
láser y mide la luz que rebota con la energía cambiada por las vibraciones de las moléculas. Su gracia
práctica: **atraviesa vidrio y plástico transparente**, así que puedes identificar un solvente sin destapar
el frasco, y no le molesta el agua. Su límite práctico: la **fluorescencia** de casi cualquier extracto
vegetal o fúngico oscuro ahoga la señal. Vale la pena saber cuándo pedirla y cuándo es plata botada.

Términos: **dispersión Raman (Raman scattering)** = fracción mínima de la luz que rebota con energía
cambiada. **desplazamiento Raman (Raman shift, cm⁻¹)** = eje x, la diferencia de energía. **fluorescencia
(fluorescence)** = emisión de la muestra que satura el detector y esconde el espectro Raman.
**SERS (Surface-Enhanced Raman Spectroscopy)** = Raman amplificado con nanopartículas metálicas, gana
sensibilidad enorme a costa de reproducibilidad.

## Raman vs FTIR: son complementarias, no sustitutas

| | Raman | FTIR |
|---|---|---|
| Regla de selección | Cambio de polarizabilidad | Cambio de momento dipolar |
| Enlaces que ve fuerte | C=C, C-S, S-S, anillos aromáticos, esqueleto de carbono | O-H, C=O, C-O, N-H |
| Agua | Casi invisible: **puedes medir en solución acuosa** | Interfiere fuerte |
| Vidrio / plástico | Los atraviesa (identificación sin abrir) | No |
| Enemigo #1 | Fluorescencia de la matriz | Humedad |
| Muestra oscura o coloreada | Mala: absorbe el láser, puede quemarse | Sin problema con ATR |

Una banda intensa en Raman suele ser débil en IR y viceversa. Para una identificación robusta, el par
Raman + FTIR es mucho más fuerte que cualquiera de las dos sola.

## Dónde Raman sí gana

- **Identificación de solventes y reactivos entrantes** sin abrir el envase: etanol, isopropanol, acetona,
  heptano, acetonitrilo. Reduce riesgo de mezclas y de contaminación cruzada.
- **Polimorfos y estado sólido**: dos formas cristalinas del mismo principio activo dan espectros distintos.
  Relevante en aislados de cannabinoides (CBD cristalino vs amorfo) y en excipientes.
- **Materiales de empaque**: distinguir PET de PP de PE en la línea (ver `163`).
- **Detección de adulterantes en polvos claros**: sustitución con azúcar, celulosa, dióxido de titanio.
  El TiO₂ da bandas muy intensas y características (anatasa ~144 cm⁻¹): es delator.
- **Mapeo de distribución** (Raman imaging): ver si el activo quedó bien repartido en una tableta.

## Dónde Raman se cae

- **Extractos oscuros** (chaga, reishi, propóleo, aceites full spectrum de cannabis): fluorescencia masiva.
  Mitigaciones: láser de 785 nm o 1064 nm en vez de 532 nm, *photobleaching* previo, corrección de línea
  base. Aun así muchas veces no se recupera nada usable.
- **Trazas**: Raman convencional es poco sensible. Detecta componentes mayoritarios, típicamente por encima
  de ~1 % p/p (orden de magnitud, depende del compuesto y del equipo). Para ppm hay que ir a MS.
- **Cuantificación exacta sin modelo**: igual que NIR, necesita quimiometría y calibración propia (`105`).
- **Muestras que se calientan**: el láser puede degradar o quemar material seco y oscuro. Baja potencia,
  gira la muestra.

## Cómo se comprueba

1. **Calibración del eje**: patrón de silicio, banda a 520,7 cm⁻¹. Verificación diaria.
2. **Respuesta de intensidad**: estándar de intensidad relativa (p. ej. materiales de referencia SRM para
   corrección de respuesta espectral) si vas a comparar intensidades entre equipos.
3. **Biblioteca propia**: igual que en FTIR, la identificación es por correlación contra espectros de
   material verificado por método ortogonal, con umbral definido **antes** de medir (ver `92`).
4. **Confirmación ortogonal** de cualquier hallazgo que dispare una decisión cara.

## Ejemplo aplicado (ILUSTRATIVO)

Control de entrada de solventes en una planta de extracción de cannabis.

```
Envase rotulado : "Etanol absoluto, grado alimenticio, 190 proof"
Raman de mano, a traves del vidrio ambar, 785 nm, 3 s
Bandas halladas : 883 cm-1 (C-C-O), 1053, 1096, 2880-2975 (C-H)
Correlacion vs biblioteca "etanol"        : 0,982   -> ACEPTA
Correlacion vs biblioteca "isopropanol"   : 0,61
Tiempo total    : 45 s por tambor, 8 tambores
```

Sin Raman, la alternativa era enviar una alícuota a GC y esperar 5 días, o creerle al proveedor. El mismo
equipo, aplicado a un extracto de reishi, devolvió una línea base fluorescente sin bandas: ahí Raman no
sirve y la identidad hay que resolverla por FTIR, HPLC o ITS. (Cifras ilustrativas.)

## Nota sobre SERS y los "detectores de pesticidas" portátiles

A agosto de 2026 circulan equipos portátiles que prometen medir pesticidas en cannabis o en alimentos por
SERS. La química es real y la sensibilidad puede llegar a niveles bajos, pero la **reproducibilidad** entre
sustratos SERS y entre matrices sigue siendo el problema abierto. Ningún regulador serio acepta SERS como
método de cumplimiento para residuos de plaguicidas: eso se resuelve por LC-MS/MS y GC-MS/MS
(ver `102-pesticidas-multiresiduo.md`). Úsalo, si acaso, como tamiz interno; nunca como resultado que
pongas en un COA.

## Errores comunes

- **Comprar un Raman portátil creyendo que reemplaza el laboratorio.** Reemplaza una parte del control de
  identidad, nada más.
- **Insistir con Raman en extractos oscuros** y culpar al equipo. El problema es la fluorescencia de la
  matriz: cambia de técnica.
- **Subir la potencia del láser** para "ver mejor" y quemar la muestra; el espectro que sale ya no es de lo
  que querías medir.
- **Usar la biblioteca de fábrica** en matrices naturales; esas bibliotecas son de sustancias puras.
- **Reportar un resultado SERS de trazas como si fuera cuantitativo.**
- **No registrar láser, potencia, tiempo de integración y número de acumulaciones.** Sin eso el espectro no
  es reproducible y el dato no es auditable.

## Conexión con otros módulos

→ `92-ftir-y-nir.md` — la técnica complementaria; juntas dan identidad robusta.
→ `105-quimiometria-pca-y-modelos.md` — sin modelo validado no hay cuantificación por Raman.
→ `102-pesticidas-multiresiduo.md` — cómo se miden de verdad los residuos.
→ `163-envase-primario-y-compatibilidad.md` — identificación de materiales de empaque.
→ `87-solventes-residuales.md` — el control que sí es de cumplimiento para solventes.