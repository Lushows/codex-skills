# 383 — Umbrales por tipo de contenido

**Qué resuelve:** un umbral no es una opinión, es una decisión que deja huella medible. Aquí está el
experimento completo —el mismo episodio generado dos veces cambiando solo un número— con lo que se gana y
lo que se paga. La conclusión corta: **un umbral único es siempre el umbral equivocado para la mitad del
material.**

---

## 1. El umbral doble que ya existe

En `diccionario.py`, dentro del bucle que busca posición para cada elemento generado:

```python
# Sobre TEXTO el liston es otro: cualquier solape lo hace ilegible.
# Con el umbral unico del 42% entraban recortes encima de las cifras
# y el sistema los daba por buenos.
peor = 0.0
for a, b, o, txt in vivos:
    if o is None or not _solapan(t0, t1, a, b):
        continue
    tope = 0.05 if (txt or es_texto(recurso)) else 0.42
    ch = max(pisa(c, o), pisa(o, c))
    if ch >= tope:
        peor = 1.0
        break
    peor = max(peor, ch)
```

Dos detalles que se leen rápido y valen mucho:

- **`txt or es_texto(recurso)`** — el tope estricto se aplica si es texto **cualquiera de los dos**. Da
  igual quién pise a quién: si hay texto en la pareja, manda el 0,05.
- **`max(pisa(c,o), pisa(o,c))`** — aquí sí se usa el máximo de los dos sentidos, y es correcto porque es
  una **compuerta de colocación**, no un informe. Al medir para informar se normaliza siempre por el que
  queda debajo (`380` §3).

Y hay un tercer tope, en la segunda pasada del contrapeso: `0.05 if (txt or es_texto(recurso)) else 0.30`.
Más estricto que el de colocación, porque una pieza de relleno no tiene derecho a molestar a nadie.

---

## 2. El experimento: el mismo episodio con un solo umbral

`ep01-lustig`, generado dos veces. Única diferencia: sustituir las dos líneas de `tope` por el valor único
de foto (`0.42` y `0.30`). Mismo guion, mismo vocabulario, mismo banco de recursos.

| | **umbral doble** (0,42 foto / 0,05 texto) | **umbral único** (0,42 para todo) |
|---|---|---|
| elementos colocados | **61** | 66 |
| parejas simultáneas | 96 | 121 |
| pisada-segundos | **3,33** | 6,94 |
| pisadas sobre texto por encima del 5% | **2** | **14** |

Las doce que desaparecen, con nombre y apellidos:

| El de abajo (texto) | El de encima | Tapado | Dur | Bloque |
|---|---|---|---|---|
| `m_consta` | `m_cuenta` | 31,3% | 1,81 s | metodo |
| `d_1890` | `certificado_defuncion` | 24,1% | 2,80 s | muerte |
| `d_anos` | `calle_paris` | 19,6% | 0,50 s | torre |
| `linea_03` | `bajo_la_torre` | 19,2% | 0,63 s | torre |
| `d_1890` | `retrato_lustig` | 17,4% | 1,51 s | muerte |
| `linea_06` | `plano_paris_1922` | 16,8% | 0,36 s | metodo |
| `linea_02` | `panorama_paris_1926` | 16,3% | 2,48 s | nombre |
| `linea_06` | `paris_1927` | 13,9% | 2,60 s | metodo |
| `linea_06` | `banco_paris_1929` | 11,0% | 0,42 s | metodo |
| `sello_consta` | `ficha_identidades` | 10,6% | 0,26 s | oficio |
| `d_1890` | `casilla_nombre` | 10,1% | 0,76 s | muerte |
| `linea_02` | `aviso_falsos` | 8,5% | 1,22 s | nombre |

Doce parejas sobre **siete piezas de texto distintas**: `d_1890`, `d_anos`, `linea_02`, `linea_03`,
`linea_06`, `m_consta`, `sello_consta`. Siete elementos que con el umbral único quedaban pisados y el
sistema daba por buenos.

Y fíjate en el rango: **ninguna llega al 32%.** Con un umbral del 42% no salta ni una. Todas son «leves»
según la vara de la foto y todas son ilegibles según la vara del texto.

---

