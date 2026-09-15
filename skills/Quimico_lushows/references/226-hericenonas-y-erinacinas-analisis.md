# 226 — Hericenonas y erinacinas: cómo se analizan (y por qué casi nadie lo hace)

Estos dos nombres aparecen en todas las etiquetas de melena de león y casi nunca en un informe de
laboratorio. La razón es concreta: son familias con muchos miembros, patrones de referencia escasos, y hasta
hace muy poco no había un método que las midiera todas juntas. Este módulo te da el estado del arte a agosto
de 2026 para que sepas qué pedir, qué esperar y cuándo simplemente **no declararlas**.

Términos: **hericenona (hericenone)** = meroterpenoide aromático del cuerpo fructífero de *Hericium
erinaceus*; se numeran (hericenona C, D, E...). **erinacina (erinacine)** = diterpenoide de tipo ciatano del
micelio, con letras (erinacina A, B, C...), frecuentemente como xilósido. **hericeno (hericene)** = serie
aromática relacionada. **UHPLC-UV** = cromatografía líquida de ultra alta resolución con detección
ultravioleta. **meroterpenoide (meroterpenoid)** = molécula híbrida, parte terpénica y parte de otra ruta.

## Dónde vive cada una

| Familia | Tejido | Nota analítica |
|---|---|---|
| Hericenonas y hericenos | Cuerpo fructífero | Aromáticas, absorben bien en UV |
| Erinacinas | Micelio | El cuerpo fructífero por lo general no las produce en cantidad detectable |

Fuente: revisión de Kawagishi y colaboradores sobre hericenonas y erinacinas como estimuladores de la
biosíntesis de NGF (*Mycology*, 2010, tandfonline.com); y estudio sobre influencia de sustrato y tipo de
tejido en la producción de erinacinas y la expresión de sus genes biosintéticos (*Journal of Fungi* /
PMC11969743, 2025). Trabajo reciente de aislamiento e identificación de hericenonas en cuerpos fructíferos:
*Journal of Natural Products*, 2025 (PMC11773572 / pubs.acs.org, 10.1021/acs.jnatprod.4c01018).

## El método actual de referencia

En 2026 se publicó un método **UHPLC-UV validado para determinación simultánea de hericenonas, hericenos,
erinacinas y ergosterol** en materias primas y productos terminados derivados de cuerpo fructífero y/o
micelio de *H. erinaceus*, con separación cromatográfica confiable y una corrida total de alrededor de
**38 minutos** (*Molecules* / PMC12899107).

Ese método resuelve tres problemas de una vez:

1. Mide marcadores de **las dos partes** del hongo en la misma corrida, así que sirve para verificar qué
   material te vendieron.
2. Incluye **ergosterol**, que es el indicador de biomasa fúngica real (ver `238`).
3. Está validado, así que se puede citar en un expediente y no solo en una conversación.

Condiciones que puedes esperar (orden de magnitud; el método publicado manda):

```
Columna:      C18 sub-2 um, UHPLC
Fase movil:   agua acidificada / acetonitrilo, gradiente largo
Deteccion:    UV; las hericenonas y hericenos absorben en el rango aromatico,
              el ergosterol tiene su maximo caracteristico cerca de 282 nm
Corrida:      ~38 min
Preparacion:  extraccion con solvente organico (metanol/etanol), filtracion 0,22 um
Confirmacion: LC-MS/MS o HRMS si necesitas identidad inequivoca (ver 84)
```

## El problema de los patrones

Sin patrón de referencia certificado no hay cuantificación, solo estimación (ver `70`). Para hericenonas y
erinacinas los patrones comerciales son pocos, caros y no siempre disponibles. Opciones reales:

| Situación | Qué se puede hacer | Qué se puede declarar |
|---|---|---|
| Tienes patrón de erinacina A | Cuantificación absoluta de ese analito | "erinacina A: X mg/g base seca (UHPLC-UV)" |
| No tienes patrón | Perfil relativo / huella cromatográfica | "perfil cromatográfico conforme al material de referencia interno" |
| Solo quieres verificar material | Ergosterol + β/α-glucano + ITS | Identidad y material, no potencia de estos marcadores |
| Necesitas identidad estructural | HRMS y RMN | Identificación, no cuantificación de rutina |

**Regla honesta:** si no lo puedes medir, no lo declares. Una etiqueta que dice "rico en erinacinas" sin
ensayo es un claim de composición sin respaldo, y eso también es un riesgo regulatorio, no solo un problema
científico (ver `276`, `282`).

## Alternativa práctica: la huella cromatográfica

Cuando el objetivo es control de lote y no un número absoluto, se usa **fingerprinting**: se corre el
método, se guarda el cromatograma de un lote de referencia y cada lote nuevo se compara (tiempos de
retención, relaciones de área entre picos). Es un control de identidad y consistencia perfectamente válido,
mucho más barato, y se declara como lo que es (ver `104`, `60`).

## Ejemplo aplicado — decidir el plan analítico de BIO-SETA

**(ILUSTRATIVO)**

```
Objetivo comercial: vender extracto de melena de leon de cuerpo fructifero.

Plan minimo (obligatorio, por lote):
   identidad ITS ................ 1 vez por proveedor/cepa
   beta y alfa-glucano K-YBGL ... cada lote      -> sostiene la etiqueta
   humedad ...................... cada lote
   metales pesados ICP-MS ....... cada lote o por frecuencia definida

Plan ampliado (cuando el presupuesto lo permita):
   UHPLC-UV simultaneo .......... perfil de hericenonas/hericenos + ergosterol
                                  -> confirma cuerpo fructifero y da huella de lote

Lo que NO se hace: declarar "0,3 % hericenonas" porque el proveedor lo dijo.
```

## Qué se puede y qué no se puede afirmar

- Se puede reportar un valor **si lo mediste**, con método, patrón, unidad y base.
- Se puede describir el estado de la ciencia: "las hericenonas y erinacinas han sido estudiadas por su
  efecto sobre la biosíntesis de NGF en cultivos celulares" `[in vitro]`.
- **No se puede** decir que estimulan el crecimiento de nervios en personas, que mejoran la memoria o que
  previenen enfermedades neurológicas. Esa frase específica ya fue un problema para BIO-SETA (ver `268`).
- **No se puede** citar erinacinas en un producto de cuerpo fructífero (ver `225`).
- Recuerda que un aumento de NGF en astrocitos de roedor en placa es un hallazgo mecanístico, no un
  desenlace clínico (ver `12`, `119`).

## Errores comunes

- Declarar el marcador que corresponde a la otra parte del hongo.
- Aceptar un "análisis" que sea solo un cromatograma sin patrón ni identificación de picos.
- Pedir "hericenonas totales": no es una categoría analítica bien definida como tal; pide analitos
  identificados o huella.
- Usar un método de cannabis o de otra matriz sin verificar que separa estos compuestos.
- No correr humedad y reportar en base húmeda (`07`).

## Conexión con otros módulos

→ `225-melena-de-leon-hericium-quimica.md` — el contexto de la especie.
→ `238-ergosterol-como-marcador.md` — el analito que va en la misma corrida y prueba biomasa.
→ `70-patrones-de-referencia-y-trazabilidad.md` — sin patrón no hay cuantificación.
→ `104-metabolomica-y-huella-quimica.md` — el enfoque de fingerprinting.
→ `12-niveles-de-evidencia.md` — cómo se nombra un `[in vitro]` sin exagerarlo.
