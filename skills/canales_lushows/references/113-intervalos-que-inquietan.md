# 113 · Intervalos que inquietan

**Qué resuelve:** cómo producir inquietud sin subir el volumen ni añadir efectos. Se
hace con **dos notas**, eligiendo bien la distancia entre ellas, y colocándolas en el
punto exacto del episodio donde el relato se vuelve incómodo.

---

## La tabla, con frecuencias reales

Medido con `hz()` del motor, partiendo de Re3 = **146,83 Hz**:

| Intervalo | Nota | Hz | Razón | Qué hace |
|---|---|---|---|---|
| Unísono | Re3 | 146,83 | 1,0000 | Nada |
| **2ª menor** | Mi♭3 | 155,56 | **1,0595** | Roce. Áspero, sucio, físico |
| 3ª menor | Fa3 | 174,61 | 1,1892 | Color menor. Estable |
| 4ª justa | Sol3 | 196,00 | 1,3348 | Suspende. Ni pregunta ni responde |
| **Tritono** | La♭3 | 207,65 | **1,4142** | Algo no encaja. No es sucio: es raro |
| 5ª justa | La3 | 220,00 | 1,4983 | Reposo. El colchón por defecto |
| 6ª menor | Si♭3 | 233,08 | 1,5874 | Peso hacia abajo. La caída (`115`) |
| 7ª mayor | Do#4 | 277,18 | 1,8877 | Tirón máximo hacia la tónica (`111`) |

`1,4142` es √2, la mitad exacta de la octava en semitonos: seis y seis. Por eso el
tritono no pertenece a ningún lado.

## Lo físico y lo aprendido: no es lo mismo

Hay que separarlo, porque se usan distinto.

**La segunda menor tiene base física.** Re3 (146,83) y Mi♭3 (155,56) están separadas
**8,73 Hz**, dentro de la misma banda crítica del oído a esa altura. Los dos tonos no se
resuelven como notas distintas: baten. Una octava arriba —Re4 (293,66) y Mi♭4 (311,13)—
el batido sube a **17,47 Hz**, que es cerca de donde la aspereza es máxima. Eso no
depende de la cultura de nadie: es mecánica de la cóclea.

**El tritono no.** Re3 (146,83) y La♭3 (207,65) están a 60 Hz de distancia, muy fuera de
la banda crítica: **no producen aspereza medible**. Lo que produce el tritono es una
violación de la sintaxis tonal — el oyente sabe, porque lo ha aprendido oyendo, que ese
intervalo tiene que moverse, y no se mueve. En un oyente sin esa exposición, el efecto
es mucho más débil.

> El cuento de *diabolus in musica* se suele contar mal. La frase medieval
> *"mi contra fa est diabolus in musica"* era una **regla de solfeo** sobre cantar la
> cuarta aumentada, no una prohibición religiosa del intervalo. Que el tritono inquiete
> es **convención cultural aprendida**, no una ley de la física.

Consecuencia práctica: la 2ª menor **se oye** incluso muy baja y en un altavoz malo. El
tritono necesita estar presente en la mezcla para que la sintaxis se perciba.

## El caso real del canal: la cuarta aumentada de `_sospecha`

`piano.py:164` construye el acorde de la pieza *sospecha* así:

```python
for k, acorde in enumerate(["Ab3", "D3", "F3"]):        # el tritono D-Ab
    notas.append((t0 + 1.05 + k * 0.012, acorde, 2.2, 0.34))
```

`Ab3 = 207,65 Hz` contra `D3 = 146,83 Hz` → **razón 1,4142**. Y contra el bajo
`D2 = 73,42 Hz`, la razón es 2,8283: el mismo tritono, una octava más abierto.

Y en `ep01-lustig/acabar.py:83` la pieza tiene su sitio exacto:

```python
MUSICA = {
    "nombre": ("mus_expediente", 0.45),   # el documento: lo que consta
    "torre":  ("mus_sospecha",   0.72),   # la leyenda, con su cuarta aumentada
}
```

