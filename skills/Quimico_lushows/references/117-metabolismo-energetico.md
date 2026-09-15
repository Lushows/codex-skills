# 117 — Metabolismo energético (por qué "da energía" casi nunca significa lo que el cliente cree)

"Da energía" es probablemente el claim más vendido y peor sustentado del mercado de suplementos. Este módulo
te explica de dónde sale la energía de verdad —ATP, glucólisis, Krebs, cadena respiratoria— para que puedas
distinguir tres cosas que el marketing mezcla a propósito: aportar calorías, aportar un cofactor que falta,
y producir una sensación de alerta por estimulación del sistema nervioso. Solo la primera es energía en
sentido físico. El error caro: prometer "energía" con un ingrediente que no aporta calorías ni corrige una
deficiencia y terminar con una etiqueta insostenible.

Términos: **ATP (adenosine triphosphate)** = la moneda energética de la célula; se gasta y se regenera
constantemente. **Glucólisis (glycolysis)** = ruptura de glucosa a piruvato en el citosol, sin oxígeno.
**Ciclo de Krebs (TCA cycle / citric acid cycle)** = ruta mitocondrial que oxida acetil-CoA y produce NADH
y FADH2. **Fosforilación oxidativa (oxidative phosphorylation)** = la cadena respiratoria mitocondrial que
convierte ese NADH en ATP usando oxígeno. **Cofactor (cofactor)** = molécula no proteica que una enzima
necesita para funcionar (NAD+, FAD, CoA, Mg2+).

## El mapa en cuatro pasos

```
Glucosa (C6H12O6)
   │  glucólisis (citosol, anaerobia)
   ▼  balance neto: 2 ATP + 2 NADH + 2 piruvato
Piruvato
   │  piruvato deshidrogenasa (matriz mitocondrial) — requiere tiamina (B1), lipoato, CoA (B5), FAD (B2), NAD (B3)
   ▼
Acetil-CoA
   │  ciclo de Krebs → 3 NADH + 1 FADH2 + 1 GTP por vuelta
   ▼
NADH / FADH2
   │  cadena respiratoria (complejos I–IV) + ATP sintasa, consume O2
   ▼
ATP  (rendimiento total aproximado por glucosa: ~30–32 ATP, valor de literatura, no una constante exacta)
```

Dato que cambia la conversación con un cliente: un adulto **recicla** del orden de su propio peso corporal
en ATP al día (reportado en la literatura fisiológica). El cuerpo no almacena ATP; lo regenera. Ningún
suplemento "aporta ATP" en cantidad relevante por vía oral: el ATP oral se hidroliza en el tracto digestivo.

## De dónde sale realmente la energía

| Fuente | Aporte energético | ¿Se puede llamar "energía"? |
|---|---|---|
| Carbohidratos | ~4 kcal/g | Sí, es energía física real |
| Proteínas | ~4 kcal/g | Sí, aunque su función principal no es esa |
| Grasas | ~9 kcal/g | Sí |
| Alcohol | ~7 kcal/g | Sí (y no es recomendable como fuente) |
| Vitaminas B como cofactor | 0 kcal/g | Solo si hay deficiencia real medida |
| Cafeína, teobromina | 0 kcal/g | No: es alerta por antagonismo de adenosina |
| Extractos de hongos | ~0 kcal a la dosis usada | No en sentido calórico |

Un extracto de cordyceps a 1 g/día aporta, como mucho, ~4 kcal. Eso es menos que una uva. Cualquier
sensación reportada no proviene de calorías.

## Los tres significados de "energía" (sepáralos siempre)

1. **Energía calórica** — aportas sustrato oxidable. Medible: kcal/porción, tabla nutricional.
2. **Corrección de una deficiencia** — si a alguien le falta B12, hierro o B1, corregirlo mejora la
   producción de ATP. Pero esto requiere **medir la deficiencia primero**, y hablar de la deficiencia como
   enfermedad ya entra en terreno regulado (ver `267`).
3. **Percepción de alerta / menor fatiga percibida** — es un desenlace subjetivo, se mide con escalas
   validadas y es enormemente sensible al placebo. Requiere ECA doble ciego para significar algo.

