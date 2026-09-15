# 376 — Legibilidad real en un celular y zonas seguras (verificado ago-2026)


> ⚠️ **Las cifras de zona segura de este módulo no son la referencia.**
> El dueño es `45-zona-segura-por-plataforma`, que además distingue el recorte
> geométrico (se calcula) de la interfaz de la app (se mide, y caduca). Antes de
> montar con un número de aquí, mídelo con `418-medir-la-zona-segura-de-verdad`.
`44` cubre la tipografía y `45` las zonas seguras. Este módulo actualiza los números a **agosto de 2026**
—incluida la unificación de zonas seguras que Meta hizo este año— y añade lo que ninguno de los dos
tiene: **cómo se mide la legibilidad de verdad**, en milímetros sobre el vidrio del teléfono, y por qué
para esta gramática el contorno le gana a la sombra.

> **Advertencia de honestidad.** Meta sí publica lineamientos de zona segura para anuncios y trae un
> chequeo integrado en el administrador de anuncios. **TikTok no publica una especificación oficial en
> píxeles**: todas las cifras que circulan son mediciones de terceros sobre capturas reales, y varían
> entre fuentes. Trata los números de TikTok como aproximaciones buenas, no como norma. Y verifica
> siempre con una captura de tu propio teléfono antes de dar algo por bueno.

---

## 1. La legibilidad no se mide en píxeles: se mide en milímetros

Un teléfono típico de 6,1" reproduce un video 9:16 a pantalla completa en unos **7 cm de ancho por 12,4
cm de alto**. Sobre un lienzo de 1080x1920, eso significa:

```
1 píxel ≈ 0,065 mm en el vidrio
```

Con eso, cualquier tamaño de texto se traduce a algo comprobable:

| Altura de mayúscula | En el vidrio | Referencia |
|---|---|---|
| 40 px | 2,6 mm | Como la letra pequeña de un contrato. **Ilegible en movimiento** |
| 67 px | 4,3 mm | Mínimo absoluto. Se lee, pero exige esfuerzo |
| **115-155 px** | **7,5-10 mm** | **El rango de la palabra suelta. Se lee sin esfuerzo** |
| 200 px | 13 mm | Titular de impacto. Solo cabe una palabra corta |
| 300+ px | 19+ mm | Solo para 2-4 letras (`NO`, `HOY`, `YA`) |

**Las tres reglas duras:**

1. **Mínimo absoluto: 3,5% de la altura del cuadro** = 67 px sobre 1920. Por debajo de eso, no importa
   qué fuente uses.
2. **Rango de trabajo para palabra suelta: 6-8% de la altura** = 115 a 155 px.
3. **El texto en movimiento necesita ~30% más de tamaño que el texto quieto.** Si el plano tiene
   movimiento de cámara o el texto entra desplazándose, sube el tamaño.

### El tamaño 15 de CapCut
El valor del control de tamaño de CapCut **no es píxeles**: es un número relativo que además se multiplica
por la escala del segmento. Lo único que importa es la altura resultante en el cuadro. Cómo se comprueba
en 30 segundos:

1. Exporta un fotograma con el texto puesto.
2. Ábrelo en cualquier visor y mide la altura de una mayúscula en píxeles.
3. Divide entre 1920. Si da menos de 0,035, no sirve.

Hazlo **una vez** con tu estilo base y ya lo sabes para siempre. Es la medición más rentable de todo el
bloque.

---

## 2. La prueba del brazo estirado

La verificación de campo, sin herramientas:

> Exporta. Manda el video a tu WhatsApp. Míralo en el celular **con el brazo estirado**, al aire libre,
> a mediodía, con el brillo al 50%.

Si se lee ahí, se lee en cualquier parte. Es más exigente que cualquier medición, porque suma tres cosas
que ningún monitor reproduce: distancia, sol, y brillo bajo.

La versión rápida de escritorio: aleja el monitor hasta que el video ocupe el ancho de una tarjeta de
crédito. Es aproximadamente la misma exigencia.

---

## 3. Contorno vs. sombra: por qué el contorno gana

La gramática medida usa **contorno sí, sombra no**. No es capricho, y conviene entender por qué para
saber cuándo romperlo.

