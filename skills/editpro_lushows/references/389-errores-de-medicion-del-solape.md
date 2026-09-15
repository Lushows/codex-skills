# 389 — Errores de medición del solape

**Qué resuelve:** un medidor de pisadas equivocado es peor que no tenerlo, porque da permiso. Aquí están
los doce fallos que he encontrado midiendo el motor real, cada uno con el número que lo demuestra. Once son
de modelo —el medidor describe un vídeo que no es el que se va a renderizar— y uno es de proceso.

---

## Familia A · El medidor mide otra cosa

### 1. Ordenar la pareja por tiempo y llamarlo capa

`motor.py` encadena los overlays en el orden de la **lista**; el último va encima. El orden de entrada es
independiente. Medido: **30 de 96** parejas de `ep01-lustig` (31%) y **27 de 93** de `episodio01` (29%)
tienen los dos órdenes cruzados. Un medidor que ordene por reloj calcula, en un tercio de los casos, cuánto
tapa el de abajo al de arriba: un número sin significado. `auditar.py:563` hace exactamente eso y por eso
no reporta nada (`386`).

### 2. Medir el rectángulo y llamarlo contenido

| Caso real | Rectángulo | Tinta |
|---|---|---|
| `t_ningun` bajo `boveda`, 2,45 s | 15,6% | **0,0%** |
| `usd_11` bajo `dinero_real`, 2,10 s | 47,9% | **4,3%** |
| `torre_construccion` bajo `hotel_crillon`, 1,74 s | 18,9% | **36,3%** |

Falla en los dos sentidos y por factores de once y de dos. Una cifra suelta lleva un 11% de tinta y un 43%
de aire transparente; un recorte con silueta tiene la caja medio vacía por las esquinas (`381`).

### 3. Ignorar la rotación

`motor.py` rota cada elemento con `rotate=…:ow=rotw(…):oh=roth(…)`, que **agranda el lienzo del PNG**. La
caja que el medidor calcula es la sin rotar:

| Elemento | Giro | Área real | Desplazamiento del centro |
|---|---|---|---|
| 900×600 (recorte) | 2,4° | **+9,1%** | (12,2 , 18,6) px |
| 1180×340 (cifra) | 3,1° | **+20,3%** | (8,4 , 31,7) px |
| 1280×600 (héroe) | 3,8° | **+17,2%** | (18,5 , 41,8) px |

Una cifra torcida 3,1° ocupa un quinto más de superficie y se dibuja 31,7 px más abajo de donde el medidor
la puso. Un umbral del 5% no sobrevive a un error de 31 px.

### 4. Ignorar la deriva

`deriva` se aplica como `(t - t0) * dx`: es **píxeles por segundo, durante toda la vida**. Con `dx=9` y una
vida de 2,6 s el elemento acaba **23,4 px** a la derecha de donde el medidor lo dejó. Se mide la posición
de reposo y se renderiza una posición que se mueve.

### 5. Ignorar la entrada

Con `entrada: "izq"` el elemento arranca **520 px** a la izquierda y tarda 0,36 s en llegar a su sitio;
con `"abajo"`, 380 px por debajo. Durante esos 0,36 s el elemento **no está donde el medidor lo pone**.
Medido sobre los contactos del censo:

| Episodio | Contacto declarado | Contacto que cae durante una entrada | Pisadas que solo existen durante la entrada |
|---|---|---|---|
| `ep01-lustig` | 35,46 s | **9,74 s (27%)** | **6 de 31** |
| `episodio01` | 40,88 s | **9,95 s (24%)** | **8 de 35** |

Y el detalle que lo remata: la pisada más fuerte de `episodio01` por porcentaje —`fajo` bajo `camiones`,
77,3%— **es una de las fantasma**. Dura 0,14 s y esas catorce centésimas caen enteras dentro de la entrada.

### 6. Contar la vida entera, con los fundidos

Un elemento a medio fundir no está en pantalla. `auditar.py` cuenta presente desde el 35% de opacidad:
entra 0,105 s tarde y se va `0,35 × fade_out` antes. Para un `micro` eso es el **13,8%** de su vida (`385`).
Dos elementos que se rozan una décima puede que no coincidan nunca.

### 7. Asumir que `pisa()` es simétrica

