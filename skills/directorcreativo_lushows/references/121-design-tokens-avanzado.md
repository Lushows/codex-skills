# 121 — Design tokens avanzado

Un **design token** es un valor de diseño con nombre, definido una vez y usado en todas partes (ya lo viste en 87). Este módulo va al nivel pro: el formato estándar de la industria (DTCG), los tres niveles de token bien hechos, y cómo un mismo sistema viste varias marcas o un modo claro/oscuro cambiando solo los valores. Esto es lo que separa un sistema de juguete de uno que escala.

## Repaso de 30 segundos
En vez de escribir `#1B5E20` en 40 lugares, defines `color-brand-primary = #1B5E20` una vez. Cambias el token, cambia todo. Un token tiene: **nombre** (qué es), **valor** (cuánto/cuál) y opcionalmente **tipo** (color, dimensión, fuente).

## El formato estándar: DTCG (W3C)
A 2026 existe un estándar abierto, el **Design Tokens Community Group (DTCG)** del W3C, que define un formato JSON común para que herramientas distintas (Figma, Style Dictionary, Tokens Studio) hablen el mismo idioma. La clave: cada token usa `$value` y `$type`.

```json
{
  "color": {
    "brand": {
      "primary": { "$value": "#1B5E20", "$type": "color" },
      "accent":  { "$value": "#C5E1A5", "$type": "color" }
    }
  },
  "space": {
    "base": { "$value": "8px", "$type": "dimension" }
  }
}
```
Que exista un estándar importa: no quedas atrapado en una sola herramienta. Si mañana cambias de software, tus tokens viajan.

## Los 3 niveles (token tiers) — bien hechos
Esta es la parte que casi todos hacen mal. Un sistema serio separa tres capas:

| Nivel | Nombre | Qué responde | Ejemplo |
|---|---|---|---|
| 1 | **Primitivo** | "¿qué color en bruto existe?" | `green-700 = #1B5E20` |
| 2 | **Semántico** | "¿qué ROL cumple?" | `color-action = green-700` |
| 3 | **Componente** | "¿dónde se usa?" | `button-bg = color-action` |

```json
{
  "green-700":   { "$value": "#1B5E20" },
  "color-action":{ "$value": "{green-700}" },
  "button-bg":   { "$value": "{color-action}" }
}
```
Las llaves `{green-700}` son **referencias** (alias): el token apunta a otro, no repite el valor.

**Por qué importa tanto:** el día que el cliente quiere el verde más oscuro, cambias `green-700` en un solo sitio y se propaga a action, a button-bg y a todo lo demás. Sin esta cadena, terminas con `#1B5E20` regado y desincronizado (ver 87 para el caso simple).

## Theming: un sistema, muchas pieles
**Theming** = cambiar la apariencia sin cambiar la estructura. Se logra cambiando SOLO los tokens semánticos, no los componentes.

### Modo claro / oscuro
```json
// tema claro
"color-bg":   { "$value": "{white}" },
"color-text": { "$value": "{gray-900}" }

// tema oscuro (mismos nombres, otros valores)
"color-bg":   { "$value": "{gray-900}" },
"color-text": { "$value": "{gray-50}" }
```
El botón nunca sabe si está en claro u oscuro: solo pide `color-bg`. Cambias el tema, los componentes obedecen solos.

### Multi-brand (varias marcas, un sistema)
La misma idea sirve para vestir 2-3 marcas hermanas. Cada marca redefine los primitivos/semánticos; los componentes no se tocan (ver 125 para el caso completo).
```
marca-A:  color-action = green-700
marca-B:  color-action = blue-600
```
Mismo botón, dos marcas, cero código duplicado.

## De token a código real (la cadena de producción)
La herramienta clave a 2026 es **Style Dictionary** (de Amazon): toma tu JSON de tokens y genera automáticamente variables CSS, Sass, código iOS/Android, etc. Una fuente, muchos destinos.

```
tokens.json  →  Style Dictionary  →  variables.css  (web)
                                  →  Colors.swift   (iOS)
                                  →  colors.xml      (Android)
```
Salida CSS típica:
```css
:root {
  --color-action: #1B5E20;
  --button-bg: var(--color-action);
  --space-base: 8px;
}
```
**Tokens Studio** es el plugin de Figma que conecta los tokens del diseño con ese JSON, para que diseño y código no se separen (ver 122 y 127).

## Naming de tokens (la regla que evita el caos)
Patrón recomendado: `categoría-rol-variante-estado`
```
color-action-default
color-action-hover
color-text-muted
space-inset-md
radius-button
font-size-heading-lg
```
Reglas:
- [ ] Sin tildes ni espacios, en inglés (estándar de la industria).
- [ ] El nombre describe el ROL, no el aspecto: `color-action`, no `color-green`. (Si mañana es azul, el nombre `color-green` miente.)
- [ ] Escala consistente: `sm / md / lg / xl`, no `chico / mediano2 / grande-real`.

## Errores comunes
- Saltarse el nivel semántico (todo apunta directo al primitivo) → imposible hacer theming.
- Nombrar por color (`color-blue`) en vez de por rol (`color-action`).
- 50 tonos de gris sin sistema → reduce a una escala de 9-10 pasos.
- Tokens en Figma que no llegan al código → diseño y producto divergen.

## Mini-checklist
- [ ] Tokens en JSON con `$value`/`$type` (formato DTCG)
- [ ] 3 niveles: primitivo → semántico → componente
- [ ] Theming por tokens semánticos (claro/oscuro o multi-marca)
- [ ] Naming por rol, sin tildes, escala consistente
- [ ] Pipeline a CSS/código (Style Dictionary) si hay producto digital
- [ ] Tokens Studio conectando Figma ↔ JSON

**Siguiente paso**: con los tokens definidos, hay que construirlos y mantenerlos donde se diseña. Pasa a 122 Figma avanzado: variables, modes y components.
