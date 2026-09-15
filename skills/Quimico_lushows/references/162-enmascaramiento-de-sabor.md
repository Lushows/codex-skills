# 162 — Enmascaramiento de sabor (el amargo que devuelve el producto y arruina la recompra)

Un producto que sabe mal no se toma. Y un producto que no se toma no genera recompra, que es donde vive el
negocio. En hongos el problema tiene nombre: los triterpenos del reishi son de lo más amargo del reino vegetal
y fúngico; el chaga es terroso; los extractos de cannabis dejan un retrogusto herbal persistente. Este módulo
ordena las soluciones de la más barata a la más cara, y dice claramente cuál funciona de verdad.

Términos: **enmascaramiento (taste masking)** = impedir que la molécula amarga llegue al receptor.
**Receptores T2R (bitter taste receptors)** = familia de receptores del sabor amargo en la lengua.
**Recubrimiento (coating)** = barrera física sobre la partícula o la unidad. **Bloqueador de amargo (bitter
blocker)** = sustancia que interfiere con la señal del receptor. **Panel sensorial (sensory panel)** =
evaluación por catadores, ciega y estructurada.

## El principio: hay tres formas de ganar

1. **Que la molécula no toque la lengua** — cápsula, recubrimiento, encapsulación, complejo de inclusión.
2. **Que el receptor no la reconozca** — bloqueadores de amargo, ciclodextrinas.
3. **Que otra cosa domine la percepción** — dulzor, acidez, aromas, sal, grasa, temperatura.

Solo la primera es infalible. La tercera es la más barata y la más usada. La segunda es la más interesante y la
menos conocida.

## Escala de soluciones, de barata a cara

| Estrategia | Costo | Eficacia contra amargo fuerte | ¿Pyme? |
|---|---|---|---|
| **Cápsula** | Prácticamente cero | **Total** | Sí (`154`) |
| Dulzor (sacarosa, estevia, sucralosa) | Muy bajo | Parcial | Sí |
| Acidez (cítrico, málico) | Muy bajo | Parcial; corta el amargo | Sí |
| Sal (pizca de NaCl) | Nulo | Sorprendentemente útil, suprime amargo | Sí |
| Grasa / lácteo | Bajo | Buena: la grasa secuestra lipofílicos | Sí |
| Cacao, café, canela, jengibre | Bajo | Buena por enmascaramiento aromático | Sí |
| Ciclodextrina (HP-β-CD) | Medio-alto | **Muy buena, mecanismo real** | Sí, por amasado (`158`) |
| Bloqueadores de amargo comerciales | Medio | Variable según molécula | Sí, si el ingrediente está permitido |
| Recubrimiento de partícula (lecho fluido) | Alto | Muy buena | Maquila |
| Microencapsulación por spray | Alto | Muy buena | Maquila (`150`) |
| Tableta recubierta | Alto | Total mientras no se mastique | Maquila (`155`) |

Conclusión de ingeniería, sin romanticismo: **si el producto es muy amargo y no necesitas que sea bebible, la
cápsula gana por goleada.** Todo el resto del módulo aplica cuando el formato bebible o el polvo suelto es una
decisión de negocio ya tomada.

## El trío que funciona en polvos bebibles

Para un polvo funcional de hongos que se mezcla en agua, café o batido, la combinación que resuelve el 80 % de
los casos:

```
1. CACAO ALCALINIZADO (5–20 % de la porción)
   El cacao es amargo también, pero es un amargo ACEPTADO y culturalmente asociado a "bueno".
   Enmascara por dominancia aromática y por contenido graso.

2. DULZOR (estevia/monk fruit 0,05–0,3 %, o azúcar según posicionamiento)
   Los edulcorantes intensos tienen su propio retrogusto: mézclalos (estevia + eritritol)
   para que ninguno domine.

3. SAL (0,05–0,15 %)
   El sodio suprime la percepción de amargo de forma bien documentada en ciencia sensorial.
   Es el truco más barato y el menos usado.

+ opcional: canela, vainilla, jengibre — aromas cálidos que "cubren" lo terroso.
```

Un detalle de formulación que ahorra iteraciones: el amargo **se percibe tarde y dura**. La acidez y el dulzor
actúan al inicio. Por eso un producto puede "entrar bien" y dejar un retrogusto pésimo. Si vas a evaluar,
evalúa a los 30 y a los 60 segundos, no solo el primer sorbo.

## Ciclodextrinas: el mecanismo real