## 3. Lo que cuesta el umbral estricto

Esto no sale gratis y hay que decirlo: **61 elementos frente a 66**. Cinco elementos menos, un 8% menos de
densidad. Cinco veces que el generador buscó sitio, no encontró ninguno que respetara el 5% y prefirió no
poner nada antes que pisar una cifra.

Es la decisión correcta y está escrita en el propio código: *«si aun así no cabe, se descarta: amontonarlo
encima de otro cuesta un evento y no comunica nada»*. Pero es una decisión, no un regalo. Si el episodio se
queda flojo de eventos por minuto, la salida **no** es aflojar el umbral: es añadir posiciones a las bandas
o material al banco (`canales_lushows/191`).

---

## 4. La tabla de umbrales

Con lo medido en las dos versiones, esto es lo que sostengo:

| Lo que queda debajo | Tope | Por qué ese número |
|---|---|---|
| **cifra** | 0,02 | media cifra es una cifra falsa; ni una esquina |
| **rótulo de una línea** | 0,05 | tapado a medias, el objeto se queda sin explicar |
| **marca / sello / logotipo** | 0,05 | es una señal, y una señal a medias no señala |
| **titular con plancha** | 0,08 | la plancha da margen, la palabra no |
| **documento / ficha** | 0,15 | se lee como papel; un solape leve incluso ayuda |
| **retrato (zona protegida)** | 0,20 sobre el 40% superior | `382` |
| **recorte de foto** | 0,42 | por encima de eso se paga un recorte que no se ve |
| **pieza de contrapeso** | 0,30 | el relleno no tiene derecho a molestar |
| **fondo / ambiente** | sin tope | es fondo (`382` §2) |

Los dos extremos son los que importan: **0,02 para una cifra y 0,42 para una foto es un factor de 21**. Ese
factor es el módulo entero.

---

## 5. Los tres umbrales del sistema, y por qué no coinciden

| Dónde | Valor | Para qué sirve |
|---|---|---|
| colocación (`generar`) | 0,42 / 0,05 | **evitar** que la pisada se cree |
| contrapeso | 0,30 / 0,05 | evitar que el relleno estorbe |
| auditoría (`auditar.py:563`) | 0,55 | **reportar** lo que ya se creó |

Que el de auditoría sea más flojo que el de colocación es correcto: la compuerta previene, el informe caza
lo que se escapó. Lo que **no** es correcto es que el de auditoría no distinga texto de foto, y que además
ordene la pareja por tiempo en vez de por capa. Las dos cosas, en `386`.

---

## 6. Frontera

**`directorcreativo_lushows` decide qué es legible para esta marca** —qué cuerpo mínimo, qué contraste, qué
nivel de suciedad admite el estilo. **`editpro_lushows` convierte esa decisión en un número y la
comprueba.** Si la respuesta es «en este canal la cifra es sagrada», el número es 0,02 y el generador lo
respeta en cada plano sin que nadie vuelva a mirarlo. Si el umbral concreto solo vale para el motor del
canal documental, vive en `canales_lushows`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Un umbral único para todo el material | 12 pisadas sobre 7 piezas de texto, ninguna por encima del 32% |
| Elegir el umbral por el caso más frecuente (la foto) | El texto, que es minoría, queda desprotegido siempre |
| Aflojar el umbral porque faltan eventos por minuto | Se compra densidad con información ilegible |
| Aplicar el tope estricto solo si el **de abajo** es texto | Un recorte que entra bajo una cifra también la rompe |
| Usar el umbral de colocación como umbral de informe | La compuerta usa `max()` de los dos sentidos; el informe no (`380`) |
| Tener tres umbrales y ninguno documentado | Nadie sabe cuál tocar cuando el episodio sale mal |
| Cambiar el umbral sin volver a medir el episodio entero | El efecto no es local: mover el tope recoloca todo (61 → 66 elementos) |

## Relacionado

`380` qué es pisar en números · `381` el área que importa · `382` la zona protegida · `384` medir el solape
antes de renderizar · `386` el elemento enterrado · `387` pisar a propósito ·
`canales_lushows/26` cuánto solape es correcto · `canales_lushows/141` elegir un umbral
