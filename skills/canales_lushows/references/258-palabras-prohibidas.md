# 258 · Palabras prohibidas

**Qué resuelve:** que el episodio no ilustre lo que no debe ilustrar. Hay palabras que
suenan fuertes y que, puestas en imagen, activan el icono amarillo de YouTube y hunden el
CPM del canal. El foco de Paper Empires es el dinero y el documento, no el delito en
primer plano. Y hay un detalle de implementación que convirtió esta lista en decorado
durante semanas.

---

## La lista

```python
# ep01-lustig/vocabulario.py
# Estas no se ilustran aunque suenen fuertes: el foco del canal es el dinero y el
# documento, no el delito en primer plano. Activan el icono amarillo y hunden el CPM.
PROHIBIDAS = {"droga", "violencia", "muertos", "armas", "sangre", "asesinato"}
```

La del banco es parecida pero no igual —lleva «narcotrafico» y «cocaina», que vienen del
episodio del Chapo, y no lleva «sangre» ni «asesinato»—, y esa diferencia es
exactamente el tamaño del agujero.

## Dónde actúa: antes que nada

```python
for p in palabras:
    t, w = p["t"], p["limpia"]
    if not (ini <= t < fin) or w in PROHIBIDAS or w not in V_EPI:
        continue
```

Una sola línea, y el orden de ese `or` es la regla: `w in PROHIBIDAS` se evalúa **antes**
que `w not in V_EPI`. Así una palabra prohibida sigue prohibida aunque alguien le añada
una entrada al vocabulario por descuido, y la lista no depende de acordarse de limpiar
`V`. Es la única compuerta del sistema que gana al diccionario.

## El fallo: la lista del episodio no se aplicaba

`generar()` lee `PROHIBIDAS` como **global del módulo** `diccionario`. Si el guion visual
no la sustituye, se usa la del banco y la del episodio se queda mirando.

```python
diccionario.PROHIBIDAS = PROHIBIDAS
# sin esto se usaba la lista del banco y la del episodio era decorativa
```

Comprobación de que hoy sí se aplica, ejecutada tras importar el guion visual:

```
d.PROHIBIDAS: ['armas','asesinato','droga','muertos','sangre','violencia']
voc.PROHIBIDAS: ['armas','asesinato','droga','muertos','sangre','violencia']
¿son el mismo objeto? True
```

Ese `True` es la prueba. Sin la asignación, `d.PROHIBIDAS` seguiría siendo el conjunto del
banco y la comparación diría `False`.

## Cuánto costaba, medido

En el guion del episodio 01 no suena ninguna palabra prohibida, así que hoy el agujero no
cuesta nada: es **latente**. Para medirlo hay que provocarlo. Añadiendo al `PROHIBIDAS`
del episodio dos palabras que sí suenan («presos», «chatarrero»), ambas con entrada en
`V`:

| Versión | Elementos | Colgado de esas palabras |
|---|---|---|
| con la lista del episodio (actual) | 59 | nada |
| con la del banco (el fallo) | 61 | `chatarreria`, `galeria_celdas` |

Dos elementos que el episodio había prohibido expresamente, en pantalla, sin ningún
aviso. En un episodio sobre un cartel o sobre un crimen, esos dos elementos son el icono
amarillo.

## Por qué una lista y no el criterio de quien monta

Porque la decisión no es visual, es económica, y se toma una vez por canal:

1. **No la tomas en caliente.** A las dos de la mañana, montando, una foto de archivo
   fuerte parece buena idea. La lista decide por ti.
2. **Sobrevive al generador.** Con diccionario automático, nadie mira palabra por palabra
   lo que entra: la única defensa es una compuerta en el código.
3. **Es auditable.** Un episodio desmonetizado se explica mirando la lista y el guion, no
   la memoria de quien montó.

## Lo que la lista NO hace

No censura el guion: la palabra **se dice**. Se puede hablar de la droga, del asesinato o
de los muertos —es un canal de documentales, no un folleto—; lo que no se hace es
ponerles una imagen y convertir la frase en un plano. Y no cubre lo que entra a mano: la
capa `CLAVE` no pasa por `generar()`, así que un plano escrito a mano puede saltarse la
lista sin que nada avise. Ahí la compuerta es humana.

## La comprobación que conviene tener

```python
# al arrancar el montaje del episodio
assert diccionario.PROHIBIDAS is PROHIBIDAS, "el generador usa la lista del banco"
assert diccionario.NUNCA_AUTO is NUNCA_AUTO, "el generador usa NUNCA_AUTO del banco"
suenan = set(p["limpia"] for p in PALABRAS) & PROHIBIDAS
if suenan:
    print("  ! palabras prohibidas que suenan en el guion:", sorted(suenan))
```

Dos `assert` y un aviso. El coste de no tenerlos ya está medido arriba.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Editar la lista del episodio sin asignarla al módulo | La lista es decorativa; manda la del banco |
| Comprobar `PROHIBIDAS` después de consultar `V` | Una entrada añadida por descuido se salta la lista |
| Copiar la lista de otro episodio sin revisarla | Palabras de otra historia; faltan las de esta |
| Creer que cubre la capa escrita a mano | `CLAVE` no pasa por el generador |
| Prohibir la palabra en el guion en vez de en la imagen | Se empobrece el relato sin ganar CPM |
| No avisar cuando una prohibida suena | Nadie sabe que la compuerta se ha usado |

## Relacionado

`251` · `257` · `250` · `139` · `99`
