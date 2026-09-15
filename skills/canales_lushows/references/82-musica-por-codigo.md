# 82 · Música por código

**Qué resuelve:** el episodio necesita música y ninguna pista descargada es segura —
Content ID no perdona ni las "libres de derechos" mal licenciadas. La banda se compone
con `sine`, con armonía de verdad, y no puede recibir un reclamo jamás.

---

## Un acorde es una suma de senos

Un `sine` solo es un pitido de examen de oído. Un **acorde con cuerpo** necesita cinco
cosas, y en este orden:

| # | Ingrediente | Cómo | Por qué |
|---|---|---|---|
| 1 | Fundamental | `sine=f=55` | La nota. Manda |
| 2 | Quinta | `sine=f=82.41` a −5 dB | Abre el acorde sin decidir mayor/menor |
| 3 | Tercera | `sine=f=65.41` a −9 dB | Decide el color. Siempre la más floja |
| 4 | **Desafinado** | copia a `f*1.003` a −8 dB | Bate contra el original: eso es "cuerpo" |
| 5 | Aire | `anoisesrc=c=brown:a=0.11,lowpass=f=420` | Le da sitio en el mundo |

Sin el punto 4 el acorde suena a órgano de juguete. El batido entre dos senos separados
un 0,3% es lo que en un instrumento real produce el cuerpo de varias cuerdas.

## Frecuencias de trabajo (registro grave, que es donde vive este canal)

`f = 440 · 2^(n/12)`, con n = semitonos desde La4.

| Nota | Hz | Nota | Hz |
|---|---|---|---|
| La1 | 55,00 | Do2 | 65,41 |
| Re2 | 73,42 | Mi2 | 82,41 |
| Fa2 | 87,31 | Sol2 | 98,00 |
| La2 | 110,00 | Do3 | 130,81 |

Por debajo de 45 Hz un altavoz de móvil no reproduce nada: ahí solo van los **impactos**
(`84`), que se sienten en un buen equipo y no estorban en el malo.

## Construir un acorde

```python
def acorde(raiz, dur, ix=0, tercera_menor=True, nivel=0.30):
    """`ix` da un prefijo ÚNICO a las etiquetas: sin él, dos acordes en el mismo
    filter_complex declaran [c1] dos veces y ffmpeg rechaza el grafo entero."""
    q = raiz * 1.4983                                   # quinta justa (2^(7/12))
    t = raiz * (1.1892 if tercera_menor else 1.2599)    # 3ªm o 3ªM
    p = f"c{ix}"
    return (
        f"sine=f={raiz:.2f}:d={dur:.2f},volume={nivel:.3f}[{p}a];"
        f"sine=f={raiz*1.003:.2f}:d={dur:.2f},volume={nivel*0.40:.3f}[{p}b];"
        f"sine=f={q:.2f}:d={dur:.2f},volume={nivel*0.56:.3f}[{p}c];"
        f"sine=f={t:.2f}:d={dur:.2f},volume={nivel*0.36:.3f}[{p}d];"
        f"anoisesrc=c=brown:a=0.11:d={dur:.2f},lowpass=f=420[{p}e];"
        f"[{p}a][{p}b][{p}c][{p}d][{p}e]amix=inputs=5:normalize=0,"
        f"lowpass=f=1100,tremolo=f=0.14:d=0.28"         # respiración, no vibrato
    )
```

`tremolo=f=0.14` es un latido de siete segundos: no se oye como efecto, se percibe como
que la música está viva. Con `f` por encima de 1 Hz ya suena a truco.

## La tensión no es volumen, es intervalo

| Recurso | Intervalo | Cómo se escribe | Qué produce |
|---|---|---|---|
| Estable | quinta | `f`, `f*1.4983` | Reposo. Es el colchón por defecto |
| Duda | cuarta suspendida | `f`, `f*1.3348` | Ni mayor ni menor: pregunta abierta |
| **Amenaza** | tritono | `f`, `f*1.4142` | El intervalo del peligro |
| **Angustia** | segunda menor | `f`, `f*1.0595` | Roce sucio; usar poco y bajo |
| Alivio | octava | `f`, `f*2` | Se abre. Es la revelación |

Una escena de tensión no se hace subiendo el drone: se hace **añadiendo el tritono a
−10 dB** bajo el acorde que ya estaba. El espectador no sabe qué cambió; solo se pone
nervioso.

## Un tema por escena

| Escena | Armonía | Nivel bajo la voz |
|---|---|---|
| Gancho | Fundamental + quinta, sin tercera | −13 LU |
| Pregunta | Cuarta suspendida | −14 LU |
| Desarrollo | Menor, con latido (`dr_latido`) | −13 LU |
| Antes de la cifra | Se añade el tritono, riser encima (`84`) | −11 LU |
| Revelación | Octava abierta + `aecho` largo | −12 LU |
| Remate | Vuelve a fundamental + quinta, se apaga en 3,2 s | −15 LU |

El recorrido completo es **una sola nota raíz** que no cambia en todo el episodio; lo
que cambia son las voces que se le suman encima. Cambiar de tonalidad a mitad de un
episodio de 90 s se oye como que empezó otro vídeo.

## Encadenar una progresión sin costura

```python
def progresion(raices, paso, solape=1.2):
    """Cada acorde entra antes de que muera el anterior: nunca hay hueco."""
    partes, etiquetas = [], []
    for i, r in enumerate(raices):
        d = paso + solape
        ini = i * paso
        partes.append(
            f"{acorde(r, d, ix=i)},"
            f"afade=t=in:st=0:d={solape:.2f},"
            f"afade=t=out:st={d-solape:.2f}:d={solape:.2f},"
            f"adelay={int(ini*1000)}|{int(ini*1000)}[p{i}]")
        etiquetas.append(f"[p{i}]")
    return ";".join(partes) + ";" + "".join(etiquetas) + \
           f"amix=inputs={len(raices)}:normalize=0:duration=longest[mus]"

# descenso clásico de cuatro acordes, 8 s cada uno
FC = progresion([55.00, 87.31, 65.41, 98.00], paso=8.0)
```

El `solape` es obligatorio: sin él, entre acorde y acorde queda un microsilencio que se
lee exactamente igual que el problema del colchón bajo (`80`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Acorde sin voz desafinada | Suena a órgano barato de sintetizador |
| Cambiar de tonalidad dentro del episodio | Se percibe como que empezó otro vídeo |
| Tritono a nivel audible | Deja de inquietar y molesta: va 10 dB bajo el acorde |
| Notas bajo 45 Hz como música | Inaudibles en móvil; ese registro es solo para impactos |
| `tremolo` por encima de 1 Hz | Suena a efecto, no a respiración |
| Etiquetas fijas en `acorde()` | Dos acordes declaran `[c1]`: ffmpeg rechaza el grafo entero |
| Progresión sin solape | Microsilencio entre acordes, igual de audible que un corte |
| Música que sube en el clímax | El clímax se hace con **silencio** (`84`), no con volumen |

## Relacionado

`80` arquitectura · `81` sintetizar · `84` picos · `85` ducking
