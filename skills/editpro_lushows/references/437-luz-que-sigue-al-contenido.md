# 437 — Luz que sigue al contenido

> Un destello colocado "a los 4,2 segundos" es un efecto. El mismo destello colocado "sobre la palabra
> *aprendiz*" es montaje. La diferencia no se ve en el resultado: se ve cuando cambias el guion y uno se
> recoloca solo y el otro se queda donde estaba.

Este módulo es sobre **anclar** la luz: a una palabra, a un acento musical o a un sujeto que se mueve.
El criterio de si ese destello merece existir está en `430`; la forma de su curva, en `431`.

---

## 1. Los tres anclajes, por orden de utilidad

| Anclaje | A qué se pega | Cuándo |
|---|---|---|
| **A la palabra** | marca de tiempo de una palabra de la locución | pieza hablada: documental, explicativo, anuncio con voz |
| **Al acento musical** | el golpe de la pista | pieza sin voz o con música que manda (`24`) |
| **Al sujeto** | una posición en el cuadro que se mueve | luz práctica que pasa, un reflejo que recorre (`264`) |

El primero es el que más rinde y el que casi nadie usa, porque exige tener la transcripción con
tiempos. Conseguirla cuesta un comando (`124`).

---

## 2. Anclar a una palabra: cómo se resuelve

El patrón, tal y como funciona en el motor documental, tiene cuatro pasos y los cuatro tienen su trampa:

```python
anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", d["ancla"]).lower()      # 1. normalizar
cand = [p for p in palabras if p["limpia"] == anc
        and t0 - 0.6 <= p["t"] <= t1]                              # 2. buscar EN SU BLOQUE
if not cand:
    print(f"  ! destello sin ancla en {esc['id']}: '{d['ancla']}'") # 3. avisar
    continue
td = cand[0]["t"] - t0 + d.get("offset", 0)                        # 4. relativo + ajuste
```

1. **Normalizar sin comerse las tildes.** `[^\w]` en Python 3 con `re.UNICODE` ya conserva acentos, pero
   la clase explícita de vocales acentuadas evita sorpresas si alguien cambia la expresión. *"broma,"* y
   *"Broma"* tienen que resolver a lo mismo.
2. **Buscar sólo dentro del bloque**, con un margen de 0,6 s hacia atrás. Si buscas en todo el episodio,
   *papel* aparece cinco veces y el destello se va al primer *papel*, que está en otro bloque.
3. **Avisar cuando no aparece** — y ver §5, porque este aviso se pierde.
4. **Convertir a tiempo relativo al plano**, porque el filtro se aplica a un clip que empieza en cero.

---

## 3. El desfase medido: la luz llega un fotograma antes

La marca de tiempo señala el **inicio** de la palabra. Los destellos del piloto documental no se colocan
ahí: todos llevan un adelanto.

| Episodio | Palabra | Offset declarado | En fotogramas a 25 fps |
|---|---|---|---|
| lustig | hombre, broma | −0,04 s | 1 fotograma |
| lustig | aprendiz, Eiffel, consta | −0,05 s | 1,25 fotogramas |
| ep 01 | papel, fachada | −0,03 s | 0,75 fotogramas |
| ep 01 | millones, toneladas | −0,04 s | 1 fotograma |
| ep 01 | chapo, pescado | −0,05 s | 1,25 fotogramas |

**Diez de once destellos caen entre −0,03 y −0,05 s: siempre dentro de un fotograma de adelanto.** Es la
misma cifra que gobierna el sonido (`433`), y encaja: el impacto va 10–30 ms antes de la luz, y la luz va
30–50 ms antes del inicio de la palabra. Primero se oye, luego se ve, luego se dice.

**Cómo afinarlo en tu material en vez de copiar el número:** renderiza tres versiones con offset −0,08,
−0,04 y 0,00, mídelas (`432`), y mira las tres seguidas con auriculares. Si el destello se siente
"tarde", el ancla está bien y el offset es corto. Si se siente desconectado, sobra adelanto.

---

## 4. Qué palabra se ancla

No cualquiera. Tres reglas que salen de mirar las once anclas reales:

