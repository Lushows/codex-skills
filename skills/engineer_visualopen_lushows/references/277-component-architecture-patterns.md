# 277 · Arquitectura de componentes: composición, compound, headless

> Un componente bien diseñado expone *forma*, no opciones. La diferencia entre 8 props booleanas
> y un compound component es la diferencia entre una API que se rompe y una que escala.

## El eje real: props-explosion vs composición
La señal de mal diseño es el crecimiento de props (`size`, `variant`, `hasIcon`, `iconLeft`,
`loading`, `outlined`...). Cada flag nueva multiplica el espacio de estados. La cura es **invertir el
control**: en vez de configurar, *componer*. Pasa `children`/slots y deja que el consumidor arme la forma.

```jsx
// ❌ config-hell: cada caso nuevo = otra prop
<Card title="X" subtitle="Y" footer="Z" badge="new" badgeColor="red" />
// ✅ composición: la forma vive en el consumidor
<Card>
  <Card.Header><Badge tone="red">new</Badge>X</Card.Header>
  <Card.Body>Y</Card.Body>
</Card>
```

## Compound components (estado compartido implícito)
Padre + hijos coordinados vía **Context interno**. El consumidor ordena/omite piezas; el estado se
comparte sin prop-drilling. Patrón de Radix/shadcn.

```jsx
const TabsCtx = createContext(null)
function Tabs({ defaultValue, children }) {
  const [value, setValue] = useState(defaultValue)
  return <TabsCtx value={{ value, setValue }}>{children}</TabsCtx> // React 19: <Ctx> sin .Provider
}
Tabs.Trigger = ({ value, children }) => {
  const { value: cur, setValue } = use(TabsCtx)            // use() lee context
  return <button data-state={cur===value?'active':''} onClick={()=>setValue(value)}>{children}</button>
}
```

## Headless / hooks-as-API
Separa **lógica** (estado, a11y, teclado) de **render** (markup, estilos). El hook devuelve props-getters;
tú pintas. Es lo que hace TanStack Table, Downshift, React Aria. Máxima reutilización, cero opinión visual.

```jsx
const { getToggleProps, isOpen } = useDisclosure()
<button {...getToggleProps()}>{isOpen ? 'cerrar' : 'abrir'}</button>
```

| Patrón | Cuándo | Coste |
|---|---|---|
| Props simples | hoja sin variantes (Avatar, Spinner) | bajo |
| `cva`/variants | design-system con N variantes fijas | medio (ver [[88-design-systems-tokens]]) |
| Compound | grupos con estado compartido (Tabs, Accordion, Select) | medio |
| Headless hook | lógica compleja reusada en ≥2 skins | alto, paga en escala |

## Server vs Client components (la frontera que más se equivoca)
En RSC el default es **Server**; `'use client'` marca la *frontera*, y todo lo importado por debajo
se vuelve cliente. Patrón clave: **mantén client components como hojas** y pásales server-rendered
`children` para no arrastrar data-fetching al bundle del cliente.

```jsx
// layout.server.jsx — Server fetchea; ClientShell solo aporta interactividad
<ClientShell><ServerExpensiveTree/></ClientShell>  // children server cruzan la frontera sin "cliente-izarse"
```
- Server: data-fetching, secretos, deps pesadas (markdown, date libs) → 0 KB al cliente.
- Client: estado, efectos, listeners, browser APIs, Context con setters.
- Nunca importes un Server Component *dentro* de uno client; pásalo como prop/children.

## Gotchas
1. Compound con Context: si el padre re-renderiza, memoiza el `value` o todos los triggers re-render.
2. Props-getters headless deben **mergear** `onClick`/`ref` del consumidor, no pisarlos.
3. `forwardRef` dejó de ser obligatorio en React 19 (`ref` es prop normal) — limpia el boilerplate viejo.
4. No conviertas todo en headless: para una hoja sin variantes es sobre-ingeniería.

Cruza con [[91-nextjs-react-a-fondo-2026]], [[88-design-systems-tokens]] y [[87-state-management-avanzado]].
