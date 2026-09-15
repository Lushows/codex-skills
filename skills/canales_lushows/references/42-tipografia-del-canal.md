# 42 · Tipografía del canal

**Qué resuelve:** cada lámina se escribe con la tipografía que se tuvo a mano, así que
el episodio se ve hecho por tres personas distintas. Esto fija las **tres familias**,
sus tamaños y cuándo se usa cada una. Fuera de esta tabla no se escribe nada.

---

## ⚠️ Comprobación previa: Archivo NO está instalada

Verificado en esta máquina (`C:\Windows\Fonts`, 671 archivos, y sin carpeta de fuentes
de usuario): **no hay ningún archivo de la familia Archivo.** El CSS del proyecto dice
`font-family:'Archivo','Helvetica Neue',Arial,sans-serif` — como no existen ni Archivo
ni Helvetica Neue, **hoy todos los titulares del canal se están renderizando en Arial.**

```bash
ls C:/Windows/Fonts/ | grep -i archiv        # sin resultados = no está
```

Dos salidas, hay que elegir una: **instalarla** (Google Fonts, licencia SIL OFL) y
confirmar el nombre exacto del archivo antes de usarlo en `drawtext`, o **asumir Arial
Black** (`ariblk.ttf`) como titular — grotesca de peso extremo, que es lo que pide un
titular de portada. Mientras no se decida, el titular es Arial Black declarado a
propósito, no Arial por accidente.

---

## Las tres familias

| | **Titular** | **Dato** | **Documento** |
|---|---|---|---|
| Familia | Archivo · si no, Arial Black | **Consolas** | **Georgia** |
| Archivo `.ttf` | `ariblk.ttf` | `consola.ttf` `consolab.ttf` | `georgia.ttf` `georgiab.ttf` |
| Suplente | Arial Bold `arialbd.ttf` | Courier New `cour.ttf` | Times New Roman `times.ttf` |
| Voz | la afirmación | la prueba | la fuente |
| Caja | MAYÚSCULAS | MAYÚSCULAS o versal | Frase normal |
| Interletra | −0,01 a 0 em | +0,10 a +0,28 em | 0 em |
| Interlínea | 0,92 em | 1,35 em | 1,45 em |
| Color por defecto | papel `#EDE6D6` | oro `#E8C547` | papel `#E6DCC4` |

**Cuándo cada una:**

- **Titular** — gancho, nombre del protagonista, remate, intertítulos, cantidad
  grande. Va poco y va enorme. Nunca más de 5 palabras.
- **Dato** — todo lo que quiere leerse como salida de máquina: expedientes, fechas,
  unidades, atribuciones de fuente, sellos, contadores, rótulos. Es la familia que más
  metraje ocupa en este canal.
- **Documento** — citas textuales, párrafos de un acta, facsímiles. **Times New Roman**
  se reserva para facsímil de papel oficial mecanografiado; Georgia es editorial.

---

## La escala (lienzo 1920×1080)

Todos los tamaños son de `font-size` en píxeles. La escala es 1,25× entre pasos.

| Nivel | Uso | Titular | Dato | Documento |
|---|---|---|---|---|
| XL | cifra de impacto, gancho | 150-220 | 120-170 | — |
| L | nombre, remate | 92-120 | 76-96 | 64-80 |
| M | intertítulo, cita | 62-76 | 52-64 | 46-56 |
| S | rótulo, campo de ficha | 44-56 | 38-48 | 36-44 |
| XS | atribución, fuente, pie | — | 28-34 | 26-32 |

**Piso absoluto: 34 px**, y sólo para la fuente al pie. Nada por debajo (ver `49`).

### El tamaño NO es la altura legible

Medido con las fuentes de esta máquina — altura de la caja de mayúsculas, en em:

| Familia | Caja de `H` | Caja de `0` |
|---|---|---|
| Arial / Arial Black | 0,716 em | 0,731 / 0,740 em |
| Georgia | 0,693 em | **0,556 em** ⚠ |
| Times New Roman | 0,663 em | 0,687 em |
| Consolas | 0,638 em | 0,656 em |
| Courier New | **0,571 em** | 0,641 em |

Consecuencias que hay que tener presentes:

- Un `44 px` de Courier New tiene la misma altura real que un `35 px` de Arial. **El
  mínimo se fija sobre la altura de mayúscula, no sobre el `font-size`** (`49`).
- **Georgia lleva cifras de estilo antiguo**: sus dígitos miden 0,556 em, más bajos que
  sus mayúsculas, y el 3, el 4, el 7 y el 9 bajan de la línea base. Una cifra en
  Georgia se ve descolocada y pequeña. **Ninguna cifra va en Georgia** — las cifras son
  siempre familia Dato.

Para igualar altura óptica: `font-size = altura deseada / caja de la familia`. Una
caja de 44 px son 61 px en Arial, 63 px en Georgia y 69 px en Consolas.

---

## Cómo se escribe cada una

**Titular y documento → siempre HTML + Chrome.** `drawtext` no controla la interletra,
no parte líneas, no hace versalitas y no selecciona el peso de una fuente variable
(libfreetype renderiza la instancia por defecto). Archivo, si se instala, es variable:
sólo desde el navegador se puede pedir el peso 800.

```css
/* la cabecera de cualquier lámina de texto del canal */
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:transparent;overflow:hidden}
.tit{font-family:'Archivo','Arial Black',Arial,sans-serif;font-weight:800;
     letter-spacing:-.005em;line-height:.92;color:#EDE6D6;text-transform:uppercase}
.dat{font-family:'Consolas','Courier New',monospace;letter-spacing:.16em;
     line-height:1.35;color:#E8C547}
.doc{font-family:Georgia,'Times New Roman',serif;line-height:1.45;color:#E6DCC4}
```

**Dato → `drawtext` vale**, y es más barato cuando el texto cambia en el tiempo
(contadores, relojes, campos que se escriben). Ruta de fuente en Windows: los dos
puntos de la unidad hay que escaparlos.

```bash
ffmpeg -i fondo.mp4 -vf "drawtext=fontfile='C\:/Windows/Fonts/consolab.ttf':\
text='EXPEDIENTE 20\:52':expansion=none:fontcolor=0xE8C547:fontsize=48:\
x=120:y=880" -y salida.mp4
```

`expansion=none` desactiva la expansión de `%{…}` de drawtext: sin eso, un `%` en el
texto lanza `Stray %` y el porcentaje puede desaparecer. Comprobado (`46`).

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Declarar `'Archivo'` sin instalarla | Cae en Arial en silencio; el canal pierde su titular |
| Cifras en Georgia | Dígitos de estilo antiguo: bajos, descolgados, se ven mal alineados |
| Comparar familias por `font-size` | Courier a 44 px se lee como Arial a 35 px |
| Interletra 0 en la familia Dato | Pierde el aire de máquina; se lee como texto normal apretado |
| Titular en minúsculas | Rompe el sistema: el titular del canal es caja alta siempre |
| Cuatro familias "porque quedaba bien" | Es la señal más rápida de trabajo amateur |
| Usar `drawtext` para un titular | Sin control de interletra ni de peso variable |

## Relacionado

`40` el texto como canal principal · `41` máquina de escribir ·
`44` la cifra en pantalla · `46` texto sobre collage · `49` zona segura y tamaños
