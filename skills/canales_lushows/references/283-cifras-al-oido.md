# 283 · Cifras al oído

**Qué resuelve:** este es un canal de dinero: las cifras son el producto. Y hay una regla
del canal que a todo el mundo le parece un capricho hasta que la oye fallar: **en el
guion, los números se escriben en letra**. En pantalla van en dígitos. Son dos columnas
distintas, para dos sentidos distintos, y no se mezclan.

```
   guion.md, lo que dice la voz        tabla de pantalla, lo que se ve
   ─────────────────────────────       ──────────────────────────────
   «El once de marzo de mil            11 de marzo de 1947
    novecientos cuarenta y siete»
   «Preso cinco mil novecientos        «Robert V. Miller», preso #5954-H
    cincuenta y cuatro, hache»
```

Está así en `piloto/ep01-lustig/guion.md`: el bloque de locución en letra, la tabla «Los
datos de este minuto» en dígitos. **El oído se queda con la magnitud, el ojo con la
precisión.** Es un reparto, no una repetición (§ `44`).

---

## Por qué no se le puede dejar la cifra a la voz

Porque no la lee: la **trocea**. `edge-tts` expone su segmentación en los eventos
`WordBoundary`, y ahí se ve exactamente qué unidades pronuncia:

```python
import asyncio, edge_tts
async def tokens(t):
    com = edge_tts.Communicate(t, "es-MX-JorgeNeural", rate="-6%", pitch="-2Hz",
                               boundary="WordBoundary")
    async for ch in com.stream():
        if ch["type"] == "WordBoundary":
            print("%6.2f  %5.2f  %r" % (ch["offset"]/1e7, ch["duration"]/1e7, ch["text"]))
asyncio.run(tokens("1.437.892 dólares."))
```

Lo que devuelve, medido:

| Escrito | Cómo lo trocea | Veredicto |
|---|---|---|
| `1.437.892 dólares` | `1` · `.` · `437` · `.` · `892` · `dólares` | 🔴 **El separador de miles es un token propio.** Lee los puntos |
| `$2.5B` | `$2` · `.` · `5B` | 🔴 Tres trozos, con el punto dicho |
| `27,4%` | `27` · `,` · `4` · `%` | 🟡 Sobrevive, pero la coma se pronuncia y cuesta 0,29 s |
| `12.600 millones` | un solo token de 2,34 s | 🟢 Éste sí lo resuelve entero |
| `11/03/1947` | un solo token de 2,77 s | 🟡 Lo resuelve, pero no se sabe **cómo** sin escucharlo |
| `3(a)` | `3` · `a` | 🟡 Los paréntesis desaparecen: dice «tres a» |

El criterio no es «los dígitos son malos»: es que **el motor es inconsistente**.
`12.600` lo entiende y `1.437.892` no, con el mismo separador. Un guion que depende de
eso es un guion que depende de la suerte.

## El caso del número de preso, medido

| Escrito | Duración total | Lo que sabemos |
|---|---|---|
| `Preso 5954-H.` | **3,72 s** — un solo token de 2,37 s | |
| `Preso cinco mil novecientos cincuenta y cuatro, hache.` | **4,13 s** — 8 tokens, 2,75 s de habla | |

La forma en dígitos es **0,38 s más corta** que el cardinal completo. Eso basta para
saber que **no está diciendo el cardinal completo**: no le cabe. Dirá «cincuenta y nueve
cincuenta y cuatro», o los dígitos sueltos, o cualquier otra cosa — y lo que diga, dirá
algo distinto de lo que pone el certificado. Por eso en el guion está escrito en letra.

> **Lo que la duración no puede decidir.** Que una forma dure lo mismo que otra no prueba
> que diga lo mismo (`11/03/1947` y su versión en letra duran 4,03 s las dos). La
> duración descarta; **confirmar exige escuchar**. Es la única parte de este bloque que
> no se puede automatizar.

## Y además, en letra se retiene

No es sólo un problema de pronunciación. Es el mismo motivo de § `95`: el oído no puede
releer.

| Escrito para la voz | Duración | Qué se retiene |
|---|---|---|
| `1.437.892 dólares` | 5,54 s | Nada. Y encima suena a error |
| «casi un millón y medio de dólares» | **3,12 s** | La magnitud |
| `27,4%` | 3,12 s | «veintisiete coma cuatro» |
| «algo más de la cuarta parte» | **2,69 s** | La proporción |
| `$2.5B` | 2,86 s | Nada |
| «dos mil quinientos millones de dólares» | 3,41 s | La escala |

La versión redondeada es **más corta y más clara** en los tres casos de comparación
directa. El guion no pierde nada por redondear: el dato exacto está en pantalla, con su
fuente.

## Las reglas del canal

1. **Todo número que diga la voz, en letra.** Fechas, cantidades, expedientes, casillas.
2. **Redondear en la voz; el exacto en pantalla.** «casi un millón y medio» + `1.437.892`
   en el rótulo, con la fuente debajo.
3. **Una cifra por frase.** Dos se anulan.
4. **Cada cifra, anclada** a algo conocido inmediatamente después: ciento veintiséis
   toneladas, tres camiones, vez y media el Everest.
5. **Unidades siempre**: dólares de qué año, por año o en total.
6. **Por encima del 100%, en veces**: «tres veces más», no «un trescientos por ciento».
7. **Los identificadores se deletrean con palabra**: «cinco mil novecientos cincuenta y
   cuatro, **hache**» — la letra suelta se convierte en su nombre.

## La comprobación antes de aprobar la voz

```python
import re, io
texto = io.open("piloto/ep01-lustig/guion.txt", encoding="utf-8").read()
sospechosos = re.findall(r"[\$€]?\d[\d.,/%-]*[A-Za-z%]?", texto)
print(sospechosos)      # sobre el guion del piloto → []
```

Una lista vacía es la condición para pasar a la fase 3. Cualquier cosa que salga ahí es
una cifra que va a locutar el motor a su manera.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dejar `1.437.892` en el texto de la locución | Lee los puntos: «uno punto cuatrocientos treinta y siete punto…» |
| Dejar `$2.5B` | Lo parte en tres y dice el punto |
| Fiarse de que «con `12.600` funcionó» | El motor es inconsistente: con otro número no funciona |
| Dar por buena una cifra porque la duración cuadra | La duración descarta, no confirma. Hay que escucharla |
| Repetir en la voz la cifra exacta que ya está en pantalla | Se desperdicia el reparto: la voz debe dar la magnitud |
| Dos cifras en la misma frase | Se anulan y no se retiene ninguna |
| Escribir la letra de un expediente suelta (`H`) | La deletrea o la ignora: se escribe «hache» |
| Cambiar una cifra del guion después de la fase 3 | Cambia la duración y con ella todos los tiempos (§ `284`) |

## Relacionado

`44` la cifra en pantalla · `95` escribir para el oído · `280` escribir para una voz
sintética · `36` contadores y cifras animadas · `27` composición de datos ·
`96` verificación de datos
