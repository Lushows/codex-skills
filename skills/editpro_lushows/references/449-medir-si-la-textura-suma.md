# 449 — Medir si la textura suma

Todas las decisiones de los ocho módulos anteriores acaban en la misma pregunta: *¿esto que le he
puesto está mejorando el vídeo o solo me lo está encareciendo?* Este módulo es el protocolo para
contestarla, y empieza por una advertencia: **la métrica que todo el mundo usa para esto no sirve.**

---

## 1. SSIM y VMAF no pueden juzgar textura

`editpro/93` explica bien las tres métricas de calidad y cuándo usarlas. Ninguna de las tres vale
aquí, y la razón es de definición: **miden la diferencia con el original, y la textura *es* una
diferencia con el original que tú has introducido a propósito.**

Medido: cuatro texturas aplicadas al mismo plano de 5 s, comparadas contra el plano limpio.

| textura | SSIM (All) | ¿cuánto se ve? |
|---|---|---|
| halación `sigma=22`, op. 0,35 | **0,9915** | mucho — es el rasgo más visible de los cuatro |
| `noise=alls=5:allf=t+u` | 0,9765 | poco |
| `vignette=PI/5.6` | 0,9658 | poco |
| aberración radial 0,42 % | **0,8952** | **casi nada** |

El orden es **exactamente el inverso del visual**. SSIM declara a la aberración cuatro veces más
dañina que la halación, cuando la aberración es el efecto que nadie nota y la halación el que
transforma el plano. Es el caso de libro de `canales/142`: un número correcto de algo que no es lo
que querías saber.

> **Contra el original, toda textura puntúa mal. Es lo que significa poner textura.** SSIM y VMAF
> solo sirven aquí para una cosa: comparar el **export** contra el **master ya texturado**, que es
> otra pregunta (¿cuánto me destroza la compresión?) y la responde `editpro/93`.

---

## 2. La trampa del `-loglevel` (verificada hoy)

Antes de nada, porque si no, el protocolo entero devuelve silencio. `psnr`, `ssim` y `signalstats`
**imprimen en nivel `info`**. Con `-loglevel error` no sale nada: ni resultado, ni aviso, ni error.

```bash
# ❌ silencio: parece que falló
ffmpeg -loglevel error -i a.mp4 -i b.mp4 -lavfi "[0:v][1:v]ssim" -f null -

# ✅
ffmpeg -hide_banner -loglevel info -i a.mp4 -i b.mp4 -lavfi "[0:v][1:v]ssim" -f null - 2>&1 | grep -i SSIM
```

Y comprueba siempre que la línea que esperas aparece de verdad, en vez de dar por buena una tabla
vacía: es exactamente el «filtro que descarta todo» de `canales/152`.

---

## 3. Las cuatro medidas que sí contestan

Cada una responde una pregunta distinta y ninguna sustituye a las otras.

| # | Pregunta | Medida | Umbral |
|---|---|---|---|
| 1 | ¿el grano está vivo? | σ temporal sobre plano quieto | > 0,3 vivo · < 0,05 muerto |
| 2 | ¿se ve como materia? | suelo de ruido y razón p95/suelo | archivo 10–16 · fondo 2–7 |
| 3 | ¿queda banda? | anchura media del escalón en el degradado | < 3 px |
| 4 | ¿cuánto cuesta? | bytes del export, contra el mismo export sin la textura | el presupuesto que tengas |

```python
# 1. sigma temporal          -> editpro/441 §2 y editpro/446 §1
# 2. suelo y razon           -> editpro/447 §1
# 3. anchura del escalon     -> editpro/440 §2
# 4. bytes                   -> os.path.getsize, sobre el EXPORT, no sobre el master
```

Y la medida del color, que es independiente de las cuatro y ya está resuelta: **dispersión de tono**,
umbral ≤ 0,005, en `canales/197`. No se mide con saturación (no es monótona: 61,1 → 48,0 → 52,5).

---

## 4. El protocolo, en orden

```
1. Exporta el plano SIN la textura, con el CRF real de publicación.
2. Exporta el plano CON la textura, con el MISMO CRF.
3. Mide σ temporal en los dos.  Si la diferencia es < 0,05 -> la textura no llegó. PARA.
4. Mide la anchura del escalón en la zona de degradado de los dos.
5. Mide bytes. Apunta el múltiplo.
6. Decide con la tabla del §5. Y solo entonces mira los dos vídeos.
```