| | **Contorno** | **Sombra** |
|---|---|---|
| Cómo separa del fondo | Rodea la letra por completo | Solo por un lado |
| Sobre fondo con detalle (una cocina, una multitud) | Funciona igual de bien en todas direcciones | Falla del lado donde no hay sombra |
| Sobre fondo claro | Funciona si el contorno es oscuro | Funciona |
| Sobre fondo oscuro | Funciona si el contorno es claro | **No hace nada**: sombra oscura sobre oscuro |
| Al comprimir la plataforma | El borde duro sobrevive bien | La sombra difuminada se convierte en bandas sucias |
| Coste de legibilidad | Come un poco de contraforma en letras cerradas | Ninguno |
| Con el sándwich (`377`) | El borde define la letra contra el sujeto | Se pierde detrás del recorte |

El punto decisivo es el tercero: **una sombra no protege contra un fondo oscuro, y el video de un
restaurante de noche o un bar es oscuro**. El contorno protege siempre porque es un anillo cerrado.

### El grosor correcto
Regla: **entre el 8% y el 12% de la altura de la mayúscula**. Con letra de 130 px, contorno de 10 a 16 px.

- Menos del 6%: no separa nada, se ve como un borde sucio.
- Más del 15%: se cierran las contraformas de la `a`, la `e`, la `o` y la palabra se vuelve una mancha.
  Esto empeora justo en las palabras grandes, que es donde menos lo esperas.

### Cuándo sí va sombra
Un solo caso: **texto pequeño sobre fondo con brillo medio y sin detalle** —un rótulo sobre una pared
lisa, la letra legal—. Ahí una sombra dura, desplazada 4-6 px, sin difuminar, sale más limpia que un
contorno. Difuminada nunca: la compresión la destroza.

---

## 4. Zonas seguras — Instagram / Facebook (dato con respaldo)

Meta unificó en **marzo de 2026** las zonas seguras de Facebook Stories, Instagram Stories, Facebook
Reels e Instagram Reels en un solo estándar 9:16, expresado en **porcentajes** en vez de píxeles fijos y
construido sobre la ubicación más exigente (Reels):

| Borde | Porcentaje | Sobre 1080x1920 |
|---|---|---|
| Superior | **14%** | 269 px |
| Inferior | **20% a 35%** | 384 a 672 px |
| Laterales | **6% cada uno** | 65 px cada lado |

El rango de abajo no es ambigüedad: **20%** es lo mínimo tolerable y **35%** es lo que de verdad ocupa la
interfaz de Reels cuando hay caption largo, nombre de cuenta, pista de audio y botón de llamado a la
acción. Para un anuncio con CTA, usa 35%. Para orgánico sin caption largo, 20-25% suele bastar.

El administrador de anuncios de Meta incluye una validación de zona segura antes de publicar: úsala, es
el único juez que no discute.

**Zona segura resultante (criterio estricto):**

```
x: 65 → 1015      (950 px de ancho útil)
y: 269 → 1248     (979 px de alto útil)
```

---

## 5. Zonas seguras — TikTok (medición de terceros, sin norma oficial)

TikTok no publica una tabla oficial en píxeles. Las mediciones de terceros hechas este año convergen en:

| Borde | Píxeles sobre 1080x1920 | Qué lo ocupa |
|---|---|---|
| Superior | ~130-160 px | Pestañas "Siguiendo / Para ti", buscador |
| Inferior | ~320 px, hasta **484 px** con CTA | Usuario, caption, disco de música, barra de navegación |
| Derecha | **~120-140 px** | Foto de perfil, corazón, comentarios, compartir, disco giratorio |
| Izquierda | ~44-60 px | Recorte por relación de pantalla en algunos equipos |

La columna derecha es la diferencia grande contra Instagram: **TikTok apila más botones y más abajo**. Un
texto que en Reels se lee perfecto puede quedar tapado por el corazón en TikTok.

---

## 6. El rectángulo que sirve para las tres redes

Si publicas la misma pieza en Instagram, TikTok y Shorts —lo normal—, olvida las tres tablas y usa el
peor caso de cada borde:

```
        0                                          1080
        ┌───────────────────────────────────────────┐
        │              NO PONER NADA                │  0 → 270
   270  ├───────────────────────────────────────────┤
        │  ┌─────────────────────────────────────┐  │
        │  │                                     │  │
        │  │        ZONA SEGURA UNIVERSAL        │  │
        │  │            810 x 980 px             │  │
        │  │       x: 130→940   y: 270→1250      │  │
        │  │                                     │  │
        │  └─────────────────────────────────────┘  │
  1250  ├───────────────────────────────────────────┤
        │              NO PONER NADA                │  1250 → 1920
        └───────────────────────────────────────────┘
       130                                        940
```

