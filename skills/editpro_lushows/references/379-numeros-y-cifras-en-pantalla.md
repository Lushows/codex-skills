# 379 — Números y cifras en pantalla: se leen distinto, se tratan distinto

Un número no es una palabra corta. Se procesa por otra vía, se recuerda de otra forma y falla de otra
manera. Por eso en la gramática medida los números llevan **whoosh** y no el mismo golpe que las
palabras: el oído ya sabía, antes que la teoría, que son otra cosa.

`46` cubre cómo se escriben los números en el guion de texto. Este módulo es cómo se **coreografían**.

---

## 1. Tres diferencias que lo cambian todo

**a) Un número no se reconoce por su forma: se lee dígito por dígito.**
`GRATIS` se reconoce de un golpe, como una silueta. `$10.000` obliga a recorrer los caracteres y a
contar posiciones. Consecuencia directa: **un número necesita más tiempo en pantalla que una palabra del
mismo largo.** Regla práctica: **+40% de duración**.

| | Palabra | Número |
|---|---|---|
| Duración mínima | 0,6 s | **0,9 s** |
| Duración cómoda | 1,2 s | **1,7 s** |
| En cascada | puede quedarse 2 s | **mínimo 2,5 s** |

**b) Un número exige precisión.** Una palabra mal leída se recupera por contexto; un número mal leído es
un error de información. `$10.000` leído como `$100.000` no es un matiz: es una venta perdida y un
comentario furioso. Todo el tratamiento tipográfico de los números existe para eliminar esa ambigüedad.

**c) Un número es una promesa verificable.** El espectador puede comprobarlo. Un número redondo y falso
—"ahorra 50%"— destruye más confianza de la que construye. Ver §8.

---

## 2. Cómo se escribe un número en pantalla

Reglas duras, todas por legibilidad:

| Regla | Bien | Mal |
|---|---|---|
| Cifras, nunca letras | `10.000` | `diez mil` |
| Separador de miles siempre (Colombia: punto) | `$10.000` | `$10000` |
| Sin decimales si no aportan | `$10.000` | `$10.000,00` |
| Redondear lo que se puede redondear | `3 MESES` | `2,8 MESES` |
| Símbolo pegado a la cifra | `$10.000` | `$ 10.000` |
| Unidad más pequeña que la cifra | `30`**`min`** | `30 MIN` todo igual |
| Porcentaje con el símbolo, no la palabra | `40%` | `40 POR CIENTO` |
| Los años completos | `2026` | `'26` |

**El separador de miles es el más importante.** Sin él, `10000` obliga a contar ceros —y en un video que
dura 1,5 segundos, nadie cuenta ceros: adivina, y adivina mal. Es la diferencia entre un precio que se
entiende y un precio que se malinterpreta.

### El caso del precio colombiano
`$10.000` tiene 7 caracteres y una particularidad: **el `$` y el `.` no aportan altura**, solo ancho. Si
usas la fórmula de escala por longitud (`378`) sobre 7 caracteres crudos, el número queda un poco más
pequeño de lo que debería. Dos opciones:

- Usa la versión con anchos pesados de `378`, donde `$` pesa 0,95 y `.` pesa 0,4.
- O simplemente sube un 10% la escala de los precios como categoría.

---

## 3. La jerarquía interna de una cifra

Un precio no es un bloque uniforme. Tiene partes con distinta importancia:

```
        SOLO          ← 45% del tamaño, gris o blanco
      $10.000         ← 100%, color de marca
      PAGO ÚNICO      ← 45%, blanco
```

La cifra manda; el contexto la acompaña. Tres niveles, nunca más.

Variantes que funcionan:
- **Símbolo más pequeño que la cifra.** `$` al 70% del tamaño de los dígitos, alineado arriba. Es un
  recurso de diseño editorial clásico y hace que el precio se vea más contundente.
- **Los ceros más finos** —si la fuente tiene versiones de distinto grosor—. Destaca el dígito
  significativo. Solo con fuentes que lo permitan; no fuerces.
- **La rebaja tachada.** `$30.000` tachado en gris arriba, `$10.000` grande abajo. El tachado **entra
  después**: primero se lee el precio alto, y a los 0,4 s aparece la línea. Ese medio segundo es todo el
  efecto.

