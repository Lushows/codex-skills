# 296 · El recorte que no se usa

**Qué resuelve:** la mitad del banco de un episodio no llega a pantalla, y el primer
impulso al verlo es recortar la curación para dejar de «malgastar» trabajo. Es
exactamente al revés. El banco sobrante **es la herramienta**: cuando a mitad de montaje
falta algo, la diferencia entre un episodio que se sostiene y uno que repite imágenes está
en tener treinta y seis piezas limpias esperando.

`191` fija el cupo por escenario y qué hacer cuando un escenario no lo llena. `253` es la
ventana antirrepetición y por qué falla en silencio. `252` es la rotación de alternativas.
Aquí: **el embudo completo con sus números de hoy**, y la regla de qué se hace cuando algo
falta.

---

## El embudo, medido en `ep01-lustig`

| Etapa | Piezas | Se cae |
|---|---|---|
| Candidatos del sondeo (`sondeo.json`) | **988** | |
| Fuentes curadas y descargadas (`fuentes.json`) | **80** | −92 % |
| Recortes generados (`recortes/*.png`) | **69** | −14 % |
| **Recortes que llegan a pantalla** | **33** | **−52 %** |

**48 % de aprovechamiento del banco.** Los 36 que se quedan fuera no son un error: son
`a_bordo`, `automovil_1927`, `bono_20000`, `bono_50000`, `cartel_fbi`, `celda_alcatraz`,
`certificado_defuncion`, `concorde_1922`, `moneda_confiscada`, `opera_1920s`,
`panorama_paris_1926`, `patio_alcatraz`, `perfil_lustig`, `plano_ciudad`, `plano_metro`,
`presos_grabado`, `torre_aerea`, `torre_citroen`, `torre_dirigible`, `torre_hoy`,
`vapor_arabia` y quince más.

Mírala dos veces, esa lista. No es material flojo: hay dos bonos, un cartel del FBI, un
certificado, cuatro vistas distintas de la torre. Es material **bueno que no le tocó el
turno**, porque el guion de este episodio duró 63 s y habló de lo que habló.

## De dónde sale cada caída

- **988 → 80.** Es la curación por escenario (`190`, `191`): se busca por escenario, se
  clasifica el resultado (`175`), se descarta lo que parece libre y no lo es (`185`) y se
  llena el cupo. El 92 % que se cae son duplicados, resoluciones insuficientes, licencias
  que no aguantan y material que ilustra otra cosa.
- **80 → 69.** Once fuentes no sobreviven al recorte: silueta que falla y no mejora al
  caer a tijera, ancho útil por debajo del mínimo (`194`), alfa que no se puede limpiar
  (`196`). Esta caída sí es pérdida, y es la que conviene bajar.
- **69 → 33.** El diccionario asigna imagen a palabra (`250`). Si la palabra no aparece en
  el guion, la pieza no entra. `certificado_defuncion` es el ejemplo perfecto: la voz dice
  «en el certificado pone que se llamaba Robert Miller», y lo que entra en pantalla no es
  el certificado entero sino `casilla_nombre`, el recorte de la casilla. El documento
  completo se queda en el banco, correctamente.

## Lo que sí es un número de calidad

```
Repeticion: 59 gestos · 53 recursos distintos · 1,11 usos por recurso  (objetivo <= 1,25)
motivos declarados (vuelven a proposito): linea, m_consta, m_cuenta
sin repeticiones: ningun recurso sale de mas ni vuelve demasiado pronto
```

Contados directamente sobre la tabla de escenas: **59 gestos sobre 56 recursos**, y solo
tres se repiten —`m_consta`, `m_cuenta` y `sello_consta`—, los tres declarados como
motivos (`254`), es decir, vuelven porque tienen que volver: son la marca de «esto sí
consta» que estructura el episodio.

*Ninguno de los 33 recortes de archivo aparece dos veces.* Con 36 piezas en reserva, no
hizo falta.

