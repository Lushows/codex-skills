# 424 — El efecto que tapa un problema

`423` trata el efecto que no hace nada. Éste trata el contrario y es más caro: el efecto que **sí** hace
algo —se mide, se ve, cuesta CPU— pero lo que hace es ocultar un defecto en vez de arreglarlo.

Es la clase de decisión que parece buena en la sesión de montaje y mala seis meses después, cuando el
material vuelve a aparecer y la tapa hay que volver a poner. El diagnóstico es siempre el mismo: **el
efecto está compensando aguas abajo un problema que tiene solución aguas arriba.**

---

## 1. El catálogo, con su medida

| Se pone… | Para tapar… | La medida que lo delata | La solución real |
|---|---|---|---|
| `gblur` de fondo | fondo feo o desordenado | peso codificado cae >50% | reencuadre (`102`) o rodaje (`174`) |
| `unsharp` fuerte | plano desenfocado | `unsharp` sube el peso +76% y no recupera detalle | descartar la toma (`336`) |
| grano grueso | banding / bloques de compresión | YDIF sube y el banding sigue en el histograma | fuente mejor o `gradfun` |
| viñeta pesada | esquinas quemadas o sucias | caída borde→centro >30% (`444`) | corregir la luz, recortar |
| saturación alta | material apagado o mal balanceado | `SATAVG` sube y `HUEAVG` no se mueve | balance de blancos (`61`) |
| `eq=brightness` global | plano subexpuesto | `YMIN` sube con `YAVG`: negros lavados | recuperar de la fuente, o descartar |
| desenfoque de movimiento | corte que no funciona | `YDIF` tapado en 3 fotogramas | cambiar el punto de corte (`324`) |
| `hqdn3d` fuerte | ruido de ISO alto | SSIM 0,985 y la piel plastificada | regrabar; o asumir el ruido (`440`) |
| transición vistosa | dos planos que no casan | — | emparejar color (`62`) o cortar antes |

La columna que importa es la tercera. Casi todos estos efectos **se delatan por un número que no
cuadra con su hipótesis**.

---

## 2. El test de los tres negros

La forma más rápida de saber si un efecto está tapando algo: **quítalo y mira el material desnudo, a
tamaño completo, en un fotograma congelado.**

```bash
# El fotograma crudo, sin nada de la cadena
ffmpeg -hide_banner -y -ss 14.2 -i fuente.mp4 -frames:v 1 crudo.png
# El mismo, con la cadena completa
ffmpeg -hide_banner -y -ss 14.2 -i fuente.mp4 -vf "$CADENA" -frames:v 1 acabado.png
# Los dos, lado a lado, al 100%
ffmpeg -hide_banner -y -i crudo.png -i acabado.png -filter_complex hstack comparar.png
```

Tres preguntas sobre `crudo.png`:

1. **¿El problema existe sin el efecto?** Si no lo ves en el crudo, el efecto no está tapando nada:
   está haciendo su trabajo.
2. **¿El efecto lo resuelve o lo esconde?** Un fondo desenfocado no está ordenado: está borroso. Un
   plano con `unsharp` no tiene más detalle: tiene más contraste en los bordes que ya había.
3. **¿Existe la versión sin el problema?** Otra toma, otro encuadre, otro plano de cobertura. Si existe,
   el efecto es un parche caro.

---

## 3. El que más engaña: `unsharp` sobre un plano desenfocado

Merece su sección porque es el más frecuente y el peor entendido. `unsharp` **no añade detalle**:
aumenta el contraste local alrededor de los bordes que ya existían. Sobre un plano enfocado da
sensación de nitidez; sobre uno desenfocado da halos.

Medido hoy sobre el clip de 4 s a 1080p:

| | `utime` | coste propio | PSNR | SSIM | MB |
|---|---|---|---|---|---|
| nada | 2,86 | — | — | — | 1,17 |
| `unsharp=5:5:0.2:5:5:0.0` | 7,19 | +4,33 | 47,95 | 0,9975 | 1,34 (+15%) |
| `unsharp=5:5:0.8:5:5:0.0` | 7,45 | **+4,59** | 37,22 | 0,9740 | **2,06 (+76%)** |

El +76% de peso es la prueba material de lo que hace: **está creando información nueva**. Si el plano
estaba desenfocado, esa información no es detalle recuperado, son halos —y el codificador los paga como
si fueran detalle. Pagas el filtro más caro de la tabla, pagas un 76% de bitrate, y lo que entregas es
un plano desenfocado con bordes duros.

**Cómo se decide:** saca el fotograma al 200% en la zona de un borde de alto contraste. Si aparece una
línea clara pegada a una oscura que en el crudo no estaba, eso es un halo, y el resto de tu audiencia
también lo va a ver en cuanto el video se comprima. La dosis que se sostiene en material real está
entre 0,2 y 0,5; 0,8 es ya el territorio de la tapa.

---

## 4. El caso legítimo: cuando tapar es la decisión correcta

No todo parche es un error. Hay tres situaciones donde tapar es profesional:

**a) No existe la versión sin el problema.** Material de archivo, una toma irrepetible, una grabación de
un evento que ya pasó. Aquí el parche no compite con nada mejor. El canal documental trabaja
íntegramente sobre recortes de archivo del siglo pasado: el grano y la viñeta no tapan un defecto, son
la única manera de que ocho fuentes distintas convivan (`427`).

**b) El coste de arreglarlo excede el valor de la pieza.** Un reel de $10.000 de presupuesto con un
plano ligeramente subexpuesto no justifica volver a rodar.

