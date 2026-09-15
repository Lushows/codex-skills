# 344 — Cámara lenta y velocidad en comida

**Qué resuelve:** cuándo la comida pide lentitud y cuándo la lentitud la mata. La cámara lenta es el
efecto más usado y peor usado del contenido gastronómico: hace que un vertido sea hipnótico y que unas
manos trabajando se vuelvan insoportables.

**La regla que resume el módulo:**

> **La cámara lenta es para eventos que duran MENOS de un segundo en la vida real.**
> Todo lo demás se ve mejor a velocidad normal.

---

## 1. La matemática, sin misterio

Grabar en cámara lenta es grabar **más fotogramas por segundo de los que se van a reproducir**.

```
Grabas a 120 fps  ->  se reproduce a 30 fps  ->  4 veces mas lento  (25% de velocidad)
Grabas a 240 fps  ->  se reproduce a 30 fps  ->  8 veces mas lento  (12,5%)
Grabas a  60 fps  ->  se reproduce a 30 fps  ->  2 veces mas lento  (50%)
```

Verificado con una prueba real: 2 segundos grabados a 120 fps se convierten en **8 segundos exactos** a
30 fps, conservando los 240 fotogramas. Nada se inventa, nada se repite: por eso se ve fluido de verdad.

**El número que importa de verdad:** cuánto va a durar en pantalla.

```
Accion real       Factor    Duracion en pantalla     Veredicto
0,4 s (salpicon)   x8        3,2 s                    perfecto
0,8 s (chorro)     x4        3,2 s                    perfecto
1,5 s (vertido)    x4        6,0 s                    ya es largo -> usar x2
3,0 s (cortar)     x4       12,0 s                    MUERTO. usa velocidad normal.
```

**El límite práctico en un reel: ningún plano lento debería pasar de 3 segundos en pantalla.** Si te
pasas, no es "cinematográfico": es que el video se detuvo.

---

## 2. Lo que la cámara lenta te cuesta (y nadie te dice)

### a) Luz. Muchísima luz.

Para grabar a 120 fps el obturador tiene que ser mínimo 1/120 s, y a 240 fps mínimo 1/240 s. Cada salto
**divide la luz que entra a la mitad**:

```
30 fps  con obturador 1/60    ->  luz de referencia
120 fps con obturador 1/120   ->  la MITAD de luz
240 fps con obturador 1/240   ->  la CUARTA PARTE de luz
```

Consecuencia directa para un bar de noche: **la cámara lenta a 240 fps en tu bar, con la luz del bar,
va a salir con ruido y con colores sucios.** No es que tu celular sea malo: es física.

**Qué hacer con eso, en orden:**

1. **Cámara lenta de día, en la ventana.** Ahí sobra luz y sale limpia. Los planos de cerveza y salsa
   grábalos en la mesa de la ventana, aunque el video "sea de noche" (`340`).
2. Si tiene que ser de noche: **120 fps, no 240**, y acerca la lámpara.
3. Si aun así sale sucia: grábalo a **30 fps y ralentiza a 50%** en la edición. Se ve un poco menos
   fluido pero mucho más limpio. Limpio le gana a fluido siempre.

### b) Parpadeo de los LED

Colombia va a **60 Hz**. A 120 y 240 fps aparecen **bandas horizontales moviéndose** bajo casi cualquier
LED barato. En cámara lenta el problema se magnifica porque estás muestreando el parpadeo muchas veces
por segundo.

**Regla:** cámara lenta bajo LED del bar = revisa la pantalla antes de grabar. Si hay bandas, cambia a
luz de ventana o a una fuente distinta. Si el celular tiene "anti-parpadeo / anti-flicker" en ajustes,
ponlo en **60 Hz**.

### c) El sonido se pierde

El audio grabado en modo cámara lenta o no existe o queda irreconocible. **Todo plano lento se queda
mudo y hay que ponerle sonido después** (`346`, `77`). Esto no es un problema: es una decisión. Un
vertido en cámara lenta con el sonido del vertido a velocidad normal encima es uno de los recursos que
mejor funcionan.

---

## 3. Qué comida pide cámara lenta y cuál no

### SÍ pide lentitud

