# 64 · Mapas y rutas

**Qué resuelve:** el mapa es el recurso que más se usa mal en este nicho. Aquí está
cómo se traza una ruta que se dibuja sola, cómo late un punto, de dónde salen las
fronteras sin pisar una licencia — y la regla que evita el error factual más caro.

---

## 🔴 La regla que va primero: el mapa debe ser el lugar del que habla la voz

**Ocurrió en el piloto.** Se puso un mapa rotulado "Altiplano" mientras la locución
hablaba del penal del Altiplano, en México. El mapa era el **altiplano andino**. Nadie
lo notó hasta la revisión: se veía bien, tenía relieve, tenía rótulo, y era otro
continente.

Un canal de documentales vive de que lo que se ve confirme lo que se oye. Un mapa
equivocado no es un fallo estético: es la prueba en pantalla de que no verificamos.

**El protocolo, sin excepciones:**

1. El mapa se elige **por coordenadas**, no por nombre. Los topónimos se repiten entre
   países; las coordenadas no.
2. Las coordenadas se anotan en `archivo/fuentes.json` junto a la pieza.
3. El rótulo lleva **el nombre exacto y el país**: `ALTIPLANO · EDO. DE MÉXICO`.
4. Antes de renderizar, leer en voz alta la frase del guion mirando el mapa. Si hay que
   explicar por qué encaja, no encaja.

## De dónde salen las fronteras

| Sí | No |
|---|---|
| **Natural Earth** — dominio público, `.geojson` de países, estados y costas | Captura de Google Maps, Bing o Apple: son obra con licencia |
| Trazado propio dibujado sobre una referencia | Mapa "encontrado en internet" sin licencia verificada |
| Mapa esquemático inventado a propósito y **rotulado como esquema** | Un esquema presentado como mapa real |

Un GeoJSON se convierte en `path` de SVG con una proyección sencilla. Para un plano de
región basta la equirectangular con corrección de latitud:

```python
import io, json, math

def a_path(geojson, w=1400, h=900, pad=40):
    """GeoJSON -> atributo 'd' de un <path>. Equirectangular con corrección de latitud."""
    datos = json.load(io.open(geojson, encoding="utf-8"))
    anillos = []
    for f in datos["features"]:
        g = f["geometry"]
        pols = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for pol in pols:
            anillos.extend(pol)
    pts = [c for a in anillos for c in a]
    lats = [c[1] for c in pts]
    k = math.cos(math.radians(sum(lats) / len(lats)))   # corrige la longitud
    xs = [c[0]*k for c in pts]
    x0, x1, y0, y1 = min(xs), max(xs), min(lats), max(lats)
    s = min((w - 2*pad) / (x1 - x0), (h - 2*pad) / (y1 - y0))
    d = []
    for a in anillos:
        p = [(pad + (c[0]*k - x0)*s, h - pad - (c[1] - y0)*s) for c in a]
        d.append("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in p) + " Z")
    return " ".join(d)
```

Estilo del canal: relleno `#1B2A22` al 55%, borde `#E6DCC4` de 2 px al 40%. El mapa es
**cama**, no plano: si compite con el recorte, sobra (`50`).

## La ruta que se traza sola

`stroke-dasharray` deja dibujar el trazo hasta una fracción exacta, y a diferencia del
`crop` funciona aunque la ruta vuelva sobre sí misma. La longitud del trazo la calcula
la propia página y el estado llega por el `#hash` de la URL:

```html
<!doctype html><meta charset='utf-8'>
<style>html,body{margin:0;background:transparent;width:1400px;height:900px}</style>
<svg width="1400" height="900">
  <path id="ruta" d="M180 720 C 420 640, 520 420, 760 380 S 1120 300, 1250 190"
        stroke="#E3120B" stroke-width="9" fill="none"
        stroke-linecap="round" stroke-linejoin="round"/>
</svg>
<script>
  const p = document.getElementById('ruta'), L = p.getTotalLength();
  const f = parseFloat(location.hash.slice(1) || 0);
  p.style.strokeDasharray  = L;
  p.style.strokeDashoffset = L * (1 - f);
</script>
```

Y la serie se genera llamando a Chrome una vez por estado:

```python
N = 20
for i in range(N):
    f = i / (N - 1)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--no-sandbox", f"--user-data-dir={PERFIL}", "--no-first-run",
                    "--default-background-color=00000000",
                    "--virtual-time-budget=1200", "--window-size=1400,900",
                    f"--screenshot=fx/ruta_{i:02d}.png",
                    f"file:///{RUTA_HTML}#{f:.4f}"], capture_output=True, timeout=120)
```

Se encadena con `cadena_serie` (`61`). **Duración total 1,2-2,0 s** para un tramo, con
`paso ≈ dur/N`. Una ruta que tarda más de 2,5 s en dibujarse se vuelve pantalla de
espera.

**La ruta no lleva punta de flecha animada.** El extremo del trazo ya indica el avance;
la flecha que persigue la línea es de plantilla (`68`).

## El punto que late

Tres estados —anillo pequeño, medio, grande y desvanecido— repetidos en ciclo. El
latido va a **0,9-1,1 s por ciclo**, cerca del pulso humano; más rápido pone nervioso.

```python
def punto(i, n=3, w=220):
    r, op = 18 + i*34, 0.85 - i*0.28
    return (w, w, f"""
<div style="position:relative;width:{w}px;height:{w}px">
  <div class="l" style="left:{w//2-r}px;top:{w//2-r}px;width:{2*r}px;height:{2*r}px;
       border:3px solid #E3120B;border-radius:50%;opacity:{op:.2f}"></div>
  <div class="l" style="left:{w//2-9}px;top:{w//2-9}px;width:18px;height:18px;
       border-radius:50%;background:#E3120B"></div>
</div>""")
```

El núcleo sólido **no cambia de tamaño** entre estados: si late el punto y el anillo a
la vez, se lee como icono de aplicación. Late el anillo; el punto se queda.

Todo punto lleva su rótulo pegado, con el nombre del lugar y —cuando aporta— la fecha.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Elegir el mapa por topónimo | El altiplano andino ilustrando un penal mexicano |
| Captura de Google Maps | Obra con licencia: reclamo y episodio caído |
| Mapa sin rótulo de país | El espectador no sabe dónde está y desconecta |
| Ruta revelada con `crop` cuando vuelve sobre sí misma | Se dibuja en el orden equivocado |
| Trazado de más de 2,5 s | Deja de ser gesto y pasa a ser espera |
| Punta de flecha persiguiendo la ruta | Efecto de plantilla |
| Latido más rápido de 0,8 s | Inquieta en vez de señalar |
| Mapa con demasiado detalle | Compite con el collage: el mapa es cama |

## Relacionado

`54` fondos de datos · `61` `cadena_serie` · `65` diagramas · `96` verificación de datos · `43` rótulos
