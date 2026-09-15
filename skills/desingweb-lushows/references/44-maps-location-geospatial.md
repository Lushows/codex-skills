# 44 — Mapas, ubicación & geoespacial UX

Para store locators, **zonas de delivery** (comercio local LatAm), "find us", real-estate, apps location-aware. **Léelo cuando haya mapas, ubicaciones o zonas de cobertura.** Pareja de 42 (gastronomía/local), 22 (SEO local), 16 (a11y).

## 1. Decisión de librería (2026)

**MapLibre GL JS por defecto · Mapbox si quieres sus servicios gestionados · Google solo si el usuario *espera* Google · Leaflet solo para casos triviales.**

| Librería | Costo | Cuándo |
|---|---|---|
| **MapLibre GL JS** | Open-source, **zero tile fees** (pagas solo el proveedor: MapTiler/OpenFreeMap gratis/Protomaps self-host) | **Default.** Mismo motor WebGL vector que Mapbox, sin lock-in |
| **Mapbox GL JS** | ~50k loads/mes gratis, luego por MAU | Si quieres Studio (editor) + geocoding/routing gestionado |
| **Google Maps** | $200/mes crédito, luego per-load (pricing volátil) | Solo si esperan Google; Street View y Places insustituibles |
| **Leaflet** | Gratis ~40KB, raster | Mapa simple, pocos pins (un solo "find us" → mejor imagen estática) |

**Ventaja vector tile** (MapLibre/Mapbox): estilo en cliente vía GPU → zoom/rotación fluidos, restyle instantáneo (`setPaintProperty`), un JSON de estilo controla todo el look. Raster no se re-estila.
```js
const map=new maplibregl.Map({container:'map',style:'https://tiles.openfreemap.org/styles/liberty',
  center:[-74.08,4.65],zoom:12,attributionControl:true});  // [lng,lat] — lng primero
map.addControl(new maplibregl.NavigationControl(),'top-right');
```
Bundle MapLibre ~200KB gzip → siempre lazy-load (§5).

## 2. Store locator UX (canónico)

Estructura ganadora: **search/filter + list + map sincronizados.** Desktop: lista izq (~380px) + mapa der; cada ítem = un marker.
**Sync list↔map (load-bearing):** hover en card → highlight marker · click → `flyTo` + popup · pan/zoom → re-filtra la lista por lo visible (con botón "buscar en esta área", no reordenar en cada gesto) · ordena **por proximidad** (más cercano arriba, 5-10 visibles + paginación).
**Location card:** nombre, dirección, distancia ("a 2.3 km"), **horario + status en vivo** ("Abierto · cierra 8:00 PM" verde / "Cerrado" gris), tap-to-call, botón **"Cómo llegar"**.
**Directions handoff (deep links, no routing propio):**
```js
`https://www.google.com/maps/dir/?api=1&destination=${lat},${lng}`        // Google
`https://waze.com/ul?ll=${lat},${lng}&navigate=yes`                       // Waze (clave LatAm)
`https://maps.apple.com/?daddr=${lat},${lng}`                            // Apple (iOS)
```
**Geolocation "usar mi ubicación":** botón explícito (NUNCA auto-prompt al cargar), con fallback a input manual si se deniega.
**Mobile:** **list-first con bottom-sheet** arrastrable (peek 1-2 cards → expandido lista completa; seleccionar colapsa + flyTo). Evita split 50/50. `env(safe-area-inset-bottom)`.

## 3. Custom styling & branded maps

El default azul-Google grita "genérico". Mapa premium = **muted + decluttered + on-brand.**
**Mapbox Studio** (visual): parte de "Monochrome", recolorea roads/water/labels, **oculta POI icons** (ruido #1), baja saturación; exporta `style.json` (idéntico en MapLibre).
**Por código (MapLibre):** declutter tras `load`:
```js
map.on('load',()=>{
  map.getStyle().layers.filter(l=>/poi|place-label/.test(l.id)).forEach(l=>map.setLayoutProperty(l.id,'visibility','none'));
  map.setPaintProperty('water','fill-color','#0d3b34'); map.setPaintProperty('road-primary','line-color','#1f2d2b');
});
```
**Dark map elegante:** background casi-negro (`#0a0f0d`), roads un paso más claro, labels gris-claro con halo oscuro, **un solo acento (tu brand) para los markers** → el mapa retrocede, los pins resaltan.
**Custom marker SVG** (no el pin rojo default): `new maplibregl.Marker({element:el, anchor:'bottom'})` con un `<svg>` pin de marca (la punta apunta al punto).

