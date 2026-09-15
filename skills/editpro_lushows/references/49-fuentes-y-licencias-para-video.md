# 49 — Fuentes y licencias para video

## Por qué esto importa de verdad

Una fuente es software con licencia. Usar la que estaba instalada en tu computador porque venía con
Windows, con Photoshop o con un pack que bajaste de un sitio raro **te puede costar plata** — y las
fundiciones tipográficas sí demandan, especialmente cuando la fuente aparece en un anuncio pagado con
alcance medible.

El riesgo no es teórico ni parejo. Escala así:

| Uso | Riesgo |
|---|---|
| Video personal que no se publica | Ninguno en la práctica |
| Contenido orgánico de una marca pequeña | Bajo, pero real |
| **Anuncio pagado** | **Alto: hay presupuesto visible y alcance documentado** |
| Video para un cliente que lo usa comercialmente | Alto, y además te expone a ti como proveedor |
| Producto que se revende (plantillas, cursos) | Muy alto |

La buena noticia: **hay tantas fuentes libres excelentes que no hay razón para correr el riesgo.**

---

## Los tipos de licencia que te vas a encontrar

### SIL Open Font License (OFL) — la que quieres

Es la licencia de la gran mayoría de fuentes de Google Fonts y del ecosistema tipográfico libre.

**Lo que SÍ puedes hacer con una fuente OFL:**

- Usarla en video comercial, incluyendo **anuncios pagados**. Sin pagar, sin pedir permiso, sin atribución
  obligatoria en la pieza.
- Quemarla en el video (renderizarla). Un video con texto renderizado **no es distribución de la fuente**:
  la OFL no considera que incrustar la fuente en un documento o archivo sea distribuirla, así que sus
  requisitos de redistribución no aplican a tu MP4.
- Modificarla (ajustar glifos, hacer una variante) siempre que **no uses un nombre reservado** de la
  original.
- Empaquetarla y distribuirla junto con software o productos que vendes.
- Usarla en logos y marcas registradas de tus clientes.

**Lo que NO puedes hacer:**

- **Vender la fuente sola.** Ni la original ni una versión modificada, en un paquete cuyo valor sea la
  fuente misma. Esa es prácticamente la única restricción real de la OFL.
- Usar el nombre reservado (RFN) de la fuente en una versión modificada tuya.

Para lo que hacemos en video, la OFL es **permiso total**.

### Apache 2.0

Algunas fuentes de Google Fonts (Roboto, Open Sans en su origen) están bajo Apache 2.0. Igual de permisiva
para uso comercial. Sin restricciones prácticas para video.

### Licencia de escritorio (Desktop) comercial

La que compras en MyFonts, Fontspring, Adobe Fonts, etc. Cubre instalar la fuente y usarla para crear
diseños. **Normalmente cubre video**, pero:

- Lee la letra chica: algunas ponen límites por número de puestos de trabajo.
- Algunas separan "broadcast" (TV, cine) como licencia aparte y más cara.
- **Adobe Fonts** está incluida en tu suscripción de Creative Cloud y cubre uso en video, pero **solo
  mientras la suscripción esté activa**, y **no te deja compartir el archivo de la fuente** con nadie más
  ni subirlo a un servidor. Eso choca con el flujo de `fontsdir` en un pipeline compartido.

### Licencia de sistema operativo

Las fuentes que vienen con Windows o macOS **no son tuyas para usar libremente**. Están licenciadas para
usarse con ese sistema. Helvetica (macOS), Segoe UI (Windows), Calibri, Corbel, Candara: su licencia es
del sistema, no un permiso comercial abierto.

En la práctica nadie te va a demandar por usar Arial en un reel. Pero si estás cobrando por el video,
usa una fuente libre y quítate el tema de encima.

### "Free for personal use"

La trampa más común de los sitios de fuentes gratis. Significa exactamente lo que dice: **para uso
personal**. Un anuncio de tu negocio no es uso personal. Un video de cliente tampoco.

