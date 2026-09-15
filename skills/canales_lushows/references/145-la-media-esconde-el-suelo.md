# 145 · La media esconde el suelo

**Qué resuelve:** cobertura media en objetivo y medio episodio pelado. Un promedio
describe el episodio que nadie ve; lo que se ve son los momentos malos.

---

## Por qué la media miente aquí

La cobertura media es una integral: dos láminas grandes de 4 segundos levantan el
promedio del episodio entero. El espectador no integra — **se aburre en el tramo malo y
se va**.

Un caso aritmético del canal, 60 segundos:

| Tramo | Duración | Cobertura | Aporte a la media |
|---|---|---|---|
| Dos láminas a página completa | 8 s | 62 % | 8,3 pp |
| Resto del episodio | 52 s | 21 % | 18,2 pp |
| **Media** | 60 s | **26,5 %** | dentro del objetivo 22–38 % |

Aprobado, y 52 segundos por debajo del suelo. El promedio dio permiso.

## La medida correcta: el suelo, no la media

Lo que hay que subir es el **mínimo sostenido**. El auditor no se queda en el promedio:
cuenta los segundos por debajo del suelo y **lista los tramos, con su pico**.

```python
pobres = sum(1 for c in cob if c < 0.14) * paso        # total en segundos

flojos, ini = [], None
for i, c in enumerate(cob):
    if c < 0.14 and ini is None:
        ini = i * paso
    elif c >= 0.14 and ini is not None:
        if i * paso - ini >= 0.8:                      # menos de 0,8 s no se percibe
            flojos.append((ini, i * paso))
        ini = None
if ini is not None and T - ini >= 0.8:
    flojos.append((ini, T))
```

Y al imprimirlos, cada tramo lleva **su máximo** y las palabras que se oyen encima:

```python
for a, b in flojos:
    e = next((x["id"] for x in ESCENAS if x["ini"] <= a < x["fin"]), "?")
    pals = " ".join(p["limpia"] for p in PAL if a <= p["t"] < b)[:46]
    pico = max(cob[int(a/paso):max(int(a/paso)+1, int(b/paso))]) * 100
    print(f"   {a:6.2f} - {b:6.2f}  ({b-a:4.2f} s)  {e:9s} max {pico:4.1f}%  \"{pals}\"")
```

## Por qué el pico, y no sólo la duración

El pico dice **qué tipo de arreglo hace falta**, y ahorra la vuelta en falso:

| Pico del tramo | Diagnóstico | Arreglo |
|---|---|---|
| 1–4 % | Ahí no hay nada, sólo un rótulo suelto | Escena sin guion visual: se rehace |
| 5–9 % | Hay material pero diminuto | Ampliar `w` del principal |
| 10–13 % | Falta una capa | Lámina de fondo o un segundo recorte |

Sin el pico, los tres casos se leen igual en el informe y hay que ir a mirar la tabla
elemento por elemento.

## Las palabras del tramo

Imprimir la locución que suena encima (`pals`) convierte el aviso en una instrucción.
`22.4 - 24.8 max 8.1% "aprendiz de vendedor no se llamaba miller"` dice a la vez dónde
está el problema y **qué imagen falta**: ahí hace falta el nombre, el documento, la
cara. Un aviso con sólo el segundo obliga a abrir el guion; con la frase, se arregla
desde el informe.

## Umbrales del suelo

| Parámetro | Valor | Motivo |
|---|---|---|
| Suelo de cobertura | 14 % del lienzo | Debajo el recorte "flota" sobre el fondo |
| Duración mínima del tramo | 0,8 s | Un bajón más corto es un relevo, no un agujero |
| Objetivo | 0 tramos | Si aparece uno solo, se arregla ese |

Regla de lectura: **media + suelo, siempre juntos.** Media alta y suelo malo es reparto
desigual (este módulo). Media baja y suelo bueno es un episodio uniformemente escaso
(se sube todo, `144`). Media alta y suelo bueno con el cuadro feo es reparto espacial,
no cantidad (`148`).

## La misma trampa en las otras medidas

No es exclusiva de la cobertura. Cada promedio del informe tiene su lista de tramos al
lado, por el mismo motivo:

| Media | Lo que esconde | Cómo se destapa |
|---|---|---|
| Cobertura media | Tramos con el cuadro casi vacío | Lista de flojos con pico |
| Simultaneidad media 2,15 | Un plano con un solo elemento arrinconado | Cuadro descompensado (`148`) |
| Eventos/min del episodio | Una escena a 41 y otra a 60 | Tabla escena por escena |
| Reparto 3×3 del episodio | Un recuadro muerto en un bloque concreto | Reparto por escena |

Salida real de `ep01-lustig`, donde la tabla por escena delata lo que la media tapa:

```
   muerte     16.15 s  12 elem   48.3 ev/min  simult 2.07  hueco  0.0 s
   nombre     11.53 s   7 elem   41.6 ev/min  simult 1.71  hueco  0.0 s
   torre      15.88 s  15 elem   60.5 ev/min  simult 2.49  hueco  0.6 s
```

Media 49,2 ev/min; la escena `nombre` va a 41,6 con simultaneidad 1,71. Esa es la que
se ve floja, y no aparece en ninguna media.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar el episodio por bueno con la media en rango | Medio episodio por debajo del suelo, aprobado |
| Subir la media metiendo una lámina enorme | El promedio sube, el tramo flojo sigue igual |
| Listar los tramos sin el pico | No se sabe si falta una capa o falta la escena entera |
| Listar el tramo sin la frase | Hay que abrir el guion para saber qué poner |
| Reportar una media sin su desglose por escena | La escena floja se esconde detrás del promedio |

## Relacionado

`18` densidad por tipo de bloque · `19` errores de ritmo · `144` presencia no es
superficie · `146` medir lo que se ve · `148` el cuadro de mando
