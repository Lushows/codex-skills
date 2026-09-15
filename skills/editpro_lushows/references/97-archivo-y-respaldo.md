# 97 — Archivo y respaldo: qué guardar, qué botar, cuánto cuesta

> Hay dos formas de aprender esto. Una es leer este módulo. La otra es que se te muera el disco con el
> proyecto de un cliente adentro. La segunda enseña más, pero cuesta el cliente.

---

## La regla 3-2-1

Es el estándar de la industria y es simple:

- **3** copias de todo lo que no puedas volver a conseguir
- en **2** tipos de medio distintos (por ejemplo, disco duro externo + nube)
- con **1** copia fuera de tu casa u oficina

Por qué importa cada número:

- **3 copias:** los discos fallan. La probabilidad de que fallen dos a la vez es baja; la de que falle uno
  es alta (los discos mecánicos rondan un 2–5% de fallo anual, y suben con la edad).
- **2 medios:** si guardas todo en discos de la misma marca y del mismo lote, pueden fallar por la misma
  razón al mismo tiempo. Ha pasado.
- **1 fuera de sitio:** robo, incendio, inundación, un rayo que quema la casa entera. Es la copia que te
  salva del desastre físico.

**El material bruto de una grabación es irrepetible.** No puedes volver a grabar el momento. Todo lo demás
—cortes, exportaciones, subtítulos— se puede rehacer. Esa distinción manda todo lo que sigue.

---

## Qué guardar y qué botar

| Cosa | ¿Guardar? | Por cuánto | Por qué |
|---|---|---|---|
| **Material bruto de cámara** | ✅ **SÍ** | Permanente (o mínimo 2 años) | Irrepetible |
| **Audio grabado aparte** | ✅ **SÍ** | Permanente | Irrepetible |
| **Archivo de proyecto** (.prproj, .drp) | ✅ **SÍ** | Permanente | Pesa kilobytes, vale oro |
| **Máster de entrega** (ProRes) | ✅ **SÍ** | 1–2 años | Rehacerlo cuesta horas |
| **Entregas aprobadas** (.mp4) | ✅ **SÍ** | Permanente | Respaldo de lo que entregaste |
| **Subtítulos, guion, notas** | ✅ **SÍ** | Permanente | Pesan nada |
| **Insumos con licencia** (música, LUTs, gráficos) | ✅ **SÍ** | Permanente | Pagaste por ellos |
| **Archivos de caché y previsualizaciones** | ❌ **NO** | — | Se regeneran solos. Pesan GB |
| **Proxies** | ❌ NO | — | Se regeneran del bruto |
| **Exportaciones `wip`** | ❌ NO | Se borran al cerrar | Nadie las va a pedir |
| **Exportaciones `rev` viejas** | ⚠️ Las últimas 2 | 6 meses | Por si el cliente vuelve atrás |
| **Tomas descartadas obviamente malas** | ⚠️ Depende | — | Ver más abajo |
| **Autoguardados del editor** | ❌ NO | — | Basura después de cerrar |

**Sobre las tomas malas:** la tentación es borrar las tomas donde alguien se equivocó. **No las borres en
el primer año.** Razones: (a) los bloopers son contenido que vende y a veces se piden meses después,
(b) una toma "mala" puede tener 2 segundos de b-roll usable, (c) el cliente puede pedir una versión
distinta. Si el espacio aprieta, bótalas **después** de que el proyecto cierre y pase un año.

---

## Cuánto pesa un proyecto de verdad

Números reales para que puedas presupuestar almacenamiento.

### Material bruto por minuto grabado

| Fuente | Peso por minuto |
|---|---|
| Celular 1080p30 (H.264) | ~130 MB |
| Celular 4K30 (HEVC) | ~350 MB |
| iPhone 4K60 ProRes | **~6 GB** |
| Cámara sin espejo 4K30 (H.264) | ~750 MB |
| Cámara 4K con códec de alta tasa (400 Mbps) | ~3 GB |
| Grabación externa ProRes 422 HQ 1080p30 | **~1,3 GB** |
| Grabación externa ProRes 422 HQ 4K30 | **~5,3 GB** |
| Audio WAV 48 kHz 24-bit estéreo | ~17 MB |

### Un proyecto típico, con números

**Reel de 30 segundos, grabado con celular 4K, 45 minutos de material bruto:**

