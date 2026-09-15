# 27 — Catálisis y enzimas (bajarle la barrera a la reacción, a propósito o sin querer)

Un catalizador acelera una reacción sin consumirse. Suena a laboratorio, pero en tu operación hay
catálisis en todas partes y casi siempre no invitada: el hierro del molino que dispara la oxidación de un
extracto, la arcilla del filtro que isomeriza Δ9-THC a Δ8, el ácido residual de una limpieza que hidroliza
un éster. Y hay catálisis que sí quieres pagar: enzimas que rompen la pared celular del hongo y suben el
rendimiento de β-glucano sin subir la temperatura. Saber cuál es cuál convierte "el lote salió raro" en
"el lote 07 pasó por el tanque nuevo y ese tanque suelta hierro".

Términos: **catalizador (catalyst)** = sustancia que baja la energía de activación (Ea) y no aparece en la
estequiometría neta. **catálisis homogénea (homogeneous catalysis)** = catalizador en la misma fase que
los reactivos (un ácido en solución). **heterogénea (heterogeneous)** = en fase distinta (una arcilla, un
metal sólido). **enzima (enzyme)** = catalizador proteico, muy selectivo, que trabaja en condiciones
suaves. **cofactor (cofactor)** = molécula o ion que la enzima necesita para funcionar. **inhibidor
(inhibitor)** = lo que frena a la enzima.

## Lo que un catalizador hace y lo que NO hace

```
SÍ hace:  baja Ea  →  sube k (Arrhenius)  →  la reacción llega antes al mismo destino
NO hace:  cambiar K, cambiar ΔG, ni volver espontáneo lo que no lo es (`21`, `25`)

Acelera por igual la reacción directa y la inversa. Si el equilibrio te da 70 %, con catalizador
te seguirá dando 70 % — solo que en 20 min en vez de 8 horas.
```

Esa asimetría es la trampa: un catalizador **también acelera la reacción que te destruye el producto**. Si
metes un ácido para acelerar una conversión y ese ácido isomeriza tu cannabinoide, ganaste tiempo y
perdiste el lote (`180`).

## Catálisis no invitada: la que te está costando plata ahora

| Catalizador accidental | De dónde sale | Qué acelera | Cómo se controla |
|---|---|---|---|
| Fe²⁺, Cu⁺ trazas | Molino, tanque, agua, materia prima | Autooxidación radicalaria (Fenton) | Acero 316 L, agua tipo II, quelante (citrato) (`24`, `106`) |
| Ácidos de Lewis (arcillas, tierras filtrantes) | Bentonita, tierra de diatomeas, sílice ácida | Isomerización Δ9 → Δ8-THC; deshidrataciones | Usar medios neutralizados; verificar por HPLC antes/después (`180`, `191`) |
| Ácido o base residual de limpieza | CIP mal enjuagado | Hidrólisis de ésteres, degradación de glicósidos | Verificar pH del último enjuague y registrarlo (`46`, `169`) |
| Luz UV + fotosensibilizadores | Vidrio transparente, riboflavina en la matriz | Fotodegradación de terpenos y fenoles | Ámbar, aluminio, opaco (`61`, `163`) |
| Enzimas propias del material (polifenol oxidasa) | El hongo o la planta fresca | Pardeamiento enzimático en cuanto se corta | Blanqueado térmico o secado rápido (`62`, `142`) |
| Superficies de níquel o cobre | Tuberías, válvulas, serpentines viejos | Oxidación y color | Cambio de material; ICP-MS al producto (`88`) |

## Catálisis que sí conviene comprar: enzimas en extracción

La pared celular del hongo es quitina + β-glucanos entrecruzados; la de la planta es celulosa + pectina +
lignina. Las enzimas rompen esa red a 45–55 °C, sin el costo energético ni la degradación que trae hervir
horas. Es el corazón de la **extracción asistida por enzimas** (`147`).

| Enzima | Sustrato que ataca | Condiciones típicas reportadas | Efecto buscado |
|---|---|---|---|
| Celulasa | Celulosa de la pared vegetal | pH 4,5–5,5 · 45–55 °C · 1–3 h | Libera activos atrapados en material vegetal |
| Quitinasa | Quitina de la pared fúngica | pH 5–6 · 40–50 °C | Libera β-glucano de la matriz fúngica |
| β-glucanasa | β-glucano | pH 4,5–6 · 40–55 °C | **Cuidado**: si te pasas, degradas el activo que vendes |
| Pectinasa | Pectina | pH 3,5–5 · 45–50 °C | Baja viscosidad, mejora filtración |
| Proteasa | Proteínas de la matriz | pH 6–8 · 45–60 °C | Libera complejos proteína-polisacárido |
| α-amilasa / amiloglucosidasa | Almidón (α-glucano) | pH 5–6,5 · 55–90 °C | Es exactamente el paso del método K-YBGL (`221`) |

