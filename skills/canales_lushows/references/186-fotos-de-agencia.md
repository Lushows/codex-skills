# 186 · Fotos de agencia: la línea roja

**Qué resuelve:** reconocer material de Getty Images, AP, Reuters, AFP, EFE o
Shutterstock **aunque llegue recortado, sin marca de agua y alojado en una web
pública**. Es la única categoría del manual sin matices: no entra nunca.

> ⚠️ **Esto no es asesoría legal.** Es la línea roja de producción del canal.

---

## Por qué línea roja y no «riesgo alto»

Las agencias viven de licenciar imagen: tienen la foto catalogada con identificador,
fecha y fotógrafo, medios dedicados a encontrar usos no licenciados y una vía estándar
para reclamar. No hay lectura benévola de un documental monetizado que usa su material
sin licencia. Y al revés de lo que mucha gente cree, **recortar, virar el color o añadir
grano no mejora nada**: nuestro collage transforma la pieza hasta que no se reconoce,
y eso no cambia el derecho; solo hace pensar que se hizo para esconderlo.

## Cómo se reconocen

**Por la marca de agua.** Getty superpone trama y texto en diagonal; AP, Reuters, AFP y
EFE estampan crédito en una esquina o al pie. Si se ve, cae ahí mismo.

**Por el vocabulario del pie**, que sobrevive al recorte porque vive en el texto:

| Marca en el pie o la ficha | Significado |
|---|---|
| `Getty Images`, `AP Photo`, `REUTERS/…`, `AFP`, `EPA`, `EFE` | Agencia: descarte directo |
| `Shutterstock`, `Alamy`, `Adobe Stock`, `iStock` | Banco de pago |
| `handout` | Foto entregada por una institución a la prensa, con sus condiciones |
| `pool photo` | Compartida entre medios acreditados. No es libre |
| `courtesy of` | Cesión a **ese** medio, no al mundo |
| `via <medio>` | La cadena pasa por un tercero que no cedió nada |
| `editorial use only` | Prohibido comercialmente: justo nuestro caso |
| `stringer`, `contributor` | Fotógrafo de agencia |

**Este vocabulario también aparece en webs `.gov`.** Es exactamente el borde nº 4 del
§ 182: una agencia federal publica una foto de agencia y el dominio engaña.

**Por la forma del archivo:** identificador de catálogo en el nombre (`gettyimages-`,
`RTX…`, cadenas de 8–12 dígitos), restos de trama o texto borroso en los bordes tras un
recorte apresurado, crédito incrustado en los metadatos. Tres señales juntas bastan.

## El olfateador de metadatos

```python
# -*- coding: utf-8 -*-
# OLFATO DE AGENCIA · no prueba nada: LEVANTA LA MANO para que mire un humano.
import os, re, sys
from PIL import Image

# Texto de campos EXIF: aqui se puede ser fino.
AGENCIAS = re.compile(
    r"getty|associated\s*press|\bap\s*photo\b|reuters|\bafp\b|\befe\b|\bepa\b|"
    r"shutterstock|alamy|adobe\s*stock|istock|depositphotos|corbis|"
    r"editorial\s*use|handout|pool\s*photo|courtesy\s*of|stringer", re.I)
# Barrido del binario: SOLO cadenas largas e inequivocas (ver la trampa de abajo).
EN_CRUDO = re.compile(
    r"getty|associated\s*press|reuters|shutterstock|alamy|adobe\s*stock|"
    r"istock|depositphotos|corbis|editorial\s*use|pool\s*photo|courtesy\s*of", re.I)
CAMPOS = {315: "Artist", 33432: "Copyright", 270: "ImageDescription",
          40091: "XPTitle", 40093: "XPAuthor"}

def olfatear(ruta):
    avisos = []
    try:
        exif = Image.open(ruta).getexif() or {}
    except Exception as e:
        return [f"no se pudo abrir: {e}"]
    for tag, nombre in CAMPOS.items():
        v = exif.get(tag)
        if isinstance(v, bytes):
            v = v.decode("utf-16-le" if tag >= 40091 else "latin1", "ignore")
        if v and AGENCIAS.search(str(v)):
            avisos.append(f"EXIF {nombre}: {str(v)[:90]}")
    # IPTC/XMP van crudos dentro del JPEG: se leen las cadenas imprimibles largas
    crudo = open(ruta, "rb").read(300_000).decode("latin1", "ignore")
    for cadena in re.findall(r"[ -~]{6,}", crudo):
        for m in set(EN_CRUDO.findall(cadena)):
            avisos.append(f"cadena en metadatos: {m}")
    if AGENCIAS.search(os.path.basename(ruta)):
        avisos.append("el nombre del archivo nombra una agencia")
    return sorted(set(avisos))

if __name__ == "__main__":
    sucias = 0
    for r in sys.argv[1:]:
        a = olfatear(r)
        if a:
            sucias += 1
            print(f"\n  ! {os.path.basename(r)}")
            for x in a:
                print(f"      {x}")
    print(f"\n  {sucias}/{len(sys.argv)-1} archivo(s) con olor a agencia")
    sys.exit(1 if sucias else 0)
```

## Dos lecciones medidas sobre el archivo real del piloto

**1 · Las siglas cortas son inservibles contra el binario.** La primera versión buscaba
`\bap\b` dentro de los bytes del JPEG: marcó **72 de 80 archivos**, porque un fichero
comprimido contiene «ap» por azar. Limitando el barrido en crudo a cadenas largas e
inequívocas sobre secuencias imprimibles de seis o más caracteres, la señal baja a
**2 de 81**: eso ya es una lista que alguien mira.

**2 · El aviso que quedó es un falso positivo perfecto.** La foto de la Torre Eiffel en
construcción de Durandelle lleva en sus metadatos *«The J. Paul Getty Museum, Los
Angeles»*: es el **museo Getty**, no Getty Images. La pieza está en Commons, en dominio
público, y es legítima. Por eso el script **avisa y no descarta**: un filtro que
decidiera solo habría tirado una de las mejores piezas del episodio.

Y la advertencia contra la falsa confianza: **un resultado limpio no absuelve.** Los
metadatos se borran al reencodear y todo el archivo pasa por reprocesado.

## Cuando la única foto buena es de agencia

Salidas, en orden: **el documento** (acta, sentencia, registro: suele ser federal y más
fuerte narrativamente); **el lugar hoy**, rotulado con la fecha; **un retrato oficial
libre** (comparecencia, ficha policial); **reconstrucción propia**, siempre rotulada; o
**que ese plano no exista** — un rótulo, una cifra, un plano de descanso (§ 16).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Recortar la marca de agua | Uso no licenciado **y** agravante de intencionalidad |
| «Es un recorte pequeño, no se reconoce» | El derecho no depende del tamaño del recorte |
| Tomar por libre una foto de agencia en una web `.gov` | El borde clásico del § 182 |
| Ignorar `handout`, `pool`, `courtesy of` | Vocabulario de prensa: nunca es cesión al mundo |
| Buscar siglas cortas dentro del binario | 72 de 80 falsos positivos: el aviso se vuelve ruido |
| Dejar que el script descarte solo | Habría tirado la Durandelle por decir «Getty Museum» |
| Fiarse de que los metadatos salgan limpios | Se borran al reencodear: no absuelven |

## Relacionado

`182` obra del gobierno federal · `185` lo que parece libre y no lo es ·
`187` fotogramas de película · `188` `fuentes.json` como compuerta ·
`189` defender un episodio