| Componente | Peso |
|---|---|
| Bruto (45 min a 4K HEVC) | 15,7 GB |
| Audio aparte (45 min WAV) | 0,8 GB |
| Insumos (música, gráficos) | 0,3 GB |
| Proyecto + notas + srt | 0,01 GB |
| Máster ProRes (30 s) | 0,7 GB |
| Entregas (5 versiones mp4) | 0,15 GB |
| **Total a archivar** | **~17,7 GB** |
| Caché y proxies (se botan) | 8–20 GB |

**Video corporativo de 5 minutos, dos cámaras, 3 horas de material:**

| Componente | Peso |
|---|---|
| Bruto (2 cámaras × 3 h a 4K) | ~270 GB |
| Audio (2 pistas × 3 h WAV) | ~6 GB |
| Insumos | ~2 GB |
| Máster ProRes 1080p (5 min) | ~6,5 GB |
| Entregas | ~1 GB |
| **Total a archivar** | **~285 GB** |

Traducción: **un disco de 4 TB te da unos 14 proyectos corporativos o unos 200 reels.** Menos de lo que
uno cree.

---

## Cómo bajar el peso del archivo sin perder nada importante

### 1. Bota la caché, siempre

Es la ganancia más grande y más gratuita. Cada editor guarda decenas de GB de caché que se regeneran solos.

- Premiere: `Media Cache Files`, `Media Cache Database`, `Peak Files` (`.pek`)
- DaVinci Resolve: carpeta `CacheClip`, optimized media
- Final Cut: `Render Files`, `Proxy Media` dentro de la Library

Encontrar los grandes desperdicios:
```bash
# Los 20 archivos más pesados de un proyecto
find . -type f -size +100M -exec ls -lh {} \; | sort -k5 -hr | head -20

# Lo que pesa cada carpeta
du -sh */ | sort -hr
```

```powershell
# PowerShell: lo mismo en Windows
Get-ChildItem -Recurse -File | Sort-Object Length -Descending |
  Select-Object -First 20 FullName, @{n='GB';e={[math]::Round($_.Length/1GB,2)}}
```

### 2. Recorta el bruto que jamás vas a usar