- **Sustantivo concreto o cifra**, nunca un verbo ni una preposición: *millones*, *toneladas*, *papel*,
  *fachada*, *aprendiz*, *Eiffel*, *pescado*. Se anclan cosas que se pueden ver.
- **La última palabra de peso de la frase**, no la primera. El destello cierra, no abre.
- **Una sola vez por idea.** Si el bloque dice *papel* tres veces, se ancla la tercera — la que remata —
  y las otras dos se dejan a oscuras.

---

## 5. El fallo que se cuela: el ancla que ya no existe

Cambias una palabra del guion, regeneras la locución, y el destello **desaparece**. El motor imprime un
aviso y sigue; el render termina bien, el vídeo dura lo mismo y nadie lo nota. Es el hermano pequeño del
`eval=frame` olvidado (`431`).

La comprobación, que cuesta dos líneas y hay que dejar puesta:

```bash
# cuántos destellos se declararon frente a cuántos avisaron de que no encontraron su ancla
python motor.py 2>&1 | tee render.log
grep -c "destello sin ancla" render.log        # tiene que dar 0
```

Y la comprobación independiente, que es la buena porque no se fía del propio motor: contar los picos de
luminancia del render y compararlos con la tabla de destellos declarados (`432`). Si declaraste seis y
el vídeo tiene cinco picos, falta uno.

---

## 6. Anclar al sujeto: la luz que recorre

Cuando la luz tiene que moverse con algo del cuadro — un reflejo que pasa, un foco que barre — el
anclaje ya no es temporal sino espacial, y se hace con la posición como expresión de `t`:

```bash
ffmpeg -y -i plano.mp4 -f lavfi -i "color=c=0xFFE7B8:s=1080x1920" -filter_complex "\
[1:v]format=rgba,geq=a='190*exp(-pow((X-(-300+1500*T))/220\,2))':r='r(X,Y)':g='g(X,Y)':b='b(X,Y)'[luz];\
[0:v][luz]blend=all_mode=screen:all_opacity=0.35:shortest=1[o]" \
  -map "[o]" -c:v libx264 -crf 18 -pix_fmt yuv420p barrido.mp4
```

Una banda gaussiana vertical cuyo centro va de −300 a 1200 px en un segundo. **`geq` usa `T` mayúscula**
para el tiempo y `X`/`Y` para la posición, al revés que `enable`, que usa `t` minúscula (`53`). Y `geq`
es lentísimo: si la banda no cambia de forma, genera la rampa una vez como PNG y muévela con `overlay`.

---

## Errores frecuentes

- **Colocar el destello por segundo y no por palabra.** Al primer cambio de guion queda huérfano.
- **Buscar el ancla en todo el episodio.** Se va a la primera aparición, que suele estar en otro bloque.
  Busca dentro de la ventana del bloque.
- **Anclar un verbo o una muletilla.** No se puede ver un verbo. Sustantivos concretos y cifras.
- **Anclar la primera palabra de la frase.** El destello es punto, no mayúscula.
- **Offset positivo.** Pone la luz después del ataque de la sílaba y se siente tarde. El rango que
  funciona es de −0,03 a −0,05 s.
- **Adelantar más de un fotograma.** Ya no acompaña a la palabra: la anuncia y se desconecta.
- **Ignorar el aviso de "ancla no encontrada".** Es la vía principal por la que un destello desaparece
  sin que nadie se entere.
- **Usar `t` minúscula en `geq`.** Ahí la variable de tiempo es `T`; en `enable` es `t`.
- **Renderizar `geq` sobre vídeo completo.** Minutos por plano. Genera el PNG una vez y desplázalo.

---

## Relacionado

- `430` — qué palabra merece un destello.
- `431`, `432` — la campana y su medición.
- `433` — el sonido, que va 10–30 ms antes que la luz.
- `124` — transcripción y timecodes con IA: de dónde salen las marcas de tiempo por palabra.
- `24`, `374` — anclar al acento musical y al contratiempo del texto.
- `264` — tracking y seguimiento, cuando la luz sigue a algo que se mueve de verdad.
- `canales_lushows` `123-musica-anclada-a-palabra.md` y `241-resolucion-de-anclas.md` — el resolvedor de
  anclas completo del motor documental, con sus casos límite.
