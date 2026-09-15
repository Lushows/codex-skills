# 297 · Documentos como imagen: el suelo de legibilidad

**Qué resuelve:** un gráfico con texto se genera a un ancho y se enseña a otro. El
generador comprueba su propia legibilidad contra un ancho **constante** —0,80 del lienzo,
1536 px— y se aprueba a sí mismo; el montaje lo saca a 520. Quince de dieciséis piezas
pasaban una prueba que medía otra cosa. La comprobación tiene que vivir donde se conoce el
ancho de verdad, y el número que la hace posible se calcula **del propio HTML**.

`48` explica por qué una cita en pantalla convierte una afirmación en prueba. `62` tiene
los gestos que se hacen encima de un documento. `164` mide la legibilidad por altura sobre
el render. Aquí: **el suelo, de dónde sale, y qué pasa cuando manda.**

---

## El suelo, calculado del HTML

```python
SUELO_TEXTO = 28.0          # px en pantalla sobre lienzo de 1920

def ancho_legible(recurso):
    """Ancho minimo en px para que el cuerpo MAYOR del grafico llegue al suelo."""
    nativo = Image.open(ruta).size[0]
    src = io.open(os.path.join(os.path.dirname(ruta), "_" + recurso + ".html")).read()
    cuerpos = [float(x) for x in re.findall(r"font-size\s*:\s*([\d.]+)px", src)]
    return int(SUELO_TEXTO * nativo / max(cuerpos) + 0.5)
```

Tres decisiones, y la del medio es la que hace que el sistema funcione:

- **El HTML es la fuente.** Los gráficos del canal se dibujan en Chrome y se capturan; el
  `.html` queda al lado del `.png`. Leer los `font-size` de ahí da el cuerpo real en píxeles
  nativos sin OCR, sin heurísticas y sin medir alturas de letra en la imagen.
- **`max(cuerpos)`, el cuerpo MAYOR.** Es la decisión no obvia. Si se usara el menor, cada
  gráfico con una nota a pie exigiría un ancho imposible y el montaje no podría colocar
  nada. La regla del canal es más honesta: **la letra pequeña puede ser textura; lo que no
  puede pasar es que ni el titular se lea.**
- **28 px sobre 1920.** Es el 2,6 % de la altura del cuadro. Coincide con el suelo de
  `164` y sobrevive a la prueba del pulgar (`166`).

## Medido hoy: 23 piezas con texto en `ep01-lustig`

| Recurso | Nativo | `w` | Escala | Cuerpo menor | Cuerpo mayor | Suelo |
|---|---|---|---|---|---|---|
| `huella_expediente` | 1700 | 820 | ×0,48 | **16,4** | 46,3 | 496 |
| `titular_prensa` | 1280 | 620 | ×0,48 | **16,5** | 44,6 | 390 |
| `ficha_identidades` | 1660 | **861** | ×0,52 | 17,6 | 28,0 | **861** |
| `columna_doble` | 1620 | **872** | ×0,54 | 18,3 | **28,0** | **872** |
| `mapa_ruta` | 1660 | **894** | ×0,54 | 18,3 | 28,0 | **894** |
| `reloj_1947` | 900 | 510 | ×0,57 | 19,3 | 40,8 | 350 |
| `balanza_05` | 1560 | **1040** | ×0,67 | 22,7 | 28,0 | **1040** |
| `linea_00` | 1700 | **1190** | ×0,70 | 26,6 | 28,0 | **1190** |
| `c_oficio` | 1220 | 1011 | ×0,83 | 28,2 | 39,8 | 712 |
| `d_preso` | 1354 | 1380 | **×1,02** | 34,7 | 152,9 | 253 |
| `m_cuenta` | 900 | 760 | ×0,84 | 49,0 | 49,0 | 434 |

Lo que hay que leer:

- **El suelo manda de verdad.** Cinco piezas —`ficha_identidades`, `columna_doble`,
  `mapa_ruta`, `balanza_05`, `linea_00`— tienen `w` **exactamente igual** a su suelo. No es
  coincidencia: el motor las subió hasta ahí. Sin el suelo, el equilibrio del cuadro las
  habría dejado a 600 y su titular habría salido a 19 px.
- **14 de 23 tienen el cuerpo menor por debajo de 28 px.** Y está bien. En
  `huella_expediente` el menor son 16,4 px de referencia de expediente: eso es textura de
  documento, y el titular sale a 46,3.
- **Solo una pieza falla de verdad.** `columna_doble` tiene el cuerpo mayor justo en el
  suelo y el menor en 18,3: no le sobra nada. Es la que hay que rehacer con menos texto,
  no con más ancho.
