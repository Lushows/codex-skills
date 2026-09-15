# 21 — Forms & inputs UX (donde se ganan/pierden las conversiones)

Los formularios deciden conversiones (checkout, signup, lead, pago). Cada campo extra cuesta ~2-3% de conversión; abandono medio de carrito **70.19%** (Baymard). **Léelo en todo checkout, registro, captura o pago.** Pareja de 16 (a11y), 17 (copy) y 11 (e-commerce).

## 1. Layout y estructura

- **Single-column, sin excepciones.** El ojo recorre verticalmente sin saltos. Única excepción: campos atómicos cortos en una fila (Ciudad/CP, Mes/Año de tarjeta).
- **Label arriba (top-aligned) gana** — escaneo vertical rápido, no se corta en móvil. Label a la izquierda solo en back-office denso.
- **Marca lo OPCIONAL, no lo requerido.** Si el 90% es obligatorio, marca los pocos opcionales con texto: `Empresa (opcional)`.
- **Agrupa con `<fieldset>`/`<legend>`** ("Contacto", "Envío", "Pago").
- **Elimina todo lo no esencial.** Checkout medio = 14.88 campos; Baymard: **~7-8 bastan**. Combina nombre+apellido, autocompleta ciudad/depto desde CP, elimina "confirmar email".
- **Single-page vs multi-step:** lo que mata es el **total de campos**, no las páginas. One-page/accordion para productos simples (AOV<$150, móvil, 1-3 ítems). Multi-step para alto valor/muchos campos (15 campos en 3 pasos lógicos > 10 en una página, por compromiso progresivo). Patrón Shopify: accordion de pasos que colapsan al completarse + progress indicator visible.

## 2. Input types & poder nativo

El HTML correcto invoca el teclado correcto en móvil y habilita autofill. La tripleta `type` + `inputmode` + `autocomplete` es un equipo. **Tabla de oro:**

| Campo | HTML |
|---|---|
| Nombre completo | `type="text" autocomplete="name" autocapitalize="words" enterkeyhint="next"` |
| Email | `type="email" inputmode="email" autocomplete="email" autocapitalize="off" spellcheck="false"` |
| Teléfono | `type="tel" inputmode="tel" autocomplete="tel"` |
| OTP/SMS | `inputmode="numeric" autocomplete="one-time-code" maxlength="6"` |
| Dirección | `autocomplete="street-address"` (o `address-line1/2`) |
| Ciudad | `autocomplete="address-level2"` · Depto: `address-level1` |
| Código postal | `inputmode="numeric" autocomplete="postal-code"` |
| Nº tarjeta | `inputmode="numeric" autocomplete="cc-number"` |
| Nombre tarjeta | `autocomplete="cc-name"` · Venc: `cc-exp` (un campo MM/AA) · CVC: `inputmode="numeric" autocomplete="cc-csc"` |
| Password login | `autocomplete="current-password"` · Registro: `new-password` |

**Notas críticas:**
- `enterkeyhint="next|done|go|send|search"` cambia la tecla Enter del teclado virtual → guía el avance.
- `autocomplete` es obligatorio para **WCAG 1.3.5 (AA)** y para autofill iOS/Android. Prefija: `autocomplete="shipping postal-code"`.
- **`<select>` nativo siempre que puedas** (accesible, gratis, teclado móvil). Custom combobox solo si necesitas búsqueda con filtrado (y reimplementa toda la a11y de teclado). Chrome ya estiliza con `appearance:base-select`.
- **`field-sizing:content`** (CSS 2025): inputs/textarea crecen con el contenido, sin JS de auto-resize.
- **NO uses `type="number"`** para tarjeta/código/teléfono (añade spinners, rechaza ceros líderes) → usa `inputmode="numeric"`.
- **Tarjeta:** un campo, auto-formato con espacios cada 4 dígitos en `input`, detección de marca por BIN. Si manejas pagos, usa **Stripe Elements/iframes PCI**, no reinventes.

## 3. Validación & errores

