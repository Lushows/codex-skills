# 387 — Pisar a propósito

**Qué resuelve:** todo el bloque `380`–`386` empuja hacia el mismo sitio: menos pisadas. Y hay pisadas que
son la idea. El problema no es tenerlas, es que **un medidor no distingue una decisión de un descuido**, y
la pisada deliberada que no se declara se convierte, dos versiones después, en un aviso que alguien
«arregla».

> **Qué cuenta cada disposición** —el acta tapando media cara, el retrato tapando el edificio, la cifra por
> delante de quien la movió, entrar por encima vs. entrar por debajo— está en `canales_lushows/26`, y no se
> repite. **La mecánica** de meter un gráfico dentro del plano duplicando el vídeo y enmascarando lo que
> debe pasar por delante está en `204` §3.5. Este módulo es lo que falta entre las dos: **cómo se declara
> para que sobreviva a la medición.**

---

## 1. Declarada, tolerada y colada

| Tipo | Cómo llegó | Qué pasa al volver a medir |
|---|---|---|
| **declarada** | alguien la eligió y la escribió con su motivo | el medidor la salta y el motivo se lee |
| **tolerada** | alguien la vio, decidió que da igual, no la anotó | vuelve a saltar en cada versión hasta que alguien la «arregla» |
| **colada** | nadie la evaluó | se descubre en la grilla, ya renderizada (`386`) |

La diferencia entre declarada y tolerada no es estética: es la que decide si dentro de tres meses el
episodio 07 sigue teniendo esa oclusión o si alguien la quitó pensando que era un fallo.

---

## 2. El precedente: `MOTIVOS`

El sistema ya resuelve este problema exacto para otra cosa. `auditar.py` mide repetición de recursos y
grita cuando algo sale demasiadas veces. Pero hay recursos que **están hechos para volver**: las marcas de
columna, la línea de tiempo que se construye. Se declaran en el guion visual:

```python
# MOTIVOS: recursos que estan hechos para volver. Son la gramatica del episodio
# (las marcas de columna, el logotipo, la linea de tiempo que se construye), no
# falta de material. Se declaran en el guion visual como MOTIVOS.
MOTIVOS = {"m_consta", "m_cuenta", "linea"}
```

Y el auditor los respeta y además **los imprime**: `motivos declarados (vuelven a proposito): linea,
m_consta, m_cuenta`. Eso último es lo importante: la excepción no es invisible, sale en el informe cada vez.

La pisada deliberada se declara igual.

---

## 3. `PISADAS_OK`: la declaración

```python
# Pisadas que son la IDEA, no un defecto. Cada una lleva su motivo, porque dentro
# de tres meses el motivo es lo unico que impide que alguien la "arregle".
PISADAS_OK = {
    ("acta_condena", "retrato_lustig"): {
        "tope": 0.55, "motivo": "la identidad queda enterrada bajo el expediente"},
    ("torre_esquema", "trenes_chatarra"): {
        "tope": 0.30, "motivo": "la chatarra se come el plano: es lo que paso"},
}
```

Tres reglas sobre ese diccionario, y ninguna es negociable:

1. **La clave es el par ordenado (el de abajo, el de encima).** La pisada al revés no está declarada y debe
   seguir saltando: si el orden de capa se invierte por accidente, el sentido se invierte con él.
2. **Lleva tope propio, no un permiso en blanco.** Declarar que el acta tape el retrato no autoriza a que
   lo entierre al 100%: si pasa del `tope` declarado, sigue siendo un hallazgo.
3. **Lleva motivo en texto, y el informe lo imprime.** Una excepción sin motivo es deuda.

En el censo (`384`), una línea:

```python
excepcion = PISADAS_OK.get((bajo, arriba))
if excepcion and v <= excepcion["tope"]:
    declaradas.append((v, bajo, arriba, excepcion["motivo"]))
    continue
```

---

## 4. El agujero real del piloto: la mano contra la mano

Corriendo el censo sobre `ep01-lustig`, sobreviven exactamente dos pisadas sobre texto:

| El de abajo | El de encima | Tapado | Dur | Bloque |
|---|---|---|---|---|
| `m_cuenta` | `balanza_05` | 7,0% | 2,02 s | metodo |
| `m_consta` | `balanza_05` | 5,1% | 2,02 s | metodo |

Las tres piezas —`m_consta`, `m_cuenta` y `balanza_05`— están en la **capa CLAVE**, escritas a mano. Y la
compuerta de `diccionario.generar()` **no las comprueba entre sí**: los elementos escritos a mano entran en
`vivos` como reservados, el generador evita pisarlos, pero nadie comprueba la mano contra la mano.

Por eso son las únicas dos que quedan. No sobrevivieron porque alguien decidiera que la balanza debe tocar
las marcas de columna: sobrevivieron porque **nadie las evaluó nunca**.

> Son pisadas *coladas* que parecen *toleradas*. La salida no es una tercera: o se declaran con su motivo
> —y entonces son una decisión y el informe lo dice— o se arreglan moviendo la balanza treinta píxeles. Lo
> que no vale es dejarlas donde están y llamar a eso criterio.

Y la corrección estructural, que es la que de verdad cierra el agujero: **la compuerta tiene que
comprobarse también dentro de la capa escrita a mano**, no solo entre la mano y lo generado.

---

## 5. El presupuesto de pisadas deliberadas

`204` ya lo dice para la oclusión de composición: **una jugada por vídeo**, en el momento que importa; diez
oclusiones son una tarde perdida. Para el collage documental la cuenta que sostengo, con los números del
piloto, es:

| Alcance | Pisadas declaradas |
|---|---|
| por bloque | **1** como máximo |
| por episodio de un minuto | **2**, y solo si cuentan cosas distintas |
| dentro del mismo gesto | 0 — si dos elementos se apilan a propósito, es **una** decisión, no dos |

La razón es de lectura, no de higiene: la oclusión deliberada significa porque es rara. Si el episodio
tiene cinco, ninguna significa nada y todas se leen como descuido —que es exactamente el estado del que
salió `episodio01`, con 7,77 pisada-segundos y cuatro parejas por encima del 42% (`380` §4).

---

## 6. Lo que no se declara nunca

Aunque venga firmado por quien sea:

- Una **cifra** mientras la voz la dice. Ni una esquina.
- Un **rótulo**: tapado, el objeto se queda sin explicar y pasa a ser ruido.
- El elemento que **sostiene la frase que se está oyendo**.
- Un elemento **al 100%** durante más de medio segundo: eso no es oclusión, es tirar un recurso (`386`).

La lista completa y su razonamiento están en `canales_lushows/26`, sección «Lo que nunca se tapa».

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tolerar una pisada sin declararla | Vuelve a saltar en cada versión hasta que alguien la quita |
| Declararla sin tope | Se autoriza también el enterramiento al 100% |
| Declararla sin motivo escrito | Dentro de tres meses nadie sabe si era una idea o un descuido |
| Declarar el par sin orden | Si la capa se invierte, la oclusión cuenta lo contrario y nadie se entera |
| No comprobar la mano contra la mano | Las únicas pisadas que sobreviven son las que nadie evaluó |
| Cinco oclusiones deliberadas en un minuto | Ninguna significa nada; todas se leen como fallo de montaje |
| Declarar para no arreglar | La declaración es para lo que cuenta algo, no para lo que da pereza mover |

## Relacionado

`380` qué es pisar en números · `383` umbrales por tipo de contenido · `386` el elemento enterrado ·
`388` informar una pisada · `204` §3.5 oclusión como recurso de composición ·
`canales_lushows/26` qué cuenta cada disposición · `canales_lushows/22` profundidad por capas
