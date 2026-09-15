# 22 — Keywords negativas

Lee este módulo cuando tu campaña gasta y no vende, cuando abriste broad (ver 21) y entró tráfico raro, o simplemente cada semana como rutina sagrada. Las **keywords negativas** le dicen a Google "para estas búsquedas, NO me muestres". Son la **palanca #1** de rentabilidad en toda cuenta de Search. No es exageración: en la mayoría de cuentas que "no funcionan", el problema no es la puja ni el anuncio — es que están pagando clics de búsquedas que jamás iban a comprar, y nadie las podó. Google captura intención, sí, pero también captura **ruido** alrededor de esa intención; los negativos separan el grano de la paja.

## Por qué son la palanca #1

Google gana cuando das clics. Tú ganas cuando vendes. Esos intereses no siempre coinciden: el algoritmo, especialmente en broad, AI Max (ver 90) y PMax, va a estirarse hacia búsquedas tangenciales para gastar tu presupuesto. Los negativos son tu único freno directo.

Ejemplo real con números COP 2026: vendes la calculadora de costos a $10.000 COP. Sin negativos, broad te mete en "calculadora gratis", "plantilla excel gratis", "curso de costos gratis", "como calcular costos sin pagar", "plantilla costos pdf descargar". Cada clic de esos te cuesta $400–$1.200 COP y **nunca** compra. Si gastas $600.000/mes y el 40% se va ahí, son $240.000 quemados. Metes el negativo `gratis` (amplia) y recuperas ese 40% para búsquedas que sí pagan. Eso es más impacto que cualquier ajuste de puja: bajar el CPC un 10% es marginal; cortar el 40% de gasto inútil es transformador. Por eso un buyer serio dedica más tiempo a negativos que a pujas.

## El reporte de términos de búsqueda — tu mina

El **reporte de términos de búsqueda** (Search Terms) muestra las búsquedas REALES que dispararon tus anuncios — distinto de tus keywords, que son lo que tú pediste (ver 68 para leerlo a fondo). Aquí vives la diferencia entre lo que crees que pasa y lo que pasa.

Ruta: Campaña → Keywords → pestaña **Términos de búsqueda**.

Rutina semanal (10–15 min, no negociable):
1. Filtra por gasto de mayor a menor.
2. Lee cada término. Pregúntate: *¿esta persona compraría mi oferta?*
3. Marca los que NO → agrégalos como negativos.
4. Marca los que SÍ y no tenías → considéralos como keywords nuevas (ver 20).

Niveles de negativo (concordancia, igual que las positivas):
- `gratis` (amplia) → bloquea cualquier búsqueda con esa palabra en cualquier orden.
- `"plantilla gratis"` (frase) → bloquea esa frase contigua.
- `[calculadora gratis]` (exacta) → bloquea solo esa búsqueda exacta.

Usa amplia para palabras-veneno universales y frase/exacta cuando quieres bloquear algo específico sin matar búsquedas válidas que comparten una palabra.

## Lista de veneno universal — cópiala y aplícala el día 1

Esta lista, en concordancia amplia salvo donde se indique, aplica a casi cualquier cuenta LatAm de producto digital/B2B. Arma una lista maestra y ponla a toda cuenta nueva el día 1:

```
gratis            curso             empleo            trabajo
pdf               descargar         torrent           crack
pirata            mega              drive             "como hacer"
"paso a paso"     tutorial          ejemplo           plantilla gratis (frase)
casero            tarea             estudiante        wikipedia
youtube           significado       definición        que es (frase)
opiniones falsas  estafa            "es confiable"
```

Para gastronomía específico, suma según tu caso: `recetas` (si vendes software, no recetas), `domicilio` (si no haces domicilios), `empleo cocinero`, `vacante`, `sueldo`, `curso gastronomía`. Piensa: ¿qué busca alguien que NUNCA me compraría pero usa mis palabras? Eso va a negativos.

## Listas de negativos a nivel cuenta vs campaña

No agregues los mismos negativos uno por uno en cada campaña. Crea **listas de negativos reutilizables**:

| Nivel | Qué va ahí | Ejemplo |
|---|---|---|
| Lista a nivel cuenta | Veneno universal que NUNCA quieres en ninguna campaña | gratis, empleo, trabajo, pdf, torrent, "como hacer", pirata, crack |
| Negativos de campaña | Específicos de esa oferta | en una campaña de "restaurante", negar "cafetería" si tienes campaña aparte |
| Negativos de grupo | Para separar grupos entre sí | que "comprar" no entre al grupo informacional |