**c) El defecto es parte del carácter.** Un VHS que se ve a VHS. Aquí no hay problema que tapar: hay una
decisión de estilo, y esa decisión es de `directorcreativo_lushows`, no de este bloque.

**La diferencia operativa entre un parche legítimo y uno vergonzante es que el legítimo está escrito.**
En la ficha del efecto (`421`) hay una línea que dice *«tapa el banding del archivo del 78; no hay
fuente mejor»*. Eso convierte el parche en una decisión documentada que se puede revisar cuando aparezca
una fuente mejor.

---

## 5. El efecto que tapa un problema de montaje

La variante que no es de imagen y que casi nadie reconoce: **la transición vistosa que existe porque los
dos planos no casan.** Un `xfade=zoomin` en un punto donde un corte duro chirría no arregla el corte;
anuncia que había uno.

El test es de `50`, y es brutal: **quita la transición y pon corte duro.** Si el corte funciona, la
transición sobraba. Si no funciona, el problema no es la transición: es el punto de corte, o la elección
de planos, o la continuidad (`338`). Cambiar el punto de corte cuesta treinta segundos; la transición
costaba render y presupuesto de atención, y no resolvía nada.

Lo mismo con el desenfoque de movimiento sobre un corte: tapa 3 fotogramas y deja el problema intacto
los otros ciento sesenta.

---

## 6. El coste oculto de una tapa

Una tapa no se paga una vez:

- **Se paga en cada entrega.** El material no mejora: cada vez que ese plano vuelva a usarse, la tapa
  hay que volver a ponerla.
- **Se paga en bitrate justo donde no hay.** `unsharp` sube el peso un 76% y `noise` un 73%. Si la
  entrega va a una red que recomprime, ese bitrate extra sale del presupuesto de todo lo demás: la tapa
  degrada el resto de la pieza (`428`).
- **Se paga en la siguiente pieza.** El plano malo sigue en el banco. Sin una nota que diga por qué se
  tapó, el siguiente editor lo vuelve a elegir.
- **Se paga en el rodaje que no cambia.** Si el editor tapa la subexposición en vez de informarla, en el
  próximo rodaje vuelve a venir subexpuesto. Ver `170` y `388`.

---

## 7. El protocolo de tres pasos

```
1. AISLA        quita el efecto, saca el fotograma crudo, miralo al 100%
2. CLASIFICA    ¿el problema existe en el crudo?
                  no  -> el efecto no tapa nada. Sigue.
                  si  -> ¿existe una version sin el problema?
                           si -> usala. El efecto sobra.
                           no -> es un parche legitimo. Ve al paso 3.
3. DOCUMENTA    en la ficha del efecto: que tapa, por que no hay alternativa,
                y que haria falta para no necesitarlo. Con fecha.
```

El paso 3 es el que convierte una chapuza en una decisión. Y el «qué haría falta» es lo que acaba en el
briefing del próximo rodaje.

---

## Errores frecuentes

- **Subir `unsharp` para arreglar un plano desenfocado.** No añade detalle: añade halos y +76% de peso.
- **Desenfocar un fondo desordenado.** Un fondo borroso sigue siendo un fondo malo, y ahora además es
  obviamente posterior.
- **Meter grano para tapar banding.** El banding sigue ahí debajo; para eso está `gradfun`.
- **Subir brillo global para levantar un subexpuesto.** Sube `YMIN` con `YAVG`: los negros se lavan y la
  imagen se ve sucia, no expuesta.
- **Poner una transición donde el corte no funciona.** Prueba el corte duro primero.
- **Denoise fuerte sobre piel.** La piel plastificada se nota mucho más que el ruido que tapaba (`67`).
- **Tapar y no informar.** El rodaje siguiente repite el error.
- **No dejar por escrito qué tapa cada parche.** En tres meses nadie sabe si se puede quitar.
- **Confundir estilo con tapa.** El grano del canal documental no tapa: es la gramática. Escríbelo para
  que se distinga.
- **Decidir sobre el fotograma ya procesado.** El diagnóstico se hace sobre el crudo.

---

## Checklist

- [ ] Saqué el fotograma crudo, sin cadena, y lo miré al 100%.
- [ ] Sé si el problema existe en el crudo o lo estaba inventando el efecto.
- [ ] Comprobé si existe otra toma, otro encuadre u otra fuente sin el problema.
- [ ] Si el efecto es un parche, está escrito en la ficha con su motivo y su fecha.
- [ ] La ficha dice qué haría falta para no necesitarlo.
- [ ] Si hay `unsharp`, la dosis está por debajo de 0,5 y comprobé los bordes al 200%.
- [ ] Si hay una transición vistosa, probé antes el corte duro.
- [ ] El coste en bitrate del parche cabe en el presupuesto de la entrega (`428`).
- [ ] Lo que aprendí del material defectuoso está en el briefing del próximo rodaje (`170`).

---

## Relacionado

- `423` — el efecto que directamente no hace nada
- `421` — la ficha del efecto, donde se documenta un parche
- `422` — lo que cuesta en CPU y en atención
- `428` — por qué el bitrate que se lleva una tapa sale del resto de la pieza
- `429` — cuándo se retira
- `50` — cuándo usar transición: la prueba del corte duro
- `61`, `62`, `67` — corrección, emparejado y piel
- `336` — descartar sin culpa
- `170`, `388` — devolver el problema al rodaje, e informar una pisada
- `directorcreativo_lushows` — si el «defecto» es en realidad el estilo, la decisión es de esa skill
