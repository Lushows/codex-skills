# El bundle y por qué multiplica

## El hallazgo, sin rodeos

Subir el ticket 57% no sube la utilidad 57%. La **multiplica**. En la corrida verificada de México:

| | Suelto (699 MXN) | Bundle + MSI (1.099 MXN) | Cambio |
|---|---|---|---|
| Ticket | USD 38,20 | USD 60,05 | **+57%** |
| Costo total por pedido | USD 22,92 | USD 29,33 | +28% |
| **Techo de CAC** | **USD 15,28** | **USD 30,73** | **+101%** |
| CAC observado | USD 12,65 | USD 10,54 | −17% |
| **Utilidad por pedido** | **USD 2,63** | **USD 20,18** | **el salto** |
| Holgura | 1,21x (trabajas gratis) | 2,92x (sano) | — |
| ROAS de equilibrio | 2,50 | **1,95** | más fácil |

### Las dos cifras del salto (no las confundas)

Circulan dos números y ambos son correctos, porque miden **comparaciones distintas**:

| Comparación | Utilidad antes | Utilidad después | Salto |
|---|---|---|---|
| **Prepago**: suelto 699 → bundle 1.099 + MSI | USD 2,63 | USD 20,18 | **+667%** |
| **Contraentrega**: 699 confirmado → 1.099 confirmado | USD 4,11 | USD 20,38 | **+396%** |

El caso prepago salta más porque parte de una base peor: a 699 MXN prepago la holgura es de 1,21x,
o sea que estás trabajando casi gratis. La lección es la misma en ambos: **cuanto más apretado está
tu margen, más brutal es el efecto de subir el ticket.**

Verifica siempre con tus propios números en `228`.

## Por qué pasa esto: costos fijos por pedido

Esta es la idea completa, y casi nadie la tiene clara:

```
COSTOS QUE SUBEN CON EL VALOR DEL PEDIDO     COSTOS FIJOS POR PEDIDO
─────────────────────────────────────────    ────────────────────────────────
· costo del producto adicional               · flete al cliente  (USD 8,74)
· comisión de pasarela (% del ticket)        · CAC              (USD ~10,54)
· arancel proporcional                       · costo de atención por pedido
                                             · empaque y manipulación
```

El flete y el CAC **no saben cuánto vale lo que va adentro de la caja**. Cuestan lo mismo si mandas
un producto de USD 10 o un bundle de USD 30. Por eso:

```
Costo marginal del contenido extra:  USD 29,33 − USD 22,92 =  USD  6,41
Ingreso marginal por ese contenido:  USD 60,05 − USD 38,20 =  USD 21,85
Margen marginal del bundle:                                   USD 15,44
```

Cada peso adicional de ticket que cuesta poco **cae casi limpio al techo de CAC**. Ese es todo el
mecanismo. No hay magia.

## La tabla que hay que entender

| Componente (USD) | Suelto | Bundle | ¿Escala con el ticket? |
|---|---|---|---|
| Flete al cliente | 8,74 | 8,74 | **NO** |
| CAC | 12,65 | 10,54 | **NO** (y bajó, porque el bundle convierte mejor) |
| Costo puesto en bodega | 11,61 | 16,22 | sí |
| Pasarela (+MSI en el bundle) | 1,64 | 3,30 | sí |
| Atención por pedido | 0,30 | 0,30 | NO |
| Fallidos prorrateados (`229`) | 0,63 | 0,77 | parcialmente |
| **Total costos por pedido** | **22,92** | **29,33** | |

Dos de los renglones más grandes no se mueven. Ese es el regalo.

## Por qué además baja el CAC

No solo sube el ticket: el bundle **convierte mejor**, porque:

1. La oferta se ve más completa y menos comparable (no hay con qué compararla en un marketplace).
2. Cruza el umbral de MSI en México (+36% de CVR por ~1,5 pp de comisión).
3. El "ahorro vs comprar por separado" es un ancla verificable (`217`).

Menos CAC con más ticket es la combinación que abre la holgura de 1,21x a 2,92x.

## Cómo se arma un bundle que no destruye valor

| Regla | Explicación |
|---|---|
| Cada pieza resuelve el **siguiente** obstáculo | después de usar el núcleo, ¿qué le falta? |
| Cada pieza debe sostener la misma promesa (`215`) | si no, se ve como relleno |
| Peso y volumen bajo | el flete es fijo **hasta cierto peso**; ver `145` |
| Costo marginal bajo | busca 1:3 o mejor entre costo extra e ingreso extra |
| Incluye al menos un digital | costo marginal ~0, valor percibido real |

### Tipos de pieza

| Tipo | Costo extra | Valor percibido | Ejemplo |
|---|---|---|---|
| Más unidades del mismo | medio | medio | "llevas 2, uno para el carro" |
| Accesorio complementario | bajo | alto | estuche, repuestos, base |
| Consumible / repuesto | bajo | alto | filtros, cartuchos, cuchillas |
| Digital (guía, recetario, rutina) | ~0 | medio-alto | PDF, video, plantilla |
| Servicio (soporte, cambio) | bajo si operas bien | alto | WhatsApp 30 días |

### Lo que NO va en un bundle

- Algo pesado que dispare el flete y te coma la ganancia marginal.
- Algo que no tenga nada que ver (se lee como saldo de bodega).
- Algo que el cliente ya tiene (cables, bolsas).
- Algo cuyo costo unitario sea alto y su valor percibido bajo.

## Bundle vs descuento: no son lo mismo

| | Descuento 20% | Bundle que sube ticket 57% |
|---|---|---|
| Ticket | baja | sube |
| Techo de CAC | baja | sube |
| Margen | se destruye | se expande |
| Percepción | producto barato | oferta completa |
| Recuperable | difícil | sí |

Cuando el CPM sube en Q4, el instinto es descontar. Es exactamente lo contrario de lo correcto.
Ver `221` y `238`.

## Verificación antes de lanzar

```
1. Calcula el costo puesto en bodega del bundle completo          (28)
2. Verifica el múltiplo mínimo del país                           (42)
3. Corre el modelo                                                (228)
4. Exige holgura ≥ 2,0x en escenario conservador                  (11)
5. Si no pasa, quita la pieza de peor relación costo/valor y repite
```

## Aplicación México dic-2026

El bundle de ~1.099 MXN no es una decisión de marketing: es la **única** configuración probada que
deja holgura sana con el CPM mexicano (USD 4,50 base, +20-50% en Q4) y el flete de USD 8,74. Con el
producto suelto a 699 MXN, la operación de diciembre trabajaría gratis. Lanzar sin bundle es
lanzar a perder.

## Relacionados
`11` · `28` · `42` · `145` · `210` · `215` · `216` · `217` · `219` · `220` · `221` · `223` · `228` · `229` · `238`