`torre_citroen_noche` y `r_sinfuente` comparten exactamente los mismos píxeles cortados: **11,2%** para el
plano grande, **46,7%** para el rótulo. Normalizar por el grande convierte un rótulo destrozado en un
mordisco. Normalizar con `max()` de los dos sentidos convierte todo roce con una pieza pequeña en alarma.
En el **informe** se normaliza siempre por el que queda debajo; el `max()` solo vale como compuerta de
colocación (`383` §1).

### 8. No fijar el lienzo

Las posiciones son expresiones `W*0,44` / `H*0,36`. Si el medidor asume 1920×1080 y el motor renderiza
otra cosa —o al revés— **todas** las coordenadas salen corridas y el censo entero es ficción. El lienzo se
lee de un sitio, no se escribe en dos.

### 9. Buscar el recurso de otra manera que el motor

En `auditar.py` llegó a haber cuatro copias de «buscar el fichero», y la más estrecha no miraba en
`archivo/` ni aceptaba `.jpg`: devolvía superficie **cero** para recortes que sí salían en pantalla. Una
función, la misma que `motor.buscar()`, o se mide un episodio que no existe.

---

## Familia B · El número está bien y la conclusión está mal

### 10. Promediar las pisadas

La media sube con dos apilados correctos y esconde el enterramiento. Lo que hay que mirar es el **techo** y
la suma de pisada-segundos, nunca la media. Es la misma trampa que el auditor ya documenta para la
cobertura: *«lo que hay que subir es el SUELO, no la media»*, aquí al revés.

### 11. Un umbral único para todo el material

Doce pisadas sobre siete piezas de texto distintas en `ep01-lustig`, y **ninguna llega al 32%**: con la
vara de la foto (42%) no salta ni una (`383`). El factor entre el umbral de una cifra y el de una foto es
de veintiuno.

### 12. Ordenar por porcentaje

Una pisada del 19,6% durante 3,16 s pesa **5,7 veces** más que una del 77,3% durante 0,14 s — y la segunda,
además, es fantasma (error 5). Se ordena por pisada-segundos (`385`).

---

## Familia C · El proceso

### 13. Medir una generación y renderizar otra

El guion visual **se genera en cada importación**. Hoy mismo, con otro proceso tocando `diccionario.py` a
media sesión, el censo de `episodio01` pasó de **87 a 93** parejas simultáneas sin que yo cambiara nada de
lo mío. Un censo sin la huella del código con el que se midió no es reproducible y no se puede comparar con
el anterior (`388` §1).

---

## Errores frecuentes

Tabla de bolsillo. Si el censo da un número raro, se baja por aquí en orden:

| Síntoma | Causa probable | Comprobación |
|---|---|---|
| El censo sale limpio y la grilla no | Pareja ordenada por tiempo | Contar discrepancias capa/tiempo (§1) |
| Alarmas sobre piezas que en pantalla están enteras | Se mide el rectángulo | Medir la tinta de esas tres (§2) |
| Los números bailan entre versiones sin tocar nada | Otra generación del guion | Huella del código en la cabecera (§13) |
| Pisadas de menos de 0,4 s por todas partes | No se descuenta la entrada | 24–27% del contacto es entrada (§5) |
| Todo lo que toca una pieza pequeña sale grave | `max()` de los dos sentidos | Normalizar por el de abajo (§7) |
| El texto nunca salta | Umbral único | Bajar a 0,05 y volver a contar (§11) |
| Un elemento aparece 30 px más abajo que en el censo | Rotación no modelada | Recalcular con `rotw`/`roth` (§3) |
| Un recorte de archivo cuenta como área cero | Segunda función de búsqueda | Unificar con `motor.buscar()` (§9) |
| El episodio mejora en la media y empeora al verlo | Se promedió | Techo + pisada-segundos (§10) |

Y el error que no es de medición y se lleva a todos por delante: **confiar en el número y no mirar la
grilla**. El censo no ve contraste, ni siluetas que se confunden, ni un recorte oscuro sobre fondo oscuro.
Ordena el trabajo; no lo termina (`canales_lushows/160`–`169`).

## Relacionado

`380` qué es pisar en números · `381` el área que importa · `383` umbrales por tipo de contenido ·
`384` medir el solape antes de renderizar · `385` la pisada que dura · `386` el elemento enterrado ·
`388` informar una pisada · `109` ffmpeg trampas y errores ·
`canales_lushows/142` la medida que miente · `canales_lushows/143` la alarma en falso
