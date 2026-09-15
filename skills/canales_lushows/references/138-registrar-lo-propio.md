# 138 · Registrar lo propio

**Qué resuelve:** cómo se demuestra que una pista es nuestra **el día en que hace falta**,
que nunca es el día en que se genera. Es el equivalente sonoro de `fuentes.json`: un
manifiesto donde toda pista del episodio tiene una entrada, o el render no sale.

> ⚖️ **Esto no es asesoría legal** ni un sustituto de un registro formal de obra. Es la
> documentación que convierte «es mía» en algo que otro puede comprobar.

---

## Por qué existe

Una disputa (§ 133) se gana con **material de origen y fecha**, no con una afirmación.
«Es mía» es exactamente lo que escribe también quien subió música ajena; la diferencia
la marca poder adjuntar el código que produce ese audio y que cualquiera puede ejecutar.

Y hay un segundo motivo, menos dramático y más frecuente: **poder regenerar**. Si hay
que subir medio tono el tema del episodio 7, con el manifiesto es un parámetro; sin él,
es rehacer la pista a oído.

## El archivo: `audio/pistas.json`

Una entrada por pista, por efecto y por atmósfera. Vive en el repositorio, versionado.

| Campo | Qué guarda | Por qué |
|---|---|---|
| `alias` | nombre estable (`tema_ep07_tension`) | es el que usa el guion visual (§ 192) |
| `tipo` | música · efecto · atmósfera · archivo | decide qué otras comprobaciones aplican |
| `origen` | `sintetizado` · `archivo` · `banco` | el que no sea `sintetizado` arrastra § 134 o § 137 |
| `script` | ruta al generador, p. ej. `audio/generar_tension.py` | **la prueba principal** |
| `script_sha256` | hash del script en el momento de generar | ata la prueba a una versión concreta |
| `comando` | el comando de ffmpeg completo, literal | reproducible sin leer el script |
| `ffmpeg_version` | salida de `ffmpeg -version`, primera línea | la reproducción depende de la versión |
| `parametros` | tonalidad, tempo, duración, semilla si la hay | permite regenerar variaciones (§ 127) |
| `fecha_utc` | ISO 8601, en UTC | el panel del canal ya enseña horas en UTC: una sola zona |
| `wav_sha256` | hash del archivo resultante | identifica el audio exacto que salió al vídeo |
| `duracion_s` | segundos | cuadra con el manifiesto del montaje |
| `uso` | episodio y tramo donde suena | contestar «¿dónde está esto?» en dos segundos |
| `autor` | `Paper Empires` | quién declara la titularidad |
| `licencia` | `propia`, o ruta al PDF si `origen` ≠ sintetizado | la compuerta de § 134 |

### Ejemplo de entrada

```json
{
  "alias": "tema_ep07_tension",
  "tipo": "musica",
  "origen": "sintetizado",
  "script": "audio/generar_tension.py",
  "script_sha256": "9f2c…",
  "comando": "ffmpeg -f lavfi -i \"sine=f=110:d=42\" …",
  "ffmpeg_version": "ffmpeg version 8.1",
  "parametros": { "tonalidad": "La menor", "bpm": 68, "duracion_s": 42 },
  "fecha_utc": "2026-09-11T14:03:22Z",
  "wav_sha256": "1a77…",
  "duracion_s": 42.0,
  "uso": [{ "episodio": "ep07", "tramo": "02:10-02:52" }],
  "autor": "Paper Empires",
  "licencia": "propia"
}
```

## La compuerta

El manifiesto solo sirve si es **obligatorio**. La comprobación que lo hace obligatorio:

```
antes de renderizar:
  para cada pista de audio que entra al montaje:
      ¿tiene entrada en pistas.json?            → si no, ABORTAR
      ¿existe el script y su sha256 coincide?   → si no, ABORTAR
      ¿el wav_sha256 coincide con el archivo?   → si no, ABORTAR
      si origen != "sintetizado":
          ¿existe el PDF de licencia en la ruta? → si no, ABORTAR
```

Es el mismo principio que `fuentes.json` como compuerta (§ 188): una comprobación que
solo avisa se ignora a la tercera semana; una que **detiene el render** no.

## El historial de git como indicio

Los scripts viven en el repositorio, así que cada pista tiene además un commit fechado
que la precede. Es una capa más de respaldo y no cuesta nada.

⚠️ **Sin exagerar lo que vale:** un commit lo firma quien quiera con la fecha que quiera
en local. Es un **indicio consistente** —sobre todo si el repositorio está publicado en
un servidor externo, con su historial—, no una prueba con fecha cierta. No lo presentes
como si fuera un registro notarial.

## Registro formal: cuándo sí

Existe la opción de registrar una obra musical en la oficina de derecho de autor que
corresponda (en Colombia, la Dirección Nacional de Derecho de Autor; en Estados Unidos,
la Copyright Office). No lo hacemos pista por pista: no tendría sentido para cuarenta
efectos por episodio.

Tiene sentido plantearlo si **una pieza se convierte en el tema identificativo del
canal** —la sintonía de cabecera, el motivo que vuelve (§ 126, § 254)—, porque entonces
pasa a ser un activo de marca.

⚠️ **No conozco con certeza los requisitos, plazos y costes de cada oficina y no los voy
a inventar.** Si llega el momento, se comprueba en la web oficial del país y, si el
activo importa, con un abogado. **Pendiente de verificar.**

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Generar una pista «rápida» en la terminal y no anotarla | Es justo la que aparecerá en la reclamación |
| Guardar el script pero no el comando ni los parámetros | No se puede regenerar ni demostrar cómo salió |
| No guardar la versión de ffmpeg | La prueba pierde la parte reproducible (§ 135) |
| Fechas en hora local | Dos episodios con la misma marca y ningún orden claro |
| Rehacer una pista y no actualizar el `wav_sha256` | El manifiesto apunta a un audio que ya no es ese |
| Manifiesto que avisa pero no detiene el render | Se ignora a la tercera semana |
| Presentar el historial de git como prueba definitiva | Se defiende con más confianza de la que el indicio aguanta |
| Registrar la pista solo después de la reclamación | La fecha posterior resta, no suma |

## Relacionado

`133` reclamaciones · `135` sintetizar es la garantía · `89` biblioteca de sonido ·
`188` `fuentes.json` como compuerta · `199` el manifiesto del material
