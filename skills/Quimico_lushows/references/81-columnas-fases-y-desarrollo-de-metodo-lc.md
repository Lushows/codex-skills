# 81 — Columnas, fases y desarrollo de método LC: por qué dos laboratorios dan números distintos

Cuando dos laboratorios te dan potencias diferentes de la misma muestra, la causa está casi siempre en la
columna y en el método, no en la mala fe. Este módulo explica cómo se elige la fase estacionaria, cómo se
desarrolla un método de cromatografía líquida y qué preguntas hacen que un proveedor de servicio se ponga
serio contigo. No vas a desarrollar el método tú, pero sí vas a **aprobar el que te cobran** y a decidir si
el número que sostiene tu etiqueta es defendible.

Términos:
- **Fase estacionaria (stationary phase)** = lo que está unido a la sílice dentro de la columna y decide qué
  se retiene.
- **Selectividad (α, selectivity)** = qué tan distinto retiene la columna a dos compuestos. Es la palanca más
  potente para separar.
- **Retención (k, retention factor)** = cuánto se demora un compuesto respecto al frente no retenido.
- **Resolución (Rs)** = qué tan separados quedan dos picos. Rs ≥ 1,5 = separación a línea base.
- **End-capping** = tapar los silanoles libres de la sílice para evitar colas.
- **Core-shell (superficially porous)** = partícula con núcleo sólido y capa porosa: eficiencia de UHPLC a
  presión de HPLC.

## La ecuación que gobierna todo

```
Rs = (raiz(N)/4) * ((alfa - 1)/alfa) * (k/(1 + k))
      \_______/     \______________/   \________/
      eficiencia      SELECTIVIDAD      retencion

- N (eficiencia): duplicarlo solo mejora Rs en raiz(2) = 1,41. Caro y con techo.
- alfa (selectividad): cambiar de C18 a fenil-hexilo puede duplicar Rs. BARATO.
- k (retencion): subir k de 1 a 5 ayuda mucho; de 5 a 20 casi nada y alarga la corrida.

Traduccion de negocio: si el laboratorio te dice "no separa, hay que comprar
un UHPLC", casi siempre miente por comodidad. Lo primero es cambiar la QUIMICA
de la columna o el solvente organico, no el equipo.
```

## Catálogo de fases: qué usar para qué

| Fase estacionaria | Cómo retiene | Buena para | En nuestro mundo |
|---|---|---|---|
| **C18 (ODS)** | Hidrofóbica, cadena de 18 carbonos | El 80 % de todo | Cannabinoides, psilocibina, la mayoría de marcadores |
| **C8** | Igual pero menos retentiva | Compuestos muy apolares que en C18 no salen | Lípidos, algunos triterpenos |
| **Fenil-hexilo (phenyl-hexyl)** | Interacción π-π con anillos aromáticos | Isómeros aromáticos que C18 no separa | Δ8 vs Δ9-THC, CBD vs CBG (`180`) |
| **PFP (pentafluorophenyl)** | π-π + dipolo + interacción con halógenos | Isómeros posicionales, bases | Alcaloides, cannabinoides isoméricos |
| **HILIC** (hydrophilic interaction) | Retiene lo **polar**; móvil rica en acetonitrilo | Compuestos muy polares que en RP salen en el frente | **Psilocibina** (zwitteriónica, mal retenida en C18) |
| **Intercambio iónico (IEX)** | Carga | Proteínas, azúcares fosforilados | Poco frecuente aquí |
| **Quiral (chiral)** | Reconoce enantiómeros | Separar R/S | Verificación de quiralidad (`43`) |
| **SEC / GPC** | Tamaño molecular | Polisacáridos, determinar peso molecular | Distribución de peso molecular de β-glucanos (`219`) |

La fila de HILIC merece énfasis: **la psilocibina es una molécula zwitteriónica y muy polar**. En una C18
convencional sale casi con el frente del solvente, donde eluye toda la matriz, y la cuantificación se
degrada. Por eso los métodos modernos usan C18 polar-embedded, C18 compatible con 100 % acuoso, o
directamente HILIC, con buffer de formiato o acetato de amonio (`256`).