810 x 980 px. Parece poco. **Es exactamente el espacio que tienes**, y trabajar dentro de él desde el
principio ahorra rehacer piezas.

Consecuencia práctica para la cascada (`372`): con 6 palabras y paso de 170 px necesitas 850 px de alto,
y el rectángulo útil tiene 980. Cabe con 65 px de margen arriba y abajo. **Justísimo.** Por eso 6 es el
tope: no es una regla estética, es aritmética de zona segura.

---

## 7. Contraste: la medida que decide

El contraste entre la letra y lo que hay detrás manda por encima del tamaño. Cómo se verifica sin
herramientas: **pon el fotograma en blanco y negro y míralo entrecerrando los ojos.** Si el texto
desaparece contra el fondo, no hay contraste suficiente, aunque en color se vea bien.

Los tres arreglos, en orden de preferencia:

1. **Contorno del color opuesto.** Letra blanca, contorno oscuro. Resuelve el 90%.
2. **Oscurecer el fondo detrás del texto.** Una capa negra al 25-35% con desenfoque generoso, solo en la
   zona del texto. Mucho mejor que una caja de color sólido, que se ve a plantilla.
3. **Mover el texto.** Muchas veces el problema no es el texto: es que está encima de la única zona
   clara del plano. Súbelo 200 px y desaparece el problema.

---

## 8. Comprobación final antes de publicar

Cuatro pasos, cinco minutos:

1. Exporta y súbelo como **borrador** en la app real (Reels y TikTok tienen borradores).
2. Mira la vista previa **con la interfaz encima**. Es la única forma de ver dónde caen los botones de
   verdad.
3. Escribe el caption que vas a usar. Un caption de 3 líneas sube el bloque inferior y puede tapar tu
   remate.
4. La prueba del brazo estirado, al sol.

Nunca publiques desde el computador sin haber visto la vista previa dentro de la app. Es donde aparecen
el 100% de los textos tapados.

---

## Errores comunes

1. **Confiar en el tamaño que se ve en el editor del computador.** El monitor miente: el video real mide
   7 cm de ancho.
2. **Texto por debajo del 3,5% de la altura del cuadro.** Ninguna fuente lo salva.
3. **Bajar el texto a la banda inferior "para que no tape la cara".** Ahí es donde vive el caption.
4. **Ignorar la columna de botones de TikTok**, que es más ancha y más alta que la de Instagram.
5. **Usar sombra sobre fondo oscuro.** No hace absolutamente nada.
6. **Sombra difuminada.** La compresión de la plataforma la convierte en bandas sucias.
7. **Contorno de más del 15%** de la altura: cierra las contraformas y la palabra se vuelve mancha.
8. **Caja de color sólido detrás del texto.** Legible, sí; barata, también. Mejor oscurecer con desenfoque.
9. **Diseñar en la zona segura de Instagram y publicar en TikTok.** Los bordes no coinciden.
10. **Olvidar que el caption largo sube la interfaz.** Prueba con el caption real puesto.
11. **No revisar en blanco y negro.** Es la prueba de contraste más rápida que existe.
12. **Dar por oficiales los números de TikTok.** Son mediciones de terceros: verifica con tu propio
    teléfono.
13. **No usar la validación de zona segura del administrador de anuncios de Meta** cuando la pieza va a
    pauta. Es gratis y es el juez final.

---

## Checklist

- [ ] Medí una vez la altura real en píxeles de mi estilo base y es ≥ 3,5% de 1920
- [ ] La palabra suelta está entre el 6% y el 8% de la altura del cuadro
- [ ] Todo el texto vive dentro de x:130-940, y:270-1250
- [ ] La cascada más larga cabe dentro de esos 980 px de alto
- [ ] Contorno entre el 8% y el 12% de la altura de la mayúscula
- [ ] No hay sombras difuminadas en ninguna parte
- [ ] Revisé un fotograma en blanco y negro y el texto sobrevive
- [ ] Si hubo poco contraste, lo arreglé moviendo el texto o oscureciendo el fondo, no con caja sólida
- [ ] Subí un borrador a Instagram y a TikTok y vi la vista previa con la interfaz encima
- [ ] Probé con el caption real escrito, no con el campo vacío
- [ ] Hice la prueba del brazo estirado al sol
- [ ] Si va a pauta, pasé la validación de zona segura del administrador de anuncios
