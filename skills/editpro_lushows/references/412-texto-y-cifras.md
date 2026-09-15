# 412 · Texto y cifras: lo que se lee entero o no se lee

**Qué resuelve:** el texto es el intocable de tolerancia cero, y aun así es el que más se pierde, por
dos motivos distintos que se confunden: **queda tapado** (lo trata `45`) o **queda pequeño** (lo trata
`376` en milímetros sobre el vidrio). Este módulo cubre el tercer motivo, el que no está en ninguno de
los dos: **el texto encogió en el camino y nadie lo midió**, porque el cuerpo que se declara no es el
cuerpo que se ve.

---

## La fórmula, que no es opcional

Cuando el texto se genera como pieza —un PNG hecho con Chrome desde HTML, que es como trabaja el motor
del canal documental y como se hacen las piezas de Bendita Pola— hay **dos reducciones encadenadas**:

```
px_en_el_lienzo = cuerpo_declarado_en_el_HTML × (ancho_mostrado / ancho_nativo_del_PNG)
```

El `ancho_mostrado` es el `w` con el que el montaje coloca esa pieza. **No es una constante.** La misma
pieza colocada a dos anchos distintos da dos veredictos distintos, y ése es exactamente el fallo que
hay que cazar.

> **Trampa verificada en el repositorio real:** `ep01-lustig/fx_lustig.py:33` y `fx_extra.py:44`
> declaran `ANCHO_MOSTRADO = 0.80 * 1920` — 1536 px — y comprueban **todas** las piezas contra ese
> supuesto. Una pieza colocada a 520 px se auditaba como si midiera 1536: tres veces más grande de lo
> que sale en pantalla. Aprueban once medidas y la letra es ilegible.

---

## La medida, ejecutada hoy

Corrido el **11-sep-2026** sobre `ep01-lustig`, leyendo el ancho real de **cada uso** en el guion
visual y el ancho nativo de cada PNG con PIL:

```python
for n in sorted(usos):
    pw = Image.open(motor.buscar(n)).width          # ancho nativo del PNG
    c  = cuerpo(n)                                  # cuerpo más pequeño del HTML
    for w in sorted(usos[n]):                       # un veredicto POR USO
        px = c * w / pw
        print(f"{n:<14}{c:>6}{pw:>7}{w:>7}{w/pw:>7.3f}{px:>11.1f}")
```

```
pieza           HTML    PNG  mostr      x  px lienzo  veredicto
d_1890            34   1516   1340  0.884       30.1  OK
d_fecha           34   1180   1380  1.169       39.8  OK
d_preso           34   1354   1380  1.019       34.7  OK
m_consta          56    900    700  0.778       43.6  OK
m_consta          56    900    760  0.844       47.3  OK
m_cuenta          58    900    760  0.844       49.0  OK
r_casilla         38    897    968  1.079       41.0  OK
r_sinfuente       38    950    720  0.758       28.8  OK

7 piezas de texto en pantalla · el cuerpo más pequeño es 28.8 px sobre lienzo de 1920 · suelo 28 px
```

**7 piezas, la más pequeña a 28,8 px y ninguna por debajo del suelo.** Y se ve de dónde sale el número:
`r_sinfuente` se declara a 38 px en el HTML y se muestra al 0,758 de su ancho nativo → 28,8. Con 4 px
menos de cuerpo declarado habría bajado a 25,6 y nadie se habría enterado.

Fíjate también en el factor: va de **0,758 a 1,169**. Es decir, algunas piezas se *amplían*. Un supuesto
fijo del 0,80 o del 0,85 no describe nada.

---

## Los dos suelos, y cuál usar

| Suelo | Valor | De dónde sale | Cuándo manda |
|---|---|---|---|
| **Cuerpo en pantalla** | **28 px** sobre 1920 (0,0146 de la altura) | El que usa el motor del canal | Piezas HTML→PNG |
| Caja de mayúscula | 20 px sobre 1920 | `canales_lushows/164` | Cuando importa comparar fuentes |
| Milímetros en el vidrio | 4,3 mm mínimo | `376` | Cuando decide la legibilidad real en móvil |

No son tres reglas que compiten: son la misma medida en tres unidades. El de 28 px es el operativo
porque se comprueba sin abrir la fuente. Para 9:16 sobre 1080×1920, el mismo suelo en tanto por uno
de la altura da **28 px**; para 16:9 sobre 1920×1080 da **16 px**, y ahí la trampa es al revés: cabe,
pero en un móvil viendo el horizontal no se lee (`376`).

---

## La cifra tiene una regla propia

Un texto partido por una banda de interfaz pierde una palabra y se adivina. **Una cifra partida
cambia de valor.** Por eso:

- La cifra nunca se coloca a caballo de una banda. Ni de la barra del reproductor (`416`), ni del
  borde de la ventana de recorte (`417`).
- La cifra no se alinea a la derecha en vertical: ahí está la columna de iconos (`45`).
- Un contador animado **cambia de ancho mientras cuenta**. Se reserva el sitio del valor final, no del
  inicial (ver `379`), y se comprueba con el fotograma del último valor, no del primero.
- Si la cifra lleva unidad o moneda, se mide la caja **con** la unidad: `$1.250.000 COP` es 60% más
  ancho que `1250000`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Auditar el cuerpo con un `ANCHO_MOSTRADO` constante | Se aprueba una pieza que en pantalla mide un tercio |
| Un veredicto por pieza en vez de por uso | La misma pieza a dos anchos: uno legible, otro no, y sólo se ve uno |
| Registrar el cuerpo «medio» de la pieza | Lo que decide es la fuente **más pequeña** que aparece en ella |
| Una pieza sin registro de cuerpo mínimo | Aprueba por ausencia: nadie comprueba lo que nadie declaró |
| Medir en el PNG y no en el lienzo | El PNG siempre se ve grande; se muestra reducido |
| Bajar el cuerpo para que quepa el texto | Se pierde el dato. Se acorta el texto (`419`) |
| Colocar una cifra a caballo de una banda | Un texto se adivina; una cifra cambia de valor |
| Reservar el sitio del primer valor del contador | Al llegar al final se sale o se parte |
| Comprobar en el monitor grande | Ahí se lee todo, incluso lo que no se lee |

## Relacionado

`376` legibilidad en milímetros y contorno · `410` el mapa de intocables · `416` la banda de la barra ·
`419` cuando no cabe · `379` números y cifras en pantalla · `canales_lushows/164` caja de mayúscula por
fuente · `canales_lushows/49` mínimos por tipo de texto
