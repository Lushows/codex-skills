# 96 — Versiones y nomenclatura: no volver a perderse

> `final_FINAL_v2_bueno_ESTE_SI.mp4` no es un chiste de internet: es el síntoma de un sistema que no
> existe. Y cuesta dinero real —en horas perdidas, en reexportaciones y en el día que le mandas al cliente
> la versión equivocada.

---

## El problema, dicho sin rodeos

Un proyecto de video normal genera, sin exagerar:

- 3 a 8 cortes distintos antes de aprobación
- 2 a 5 versiones por plataforma de cada corte aprobado
- 3 a 10 variantes de gancho si va a pauta
- 2 a 4 rondas de correcciones del cliente

Eso son **fácilmente 40 archivos** para un solo video de 30 segundos. Sin sistema, a la semana 2 no sabes
cuál es cuál y terminas abriendo todos para ver.

Peor: **el día que el cliente diga "prefiero la versión de antes", tienes que poder encontrarla en 10
segundos.** Si no puedes, quedas mal o la rehaces gratis.

---

## Las tres reglas que resuelven el 90%

### Regla 1 — La palabra "final" está prohibida

No existe. No la escribas. La versión final no se llama final: se llama **v05** y está marcada como
aprobada en otra parte.

En el momento en que escribes "final", garantizas que va a haber un "final2". Es una ley de la naturaleza.

### Regla 2 — Los números llevan cero delante

`v01`, `v02`, ... `v10`, `v11`.

Sin el cero, el computador ordena así: `v1, v10, v11, v2, v3`. Con el cero, ordena bien. Es una tontería
que te ahorra irritación diaria.

Lo mismo con las fechas: **siempre `AAAA-MM-DD`**. `2026-08-04`, no `4-ago-26` ni `04/08/2026`. Es el único
formato que se ordena solo alfabéticamente y el único que no se confunde entre día y mes.

### Regla 3 — El nombre se lee sin abrir el archivo

Si necesitas abrir el archivo para saber qué es, el nombre está mal.

---

## El esquema de nombres

```
PROYECTO_PIEZA_PLATAFORMA_vNN_ESTADO.ext
```

Ejemplos reales:

```
gastro_calc-reel01_ig9x16_v03_rev.mp4
gastro_calc-reel01_ig9x16_v05_apro.mp4
gastro_calc-reel01_tiktok_v05_apro.mp4
gastro_calc-reel01_wa720_v05_apro.mp4
gastro_calc-reel01_master_v05_apro.mov
```

Piezas del nombre:

| Parte | Qué es | Ejemplos |
|---|---|---|
| **PROYECTO** | Cliente o marca, corto | `gastro`, `bioseta`, `avispao` |
| **PIEZA** | Qué video es | `calc-reel01`, `testimonio-ana`, `demo-app` |
| **PLATAFORMA** | Destino y formato | `ig9x16`, `ig4x5`, `tiktok`, `yt1080`, `wa720`, `master` |
| **vNN** | Versión, con cero delante | `v01`, `v07` |
| **ESTADO** | En qué punto está | `wip`, `rev`, `apro`, `pub` |

**Estados, y qué significan exactamente:**

| Estado | Significado | Quién lo pone |
|---|---|---|
| `wip` | *Work in progress.* No se le muestra a nadie | Tú |
| `rev` | Listo para que el cliente lo revise | Tú, al mandarlo |
| `nota` | Tiene comentarios pendientes de aplicar | Tú, al recibir feedback |
| `apro` | Aprobado por el cliente. **Congelado, no se toca** | Tú, cuando el cliente aprueba **por escrito** |
| `pub` | Publicado. Es lo que está en vivo | Tú, después de publicar |

**Nunca borres un `apro`.** Es el archivo que respalda "esto fue lo que aprobaste".

Reglas de forma:
- **Todo en minúsculas.** Windows no distingue mayúsculas, Linux sí, y las nubes se comportan de las dos
  formas. Minúsculas siempre y no tienes el problema.
- **Sin espacios.** Usa `_` para separar campos y `-` dentro de un campo. Los espacios rompen comandos de
  terminal y URLs.
- **Sin tildes ni ñ en nombres de archivo.** `campaña` se convierte en basura en algún sistema en algún
  momento. Escribe `campana` y sigue.
- **Sin caracteres raros.** Nada de `#`, `%`, `&`, `:`, `/`.

---

## Cuándo sube el número de versión

Esta es la parte que la gente hace mal. La regla es simple:

**La versión sube cuando el archivo sale de tus manos.**

