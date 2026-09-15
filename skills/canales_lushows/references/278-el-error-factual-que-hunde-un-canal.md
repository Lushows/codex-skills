# 278 · El error factual que hunde un canal

**Qué resuelve:** no todos los errores cuestan lo mismo, y el más caro no es el más
visible. En un canal cuyo argumento de venta es **separar lo que consta de lo que se
cuenta**, un error factual no estropea un episodio: estropea la marca. Este módulo
clasifica los errores por coste y documenta el que casi cometemos en el piloto.

---

## La taxonomía, por coste

| Tipo | Ejemplo | Qué pierde |
|---|---|---|
| **Adorno** | un coche de 1930 en una escena de 1925 | Nada, si nadie lo ve; un comentario, si lo ven |
| **Dato** | una cifra redondeada del titular en vez de la del documento | La cifra, y la confianza en las demás cifras |
| **Identidad** | una foto que coincide solo por el nombre —el error del Altiplano (§ `96`) | La confianza en **todo** el episodio |
| **Imputación** | decir «condenado por» cuando hay acusación | La credibilidad y, con persona viva, el terreno jurídico (§ `277`) |
| **De método** | afirmar como probado algo que está en la columna de la leyenda | **El canal**: es justo lo que promete no hacer |

Las dos últimas filas son las que hunden. El espectador perdona un coche; no perdona
descubrir que el vídeo que le prometía rigor no lo tenía.

## El error de método tiene una forma concreta

Poner un dato que no consta **dentro del territorio de lo que consta**. Se cuela de tres
maneras:

1. **Por la voz**, cuando se olvida la fórmula (§ `272`).
2. **Por la pantalla**, cuando la marca de columna dice una cosa y la locución otra
   (§ `273`: el desajuste real de 3,31 s del piloto).
3. **Por una pieza propia con una cifra de más.** Por eso la tarjeta de la condena federal
   va **sin año**: el certificado prueba el oficio, no la fecha. Poner 1935 habría sido
   cometer exactamente lo que el episodio denuncia (§ `271`).

## El caso del piloto: 5954-H contra 48065

Dos documentos, la misma persona, dos números:

| Documento | Número |
|---|---|
| Certificado de defunción, 1947 | **#5954-H** |
| Ficha policial | **No. 48065** |

**No es una contradicción**: son numeraciones de dos instituciones distintas y de momentos
distintos. Pero si aparecen los dos en el mismo plano, el espectador no lee «dos
instituciones»: lee **un error nuestro**. Y ese es el punto incómodo de este módulo:

> Un error *aparente* tiene el mismo coste que un error real. El espectador no tiene
> acceso a nuestras notas.

La regla que salió de ahí, escrita en la hoja de hechos antes de montar: **la ficha
policial y la casilla del número del certificado no comparten plano**. Si algún tramo
posterior obliga a juntarlas, se rotulan las dos con su institución.

## Cómo se comprueba, en vez de recordarlo

Una regla escrita en un `.md` no se cumple sola. Se declara la pareja incompatible y se
comprueba contra la tabla de eventos ya resuelta:

```python
# Piezas que NO pueden compartir plano, con el motivo escrito.
INCOMPATIBLES = [
    ("d_preso", "ficha_policial",
     "5954-H (certificado, 1947) contra No. 48065 (ficha policial): dos numeraciones"),
]

for x, y, motivo in INCOMPATIBLES:
    for a, b, r in vidas:                     # vidas = (inicio, fin, recurso)
        if r != x: continue
        for c, d, s in vidas:
            if s != y: continue
            sep = max(a, c) - min(b, d)       # negativo = se solapan
            print(("  X COMPARTEN PLANO · " + motivo) if sep < 0 else
                  f"  ok {x} [{a:.2f}-{b:.2f}] y {y} [{c:.2f}-{d:.2f}] · separados {sep:.2f} s")
```

Salida real sobre el minuto 1:

```
  ok d_preso [11.98-15.08] y ficha_policial [24.77-28.37] · separados 9.68 s
  CONSTA     4 marcas ·  9.37 s en pantalla (14.8% del tramo)
  SE CUENTA  3 marcas ·  7.32 s en pantalla (11.5% del tramo)

59 elementos · 63.45 s · 0 choque(s) de columna
```

### Lo que enseña la salida, más allá del «ok»

La hoja de hechos dice que las dos piezas están separadas **trece segundos** («preso en
12,14 · la ficha en 25,07»). La tabla de eventos resuelta contra la locución actual dice
**11,98 y 24,77**. Nadie se equivocó: la locución se movió y los anclajes se movieron con
ella. Pero la consecuencia sí importa:

> **Un número escrito a mano en una nota envejece en cuanto cambia la voz.** El número que
> manda es el que sale de resolver la tabla de eventos, y por eso esto se **mide** antes de
> cada render, no se recuerda.

Con 9,68 s de separación el margen es cómodo. Con 0,5 s no lo sería, y nadie lo habría
notado leyendo el guion visual.

## La cadena de tres filtros

Cada fallo se caza en una fase concreta, y cuesta más cuanto más tarde se detecte:

| Filtro | Fase | Qué caza | Coste de arreglarlo |
|---|---|---|---|
| **Hoja de hechos** en dos columnas | 1 · investigar | datos sin fuente, estados mal (§ `270`) | minutos |
| **Fórmulas** contra estados | 2 · guion | afirmar en indicativo lo no probado (§ `272`) | minutos |
| **Chequeo imagen ↔ voz** | 6 · guion visual | el error de identidad (§ `96`) | una hora |
| **Incompatibles + territorios** | 6 · guion visual | errores aparentes y desajustes de columna | una hora |
| **Grilla de fotogramas** | 8 · verificar | erratas, rótulos cruzados, fechas (§ `160`) | re-render |
| **El comentario de un espectador** | publicado | todo lo anterior | § `279` |

Si el error llega al último filtro, ya no es un error de producción: es un problema de
comunicación pública.

## Por qué este canal es más frágil que otros

Un canal de curiosidades que se equivoca en una fecha pierde una fecha. Nosotros hemos
puesto en pantalla una tarjeta que dice `LO QUE CONSTA` con un sello de archivo. **Hemos
subido la apuesta a propósito**, porque esa es la diferencia frente a la competencia, y la
contrapartida es que un solo error de método vale por diez de adorno.

La compensación: cuando el método se cumple, un error de adorno **no contamina** el resto,
porque el espectador ya ha visto que lo importante va marcado y citado.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Confiar en una regla escrita en la hoja de hechos y no comprobarla | La locución se mueve y la regla deja de cumplirse en silencio |
| Fiarse de un número apuntado a mano tres fases antes | 12,14 contra 11,98: pequeño hoy, mortal cuando el margen sea de medio segundo |
| Juntar dos documentos con numeraciones distintas sin rotular la institución | Error aparente = error real a ojos del espectador |
| Dar por bueno un plano porque «el dato es cierto» | Cierto y colocado en la columna equivocada sigue siendo un fallo de método |
| Rellenar una fecha que no consta para que la pieza quede completa | Se comete lo que el episodio denuncia |
| Buscar el error viendo el vídeo | Los desajustes de medio segundo no se ven; se leen en la tabla |
| Dejar todo el control para la fase 8 | Un fallo de guion corregido en la fase 8 cuesta las fases 3 a 7 |

## Relacionado

`270` el método · `271` las dos columnas en pantalla · `272` fórmulas de atribución ·
`273` marcar sin aburrir · `277` personas vivas · `279` rectificar en público ·
`96` verificación de datos · `160` la grilla de fotogramas · `167` verificación cruzada ·
`17` medir el montaje