---

## 4. El sonido: por qué whoosh y no golpe

En la gramática medida, cada palabra que entra lleva un golpe corto (~0,27 s) y **los números llevan
whoosh**. Es la decisión correcta y tiene explicación:

- El **golpe** es percusivo, instantáneo. Marca un evento puntual: una palabra que aterriza.
- El **whoosh** tiene duración y dirección: sube o baja, viene de algún lado. Marca un **desplazamiento o
  una magnitud**, que es exactamente lo que es un número.

Además, en la práctica: los números suelen entrar solos o en pares, no en cascadas de seis. Un whoosh de
0,4 s no cabría en una cascada a 0,18 s de intervalo, pero cabe perfecto para un precio que entra solo.

**Reglas del whoosh:**
- Duración 0,3-0,5 s, con el pico justo **en** el fotograma en que aparece el número, no después.
- Baja el volumen de la música 3-4 dB durante el whoosh (`75`). Si no, el whoosh y la música se pelean y
  el número pierde peso.
- **Un whoosh por número.** Tres números seguidos con tres whooshes suena a videojuego. Para
  enumeraciones de cifras, whoosh solo en el total.

---

## 5. Números que cuentan (el contador animado)

Un número que sube de 0 al valor final es de los pocos movimientos de texto que sobreviven a las modas,
porque **el movimiento significa algo**: representa acumulación.

Reglas:
- **Duración 0,6-1,0 s.** Menos y es un parpadeo; más y el espectador espera con impaciencia.
- **Desacelerar al final.** Rápido al principio, lento al llegar. Un contador lineal se siente mecánico.
- **Ancho fijo.** El problema técnico real: al pasar de `999` a `1.000` el número cambia de ancho y todo
  el bloque salta. Si el texto está centrado, salta hacia los dos lados y se ve fatal.
  **Solución: alinea el contador a la izquierda, o rellena con ceros/espacios para ancho constante.**
- **Solo para cifras que valga la pena ver crecer:** un ahorro acumulado, un total de clientes, una
  pérdida que sube. Nunca para un precio: un precio que sube es exactamente el mensaje contrario al que
  quieres.

**Cuándo no:** si el número es pequeño (`3 PASOS`), contar de 0 a 3 no cuenta nada. El contador se gana
su lugar cuando la cifra es grande.

---

## 6. La cascada de cifras que suma

Formato de altísimo rendimiento para explicar un costo:

```
t=0,00   CARNE           $4.200
t=0,25   PAPA              $800
t=0,50   ACEITE            $350
t=0,75   GAS               $200
t=1,20   ────────────────────────    ← la línea entra sola
t=1,45   TE CUESTA       $5.550      ← más grande, color de marca, whoosh
```

Cuatro detalles que lo hacen funcionar:

1. **Los números alineados a la derecha.** Es la única alineación que permite comparar cifras de un
   vistazo: las unidades quedan una debajo de otra. Los rótulos a la izquierda, los números a la derecha.
2. **Todas las cifras del mismo tamaño**, menos el total. Aquí **no** se aplica escala por longitud: la
   comparación exige tamaño uniforme. Es la excepción a `378`.
3. **La línea de suma entra sola**, con su propio momento. Es el "por lo tanto".
4. **El total lleva whoosh; los sumandos llevan golpe suave.** Distinto sonido = distinta categoría.

Ese bloque dura unos 4 segundos y es probablemente el uso más rentable de texto en pantalla para vender
una calculadora de costos.

---

## 7. Números que no son cifras: fechas, horas, teléfonos

| Tipo | Tratamiento |
|---|---|
| **Teléfono** | Agrupado: `320 866 5248`, nunca corrido. Y en pantalla **más tiempo que nada**: mínimo 3 s |
| **Hora** | `6 PM`, no `18:00`, salvo público técnico |
| **Fecha límite** | Con día de la semana: `HASTA EL VIERNES` funciona mejor que `HASTA EL 31` |
| **Duración** | `2 MIN`, no `120 SEGUNDOS` |
| **Cantidad pequeña** | Del 1 al 9 en cifra igual: `3 PASOS`, no `TRES PASOS`. En video mandan las cifras |