El bloque `torre` va de **34,41 s a 50,29 s** (`guion_visual.py:37`) y, con el cruce de
1,2 s, la pieza entra en el **segundo 33,81** al nivel `0,34 × 0,72 = 0,245`. Ahí es
donde la locución deja el certificado de defunción y empieza *"la versión que ha llegado
hasta hoy dice…"*. **El tritono entra en la frase en que el episodio deja de estar
probado.** No es decoración: es la marca de agua del método del canal.

## Cómo se escriben los tres

```python
# TRITONO — inquietud, presente en la mezcla. Va EN el acorde
TRITONO = [(0.00,"D2",3.0,0.92), (1.10,"Ab3",2.2,0.34),
           (1.11,"D3", 2.2,0.34),(1.13,"F3", 2.2,0.34),
           (3.40,"D2",3.0,0.92), (4.50,"Ab3",2.2,0.34),
           (4.51,"D3", 2.2,0.34),(4.53,"F3", 2.2,0.34),
           (3.80,"Bb4",1.5,0.46),(4.75,"Ab4",1.5,0.46)]   # 10 notas · 7,67 s

# SEGUNDA MENOR — aspereza física. SIEMPRE muy por debajo del acorde
SEGUNDA = [(0.00,"D2", 3.0,0.92),(1.10,"D3", 2.2,0.34),
           (1.12,"F3", 2.2,0.34),
           (1.14,"Eb4",2.2,0.16),      # 🔴 0,16 contra 0,34: la mitad de nivel
           (1.16,"D4", 2.2,0.34)]      # 5 notas · 4,30 s

# DISMINUIDO — inestabilidad total: dos tritonos apilados. Dura poco
DISMIN  = [(0.00,"B1", 3.0,0.92),(1.10,"D3", 2.2,0.34),
           (1.12,"F3", 2.2,0.34),(1.14,"Ab3",2.2,0.34)]   # 4 notas · 4,28 s
```

El acorde disminuido `B–D–F–Ab` contiene **dos** tritonos (Si-Fa y Re-Lab). No apunta a
ninguna tónica: por eso sirve para el instante del desplome y para nada más.

## Dónde va cada uno

| Intervalo | Tramo del episodio | Nivel | Duración |
|---|---|---|---|
| 4ª justa (sus) | La pregunta, antes de la cifra | 0,34 | Libre |
| **Tritono** | Lo narrado sin prueba · la sospecha · la trampa | 0,30 – 0,36 | Un bloque entero |
| **2ª menor** | El dato incómodo, la víctima nombrada | **0,14 – 0,18** | 2-4 s. Nunca un bloque |
| Disminuido | El desplome, la detención | 0,30 | 1-2 compases |
| 6ª menor | La caída larga | 0,36 | Progresión entera (`115`) |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Segunda menor al mismo nivel que el acorde | Deja de inquietar y molesta: el espectador cierra el vídeo |
| Tritono demasiado bajo | No se percibe la sintaxis rota: se pierde el efecto y solo queda barro |
| Tritono en todo el episodio | A los tres minutos es el color normal y ya no significa nada |
| Acorde disminuido como colchón | No apunta a ninguna tónica: el oído no encuentra suelo y se cansa |
| Meter el tritono donde el relato sí está documentado | Se contradice el método del canal: el sonido dice "sospecha" y el texto dice "consta" |
| Vender el tritono como dato neurológico | Es convención aprendida. La 2ª menor sí tiene base física (batido en banda crítica) |
| Cambiar `_sospecha` sin mirar `acabar.py` | La pieza está anclada al bloque `torre`: cambiarla mueve el sentido del episodio |

## Relacionado

`110` tonalidad y significado · `111` la armonía que no resuelve · `114` modos y color ·
`115` progresiones por tramo · `92` el aporte original · `84` picos dramáticos
