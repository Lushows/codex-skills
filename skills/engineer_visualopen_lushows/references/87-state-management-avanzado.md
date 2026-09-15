# 87 — State management avanzado (React/frontend)

## El frame que define 2026: server state vs client state son disciplinas SEPARADAS
El mayor shift. **TanStack Query** posee el *server state* (caching, dedup, stale-while-revalidate, refetch, GC de
data remota). **Zustand/Jotai/Valtio** poseen el *client state* (UI que nunca vino del server: modales, wizards,
theme, tab). Mezclarlos (fetch+cache a mano en Redux) es anti-patrón. **Stack pragmático 2026: Zustand (client) + TanStack Query (server) + nuqs (URL state)**, ~18KB.

## Las opciones
- **Zustand (~3KB)** — el default. Store único, sin provider, selectores hook.
  ```js
  const useStore = create((set) => ({ count:0, inc:()=>set(s=>({count:s.count+1})) }))
  const count = useStore(s => s.count)   // selector = re-render dirigido
  ```
- **Jotai (~4KB)** — atómico/bottom-up. Para estado granular con **derived atoms** (recomputan solo si cambian deps). Genial para forms/canvas.
  ```js
  const priceAtom = atom(100); const taxedAtom = atom(get => get(priceAtom)*1.19)
  ```
- **Redux Toolkit (~15KB)** — sobrevive para apps grandes complejas (middleware, time-travel, RTK Query). Ya no es el default.
- **Valtio (~4KB)** — Proxies, escritura estilo mutable. Nicho ergonómico.

## Signals & React 19
Solid/Preact/Vue/**Angular** (signals estables en v19) usan signals (reactividad fina sin VDOM). **React deliberadamente NO los adopta** (chocan con "UI as a function of state"). La propuesta TC39 Signals sigue **Stage 1**. **React 19 built-ins** absorben casos: `use()` (lee promesas/context), **Actions** + `useActionState` + `useFormStatus`, **`useOptimistic`** (UI optimista nativa, reemplaza middleware Redux).

## Gotchas
1. No pongas server data en Zustand/Redux — reimplementas caching mal; es trabajo de TanStack Query.
2. Olvidar selectores en Zustand (`useStore()` sin selector) re-renderiza en cada cambio.
3. Átomos Jotai dentro de componentes se recrean cada render — defínelos a module scope.
4. `useOptimistic` revierte solo si la action lanza — no hagas rollback manual además.
5. RTK es overkill para apps chicas (15KB + ceremonia).
6. El hype de signals ≠ realidad React — samples de Solid/Angular no traducen; no esperes soporte de 1ª clase.

**Fuentes:** pkgpulse.com/blog (state of React state mgmt 2026) · react.dev/blog (React 19) · react.dev/reference/react/useOptimistic.
