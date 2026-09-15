# 111 — Banderas rojas en un COA (el catálogo de señales de alarma, una por una)

El módulo `110` te enseñó a leer un certificado completo. Este es la versión de combate: el catálogo de
señales que, cuando aparecen, te dicen que el documento no soporta la decisión que ibas a tomar. Casi ninguna
de estas banderas es una acusación de fraude —muchas son descuido, plantilla vieja o laboratorio barato—, pero
todas tienen la misma consecuencia práctica: **con ese papel no puedes liberar un lote, ni sostener una
etiqueta, ni defenderte ante una autoridad**. Léelo como una lista de chequeo de cinco minutos antes de pagar
una compra.

Términos: **bandera roja (red flag)** = señal que obliga a preguntar antes de aceptar. **base (basis)** = con
o sin agua. **LOD/LOQ** = límite de detección / cuantificación (`73`). **alcance acreditado (scope)** = lo que
la acreditación realmente cubre (`107`). **ND (not detected)** = por debajo del LOD del método usado.

## Nivel 1 — banderas que invalidan el documento (no se negocia, se rechaza)

| # | Bandera roja | Por qué invalida |
|---|---|---|
| 1 | **"Polisacáridos" o "polisacáridos totales" en vez de β-glucano** | Mide también almidón del grano, manitol y trehalosa. Es el disfraz #1 del micelio en grano (`218`, `222`) |
| 2 | **Sin método declarado por ensayo** | Un número sin método no es auditable ni comparable |
| 3 | **Sin número de lote** | No es trazable: el COA no ampara ningún producto físico |
| 4 | **Sin base declarada** (ni humedad para deducirla) | 27,6 % tal cual con 8 % de humedad son 30,0 % base seca. Sin base, no se compara con nada (`07`) |
| 5 | **Fecha de análisis anterior a la de producción del lote** | Físicamente imposible: es documento reciclado o transcripción errada |
| 6 | **"No detectado" sin LOD/LOQ** | ND no significa ausencia; significa "por debajo de un límite que no me dijiste" |
| 7 | **LOQ mayor que el límite de especificación** | El "cumple" es vacío: el método no puede ver el nivel que importa |
| 8 | **Sin firma ni responsable identificable** | Un PDF sin responsable no es un certificado, es un archivo |

## Nivel 2 — banderas que exigen explicación antes de aceptar

**9. Laboratorio sin acreditación para ESE ensayo.** El logo va en el encabezado; el alcance va en el anexo
técnico. Un laboratorio acreditado para metales en agua no lo está para metales en polvo de hongo. Preguntar
sin agresividad: *"¿este ensayo en esta matriz está dentro de su alcance? Si no, ¿lo reportan como fuera de
alcance?"*. Reportar fuera de alcance es legítimo; ocultarlo no (`107`).

**10. Alcance de acreditación que no cubre la matriz.** Variante de la anterior y la más frecuente: el ensayo
sí está, la matriz no. Métodos se validan **por matriz**; un extracto oleoso y un polvo no son el mismo
problema analítico (`75`).

**11. La muestra la envió el proveedor, no tú.** Entonces el COA describe lo que el proveedor eligió mandar,
no el lote. Es el sesgo más grande de todo el sistema y no cuesta nada corregirlo: muestrear tú, o pedir
muestreo del laboratorio (`109`).

**12. Ausencia de humedad en un producto sólido.** Sin humedad no hay base seca, no hay corrección, no hay
comparación y no hay predicción de estabilidad (`98`, `35`).

**13. Resultados sospechosamente redondos.** "30,0 %", "20 %", "50 mg/g", tres analitos terminados en cero.
Un resultado instrumental real tiene decimales sucios: 30,7; 4,1; 0,082. Números redondos en cadena huelen a
valor de etiqueta copiado, a redondeo intencional o a resultado "ajustado" al claim. No es prueba de fraude,
es motivo para pedir los datos crudos.

**14. Un solo lote presentado como si fuera la especificación.** "Nuestro reishi tiene 30 % de β-glucano"
respaldado por un COA. Una especificación necesita varios lotes y un **rango** (`282`).

**15. COA de la marca y no del lote.** Muy común en importación: un certificado de hace dos años que
"representa el producto". No representa nada de lo que te van a despachar.

**16. Incertidumbre ausente en un resultado que decide un cumple/no cumple.** Sin U y sin regla de decisión,
el veredicto no es defendible (`76`, `107`).

**17. Método de cereales aplicado a hongos.** Un COA de hongo que cite AOAC 995.16 o "mixed-linkage β-glucan"
usó liquenasa, que no reconoce el β-glucano 1,3:1,6 fúngico. Da casi cero, y ese cero no significa lo que
parece (`91`).