Advertencia grande: la β-glucanasa y la amilasa hacen cosas opuestas para tu etiqueta. La amilasa **quita
el confusor** (almidón del grano) y por eso el método Megazyme la usa (`220`, `221`); la β-glucanasa
**destruye tu activo** si se deja actuar de más. Una extracción enzimática mal controlada baja el
β-glucano medible aunque el rendimiento de masa suba.

## Enzimas: las cuatro variables que las mandan

```
pH        →  cada enzima tiene su óptimo; fuera de ±1 unidad pierde gran parte de su actividad (`23`)
T         →  la actividad sube con T hasta que la proteína se desnaturaliza; hay un máximo agudo
Tiempo    →  la reacción sigue mientras la enzima esté activa: hay que INACTIVARLA a propósito
Dosis     →  se expresa en unidades de actividad (U) por gramo de sustrato, no en gramos de polvo
```

Inactivación: 85–95 °C por 5–10 min, o bajar el pH fuera del rango. Si no inactivas, la enzima sigue
trabajando en el tanque de espera y el lote que analizas no es el que envasas.

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Cuánta actividad tiene la enzima que compré? | Ensayo de actividad del proveedor, verificado con sustrato patrón | U/g o U/mL, a pH y T declarados |
| ¿La enzima mejoró mi rendimiento? | Extracción con y sin enzima, mismo lote, activo por método específico | mg/g biomasa b.s. (`221`, `79`) |
| ¿Se pasó y degradó mi activo? | β-glucano por K-YBGL y perfil de peso molecular por SEC | % p/p b.s.; distribución de PM (`219`) |
| ¿Quedó enzima activa en el producto? | Ensayo de actividad residual sobre el producto terminado | U/g; también proteína residual (alérgeno, `137`) |
| ¿Hay catálisis metálica no deseada? | ICP-MS de Fe, Cu, Ni, Mn en producto y en agua de proceso | mg/kg (ppm) (`88`, `106`) |
| ¿Se isomerizó el cannabinoide en el filtro? | HPLC con resolución Δ8/Δ9, antes y después del paso | % de área relativa (`180`, `198`) |

## Ejemplo aplicado — enzima en extracción de reishi: hasta dónde sí

Cuerpo fructífero molido a 0,5 mm, agua 1:20, pretratamiento enzimático a 50 °C y pH 5,0, luego decocción
a 95 °C por 60 min **(ILUSTRATIVO)**:

```
Tratamiento previo                 Extracto seco   β-glucano extraído   Recuperación
                                   (% p/p b.s.)    (mg/g biomasa b.s.)  (% del contenido)
Sin enzima                             18,4                148              55 %
Quitinasa 50 U/g, 60 min               22,1                196              73 %
Quitinasa 50 U/g, 180 min              23,8                201              75 %
Quitinasa + β-glucanasa 20 U/g, 60 min 27,6                 92              34 %

Contenido de β-glucano en la biomasa (K-YBGL): 268 mg/g b.s.
```

Lo que enseña: la quitinasa sube la recuperación de 55 % a 73 % con 60 min, y las 2 horas extra casi no
aportan (plateau, `21`). La combinación con β-glucanasa sube el **rendimiento de masa** a 27,6 % —el
número que un proveedor te mostraría orgulloso— mientras **destruye** el activo: 92 mg/g contra 196. Si tu
único control es el rendimiento gravimétrico, este proceso te parece el mejor de los cuatro. Ese es
exactamente el tipo de fraude involuntario que el método específico detecta y el genérico no (`222`).

## Errores comunes

- Comprar enzima por kilos en vez de por unidades de actividad. El polvo puede ser 90 % soporte inerte.
- No inactivar la enzima. El proceso sigue en el tanque y en el tambor.
- Evaluar una extracción enzimática solo por rendimiento de masa. Hay que medir el activo específico.
- Ignorar que la enzima es proteína: aporta alérgenos potenciales y debe declararse según el marco
  aplicable (`137`, `272`).
- Usar tierras filtrantes ácidas con cannabinoides y luego sorprenderse con el Δ8 en el COA (`180`).
- Culpar al "lote de materia prima" cuando el cambio real fue una válvula de cobre o un tanque nuevo.
- Creer que un catalizador cambia el equilibrio. No lo cambia; solo lo alcanza antes (`21`).

## Conexión con otros módulos

→ `26-cinetica-de-reaccion.md` — la Ea que el catalizador baja.
→ `116-enzimas-y-cinetica-de-michaelis-menten.md` — la cinética enzimática formal (Km, Vmax).
→ `147-ultrasonido-microondas-y-enzimas.md` — el proceso de planta con enzimas, paso a paso.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — enzimas usadas como herramienta analítica.
→ `24-oxido-reduccion.md` — catálisis metálica de la oxidación.
→ `180-delta8-delta10-e-isomerizacion.md` — catálisis ácida no deseada en cannabis.
→ `62-maillard-y-pardeamiento.md` — pardeamiento enzimático y no enzimático.