El orden importa. Mirarlos primero contamina: cuando uno acaba de pasar media hora poniendo grano,
lo ve. El paso 3 es el que evita publicar una textura que la compresión borró
(`editpro/446`): si no llegó, los demás pasos sobran.

---

## 5. La tabla de decisión, con lo medido en este bloque

Coste sobre 5 s de collage 1080p (CRF 12 para el tiempo y el peso relativo):

| textura | tiempo | bytes | ¿sobrevive a CRF 24? | veredicto |
|---|---|---|---|---|
| **halación** | ×1,17 | **×1,09** | sí — es baja frecuencia (razonado, no medido aquí) | **casi siempre sí** |
| **sangrado de croma** | ×1,05 | **×0,97** | sí — idem | sí, si la época lo justifica |
| **polvo / arañazo** | despreciable | **×1,00** | **82–89 %, medido** | **sí, es gratis** |
| aberración radial | ×1,15 | ×1,39 | sí, pero se la come el 4:2:0 si < 2 px | según el plano |
| viñeta | ×1,22 | ×1,31 | sí, pero bandea | sí, con grano detrás |
| **grano global** | ×1,62 | **×8,49** | **0,2 % sobre plano · 17 % sobre detalle, medido** | **casi nunca global** |

Las dos filas marcadas «razonado» son las únicas de la tabla que no vienen de una medida: la halación
y el sangrado son desenfoques de radio grande, y lo que la compresión destruye es la alta frecuencia.
Mídelas tú si la decisión depende de ellas.

La lectura práctica en una línea: **lo que cuesta bits no sobrevive, y lo que sobrevive no cuesta
bits.** El grano es la única textura que está en la esquina mala de las dos columnas, y es
precisamente la que todo el mundo pone primero.

---

## 6. Cuándo NO medir

Medir cuesta tiempo y este protocolo son unos veinte minutos por plano en un equipo normal. No lo
apliques a cada plano: aplícalo **una vez por cadena de acabado** y reutiliza la decisión mientras el
material y el destino no cambien. Se vuelve a medir cuando cambia:

- el CRF o el destino de publicación (es la variable que más manda),
- la resolución de export,
- el tipo de material (archivo escaneado / generado / cámara),
- la versión de ffmpeg (los números de este bloque son de una compilación concreta).

Y se mide **siempre** la primera vez que se monta una cadena por canal o por conversión de espacio
de color: la prueba nula de `editpro/443` §3 y `editpro/445` §3 encontró en ambos casos un fallo que
ningún ojo detecta.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Usar SSIM o VMAF para juzgar textura | Puntúa al revés: 0,8952 a lo invisible, 0,9915 a lo evidente |
| `-loglevel error` al medir | Silencio absoluto; se da por buena una tabla vacía |
| Medir sobre el master en vez de sobre el export | El master conserva el 95 % del grano y el export el 4 % |
| Medir σ temporal sobre material con movimiento | El movimiento genera varianza y tapa el resultado |
| Una sola medida | Cada una contesta una pregunta distinta; ninguna vale por las otras |
| Mirar los vídeos antes de medir | Ya has decidido; los números solo confirmarán lo que quieres |
| Medir el color con saturación | No es monótona (`canales/197`) |
| Volver a medir cada plano | Se mide la cadena, no el plano |
| No volver a medir al cambiar el CRF de publicación | Es la variable que más cambia el resultado |
| Aceptar un número sin comprobar que la línea salió | `canales/152`: el filtro que descarta todo |

---

## Relacionado

`editpro/93` compresión sin perder calidad (PSNR, SSIM, VMAF y para qué sirven de verdad) ·
`editpro/440` la anchura del escalón · `editpro/441` la σ temporal · `editpro/446` supervivencia a la
compresión · `editpro/447` suelo de ruido y razón p95/suelo · `editpro/448` textura por capa ·
`editpro/133` verificación automática · `canales/142` la medida que miente · `canales/152` filtros que
descartan todo · `canales/197` dispersión de tono · `canales/140` medir antes de renderizar ·
`canales/147` cuando una métrica deja de servir
