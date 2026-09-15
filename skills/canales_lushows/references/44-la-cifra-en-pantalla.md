# 44 · La cifra en pantalla

**Qué resuelve:** este es un canal de dinero y las cifras son el producto. Pero una
cifra dicha se pierde y una cifra escrita mal —pequeña, sin unidad, sin fuente, con el
mismo tiempo que un rótulo— se pierde igual. Aquí está la especificación completa.

---

## Por qué una cifra necesita más tiempo

Una palabra se reconoce por su silueta: el ojo la capta entera de una fijación. **Un
número no tiene silueta.** `126` y `128` son la misma forma; hay que leer dígito a
dígito y luego reconstruir la magnitud (¿ciento veintiséis? ¿mil doscientos sesenta?).
Por eso una cifra en pantalla el mismo tiempo que un rótulo se percibe como que "pasó
algo con un número" — y esa es exactamente la sensación que arruina el dato.

```
duración = 1,1 s (base)
         + 0,30 s por cada grupo de miles
         + 0,45 s si lleva unidad o moneda
         + 0,70 s si lleva comparación
mínimo 2,0 s · máximo 6,0 s
```

| Cifra | Cálculo | Duración |
|---|---|---|
| `47` | 1,1 + 0,30 | **2,0 s** (mínimo) |
| `126 t` + comparación | 1,1 + 0,30 + 0,45 + 0,70 | **2,55 s** |
| `$207.000.000.000` | 1,1 + 4×0,30 + 0,45 | **2,75 s** |

**Y no se queda quieta.** La regla del canal —nada quieto más de 2 s— se cumple con
micro-deriva o con un cambio de estado, no alargando la fijeza (`13`).

---

## Anatomía de la cifra

Cuatro piezas, siempre en este orden de lectura:

```
   ┌──────────────────────────────┐
   │  126 TONELADAS               │  ← cifra + unidad
   │  ────────────────            │  ← regla
   │  tres tráileres cargados     │  ← comparación (opcional)
   │  DOJ · 2:14-cr-00196         │  ← fuente
   └──────────────────────────────┘
```

| Pieza | Familia | Tamaño | Color | Regla |
|---|---|---|---|---|
| **Cifra** | Dato (Consolas Bold) | 120-220 px | oro `#E8C547` | Sólo el número |
| **Unidad** | Dato (Consolas) | 40% de la cifra | papel `#E6DCC4` | Siempre presente |
| **Comparación** | Dato o Titular | 44-60 px | papel `#E6DCC4` | Ver `63` |
| **Fuente** | Dato | 28-34 px, `.16em` | papel al 60% | Nunca falta |

**El oro es de la cifra y sólo de la cifra.** Usado también en rótulo, unidad y fuente,
deja de significar "aquí está el dato" (`46`).

**Nunca en Georgia.** Sus dígitos miden 0,556 em contra 0,693 em de sus mayúsculas y
varios bajan de la línea base: una cifra en Georgia sale pequeña y descolgada (`42`).

### Formato del número

| Regla | Ejemplo |
|---|---|
| Punto de millar, coma decimal | `1.400.000` · `2,4 m` |
| Magnitudes grandes abreviadas, no en dígitos | `$1.400 M`, no `$1.400.000.000` |
| Espacio fino entre número y unidad | `126 t`, nunca `126t` |
| Moneda delante y explícita | `US$ 1.400 M` si conviven divisas |
| **Nada de decimales inventados** | Si la fuente dice "unos 200", va `≈ 200` |

Ese `≈` no es un adorno: es lo que hace defendible el episodio (`96`).

---

## El gesto de entrada

Una cifra **no se escribe** con la máquina de escribir: **golpea**. Escribirla la
convierte en trámite; el golpe la convierte en revelación (`41`).

| Fase | Escala | Tiempo |
|---|---|---|
| entrada | 0,74 → 1,06 | 0-0,18 s |
| asentamiento | 1,06 → 1,00 | 0,18-0,32 s |
| vida | deriva de 6-10 px | resto |
| salida | fundido, sin escala | 0,35 s |

El sobre-impulso a 1,06 separa el golpe del simple *fade-in*. Implementación con
`zoompan` sobre el PNG de la cifra en `47`.

Las demás piezas entran **después**, encadenadas — es el orden en que se leen:

```python
{"r": "cif_126",     "ancla": "toneladas", "offset": -0.15, "dura": 2.6, "w": 520},
{"r": "cif_126_und", "ancla": "toneladas", "offset":  0.12, "dura": 2.3, "w": 300},
{"r": "cif_126_cmp", "ancla": "toneladas", "offset":  0.55, "dura": 1.9, "w": 640},
{"r": "cif_126_fte", "ancla": "toneladas", "offset":  0.80, "dura": 1.6, "w": 380},
```

---

## Cifras que cambian

Un contador que sube vende la magnitud mejor que el número final quieto. Se hace con
`drawtext` y una expresión de tiempo — no hace falta un PNG por fotograma.

```bash
# el contador sube de 0 a 126 entre t=2,0 y t=3,4
ffmpeg -i fondo.mp4 -vf "drawtext=fontfile='C\:/Windows/Fonts/consolab.ttf':\
text='%{eif\:min(126,max(0,(t-2.0)/1.4*126))\:d\:3}':\
fontcolor=0xE8C547:fontsize=180:x=200:y=420:\
enable='gte(t,2.0)'" -y salida.mp4
```

- `%{eif:EXPR:d:3}` imprime la expresión como entero con 3 dígitos, rellenando ceros.
  Los `:` internos van escapados: `\:`.
- Aquí **no** se pone `expansion=none` — se necesita la expansión para el contador. A
  cambio, en este texto no puede haber ningún `%` literal.
- El contador **frena antes de llegar**: se le da un 15% más de tiempo del que ocupa
  la palabra, para que el número final quede fijo mientras la voz lo pronuncia.

Para barras y gráficas que crecen, ver `36` y `63`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cifra sin unidad | `126` no significa nada; con `t` es una revelación |
| Cifra sin fuente | Es una afirmación del narrador, no un dato |
| Misma duración que un rótulo | No da tiempo a reconstruir la magnitud |
| Cifra en oro *y* rótulo en oro *y* fuente en oro | El oro deja de marcar el dato |
| Cifra en Georgia | Dígitos bajos y descolgados |
| `1400000000` en pantalla | Nadie cuenta ceros; usar `1.400 M` |
| Escribirla a máquina | Un dato de impacto entra de golpe, no se teclea |
| Decimales que la fuente no da | Falsa precisión: el error que hunde el canal |
| Contador que llega justo al terminar la palabra | El número final no se llega a leer |

## Relacionado

`40` el texto como canal principal · `42` tipografía del canal ·
`47` tipografía cinética · `63` comparaciones visuales · `36` contadores y cifras
animadas · `96` verificación de datos