Si grabaste 3 horas y usaste 4 minutos, guardar las 3 horas completas puede no tener sentido. La opción
intermedia: **guarda las tomas completas de todo lo que se usó o casi se usó, y bota los descartes
evidentes** (la cámara grabando el piso, la toma donde nadie habló, los 8 minutos de "ya estamos
grabando?").

Cortar un tramo sin recomprimir (rapidísimo, cero pérdida):
```bash
ffmpeg -ss 00:12:30 -to 00:19:45 -i bruto_completo.mp4 -c copy tramo_usado.mp4
```

Con `-c copy` el corte cae en el fotograma clave más cercano, así que puede quedar hasta 2 segundos
corrido. **Deja margen de 5 segundos a cada lado** y no vas a tener problema.

### 3. Archiva el bruto en un códec más eficiente (con cuidado)

Un bruto en H.264 de cámara puede reencodarse a HEVC y bajar ~45% de peso. **Pero es recompresión: pierdes
calidad.** Solo hazlo cuando:

- El proyecto ya está cerrado y entregado
- Es material que probablemente nunca vuelvas a editar en serio
- Lo mediste con VMAF y da ≥95

```bash
ffmpeg -i bruto.mp4 -c:v libx265 -crf 20 -preset slow \
  -pix_fmt yuv420p -c:a copy -tag:v hvc1 bruto_archivo.mp4
```

El `-tag:v hvc1` es necesario para que Apple lo reproduzca.

**Mi consejo honesto: no lo hagas para material de cliente.** Los discos son más baratos que el arrepentimiento.

### 4. Comprime el proyecto entero en un solo paquete

Para archivo frío, mete todo en un contenedor. Los videos ya están comprimidos, así que la ganancia es
mínima, pero **tener un solo archivo hace la copia mucho más rápida y confiable** que 8.000 archivos
sueltos:

```bash
tar -czf gastro_calc-reel01_archivo_2026-08-04.tar.gz gastro_calc-reel01/
```

---

## Verificar que el respaldo sirve

Esta es la parte que nadie hace y es la que importa. **Un respaldo que no verificaste no es un respaldo,
es una esperanza.**

### Sumas de verificación (checksums)

Una suma de verificación es una huella digital del archivo. Si el archivo se corrompió al copiarse, la
huella cambia.

```bash
# Al archivar: genera las huellas de todo
find . -type f -exec sha256sum {} \; > ARCHIVO.sha256

# Meses después: verifica que todo sigue intacto
sha256sum -c ARCHIVO.sha256
```

```powershell
# PowerShell
Get-ChildItem -Recurse -File | ForEach-Object {
  "$((Get-FileHash $_.FullName -Algorithm SHA256).Hash)  $($_.FullName)"
} | Out-File -Encoding utf8 ARCHIVO.sha256
```

Si algo salió corrompido, `sha256sum -c` te lo dice archivo por archivo. Sin eso, te enteras el día que
intentas abrir el video y no abre.

### Verificar que los videos no están rotos

Un archivo puede tener el tamaño correcto y estar dañado adentro. Este comando lo decodifica entero y
reporta errores:

```bash
ffmpeg -v error -i video.mp4 -f null - 2>errores.txt
# Si errores.txt está vacío, el archivo está sano
```

Para verificar una carpeta completa:
```bash
for f in *.mp4 *.mov; do
  err=$(ffmpeg -v error -i "$f" -f null - 2>&1 | head -3)
  if [ -n "$err" ]; then echo "❌ $f: $err"; else echo "✅ $f"; fi
done
```

### La prueba de restauración

Una vez cada tanto (cada tres meses está bien), **agarra un proyecto archivado al azar y ábrelo**. Si el
proyecto se relinkea y reproduce, tu sistema funciona. Si no, mejor descubrirlo ahora que cuando el
cliente lo pida.

---

## Dónde guardar: opciones y costos reales

| Medio | Costo aproximado por TB | Bueno para | Malo para |
|---|---|---|---|
| **Disco externo mecánico** | US$18–25 | Archivo grande y barato | Golpes, viajes, largo plazo sin uso |
| **SSD externo** | US$60–80 | Trabajo activo, velocidad | Costo por TB, archivo largo plazo |
| **NAS (2+ discos en espejo)** | US$150+ el equipo, más discos | Archivo local con redundancia | Incendio/robo (está en tu casa) |
| **Nube de sincronización** (Drive, Dropbox) | US$100–120/año por 2 TB | Copia fuera de sitio, compartir | Costo a gran escala |
| **Nube de archivo frío** (Backblaze B2, S3 Glacier) | US$6–72/año por TB | Archivo profundo, barato | Costo y demora al recuperar |
| **Backblaze Personal** | ~US$99/año **ilimitado** | Respaldo continuo de un computador | Solo respalda discos conectados |

**Un montaje realista para alguien que edita solo:**

1. **Disco de trabajo (SSD)** — proyecto activo. Rápido, se vacía al cerrar el proyecto.
2. **Disco de archivo (mecánico 8–16 TB)** — proyectos cerrados. Copia 1.
3. **Segundo disco de archivo idéntico** — copia 2, se sincroniza cada semana. Guardado en otro lugar.
4. **Nube fría (B2 o similar)** — copia 3, solo el bruto irremplazable y las entregas aprobadas.

Costo real: unos US$400 de discos una vez + unos US$60–150 al año de nube. **Contra perder un proyecto de
cliente, es gratis.**

Sincronizar los discos sin copiar lo que ya está:
```bash
rsync -av --progress /Volumes/ARCHIVO1/ /Volumes/ARCHIVO2/
```
```powershell
robocopy "D:\ARCHIVO" "E:\ARCHIVO" /MIR /R:2 /W:5 /LOG:sync.log
```
Cuidado con `/MIR`: **borra en el destino lo que no está en el origen.** Es lo que quieres para un espejo,
y es un desastre si te equivocas de orden.

---

## Verdades sobre los medios que casi nadie sabe

- **Un disco mecánico desconectado se degrada.** Los cojinetes se pegan y los sectores se desmagnetizan. Un
  disco guardado en un cajón 5 años puede no arrancar. **Conéctalos y léelos al menos una vez al año.**
- **Un SSD desconectado pierde datos más rápido que un mecánico.** La carga de las celdas se fuga. **Los
  SSD no son medio de archivo a largo plazo.** Sirven para trabajar, no para guardar.
- **La nube de sincronización no es respaldo.** Si borras un archivo, se borra en la nube también. Los
  servicios guardan versiones 30 días y ya. Respaldo de verdad es una copia que **no se sincroniza**.
- **El ransomware sigue las unidades conectadas.** Si tu disco de respaldo está siempre enchufado, se cifra
  con el resto. Una copia debe estar **desconectada**.

---

## Cerrar un proyecto: el ritual

Cuando el cliente aprueba y publica, haz esto de una vez y no lo dejes para después:

```bash
PROY="gastro_calc-reel01"

# 1. Borra caché, proxies y autoguardados
rm -rf $PROY/03_proyecto/autoguardado/*
rm -rf $PROY/04_export/wip/*
find $PROY -name "*.pek" -delete
find $PROY -name "CacheClip" -type d -exec rm -rf {} +

# 2. Verifica que todos los videos están sanos
find $PROY -name "*.mp4" -o -name "*.mov" | while read f; do
  err=$(ffmpeg -v error -i "$f" -f null - 2>&1 | head -2)
  [ -n "$err" ] && echo "❌ $f"
done

# 3. Genera las huellas
cd $PROY && find . -type f -exec sha256sum {} \; > ARCHIVO.sha256 && cd ..

# 4. Escribe el README de cierre
cat > $PROY/LEEME.txt <<'EOF'
Proyecto: gastro_calc-reel01
Cliente: GastroLatam
Cerrado: 2026-08-04
Versión aprobada: v05
Máster: 04_export/apro/gastro_calc-reel01_master_v05_apro.mov
Editor usado: DaVinci Resolve 20
Música: "Nombre" — licencia Epidemic Sound, ID XXXX, vigente hasta 2027-03
Notas: el cliente pidió mantener el gancho tal cual en futuras versiones.
EOF

# 5. Mira cuánto pesa
du -sh $PROY

# 6. Copia a los dos discos de archivo
rsync -av --progress $PROY/ /Volumes/ARCHIVO1/$PROY/
rsync -av --progress $PROY/ /Volumes/ARCHIVO2/$PROY/
```

Ese `LEEME.txt` con la **licencia de la música y su vencimiento** te salva de un reclamo de derechos dos
años después. Anótalo siempre.

---

## Errores comunes

1. **Tener una sola copia.** No es respaldo, es una apuesta.
2. **Las tres copias en el mismo cuarto.** Un incendio o un robo se lleva las tres.
3. **Creer que Google Drive es respaldo.** Es sincronización: si borras, borra. Si un virus cifra, cifra.
4. **Respaldar en SSD para el largo plazo.** Pierde carga desconectado. Los SSD son para trabajar.
5. **Nunca verificar el respaldo.** El 100% de los respaldos funcionan hasta que los necesitas.
6. **Archivar la caché junto con el proyecto.** Puedes estar guardando 20 GB de basura regenerable por
   proyecto.
7. **Botar el bruto para ahorrar espacio.** Es lo único irrepetible del proyecto entero.
8. **Guardar solo el `.mp4` de entrega y no el máster ni el proyecto.** El día que pidan un cambio de una
   palabra, hay que rehacer todo.
9. **Dejar el disco de respaldo siempre conectado.** El ransomware se lo lleva con el resto.
10. **No anotar la licencia de la música.** Dos años después no sabes si puedes reutilizar la pieza.
11. **Comprimir el bruto a HEVC "para ahorrar" antes de que el proyecto cierre.** Pérdida irreversible en
    material que todavía puedes necesitar.
12. **Usar `robocopy /MIR` o `rsync --delete` con el origen y el destino invertidos.** Borra el archivo
    bueno con el vacío. Revisa dos veces antes de dar enter.

---

## Checklist

Al cerrar y archivar cualquier proyecto:

- [ ] Caché, proxies, autoguardados y exportaciones `wip` **eliminados**
- [ ] El **material bruto completo** está guardado y sin renombrar
- [ ] El **archivo de proyecto** del editor está guardado
- [ ] El **máster** de la versión aprobada está guardado
- [ ] Las **entregas aprobadas** (`apro`) están guardadas
- [ ] Guion, notas, `.srt` y registro de versiones incluidos
- [ ] Todos los videos verificados con `ffmpeg -v error -f null -` sin errores
- [ ] Sumas SHA-256 generadas y guardadas junto al proyecto
- [ ] `LEEME.txt` escrito: cliente, fecha, versión aprobada, editor usado, **licencias de música con
      vencimiento**
- [ ] **Tres copias** en **dos medios**, con **una fuera de sitio** (regla 3-2-1)
- [ ] Al menos una copia está **desconectada** del computador
- [ ] Anoté cuánto pesa el proyecto archivado
- [ ] Cada tres meses: abro un proyecto archivado al azar y **compruebo que restaura**
- [ ] Cada año: conecto y leo los discos de archivo para que no se degraden