El teléfono merece un párrafo aparte: es el único texto de un video que el espectador **tiene que
transcribir**. Necesita el triple de tiempo, agrupación en bloques de 3, tamaño grande, y —si es
posible— aparecer dos veces. En la práctica, casi siempre es mejor no poner el teléfono y mandar a un
enlace o a un botón, precisamente porque transcribir es una fricción enorme.

---

## 8. La honestidad del número

Un número en pantalla es una afirmación pública. Tres reglas que evitan problemas:

1. **Si no lo puedes sustentar, no lo pongas.** "Ahorra hasta 40%" sin un cálculo detrás es una promesa
   que alguien va a reclamar.
2. **Los números redondos suenan inventados; los específicos suenan reales.** `$10.000` es un precio.
   `1.847 restaurantes` suena a dato; `2.000 restaurantes` suena a estimado.
3. **La palabra "hasta" te salva legalmente y te cuesta credibilidad.** Úsala solo si de verdad hace
   falta.

Y un detalle de plataforma: las cifras de precio en anuncios se revisan. Si en el video dice `$10.000` y
en el chat el precio es otro, eso además de un problema de confianza es un problema de política
publicitaria.

---

## 9. Verificación obligatoria

Los números son lo único del video que hay que **verificar dos veces**, porque el error no se nota al
mirar:

- [ ] Leer el número en voz alta mirando la pantalla.
- [ ] Contarle los ceros. Literalmente.
- [ ] Comprobar que coincide con el precio real que dice el bot, la landing y el anuncio.
- [ ] Comprobar que el separador de miles está.
- [ ] Comprobar que el símbolo de moneda está y es el correcto.

Es la única lista de este bloque que se hace **dos veces**: una al montar y otra antes de exportar.

---

## Errores comunes

1. **Escribir el número en letras.** `diez mil` ocupa más y se lee peor que `$10.000`.
2. **Omitir el separador de miles.** El espectador no cuenta ceros: adivina, y adivina mal.
3. **Darle a un número el mismo tiempo que a una palabra.** Necesita ~40% más.
4. **Decimales innecesarios.** `$10.000,00` alarga y no aporta nada.
5. **Separar el símbolo de la cifra** (`$ 10.000`): parece dos elementos distintos.
6. **Contador centrado sin ancho fijo.** Salta hacia los lados al cambiar de dígitos.
7. **Contador de más de 1 segundo.** El espectador se impacienta esperando el final.
8. **Contador lineal.** Se siente mecánico; hay que desacelerar al llegar.
9. **Animar un precio hacia arriba.** El movimiento dice lo contrario del mensaje.
10. **Whoosh en cada cifra de una enumeración.** Suena a videojuego; whoosh solo en el total.
11. **Cifras de una suma con tamaños distintos.** Rompe la comparación; aquí no aplica la escala por
    longitud.
12. **Sumandos alineados a la izquierda.** Los números se comparan alineados a la derecha.
13. **Teléfono corrido y en pantalla 1,5 s.** Nadie lo alcanza a transcribir.
14. **Números que no se pueden sustentar**, o que no coinciden con el precio real del chat y la landing.

---

## Checklist

- [ ] Todos los números están en cifras, no en letras
- [ ] Separador de miles presente en todas las cantidades de 4+ dígitos
- [ ] Sin decimales, salvo que aporten
- [ ] Símbolo de moneda pegado a la cifra
- [ ] Cada número dura al menos 0,9 s (1,7 s si es el precio principal)
- [ ] El precio tiene tres niveles como máximo (contexto / cifra / condición)
- [ ] Los números llevan whoosh; las palabras llevan golpe
- [ ] La música baja 3-4 dB durante el whoosh
- [ ] Si hay contador: ancho fijo, 0,6-1,0 s, desacelerando al final
- [ ] En sumas: rótulos a la izquierda, cifras alineadas a la derecha, mismo tamaño
- [ ] El total es más grande, de otro color y con otro sonido
- [ ] Si hay teléfono: agrupado en bloques de 3 y mínimo 3 s en pantalla
- [ ] Leí cada número en voz alta y le conté los ceros
- [ ] Verifiqué que las cifras coinciden con el precio real del chat, la landing y el anuncio
