# 61 — Estabilidad química: luz, calor, oxígeno y humedad (qué se come tus activos)

Tu producto sale del laboratorio con 28 % de β-glucano o con 850 mg de CBD por frasco, y dieciocho meses
después, en la estantería de una tienda de Barranquilla a 32 °C, ya no es el mismo producto. Este módulo es
el mapa de los cuatro enemigos —luz, calor, oxígeno y humedad— más dos cómplices (pH y metales traza), qué
le hace cada uno a cada familia de moléculas, y qué envase lo detiene. El error caro que evita: poner
"vencimiento: 24 meses" en la etiqueta porque suena bien, sin un solo dato que lo sostenga, y que un
control de la autoridad o un cliente con un COA de contramuestra te lo desarme.

Términos: **degradación (degradation)** = pérdida química del activo. **Estrés/forced degradation (forced
degradation study)** = someter la muestra a condiciones extremas a propósito para saber por dónde se rompe.
**Producto de degradación (degradant)** = lo que queda cuando el activo se rompe; a veces es el marcador que
delata mal almacenamiento. **Actividad de agua (water activity, a_w)** = agua disponible para reaccionar, de
0 a 1; no es lo mismo que % de humedad (`35`). **Espacio de cabeza (headspace)** = aire dentro del envase.

## Los seis estresores, en orden de daño real

| Estresor | Mecanismo | Familia más vulnerable | Contramedida |
|---|---|---|---|
| **Oxígeno** | Autooxidación por radicales; se acelera con metales traza | Lípidos, terpenos, cannabinoides, polifenoles | Purga con N₂, envase de baja permeabilidad, absorbedor de O₂, antioxidante |
| **Luz (UV y visible)** | Fotólisis y fotooxidación; la UV-B rompe enlaces directo | Cannabinoides, vitamina D₂, quinonas, pigmentos, psilocina | Vidrio ámbar, envase opaco, estuche |
| **Calor** | Acelera **toda** reacción (Arrhenius); además descarboxila | Formas ácidas (THCA/CBDA), psilocibina, terpenos | Cadena de temperatura, no dejar el contenedor al sol en puerto |
| **Humedad / a_w** | Hidroliza enlaces y habilita crecimiento microbiano | Glucanos en medio ácido, ésteres, polvo higroscópico | Desecante, sellado, control de a_w < 0,6 |
| **pH** | Catálisis ácida o básica de hidrólisis | Glicósidos, ésteres, fosfatos | Buffer en líquidos (`23`) |
| **Metales traza (Fe, Cu)** | Catalizan Fenton y oxidación | Todo lo oxidable | Quelante (ácido cítrico, EDTA donde esté permitido) |

Regla de campo: **el calor no crea rutas nuevas, las acelera.** Si algo se oxida, calentarlo lo oxida más
rápido. Por eso el estudio acelerado funciona (`165`) — y por eso deja de funcionar cuando el calor cambia
el mecanismo (fusión, cambio de forma cristalina, descarboxilación).

## Tabla por familia — quién muere de qué