Si la página no dice claramente "OFL", "Apache 2.0", "SIL" o "commercial use allowed", **asume que no
puedes**.

---

## Dónde bajarlas

### Google Fonts — la fuente principal (fonts.google.com)

Miles de familias, casi todas OFL o Apache 2.0, descarga directa de los `.ttf`, y filtros por peso, ancho
y categoría.

Descarga desde el navegador (botón "Get font" → "Download all") o el repositorio completo:

```bash
git clone --depth 1 https://github.com/google/fonts.git
```

Son varios GB. Para una sola familia es más rápido bajarla del sitio.

Después metes el `.ttf` en `fonts/` del proyecto y lo usas con `fontsdir` (ver `43`). **No hace falta
instalarla en Windows.**

### Otras fuentes confiables

| Sitio | Qué tiene |
|---|---|
| **Fontshare** (fontshare.com) | Fuentes de la fundición Indian Type Foundry, gratis para uso comercial. Excelente calidad, look actual |
| **Velvetyne** (velvetyne.fr) | Tipografía experimental libre. Para cuando quieres algo que no se parezca a nada |
| **The League of Moveable Type** | Clásicos libres: League Gothic, League Spartan |
| **Open Foundry** | Curaduría de fuentes libres bien hechas |
| **Adobe Fonts** | Incluidas en CC. Buenas, pero atadas a la suscripción y no compartibles |
| **Fontspring / MyFonts** | Comerciales. Compras y ya es tuya. Lee la licencia |

### Los sitios que debes evitar

Cualquier página con nombre tipo "descargar fuentes gratis", "1001 fonts", "dafont" en su sección de uso
personal, o los que ofrecen packs de fuentes comerciales "gratis". Ahí encuentras:

- Fuentes comerciales pirateadas.
- Fuentes que dicen "free" y son "free for personal use".
- **Archivos incompletos**: sin tildes, sin Ñ, sin signos de apertura (¿ ¡). Es el problema más común y
  el que más te va a joder trabajando en español.

---

## El problema de los glifos en español

Muchas fuentes gratis están hechas por diseñadores angloparlantes y traen solo el juego básico ASCII.
Te enteras cuando renderizas "MÁS" y sale "MS", "MÁS" con un cuadrito, o simplemente sin la tilde.

### Verificar antes de usar

Renderiza una cadena de prueba con todos los caracteres problemáticos del español:

```bash
ffmpeg -f lavfi -i color=c=black:s=1080x600:d=1 \
  -vf "drawtext=fontfile=fonts/Anton-Regular.ttf:text='ÁÉÍÓÚ ÑñÜü ¿¡ ÀÂ':fontcolor=white:fontsize=90:x=(w-tw)/2:y=(h-th)/2" \
  -frames:v 1 -y glifos.png
```

Abre `glifos.png`. Si ves cuadritos, espacios en blanco donde debía haber letras, o caracteres
sustituidos, **esa fuente no sirve para español**. Bótala y busca otra.

Prueba también los caracteres que usas en rótulos: `·` (punto medio), `–` (raya), `€`/`$`, `%`, `°`.

### Fuentes verificadas para español (todas libres)

| Fuente | Tipo | Uso | Licencia |
|---|---|---|---|
| **Anton** | Grotesca condensada, peso único muy pesado | Golpes de subtitulado, titulares | OFL |
| **Archivo Black** | Grotesca pesada, más ancha | Titulares, alternativa a Anton | OFL |
| **Bebas Neue** | Condensada alta, solo mayúsculas | Titulares muy verticales | OFL |
| **Oswald** | Condensada, varios pesos | Subtítulos y rótulos, más versátil | OFL |
| **League Gothic** | Condensada clásica | Titulares con carácter | OFL |
| **Inter** | Grotesca neutra, muchos pesos + variable | Rótulos, descriptores, datos | OFL |
| **Barlow** | Grotesca, familia enorme (condensed, semi) | Sistema completo de una marca | OFL |
| **Space Grotesk** | Grotesca con personalidad, look técnico | Marcas de tecnología | OFL |
| **Schibsted Grotesk** | Grotesca editorial | Titulares y texto de marca | OFL |
| **Geist / Geist Mono** | Grotesca y monoespaciada modernas | Look de producto digital | OFL |
| **Playfair Display** | Serif de contraste alto | Lujo, gastronomía, editorial | OFL |
| **Instrument Serif** | Serif display elegante | Titulares de marca premium | OFL |

