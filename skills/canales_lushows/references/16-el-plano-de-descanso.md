# 16 · El plano de descanso

**Qué resuelve:** la regla del hueco prohibido (`11`) llevada al absurdo produce un
episodio sin respiración. Este módulo dice los pocos casos en que el cuadro puede
aligerarse, y cómo se declara para que el auditor no lo cuente como fallo.

---

## Descanso no es hueco

| | Descanso | Hueco |
|---|---|---|
| Decisión | deliberada, declarada en la tabla | accidental |
| Elementos vivos | **1** (nunca 0) | 0 |
| Qué hace la voz | pausa, o una frase corta que remata | sigue narrando |
| Cuándo cae | justo después de un pico | en cualquier sitio |
| Duración | 1,2-2,0 s | lo que salga |
| Fondo | en movimiento y con punto de luz | el que hubiera |

**Un descanso con cero elementos es un hueco**, por bien intencionado que sea. El
espectador no distingue "aire" de "se acabó el material": lo único que ve es fondo.

## Los cinco casos válidos

1. **La revelación.** La frase que da la vuelta al episodio. Un elemento —la cifra, la
   foto, el documento— y nada más, 1,5-2,0 s. Es la frenada del módulo `15`.
2. **El silencio del guion.** Una pausa de locución de más de 0,8 s (los puntos
   suspensivos del guion). El detector de huecos la marca con `la voz dice: (silencio)`:
   ésos son los candidatos legítimos. En el piloto hay dos, de 0,60 s y 0,46 s.
3. **El fondo ES el dato.** Un mapa, un diagrama o un plano a pantalla completa que el
   espectador tiene que leer. Aquí el fondo deja de ser fondo y pasa a ser el elemento:
   se declara un rótulo encima y deja de ser descanso.
4. **El cierre del episodio.** Los últimos 2-3 s. Se baja a un elemento y se deja morir.
5. **La bisagra entre bloques.** 0,4-0,8 s con un solo elemento al cambiar de acto.
   Nunca más de 0,8 s: una bisagra larga se lee como que el vídeo se ha terminado.

Fuera de estos cinco, **no hay descanso que valga**.

## Las cuatro condiciones

Un descanso sólo es legítimo si cumple las cuatro:

| Condición | Umbral |
|---|---|
| Va después de un pico | escalada de 3-4 eventos inmediatamente antes (`15`) |
| Coincide con la voz | pausa, o frase de cierre; nunca en mitad de una enumeración |
| Dura poco | 1,2-2,0 s (0,4-0,8 s si es bisagra) |
| Hay un elemento vivo | exactamente 1, sin deriva, sin acentos encima |

Y una condición de reparto: **como mucho un descanso por minuto**, y ninguno en los
primeros 15 s. El gancho no descansa.

## Cómo se declara

En `guion_visual.py`, junto a `ESCENAS`, una lista de tramos. El auditor (`17`) la lee
con `getattr(gv, "DESCANSOS", [])` y no cuenta esos tramos como huecos:

```python
# Tramos de descanso deliberado (inicio, fin) en segundos absolutos.
# Cada uno lleva su justificacion: si no se puede escribir, no es un descanso.
DESCANSOS = [
    (22.69, 23.29),   # silencio del guion tras "de tunel"
    (24.48, 24.94),   # silencio del guion tras "rieles"
    (46.20, 47.90),   # revelacion: "dieciocho minutos de ventaja"
]
```

Escribir el motivo al lado no es burocracia: es el filtro. Un descanso que no se puede
justificar en media línea es un hueco al que se le ha puesto nombre.

## El descanso en la mezcla

El descanso visual sólo funciona si el audio no se vacía a la vez. Con el cuadro
aligerado, **el colchón tiene que seguir sonando** — si coinciden el vacío visual y el
silencio de sala, el espectador cree que el vídeo se cortó. Es la misma regla del
room tone continuo (`80`, `85`): la capa de sala nunca se apaga.

Al revés sí funciona y es de los mejores recursos del oficio: **silencio de música +
un solo elemento en pantalla** durante 1,5 s, y el golpe siguiente pega el doble.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Declarar como descanso un hueco que ya existía | Se legaliza el defecto y el auditor deja de avisar |
| Descanso en los primeros 15 s | Se pierde al espectador antes de haberlo ganado |
| Dos descansos seguidos en el mismo minuto | El episodio se desinfla y no se recupera |
| Descanso de 3 s "porque el fondo es bonito" | A partir de 2 s el fondo es una foto fija |
| Descanso sin pico delante | No es aire, es un bajón: nada lo justifica |
| Vaciar también el audio | Se lee como corte de reproducción, no como pausa |
| `DESCANSOS` sin comentario de motivo | En la revisión siguiente nadie sabe si era intención o pereza |

## Relacionado

`11` el hueco prohibido · `15` rampa de ritmo · `17` medir el montaje ·
`18` densidad por tipo de bloque · `80` arquitectura de la mezcla · `84` picos dramáticos