## Anatomía de una columna y qué significa cada número

```
"Kinetex C18, 150 x 4,6 mm, 2,6 um, 100 A"

  Kinetex ...... marca / tecnologia (aqui core-shell)
  C18 .......... quimica de la fase
  150 mm ....... largo: mas largo = mas N = mas resolucion y mas tiempo y mas presion
  4,6 mm ....... diametro interno: define el flujo (1,0-1,5 mL/min).
                 2,1 mm es para UHPLC/MS (0,3-0,6 mL/min, menos solvente)
  2,6 um ....... tamano de particula: mas pequeno = mas eficiencia y mas presion
  100 A ........ tamano de poro: 100 A para moleculas pequenas;
                 300 A para proteinas y polimeros

Costo de una columna analitica (ILUSTRATIVO): USD 400-900.
Vida util: 500-2000 inyecciones segun lo sucia que este la matriz.
Por eso el laboratorio cobra caro las matrices grasas (aceites, concentrados):
le matan columnas.
```

## Desarrollo de método LC, paso a paso

| Paso | Qué se hace | Decisión que sale |
|---|---|---|
| 1. Definir el ATP | Qué analitos, en qué matriz, en qué rango, con qué exactitud (`75`) | Alcance del método |
| 2. Conocer los analitos | pKa, logP, cromóforo, estabilidad | Modo (RP/HILIC), λ, pH de trabajo |
| 3. Barrido inicial (scouting) | Gradiente amplio 5→95 % B en C18, 2 solventes (ACN y MeOH) | ¿Se retiene? ¿Cuántos picos hay? |
| 4. Ajustar selectividad | Cambiar solvente orgánico, pH, temperatura, o fase | Se resuelve el par crítico |
| 5. Optimizar gradiente | Achatar la pendiente donde están los picos difíciles | Corrida final |
| 6. Robustez preliminar | Variar ±0,2 pH, ±5 °C, ±2 % B | Parámetros críticos identificados |
| 7. Preparación de muestra | Solvente, sonicación, dilución, filtro (`68`, `69`) | Recuperación aceptable |
| 8. Validación | ICH Q2(R2) (`75`) | Método defendible |

Reglas prácticas que valen para leer cualquier método:

- **pH: dos unidades de distancia del pKa.** Un ácido (THCA, pKa ≈ 3) se cromatografía a pH ≈ 2–2,5 para que
  esté neutro y retenga bien. Por eso el 0,1 % de ácido fórmico (`79`).
- **Metanol vs acetonitrilo cambia la selectividad**, no solo la fuerza. Cambiar de uno a otro es la forma
  más barata de resolver una coelución.
- **La temperatura mueve pares críticos.** En cannabinoides, CBD/CBG es sensible a temperatura; sin horno de
  columna, el método no es reproducible entre días.
- **La sílice clásica se disuelve por encima de pH 8** y se hidroliza por debajo de pH 2. Fuera de ese rango
  hay que usar columnas híbridas.

## Ejemplo aplicado — separar 11 cannabinoides incluyendo Δ8 y Δ9-THC