Todas tienen juego completo de español. Todas se pueden usar en anuncios pagados sin pagar nada.

---

## La lista negra estética

Estas fuentes son legales de usar. El problema no es la licencia: es que **cargan un significado cultural
que tú no controlas**. Ponerlas es decir algo que no querías decir.

| Fuente | Qué comunica hoy | Por qué |
|---|---|---|
| **Impact** | **Meme de 2010** | Es la fuente de los memes con texto arriba y abajo. Nada de lo que pongas en Impact se lee en serio |
| **Comic Sans** | Amateur, infantil, chiste | Diseñada para bocadillos de un asistente de Microsoft. Es el símbolo mundial del mal diseño |
| **Papyrus** | Turismo espiritual barato | Salones de yoga, tiendas esotéricas, y *Avatar*. Hay un sketch famoso sobre lo malo que es usarla |
| **Curlz MT** | Cumpleaños infantil de 2003 | — |
| **Brush Script** | Peluquería de barrio, años 90 | — |
| **Bleeding Cowboys** | Camiseta de feria | La fuente western con salpicaduras que usó todo el mundo en 2009 |
| **Trajan** | Póster de película genérico | Tanto póster de drama la gastó por completo |
| **Lobster** | Blog de comida de 2012 | Fue tan popular en su momento que quedó fechada |
| **Chalkduster / tiza** | Cafetería con pizarra falsa | — |
| **Arial** | Nada. Ausencia de decisión | No es fea, es la que sale cuando no elegiste. Se lee como descuido |

### El caso especial: el subtítulo amarillo de karaoke

No es una fuente, es un estilo: **texto amarillo con contorno negro y resalte palabra por palabra**. Es el
default de CapCut, TikTok y todas las apps de subtitulado automático.

No está mal técnicamente. Está mal porque **es la firma visual de "hecho con la plantilla"**. Millones de
videos se ven exactamente igual. Tu contenido pierde toda distinción.

La alternativa cuesta nada: blanco con **contorno del color de tu marca** (ver `40` y `44`). Mismo esfuerzo,
resultado propio.

---

## Cómo elegir la fuente de un proyecto

### 1. Pregunta si la marca ya tiene una

Si el cliente tiene manual de marca, **la fuente ya está decidida**. Tu trabajo es aplicarla, no elegir.
Si la fuente de marca es demasiado fina para video (muy común: las marcas eligen para web e impreso), usa
**el peso más pesado disponible de esa misma familia**, no otra fuente.

Si no hay identidad definida, pasa por `directorcreativo_lushows` antes de inventar.

### 2. Sistema de dos fuentes, máximo

- Una **display** pesada para los golpes y titulares (Anton, Archivo Black, Bebas Neue).
- Una **de texto** neutra para rótulos, descriptores y datos (Inter, Barlow, Space Grotesk).

Tres fuentes en un video de 45 segundos es desorden. Una sola es perfectamente válido si tiene varios
pesos.

### 3. Verifica el juego de caracteres

Antes de comprometerte, renderiza la cadena de prueba de arriba. Diez segundos que te ahorran rehacer el
proyecto.

### 4. Prueba a tamaño real, en celular

Una fuente que se ve preciosa a 300 px en el monitor puede ser ilegible a 150 px comprimida en un celular.
Ver `44`.

---

## Empaquetar las fuentes en el proyecto

```
proyecto/
  entrada.mp4
  texto.ass
  fonts/
    Anton-Regular.ttf
    Inter-SemiBold.ttf
    LICENSE-Anton.txt
    LICENSE-Inter.txt
  render.sh
```

