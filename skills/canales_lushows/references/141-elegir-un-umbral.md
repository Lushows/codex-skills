# 141 · Elegir un umbral y defenderlo

**Qué resuelve:** umbrales puestos a ojo, que no se pueden discutir; y la tentación de
bajar el listón cuando el episodio no lo cumple.

---

## De dónde sale un número

Un umbral del canal no se elige: **se calibra**. El procedimiento es siempre el mismo y
deja rastro:

1. **Medir lo que ya existe.** Se pasa la medida por los episodios y pruebas que hay,
   incluidos los que se ven mal.
2. **Separar por juicio humano.** Se marcan a mano los tramos que se ven flojos mirando
   la rejilla de fotogramas. Sin mirar el número.
3. **Buscar el corte que separa los dos montones.** El umbral es el valor donde las dos
   listas dejan de mezclarse, no una cifra redonda.
4. **Escribirlo con su motivo al lado**, en el propio código.

Ejemplo real, el hueco: `HUECO_MIN = 0.40`, con el comentario *"por debajo de esto el
ojo no lo registra como vacío"*. Un corte a negro de 0,25 s pasa como parpadeo de
montaje; a partir de 0,4 s se lee como error. El número no es bonito, es el sitio donde
cambia la percepción.

## Los umbrales vivos y su procedencia

| Umbral | Valor | Por qué ese |
|---|---|---|
| `HUECO_MIN` | 0,40 s | Debajo no se percibe como vacío |
| eventos/min | ≥ 44 | Debajo el montaje se lee como pase de diapositivas (`10`) |
| simultaneidad media | ≥ 2,00 | Con 1 elemento vivo no hay collage, hay sustitución (`12`) |
| duración media | 1,6–2,4 s | Debajo parpadea, encima hay planos muertos (`13`) |
| cobertura media | 22–38 % | Debajo se lee vacío; encima se tapa el fondo y se satura |
| cuadro casi vacío | < 14 % cubierto | Suelo medido en la rejilla: por debajo el recorte "flota" |
| recuadro muerto | < 12 % del tiempo | Agujero fijo en la composición (`20`) |
| separación de repetición | 25 s | Antes de eso el espectador recuerda la imagen |
| gesto | 2,5 s | Usos más juntos se leen como UN movimiento, no como repetición |
| oclusión | > 55 % tapado | El de abajo deja de comunicar |
| fuera de cuadro | > 12 % fuera | Sangrado de página aceptable hasta ahí (`25`) |

## El umbral no es igual en todo el episodio

Un solo número para todo el episodio obliga a que el remate corra tanto como el gancho,
y el remate necesita aire (`18`). Por eso el objetivo de densidad es **por tipo de
bloque**:

```python
OBJ_BLOQUE = {"gancho": 50, "pregunta": 44, "peso": 36, "maquina": 40,
              "piezas": 40, "remate": 30}
```

Y el informe por escena marca `<-- flojo` contra el objetivo de SU bloque, no contra 44.

## Qué hacer cuando el episodio no lo cumple

Se mueve el montaje. **Nunca el umbral.** Bajar la meta a 38 ev/min porque el episodio
da 38 no arregla nada: convierte el auditor en un sello de goma y el canal pierde la
única medida objetiva que tenía.

Lección del piloto: 67,4 ev/min contra una meta de 44 —muy por encima— y el episodio
se veía pobre igual, porque la simultaneidad era 1,12. Si se hubiera "ajustado" el
umbral al alza para castigarlo, el diagnóstico seguiría siendo falso. **El problema no
estaba en el número; estaba en qué número se miraba** (`142`, `148`).

Orden de corrección cuando algo no pasa:

1. Anclas huérfanas (si hay, todo lo demás describe otro montaje).
2. Huecos, los largos primero.
3. Simultaneidad y cobertura.
4. Duración media, sólo si sigue fuera después de lo anterior.
5. Eventos/min: casi nunca hay que tocarlo, sube solo al arreglar 2 y 3.

## Cuándo SÍ se toca un umbral

Hay un caso legítimo, y exige las mismas cuatro pruebas del principio:

- **La métrica cambió de definición.** Al pasar de "superficie del elemento" a
  "superficie visible dentro del lienzo" (`146`), la cobertura de un mismo episodio
  cayó de 46,9 % a un valor menor. El rango 22–38 % se recalibró **porque medía otra
  cosa**, no porque un episodio no pasara.
- **El formato cambió.** El vertical (9:16) tiene otro lienzo y otros suelos.

Se documenta en el código, con la fecha y el episodio donde se comprobó. Un umbral sin
procedencia escrita es un umbral que alguien bajará dentro de tres meses.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Elegir el umbral por número redondo | No separa los buenos de los malos; sólo da conversación |
| Bajarlo para que el episodio pase | El auditor deja de ser una medida y pasa a ser un trámite |
| Un solo umbral para todo el episodio | El remate se mide con la vara del gancho y sale "flojo" siempre |
| Subirlo "por exigencia" sin calibrar | Alarmas continuas; la gente deja de leer el informe (`143`) |
| Cambiar el umbral y no el comentario | Nadie sabe ya de dónde salió el número |

## Relacionado

`10` densidad de eventos · `18` densidad por tipo de bloque · `140` medir antes de
renderizar · `142` la medida que miente · `147` cuándo una métrica deja de servir