```
Problema: metodo de 6 cannabinoides en C18 no separa D8-THC de D9-THC (Rs = 0,6).
          El producto de un cliente reportaba 0,25 % de "D9" y en realidad era
          una suma de isomeros (180).

Intentos y resultado (ILUSTRATIVO):
  a) Alargar la columna 150 -> 250 mm C18 ......... Rs 0,6 -> 0,9   insuficiente
  b) Bajar temperatura 40 -> 25 C ................. Rs 0,9 -> 1,1   insuficiente
  c) Cambiar acetonitrilo por metanol ............. Rs 1,1 -> 1,3   insuficiente
  d) Cambiar fase C18 -> FENIL-HEXILO, 150 mm ..... Rs = 2,1        RESUELTO
     (interaccion pi-pi con el anillo aromatico distingue la posicion
      del doble enlace en el anillo de terpeno)

Metodo final (ILUSTRATIVO):
  Columna: fenil-hexilo 150 x 4,6 mm, 2,7 um core-shell, 35 C
  A: agua + 0,1 % acido formico | B: metanol + 0,1 % acido formico
  Gradiente: 70 % B (0 min) -> 78 % B (14 min) -> 95 % B (16-18 min) -> 70 % B (21 min)
  Flujo 1,0 mL/min | DAD 228 nm (cuant.) y 280 nm (CBN, confirmacion)
  Par critico declarado: D8-THC / D9-THC, Rs >= 1,5 como criterio de SST (77)

Costo del desarrollo (ILUSTRATIVO): COP 5-10 millones y 4-6 semanas,
mas la validacion aparte (75).
```

Ese ejercicio es el que hay que exigirle a un laboratorio que dice "yo hago cannabinoides": **¿cuál es tu
par crítico declarado y qué resolución te da?** Si nunca separó Δ8 de Δ9, su método es de la era anterior a
los semisintéticos (`181`).

## Cuidado de la columna (por qué te lo cobran)

| Enemigo | Qué hace | Prevención |
|---|---|---|
| Matriz grasa (aceites, concentrados) | Se acumula en cabeza de columna, sube presión | Dilución, SPE (`69`), precolumna (guard column) |
| Partículas | Tapan el frit | Filtro de 0,22–0,45 µm en todas las muestras |
| pH extremo | Disuelve la sílice | Trabajar pH 2–8 o columna híbrida |
| Buffers secándose | Cristalizan y tapan | Lavar con agua antes de guardar en orgánico |
| Choque de presión | Colapsa el lecho | Subir flujo gradualmente |

## Qué preguntarle al laboratorio

1. ¿Cuál es su **par crítico** en mi matriz y qué **Rs** obtiene? ¿Está en su SST?
2. ¿Su método separa **Δ8 de Δ9-THC**? ¿Y CBD de CBG? ¿Me muestra el cromatograma de la mezcla de patrones?
3. ¿Usan **precolumna**? ¿Cada cuánto cambian la analítica?
4. ¿Qué **preparación de muestra** aplican a matriz grasa y cuál es su recuperación?
5. Si mi producto es psilocibina: ¿qué columna usan y cómo garantizan retención de un compuesto tan polar?
6. ¿El método es propio, de farmacopea o de una nota de aplicación del fabricante del equipo? (Las tres son
   válidas, pero cambian lo que puedes exigir — `280`, `281`.)

## Errores comunes

- **Creer que "C18" describe una columna.** Hay cientos de C18 con selectividades distintas; la marca y el
  end-capping importan.
- **Comparar potencias entre laboratorios con métodos distintos** y llamar fraude a lo que es selectividad.
- **Pedir "más resolución" comprando equipo** en vez de cambiar fase o solvente.
- **Aceptar un método sin par crítico declarado.** Es el indicador más rápido de método copiado sin entender.
- **Ignorar la preparación de muestra.** Un método cromatográfico perfecto sobre una extracción incompleta da
  un resultado bajo y reproducible: preciso y falso (`68`).
- **No pedir el cromatograma.** Todo lo anterior se ve en 30 segundos mirando el cromatograma.

## Conexión con otros módulos

→ `31-principio-de-la-cromatografia.md` — la teoría de N, k y α.
→ `79-hplc-y-uhplc.md` — el equipo y el método de cannabinoides de referencia.
→ `80-deteccion-uv-dad-y-pureza-de-pico.md` — por qué la coelución no siempre se ve.
→ `83-lc-ms-ms-y-mrm.md` — cuando la selectividad la pone el detector y no la columna.
→ `69-extraccion-para-analisis-spe-y-quechers.md` — limpiar la muestra para no matar la columna.
→ `180-delta8-delta10-e-isomerizacion.md` — el par crítico que define un laboratorio moderno.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — el caso HILIC / compuesto polar.
