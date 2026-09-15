# 299 · Cuándo una foto no aporta

**Qué resuelve:** la decisión que cierra el bloque. Los ocho módulos anteriores dicen cómo
hacer que un recorte funcione; este dice **cuándo dejar de intentarlo**. Con 36 piezas
limpias esperando en el banco (`296`), quitar sale casi siempre más barato que arreglar, y
el único error grave es no distinguir las cuatro causas, porque cada una tiene una salida
distinta.

---

## La prueba, que es de dos segundos

**Se quita el elemento y se vuelve a mirar el cuadro. Si no cambia, no estaba aportando.**

Es la misma prueba que `editpro/391` aplica al plano pequeño, y aquí vale porque el canal
no tiene lente: un recorte que no manda, no ocluye a nadie y no ilustra la palabra que se
está diciendo no está haciendo nada que se pueda medir.

La única precaución es que la prueba se hace sobre el **fotograma compuesto**, no sobre la
tabla de eventos. En la tabla todo aporta: ocupa su recuadro y suma cobertura.

## Las cuatro causas, y qué hace cada una

| Causa | Cómo se detecta | Qué se hace |
|---|---|---|
| **No se ve** | `292` antes del render, `163` después | Gamma mínima, o quitar |
| **Está tapada** | `auditar.py`, solape sobre el que entra después | Recolocar, o quitar |
| **No manda** | dominio < 0,42 durante ≥ 1 s (`293`) | Alargar al mayor, o quitar el tercero |
| **No se lee** | cuerpo mayor bajo 28 px (`297`) | Subir al suelo, o rehacer la pieza |

Y hay una quinta que no es de composición: **no ilustra nada**. Una foto correcta,
visible, dominante y legible que está en pantalla porque tocaba llenar un hueco. Esa no la
caza ninguna medida; la caza el guion (`251`: qué palabra merece imagen).

## Qué dice el episodio de hoy

```
--- elementos LAVADOS contra su fondo (3) ---   8,4 · 8,5 · 11,3   (ninguno por debajo de 8)
--- cuadro PLANO: ningun elemento manda (2.3 s) ---   dos tramos, 1,10 s y 1,20 s
--- TEXTO POR DEBAJO DE 28 px ---   14 de 23 en el cuerpo menor, 1 en el mayor
(sin seccion de elementos TAPADOS: cero)
```

**Cero tapados** es el dato que más dice, porque el umbral no es uno solo:

```python
# el texto no aguanta lo mismo que una foto: taparle el 20% a una cifra la hace
# ilegible y taparselo a una fotografia no molesta a nadie
tope = 0.18 if es_texto(r1) else 0.55
```

**18 % para el texto, 55 % para una foto.** Una foto tapada a medias sigue aportando —de
hecho la oclusión es la prueba más fuerte de profundidad que tiene un collage (`26`)—;
una cifra tapada al 20 % ya no se lee y ocupa sitio para nada. Un solo umbral, el que
fuese, habría dado falsos en un lado y ceguera en el otro.

## La salida que no es quitar: ascender a DOCUMENTO

`23` la describe para el caso del ángulo de cámara y merece repetirse aquí porque rescata
casi todo lo que fallaría por empate: cuando una foto no encaja en la escena, se deja de
fingir que está **dentro** de ella y pasa a ser **un papel pegado encima**. Margen grueso,
sombra larga, tres grados de inclinación y rótulo con la fuente. Un documento pinchado en
un tablero no tiene que empatar la perspectiva con nada.

No sirve para las cuatro causas. Sirve para el empate y el ángulo; no salva a un recorte
que no se lee ni a uno que no manda.

## El caso contrario: el hueco que sí se deja

Quitar tiene un límite, y la auditoría lo vigila por el otro lado:

```
cuadro casi vacio       3.85 s = 6%  (menos del 14% cubierto)
HUECOS                     0
   0.00 -   0.80  (0.80 s)  muerte    max 13.0%  "el once de"
```

**6 % del episodio con el cuadro casi vacío, y está bien.** Los 0,8 s del arranque, sobre
«el once de», son el aire del principio: la voz entra sola y el cuadro se llena después.
Un hueco de verdad —`HUECOS: 0`— es otra cosa y no se tolera. Entre «respirar» y «no hay
nada» hay 14 puntos de cobertura, y esa frontera está medida en `28` y en `11`.

Así que la decisión no es «quitar hasta que quede limpio», sino quitar mientras la
cobertura del tramo siga por encima del suelo. Hoy el episodio va a **36,1 % de cobertura
media**, dentro del objetivo 22–38: hay sitio para quitar dos o tres cosas.

## El orden de la decisión

1. **¿Se ve?** Si no, `292`. Es lo más barato de arreglar y lo más caro de dejar.
2. **¿La tapa alguien?** Si sí, recolocar es gratis; el elemento no tiene la culpa.
3. **¿La palabra que ilustra existe en el guion?** Si no, sobra, y ninguna corrección de
   composición lo va a cambiar.
4. **¿Cambia el cuadro si la quito?** Si no, se quita.
5. **¿Baja la cobertura del tramo por debajo del 14 %?** Entonces no se quita: se
   sustituye por una del banco.

Los pasos 1 y 2 son del auditor. El 3 es del guion visual. El 4 y el 5 son de mirar.

## Lo que nunca es la respuesta

- **Bajar la opacidad** para que «moleste menos». La opacidad siempre es 1; un elemento
  al 60 % es doble exposición, no discreción.
- **Encogerla** hasta que quepa sin estorbar. Por debajo del 34 % de la altura del lienzo
  el elemento deja de pesar y lo único que aporta es suciedad (`editpro/391`, `21`).
- **Desenfocarla** para mandarla al fondo. Sin lente no hay desenfoque creíble (`293`).
- **Dejarla porque costó buscarla.** Las 36 del banco costaron lo mismo y no están.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Confundir tapada con lavada | Dan el mismo número y tienen arreglos opuestos (`163`) |
| Un solo umbral de oclusión | Falsos en las fotos, ceguera en las cifras |
| Quitar sin mirar la cobertura del tramo | Se cambia un elemento flojo por un cuadro vacío |
| Arreglar composición cuando el problema es el guion | La imagen no ilustra nada y sigue sin hacerlo |
| Bajar la opacidad para que estorbe menos | Doble exposición: rompe el lenguaje del canal |
| Encoger por debajo del 34 % de la altura | Deja de pesar y ensucia |
| Tratar los 0,8 s de arranque como un hueco | Es el aire del principio; el hueco de verdad es otra cosa |
| Defender una pieza porque costó encontrarla | El banco entero costó lo mismo |
| Decidir sobre la tabla de eventos | Ahí todo aporta: hay que mirar el fotograma |

## Relacionado

`292` empatar recorte y fondo (la compuerta barata) · `293` profundidad sin 3D ·
`296` el recorte que no se usa · `297` documentos como imagen ·
`163` contraste elemento-fondo · `26` superposición y oclusión · `28` respiración del
cuadro · `11` el hueco prohibido · `21` peso visual y jerarquía ·
`23` empatar recorte y fondo (ascender a documento) · `251` qué palabra merece imagen ·
`editpro/391` el escalón de tamaño (el suelo del elemento)