- Haces 40 cambios sin mostrárselos a nadie → sigue siendo la misma versión
- Se lo mandas al cliente → **v03**
- El cliente pide cambios, los haces, se lo vuelves a mandar → **v04**

Así, "v04" significa literalmente "la cuarta vez que viste esto". El cliente y tú hablan el mismo idioma y
"lo que me mandaste el martes" se vuelve "la v04".

**Sub-versiones (`v03a`, `v03b`):** solo para variantes paralelas de la misma versión, no para
correcciones. Ejemplo legítimo: tres ganchos distintos sobre el mismo cuerpo para probar en pauta →
`v05a-gancho-precio`, `v05b-gancho-error`, `v05c-gancho-pregunta`.

---

## Estructura de carpetas

```
gastro_calc-reel01/
├── 01_bruto/            ← Material original. NUNCA se modifica ni se renombra
│   ├── camara/
│   ├── audio/
│   └── recibido/        ← lo que mandó el cliente
├── 02_insumos/          ← Música, gráficos, logos, tipografías, LUTs
├── 03_proyecto/         ← Archivos del editor (.prproj, .drp, proyecto CapCut)
│   └── autoguardado/
├── 04_export/
│   ├── wip/             ← Borradores tuyos. Se puede vaciar sin culpa
│   ├── rev/             ← Lo que le mandaste al cliente
│   └── apro/            ← Aprobados. INTOCABLES
├── 05_entrega/          ← Lo que se le entrega al cliente, con su README
└── 06_notas/            ← Feedback, guion, transcripciones, .srt
```

**Los números delante de las carpetas** son para que se ordenen en el orden en que las usas, no
alfabéticamente. Vale para carpetas y para archivos.

**`01_bruto` es sagrado.** Nunca renombres, muevas ni edites nada ahí adentro. Si necesitas convertir algo,
la conversión sale a otra carpeta. El día que necesites volver al original, tiene que estar exactamente
como llegó.

---

## El registro de versiones

Un archivo de texto plano en la raíz del proyecto. Treinta segundos por versión, y te salva la vida:

`06_notas/versiones.md`

```markdown
# gastro_calc-reel01 — registro

## v05 — 2026-08-04 — APROBADO
Corte de 34 s. Gancho "tu plato estrella te está quebrando".
Se acortó el bloque del medio 2,1 s. Música bajada 3 dB bajo la voz.
Verificación de audio corrida: limpia (ver 98).
Aprobado por Luis por WhatsApp 2026-08-04 16:22.
Exportados: ig9x16, ig4x5, tiktok, wa720, master ProRes.

## v04 — 2026-08-03 — con notas
Notas del cliente:
- "el precio se ve muy poco tiempo" → APLICADO en v05 (3,2 s en pantalla)
- "la música tapa la voz al final" → APLICADO en v05
- "me gusta el gancho, no lo toques" → respetado

## v03 — 2026-08-02 — revisión
Primera versión con subtítulos quemados. Duración 41 s.
Cliente pidió acortar.

## v02 — 2026-08-01 — interno
Prueba de dos ganchos distintos. Se escogió el B.

## v01 — 2026-07-31 — interno
Ensamblaje bruto. 1:12. Sin música ni texto.
```

Con eso, seis meses después sabes exactamente qué pasó, qué pidió el cliente y por qué el video quedó como
quedó. Y si el cliente vuelve con "hagamos otro igual al de agosto", tienes la receta.

---

## Comandos útiles para no perderte

**Ver qué exportaste, ordenado por fecha:**
```bash
ls -lht 04_export/ | head -20
```

**Comparar dos versiones para ver qué cambió técnicamente:**
```bash
for f in v04.mp4 v05.mp4; do
  echo "=== $f ==="
  ffprobe -v error -show_entries format=duration,size,bit_rate \
    -show_entries stream=codec_name,width,height,r_frame_rate \
    -of default=noprint_wrappers=1 "$f"
done
```

**Renombrar en lote** (si heredaste un desastre):
```bash
# Bash: pasar todo a minúsculas y cambiar espacios por guion bajo
for f in *.mp4; do
  nuevo=$(echo "$f" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
  [ "$f" != "$nuevo" ] && mv -- "$f" "$nuevo"
done
```

```powershell
# PowerShell: lo mismo en Windows
Get-ChildItem *.mp4 | ForEach-Object {
  $nuevo = $_.Name.ToLower() -replace ' ', '_'
  if ($_.Name -cne $nuevo) { Rename-Item $_.FullName $nuevo }
}
```

