# 228 — Cordicepina y adenosina: el análisis del marcador de Cordyceps

La cordicepina es de los pocos marcadores del mundo de los hongos que es una molécula pequeña, bien
definida, con patrón comercial disponible y método sencillo. Eso la vuelve la mejor herramienta que tienes
para auditar un cordyceps: si el proveedor no te la puede medir, es porque no la tiene. Este módulo te da el
método completo, qué exigir en el informe y cómo no confundirla con la adenosina, que es su parecida barata.

Términos: **cordicepina (cordycepin)** = 3'-desoxiadenosina; nucleósido de adenina al que le falta el
hidroxilo en el carbono 3' de la ribosa. **adenosina (adenosine)** = adenina + ribosa completa; presente en
casi todo tejido biológico. **nucleósido (nucleoside)** = base nitrogenada + azúcar, sin fosfato.
**LOQ (limit of quantitation)** = concentración mínima que se puede cuantificar con exactitud aceptable.

## Las dos moléculas, lado a lado

| | Cordicepina | Adenosina |
|---|---|---|
| Nombre químico | 3'-desoxiadenosina | Adenosina |
| Fórmula | C₁₀H₁₃N₅O₃ | C₁₀H₁₃N₅O₄ |
| Masa monoisotópica aprox. | 251,1 | 267,1 |
| Diferencia estructural | Le falta un oxígeno (el OH en 3') | Ribosa completa |
| Especificidad como marcador | Alta: característica de *C. militaris* | Baja: está en cualquier material biológico |
| Absorbancia UV | Máximo cerca de 260 nm | Máximo cerca de 260 nm |

Los 16 Da de diferencia se ven bien en masas, pero **en UV se ven casi idénticas**: mismo cromóforo de
adenina, mismo máximo. Por eso la separación cromatográfica tiene que estar bien resuelta, y por eso un
"pico a 260 nm" no es prueba de cordicepina si no coincide con el patrón y, mejor aún, se confirma por masas.

## El método, paso a paso

```
1. MUESTRA
   Moler fino y homogeneo. Pesar del orden de 0,5-1 g (ajustar segun matriz).

2. EXTRACCION
   Metanol acuoso (p. ej. 50-70 %) o agua, con ultrasonido 20-30 min,
   o reflujo. Los nucleosidos son polares: el agua/metanol acuoso funciona.
   Centrifugar, aforar, filtrar por 0,22 um.

3. CROMATOGRAFIA (HPLC-UV)
   Columna:   C18, 4,6 x 250 mm, 5 um (o UHPLC sub-2 um)
   Fase movil: A = agua o buffer fosfato/formiato pH ~3-4
               B = metanol o acetonitrilo (los nucleosidos eluyen temprano)
   Elucion:   isocratica baja en organico, o gradiente suave
   Deteccion: UV 260 nm
   Patrones:  cordicepina y adenosina certificados, curva de 5-6 niveles

4. CONFIRMACION (recomendada)
   LC-MS/MS en modo positivo, transiciones MRM caracteristicas de cada
   nucleosido. Elimina la duda de coelucion. Ver 83.

5. HUMEDAD EN PARALELO
   Karl Fischer o perdida por secado, para reportar en base seca. Ver 98 y 07.
```

## Qué debe traer el informe

| Renglón | Unidad |
|---|---|
| Cordicepina | `mg/g base seca` (o `% p/p base seca`) |
| Adenosina | `mg/g base seca` |
| Método y detección (HPLC-UV 260 nm / LC-MS/MS) | texto |
| Patrones usados y su certificado | texto |
| LOD y LOQ del método | `mg/g` |
| Recuperación (spike) | `%` |
| Humedad y base | `% p/p` |
| Lote, fechas, laboratorio, acreditación | texto |

Sin LOQ no puedes interpretar un "no detectado" (ver `73`). En productos de fermentación con cordicepina
baja, la diferencia entre "no hay" y "está por debajo de un LOQ alto" es exactamente la diferencia entre un
producto y una demanda.

## Cifras de literatura (y cómo NO usarlas)

- *C. militaris* contiene mucho más cordicepina que *O. sinensis* silvestre; distribuidores citan un estudio
  de 2008 en *Journal of Agricultural and Food Chemistry* con una relación de hasta 90 veces (fuente
  secundaria; verifica el original antes de citarlo en un documento técnico).
- En cultivo optimizado, se ha reportado **136 mg/g** de cordicepina en micelio y 148,39 mg/mL en caldo al
  día 20 mediante cuantificación por MALDI-MS (PMC8424359). **Ese valor es de investigación de proceso**, no
  una expectativa comercial. Usarlo como referencia de compra te llevaría a rechazar todo el mercado.
- Para producto terminado no existe un rango de consenso publicado. Tu especificación se construye con tus
  lotes y un rango (ver `282`).

## Ejemplo aplicado — de mg/g a la etiqueta

**(ILUSTRATIVO)** Extracto con cordicepina 2,8 mg/g base seca; cápsula con 400 mg de extracto; porción de
2 cápsulas.

```
por capsula: 400 mg x (2,8 mg/g / 1000 mg/g) = 1,12 mg de cordicepina
por porcion: 1,12 x 2 = 2,24 mg de cordicepina/dia
```

Se declara así: "cordicepina 2,24 mg por porción (HPLC-UV 260 nm, base seca, lote XXXX)". Haz la cuenta en
código (`lab-tools/unidades.py` o `Matematicas_lushows`), nunca de memoria.

## Qué se puede y qué no se puede afirmar

- Se puede declarar la cantidad medida, con método, unidad y base. Eso es un claim de composición y es
  legítimo si está respaldado.
- Se puede decir que la cordicepina es el nucleósido característico de *Cordyceps militaris* y que se usa
  como marcador de identidad y calidad. Eso es química, no salud.
- **No se puede** atribuirle efectos terapéuticos. La cordicepina tiene una literatura amplia `[in vitro]` y
  `[animal]` sobre distintos mecanismos, y eso **no** autoriza ninguna afirmación sobre enfermedades en
  personas (ver `268`, `276`).
- No traslades dosis de estudios con cordicepina aislada a un extracto donde va en miligramos por porción.

## Errores comunes

- Integrar un pico a 260 nm y llamarlo cordicepina sin patrón. Puede ser adenosina u otro nucleósido.
- Reportar en base húmeda o sin decir la base.
- Aceptar "0,3 % cordycepin" sin LOQ ni cromatograma.
- Analizar la materia prima y declarar el número en el producto terminado, ya diluido con excipientes.
- Confundir manitol ("ácido cordicepínico") con cordicepina en la ficha del proveedor (ver `227`).
- Usar una columna y fase móvil de otro método (por ejemplo de cannabinoides) sin verificar que separa
  nucleósidos: eluyen muy temprano y pueden salir en el frente de solvente.

## Conexión con otros módulos

→ `227-cordyceps-quimica.md` — el contexto de la especie y sus tres materiales.
→ `237-nucleosidos-y-nucleotidos-fungicos.md` — la familia completa y otros marcadores.
→ `79-hplc-y-uhplc.md` · `80-deteccion-uv-dad-y-pureza-de-pico.md` · `83-lc-ms-ms-y-mrm.md` — las técnicas.
→ `73-lod-loq-y-rango-lineal.md` — por qué "no detectado" no significa "no hay".
→ `70-patrones-de-referencia-y-trazabilidad.md` — sin patrón no hay cuantificación.