Ruta para listas: Herramientas → Configuración compartida → **Listas de exclusión de palabras clave negativas** → creas la lista → la aplicas a las campañas que quieras. Una sola lista, aplicada a 10 campañas; editas la lista y se actualizan las 10. Límite a tener presente: hasta 5.000 negativos por lista y 20 listas por cuenta — de sobra para cualquier pyme.

## Negativos en PMax, Demand Gen, AI Max y campañas automáticas

Las campañas automáticas también necesitan freno, y en 2026 por fin se puede:
- **Performance Max (ver 12, 90):** ahora admite negativos a nivel campaña directamente en la interfaz (antes tocaba pedirlos a soporte). Aplica tu lista de veneno aquí también — PMax es de las que más se estira hacia búsquedas de marca y basura.
- **Demand Gen (ver 41):** admite exclusiones de contenido y de keywords; revísalas, no la dejes correr libre.
- **AI Max for Search (ver 90):** es la que MÁS necesita negativos porque amplía keywords sola. Vigílala con la misma rutina semanal o más seguido. Úsala con la lista de veneno aplicada desde el primer día.

Regla general: a mayor automatización de la campaña, MÁS importan los negativos, no menos. El algoritmo te da alcance; los negativos te dan rentabilidad. Negativos mal puestos también rompen: si niegas `costo` en amplia vendiendo "calculadora de costos", te apagas solo.

## Negativos de marca y de contramarca — la jugada fina

Dos usos avanzados que separan al amateur del que sabe:

1. **Negar tu marca en campañas genéricas.** Si tienes una campaña de marca aparte (recomendado, ver 39), agrega tu nombre como negativo en TODAS las demás campañas. Así las búsquedas de tu marca caen donde deben (la campaña de marca, barata y de alta conversión) y no inflan el CTR de tu genérico engañándote sobre qué funciona. Sin esto, tu Search genérico se "ve" excelente cuando en realidad es la marca la que convierte.
2. **Negar marcas de competidores donde no quieres aparecer.** Si tu broad se está colando en búsquedas del competidor y eso te trae CTR bajo y Quality Score malo, niégalas; o al revés, si quieres conquista de competidor, hazlo en una campaña dedicada y niégalas en el resto para no contaminar.

## Plantilla de auditoría semanal de negativos

Bloque de 15 minutos, mismo día cada semana (vuélvelo hábito):
```
1. Search Terms → últimos 7 días → ordenar por COSTO descendente.
2. Top 20 términos: ¿compraría esta persona? NO → negativo.
3. Filtrar términos con clics > 3 y conversiones = 0 → candidatos a negativo.
4. Términos con conversiones que NO tenías como keyword → agregar como keyword nueva (ver 20).
5. Revisar que ningún negativo nuevo bloquee una keyword positiva (simulador de Google).
6. Actualizar la lista maestra de veneno si encontraste un patrón nuevo.
```
Ese ritual, sostenido, es lo que hace que una cuenta baje su CPA mes a mes en vez de estancarse. La pauta no se "deja andando"; se poda como un jardín.

## Errores comunes — blacklist

1. **No revisar términos de búsqueda nunca.** Es el error #1 absoluto. Si solo haces UNA cosa por tu cuenta cada semana, que sea esto.
2. **Agregar negativos campaña por campaña a mano.** Usa listas a nivel cuenta. Ahorra horas y evita inconsistencias.
3. **Negativo en amplia demasiado agresivo.** Negar `costo` en amplia cuando vendes "calculadora de costos" → te apagas a ti mismo. Piensa qué búsquedas válidas comparten esa palabra antes de negar en amplia; si dudas, usa frase.
4. **Olvidar negativos en PMax/Demand Gen/AI Max.** Son las que más se estiran. Sin freno, queman más rápido.
5. **Negar solo búsquedas obvias y dejar las tangenciales.** "Curso de costos" no dice gratis pero igual no compra tu calculadora. Lee la intención, no solo busques palabras feas.
6. **No tener lista de "veneno universal" lista para cuentas nuevas.** Empieza toda cuenta con gratis, empleo, trabajo, pdf, "como hacer", descargar — ya aplicada el día 1.
7. **Negar marca propia por accidente.** Cuidado al negar términos en amplia que contengan tu nombre; revisa qué bloqueas antes de guardar.
8. **No revisar negativos viejos al cambiar de oferta.** Un negativo que tenía sentido el año pasado puede estar apagando tu nueva línea de producto. Audita la lista cada trimestre.
