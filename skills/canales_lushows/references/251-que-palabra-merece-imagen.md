# 251 · Qué palabra merece imagen

**Qué resuelve:** qué entra en el vocabulario y qué no. El criterio parece obvio —«lo que
se puede ver»— y no lo es: la trampa no está en las palabras abstractas, que se caen
solas, sino en los recursos que llevan **cifras o texto propios** y que, colgados de una
palabra cualquiera, contradicen a la voz delante del espectador.

---

## El criterio, en una línea

> Entra la palabra que nombra **algo que se puede fotografiar**. «Banco», «camiones»,
> «certificado», «torre». No entran «problema», «cantidad», «situación»: esas van como
> titular, no como imagen.

En la cabecera del banco está escrito así, y se cumple: de las 48 entradas del episodio
01, ninguna es abstracta.

| Clase | Entradas en `V` | Qué nombra |
|---|---|---|
| objeto | 30 | cosas del mundo: una calle, un telegrama, una chatarrería |
| heroe | 12 | lo que la historia mira de frente: el retrato, el certificado, la torre |
| dato | 3 | la cifra compuesta, que va a su banda propia |
| micro | 2 | sellos y marcas |
| rotulo | 1 | la etiqueta que nombra |

48 entradas apuntan a **56 recursos** porque 13 de ellas llevan alternativas (`252`).

## Cuántas palabras del guion merecen imagen, de verdad

| | Minuto 1 de `ep01-lustig` |
|---|---|
| palabras que suenan | 155 (98 distintas) |
| con entrada en `V` | 54 apariciones · 46 palabras distintas |
| proporción | **35% de lo que se dice tiene imagen declarada** |
| llegan a pantalla por diccionario | 27 |

Un tercio del texto con imagen declarada y la mitad de eso en pantalla es el punto de
equilibrio medido: por debajo el cuadro se queda flojo, por encima el generador empieza a
descartar por sitio (15 descartes ya con estos números) y el trabajo de vocabulario se
tira a la basura.

## La regla dura: nada con cifras propias entra por diccionario

```python
# Recursos que NO pueden entrar por diccionario. Llevan CIFRAS O TEXTO propios y,
# colgados de una palabra cualquiera, contradicen a la voz.
NUNCA_AUTO = {"linea_00", "linea_01", "linea_02", "linea_04",
              "linea_05", "linea_06", "d_1890", "torre_esquema"}
```

y en el generador, antes de elegir:

```python
opciones = [o for o in opciones if o not in NUNCA_AUTO]
if not opciones:
    continue
```

El caso que originó la regla: se mapeó `"altura" -> "cotas"`, un dibujo de cotas
genéricas, y en pantalla se leía «1,00 m × 1,00 m» mientras la voz decía «trece mil
setecientos metros». Reproducido hoy sobre el episodio 01, mapeando `"broma" -> "cotas"`:

```
   con la guardia (actual)  elementos 60 · 'cotas' en pantalla: no entra
   sin la guardia           elementos 61 · 'cotas' en pantalla: [('nombre','broma',1.51,721)]
   la voz, en ese segundo (33.06 s): ... durante cien años, es directamente una broma.
```

1,51 segundos de un dibujo que dice «1,00 m» sobre la frase «es directamente una broma».
El espectador no sabrá decir qué le ha chirriado, pero deja de fiarse, y un canal de
documentales vive de que se fíen.

## Cómo se decide, en la práctica

1. **Mírala.** Antes de añadir un recurso al diccionario hay que abrir el fichero. Si
   lleva números, rótulos, fechas o un nombre propio impreso, no entra: va a mano,
   anclado a su dato exacto.
2. **Léela en voz alta con la frase.** «Según todo lo que se ha contado durante cien
   años» + un plano de París de 1926: correcto. + un esquema con cotas: falso.
3. **Pregunta si sobreviviría a otra frase.** Los recursos genéricos (una calle, un
   fajo, una bóveda) sobreviven; los específicos, no. Los específicos son de la mano.
4. **Si la palabra suena una sola vez en todo el episodio, mejor a mano.** El generador
   está para lo que se repite y para lo que no merece una decisión humana.

## Dos entradas que sobran, y cómo se ven

```
entradas de V que NO suenan nunca: ['nombre', 'vendi']
```

`"nombre"` y `"vendi"` están declaradas y no aparecen en `tiempos.json`: son restos de una
versión anterior del guion. No hacen daño, pero mienten sobre el tamaño del vocabulario.
La comprobación cuesta dos líneas y conviene tenerla en el arranque del montaje:

```python
sordas = sorted(set(V) - set(p["limpia"] for p in PALABRAS))
if sordas:
    print("  ! entradas de V que no suenan en el guion:", sordas)
```

## Una palabra, un recurso, un instante

El elemento entra **antes** de su palabra, no encima: `t0 = max(ini, t - 0.16)`. Ciento
sesenta milisegundos. Llegar justo a tiempo es llegar tarde, porque el ojo necesita el
salto para encontrar la figura antes de que el oído reciba el nombre (`39`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Añadir un recurso sin abrirlo | Cifras en pantalla que contradicen a la voz |
| Mapear una palabra abstracta | Imagen decorativa: el espectador nota que no significa nada |
| Meter en `V` un recurso que ya va a mano | Sale dos veces, o se bloquea a sí mismo |
| Vocabulario enorme «por si acaso» | El generador descarta por sitio y el trabajo se pierde |
| Dejar entradas de un guion anterior | El recuento de vocabulario miente |
| Colgar de una palabra un mapa o un plano concreto | El anacronismo y el error geográfico (`198`) |

## Relacionado

`250` · `252` · `257` · `258` · `44` · `48` · `39` · `198`
