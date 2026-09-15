# 169 · El informe de auditoría

**Qué resuelve:** que una revisión sirva para algo. Un informe que dice *«el episodio se
ve flojo y hay problemas de contraste»* no se puede accionar. Uno que dice **qué, dónde,
cómo se reprodujo, qué le hace al vídeo y cuál es el arreglo** se despacha en una tarde.

---

## La anatomía de un hallazgo

Cinco campos. Faltando uno, el hallazgo vuelve al que lo escribió.

| Campo | Qué es | Si falta |
|---|---|---|
| **Hallazgo** | Una frase. Qué está mal, no qué se siente | Se discute la impresión en vez del hecho |
| **Dónde** | `archivo:línea` para código; `segundo` o `fotograma` para vídeo | Hay que buscarlo, y buscar cuesta más que arreglar |
| **Reproducción** | El comando exacto y su salida pegada | No se puede comprobar que el arreglo funcionó (`168`) |
| **Consecuencia** | Qué ve o deja de ver el espectador | Sin esto no se puede priorizar |
| **Arreglo** | El cambio concreto, con el valor nuevo | «Habría que revisarlo» no es un arreglo |

## La gravedad, y por qué ordena el informe

**El informe se ordena por gravedad, no por el orden en que se encontraron las cosas.**
Quien lo lee arregla de arriba abajo y para cuando se le acaba el tiempo; si el orden es
cronológico, lo que se queda sin arreglar es aleatorio.

| Nivel | Criterio | Ejemplo real |
|---|---|---|
| 🔴 **Llega al vídeo** | El espectador lo ve o lo oye | Tres gráficos con rótulos de 16 px en pantalla: ilegibles |
| 🟠 **Falsea una medida** | La auditoría da por bueno algo que no lo es | El auditor no ve los recursos `.jpg`: no suman superficie ni solapes (`167`) |
| 🟡 **Cuesta tiempo** | No llega al vídeo, pero obliga a rehacer | Un render que muere a los 12 min por un recurso que no existe |
| ⚪ **Nota** | Observación sin consecuencia medida hoy | Tres siluetas con ratio de borde blando 0,06-0,10 |

Dentro de cada nivel, primero lo que se arregla con un número y después lo que exige
rehacer material: el orden en que se pueden ir tachando.

## La plantilla

```markdown
# Auditoría · ep01-lustig · minuto 1 · 11-sep

Versión medida: salida/ep01-lustig-min1.mp4 (63,45 s · 25 fps · 55,7 MB)
Grilla: salida/_grid_v9.png

## Cuadro de mando
| medida            | valor      | meta      |    |
|-------------------|-----------:|-----------|----|
| eventos/min       |       47,9 | >= 44     | OK |
| simultaneidad     |       2,04 | >= 2,0    | OK |
| huecos >= 0,40 s  |          0 | 0         | OK |
| cobertura media   |        31% | 30-45%    | OK |
| integrado         | -14,1 LUFS | -14 +-1   | OK |
| pico real         |  -1,4 dBFS | <= -1,5   | OK |
| recorrido LRA     |     2,0 LU | 4-9       | CORREGIR |

## 🔴 Llega al vídeo
### 1. Los rótulos de los tres gráficos son ilegibles
- **Dónde:** `texto_lustig.py:118` (balanza_01..05); se ve en t=56,2 / 58,6 / 60,3
- **Reproducción:** `python legible.py ep01-lustig` →
  `balanza_03  font 19px  PNG 760  mostrado 656  -> 16,4 px  cap 9,4 px  ILEGIBLE`
- **Consecuencia:** el gráfico ocupa 900 px de ancho durante 2,4 s y no comunica nada.
  En móvil (`166`) es una mancha gris
- **Arreglo:** subir el rótulo de 19 a 34 px en el HTML y regenerar los cinco PNG

## 🟠 Falsea una medida
### 2. El auditor no ve los recursos que no son .png
...
```

## El cuadro de mando va primero

Antes de cualquier hallazgo, la tabla de medidas con su meta y su veredicto. Cumple tres
funciones: sitúa al lector, deja constancia de **sobre qué archivo** se midió, y permite
comparar con la auditoría anterior sin releer nada. Si el informe no dice qué archivo
midió, dentro de tres días nadie sabrá si el arreglo entró.

## Lo que NO va en el informe

| Fuera | Por qué |
|---|---|
| Impresiones sin número | «Se ve apagado» no es accionable. Con `SATAVG 5,4` ya se sabe qué palanca tocar |
| Hallazgos sin reproducir | Es lo que manda a cambiar de herramienta por un fallo de método (`168`) |
| Propuestas de refactor | Un informe de calidad del episodio no es una revisión de arquitectura |
| Cosas que ya se arreglaron mientras se escribía | Van al historial, no a la lista de pendientes |
| Un hallazgo repetido en cinco sitios, cinco veces | Es **uno** con cinco ocurrencias listadas |
| Listas de 40 puntos ⚪ | Ahogan los 🔴. Si hay más de tres notas, se resumen en una línea |

## El cierre

Dos líneas y son obligatorias:

```
VEREDICTO: 2 hallazgos 🔴 pendientes -> NO publicar
SIGUIENTE: arreglar 1 y 2, regenerar PNG, render, grilla nueva (_grid_v10) y
           volver a pasar legible.py y auditar.py
```

Un informe que no termina en *publicar / no publicar* deja la decisión al que lo lee, que
es precisamente quien pidió la auditoría para no tener que tomarla a ojo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Ordenar por orden de descubrimiento | Lo que se queda sin arreglar es aleatorio |
| Mezclar 🔴 y ⚪ en una lista plana | Nadie distingue lo urgente; se arregla lo fácil |
| Omitir el archivo y la versión medidos | No se puede comparar con la siguiente auditoría |
| Escribir el arreglo como «revisar» o «mejorar» | Vuelve al auditor con una pregunta |
| Un informe sin veredicto | Se publica igual |
| Guardar el informe y no la grilla | Dentro de un mes no hay forma de ver lo que se vio |
| Contar el mismo defecto como cinco hallazgos | Infla la gravedad y descoloca la prioridad |

## Relacionado

`168` reproducir antes de afirmar · `167` verificación cruzada · `160` la grilla de
fotogramas · `148` el cuadro de mando del episodio · `17` medir el montaje ·
`86` medir el audio