> La auditoría agrupa por `familia()` y funde usos separados por menos de `GESTO`
> segundos, así que su cuenta de recursos distintos (53) es algo menor que la cuenta
> directa (56). Es la cifra buena para el objetivo de 1,25; para saber cuántas piezas
> distintas hay en pantalla, la directa.

## La regla: primero el banco, repetir es el último recurso

Cuando el montaje deja un hueco, el orden no se negocia:

1. **Una pieza del banco que no haya salido.** Treinta y seis esperando.
2. **Una alternativa declarada del mismo concepto** (`252`), que para eso está la lista.
3. **Bajar la densidad**: dejar el hueco es legítimo si el cuadro respira (`28`).
4. **Repetir**, y solo si han pasado 25 s.

Ese último paso está en el código y no es una recomendación:

```python
recurso = max(libres, key=lambda r: _ultima(r, a))    # el que lleva mas sin salir
if _ultima(recurso, a) < 25.0:
    return None      # repetir para tapar un hueco es peor que el hueco
```

**Devolver `None` es una decisión, no un fallo.** El sistema prefiere un cuadro con un
elemento menos a un cuadro con la misma balanza por cuarta vez, que es exactamente el
defecto que `253` cuenta: el informe decía «sin repeticiones» mientras en pantalla salía
cuatro veces lo mismo.

## Cuándo el banco sobrante sí es un problema

No siempre es sano. Dos señales:

- **Un escenario entero sin usar.** Si de los catorce de `torre` entran dos, o el guion no
  habla de la torre —y entonces el cupo estaba mal puesto— o el vocabulario no tiene las
  palabras que activan esas piezas (`257`). Lo segundo se arregla en media hora y cambia
  el episodio.
- **Piezas sin ninguna palabra que las llame.** Un recorte que no está en `vocabulario.py`
  no puede entrar jamás, por mucho que exista. Comprobarlo es una línea:

```python
sin_llamada = {r for r in banco} - {r for v in V.values()
                                    for r in (v[0] if isinstance(v[0], list) else [v[0]])}
```

El material que sobra porque el guion no lo pidió es reserva. El que sobra porque nadie
puede pedirlo es trabajo perdido.

## El banco no caduca

Los 36 recortes de `ep01-lustig` están limpios, virados a la paleta del canal, con su
margen de papel y su entrada en el manifiesto (`199`). El siguiente episodio de París, o
de una cárcel federal, o de una estafa con papeles, arranca con 36 piezas hechas. El
aprovechamiento real del sondeo no es el 48 % de este episodio: es el acumulado del canal,
y sube con cada entrega.

Por eso los alias son estables (`192`) y por eso el manifiesto guarda la URL: una pieza sin
procedencia no se puede reutilizar, porque no se puede defender.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Bajar el cupo del sondeo «porque sobra material» | El primer hueco del montaje se tapa repitiendo |
| Medir el aprovechamiento por episodio | El banco es del canal, no del episodio |
| Confundir reserva con desperdicio | Las 36 piezas son lo que evita la repetición |
| Dejar piezas fuera del vocabulario | No pueden entrar nunca: eso sí es trabajo perdido |
| Repetir para tapar un hueco antes de 25 s | El espectador lo ve antes que cualquier métrica (`253`) |
| Leer «sin repeticiones» sin mirar un fotograma | El informe puede decirlo mientras la pantalla lo desmiente |
| No registrar la procedencia de lo que no se usó | Una pieza sin manifiesto no se reutiliza (`199`) |
| Tomar la cuenta de la auditoría como piezas en pantalla | Funde gestos por familia: 53 frente a 56 |

## Relacionado

`190` curar por escenario · `191` el cupo por escenario · `192` alias estables ·
`175` clasificar el resultado · `194` el ancho útil · `199` el manifiesto del material ·
`250` palabra a imagen: el método · `252` alternativas y rotación ·
`253` la ventana antirrepetición · `254` motivos: lo que vuelve a propósito ·
`257` vocabulario por episodio · `299` cuándo una foto no aporta
