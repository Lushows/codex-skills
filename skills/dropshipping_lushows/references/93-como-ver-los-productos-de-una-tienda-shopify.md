# Cómo ver los productos de una tienda Shopify

> Vigencia: 14-sep-2026. Estas rutas son **públicas por diseño de Shopify** (alimentan buscadores y
> apps). No hay que burlar ninguna protección. Si una tienda las bloquea, se respeta. Ver `106`.

## Las tres puertas públicas

| Ruta | Qué te da |
|---|---|
| `tienda.com/collections/all?sort_by=best-selling` | **El catálogo ordenado por más vendido.** La joya |
| `tienda.com/products.json?limit=250&page=1` | Catálogo completo en JSON: títulos, variantes, precios, fechas de creación |
| `tienda.com/sitemap.xml` (y `sitemap_products_1.xml`) | Todas las URLs de producto, con fecha de última modificación |

## 1. El orden "más vendido": el atajo número uno

```
https://tienda.com/collections/all?sort_by=best-selling
```

Shopify ordena por ventas reales de la tienda. El primer producto de esa lista es, casi siempre, **el
producto que están pautando y el que les da de comer.** Si su catálogo tiene 40 cosas y solo pautan
una, esto te lo revela en un clic.

Otros ordenamientos útiles:

| Parámetro | Uso |
|---|---|
| `?sort_by=created-descending` | Lo último que subieron = lo que van a probar ahora |
| `?sort_by=price-descending` | Techo de precio del catálogo |
| `?sort_by=manual` | El orden que el dueño eligió a mano (lo que quiere destacar) |

**Combinación letal:** `best-selling` te dice qué gana hoy; `created-descending` te dice qué probarán
la semana que viene. Mira las dos y sabrás su hoja de ruta.

## 2. `/products.json`: el catálogo crudo

```
https://tienda.com/products.json?limit=250&page=1
```

Devuelve JSON con, por cada producto: `title`, `handle`, `published_at`, `created_at`, `vendor`,
`product_type`, `tags`, y por cada variante `price`, `compare_at_price`, `sku`, `available`.

Lo que se lee ahí y no se ve en la web:

| Campo | Qué revela |
|---|---|
| `created_at` / `published_at` | **Cuándo subieron el producto.** Cruza con la fecha del primer anuncio (`83`) |
| `compare_at_price` | El precio tachado real, aunque no lo muestren |
| `vendor` | A veces es el nombre del proveedor sin limpiar |
| `sku` | A veces es el SKU del proveedor: lo pegas en Google y encuentras la fuente |
| `available` | Si la variante está agotada |
| `tags` | Su taxonomía interna |

## Script: volcar el catálogo a CSV

```python
#!/usr/bin/env python3
"""Vuelca el catalogo publico de una tienda Shopify a CSV.
Uso: python catalogo.py https://tienda.com salida.csv
Solo lee rutas publicas. Con pausa entre paginas para no cargar el servidor ajeno."""
import csv, json, sys, time, urllib.request

def paginas(base):
    page = 1
    while True:
        url = f"{base.rstrip('/')}/products.json?limit=250&page={page}"
        req = urllib.request.Request(url, headers={"User-Agent": "investigacion-catalogo/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                data = json.loads(r.read().decode("utf-8"))
        except Exception as e:
            print(f"  aviso: no se pudo leer pagina {page}: {e}", file=sys.stderr)
            return
        prods = data.get("products", [])
        if not prods:
            return
        yield from prods
        page += 1
        time.sleep(1.5)   # cortesia: no martillear el servidor ajeno

def main():
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(1)
    base, salida = sys.argv[1], sys.argv[2]
    filas = []
    for p in paginas(base):
        for v in p.get("variants", [{}]):
            filas.append({
                "titulo": p.get("title", ""),
                "handle": p.get("handle", ""),
                "creado": p.get("created_at", "")[:10],
                "publicado": (p.get("published_at") or "")[:10],
                "vendor": p.get("vendor", ""),
                "tipo": p.get("product_type", ""),
                "variante": v.get("title", ""),
                "sku": v.get("sku", ""),
                "precio": v.get("price", ""),
                "precio_tachado": v.get("compare_at_price", "") or "",
                "disponible": v.get("available", ""),
                "url": f"{base.rstrip('/')}/products/{p.get('handle','')}",
            })
    if not filas:
        print("Sin resultados: la tienda no es Shopify o bloquea products.json"); sys.exit(2)
    with open(salida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader(); w.writerows(filas)
    print(f"{len(filas)} filas -> {salida}")

if __name__ == "__main__":
    main()
```

Corre esto **una vez por tienda**, no en bucle sobre cientos. La diferencia entre investigación y
abuso es el volumen y la frecuencia. Ver `108`.

## 3. El sitemap

```
https://tienda.com/sitemap.xml  →  sitemap_products_1.xml
```

Da todas las URLs de producto con `<lastmod>`. Útil cuando `products.json` está bloqueado. El
`lastmod` te dice qué fichas tocaron recientemente: si editaron la ficha del producto X ayer,
probablemente está por lanzarlo o acaba de cambiar el precio.

## Qué hacer con el volcado

1. Ordena por `creado` descendente → su hoja de ruta.
2. Cruza el top de `best-selling` con los anuncios activos en Meta MX (`82`): confirma cuál pautan.
3. Mira `precio` vs `precio_tachado` → tu mapa de precios del nicho (`103`).
4. Mira las variantes: ¿venden 1x, 2x, 3x? Ese es su bundle (`104`).
5. Busca los `sku` en Google → posible proveedor.
6. Repite dentro de 3 semanas y **compara los dos CSV**: los productos nuevos son sus apuestas y los
   que cambiaron de precio te dicen dónde están apretando el margen.

Esa comparación en el tiempo es la parte que casi nadie hace y la que más vale.

## Si no es Shopify

| Plataforma | Alternativa |
|---|---|
| WooCommerce | `/wp-json/wc/store/products` a veces abierto; si no, sitemap |
| Tiendanube | Sitemap + navegación por categorías |
| Plataforma propia | Sitemap; y si no hay, navegación manual |

## Límite ético y técnico

Estas rutas son públicas. Leerlas es legítimo. **Lo que no es legítimo**: descargar sus fotos y
descripciones para usarlas en tu tienda (infracción de derechos de autor, `105`), ni golpear el
servidor con miles de peticiones (`108`).

## Relacionados
`92` espiar tiendas · `94` estimar ventas · `103` precios · `104` bundles · `105` qué copiar · `108` automatizar
