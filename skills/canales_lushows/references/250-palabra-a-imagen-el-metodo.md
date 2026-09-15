# 250 · Palabra a imagen: el método

**Qué resuelve:** de dónde sale cada elemento del montaje. La respuesta del canal es
incómoda de aceptar y por eso funciona: **lo decide el texto, no el criterio de quien
monta**. Si la voz nombra veinte cosas, en pantalla entran veinte cosas. El diccionario
visual es la máquina que traduce eso, y este módulo es su mapa.

---

## Las tres capas, y su orden

```
CLAVE     escrito a mano. Los héroes y todo lo que lleva CIFRAS PROPIAS.
          Manda: reserva su sitio y su instante.
AUTO      generado palabra por palabra desde el vocabulario del episodio.
          Rellena alrededor de la clave, sin pisarla.
PESO      contrapeso. Segunda pasada, cuando ya está todo colocado: tapa la
          mitad del cuadro que se quedó desierta.
```

El orden no es estético, es de información: hasta que no está la mano no se sabe qué
queda libre, y hasta que no está lo generado no se sabe dónde queda el hueco. El montaje
de `ep01-lustig/guion_visual.py` lo ejecuta así:

```python
diccionario.MOTIVOS = MOTIVOS
diccionario.olvidar()   # la memoria de repeticion dura todo el episodio

# PRIMERO se anota TODA la capa escrita a mano, del episodio entero.
for _nom, _ini, _fin, _f, _m in BLOQUES:
    recordar(CLAVE.get(_nom, []), PALABRAS, _ini, _fin)

for nombre, ini, fin, fondo, mov in BLOQUES:
    clave = CLAVE.get(nombre, [])
    reservados = [...]                                   # rectángulo real, no etiqueta
    auto = generar(PALABRAS, ini, fin, reservados, vocab=V)
    peso = contrapeso(PALABRAS, clave + auto, ini, fin, CONTRAPESO.get(nombre, []))
    ESCENAS.append({... "elementos": clave + auto + peso ...})
```

Que `recordar()` corra **antes del bucle y para el episodio entero** no es un detalle de
estilo: la memoria de repetición mira hacia los dos lados del tiempo (`253`), así que una
pieza que la mano va a usar en el bloque 5 tiene que existir en la memoria mientras se
monta el bloque 4. Medido: anotando bloque a bloque, `columna_doble` sale tres veces
(20,7 · 46,1 · 59,9) y dos de ellas a 13,8 s.

## Lo que produce, medido

`python auditar.py ep01-lustig`, minuto 1 del piloto, 63,45 s:

| Capa | Elementos | De dónde salen |
|---|---|---|
| CLAVE | 20 | escritos a mano en `CLAVE` del guion visual |
| AUTO | 27 | 48 entradas de `vocabulario.V` contra 155 palabras |
| PESO | 14 | `CONTRAPESO`, 5 piezas por bloque |
| **Total** | **61** | 62,4 eventos/min · simultaneidad 2,02 · cobertura 38,0% |

## Qué aporta cada capa

Apagando capas sobre el mismo guion y la misma locución:

| Montaje | Elem | ev/min | Simult | Cobertura | Casi vacío | Huecos |
|---|---|---|---|---|---|---|
| solo CLAVE (sin AUTO ni peso) | 35 | 37,8 | 1,79 | 36,3% | 4,25 s | 0 |
| CLAVE + AUTO (sin contrapeso) | 47 | 49,2 | 1,72 | 31,7% | 8,45 s | **6** |
| las tres capas | **61** | **62,4** | **2,02** | **38,0%** | **2,40 s** | **0** |

Se lee bien de arriba abajo: la mano sola no llega al objetivo de densidad (`10`); el
diccionario la sube 12 puntos pero **abre seis huecos** porque coloca por palabra, no por
cuadro; y el contrapeso es lo que cierra los huecos sin bajar la cobertura.

## El embudo de la capa AUTO

De todo lo que suena a decisiones tomadas, en el minuto 1:

| Paso | Palabras | Comentario |
|---|---|---|
| suenan en el bloque | 155 | todo el minuto, artículos incluidos |
| sin entrada en `V` | −101 | «el», «de», «que»: no se ven |
| con entrada | 54 | 46 palabras distintas |
| descartadas por `paso_min` (0,40 s) | −2 | dos entradas en el mismo cuarto de segundo |
| descartadas por la ventana de 25 s | −10 | ver `253` |
| descartadas por no caber en ningún sitio | −15 | ver `256` |
| **colocadas** | **27** | la mitad de las que tenían imagen |

Que la mitad de las candidatas se caiga **no es un fallo**: es el sistema protegiendo el
cuadro. Lo que sería un fallo es que se cayeran sin que nadie lo supiera, y por eso el
embudo se mide.

## Por bloque

| Bloque | Duración | Palabras | Con entrada | clave + auto + peso |
|---|---|---|---|---|
| muerte | 16,15 s | 38 | 11 | 4 + 8 + 5 = 17 |
| oficio | 6,73 s | 16 | 4 | 3 + 2 + 2 = 7 |
| nombre | 11,53 s | 27 | 11 | 3 + 4 + 2 = 9 |
| torre | 15,88 s | 41 | 16 | 5 + 8 + 3 = 16 |
| metodo | 13,16 s | 33 | 12 | 5 + 5 + 2 = 12 |

`oficio` es el bloque del gancho: seis segundos, cuatro palabras ilustrables y siete
elementos. La densidad ahí no la da el diccionario, la da la mano.

## Lo que el método NO decide

El diccionario elige **qué recurso** y **cuándo**; no elige el sitio a ojo: la clase
manda la banda (`256`), el equilibrio manda la posición dentro de la banda, y el
rectángulo real manda sobre la etiqueta de la banda. Tampoco decide el sentido: eso vive
en el vocabulario del episodio (`257`), que es donde un humano declara qué significa cada
palabra en esta historia concreta.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Generar AUTO antes de anotar la mano | El generador repite cinco segundos después lo que ya hay escrito |
| Anotar la mano bloque a bloque | Lo que la mano usará más tarde no existe todavía: `columna_doble` 3 veces |
| Llamar `olvidar()` por escena | La memoria no cruza escenas: 1,32 usos por recurso (`252`) |
| Pasar a `reservados` la etiqueta de banda en vez del rectángulo | Dos elementos en bandas distintas que se solapan de verdad |
| Montar sin contrapeso «porque ya hay densidad» | 6 huecos y 8,45 s de cuadro casi vacío con la misma cobertura |
| Medir con un criterio y colocar con otro | El montaje arregla algo que el auditor no comprueba |

## Relacionado

`251` · `252` · `253` · `255` · `256` · `257` · `10` · `11` · `17`