**Guarda el archivo de licencia junto a la fuente.** Cuesta 10 segundos y es tu prueba documental si
alguien algún día pregunta. También le dice al siguiente que toque el proyecto qué puede y qué no.

Con `fontsdir=fonts` el render funciona en cualquier máquina sin instalar nada:

```bash
ffmpeg -i entrada.mp4 -vf "subtitles=texto.ass:fontsdir=fonts" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy -y salida.mp4
```

### Un aviso sobre repositorios públicos

Meter fuentes OFL en un repo de git público está permitido por la licencia (redistribución con el aviso
de copyright incluido — por eso guardas el `LICENSE`). Meter fuentes **comerciales** o de **Adobe Fonts**
en un repo público es una violación clara de licencia. Si tu proyecto usa una fuente comprada, ponla en
`.gitignore` y documenta cómo obtenerla.

---

## Errores comunes

- **Usar la fuente que estaba instalada sin verificar su licencia.** Windows y Photoshop traen fuentes
  cuya licencia no cubre tu anuncio pagado.
- **Confundir "gratis" con "libre para uso comercial".** "Free for personal use" es exactamente lo que
  dice. No sirve.
- **Bajar fuentes de sitios de packs.** Piratería, archivos incompletos, o las dos.
- **No verificar tildes y Ñ.** Es el problema más frecuente al trabajar en español con fuentes de
  diseñadores angloparlantes. Renderiza la cadena de prueba, siempre.
- **Usar Impact.** Sea lo que sea que quieras decir, va a leerse como meme.
- **Usar Comic Sans o Papyrus.** Aunque sea "irónico". No lo es.
- **Dejar que salga Arial por descuido.** Casi siempre es una sustitución silenciosa de libass porque no
  encontró tu fuente. Verifica el fotograma (`43`).
- **El subtítulo amarillo de karaoke.** Legal, funcional, y garantiza que tu video se vea igual al de un
  millón de personas.
- **Tres o más fuentes en un video corto.** Dos, máximo.
- **Elegir una fuente distinta a la de la marca porque la de marca es fina.** Usa el peso más pesado de
  la misma familia. La consistencia vale más.
- **Subir fuentes comerciales o de Adobe Fonts a un repo público.** Violación clara.
- **No guardar el archivo de licencia junto a la fuente.** Es tu única prueba documental.
- **Elegir por cómo se ve en el monitor a 300 px.** Se elige por cómo se lee en celular a tamaño real.

---

## Checklist

- [ ] Sé bajo qué licencia está **cada** fuente que uso en este proyecto.
- [ ] Todas son OFL, Apache 2.0, o compradas con licencia que cubre video comercial.
- [ ] Ninguna es "free for personal use".
- [ ] Ninguna viene de un sitio de packs de dudosa procedencia.
- [ ] Rendericé la cadena de prueba `ÁÉÍÓÚ Ññ ¿¡` y **los glifos existen y se ven bien**.
- [ ] Verifiqué también los símbolos que uso: `· – $ % °`.
- [ ] Ninguna fuente está en la lista negra estética (Impact, Comic Sans, Papyrus, Trajan...).
- [ ] No estoy usando el subtítulo amarillo de karaoke por defecto.
- [ ] Máximo dos fuentes en la pieza: una display pesada y una de texto.
- [ ] Si la marca tiene fuente definida, la estoy usando (en su peso más pesado si hace falta).
- [ ] Las fuentes están en `fonts/` del proyecto, con `fontsdir=fonts` en el comando.
- [ ] El archivo `LICENSE` de cada fuente está guardado junto a ella.
- [ ] Si hay fuentes comerciales, están en `.gitignore` y documenté cómo obtenerlas.
- [ ] Confirmé en un fotograma renderizado que se usó la fuente correcta, no una sustitución.
- [ ] Probé la legibilidad a tamaño real en un celular, no en el monitor.
