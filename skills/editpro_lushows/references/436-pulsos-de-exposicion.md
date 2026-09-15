# 436 — Pulsos de exposición

> El destello dura cinco fotogramas y se ve. El pulso de exposición dura un segundo y medio y **no se
> ve**: se siente. Es el mismo filtro, la misma campana y la misma trampa del `eval=frame`, con el ancho
> multiplicado por diez y la fuerza dividida por cuatro.

`222` trata la exposición como **decisión de rodaje y de grado**: dónde cae la piel, qué se quema, qué se
recupera. Este módulo la trata como **función del tiempo**: la imagen se aclara y se vuelve a oscurecer
sin que nadie se dé cuenta, y eso hace trabajo narrativo.

---

## 1. Para qué sirve

Cuatro usos, y ninguno es "dar ritmo" (eso es la tijera, `27`):

1. **Levantar un bloque.** El gancho respira medio paso por encima del resto de la pieza. El espectador
   no lo ve; lo lee como "esto importa".
2. **Bajar un bloque explicativo.** Lo contrario, y es más útil: el tramo que explica se dice más bajo
   y se ve un poco más apagado. Es la versión visual de la automatización de voz.
3. **Hacer respirar un plano quieto.** Una lámina fija de seis segundos está muerta. Un pulso de ±4
   niveles a lo largo de esos seis segundos la mantiene viva sin moverla.
4. **Cerrar.** La luz que baja en los últimos 1,2 s es el punto final de la pieza.

---

## 2. Las dos formas: campana ancha y trapecio

**Campana ancha** — para un acento que sube y vuelve. Es la de `431` con otros números:

```
eq=brightness='0.055*exp(-pow((t-6.40)/0.55\,2))':contrast='1+0.030*exp(-pow((t-6.40)/0.55\,2))':eval=frame
```

Con `ancho`=0,55 s, la anchura a media altura es 1,665 × 0,55 = **0,92 s** y el pulso es visible durante
3,03 × 0,55 = **1,67 s**. Fíjate en el contraste: aquí va **por debajo** del brillo (×0,55), al revés
que en el destello. Un pulso lento con mucho contraste se ve como un cambio de grado, no como luz.

**Trapecio** — para sostener un bloque entero a otro nivel. Es el patrón de la automatización de voz
del motor documental, aplicado al brillo:

```
eq=brightness='0.04*max(0\,min(1\,min((t-12.10)/0.5\,(19.40-t)/0.5)))':eval=frame
```

Sube en 0,5 s, se queda, baja en 0,5 s. **La rampa de 0,5 s es el número clave**: por debajo de 0,3 s el
cambio de nivel se ve como un salto de edición; por encima de 0,8 s deja de percibirse como intención.

---

## 3. La dosis, medida

El mando es la fuerza, pero **lo que hay que fijar es el Δ de luminancia**, porque el mismo número da
resultados muy distintos según la imagen (§4).

| Δ Y medido | Qué pasa |
|---|---|
| **+2 a +5** | No se ve. Se nota al quitarlo. **Es el rango de trabajo** |
| +6 a +9 | Se empieza a ver si la imagen es lisa; sigue siendo aceptable en un cierre |
| +10 a +14 | Se ve como un cambio de exposición. Ya no es sutil |
| +15 o más | Es un destello lento, y se lee como fallo de cámara |

Y el otro control, que casi nadie mira: **la pendiente**. Por debajo de unos **8 niveles por segundo**
el cambio no se percibe conscientemente. Un pulso de +5 repartido en 1,5 s son 6,7 niveles/s: invisible.
Los mismos +5 en 0,3 s son 33: se ve.

---

## 4. El techo: dónde empiezas a quemar

Aquí está la diferencia grande con el destello: el pulso dura lo bastante como para que **el quemado se
vea**. Medido, aplicando la misma expresión (`fuerza` 0,18) sobre la misma lámina llevada a distintas
exposiciones de partida:

| Base Y | Δ Y en el pico | YMAX base | **YMAX en el pico** |
|---|---|---|---|
| 35,1 | +22,7 | 113 | 154 |
| 51,1 | +26,7 | 128 | 173 |
| 67,1 | +30,6 | 144 | 194 |
| 84,1 | +34,9 | 162 | 216 |
| 104,1 | +40,0 | 182 | 240 |
| 125,1 | +45,2 | 203 | **255 — quemado** |

