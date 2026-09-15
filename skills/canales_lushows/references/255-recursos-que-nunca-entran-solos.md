# 255 · Recursos que nunca entran solos

**Qué resuelve:** el cajón del contrapeso. Cuando un plano se queda con un único elemento
vivo, media pantalla queda desierta, y eso **no se arregla moviendo el elemento** —se
probó y solo cambia de lado el hueco—: se arregla poniendo algo enfrente. Este módulo va
de qué se pone, de dónde sale y de cuántas piezas hacen falta para que el cajón no se
vacíe a mitad de episodio.

---

## El cajón, por bloque

```python
CONTRAPESO = {
    "muerte": ["reloj_1947", "huella_expediente", "sin_padre",
               "presos_grabado", "agente_archivador"],
    "oficio": ["ficha_identidades", "columna_doble", "huella_expediente",
               "cartel_fbi", "imprenta_sellos"],
    ...
}
```

Cinco piezas por bloque, y ninguna elegida al azar: un relleno que no significa nada es
ruido y el espectador lo nota aunque no sepa decir por qué.

| Pieza | Por qué está en su bloque |
|---|---|
| `reloj_1947` | la hora que consta en el certificado (20:30) |
| `huella_expediente` | la carpeta de expediente, con las diez casillas vacías |
| `sin_padre` | la casilla 12: «No data» donde debería ir el padre |
| `ficha_identidades` | seis fichas, cinco con interrogante y una con el 5954-H |
| `columna_doble` | el documento a dos columnas: la forma del método |
| `mapa_ruta` | Hostinne · París · Nueva York · Alcatraz · Springfield |
| `titular_prensa` | la portada de Paper Empires, que no imita a ningún diario |

Detrás de esas figuras van piezas de archivo **del propio bloque** —`cartel_fbi`,
`bajo_la_torre`, `guardia_boveda`—: material real ya curado que no se usa en ningún otro
sitio del episodio.

## Cuántas hacen falta: el fondo del cajón se agota

El contrapeso elige con la misma regla que todo lo demás, la más olvidada, y respeta la
misma ventana de 25 s:

```python
recurso = max(libres, key=lambda r: _ultima(r, a))
if _ultima(recurso, a) < 25.0:
    return None      # repetir para tapar un hueco es peor que el hueco
```

Con tres piezas por bloque, esa línea se dispara casi siempre. Medido sobre
`ep01-lustig`:

| Cajón | Intentos | Devuelven `None` por cajón agotado | Contrapesos colocados | Tramos sin tapar |
|---|---|---|---|---|
| 3 por bloque | 17 | **11 (65%)** | 6 | **8** |
| 5 por bloque | 18 | 2 (11%) | **14** | 2 |

Y lo que eso hace al episodio entero:

| Cajón | Elem | ev/min | Simult | Cobertura | Cuadro casi vacío | Huecos |
|---|---|---|---|---|---|---|
| 3 por bloque | 53 | 54,8 | 1,85 | 34,3% | **6,05 s** | **3** |
| 5 por bloque | **61** | **62,4** | **2,02** | **38,0%** | 2,40 s | **0** |

Ocho elementos y tres huecos de diferencia por dos piezas más en cada lista. El cajón es
la pieza más barata de todo el sistema y la que más rinde.

## La salida NO es bajar la ventana

Es la reacción natural —«si no puedo repetir, no tapo el hueco»— y está medida en `253`:
con la ventana a 12 s vuelven tres repeticiones visibles. La escalera correcta, en orden:

1. **Mirar el banco.** En `ep01-lustig` hay 70 recortes y el montaje usa 36: hay **34 sin
   tocar**, más 79 fuentes en `archivo/` sin recortar (`259`).
2. **Ampliar el cajón del bloque** con piezas de ese bloque que signifiquen algo.
3. **Despiezar** una fuente ya curada en dos elementos distintos (`191`).
4. **Escribir el plano a mano**, si el hueco es del remate y merece una decisión humana.

## Trece tramos escorados y cuatro vueltas

El defecto no se detecta una vez: el propio contrapeso, al colocarse a la derecha, se
convierte en el único elemento del plano y abre un hueco nuevo a la izquierda.

```python
for _vuelta in range(4):
    nuevos = [e for e in (colocar(a, b) for a, b in tramos_malos()) if e]
    if not nuevos:
        break
    fuera.extend(nuevos)
```

Medido: 13 tramos escorados en la primera vuelta, 18 vistos en total, 14 tapados, 2 que
se quedan sin tapar. Con una sola vuelta se colocan 12 contrapesos; con dos, 14; de ahí
en adelante no cambia nada. Las cuatro del código son margen barato para un episodio más
denso, no un bucle que se vaya a agotar.

## El tramo vacío no espera lo mismo que el escorado

```python
def contrapeso(palabras, elementos, ini, fin, pool, ancho=820,
               minimo=0.9, paso=0.1, holgura=0.30):
    ...
    VACIO = 0.35     # un cuadro VACIO no admite el mismo umbral que uno escorado
```

Un cuadro con algo, pero todo a un lado, tolera 0,9 s. Un cuadro **vacío** no: a partir de
0,35 s el espectador lo registra. Dos umbrales, porque son dos defectos distintos con el
mismo remedio.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cajón de tres piezas | 65% de los intentos vuelven vacíos y 3 huecos en el episodio |
| Rellenar con una pieza genérica | Ruido: el espectador nota que no significa nada |
| Usar en el cajón material que ya sale por diccionario | Repetición contra la que no protege ninguna lista |
| Bajar la ventana para que el cajón dé de sí | Vuelven las repeticiones visibles (`253`) |
| Una sola vuelta de contrapeso | Dos tramos menos tapados: el relleno abre su propio hueco |
| Mismo umbral para el cuadro vacío y el escorado | O no se rellena nunca, o se rellena de más |
| Mover el elemento en vez de poner otro enfrente | El hueco cambia de lado y sigue ahí |

## Relacionado

`259` · `250` · `253` · `191` · `11` · `12` · `21`