El marketing usa el sentido (3), muestra evidencia del sentido (2) y deja que el cliente entienda (1).
Ese salto es exactamente lo que un químico honesto no hace.

## Cordyceps y el mito del ATP

El caso emblemático en hongos: se afirma que *Cordyceps* "aumenta el ATP" porque contiene **cordicepina**
(3'-desoxiadenosina) y adenosina, moléculas parecidas al esqueleto del ATP. Parecerse estructuralmente al
ATP no es producir ATP. Lo que hay:

- Cordicepina modula rutas de señalización y es un análogo de nucleósido → `[in vitro]`.
- Estudios en roedores sobre resistencia al ejercicio → `[animal]`.
- Ensayos pequeños en humanos sobre VO2máx / tolerancia al ejercicio con resultados heterogéneos y muestras
  chicas → `[clínico fase 2]` de baja potencia estadística, no replicados de forma consistente.
- Un detalle analítico incómodo: buena parte de los productos comerciales son *Cordyceps militaris* o
  micelio, no *Ophiocordyceps sinensis*, y el contenido de cordicepina varía en órdenes de magnitud entre
  lotes (ver `227`, `228`).

Traducción: hay una hipótesis con respaldo preclínico y evidencia clínica débil. Eso se puede decir. "Te da
energía" no.

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Cuánta energía aporta el producto? | Bomba calorimétrica o cálculo por Atwater desde composición | kcal/100 g y kcal/porción |
| ¿Cuánto activo hay por porción? | HPLC-DAD o LC-MS/MS del marcador (p. ej. cordicepina, `228`) | mg/g y mg/porción |
| ¿Cambia el metabolismo energético in vitro? | Seahorse (OCR/ECAR) en cultivo celular | pmol O2/min |
| ¿Cambia el rendimiento físico? | ECA cruzado con VO2máx, tiempo hasta agotamiento | mL/kg/min, s |
| ¿Cambia la fatiga percibida? | Escalas validadas (p. ej. VAS de fatiga) en ECA doble ciego | puntos de escala |

## Ejemplo aplicado — BIO-SETA

Formulación **(ILUSTRATIVO)**: cápsula de 500 mg de extracto de *Cordyceps militaris*, COA que reporta
cordicepina 0,42 % p/p base seca por HPLC-DAD. Cálculo por porción de 2 cápsulas:

```
500 mg × 2 = 1.000 mg de extracto
1.000 mg × 0,0042 = 4,2 mg de cordicepina por porción diaria
```

(Verificar con `lab-tools/unidades.py`, no de cabeza.) Ahora la pregunta útil: ¿los estudios clínicos que
se citan usaron 4,2 mg de cordicepina o 3 g de biomasa entera? Casi siempre es lo segundo, y entonces la
formulación no reproduce la exposición del estudio. Ese es el hallazgo que salva un lanzamiento: el número
no cierra, y hay que subir dosis, cambiar materia prima o bajar el tono de la comunicación.

## Errores comunes

- Vender "energía" sin aportar calorías ni haber medido una deficiencia. Es la promesa más frágil que hay.
- Confundir parecido estructural con función: cordicepina no es ATP, ergotioneína no es glutatión.
- Citar un estudio hecho con biomasa entera para justificar un extracto concentrado con dosis distinta.
- Ignorar que el efecto percibido de "energía" es placebo-sensible y necesita doble ciego para significar.
- Sumar el aporte calórico como si fuera relevante: 1 g de extracto ≈ 4 kcal, no mueve la aguja.
- Cruzar la línea hacia fatiga crónica, anemia o tiroides. Eso es enfermedad y es claim prohibido (`268`).

## Conexión con otros módulos

→ `115-bioquimica-celular-esencial.md` — dónde ocurre cada paso.
→ `116-enzimas-y-cinetica-de-michaelis-menten.md` — cómo se mide una enzima de estas rutas.
→ `227-cordyceps-quimica.md` y `228-cordicepina-y-adenosina-analisis.md` — el caso concreto.
→ `133-estres-oxidativo-y-antioxidantes.md` — la mitocondria también es la fuente principal de ROS.
→ `57-vitaminas-y-cofactores.md` — los cofactores que estas rutas necesitan.