# 125 — Multi-brand y white-label

¿Puede un mismo sistema vestir varias marcas distintas sin rehacer todo? Sí, y es una de las pruebas que más respetan en la industria. **Multi-brand** = un solo design system que produce varias marcas hermanas. **White-label** = un producto que un cliente revende con SU propia marca encima. Ambos se logran con la misma palanca: **theming por tokens** (ver 121). Estructura compartida abajo, piel intercambiable arriba.

## Los dos escenarios (no confundir)
| | Multi-brand | White-label |
|---|---|---|
| Qué es | Varias marcas tuyas (familia) | Tu producto, marca del cliente |
| Ejemplo | Marca A y Marca B del mismo grupo | un software que 50 empresas revenden con su logo |
| Quién define la piel | tú, por marca | cada cliente final |
| Cuántas pieles | pocas, conocidas | muchas, a veces infinitas |

La mecánica técnica es la misma; cambia la escala y quién controla los valores.

## La palanca: separar estructura de piel
La regla de oro de todo esto:
```
ESTRUCTURA (no cambia)      PIEL (cambia por marca)
- layout de componentes     - colores
- espaciados y tamaños      - tipografía
- comportamiento            - radios, logo, tono
- accesibilidad             - imágenes
```
Los **componentes nunca saben de qué marca son**. El botón pide `color-action` y `radius-button`; cada marca decide qué valen. Por eso los **tokens semánticos** (ver 121) son obligatorios aquí: son la capa que cada marca redefine.

## Cómo se implementa (la cadena de tokens)
```json
// Núcleo: el botón usa SOLO semánticos
"button-bg": { "$value": "{color-action}" }

// Marca A
"color-action": { "$value": "#1B5E20" },  // verde
"radius-button": { "$value": "12px" }

// Marca B
"color-action": { "$value": "#0B5FFF" },  // azul
"radius-button": { "$value": "4px" }       // más anguloso
```
Mismo `button-bg`, dos resultados. En Figma esto se logra con **modes** (un mode por marca, ver 122); en código, cargando el set de tokens de cada marca.

## Qué puede variar entre marcas
| Variable | Suele cambiar | Suele NO cambiar |
|---|---|---|
| Color | sí (lo primero) | — |
| Tipografía | sí | — |
| Radios / esquinas | sí (carácter visual) | — |
| Logo / nombre | sí | — |
| Espaciado / grid | rara vez | estructura |
| Comportamiento / UX | casi nunca | patrones |
| Accesibilidad | nunca debe bajar | siempre se mantiene |

Decisión clave: define **qué es theming** (cambiable) y **qué es columna vertebral** (intocable). Si dejas que cada marca cambie la estructura, ya no tienes un sistema: tienes N productos disfrazados.

## Niveles de personalización (de menos a más)
1. **Solo color** — lo mínimo white-label: el cliente sube su color y logo.
2. **Color + tipo + radios** — marca con carácter propio.
3. **Lo anterior + componentes opcionales** — el cliente activa/desactiva piezas.
4. **Branding total con límites** — máxima libertad dentro de reglas de accesibilidad.

A más libertad, más poder de venta pero más riesgo de que algo se vea roto. Pon **barandas**: por ejemplo, validar que el color elegido cumpla contraste mínimo (ver 128) antes de aplicarlo.

## Referentes reales
- **Spotify Encore** — sistema multi-plataforma y multi-superficie real.
- Grupos hoteleros y bancarios con varias marcas usan esta arquitectura.
- Plataformas SaaS white-label (e-commerce, reservas) donde cada cliente pone su piel: el motor es siempre tokens + theming.

## Caso para Lushows: BIO-SETA + futuras marcas
Si mañana el grupo lanza una segunda tienda (otra categoría), no rehaces el sistema: defines un nuevo set de tokens (verde → otro color, misma tipografía o una nueva) y reusas botones, tarjetas, layout del dashboard. El sistema de BIO-SETA ya es, de facto, multi-brand-ready si separaste estructura de piel desde el inicio.

## Trampas comunes
- Hardcodear el verde en los componentes → imposible cambiar de marca (el pecado capital).
- Dejar que cada marca toque la estructura → caos, ya no es un sistema.
- White-label sin barandas de contraste → clientes generan interfaces inaccesibles.
- No probar cada marca/tema → algo se rompe solo en la marca B.
- Una sola tipografía asumida → si la marca B trae fuente propia, no encaja.

## Mini-checklist
- [ ] Componentes usan SOLO tokens semánticos (cero valores hardcodeados)
- [ ] Un set de tokens por marca (color, tipo, radios, logo)
- [ ] Estructura/comportamiento/accesibilidad = intocables
- [ ] Modes en Figma, uno por marca
- [ ] Barandas de contraste para white-label abierto
- [ ] Probado en cada marca/tema antes de lanzar

**Siguiente paso**: vestir marcas es una cosa; que todo se adapte a cualquier pantalla es otra. Pasa a 126 diseño responsivo y fluido.
