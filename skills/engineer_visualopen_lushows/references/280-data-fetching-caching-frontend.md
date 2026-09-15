# 280 · Data-fetching y caching en frontend: TanStack Query, SWR, RSC

> Fetch-en-`useEffect` es deuda técnica: sin cache, sin dedup, sin reintentos, waterfalls. El server
> state es una disciplina con su propia librería. La pregunta 2026 no es "qué fetcher" sino "¿esto es
> server state o lo resuelve el server (RSC)?".

## El modelo mental: server state ≠ client state
Server state es **async, compartido, puede quedar stale, lo posee el backend**. TanStack Query lo
gestiona: cache por `queryKey`, dedup de requests simultáneos, **stale-while-revalidate**, refetch en
focus/reconnect, GC. No lo metas en Zustand/Redux (ver [[87-state-management-avanzado]]).

```jsx
const { data, isPending, error } = useQuery({
  queryKey: ['order', id],                 // identidad del cache; cambia → otra entrada
  queryFn: () => api.getOrder(id),
  staleTime: 60_000,                       // 60s "fresco": no refetch; clave para no martillar la API
  gcTime: 5*60_000,                        // cuánto vive en cache tras quedar inactivo
})
```

## staleTime vs gcTime (el malentendido #1)
- `staleTime`: cuánto se considera **fresco** (no revalida). Default 0 = revalida en cada mount.
- `gcTime`: cuánto sobrevive en memoria **sin observadores** antes de borrarse (default 5min).
Subir `staleTime` es la palanca real de performance: elimina refetches redundantes. SWR usa el mismo
modelo (`dedupingInterval`), API más mínima; TanStack gana en mutaciones e invalidación granular.

## Invalidación: la fuente de bugs de "datos viejos"
Tras mutar, invalida las queries afectadas — no recargues la página.
```jsx
const qc = useQueryClient()
useMutation({
  mutationFn: updateOrder,
  onSuccess: () => qc.invalidateQueries({ queryKey:['order', id] }), // marca stale → refetch en background
})
```
Cruza con la jerarquía de capas en [[358-caching-strategy-multilayer]] (browser → CDN → app → DB).

## Optimistic updates (UI instantánea con rollback)
```jsx
useMutation({
  mutationFn: toggleLike,
  onMutate: async (v) => {
    await qc.cancelQueries({ queryKey:['post', id] })           // evita que un refetch pise tu update
    const prev = qc.getQueryData(['post', id])
    qc.setQueryData(['post', id], o => ({ ...o, liked:v }))     // pinta ya
    return { prev }                                             // contexto para revertir
  },
  onError: (_e,_v,ctx) => qc.setQueryData(['post', id], ctx.prev), // rollback exacto
  onSettled: () => qc.invalidateQueries({ queryKey:['post', id] }),
})
```
React 19 `useOptimistic` cubre el caso simple sin librería; Query brilla cuando el dato es cache compartido.

## RSC: cuándo NO necesitas fetcher de cliente
En App Router, fetch en Server Component es lo más simple para data **inicial, no interactiva**: corre
en server, 0 KB al cliente, sin estado de loading manual. Patrón híbrido: **server hace prefetch +
`HydrationBoundary`**, cliente hidrata el cache de Query sin doble request.
```jsx
await qc.prefetchQuery({ queryKey:['order',id], queryFn })   // en el Server Component
<HydrationBoundary state={dehydrate(qc)}><ClientOrder/></HydrationBoundary>
```
Regla: data interactiva/refetcheable/compartida → Query. Data de render inicial → RSC. No los enfrentes; combínalos.

| Síntoma | Causa | Fix |
|---|---|---|
| Refetch en cada navegación | `staleTime:0` | subir staleTime |
| Datos viejos tras guardar | no invalidaste | `invalidateQueries` en `onSuccess` |
| Waterfall de requests | queries dependientes en serie | `enabled` + prefetch paralelo |
| Doble fetch en SSR | no hidrataste | `prefetchQuery` + `HydrationBoundary` |

## Gotchas
1. `queryKey` debe incluir **toda** variable del `queryFn` (id, filtros, page) o sirves cache equivocado.
2. `onMutate` sin `cancelQueries` → un refetch en vuelo revierte tu optimistic update.
3. Fetch en `useEffect` no deduplica: dos componentes = dos requests al mismo endpoint.
4. `staleTime: Infinity` sin invalidación = datos eternos viejos; combínalo siempre con invalidación por mutación.

Cruza con [[91-nextjs-react-a-fondo-2026]], [[358-caching-strategy-multilayer]] y [[87-state-management-avanzado]].
