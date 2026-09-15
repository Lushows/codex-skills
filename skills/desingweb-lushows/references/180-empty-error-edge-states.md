# 180 — Empty, error, loading & edge states (beyond the happy path)

**CRAFT.** Los estados más allá del caso de éxito (la señal de madurez). Pareja de 30 (onboarding/empty), 35 (matriz de estados), 178 (estados de tabla), 16 (a11y). Regla de oro: **el happy path es la excepción estadística — todo componente que carga datos define una matriz de 6 estados (default/loading/empty/error/partial/success), diseñada el día 1, no parcheada en QA. `empty` exitoso ≠ `error` (no los confundas con "No hay datos").**

## 1. Por qué importan

El 90% del diseño cubre el caso con datos completos; el producto real vive en empty/loading/error/partial. Matriz obligatoria por componente:
```
default → datos completos · loading → en camino · empty → query OK con 0 resultados (¡no es error!)
error → fallo de fetch/server (recuperable) · partial → algunos datos / stale · success → confirmación
```

## 2. Empty states (el más subestimado)

Cuatro variantes: **first-use** (oportunidad de onboarding — "Crea tu primer proyecto" + CTA, NO "no tienes proyectos"), **user-cleared** (celebratorio "Bandeja vacía 🎉 al día"), **no-results** (ofrece salidas: limpiar filtros, corregir typo, relacionadas), **error-as-empty** (anti-patrón grave). Anatomía (ilustración + headline + una línea + **UN CTA primario**):
```html
<div class="empty-state" role="status">
  <img src="/empty.svg" alt="" aria-hidden="true">
  <h2>Aún no tienes pedidos</h2><p>Cuando un cliente confirme, aparecerá aquí.</p>
  <button class="btn-primary">Crear pedido manual</button>
</div>
```
Dos botones del mismo peso = parálisis. Ilustración que refuerza el mensaje, nunca relleno de stock.

## 3. Loading states & perceived performance

Los usuarios perciben **skeleton screens 20-30% más rápidas** que spinners a tiempo idéntico. Cuándo: **skeleton** (forma conocida — lista/card/tabla; preserva layout → cero CLS), **spinner** (forma desconocida o <1s, botones), **progress bar** (duración conocida — upload/export), **optimistic UI** (acciones frecuentes de bajo riesgo).
```css
.skel{ background:#1a2520; background-image:linear-gradient(90deg,transparent,rgba(255,255,255,.06),transparent);
  background-size:200% 100%; animation:shimmer 1.4s infinite; }
@keyframes shimmer{ to{ background-position:-200% 0 } }
@media (prefers-reduced-motion:reduce){ .skel{ animation:none } }
```
**Optimistic con rollback** (muestra el resultado antes de confirmar, revierte si falla):
```js
async function toggleLike(id){ setLiked(id,true); try{ await api.like(id) } catch{ setLiked(id,false); toast.error('No se pudo. Reintenta.') } }
```
El skeleton debe igualar las dimensiones del contenido real (si no, CLS).

## 4. Error states & messaging

**Fórmula:** qué pasó + por qué + cómo arreglarlo + tono humano. Nunca culpes al usuario, nunca stack trace, nunca solo "Error".
```
❌ "Error 500"  ❌ "Algo salió mal"
✅ "No pudimos guardar tu pedido. Tu conexión se interrumpió. Revisa internet e intenta de nuevo." [Reintentar]
```
**Dónde:** inline (ligado a un campo), toast (no bloqueante, transitorio), page (fallo total: 404/500/offline). **404/500/offline útiles** (la ilustración divertida está bien, pero con salidas reales: search, links a secciones top, reintentar). **Error boundary** (un componente que crashea no tumba la app — `getDerivedStateFromError` + UI de retry local). **Retry** con exponential backoff y tope.

## 5. Partial & degraded states

**Stale data** ("Actualizado hace 5 min" + reintento en background — datos viejos > pantalla vacía). **Slow connection** (baja calidad antes de romper). **Offline-first** (cachea, encola mutaciones, sincroniza al reconectar; banner "Sin conexión — se guardará al volver"). **"Algunas cosas fallaron"** (4 de 5 widgets cargaron → pinta los 4, el 5º con mini-error y retry **local** — nunca tumbes los 4 buenos por 1 malo):
```jsx
{widgets.map(w => w.error ? <WidgetError onRetry={()=>refetch(w.id)} /> : <Widget data={w.data} />)}
```

## 6. El craft & el sistema

Diseña estados como sistema (Storybook con un story por estado). **`prefers-reduced-motion`** (desactiva el shimmer). **A11y:** loading `aria-busy="true"`; empty `role="status"` + `aria-live="polite"`; error `role="alert"` + `aria-live="assertive"` y **mueve el foco** al mensaje; ilustraciones decorativas `alt=""` + `aria-hidden`. **Tono** humano y accionable ("No pudimos…", nunca "Ingresaste mal…"). **Delight en el dead-end** (el empty/error es donde el cariño del producto se nota — microilustración propia, voz de marca, CTA que ayuda).

## Edge-states anti-patterns — blacklist
**mostrar solo el happy path** en Figma/Storybook · **"No data"/"Sin resultados"** genérico que sirve para empty Y error · **error-as-empty** (pintar un fallo de fetch como lista vacía) · **spinner eterno** sin timeout ni estado de error · **CLS** (skeleton de tamaño distinto al contenido) · **stack trace/código 500 crudo** · **culpar al usuario** · **dos CTAs primarios** en un empty · **404 cute-only** sin navegación · **un widget tumba el dashboard** por falta de error boundary · **shimmer sin `prefers-reduced-motion`** · **error sin foco ni `aria-live`** · **optimistic sin rollback** (datos divergen) · **toast para un error crítico** que desaparece antes de leerse.
