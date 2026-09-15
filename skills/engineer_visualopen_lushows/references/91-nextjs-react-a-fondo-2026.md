# 91 — Next.js & React a fondo (2026)

> Versiones (jun 2026): Next.js **16.x** (16.0 oct 2025), React **19.2**, **React Compiler 1.0** estable.

## El titular de Next 16: Cache Components
Ruptura con el caching implícito confuso del App Router. **Caching ahora EXPLÍCITO y opt-in** vía `'use cache'`. Nada se cachea salvo que lo digas.
```tsx
import { cacheLife, cacheTag } from 'next/cache'
async function getProducts(){
  'use cache'; cacheLife('hours'); cacheTag('products')   // TTL + tag
  return db.products.findMany()
}
```
Invalidar desde Server Action/Route Handler con `updateTag('products')` (reemplazo predecible de `revalidateTag`/`unstable_cache`).

## PPR + Turbopack + proxy
**Partial Prerendering (PPR):** cada página = **shell estático** (build) + **dynamic holes** por-request streameados (Vercel: 60-80% más rápido). PPR + Cache Components = el modelo recomendado. **Turbopack estable y default** (2-5× builds prod, Fast Refresh 10×, filesystem caching). **Middleware → `proxy.ts`** (el viejo `middleware.ts` deprecado).

## React 19 / 19.2 primitivos
**Actions** (`<form action={fn}>` con pending/error/success auto) · **`useActionState`** (`[state, formAction, isPending]`) · **`useOptimistic`** · **`use()`** (unwrap promesas/context en render) · **`useFormStatus`**.
```tsx
const [optimistic, addOptimistic] = useOptimistic(messages, (s,m)=>[...s,m])
async function send(fd){ addOptimistic({text:fd.get('text'), sending:true}); await sendMessage(fd) }
```
**React Compiler 1.0** auto-memoiza — dejas de escribir `useMemo`/`useCallback`/`memo` a mano. **RSC vs Server Actions:** RSC renderiza en server con cero JS cliente; Server Actions (`'use server'`) = capa de mutación/RPC.

## Gotchas
1. Upgrade 15→16 NO es gratis — el caching implícito se fue; páginas antes cacheadas ahora corren dinámicas hasta que añadas `'use cache'`.
2. Las cache keys de `'use cache'` se derivan de los args — args no serializables = misses sorpresa o errores de build.
3. PPR requiere que la data dinámica esté tras `<Suspense>`; sin el boundary la ruta entera sale del shell estático.
4. El rename `middleware.ts → proxy.ts` rompe lógica edge existente al upgrade.
5. React Compiler asume pureza (Rules of React); componentes impuros se saltan en silencio — instala el ESLint plugin.
6. No mezcles memoización manual con el compiler indiscriminadamente; deja que el compiler lo dueñe.

**Fuentes:** nextjs.org/blog/next-16 · react.dev/blog (React 19) · infoq.com (Next 16).