- **`d_preso` se estira un 2 % por encima de su nativo.** `editpro/391` avisa de que
  escalar por encima del nativo baja la acutancia sin que nadie lo pida. Dos por ciento es
  inocuo; conviene que no crezca.

## Dónde se aplica, y las dos políticas

En la capa automática el suelo **descarta o levanta**, sin avisar:

```python
suelo = ancho_legible(recurso)
if suelo:
    if pr and suelo * pr > H_LIENZO * 0.78:
        continue                  # legible no cabe: la pieza no entra
    ancho = max(ancho, suelo)
```

En la capa **clave** —los elementos que alguien puso a propósito— avisa en vez de
descartar:

```python
if suelo and e.get("w", 400) < suelo:
    if pr and suelo * pr <= 0.78 * 1080:
        e["w"] = suelo
    else:
        print(f"  ! {e['r']}: no cabe legible (necesita {suelo} px de ancho"
              f" y {suelo*pr:.0f} de alto)")
```

Dos políticas distintas para el mismo número, y es correcto: una pieza automática que no
cabe legible sobra; una pieza que el autor colocó a mano es una decisión suya, y el sistema
le dice el problema en vez de tomarle la decisión.

El suelo también gana al escalón de profundidad (`293`): `ancho = max(int(ancho*0.79),
suelo)`. Encoger un gráfico hasta que deje de leerse para ganar profundidad es cambiar un
defecto por otro peor.

## El tratamiento del documento, que es el contrario al del resto

| Parámetro | Foto de archivo | **Documento** | Por qué |
|---|---|---|---|
| `virar` | 0,18 – 0,78 | **0** | Envejecerlo le quita el contraste de la tinta (`197`) |
| `grano` | True | **False** | La capa se lleva el 10,2 % del contraste (`295`) |
| `nitidez` | — | **+0,4 a +0,7** | Positiva: el documento está para leerse |
| `contraste` | 1,04 – 1,10 | **1,08 – 1,12** | Un punto más, en la misma dirección |
| Empate con el fondo | color | **el margen de papel** (`25`, `291`) | No lo da el virado |

Y el aviso que sale de `294`: **los documentos van en modo `revista`, y ahí la sombra
degenera en una barra negra dura.** 22 de los 69 recortes del episodio la llevan, y son
justo estos. Hasta que se arregle la máscara, un documento tiene margen de papel pero no
tiene sombra.

## Dos cosas que corregir en el informe

La línea que imprime la auditoría es:

```
--- TEXTO POR DEBAJO DE 28 px EN PANTALLA (14 de 56) ---
```

**El 56 es el total de recursos del montaje, no el de piezas con texto.** Son 23 las que
tienen HTML propio, así que lo honesto es «14 de 23». Y el bucle imprime `sorted(ilegibles)[:12]`:
hoy hay 14 y solo se ven 12. Las dos son de una línea:

```python
print(f"\n  --- TEXTO POR DEBAJO DE {SUELO_PX:.0f} px EN PANTALLA "
      f"({len(ilegibles)} de {len(con_texto)} piezas con texto) ---")
for menor, r, nat, w, e, mayor in sorted(ilegibles):        # sin [:12]
```

Mientras tanto, el número que hay que mirar en el informe no es el titular sino la columna
**cuerpo mayor**: si baja de 28, es un defecto; si solo baja el menor, hay que mirar la
pieza.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Comprobar la legibilidad en el generador, contra un ancho fijo | Quince de dieciséis piezas aprueban una prueba que mide otra cosa |
| Calcular el suelo con el cuerpo menor | Ningún gráfico con nota al pie cabría nunca |
| Encoger un gráfico con texto para ganar profundidad | Se cambia un cuadro plano por un texto ilegible |
| Envejecer un documento | Pierde el contraste de tinta, que era su única función (`197`) |
| Ponerle la capa de grano a un documento | −10,2 % de contraste donde más se nota (`295`) |
| Estirar una pieza por encima de su nativo | Baja la acutancia sin que nadie lo pida (`editpro/391`) |
| Leer «14 de 56» como 14 de 56 piezas con texto | Son 14 de 23; el informe compara contra el total |
| Descartar en silencio una pieza clave por el suelo | La puso alguien a propósito: hay que avisar, no decidir |

## Relacionado

`48` citas y documentos · `62` efectos de documento · `164` legibilidad por altura ·
`166` la prueba del pulgar · `197` envejecer para que empate (la excepción del documento) ·
`25` el borde de papel · `291` el borde de papel medido · `293` profundidad sin 3D ·
`294` la sombra que convence · `295` grano común · `298` el archivo que se lee
