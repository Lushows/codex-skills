# 93 — TypeScript a fondo (2026)

## El gran story 2026: TypeScript 7 ("Project Corsa") — el compilador nativo en Go
Microsoft anunció **TS 7.0 Beta el 21 abr 2026**, vía `@typescript/native-preview` y el ejecutable **`tsgo`**. Port
de la codebase a **Go**, **~10× más rápido** que TS 6.0, semántica idéntica (pasa 19,926/20,000 tests = 99.6%).
**Estable esperado fin junio/inicio julio 2026.** Hoy: `tsc` (TS 6.x, JS-based) para prod, `tsgo` para velocidad. TS **6.0** = release transicional que voltea algunos defaults.
```bash
npm i -D @typescript/native-preview
npx tsgo --noEmit       # 10× más rápido, drop-in de tsc
```

## El sistema de tipos que de verdad necesitas
- **Discriminated unions** (el patrón más útil): narrow por tag literal.
  ```ts
  type Result<T> = { status:'ok'; data:T } | { status:'error'; message:string }
  ```
- **Generics + constraints:** `function pick<T, K extends keyof T>(o:T, k:K): T[K]`.
- **Conditional + `infer`:** `type ElementOf<T> = T extends (infer U)[] ? U : never`.
- **Mapped types:** `type Partial<T> = { [K in keyof T]?: T[K] }` (base de Pick/Omit/Record/ReturnType...).
- **Template literal types:** `type Route = \`/api/${string}\``.
- **`satisfies`** — valida contra un tipo SIN widening (mantienes los literales precisos):
  ```ts
  const config = { port:3000, host:'localhost' } satisfies Record<string, string|number>
  config.port   // sigue siendo number
  ```
**Narrowing:** `typeof`/`instanceof`/`in`/igualdad literal/type guards (`x is Foo`)/assertion functions.
**Strictness baseline:** `strict:true` + `noUncheckedIndexedAccess` + `exactOptionalPropertyTypes` + `verbatimModuleSyntax`.

## Gotchas
1. `tsgo`/TS 7 es **beta** a jun 2026 — mantén `tsc` como source of truth para CI emit hasta la RC estable.
2. Los ~74 edge-cases incompatibles (#61754) pueden morder en código type-level exótico — verifica `.d.ts` pesados bajo tsgo.
3. `satisfies` NO emite checks runtime — solo compile-time.
4. `noUncheckedIndexedAccess` añade `| undefined` a todo index access; activarlo tarde inunda de errores — adóptalo temprano.
5. Abusar de conditional types con `infer` mata la responsividad del IDE.
6. `as const` + `satisfies` interactúan sutilmente; el orden importa — `as const` primero, luego `satisfies`.

**Fuentes:** devblogs.microsoft.com/typescript (TS 7.0 Beta) · visualstudiomagazine.com (TS7 beta) · infoworld.com (native port).
