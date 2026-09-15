# 176 · Cuándo un caso no se puede ilustrar

**Qué resuelve:** la decisión de abandonar un caso, tomada con un número delante y no con
una sensación.

---

## El caso real: Enron

Enron es el mejor caso de fraude contable del siglo: arco completo, cifras públicas,
documentos judiciales, el auditor que se cae con el auditado. Pasa los cuatro criterios
del banco de historias menos uno. **No se puede ilustrar.**

Se comprobó por las dos vías, y este es el resultado medido el 11-sep-2026.

**Vía 1 — la categoría de cada protagonista:**

```
Category:Kenneth Lay       files=2    subcats=0
Category:Jeffrey Skilling  NO EXISTE
Category:Andrew Fastow     NO EXISTE
```

**Vía 2 — lo que hay dentro de esos dos archivos:**

```
324x400   Public domain   File:Ken Lay.jpg              (U.S. Marshals Service)
538x171   Public domain   File:Kenneth Lay signature.png
```

Y la única foto de Skilling que aparece por búsqueda libre:

```
585x650   Public domain   File:Jeffrey Skilling mug shot.jpg
```

Ese es todo el rostro libre del caso: **dos fichas policiales de menos de 700 px de ancho
y una firma**. Fastow no tiene ninguna. Por eso `sondeo.py` devuelve **0 piezas** para
`Category:Kenneth Lay`: existen, pero no aguantan un cuadro de 1920.

## El matiz que hay que decir bien

No es «Enron no tiene fotos libres». Es: **las que hay son fichas policiales pequeñas, y
una ficha policial de 324×400 no sostiene diez minutos de documental.** Ampliada a
pantalla completa se ve el píxel; usada como recorte de 400 px dentro de un collage,
aparece tres veces por minuto y canta.

La diferencia importa porque las dos frases llevan a decisiones distintas: «no hay nada»
lleva a abandonar; «hay dos y son pequeñas» abre la puerta a contar el caso por documento
(`175`) si el guion lo aguanta.

## El árbol de decisión

```
¿Existe categoría del protagonista?
├── NO ................................. no hay imagen libre. Dato firme.
└── SÍ → ¿alguna pieza >= 1100 px?
        ├── NO ......................... hay rostro pero no sirve en pantalla
        └── SÍ → ¿>= 15 piezas del caso (no de contexto)?
                 ├── NO ............... episodio de stock; replantear
                 └── SÍ → ¿>= 40 piezas útiles totales?
                          ├── NO ...... no da para 10 min; acortar o dejar
                          └── SÍ ...... ADELANTE
```

## Las tres decisiones posibles

| Decisión | Cuándo | Qué se hace |
|---|---|---|
| **Adelante** | Pasa el árbol entero | Se escribe el guion |
| **Cambiar de forma** | Hay documentos pero no rostros | Episodio construido sobre papel: actas, acusaciones, informes. En Enron las audiencias del Congreso están escaneadas a 1275×1650 y son dominio público |
| **Cambiar de caso** | Ni rostro ni documento ni escenario propio | Se abandona y se anota en el banco |

En el piloto se eligió **cambiar de caso**: se pasó a Victor Lustig, que sondeó **988
piezas libres**, con ficha policial, cárcel, torre, imprenta y billetes. El contraste no
es de calidad de la historia: es de calidad del archivo. Y el archivo se comprobó primero.

## Lo que NO se hace cuando falta el rostro

| Salida falsa | Por qué está prohibida |
|---|---|
| Generar la cara con IA | Es un retrato inventado de una persona real. Fuera, sin excepción |
| Sacar el fotograma del documental ajeno | Obra protegida; ver `187` |
| Coger la foto de agencia «que se ve en todas partes» | Que circule no la hace libre; ver `186` |
| Usar la foto de otra persona «que se le parece» | Afirmación falsa en imagen |
| Poner una silueta negra las cincuenta veces | No es ilegal, es aburrido: el episodio se cae solo |

La reconstrucción gráfica **sí** vale: silueta rotulada como tal, mapa, diagrama del flujo
del dinero, cifra animada, el documento con la firma ampliada. Lo que no vale es fingir
que se tiene una imagen que no se tiene.

## Cómo se escribe la decisión

En el banco de historias, junto al caso, se anota literalmente el número y la fecha:

```
enron · DESCARTADO POR ARCHIVO (11-sep-2026)
  Category:Jeffrey Skilling NO EXISTE · Category:Andrew Fastow NO EXISTE
  Category:Kenneth Lay = 2 archivos, máx 538x171 y 324x400
  sondeo completo: 379 piezas libres, 11 del caso
  revisar de nuevo: sep-2027
```

Con eso el caso no se vuelve a sondear cada tres meses, y si algún día alguien libera una
foto de Skilling, la nota dice exactamente qué faltaba.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Abandonar «por intuición» | Se descarta un caso que sí tenía archivo con otro nombre |
| Seguir «ya saldrá algo» | Tres días de trabajo y un montaje sin caras |
| Comprobar solo la búsqueda libre | Homónimos; parece que hay material y no lo hay |
| Comprobar solo la categoría | Se pierde lo que nadie categorizó |
| No anotar la decisión | Se repite el mismo sondeo cada trimestre |
| Rellenar con IA o con agencia | Riesgo legal y de credibilidad del canal |

## Relacionado

`97` · `170` · `173` · `174` · `175` · `186` · `187`
