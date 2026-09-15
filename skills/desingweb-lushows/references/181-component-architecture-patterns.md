# 181 — Component architecture & headless/compound patterns

**CRAFT, code-heavy (React-leaning, principios generales).** Cómo BUILD componentes reutilizables. Pareja de 15 (design systems/tokens), 35 (componentes/estados), 34 (Motion React). Regla de oro: **composition over configuration — construyes la API que tú querrías consumir; headless para lógica/a11y, tú eres dueño del estilo.**

## 1. Por qué composición vence a configuración

El anti-patrón: el componente "dios" que crece por props (un Modal con 30 props, cada requisito = una prop + rama + test, superficie O(n)). La salida: exponer **slots**:
```tsx
// ❌ config hell          // ✅ composición — API pequeña y estable
<Modal open={open} onOpenChange={setOpen}>
  <Modal.Header><Modal.Title>Confirmar</Modal.Title></Modal.Header>
  <Modal.Body>¿Eliminar el pedido?</Modal.Body>
  <Modal.Footer><Button variant="ghost" onClick={cancel}>Cancelar</Button><Button variant="destructive" onClick={confirm}>Eliminar</Button></Modal.Footer>
</Modal>
```
El componente no decide el layout, provee piezas + comportamiento (focus trap, escape). La flexibilidad la pone JSX, no un objeto de config.

## 2. Compound components (estado implícito vía Context)

Subcomponentes namespaced que comparten estado por Context sin cablear props:
```tsx
const TabsCtx = createContext(null);
const useTabs = () => { const c = useContext(TabsCtx); if(!c) throw new Error("Tabs.* fuera de <Tabs>"); return c; };
function Tabs({ defaultValue, children }){ const [value,setValue]=useState(defaultValue);
  return <TabsCtx.Provider value={{value,setValue}}>{children}</TabsCtx.Provider>; }
Tabs.Trigger = ({ value, children }) => { const c=useTabs();
  return <button role="tab" aria-selected={c.value===value} onClick={()=>c.setValue(value)}>{children}</button>; };
```
**Brilla cuando** el consumidor controla el layout (intercalar separadores, markup arbitrario). El `throw` en `useTabs` convierte mal uso en error claro.

## 3. Headless / unstyled (el estándar 2026)

Lógica + a11y sin estilos (tú controlas el diseño; la librería resuelve teclado/focus/ARIA/edge-cases). Panorama: **Radix Primitives** (maduro), **Base UI** (sucesor activo, equipo MUI — apuesta greenfield 2026), **React Aria** (Adobe, oro de a11y, i18n/RTL), **Ark UI** (multi-framework, state machines). **shadcn/ui** = copy-paste, **tú eres dueño del código** (lo pegas en tu repo y editas; cero abstracción opaca, versionado en tu git; coste: las actualizaciones no llegan solas) vs libs instaladas. **Por qué ganó headless:** la a11y correcta (roving tabindex, `aria-activedescendant`, focus restoration) es brutalmente difícil — delégala y quédate con el 100% del control visual.

## 4. asChild / polymorphic (sin wrapper-divs)

Un `<Button>` que a veces es `<a>` o `<Link>`. La solución 2026 es **`asChild` con Slot** (Radix): en vez de renderizar su DOM, fusiona props sobre su hijo:
```tsx
const Button = forwardRef(({ asChild, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "button";
  return <Comp ref={ref} className={cn(buttonVariants(props), className)} {...props} />;
});
<Button asChild><a href="/precios">Ver precios</a></Button>  {/* <a> real, sin div extra */}
```
`Slot` clona el hijo y fusiona estilos/`onClick`/refs/ARIA sobre el elemento real → DOM limpio, semántica correcta. `asChild` superó a `as` para comportamiento (compone con cualquier componente, no solo tags).

## 5. Controlled vs uncontrolled

Robusto funciona en ambos: **uncontrolled** (gestiona su estado, `defaultValue` + lee por `onChange`), **controlled** (el consumidor posee `value`). Regla: si `value` está definido → controlled. `useControllableState`:
```tsx
function useControllableState({ value, defaultValue, onChange }){
  const isControlled = value !== undefined;
  const [internal, setInternal] = useState(defaultValue);
  const setValue = useCallback(next => { if(!isControlled) setInternal(next); onChange?.(next); }, [isControlled, onChange]);
  return [isControlled ? value : internal, setValue];
}
```
El error fatal: alternar `undefined`→valor en `value` durante la vida del componente (warning React; decide el modo una vez).

## 6. Estado, a11y & design-system layer — Button completo

Layering: **primitive (headless) → styled (variants) → pattern**. Tokens (CSS vars) → `cva`/`tailwind-variants` → props; `forwardRef` para foco/forms:
```tsx
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:ring-2 focus-visible:ring-ring disabled:opacity-50 disabled:pointer-events-none",
  { variants:{ variant:{ default:"bg-primary text-primary-foreground hover:bg-primary/90", destructive:"bg-destructive text-white", ghost:"hover:bg-accent" },
    size:{ sm:"h-8 px-3", md:"h-10 px-4", lg:"h-12 px-6" } }, defaultVariants:{ variant:"default", size:"md" } });
export const Button = forwardRef(({ className, variant, size, asChild, loading, disabled, children, ...props }, ref) => {
  const Comp = asChild ? Slot : "button";
  return <Comp ref={ref} className={cn(buttonVariants({variant,size}), className)} disabled={disabled||loading} aria-busy={loading||undefined} {...props}>
    {loading && <Spinner aria-hidden className="mr-2 size-4" />}{children}</Comp>;
});
```
Reúne: variants type-safe, `asChild`, `forwardRef`, a11y horneada (`focus-visible:ring`, `aria-busy`, `disabled` real), `cn` (tailwind-merge para que el `className` del consumidor gane), tokens. El `loading` vive donde conoce la operación async, no dentro del Button.

## Component-architecture anti-patterns — blacklist
**prop-explosion/boolean soup** (`showHeader`/`hideFooter`; >8 props de config = faltan slots) · **`cloneElement` manual repartido** en vez de Context · **spread ciego sin `forwardRef`** (el consumidor no puede enfocar/integrar react-hook-form) · **reimplementar a11y a mano** en vez de headless · **`className` que no se mergea** (concatenar strings; el override pierde por especificidad) · **saltar uncontrolled→controlled** en runtime · **Context sin guard** (fallos silenciosos crípticos) · **polimorfismo con `as` mal tipado** para comportamiento (usa `asChild`) · **`useEffect` para sincronizar prop→state** en vez de derivar en render · **acoplar estilo a lógica** (`if(variant===...)` esparcido en vez de `cva`) · **wrapper-div gratuito** donde `Slot` lo haría · **forkear shadcn sin documentar la divergencia**.