| Acción | Duración real | Factor | Por qué funciona |
|---|---|---|---|
| Chorro de cerveza cayendo | 1–2 s | ×4 | La espuma y las burbujas se vuelven visibles |
| Salsa/miel cayendo | 1 s | ×4 | Se lee la viscosidad |
| Lluvia de sal, hierbas, queso rallado | 0,5 s | ×8 | Cada grano brilla y flota |
| Chisporroteo, grasa saltando | 0,3 s | ×8 | Es invisible a velocidad normal |
| Salpicón: hielo cayendo al vaso | 0,4 s | ×8 | El único modo de verlo |
| Hilo de queso estirándose | 1,5 s | ×2–×4 | El hilo tiembla y se ve tenso |
| Vapor subiendo | continuo | ×2 | El ×4 lo vuelve estático y aburrido |

### NO pide lentitud

- **Manos trabajando, cocinando, emplatando.** Ya son lentas. Ralentizarlas mata el reel.
- **Alguien caminando, entrando, sentándose.**
- **Alguien hablando.** Obvio, pero pasa.
- **El plano general del local.** Lento se ve como video de agencia inmobiliaria.
- **El corte del cuchillo.** Ya es un movimiento de 2–3 segundos. Lento se vuelve eterno. La excepción
  es el instante en que la yema o el queso empiezan a salir: eso sí, y solo ese pedacito.
- **La probada.** Alguien masticando en cámara lenta es incómodo, no apetitoso.

**Prueba mental de 3 segundos:** *si cierro los ojos y la acción todavía está pasando cuando los abro,
no era para cámara lenta.*

---

## 4. La rampa de velocidad: el recurso que sí eleva

Lo que se ve profesional casi nunca es "todo lento". Es **normal → lento → normal**, con el lento
puesto exactamente sobre el momento clave.

Estructura de un vertido de cerveza de 5 segundos en pantalla:

```
0,0 - 1,2 s   VELOCIDAD NORMAL   la mano entra con el vaso, lo pone
1,2 - 3,8 s   AL 25%             el chorro cae y la espuma sube
3,8 - 5,0 s   VELOCIDAD NORMAL   la mano levanta el vaso y sale
```

El contraste es lo que hace el efecto. Si todo va lento, no hay nada con qué comparar y el cerebro deja
de registrar que está lento.

**En CapCut:** es la herramienta **Velocidad → Curva**, con el preajuste "Montaña" o una curva hecha a
mano. Ver `214`. La clave es que los puntos de cambio caigan sobre fotogramas donde no hay movimiento
brusco, para que no se note el salto.

**Regla de la rampa:** que el cambio de velocidad no dure más de **0,3 segundos**. Rampas largas se
sienten como que se trabó el video.

---

## 5. Acelerar: el otro lado que casi no se usa

La comida también pide **rapidez**, y ahí hay contenido que casi nadie de tu competencia hace:

| Uso | Factor | Duración final |
|---|---|---|
| Preparación completa de un plato | ×8 a ×20 | 4–8 s |
| Montaje de la barra antes de abrir | ×20 a ×40 | 4–6 s |
| El local llenándose (time-lapse) | ×60 a ×200 | 5–8 s |
| El antes/después de limpiar y montar | ×15 | 3–5 s |

**Cómo se graba un time-lapse del local llenándose:** celular en trípode o pegado a una repisa alta, en
modo time-lapse, sin tocarlo, 40–60 minutos. Es el plano más barato que existe: cuesta cero atención
tuya mientras trabajas. Y comunica algo que ninguna otra toma comunica: **que el sitio se llena**.

**Cuidado real:** hay gente en el cuadro. Antes de publicar un time-lapse con clientes reconocibles,
mira `356` y `319`.

---

## 6. Los comandos (ffmpeg), verificados

**Convertir material grabado a 120 fps en cámara lenta ×4 a 30 fps:**

```bash
ffmpeg -i entrada_120fps.mp4 -vf "setpts=4*PTS" -r 30 -an salida_lenta.mp4
```

Verificado: 2 s de 120 fps → **8,0 s exactos** a 30 fps, con los 240 fotogramas conservados.
`-an` quita el audio (que en modo lento no sirve). El multiplicador de `setpts` es el factor: `2*PTS`
para ×2, `8*PTS` para ×8.

**Si tu celular ya guardó el archivo "conformado"** (o sea, ya se ve lento al abrirlo), no hagas nada:
el trabajo ya está hecho. iPhone guarda el slo-mo con la lentitud aplicada; muchos Android guardan el
archivo a 120 fps "crudo" y hay que ralentizarlo tú. Compruébalo:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 video.mp4
```

Si dice `120/1` o `240/1` → está crudo, ralentízalo. Si dice `30/1` y ya se ve lento → ya está listo.

**Cámara lenta falsa (inventando fotogramas) — el último recurso:**

```bash
ffmpeg -i normal_30fps.mp4 \
  -vf "minterpolate=fps=120:mi_mode=mci:mc_mode=aobmc:vsbmc=1,setpts=4*PTS" \
  -r 30 -an lenta_falsa.mp4
