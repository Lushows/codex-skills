# 222 — "Polisacáridos totales": por qué ese número no sirve

Si en la ficha técnica de un hongo ves "polysaccharides 30 %", lo primero que tienes que sentir es
desconfianza, no entusiasmo. Ese renglón es el más común del mercado y el menos informativo: mide
carbohidrato total, y el almidón del arroz es carbohidrato. Es el número favorito de quien vende micelio en
grano porque le permite dar una cifra alta y verdadera al mismo tiempo que engañosa. Este módulo cierra la
unidad `217`–`222`: aquí queda claro por qué el par β/α es la única lectura que decide.

Términos: **polisacáridos totales (total polysaccharides)** = todo polímero de azúcares, sin distinguir
tipo. **fenol-sulfúrico (phenol–sulfuric acid method)** = ensayo colorimétrico clásico de carbohidrato
total (Dubois et al., *Analytical Chemistry*, 1956). **precipitación etanólica (ethanol precipitation)** =
método gravimétrico donde se precipita "polisacárido" con alcohol y se pesa. **equivalentes de glucosa
(glucose equivalents)** = unidad en que suele expresarse el fenol-sulfúrico.

## Los tres métodos que se esconden detrás de la palabra

| Método | Qué mide de verdad | Qué cuenta como "polisacárido" |
|---|---|---|
| Fenol-sulfúrico (colorimétrico) | Azúcares totales tras hidrólisis | Almidón, β-glucano, manitol, azúcares libres, pectinas |
| Precipitación con etanol (gravimétrico) | Todo lo que precipite y pese | Almidón, glucano, proteína arrastrada, sales, maltodextrina |
| Antrona | Azúcares totales por color | Igual que fenol-sulfúrico |

Ninguno distingue α de β. Y el gravimétrico es peor todavía: pesa lo que precipite, incluyendo cosas que
ni siquiera son carbohidratos si el lavado fue pobre.

## El ejemplo que lo explica todo

**(ILUSTRATIVO)** Dos muestras, mismo "30 % de polisacáridos":

```
Muestra A — extracto de cuerpo fructifero
   polisacaridos (fenol-sulfurico)  30 %
   beta-glucano (K-YBGL, b.s.)      28 %
   alfa-glucano (K-YBGL, b.s.)       2 %
   -> el 30 % es casi todo activo fungico

Muestra B — micelio sobre arroz
   polisacaridos (fenol-sulfurico)  30 %
   beta-glucano (K-YBGL, b.s.)       4 %
   alfa-glucano (K-YBGL, b.s.)      26 %
   -> el 30 % es casi todo almidon de arroz
```

Las dos fichas dicen lo mismo. Los dos productos no tienen nada que ver. Y el precio del proveedor B suele
ser menos de la mitad, lo que hace que gane licitaciones por precio contra un producto real.

## Por qué el método sobrevive

- Es **barato y rápido**: un fenol-sulfúrico se corre en horas con un espectrofotómetro básico.
- Da **números altos**, que se ven bien en la ficha.
- Muchos compradores lo piden por costumbre, así que el proveedor lo entrega.
- En la farmacopea china y en trabajos académicos antiguos de *Ganoderma* se usó mucho, así que hay
  bibliografía que lo respalda como caracterización general —no como control de autenticidad.

Es decir: no es un método falso. Es un método **para otra pregunta**. Sirve para seguir un proceso de
extracción o comparar fracciones dentro de un mismo laboratorio. No sirve para decidir si compraste hongo.

## Cómo se comprueba lo que de verdad importa

| Pregunta real | Método correcto | Unidad |
|---|---|---|
| ¿Cuánto activo fúngico hay? | Megazyme K-YBGL, β-glucano | `% p/p base seca` (`221`) |
| ¿Cuánto grano hay? | Megazyme K-YBGL, α-glucano; almidón AOAC | `% p/p base seca` (`220`) |
| ¿Hay biomasa fúngica? | Ergosterol por HPLC-UV 282 nm | `mg/g base seca` (`238`) |
| ¿Es la especie? | Secuenciación ITS | % identidad (`245`) |
| ¿El extracto es lo que dice? | Balance de masa del proceso + ratio verificado | `ratio` (`242`, `151`) |

## Cómo responderle a un proveedor (guion)

```
Gracias por la ficha. Para poder evaluar el material necesito el dato en el
formato que usamos: beta-glucano y alfa-glucano por separado, metodo enzimatico
Megazyme K-YBGL, expresados en % p/p BASE SECA, con lote y laboratorio.

El valor de "polisacaridos totales" no nos sirve como criterio de compra porque
incluye almidon y no permite distinguir cuerpo fructifero de micelio sobre grano.

Si el analisis no esta disponible, podemos correrlo nosotros en laboratorio
independiente sobre una muestra de 100 g y ajustar la decision al resultado.
```

La reacción a ese correo te dice casi todo. Un proveedor serio te manda el dato o te dice honestamente que
no lo tiene y acepta la verificación. Un proveedor que insiste en que "es lo mismo" se está retratando.

## Qué se puede y qué no se puede afirmar

- No pongas "polisacáridos 30 %" en tu etiqueta pensando que es equivalente a β-glucano. Si lo mides como
  polisacáridos, decláralo como polisacáridos.
- No conviertas un valor de polisacáridos en un claim de actividad: la evidencia de inmunomodulación se
  ha estudiado sobre β-glucanos y preparaciones específicas, mayoritariamente `[in vitro]` y `[animal]`
  (ver `130`, `248`) — y nunca como prevención o tratamiento de enfermedades (ver `268`).
- Sí puedes usar polisacáridos totales internamente para seguir tu proceso de extracción, diciéndolo.

## Errores comunes

- Comparar "polisacáridos" de un proveedor con "β-glucano" de otro y concluir cuál es mejor. Son unidades
  distintas de cosas distintas.
- Aceptar un valor de polisacáridos por gravimetría sin saber cómo se lavó el precipitado.
- Pedir β-glucano y recibir "β-D-glucano por fenol-sulfúrico". Eso no existe: el fenol-sulfúrico no
  distingue enlaces.
- Usar el valor de polisacáridos para calcular la dosis de la etiqueta. Terminas declarando almidón como
  activo.
- No preguntar por la humedad: un polisacárido en base húmeda cambia con el clima del día del análisis
  (ver `07`).

## Conexión con otros módulos

→ `221-medir-beta-glucanos-metodo-megazyme.md` — el método que sí responde la pregunta.
→ `220-alfa-glucanos-y-almidon-el-confusor.md` — qué se está colando en el número.
→ `218-el-fraude-del-micelio-en-grano.md` — el negocio que este método permite.
→ `91-metodos-colorimetricos-y-enzimaticos.md` — fundamentos de colorimetría y sus límites.
→ `111-banderas-rojas-en-un-coa.md` — otras señales de un informe que no aguanta auditoría.