Dos lecturas:

1. **La misma expresión da +22,7 sobre base oscura y +45,2 sobre base clara.** El doble. La fuerza no
   es una dosis: es un coeficiente. La dosis es el Δ medido.
2. **A partir de `YMAX` ≈ 203 de partida, el pulso llega a 255 y destruye información.** En un destello
   de 5 fotogramas nadie lo nota; en un pulso de 1,5 s se ve una zona blanca plana que aparece y
   desaparece — el efecto más barato del catálogo. **Mide `YMAX`, no sólo `YAVG`** (`432`).

Regla de seguridad: si `YMAX` del plano ya pasa de 230, **no subas: baja**. Un pulso negativo
(`brightness` con signo menos) funciona igual de bien y no tiene techo hasta mucho más abajo.

---

## 5. La trampa del material de 8 bits: el bandeado

Una rampa lenta y suave sobre una pared lisa, un cielo o un fondo degradado produce **bandas**: escalones
de color visibles donde debería haber un degradado. El material de móvil, comprimido y a 8 bits, no
tiene niveles suficientes.

Se detecta mirando el plano al 200 % en las zonas lisas, y se resuelve con un poco de ruido, que es
justo lo que hace el motor documental en su cadena final:

```
eq=contrast=1.06:saturation=1.05:gamma=1.13:brightness=0.032,noise=alls=5:allf=t+u,vignette=PI/6.0
```

`noise=alls=5:allf=t+u` — ruido temporal y uniforme, apenas visible, que rompe las bandas. **El ruido se
pone al final de la cadena, después de la rampa**, o la rampa lo aplasta. Ver `66`.

> Ojo con ese `eq` del ejemplo: no lleva `eval=frame` **y está bien**, porque sus valores son constantes.
> `eval=frame` sólo hace falta cuando hay una expresión con `t` dentro (`431`).

---

## 6. Medirlo

Mismo arnés que `432`, distintas métricas: **Δ Y** (2 a 5 en trabajo normal), **pendiente** (Δ Y entre
el tiempo de subida, por debajo de 8 niveles/s), **`YMAX` en el pico** (por debajo de 250 o estás
quemando) y **bandeado** (inspección a 200 % en zonas lisas).

Y una comprobación que sólo aplica a los pulsos: **exporta la pieza entera y mira la curva de `YAVG`
completa**. Los pulsos se diseñan uno a uno y luego se pisan entre ellos; en la curva global se ve
enseguida si el bloque "bajo" acabó más alto que el "alto".

---

## Errores frecuentes

- **Usar la fuerza como si fuera la dosis.** El mismo 0,18 da +22,7 o +45,2 según la base. Fija el Δ.
- **No mirar `YMAX`.** Sobre base clara el pulso llega a 255 y aparece un parche blanco plano.
- **Rampas de menos de 0,3 s.** Se ven como un salto de edición, no como respiración.
- **Contraste alto en un pulso lento.** Se lee como cambio de grado. Aquí el contraste va por debajo del
  brillo, al contrario que en el destello.
- **Olvidar `eval=frame`** cuando hay expresión con `t`. El pulso no ocurre y no hay aviso (`431`).
- **Ponerlo donde ya hay un destello.** Dos recursos de luz en el mismo sitio se anulan.
- **No añadir ruido sobre material liso.** Bandas en la pared o en el cielo.
- **Poner el ruido antes de la rampa.** La rampa lo aplasta y no sirve de nada.
- **Diseñar los pulsos uno a uno sin mirar la curva completa.** Acaban contradiciéndose entre bloques.

---

## Relacionado

- `222` — exposición y rango dinámico: qué se quema, qué se recupera, dónde cae la piel.
- `431` — la misma campana, diez veces más estrecha.
- `432` — el arnés de medición; aquí se usa con otras métricas.
- `438` — el mismo problema de "la base manda" visto desde la fotosensibilidad.
- `61`, `62` — corrección contra gradación, y emparejar planos: un pulso mal puesto descuadra un
  emparejado bueno.
- `66` — viñeta, nitidez y textura: de dónde sale el ruido que rompe las bandas.
- `canales_lushows` `120-la-curva-de-intensidad.md` — la curva de intensidad por bloques del canal
  documental, que es lo que estos pulsos traducen a luz.