```

**Honestidad sobre esto:** funciona, pero inventa imágenes. En un chorro de cerveza o en salpicaduras
—que es justo donde querrías usarlo— produce deformaciones raras en los bordes del líquido. Además es
lento de procesar y en la prueba perdió algunos fotogramas en los extremos (de 1 s salieron 3,77 s en
vez de 4,0 s). Sirve para movimientos simples y grandes; no sirve para salpicaduras. **Preferible
siempre grabar en alta velocidad de verdad.**

---

## 7. Cómo se ve el ritmo del reel completo

La cámara lenta también es una decisión de **montaje**, no solo de plano. En un reel de 20 segundos:

```
Maximo 2 planos lentos en todo el reel.
Ninguno de mas de 3 segundos.
Nunca dos planos lentos seguidos.
El primero, despues del segundo 4 (nunca en el gancho).
```

**Por qué nunca en el gancho:** los primeros 2 segundos deciden si alguien se queda (`140`, `243`). La
cámara lenta arranca despacio por definición. El gancho tiene que ser rápido, y lo lento es el premio
que viene después.

**Por qué no dos seguidos:** el efecto vive del contraste con lo normal. Dos lentos pegados anulan el
contraste y el video se siente pesado.

---

## Errores comunes

1. **Cámara lenta a todo.** El error #1. Un reel entero lento se siente como si se hubiera trabado.
2. **Ralentizar una acción que ya dura 3 segundos.** 12 segundos de nada en pantalla.
3. **Grabar a 240 fps de noche en el bar.** Un cuarto de la luz: ruido, colores sucios, plano perdido.
4. **Poner el plano lento en el gancho.** El video arranca sin energía y la gente salta.
5. **Dos planos lentos seguidos.** Se pierde el contraste que hace el efecto.
6. **No revisar el parpadeo a 120/240 fps** bajo los LED del bar. Bandas horizontales garantizadas.
7. **Olvidar que el audio del plano lento no sirve.** El plano queda mudo y el reel se cae de golpe.
8. **Rampas de velocidad largas.** Más de 0,3 s de transición y parece que se trabó.
9. **Poner los puntos de la rampa sobre un movimiento brusco.** El cambio se nota.
10. **Ralentizar en post un video de 30 fps y creer que es lo mismo** que grabar a 120: se repiten
    fotogramas y salta. Y **usar `minterpolate` sobre líquidos**, que deforma justo donde se ve.
11. **Grabar a 120 fps y no comprobar si el archivo ya venía conformado.** Terminas ralentizando algo
    que ya estaba lento y queda a ×16.
12. **Time-lapse del local sin pensar en la gente que sale en él** (`356`, `319`).
13. **Acelerar la preparación tanto que ya no se entiende qué pasa.** Por encima de ×25 el ojo pierde
    el hilo.

---

## Checklist

- [ ] Cada plano lento corresponde a una acción que dura **menos de 1 segundo** en la vida real.
- [ ] Ningún plano lento pasa de **3 segundos** en pantalla.
- [ ] Hay **máximo 2 planos lentos** en el reel, y **no van seguidos**.
- [ ] **Ningún plano lento en los primeros 3 segundos.**
- [ ] Se eligió el factor a propósito: **×2 / ×4 / ×8**, no "el que traía el celular".
- [ ] Si es de noche, se grabó a **120 fps máximo** (no 240) o se ralentizó desde 30 fps.
- [ ] Los planos lentos importantes se grabaron **con luz de ventana**, no con la luz del bar.
- [ ] Se revisó que **no haya bandas** (parpadeo) en el material a alta velocidad.
- [ ] Anti-parpadeo del celular en **60 Hz**.
- [ ] Todos los planos lentos tienen **sonido puesto aparte** (`346`).
- [ ] Se comprobó con `ffprobe` si el archivo venía **crudo a 120/240** o **ya conformado**.
- [ ] Las rampas de velocidad duran **menos de 0,3 s** y caen en momentos sin movimiento brusco.
- [ ] Si se usó `minterpolate`, **no fue sobre líquidos**.
- [ ] Si hay time-lapse con clientes, se revisó `356` y `319` antes de publicar.
