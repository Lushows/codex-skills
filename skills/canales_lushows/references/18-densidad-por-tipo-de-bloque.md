# 18 · Densidad por tipo de bloque

**Qué resuelve:** aplicar la misma densidad a todo el episodio. El gancho se queda
corto y el explicativo se atropella, aunque la media global salga correcta.

---

## La tabla de referencia

| Bloque | Eventos/min | Intervalo | Simultaneidad | Duración media | Por qué |
|---|---|---|---|---|---|
| **Gancho** (0-15 s) | 50-60 | 1,0-1,2 s | 2,5-3,5 | 1,2-1,8 s | Hay que ganar la atención antes de que decidan irse |
| **Desarrollo** | 40-48 | 1,25-1,5 s | 2,0-3,0 | 1,6-2,2 s | Ritmo de crucero: el que sostiene el episodio |
| **Explicativo** | 35-42 | 1,4-1,7 s | 1,8-2,5 | 2,2-3,0 s | Una comparación de cifras necesita tiempo para entenderse |
| **Remate** | 30-38 | 1,6-2,0 s | 1,5-2,2 | 2,0-2,8 s | La revelación pide aire; acelerar aquí la desactiva |

**El intervalo es lo que se manipula**, no la duración de los elementos: se acelera
separando menos las entradas, no acortando las vidas (`15`).

Fíjate en que la duración media **sube** cuando la densidad baja. Son magnitudes
independientes: en el gancho hay muchos elementos cortos que se pisan; en el remate,
pocos elementos largos que también se pisan. Lo que cambia es cada cuánto entra uno.

## Cómo se reconoce cada bloque

| Bloque | Señal en el guion |
|---|---|
| Gancho | Los primeros 15 s, hasta la frase que plantea la pregunta del episodio |
| Desarrollo | Narración de hechos: "construyó", "montó", "durante tres años" |
| Explicativo | Aparecen cifras que hay que comparar, mecanismos, "cómo funcionaba" |
| Remate | La frase que da la vuelta al caso y el cierre |

Un episodio de 8 minutos no tiene un bloque de cada: tiene un gancho, cuatro o cinco
alternancias desarrollo/explicativo y un remate. **Alternar es parte del ritmo:** dos
explicativos seguidos hunden el episodio aunque cada uno esté bien montado.

## Cuántos elementos hay que declarar

Los eventos de un bloque son entradas + cortes de escena + salidas visibles. Despejando:

```
n_elementos ≈ D * (objetivo / 60) - cortes - salidas_visibles
```

Con `salidas_visibles ≈ 0,4 × n_elementos` (proporción medida en el piloto: 17 de 30),
queda una regla práctica:

```
n_elementos ≈ (D * objetivo / 60 - cortes) / 1,4
```

| Bloque | Duración | Objetivo | Cortes | Elementos a declarar |
|---|---|---|---|---|
| Gancho | 15 s | 55 | 2 | **(15·55/60 − 2)/1,4 = 8** |
| Desarrollo | 40 s | 44 | 5 | **(40·44/60 − 5)/1,4 = 17** |
| Explicativo | 25 s | 38 | 3 | **(25·38/60 − 3)/1,4 = 9** |
| Remate | 20 s | 34 | 2 | **(20·34/60 − 2)/1,4 = 7** |

Esto se calcula **antes** de escribir la tabla de eventos. Sirve para saber cuánto
material hay que preparar: si el gancho pide 8 elementos y sólo hay 4 recortes, el
problema se resuelve en la fase de material (fase 5), no montando.

## Qué compone la densidad en cada bloque

| Bloque | Reparto de elementos |
|---|---|
| **Gancho** | 3-4 acentos cortos, 2 principales de 1,5 s, 1 suelo, cortes cada 3-4 s |
| **Desarrollo** | 1 principal por idea + su rótulo + 1 apoyo, relevo continuo (`14`) |
| **Explicativo** | 1 principal largo (documento o diagrama) + cifras troceadas encima (`13`) |
| **Remate** | 1 principal, 1 rótulo, escalada de 3-4 acentos y frenada (`15`) |

En el explicativo la densidad **no** viene de cambiar de imagen: viene de que la imagen
que ya está en pantalla se va completando con datos. Cambiar de plano mientras se
explica una cifra es la forma más rápida de que no se entienda.

## Auditar por bloque, no sólo global

La tabla por escena de `auditar.py` (`17`) da eventos/min de cada escena. Se compara
contra la fila que le toca a esa escena por su tipo, no contra los 44 globales. En el
piloto, `titulares` marca 72,8 ev/min — correcto para un gancho, demasiado para lo que
es: un remate. Y `moto`, con 44,1, sería aceptable en desarrollo si no tuviera 4,58 s
de hueco dentro.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Misma densidad en todo el episodio | El gancho no engancha y el remate no remata |
| Gancho por debajo de 45 ev/min | Se pierde al espectador en los primeros 10 s y no vuelve |
| Explicativo a ritmo de desarrollo | La comparación de cifras no se entiende y el dato se pierde |
| Dos bloques explicativos seguidos | El episodio se hunde a la mitad |
| Contar elementos sin descontar cortes y salidas | Se declara un 40% más de material del necesario |
| Medir el bloque contra la media global | Una escena de remate a 72 ev/min pasa el auditor y falla en pantalla |

## Relacionado

`10` densidad de eventos · `15` rampa de ritmo · `16` el plano de descanso ·
`17` medir el montaje · `19` errores de ritmo · `93` estructura de episodio
