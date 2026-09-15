# Automatizar la investigación

> Vigencia: 14-sep-2026. Automatiza lo repetitivo. **No automatices el criterio.**

## Qué se puede automatizar y qué no

| Se automatiza bien | No se automatiza |
|---|---|
| Volcar catálogos y comparar semana a semana | Decidir si un producto vale la pena |
| Vigilar precios de 5 competidores | Formular el ángulo (`96`) |
| Recibir avisos de menciones nuevas | Leer y clasificar comentarios (`95`) |
| Archivar capturas con fecha | Deconstruir un creativo (`97`) |
| Llevar la serie temporal del radar | La conclusión del informe (`109`) |

Regla: automatiza la **recolección**; conserva el **juicio**.

## Nivel 1 — Alertas (30 min de montaje, cero mantenimiento)

| Herramienta | Qué monta | Señal que da |
|---|---|---|
| **Google Alerts** | `"producto" comprar México`, `"marca competidor"` | Menciones nuevas, notas de prensa, listados |
| **Google Trends** con correo | Términos de tu nicho, región México | Subidas de interés |
| Suscripción al boletín del competidor | Con un correo aparte | Sus ofertas, sus lanzamientos, su calendario de Buen Fin |
| Seguir sus redes desde una cuenta neutra | | Lanzamientos y creativos nuevos |

El boletín del competidor es el más subestimado: te llega a la bandeja su estrategia de correo
completa, incluidas las secuencias de carrito abandonado y las ofertas de temporada.

## Nivel 2 — Vigilancia de catálogo y precio (script)

Corre esto una vez por semana sobre tus 5 competidores. Guarda un CSV histórico y te dice qué cambió.

```python
#!/usr/bin/env python3
"""Vigilancia semanal de catalogo y precio de tiendas Shopify publicas.

Uso:
    python vigilar.py tiendas.txt historico.csv

tiendas.txt: una URL por linea (https://tienda.com)
Guarda un historico acumulado y muestra los cambios frente a la corrida anterior.
Lee solo rutas publicas y hace pausa entre peticiones.
"""
import csv, json, os, sys, time, urllib.request
from datetime import date

UA = {"User-Agent": "investigacion-competitiva/1.0"}

def catalogo(base):
    """Devuelve {(tienda, handle, variante): (titulo, precio, disponible)}"""
    out, page = {}, 1
    while True:
        url = f"{base.rstrip('/')}/products.json?limit=250&page={page}"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
                prods = json.loads(r.read().decode("utf-8")).get("products", [])
        except Exception as e:
            print(f"  aviso {base}: {e}", file=sys.stderr)
            return out
        if not prods:
            return out
        for p in prods:
            for v in p.get("variants", [{}]):
                clave = (base, p.get("handle", ""), v.get("title", ""))
                out[clave] = (p.get("title", ""), str(v.get("price", "")), str(v.get("available", "")))
        page += 1
        time.sleep(1.5)

def cargar_historico(ruta):
    if not os.path.exists(ruta):
        return {}
    ultimo = {}
    with open(ruta, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            ultimo[(fila["tienda"], fila["handle"], fila["variante"])] = (
                fila["titulo"], fila["precio"], fila["disponible"])
    return ultimo

def main():
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(1)
    lista, hist_path = sys.argv[1], sys.argv[2]
    with open(lista, encoding="utf-8") as f:
        tiendas = [l.strip() for l in f if l.strip() and not l.startswith("#")]

    previo = cargar_historico(hist_path)
    actual = {}
    for t in tiendas:
        print(f"leyendo {t} ...")
        actual.update(catalogo(t))

    nuevos  = [k for k in actual if k not in previo]
    idos    = [k for k in previo if k not in actual]
    cambios = [k for k in actual if k in previo and actual[k][1] != previo[k][1]]

    print(f"\n=== {date.today().isoformat()} ===")
    print(f"PRODUCTOS NUEVOS ({len(nuevos)}):")
    for k in nuevos:
        print(f"  + {k[0]} | {actual[k][0]} | {k[2]} | {actual[k][1]}")
    print(f"CAMBIOS DE PRECIO ({len(cambios)}):")
    for k in cambios:
        print(f"  $ {k[0]} | {actual[k][0]} | {previo[k][1]} -> {actual[k][1]}")
    print(f"DESAPARECIDOS ({len(idos)}):")
    for k in idos:
        print(f"  - {k[0]} | {previo[k][0]} | {k[2]}")

    escribir_cabecera = not os.path.exists(hist_path)
    with open(hist_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if escribir_cabecera:
            w.writerow(["fecha","tienda","handle","variante","titulo","precio","disponible"])
        hoy = date.today().isoformat()
        for k, v in actual.items():
            w.writerow([hoy, k[0], k[1], k[2], v[0], v[1], v[2]])
    print(f"\nhistorico actualizado: {hist_path} ({len(actual)} filas nuevas)")

if __name__ == "__main__":
    main()
```

Salida útil de inmediato: **productos nuevos** = lo que van a lanzar; **cambios de precio** = dónde
aprietan el margen; **desaparecidos** = lo que descartaron.

## Nivel 3 — Lo que NO debes automatizar

| Tentación | Por qué no |
|---|---|
| Scrapear la Biblioteca de Anuncios con bots | Va contra los términos de Meta; te arriesgas a bloqueos y, si usas la cuenta de la operación, a problemas mayores |
| Miles de peticiones por minuto a tiendas ajenas | Abuso; te bloquean y agrava cualquier reclamación (`106`) |
| Saltar CAPTCHA o rate limits | Cruzas la línea de "público" |
| Extraer perfiles de comentaristas | Datos personales sin base legal (LFPDPPP en México) |
| Bots que comentan en anuncios ajenos | Te reportan y quema tu marca (`07`) |

## Límites técnicos honestos

| Límite | Realidad |
|---|---|
| `/products.json` puede estar deshabilitado | Cada vez más tiendas lo bloquean. Alternativa: sitemap (`93`) |
| Cloudflare u otro WAF | Te va a bloquear si insistes. Respétalo |
| La biblioteca de Meta no tiene API pública abierta para anuncios comerciales | Hay API para anuncios políticos; para lo comercial, consulta manual |
| Cambios de HTML | Cualquier scraper de landing se rompe cada pocas semanas |

Conclusión práctica: **la parte automatizable de verdad es el catálogo y el precio.** Lo demás es
trabajo manual con rutina (`107`).

## Higiene operativa

- Corre los scripts desde tu equipo personal, no desde el servidor de la tienda.
- Pausa de al menos 1-2 segundos entre peticiones.
- Identifica tu User-Agent honestamente.
- Una corrida por semana por tienda, no continua.
- Si una tienda te bloquea, **deja de insistir**.

## Relacionados
`93` catálogo Shopify · `103` precios · `107` radar semanal · `106` legalidad · `100` detección temprana · `109` informe