La HP-β-CD atrapa la molécula amarga dentro de su cavidad hidrofóbica. Si la molécula está adentro, el receptor
T2R no la ve. No es enmascaramiento perceptual: es **secuestro molecular**. Por eso funciona con amargos que
ningún saborizante logra tapar.

Requisitos para que funcione:
- Relación molar suficiente (típicamente 1:1 a 1:2 activo:CD; hay que determinarla).
- Que el complejo se forme de verdad — se verifica por DSC, FTIR o diagrama de solubilidad (`158`, `99`).
- Que la ciclodextrina esté permitida en tu categoría de producto. A agosto de 2026, verifica el estatus del
  ingrediente concreto ante INVIMA antes de formular (`266`).

Contrapartida honesta: si el complejo es muy estable, también puede modificar la liberación del activo. No
suele ser un problema en suplementos orales, pero es algo a verificar si tu claim depende de la absorción.

## Cómo se comprueba que el enmascaramiento funcionó

No se comprueba "porque a mí me supo bien". Se comprueba con un panel:

```
PANEL SENSORIAL MÍNIMO VIABLE (pyme)

  Participantes: 10–15 personas, no involucradas en el desarrollo
  Diseño: ciego, muestras codificadas con 3 dígitos, orden aleatorizado
  Enjuague entre muestras: agua + galleta sin sal, 60 s de espera
  Escalas (0–10): amargor · astringencia · retrogusto a 60 s · agrado global
  Muestras: control (sin enmascarar) + 2–3 prototipos
  Análisis: media y desviación por atributo; prueba estadística si vas a decidir
            entre prototipos cercanos → rutea a `Matematicas_lushows`

Registro: todo va al expediente de desarrollo (`286`). Un panel sin registro no existió.
```

Complemento instrumental cuando hay presupuesto: **lengua electrónica (e-tongue)**, que mide la respuesta de
sensores a los estímulos amargos. Es cara y no reemplaza al panel; lo complementa cuando hay que comparar
muchos prototipos.

## Ejemplo aplicado — polvo bebible de reishi

```
Problema: extracto dual de reishi, amargor intenso por triterpenos.
Porción objetivo: 3,0 g con 469 mg de extracto (`161`).

Prototipos (ILUSTRATIVOS)
  P0 control:  extracto + inulina                     amargor 8,4 / agrado 2,1
  P1:          + cacao 15 % + estevia 0,10 %          amargor 5,6 / agrado 5,3
  P2:          P1 + sal 0,10 % + canela 1 %           amargor 4,1 / agrado 6,8
  P3:          extracto complejado con HP-β-CD 1:2,
               + cacao 10 % + estevia 0,08 %          amargor 2,7 / agrado 7,9

Lectura: P2 es la mejor relación costo/beneficio para lanzar.
P3 es superior pero el costo del HP-β-CD por porción hay que evaluarlo
con `contador_lushows` antes de decidir.
Decisión ILUSTRATIVA: lanzar con P2, tener P3 como versión premium.
```

## Errores comunes

- Intentar tapar un amargo intenso solo con dulzor: se obtiene un producto dulce **y** amargo, que es peor.
- Evaluar el sabor uno mismo, sin ciego y sin panel. El desarrollador siempre cree que su producto sabe bien.
- Ignorar el retrogusto: el amargo aparece tarde y es lo último que recuerda el cliente.
- Usar saborizantes a niveles altos y arruinar el posicionamiento "natural" en la lista de ingredientes.
- Añadir ciclodextrina "un poquito" sin estequiometría: no complejea nada y solo encarece.
- Recubrir partículas y luego molerlas o comprimirlas: se rompe el recubrimiento y vuelve el amargo.
- Olvidar que el sabor cambia durante la vida útil: la oxidación genera notas rancias y metálicas. Evalúa el
  sabor también en los puntos del estudio de estabilidad (`164`).

## Conexión con otros módulos

→ `158-liposomas-y-ciclodextrinas.md` — cómo se hace y se verifica el complejo de inclusión.
→ `153-formas-farmaceuticas-panorama.md` — por qué el formato es la primera decisión de sabor.
→ `156-liquidos-goteros-y-jarabes.md` — enmascaramiento en medio acuoso.
→ `164-estabilidad-ich-q1-y-vida-util.md` — el sabor como atributo de estabilidad.
→ `224-triterpenos-ganodericos-analisis.md` — las moléculas responsables del amargor del reishi.