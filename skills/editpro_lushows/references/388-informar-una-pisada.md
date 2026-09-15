# 388 — Informar una pisada

**Qué resuelve:** un hallazgo que no dice **dónde, a quién y cuánto** no se puede arreglar; y un informe
que lo dice todo pero no ordena por gravedad no se lee entero. Este módulo fija los siete campos de una
pisada reportada, el semáforo que la clasifica y lo que no debe entrar en el informe.

> `98` ya tiene la disciplina de trabajar un reporte —el verificador reporta, el editor decide, y cada
> hallazgo se clasifica en arreglar / intencional / escuchar antes de tocar nada—. Vale igual aquí y no se
> repite. `canales_lushows/169` tiene el informe de auditoría del episodio completo, del que la tabla de
> pisadas es una sección.

---

## 1. Los siete campos

Un hallazgo sin uno de estos siete no sirve para nada:

| Campo | Por qué | Sin él |
|---|---|---|
| **segundo absoluto** | es lo que se busca en la grilla y en la tabla | no se puede ir a mirarlo |
| **bloque / escena** | es la unidad en que se edita | no se sabe qué archivo abrir |
| **el de abajo** | es quien recibe el daño | no se sabe qué se pierde |
| **el de encima** | es lo que hay que mover | se mueve el que no era |
| **cuánto** (tinta, no rectángulo) | es la gravedad real (`381`) | se arregla lo que no pasaba |
| **cuánto tiempo** | multiplica la gravedad (`385`) | una pisada de 0,14 s parece urgente |
| **qué era** (foto / texto / cara) | decide el umbral (`383`) | se aplica la vara equivocada |

Y un octavo campo que no es del hallazgo sino del informe: **la huella del código con el que se midió.**
El guion visual se regenera en cada importación; un censo sin huella es un censo de otro episodio (`384`
§5).

---

## 2. El semáforo

| Nivel | Condición | Qué significa |
|---|---|---|
| 🔴 **ENTERRADO** | tinta > 55% **y** más de 0,6 s | no se renderiza. Compuerta, no aviso (`386`) |
| 🔴 **TEXTO PISADO** | tinta > 5% sobre cifra, rótulo, marca o sello | defecto siempre. No hay criterio que lo salve |
| 🟠 **ZONA PROTEGIDA** | más del 20% del 40% superior de un retrato | la cara, que es el elemento (`382`) |
| 🟠 **SOSTENIDA** | tinta > 18% durante más de 1,2 s | el ojo tiene tiempo de verla |
| 🟡 **MORDISCO** | entre el 2% y el 6% | ni limpio ni apilado: se lee como error de render |
| 🟢 **APILADO** | entre el 8% y el 18% | correcto. Papel sobre papel |
| ⚪ **DECLARADA** | está en `PISADAS_OK` y no pasa su tope | decisión. Se imprime con su motivo (`387`) |

Las franjas verde y amarilla salen de `canales_lushows/26`, que es donde se decidieron; aquí solo se les
pone el medidor delante.

**Lo que hace útil el semáforo es el orden de salida:** primero los rojos, y si hay un rojo el informe
termina ahí. No tiene sentido discutir mordiscos mientras haya un elemento enterrado.

---

## 3. El informe, en el formato de la casa

```
PISADAS · episodio01 · diccionario.py eecfab1c · 2026-09-11
93 parejas simultaneas · 35 con contacto · 7,77 pisada-segundos

🔴 ENTERRADO   (0)
🔴 TEXTO       (0 tras filtro de tinta; 3 candidatas descartadas por medir aire)
🟠 SOSTENIDA   (4)
  18,35 s  peso     fajo                bajo camiones            66,9%  0,84 s  foto
  71,90 s  remate   planta_pescado      bajo planta_pescado      19,5%  3,16 s  foto  [zona 37,1%]
  48,20 s  maquina  prensa_vieja        bajo herramientas        16,5%  2,60 s  foto
  66,30 s  piezas   planta_pescado      bajo planta_pescado2     23,7%  2,60 s  foto
🟡 MORDISCO    (4)
⚪ DECLARADA   (0)

descartadas por tinta (el rectangulo mentia):
  t_ningun  bajo boveda        rect 15,6% -> tinta 0,0%   2,45 s
  usd_11    bajo dinero_real   rect 47,9% -> tinta 4,3%   2,10 s
```

