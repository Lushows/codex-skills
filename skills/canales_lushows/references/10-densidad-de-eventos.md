# 10 · Densidad de eventos

**Qué resuelve:** el episodio se siente lento y vacío aunque cada plano por separado
esté bien. La causa casi nunca es el material: es que hay pocos eventos por minuto y
tramos donde no pasa nada.

---

## Qué cuenta como evento

Un **evento visual** es cualquier cambio que el ojo registra:

- un corte de escena
- la entrada de un elemento
- la salida de un elemento que deja hueco
- un cambio de estado (la cifra que pasa de 8.800 a 10.200)

No cuentan: el movimiento continuo del fondo ni la deriva lenta de un recorte. Esos
sostienen la atención, pero no la renuevan.

## Los números

| Eventos/min | Cómo se lee |
|---|---|
| menos de 20 | lento; se siente que "no pasa nada" |
| 25-30 | correcto para narración pausada |
| **30-40** | **el estándar del oficio**: cambio visual cada 1,5-2 s |
| **44-48** | denso, propio de un collage. El objetivo del canal |
| más de 55 | ruido: el ojo no alcanza a leer nada |

**Medición real del episodio 01 (primer intento):** 42 eventos en 80,2 s = **31,4 por
minuto**, con **22 s de hueco (28% del episodio)**. Correcto en el papel, flojo en
pantalla — porque los eventos estaban agrupados y dejaban vacíos.

## La distinción que importa: cortos vs simultáneos

Para subir de 31 a 48 hay dos caminos, y solo uno es bueno:

| Camino | Resultado |
|---|---|
| ❌ Hacer los elementos **más cortos** | Nada se llega a leer. Un retrato de 0,8 s no comunica, molesta |
| ✅ Tener **más elementos vivos a la vez** | El ojo recorre el cuadro y encuentra cosas. Es lo que hace un collage |

**La regla: 2 a 4 elementos vivos en todo momento.** Uno manda (el que sostiene la
frase), los otros acompañan. Cuando el que manda sale, ya hay otro dentro.

## Densidad por tipo de bloque

No todo el episodio va al mismo ritmo:

| Bloque | Eventos/min | Por qué |
|---|---|---|
| **Gancho** (0-15 s) | 50-60 | Hay que ganar la atención; aquí sí se acelera |
| **Desarrollo** | 40-48 | El ritmo de crucero |
| **Explicativo** (datos) | 35-42 | Una comparación necesita tiempo para entenderse |
| **Remate** | 30-38 | Se frena: la revelación necesita aire |

## Cómo se sube la densidad sin ensuciar

1. **Superponer**: mientras el retrato vive 3 s, entran y salen dos datos encima
2. **Trocear un elemento largo**: la cifra en 4 estados en vez de uno fijo
3. **Añadir rótulos**: cada objeto lleva su etiqueta, y la etiqueta es un evento
4. **Micro-elementos**: sellos, marcas, subrayados que entran 0,8 s y salen
5. **Relevo**: un elemento sale empujado por el siguiente, no por desvanecimiento

## Auditoría

`17-medir-el-montaje.md` trae el script. Se ejecuta ANTES de renderizar: la tabla de
eventos ya tiene todos los datos, no hace falta ver el video para saber si está flojo.

```
eventos/min      >= 44
huecos           0 tramos de más de 0,4 s
simultaneidad    media >= 2,0 elementos vivos
duración media   1,6 - 2,4 s por elemento
```

## Relacionado

`11` el hueco prohibido · `12` capas simultáneas · `13` ciclo de vida del elemento ·
`17` medir el montaje · `18` densidad por tipo de bloque
