# 83 · Sonido diegético

**Qué resuelve:** una foto fija es un documento; una foto fija con su sonido es un
lugar. El sonido diegético — lo que suena **dentro** de la escena — es lo que convierte
un collage de recortes en algo que el espectador cree.

---

## La regla

> **Si en pantalla hay una contadora de billetes, se oye la contadora.**

No es decoración. El oído confirma o desmiente lo que ve el ojo: cuando un objeto
aparece y no suena, el cerebro lo archiva como ilustración. Cuando suena, lo archiva
como algo que pasó.

| Capa | Naturaleza | Ejemplo |
|---|---|---|
| **Diegética** | Está en el mundo de la historia | contadora, reloj, motor, papel |
| **No diegética** | Solo la oye el espectador | música (`82`), riser, impacto (`84`) |

Las dos conviven, pero **se calibran distinto**: la diegética se ancla al fotograma; la
no diegética se ancla a la frase.

## Qué pide sonido y qué no

| Sí suena | Por qué |
|---|---|
| Un objeto que se manipula (billetes, papel, moneda, puerta) | Es la acción, y la acción es lo que se cree |
| Una máquina que aparece encendida (contadora, motor, teletipo) | Si está encendida y calla, se lee como foto |
| El **lugar** de la escena (oficina, celda, túnel, bóveda) | Un room tone convierte un fondo en un sitio |
| El obturador al entrar una ficha policial o un retrato de archivo | Marca el gesto de "esto es un documento" |

| No suena | Por qué |
|---|---|
| Un rótulo, una cifra o un mapa | Son lenguaje del narrador, no del mundo. Van con pico (`84`) |
| Una persona en un retrato fijo | Pasos o voces sobre un retrato suenan a mentira |
| Todo a la vez | Más de **dos** objetos simultáneos y ninguno se identifica |

## El anclaje: el sonido llega antes que la imagen

El ojo tarda más que el oído en identificar. Igual que los elementos visuales entran
0,1-0,2 s antes de su palabra, **el efecto diegético entra antes de su fotograma**:

| Tipo | Adelanto | Motivo |
|---|---|---|
| Objeto que aparece de golpe (obturador, papel) | **−0,20 a −0,35 s** | El sonido "trae" el objeto al cuadro |
| Máquina que ya estaba (motor, contadora, reloj) | **−0,10 s** y se sostiene | Estaba antes de que lo viéramos |
| Ambiente de lugar | Con la escena, rampa de 0,25 s | Un lugar no arranca de golpe |

## Colgar el efecto de la palabra, no del segundo

Los tiempos del episodio salen de la alineación palabra por palabra. Un efecto se
ancla a **la palabra que lo nombra**, así el montaje sobrevive a cualquier retoque:

```python
def cuando(palabra, defecto=0.0):
    """Segundo exacto de una palabra del guion, para colgar de ella un efecto."""
    for p in tiempos["palabras"]:
        if p["limpia"] == palabra:
            return p["t"]
    return defecto

# (archivo, inicio, duración, ganancia, bucle)
PISTAS = [
    # el lugar: room tone de la escena, en bucle y sin apagarse
    ("amb_oficina",  esc("maquina")[0], esc("maquina")[1]-esc("maquina")[0], 0.78, True),
    ("amb_encierro", esc("remate")[0],  esc("remate")[1]-esc("remate")[0],   1.00, True),

    # objetos, cada uno colgado de su palabra
    ("ob_contadora", 0.10,                          2.6, 0.40, False),
    ("ob_billetes",  cuando("efectivo?", 15.5)-0.30, 1.6, 0.42, False),
    ("ob_boveda",    cuando("cabe",      19.4)-0.25, 2.2, 0.46, False),
    ("ob_papel",     cuando("papel",     50.2)-0.20, 0.7, 0.50, False),
    ("ob_obturador", cuando("chapo",      8.79)-0.35, 0.5, 0.44, False),
    ("ob_teletipo",  esc("piezas")[0]+0.20,          6.0, 0.26, False),
]
```

El `defecto` no es un lujo: si la palabra desaparece del guion, el efecto cae en un
segundo razonable en vez de reventar el render.

## Niveles

| Papel del sonido | Bajo la voz | Nota |
|---|---|---|
| Room tone del lugar | **−13 a −15 LU** | Es colchón; nunca se apaga dentro de su escena |
| Objeto que **es** el plano | −8 a −10 LU | La contadora cuando el plano es la contadora |
| Objeto de acompañamiento | −12 a −14 LU | El motor mientras se habla de otra cosa |
| Objeto repetitivo largo (reloj, goteo, teletipo) | **−15 a −17 LU** | Un tictac a nivel normal se vuelve insoportable en 8 s |

Los repetitivos son el error de nivel más común: se calibran escuchando **el minuto
entero**, no los dos primeros segundos.

## El room tone hace el lugar

Un fondo construido (`50`) más un `amb_*` en bucle es todo lo que hace falta para que
una escena tenga sitio. Las cuatro salas de la biblioteca (`89`) cubren el 90% del canal:

| Escena | Ambiente | Qué añade |
|---|---|---|
| Archivo, narración neutra | `amb_sala` | El room tone base, presente en TODO el episodio |
| Amenaza, cuenta atrás | `amb_tension` | Dos graves a distancia de quinta |
| Celda, túnel, bóveda | `amb_encierro` | Ruido marrón filtrado + eco: espacio cerrado |
| Oficina, banco, despacho | `amb_oficina` | 120 Hz de fluorescente + aire |

`amb_sala` va de principio a fin del episodio, por debajo de todo lo demás. Es la cola
que une escenas rodadas en mundos distintos.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Objeto en pantalla que no suena | Se lee como ilustración; la escena no se cree |
| Máquina encendida en silencio | Delata que es una foto fija |
| Tres o más objetos a la vez | Ninguno se identifica: es ruido, no diseño |
| Efecto sincronizado exacto al fotograma | Llega tarde al oído: hace falta el adelanto |
| Efecto anclado a un segundo fijo | Cualquier cambio de voz descoloca todo el sonido |
| Tictac o goteo al nivel de un objeto normal | Insoportable al medio minuto |
| Room tone que se apaga entre escenas | Reaparece el problema del colchón (`80`) |
| Pasos o voces sobre un retrato fijo | Suena a mentira: el material es fotográfico, no filmado |

## Relacionado

`80` arquitectura · `84` picos · `89` biblioteca · `39` sincronizar gesto y palabra
