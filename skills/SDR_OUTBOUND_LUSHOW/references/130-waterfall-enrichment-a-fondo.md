# 130 — Waterfall enrichment a fondo

El **waterfall enrichment** (enriquecimiento en cascada) es encadenar varios proveedores de datos para que, si el primero no tiene el dato que buscas, pregunte al segundo, y al tercero, hasta encontrarlo — pagando solo por el que acierta. Es la técnica que sube tu cobertura de datos de ~60 % (un proveedor solo) a ~85–95 % (varios encadenados), decisiva en LatAm donde ningún proveedor cubre bien por sí solo. El módulo `29` te dio la idea; este te enseña a **montarla bien**: el orden correcto, cómo no quemar créditos, y la configuración exacta en Clay (`31`).

## El principio: ningún proveedor tiene todo, pero juntos casi sí

Cada proveedor de datos (Apollo, Prospeo, Hunter, Lusha, Cognism…) tiene su propia base, construida de forma distinta. Apollo es fuerte en tech y US; Cognism en móviles verificados y Europa; ningún gringo cubre bien el restaurante de Medellín. La **cobertura** de cada uno es un pedazo del universo, y los pedazos **se solapan poco**. Si preguntas a uno solo, te pierdes lo que ese no tiene. Si preguntas a cuatro en cascada, la unión de sus bases cubre casi todo.

La matemática es simple y contundente: si cada proveedor cubre 60 % **de forma independiente**, la probabilidad de que ninguno de 3 tenga el dato es 0,4 × 0,4 × 0,4 = 6,4 %. O sea: **93,6 % de cobertura** encadenando tres. En la práctica se solapan algo, así que la mejora real es menor pero igual enorme. (Para el cálculo exacto de tu caso → `Matematicas_lushows`.)

## La regla de oro del orden: barato y certero primero

Como pagas por el que **acierta**, el orden importa para el costo:

1. **Primero el que ya tienes / es gratis.** Si Apollo es tu base (`100`), empieza por él: ya lo pagaste.
2. **Luego el más barato por acierto** para ese tipo de dato.
3. **Al final el caro** (Cognism, Lusha), que solo se activa si los anteriores fallaron.

Así el proveedor premium solo cobra por el 15–20 % de filas que nadie más resolvió, no por todo.

```
WATERFALL DE CORREO (orden por costo, ejemplo):
  paso 1: Apollo        (ya pagado)      → ¿email? sí→FIN / no→sigue
  paso 2: Prospeo       (~$0.01–0.02)    → ¿email? sí→FIN / no→sigue
  paso 3: Hunter        (~$0.02–0.03)    → ¿email? sí→FIN / no→sigue
  paso 4: Datagma/Findymail                → ¿email? sí→FIN / no→"sin dato"
  SIEMPRE al final: NeverBounce/ZeroBounce verifica el ganador (`28`)
```

## Waterfalls distintos para datos distintos

No hay un solo waterfall; arma uno **por tipo de dato**, porque los proveedores fuertes cambian según el dato:

| Dato a enriquecer | Cascada sugerida (barato→caro) |
|---|---|
| **Email corporativo** | Apollo → Prospeo → Hunter → Findymail → verificar (`28`) |
| **Móvil / celular** | Apollo → Datagma → Lusha → Cognism |
| **Firmographics** (`15`) | Clay/Apollo → Clearbit → ZoomInfo |
| **Technographics** (`134`) | BuiltWith → Wappalyzer → Clay |
| **Señal (job change, funding)** | Clay + LinkedIn → UserGems (`133`) → Crunchbase (`135`) |
| **Dato PYME local** | Google Maps/Places → scraping web (`27`) → IA que lee la web |

El móvil casi siempre necesita más pasos que el email: los móviles verificados son el dato más escaso y caro.

## Cómo montarlo en Clay, paso a paso

Clay (`31`, `101`) es el orquestador estándar porque trae el waterfall **de fábrica**: es una columna especial que ya encadena proveedores.

1. **Sube tu tabla** (empresa + nombre + LinkedIn URL como mínimo).
2. **Añade una columna "Enrich Person → Find Work Email".** Clay ofrece el modo *waterfall*: eliges y **ordenas** los proveedores que quieres que consulte.
3. **Ordena por costo/acierto** (regla de oro arriba). Clay se detiene en el primero que acierta.
4. **Encadena una columna de verificación** después (NeverBounce nativo en Clay) → marca `valid / risky / invalid` (`28`).
5. **Filtra:** solo pasan a la campaña las filas con email `valid`. Las `risky` van a un waterfall extra o se descartan.
6. **Monitorea el "hit rate" por proveedor** (Clay lo muestra): si Hunter nunca acierta en tu nicho, sácalo del orden para no perder tiempo.

Clay cobra en **créditos** por búsqueda ejecutada; el waterfall bien ordenado minimiza créditos gastados porque frena temprano. Waterfall mal ordenado (caro primero) = factura inflada.

## Ejemplo real: 1.000 decisores de restaurantes en Colombia

```
Entrada en Clay: 1.000 restaurantes (nombre negocio + ciudad + web).
  Col 1: Buscar dueño/gerente en LinkedIn (Clay + Sales Nav, `26`)
  Col 2: WATERFALL email → Apollo → Prospeo → Hunter → Findymail
  Col 3: Verificar (NeverBounce) → valid/risky/invalid
  Col 4: WATERFALL móvil → Apollo → Datagma → Lusha  (para WhatsApp, `24`)
  Col 5: Google Places → nº reseñas + calificación (ángulo PYME, `29`)
  Filtro final: email = valid  → 780 contactos listos (78 % cobertura)
Costo: pagas 4 proveedores solo donde cada uno acertó, no 4× por fila.
```

## Errores comunes (qué NO hacer)

- **Poner el proveedor caro primero** → cobra por todo, no por el sobrante. Ordena barato→caro.
- **No verificar tras el waterfall** → el email recién hallado también rebota; siempre cierra con verificación (`28`).
- **Un waterfall gigante de 8 proveedores "por si acaso"** → después de 4–5 el retorno es marginal y gastas créditos. Mide el hit rate y poda.
- **Mismo waterfall para email y móvil** → son universos distintos; arma uno por dato.
- **No mirar el hit rate por proveedor** → sigues pagando por uno que nunca acierta en tu nicho.

## Frontera y siguiente paso

El waterfall te da la **materia prima** (datos con cobertura alta); convertirla en munición de mensaje es `29`, y usar esa munición para convencer y cerrar es `ventas_lushows`. Monta tu primer waterfall de email en Clay esta semana con 3 proveedores ordenados barato→caro, cierra con verificación (`28`), y mide el hit rate de cada uno para podar. Para technographics como dato del waterfall → `134`; para señales → `133`, `135`. Mantener esos datos vivos con el tiempo → `139`.
