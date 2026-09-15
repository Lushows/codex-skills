# 280 · Escribir para una voz sintética

**Qué resuelve:** el canal no tiene locutor. Tiene un modelo que lee exactamente lo que
le pongas delante, sin entender nada. Un locutor humano corrige de oficio: ve una sigla
rara y la desarrolla, ve una ironía y la entona, se traba y repite la toma. La voz
sintética no corrige nada. **El texto es la única palanca**, y cualquier cosa que no
esté escrita no va a pasar.

> Este módulo es la capa de arriba del bloque de voz. Lo genérico de escribir para el
> oído está en `95` (y en `editpro:280`): frase corta, sujeto delante, voz activa. Aquí
> sólo va **lo que cambia por ser una máquina la que lee**.

---

## Las cuatro cosas que un humano hace y la máquina no

| El locutor humano… | `edge-tts`… | Qué obliga a hacer |
|---|---|---|
| Entona la ironía | La lee plana, y se oye como un error de guion | Ninguna ironía. El juicio lo pone el dato |
| Desarrolla la sigla que no se puede decir | La deletrea o la destroza | Se escribe desarrollada, o se sustituye |
| Repite la toma si se traba | No se traba nunca: **se equivoca en silencio** | Hay que escuchar el resultado (§ `289`) |
| Pone el énfasis donde va | Reparte el mismo peso en toda la frase | El énfasis se **construye en la mezcla** (§ `285`) |

La cuarta es la que más sorprende y la más cara. La voz sale con un rango dinámico
plano —LRA 2,7 medido en el stem de `ep01-lustig`— y no hay forma de pedirle que
recalque una palabra. El relieve del episodio no se escribe: se monta después.

## El guion es el origen, y no se copia a mano

El texto de la locución **no se escribe en `voz.py`**. Se extrae del `guion.md` aprobado:

```python
def texto_del_guion(ruta):
    md = io.open(ruta, encoding="utf-8").read()
    md = md.split("## MINUTO 1")[1].split("## Los datos")[0]
    md = md.split("\n", 1)[1]          # descartar el resto de la línea de título
    lineas = []
    for l in md.split("\n"):
        t = l.strip()
        if not t or t.startswith(("#", ">", "|")):      continue
        if t.startswith(("- ", "* ", "+ ")) or t.startswith("---"): continue
        if t == "···":
            lineas.append("...");                       continue
        t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)          # quitar marcas de ancla
        lineas.append(t)
```

Ejecutado sobre `piloto/ep01-lustig/guion.md` devuelve **155 palabras**, que son
exactamente las de `guion.txt` y las 155 de `tiempos.json`. Si el texto se copiase a
mano, el desfase entre lo aprobado y lo grabado aparecería en la fase 6, con el montaje
hecho.

### Las tres trampas de esa extracción, las tres ya pagadas

1. **La línea de título arrastra su propia cola.** `split("## MINUTO 1")[1]` deja
   colgando el resto de ESA línea —`— guion cerrado`— y se colaba en la locución. Por eso
   está el `split("\n", 1)[1]` de la línea siguiente, y además un cinturón al final:
   `txt.split("guion cerrado")[-1]`.
2. **Una línea en negrita empieza por `*`.** Descartar todo lo que empiece por `*` se
   come frases enteras. El filtro exige el espacio: `"* "`, `"- "`, `"+ "`.
3. **Los `···` del guion no son texto.** Son la marca de pausa dramática de la casa. Se
   convierten en `...` y se **pegan a la frase anterior**, porque una línea con sólo
   puntos suspensivos se lee como una frase propia y la prosodia se rompe.

## Lo que la voz no debe ver nunca

| En el `guion.md` | Para qué está | Qué hace el extractor |
|---|---|---|
| `**palabra**` | Marca el ancla del guion visual (§ `250`) | Quita los asteriscos, deja la palabra |
| `···` | Pausa dramática | La convierte en `...` pegado a la frase anterior |
| `(nota de pronunciación)` | Para el que escribe | ⚠️ **No se filtra: se leería.** Va fuera del bloque |
| `— fuente: doc pág. N` | Control de verificación | Empieza por `—`, no por `- `: ⚠️ **se colaría** |
| Tablas, títulos, citas | Documentación del guion | Filtrados por `#`, `>`, `|` |

Las dos filas con ⚠️ son deuda conocida del extractor: hoy funciona porque las notas
viven fuera de la sección del minuto. Quien meta una nota entre dos frases se la va a
encontrar locutada.

## Siglas, nombres y extranjerismos

- **Siglas:** la primera vez desarrolladas. Después, en sigla **sólo si es
  pronunciable** (OTAN sí, SEC no). Si no lo es, se sustituye por el sustantivo: «el
  regulador», «la fiscalía».
- **Nombres extranjeros:** se fija **una** pronunciación y se escribe **como suena en
  castellano** si el modelo la destroza. No hay vergüenza en escribir «Lustig» y
  comprobar; lo que no vale es que suene distinto en el minuto 2 y en el minuto 7.
- **Palabras en otro idioma dentro de la frase:** el modelo cambia de fonética a mitad
  de palabra y suena a fallo. O se traduce, o se acepta y se comprueba.
- **Una comprobación vale más que una regla:** generar la palabra suelta cuesta dos
  segundos y sale de dudas.

```bash
edge-tts --voice es-MX-JorgeNeural --rate=-6% --pitch=-2Hz \
         --text "Lustig. Eiffel. Missouri." --write-media _prueba.mp3
```

## El tono de la casa, traducido a instrucciones para la máquina

El canal narra ingeniería, no moraliza (§ `95`). Con voz sintética eso deja de ser
estilo y se vuelve **requisito técnico**: la indignación necesita entonación, y no la
hay. Una frase escrita para ser dicha con rabia, leída plana, suena a nota de prensa.
La frase que funciona es la que **no necesita entonación para golpear**:

> «aprendiz de vendedor.»

Cuatro palabras, plana, y pega. Porque el golpe está en el contraste con lo que se acaba
de contar, no en cómo se dicen. Ése es el estándar: si la frase sólo funciona con la
entonación correcta, **está mal escrita para este canal**.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Escribir el texto de la locución en `voz.py` en vez de extraerlo | Lo grabado deja de ser lo aprobado y se descubre en la fase 6 |
| Descartar las líneas que empiezan por `*` sin exigir el espacio | Se pierden frases enteras en negrita, sin aviso |
| Dejar `···` como línea suelta | Se lee como frase: la prosodia se corta en dos |
| Meter una nota de pronunciación entre frases | La voz la lee |
| Ironía, sarcasmo, exclamaciones de indignación | Se oye como error, no como intención |
| Una sigla impronunciable | El modelo improvisa y cada vez improvisa distinto |
| Confiar en que «la voz lo entenderá» | No entiende nada: lee |
| Escribir una frase que necesita énfasis para funcionar | No hay énfasis. Hay que reescribirla o construirlo en la mezcla |

## Relacionado

`95` escribir para el oído · `281` ritmo en ppm · `282` la puntuación como partitura ·
`283` cifras al oído · `285` el relieve se construye · `289` errores de locución ·
`250` palabra a imagen · `editpro:280` escribir para el oído (genérico)
