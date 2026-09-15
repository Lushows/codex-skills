# 48 · Citas y documentos

**Qué resuelve:** el valor de una cita de expediente es que es **textual**. Si se
recita sobre una foto, el espectador sólo tiene la palabra del narrador. Puesta en
pantalla con formato de documento, la misma frase pasa de opinión a prueba — y eso es
todo el negocio de un canal de historias reales.

---

## Cuándo una frase merece este tratamiento

| Sí | No |
|---|---|
| Frase literal de una acusación, sentencia o declaración | Un resumen del narrador |
| Cifra atribuida a un organismo | Un dato general del contexto |
| Algo que el protagonista dijo, con constancia escrita | Algo que "se dice que dijo" |
| Párrafo que contradice la versión oficial | Cualquier cosa sin fuente localizable |

**Si no se puede citar el documento y la página, no se pone entre comillas.** Se
parafrasea y se sigue. Esa es la línea (`96`).

---

## Anatomía

```
   ❝
       "Los fondos se movieron a sabiendas
        de su origen ilícito."
        ───────────────────────────────────
        EE. UU. v. GUZMÁN LOERA
        2:14-cr-00196 · p. 47
```

| Pieza | Familia | Tamaño | Color | Notas |
|---|---|---|---|---|
| **Comilla de apertura** | Documento (Georgia) | 3,2× el cuerpo | rojo `#E3120B` al 85% | Decorativa, colgada del margen |
| **Cuerpo de la cita** | Documento (Georgia) | 52-72 px, interlínea 1,45 | papel `#E6DCC4` | Máximo **3 líneas** |
| **Regla** | — | 2 px, ancho del bloque | papel al 35% | Separa cita de atribución |
| **Atribución** | Dato (Consolas) | 30-36 px, `.16em`, MAYÚSCULAS | papel al 70% | Caso o documento |
| **Referencia** | Dato (Consolas) | 26-30 px, `.16em` | oro `#E8C547` al 80% | Expediente · página |

**Tres líneas es el techo.** Una cita de cinco líneas no se lee: se mira. Si el párrafo
importa entero, se parte en dos citas encadenadas o se pone el facsímil subrayado.

**Comillas tipográficas** (`«»` o `“”`), nunca la recta del teclado, que delata texto sin
componer. **La cita va en caja** (`46`): es el único texto del canal que *es* el plano
entero y no un elemento encima del plano.

---

## La lámina

```html
<!doctype html><meta charset='utf-8'><style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:transparent;overflow:hidden;width:1180px;height:520px}
.doc{font-family:Georgia,'Times New Roman',serif}
.dat{font-family:'Consolas','Courier New',monospace}
</style>
<div style="position:relative;width:1180px;height:520px;transform:rotate(-1.2deg)">
  <div style="position:absolute;inset:0;background:rgba(18,16,12,.86);
       box-shadow:0 10px 26px rgba(0,0,0,.6)"></div>
  <div class="doc" style="position:absolute;left:26px;top:-18px;font-size:210px;
       line-height:1;color:#E3120B;opacity:.85">&ldquo;</div>
  <div class="doc" style="position:absolute;left:120px;top:96px;width:990px;
       font-size:64px;line-height:1.45;color:#E6DCC4">
    Los fondos se movieron a sabiendas de su origen il&iacute;cito.</div>
  <div style="position:absolute;left:120px;top:372px;width:990px;height:2px;
       background:rgba(230,220,196,.35)"></div>
  <div class="dat" style="position:absolute;left:120px;top:404px;font-size:34px;
       letter-spacing:.16em;color:rgba(230,220,196,.70)">EE. UU. v. GUZM&Aacute;N LOERA</div>
  <div class="dat" style="position:absolute;left:120px;top:452px;font-size:28px;
       letter-spacing:.16em;color:#E8C547;opacity:.8">2&colon;14-cr-00196 &middot; p. 47</div>
</div>
```

Se renderiza con el mismo Chrome aislado que el resto de láminas (`fx.py`):
`--headless --disable-gpu --default-background-color=00000000
--virtual-time-budget=1600 --window-size=1180,520 --screenshot=…`

---

## Cómo entra

Una cita **se escribe**, no golpea. Es lo contrario que la cifra: el golpe la
convertiría en eslogan, y una cita es un documento en curso (`41`, `44`).

| Fase | Qué pasa | Tiempo |
|---|---|---|
| 0,00 | entra la caja: fundido + 18 px de deriva hacia arriba | 0,30 s |
| 0,22 | la comilla aparece con golpe corto (escala 0,8 → 1,0) | 0,16 s |
| 0,34 | el cuerpo se revela por máscara de alfa, ease-out (`47`) | ver abajo |
| final | regla, atribución y referencia, en cascada de 0,08 s | 0,26 s |

**Duración del revelado:** `caracteres / 22`, igual que la máquina de escribir (`41`).
La cita de arriba tiene 61 caracteres → **2,8 s**.

**Duración total en pantalla:** el revelado + el tiempo de lectura silenciosa del
espectador, que no es el mismo que tardó la voz en decirlo.

```
duración = caracteres/22  +  caracteres/18  +  0,6 s
```

61 caracteres → 2,8 + 3,4 + 0,6 = **6,8 s**. Es mucho para este canal, y por eso las
citas van pocas y en el momento en que la historia se detiene a respirar (`16`).

---

## Facsímil y subrayado

Cuando existe la imagen del documento real, gana el facsímil: el papel del expediente
como recorte de collage, y **la frase subrayada a mano**.

| Parámetro | Valor |
|---|---|
| Trazo | rojo `#E3120B`, 8-12 px, **bordes irregulares** (no un rectángulo) |
| Ángulo | 0,8-2° respecto de la línea de texto |
| Desborde | +10 px delante, +20 px detrás — como un rotulador que se pasa |
| Entrada | revelado por máscara de izquierda a derecha en **0,22 s**, ease-out (`47`) |
| Opacidad | 0,72-0,85, para que se lea el texto debajo · sonido: roce corto, no golpe |

Encima, ampliado, el bloque de cita compuesto: el facsímil da autenticidad y la
transcripción da legibilidad. Para sellos (`CLASSIFIED`, `EVIDENCE`, `DECOMISO`) ya hay
láminas en `fx.py`: −7°, borde de 8 px, Consolas 800, interletra `.14em`, opacidad 0,90.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cita sin expediente ni página | Es una afirmación disfrazada de prueba |
| Más de 3 líneas | No se lee; se convierte en textura |
| Comillas rectas del teclado | Delata texto sin componer |
| Cita en la familia Dato | Suena a interfaz, no a documento |
| Cita que golpea | La convierte en eslogan publicitario |
| Duración calculada sobre lo que tarda la voz | El espectador lee más despacio de lo que se recita |
| Traducir una cita y no decirlo | Si se traduce, se marca: `[trad.]` en la referencia |
| Subrayado como rectángulo perfecto | Se lee como capa digital, no como mano sobre papel |

## Relacionado

`41` máquina de escribir · `42` tipografía del canal · `46` texto sobre collage ·
`47` tipografía cinética · `62` efectos de documento · `96` verificación de datos