**18. El panel no incluye el contaminante que el proceso realmente puede dejar.** Un extracto hecho con etanol
cuyo COA no reporta solventes residuales; un cultivo en sustrato de grano sin micotoxinas; un producto
inhalado con límites tomados de alimentos.

**19. Suma que no cuadra.** Los individuales no suman el total reportado, o la resta de glucanos no da. Es
aritmética de treinta segundos que detecta transcripciones y manipulaciones.

**20. Sin identidad de especie.** En hongos, la potencia sin identidad no significa nada: *Ganoderma* tiene
decenas de especies y el mercado las mezcla (`245`, `103`).

## Cómo se ve la resta de glucanos cuando algo no cuadra (ILUSTRATIVO)

```
COA A (proveedor honesto)                COA B (sospechoso)
  Glucano total : 34,8 % p/p b.s.          "Polisacaridos totales": 50 % p/p (sin base)
  alfa-Glucano  :  4,1 % p/p b.s.          alfa-Glucano: no reportado
  beta-Glucano  : 30,7 % p/p b.s.          "beta-Glucano": 40 % p/p
  Metodo        : Megazyme K-YBGL v2025    Metodo: "metodo interno"
  Humedad       : 5,0 % (Karl Fischer)     Humedad: no reportada

Lectura de B:
  - Declara beta-glucano SIN haber medido alfa-glucano -> la resta no existe -> el numero no existe
  - 40 % sin base y sin metodo no se puede comparar con los 30,7 % de A
  - "Polisacaridos totales 50 %" es compatible con micelio sobre arroz al 40 % de almidon
Conclusion: A y B no compiten. B no reporto beta-glucano; reporto una impresion.
```

Cifras **(ILUSTRATIVO)**. Este par es el caso real más común del mercado de hongos, y el que hace que el
comprador ingenuo elija al proveedor peor porque "trae más".

## La lista de chequeo de cinco minutos

```
[ ] El lote del COA coincide con el lote fisico que tengo enfrente
[ ] Hay fecha de muestreo, de recepcion y de analisis, en secuencia logica
[ ] Dice quien tomo la muestra (si no dice: preguntalo por escrito)
[ ] Cada ensayo tiene METODO con referencia verificable
[ ] Cada resultado tiene UNIDAD y BASE; si es base tal cual, hay humedad
[ ] Cada "ND" tiene su LOD/LOQ, y el LOQ es al menos 5-10 veces menor que el limite
[ ] Hay especificacion escrita contra la cual se comparo
[ ] Si dice "Cumple": hay incertidumbre y regla de decision
[ ] El numero de acreditacion existe, esta vigente y su ANEXO cubre ensayo + matriz
[ ] Las sumas y las restas cuadran cuando las rehago
[ ] Esta firmado por una persona con nombre y cargo, y tiene pagina n de N
```

Once casillas. Si fallan las de Nivel 1, el COA se devuelve. Si fallan las de Nivel 2, se pregunta antes de
comprar — y la calidad de la respuesta te dice más del proveedor que el propio certificado.

## Errores comunes

- **Discutir el porcentaje y no el método.** La discusión que importa está en la columna de la derecha.
- **Aceptar el COA porque "está en inglés y se ve serio".** El formato no es evidencia.
- **Rechazar de entrada un ensayo reportado fuera de alcance.** A veces es la única forma de medir un analito
  raro; lo que no se acepta es que no lo digan.
- **Pedir explicaciones por teléfono.** Todo lo que vayas a usar en una disputa debe quedar por escrito (`112`).
- **Revisar el COA después de pagar.** La revisión va antes del giro, no después del contenedor.
- **Guardar solo el PDF.** Sin la cadena de custodia asociada, el COA no defiende el lote (`109`, `168`).

## Conexión con otros módulos

→ `110-como-leer-un-coa.md` — la anatomía completa del documento, campo por campo.
→ `112-como-impugnar-un-resultado.md` — el procedimiento cuando la bandera roja se confirma.
→ `113-lab-shopping-e-inflacion-de-potencia.md` — el fraude estructural detrás de varias de estas banderas.
→ `213-como-leer-un-coa-de-cannabis.md` — las banderas propias del sector cannabis.
→ `222-polisacaridos-totales-por-que-no-sirve.md` y `218-el-fraude-del-micelio-en-grano.md` — la bandera #1.
→ `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — el panorama del fraude en el mercado.
→ `295-checklist-de-calidad-quimica.md` — esta lista integrada al sistema de calidad completo.