Cuatro cosas que ese formato hace bien:

1. **La huella del código en la cabecera.** Sin ella el informe no es reproducible.
2. **Los totales arriba**, para comparar contra la versión anterior de un vistazo. 7,77 pisada-segundos
   frente a los 3,33 de `ep01-lustig` es toda la conversación.
3. **Las descartadas se imprimen.** Un hallazgo que el filtro de tinta tumba **se enseña**, no se borra: es
   la única forma de auditar el filtro. El día que el filtro empiece a tumbar cosas reales, la lista lo
   canta.
4. **La zona protegida va como anotación**, no como fila aparte. Es la misma pisada vista con otra lupa.

---

## 4. El hallazgo lleva la corrección, no la opinión

| Se escribe | No se escribe |
|---|---|
| «`balanza_05` tapa el 7,0% de `m_cuenta` durante 2,02 s» | «el bloque del método está sucio» |
| «mover `balanza_05` 30 px a la derecha lo deja en 0%» | «habría que recomponer eso» |
| «`planta_pescado` cubre el 37,1% de la zona protegida» | «la cara no se ve bien» |
| «descartada: rect 15,6% → tinta 0,0%» | *(borrarla sin más)* |

La corrección se puede calcular, y eso convierte el informe en una lista de tareas de un minuto:

```python
def empujon(cv, ct):
    """Cuantos pixeles hay que mover el de ABAJO, y en que eje, para salir del solape."""
    dx = min(cv[2], ct[2]) - max(cv[0], ct[0])
    dy = min(cv[3], ct[3]) - max(cv[1], ct[1])
    return ("x", round(dx)) if dx <= dy else ("y", round(dy))
```

Si el empujón es de menos de 40 px, el arreglo es mover. Si pasa de 120 px, el arreglo es otro: acortar la
vida de uno de los dos, o cambiar de banda, o quitar el elemento.

---

## 5. Dónde vive el informe

Al lado del guion visual, no en el chat y no en la cabeza de nadie. Un fichero por versión, con la fecha y
la huella en el nombre, y el anterior sin borrar: la comparación entre dos censos es el dato que dice si el
episodio va a mejor, y ese dato solo existe si el censo viejo sigue ahí (`317`).

En el ciclo completo, el informe de pisadas entra **antes** del render y el de verificación del corte
(`98`) **después**. Son dos informes distintos, contestan preguntas distintas y ninguno sustituye al otro:
uno mira la tabla de eventos, el otro mira el archivo exportado.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Reportar el porcentaje sin la duración | Una pisada de 0,14 s sube a lo alto de la lista |
| Reportar sin decir qué era lo tapado | Se aplica el umbral de la foto a una cifra (`383`) |
| Reportar sin la huella del código | El informe no se puede reproducir: el guion se regenera (`384`) |
| Borrar las descartadas en vez de imprimirlas | No hay forma de auditar el filtro que las descarta |
| Mezclar en una lista los rojos y los mordiscos | Se discute el 3% mientras hay un elemento enterrado |
| Escribir el juicio («queda sucio») en vez del dato | Nadie sabe qué mover ni cuánto |
| No guardar el censo anterior | Se pierde el único número que dice si la versión nueva es mejor |
| Fundir este informe con el de verificación del corte | Uno mira la tabla de eventos, el otro el archivo exportado |

## Relacionado

`384` medir el solape antes de renderizar · `385` la pisada que dura · `386` el elemento enterrado ·
`387` pisar a propósito · `389` errores de medición del solape · `98` verificación del corte ·
`133` verificación automática · `317` gestión de archivos · `canales_lushows/169` el informe de auditoría