**Timing (regla de oro):** valida **on-blur**, nunca on-keystroke. Una vez que un campo tiene error, **re-valida on-input** para limpiarlo en cuanto lo corrige. Excepciones con feedback en vivo: fuerza de contraseña, disponibilidad de usuario/email.
```js
input.addEventListener('blur', ()=>validate(input));
input.addEventListener('input', ()=>{ if(input.getAttribute('aria-invalid')==='true') validate(input) });
```
**Fórmula del buen error:** qué pasó + por qué + cómo arreglarlo, humano. "Entrada inválida" → "Ingresa un email válido, ej: nombre@correo.com". Debajo del campo, rojo + icono (no solo color).
**A11y:** `aria-invalid="true"` + `aria-describedby="err-id"` + `<p id="err-id" role="alert">`. En submit con errores, mueve foco al primer inválido + resumen arriba con anclas.
**NO deshabilites el botón submit** (lo saca del foco, oculta qué falta). Déjalos enviar y muestra errores. Si necesitas indicar "no listo": `aria-disabled="true"` (sigue enfocable) + `aria-describedby`.

## 4. Checkout/pago (e-commerce, alto riesgo)

Hallazgos Baymard:
- **Guest checkout obligatorio.** Forzar registro = causa #1 de abandono evitable. Patrón: invitado + "crear cuenta con un clic" *después* (solo pide contraseña).
- Reduce a ~7-8 campos.
- **Autofill de dirección:** un campo `autocomplete="street-address"` + autodetección por CP.
- **Express checkout arriba** (Apple/Google Pay): reducen ~120 clics a ~4; al inicio duplican conversión. Wallets ya son 49-56% del valor transado.
- **Señales de confianza a nivel de campo:** candado junto al número de tarjeta, "datos cifrados", logos de pago.
- **Recuperación de error:** nunca borres campos al fallar; resalta solo lo erróneo.
**Checkout WhatsApp/contraentrega (LatAm):** el "formulario" se reduce a **nombre, teléfono, dirección, ciudad** — confirmación/negociación en el chat. Ofrece prepago, depósito parcial (reduce RTO) o COD. WhatsApp+IA convierte 28-38% vs ~1.89% de un sitio típico.

## 5. A11y & móvil

- **Inputs ≥16px** (Safari iOS hace zoom si <16). **Nunca `user-scalable=no`** (viola WCAG 1.4.4).
- **Targets 44×44px** (Apple) / 24×24 mín (WCAG 2.5.8) en botones/checkboxes/radios.
- **Label siempre asociado** vía `for`/`id` (o envolviendo el input).
- **`enterkeyhint`** para guiar el flujo de teclado.
- **Radios/checkboxes en `<fieldset>`+`<legend>`.**
- **Multi-step:** al avanzar, mueve foco al encabezado/primer campo del nuevo paso; anuncia el cambio.

## 6. Estética premium & microinteracciones

- **Floating labels:** se ven caros, pero cuida la a11y — el label flotante debe mantener contraste AA y tamaño legible, y existir un label real (no placeholder disfrazado). Alternativa segura: label arriba siempre visible + placeholder como *ejemplo de formato*.
- **Focus:** anillo 2-3px con `:focus-visible`, color de marca, nunca `outline:none` sin reemplazo.
- **Reveal de error suave** (altura/opacidad 150-200ms ease-out), no saltos que desplazan layout.
- **Estado de envío:** spinner inline + "Procesando…", `aria-busy="true"`, evita doble-submit por lógica (no quitando el botón del DOM).
- **Éxito:** confirmación clara + checkmark + siguiente paso obvio. Checkmark verde sutil al completar cada campo válido refuerza progreso.
- **Auto-formato en vivo** (tarjeta/teléfono/fecha) sin bloquear el cursor.

## Blacklist de formularios
placeholder como label · validación on-keystroke · botón submit `disabled` hasta completar · borrar campos al fallar · multi-columna en flujo · `type="number"` para tarjeta/código/teléfono · `user-scalable=no` o inputs <16px · forzar registro antes de comprar · "confirmar email/contraseña" (usa toggle "mostrar") · asterisco en todo · color como único indicador de error · mensajes genéricos ("Inválido") sin cómo corregir · dropdown para datos cortos (mes/año, binario) · sin `autocomplete` (rompe autofill + WCAG 1.3.5) · captcha agresivo/campos de marketing en el camino crítico.