## 4. Zonas de delivery & geofencing (LatAm)

UX core: **"ingresa tu dirección para ver si llegamos."** Geocoding (dirección→coords) + point-in-polygon (coords∈zona) + pricing por zona.
**Zonas como GeoJSON polygons** (dibuja en geojson.io): `map.addSource('zones',{type:'geojson',data:zones})` + `addLayer` fill con `fill-opacity:0.15`.
**Geocoding + point-in-polygon con Turf.js:**
```js
import * as turf from '@turf/turf';
async function checkDelivery(address){
  const r=await fetch(`https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=co&q=${encodeURIComponent(address)}`);
  const [hit]=await r.json(); if(!hit) return {ok:false,reason:'address_not_found'};
  const pt=turf.point([+hit.lon,+hit.lat]);
  const zone=zones.features.find(z=>turf.booleanPointInPolygon(pt,z));
  return zone ? {ok:true,zone:zone.properties.name,fee:zone.properties.fee,eta:zone.properties.eta} : {ok:false,reason:'out_of_zone'};
}
```
Respuesta: ✅ "Llegamos al Centro · $4.000 · ~25 min" / ❌ "Aún no llegamos a tu zona — déjanos tu correo". Muestra el pin de la dirección sobre el polígono. **LatAm:** Nominatim es flojo con direcciones informales → Mapbox/Google geocoding rinden mejor + permite **drop-a-pin manual** (arrastrar el marker) como fallback.

## 5. Markers, popups, interacción & performance

**Clustering con supercluster** (Web Worker, millones de puntos) vía MapLibre nativo:
```js
map.addSource('stores',{type:'geojson',data:storesGeoJSON,cluster:true,clusterRadius:50,clusterMaxZoom:14});
map.addLayer({id:'clusters',type:'circle',source:'stores',filter:['has','point_count'],
  paint:{'circle-color':'#10b981','circle-radius':['step',['get','point_count'],16,25,22,100,30]}});
```
**Popups:** on-click (no on-hover en móvil — no hay hover). **fly-to:** `map.flyTo({center,zoom,duration:reduce?0:1200,essential:true})`.
**El facade pattern (CRÍTICO — los mapas pesan):** nunca cargues el SDK en el initial load. Imagen estática (Mapbox/MapTiler Static API) + botón; al click/scroll-into-view, `import()` dinámico y monta:
```js
new IntersectionObserver(async([e],obs)=>{ if(!e.isIntersecting)return; obs.disconnect();
  const {default:maplibregl}=await import('maplibre-gl'); mountMap(maplibregl); }).observe(document.querySelector('#map'));
```
Saca ~200KB+ del critical path → mejor LCP/INP.

## 6. Geolocation, privacy & accessibility

**Permission UX:** pide geolocation **en contexto, tras una acción** (click en "usar mi ubicación"), JAMÁS on-load. Pre-chequea sin disparar prompt:
```js
const s=await navigator.permissions.query({name:'geolocation'});
if(s.state==='granted')autoLocate(); else if(s.state==='prompt')showLocateButton(); else showAddressInput();
```
`enableHighAccuracy:false` salvo necesidad; nunca persistas coords sin consentimiento; input manual SIEMPRE como alternativa de igual jerarquía.
**Accesibilidad — "los mapas NO son accesibles por default"** (un canvas WebGL es opaco para SR/teclado):
- **El mapa es enhancement, no la única vía.** La **lista de tiendas en HTML semántico es la fuente de verdad accesible** (dirección como texto, horario, link directions) — el usuario de SR completa la tarea sin tocar el mapa.
- Canvas decorativo `aria-hidden="true"` o `aria-label` + resumen textual ("Mapa con 8 tiendas en Bogotá"). Navegación por teclado en la **lista**.
- **Static map image** como fallback de perf Y a11y (un solo "find us" → `<img>` estática con `alt` de la dirección + link a Google Maps). Dirección siempre escrita y copiable.

## Maps anti-patterns — blacklist
default ugly map (azul-Google sin estilo, POIs por todos lados) · sin alternativa en lista (solo canvas = inaccesible + sin SEO) · mapa auto-carga en el critical path (usa facade) · geolocation prompt on-load sin contexto · sin mobile pattern (split 50/50; ignorar bottom-sheet/safe-area) · fly-to ignorando `prefers-reduced-motion` · cientos de markers sin clustering · routing propio en vez de deep-link a Waze/Google/Apple · reordenar la lista en cada pan · sin attribution OSM (incumplimiento legal) · confiar en geocoding genérico para direcciones informales LatAm sin drop-a-pin · popup on-hover en móvil.