| Familia | Enemigo #1 | Qué se forma | Señal en el análisis | Envase que lo evita |
|---|---|---|---|---|
| **Cannabinoides neutros (Δ9-THC)** | Oxígeno + luz | **CBN** (cannabinol) por oxidación; también degradación a otros productos | Sube CBN, baja THC: la relación CBN/THC es el reloj del lote (`204`, `177`) | Vidrio ámbar, lleno completo, N₂, frío |
| **Cannabinoides ácidos (THCA, CBDA)** | Calor + tiempo | Descarboxilación a THC/CBD (`174`) | Baja THCA, sube THC sin cambiar THC total | Frío; no es "daño" si lo controlas, es proceso |
| **Terpenos** | Volatilidad + oxígeno | Pérdida por evaporación; óxidos (p. ej. óxidos de cariofileno) | Cae el total y cambia el perfil relativo (`199`) | Envase hermético, sin headspace, frío |
| **Psilocibina** | Calor, oxígeno, pH; luz en la psilocina | Desfosforilación a **psilocina**, y oxidación de psilocina a productos azules/quinoides | Baja psilocibina, sube psilocina y luego cae todo; oscurecimiento visible (`255`) | Frío, oscuridad, seco, sin O₂ |
| **Triterpenos (ácidos ganodéricos)** | Oxígeno y pH extremo; relativamente robustos al calor seco | Oxidación lenta; isomerización | Cambia el patrón de picos, no solo el total (`224`) | Seco, oscuro, temperatura ambiente controlada |
| **β-glucanos** | Humedad + ácido (hidrólisis); calor húmedo prolongado | Fragmentación: baja el peso molecular (Mw) sin bajar tanto el % | El % por K-YBGL puede no moverse mientras el Mw cae (`52`) | Seco, a_w baja; el ensayo no ve el daño estructural |
| **Ergotioneína** | Es antioxidante: se sacrifica | Se oxida ella para proteger lo demás | Baja con el tiempo en matriz oxidante (`235`) | Seco, sin O₂ |
| **Vitamina D₂ (ergocalciferol)** | **Luz** | Fotoisómeros (taquisterol, lumisterol) | Cae el ensayo y aparecen isómeros (`236`) | Opaco, obligatorio |
| **Polifenoles / pigmentos** | Oxígeno + pH alcalino + metales | Quinonas, polímeros pardos | Oscurecimiento, cae el ensayo (`56`, `51`) | Ámbar, quelante, pH controlado |
| **Aceites y ácidos grasos** | Oxígeno | Peróxidos → aldehídos (rancidez) | Índice de peróxidos y de anisidina (`53`) | N₂, tocoferoles, frío |

Observación crítica sobre β-glucanos: **el método más usado no ve la degradación más importante.** El
K-YBGL cuenta glucosa liberada, así que un glucano fragmentado sigue contando. Si tu producto depende del
tamaño del polímero, el estudio de estabilidad necesita SEC-MALS además del % (`52`, `219`).

## La cuenta que hay que saber hacer

La mayoría de degradaciones en producto seco se ajustan razonablemente a **orden 1**:

```
C(t) = C0 · e^(−k·t)            t½ = ln(2)/k            k = A · e^(−Ea/RT)   (Arrhenius)

Ejemplo (ILUSTRATIVO): un aceite con CBD pierde 5,0 % del activo en 6 meses a 25 °C.
  k = −ln(0,950)/6 meses = 0,00854 mes⁻¹
  Tiempo hasta el 90,0 % del declarado:  t = −ln(0,900)/0,00854 = 12,3 meses
Lectura: con ese k, una vida útil de 24 meses NO se sostiene contra un criterio de 90–110 % del declarado.
```

Estos números se ejecutan en código, nunca de cabeza: `lab-tools/vida_util_arrhenius.py` o
`Matematicas_lushows`. Y el criterio de aceptación (¿90 %? ¿95 %? ¿del declarado o del inicial?) se define
**antes** del estudio, no después de ver el resultado (`164`).

## El envase es la mitad de la formulación

| Necesidad | Solución de envase | Cuidado |
|---|---|---|
| Bloquear luz UV-Vis | Vidrio ámbar tipo III, PET ámbar, HDPE blanco opaco, estuche de cartón | El ámbar filtra, no bloquea del todo; el opaco sí |
| Bloquear oxígeno | Vidrio o **blíster alu-alu**; purga con N₂; absorbedor de O₂ | El HDPE y el PET dejan pasar oxígeno; el frasco medio vacío es headspace |
| Bloquear humedad | Blíster alu-alu, HDPE grueso con sello de inducción, desecante de sílica | El desecante se satura; los frascos abiertos a diario pierden la protección |
| Evitar migración | Compatibilidad envase-contenido: aceites y terpenos atacan plásticos blandos | Ensayo de compatibilidad y de extraíbles/lixiviables (`163`) |
| Dosis unitaria | Blíster o sobre monodosis | Sube costo; protege al máximo el activo frágil |

Para un producto con activo frágil (psilocibina en un contexto de investigación, vitamina D₂, aceite con
terpenos), **el envase decide la vida útil más que la formulación**. Para un polvo de β-glucano estable, el
envase es principalmente barrera de humedad.