**Marcar la versión dentro del archivo** para que el borrador se identifique solo aunque alguien lo
renombre:
```bash
ffmpeg -i corte.mp4 -vf "drawtext=text='v04 REVISION — NO PUBLICAR':\
fontcolor=white@0.75:fontsize=28:box=1:boxcolor=black@0.5:x=20:y=h-60" \
  -c:v libx264 -crf 24 -preset veryfast -pix_fmt yuv420p -c:a copy \
  04_export/rev/gastro_calc-reel01_ig9x16_v04_rev.mp4
```

Esa marca de agua en los borradores es **oro**: evita que un borrador termine publicado por error, que
pasa más de lo que crees.

**Poner la versión en los metadatos también:**
```bash
ffmpeg -i entrada.mp4 -c copy \
  -metadata title="gastro_calc-reel01 v05 APROBADO" \
  -metadata comment="Aprobado 2026-08-04. Máster: 04_export/apro/..._master_v05_apro.mov" \
  salida.mp4
```

---

## Usar git para los archivos de proyecto (opcional pero potente)

Los archivos de proyecto de los editores (`.prproj`, `.drp`, `.fcpxml`, los JSON de CapCut) son archivos
pequeños. **Se pueden versionar con git** aunque los videos no.

```bash
cd gastro_calc-reel01
git init
cat > .gitignore <<'EOF'
01_bruto/
02_insumos/
04_export/
05_entrega/
*.mp4
*.mov
*.wav
*.mxf
03_proyecto/autoguardado/
EOF
git add .
git commit -m "v01 — ensamblaje bruto"
```

Ventaja real: puedes volver al estado exacto del proyecto de hace tres versiones sin guardar 12 copias del
archivo. Los archivos de proyecto pesan kilobytes.

Limitación honesta: git no puede **fusionar** archivos de proyecto binarios. Sirve para volver atrás, no
para trabajar en equipo sobre el mismo corte.

---

## Errores comunes

1. **Escribir "final".** Garantiza el "final2". Usa números y estados.
2. **Números sin cero delante.** `v10` termina ordenado antes de `v2` y te confunde a diario.
3. **Fechas en formato local.** `4-8-26` puede ser 4 de agosto o 8 de abril según quién lo lea.
4. **Espacios y tildes en los nombres.** Rompen comandos, URLs y sistemas de nube.
5. **Renombrar archivos dentro de `01_bruto`.** El día que el proyecto se relinke, nada calza.
6. **Subir la versión por cada guardado.** La versión sube cuando el archivo **sale**, no cuando lo tocas.
7. **Borrar los aprobados para ahorrar espacio.** Son tu respaldo contractual. Se guardan.
8. **No llevar registro de qué cambió.** A los dos meses no recuerdas por qué la v04 se descartó y repites
   el error.
9. **Mandar borradores sin marca de agua.** Un borrador se publica por error con una facilidad
   sorprendente.
10. **Guardar todo en el escritorio.** No tiene estructura, no se respalda y se pierde con la primera
    reinstalación.
11. **Usar el mismo nombre para versiones distintas de plataformas distintas.** `reel.mp4` en cuatro
    carpetas es cuatro bombas de tiempo.
12. **No anotar quién aprobó y cuándo.** Cuando el cliente diga "yo nunca aprobé eso", necesitas la fecha
    y el medio.

---

## Checklist

Al arrancar un proyecto y al cerrar cada versión:

- [ ] Estructura de carpetas `01_bruto` … `06_notas` creada antes de empezar
- [ ] `01_bruto` tiene el material original **sin renombrar ni modificar**
- [ ] Ningún nombre de archivo contiene la palabra "final"
- [ ] Todos los nombres siguen `PROYECTO_PIEZA_PLATAFORMA_vNN_ESTADO.ext`
- [ ] Todo en **minúsculas, sin espacios, sin tildes**
- [ ] Los números de versión llevan **cero delante** (`v03`, no `v3`)
- [ ] Las fechas están en **`AAAA-MM-DD`**
- [ ] La versión sube **solo cuando el archivo sale** hacia el cliente
- [ ] Los borradores llevan **marca de agua** con la versión
- [ ] Cada versión que sale tiene su entrada en `06_notas/versiones.md`
- [ ] Los archivos `apro` están en su carpeta y **nadie los sobrescribe**
- [ ] La aprobación quedó registrada con **fecha, hora y medio**
- [ ] El máster de la versión aprobada está identificado en el registro