## Cómo se comprueba

1. **Degradación forzada** primero (`164`): calor seco, calor húmedo, ácido, base, oxidante (H₂O₂), luz
   ICH Q1B. Sirve para dos cosas: encontrar los degradantes y **demostrar que tu método analítico los separa**
   del activo (especificidad, `75`). Un método que no separa el degradante te reporta "todo bien" mientras
   el producto se cae.
2. **Estudio real y acelerado** (ICH Q1A): largo plazo en la condición de la zona climática —Colombia es
   **zona IVb, 30 °C / 75 % HR**, no 25/60— y acelerado 40 °C / 75 % HR por 6 meses (`164`, `165`).
3. **En el envase final**, no en un frasco de laboratorio. El estudio en otro envase no vale.
4. **Mínimo tres lotes** para declarar vida útil.
5. **Balance de masa**: lo que baja del activo debería aparecer como degradante. Si no aparece, o el método
   no lo ve o la muestra se perdió por otro lado (`06`).

## Ejemplo aplicado — dos frascos del mismo lote

Aceite de espectro amplio, 30 mL, declarado 1.000 mg de CBD **(ILUSTRATIVO)**, mismo lote, mismo día:

```
Frasco A: vidrio ámbar, tapa con sello, guardado a 20–25 °C, en su estuche
Frasco B: vidrio transparente, medio consumido (headspace grande), sobre la mesa junto a la ventana

A los 6 meses (HPLC-DAD, mismo método, misma curva):
  A: CBD 968 mg/frasco (96,8 % del declarado)   ·  color sin cambio
  B: CBD 861 mg/frasco (86,1 % del declarado)   ·  color más oscuro, olor cambiado
Diferencia atribuible: luz + oxígeno del headspace. Misma fórmula, distinto destino.
```

Decisión de negocio: la instrucción de conservación en la etiqueta ("consérvese en su estuche, bien cerrado,
lejos de la luz solar y del calor") no es texto de relleno, es parte de la especificación. Y si el producto
se vende para consumo en 30 días, hay que estudiar la **estabilidad en uso (in-use stability)**, con el
frasco abierto y cerrado a diario, no solo el frasco sellado.

## Errores comunes

- Declarar vida útil sin estudio, copiada del competidor. Es un dato inventado en un documento oficial (`03`).
- Hacer el estudio a 25 °C / 60 % HR cuando el mercado es Colombia. La condición correcta es 30 °C / 75 % HR.
- Estudiar en un envase distinto al que se vende. No transfiere.
- Medir solo el activo y no buscar degradantes. El balance de masa es lo que da credibilidad.
- Frascos grandes que se consumen lento: el headspace crece con cada uso y el activo se oxida al final del
  frasco, justo cuando el cliente evalúa si repite.
- Suponer que "en polvo no pasa nada". El polvo higroscópico chupa agua, la a_w sube y arranca la hidrólisis.
- Creer que un % de β-glucano estable significa estructura intacta. El método no distingue tamaño (`219`).
- Guardar la contramuestra (retention sample) en peores condiciones que el producto. Entonces no sirve de
  contraprueba (`168`).

## Conexión con otros módulos

→ `164-estabilidad-ich-q1-y-vida-util.md` — el diseño formal del estudio y los criterios de aceptación.
→ `165-estudios-acelerados-y-arrhenius.md` — cómo se extrapola y cuándo la extrapolación es inválida.
→ `163-envase-primario-y-compatibilidad.md` — el módulo dueño del envase, barreras y lixiviables.
→ `204-estabilidad-y-degradacion-del-thc.md` — el caso cannabis, con CBN como reloj.
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — el caso psilocibio, en detalle.
→ `47-oxidacion-y-degradacion-de-productos-naturales.md` — los mecanismos químicos de fondo.
→ `35-actividad-de-agua-y-humedad.md` y `98-karl-fischer-y-humedad.md` — medir el agua bien.
→ `240-secado-y-perdida-de-activos.md` — dónde empieza la pérdida: antes de envasar.
