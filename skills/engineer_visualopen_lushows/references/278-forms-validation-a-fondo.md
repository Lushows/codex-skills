# 278 · Forms y validación a fondo: react-hook-form + Zod

> El form es donde la UI toca datos sucios del usuario. La regla de oro 2026: **un solo schema Zod**
> valida en cliente (UX rápida) y en servidor (verdad), sin duplicar reglas.

## Por qué uncontrolled gana
react-hook-form (RHF v7, sigue siendo el default) usa inputs **no controlados**: registra refs y lee
valores on-submit, evitando un re-render por tecla. Para forms grandes esto es la diferencia entre
fluido y laggy. TanStack Form es la alternativa con tipado más estricto e integración de ecosistema,
pero pesa más (~20KB vs RHF ~9KB). [verificado: comparativas 2026]

```jsx
const schema = z.object({
  email: z.string().email('Email inválido'),
  qty: z.coerce.number().int().min(1).max(99),       // coerce: "3" → 3 desde el input
})
type Form = z.infer<typeof schema>                    // tipo derivado del schema, fuente única
const { register, handleSubmit, formState:{ errors, isSubmitting } } =
  useForm<Form>({ resolver: zodResolver(schema), mode:'onTouched' })
<input {...register('email')} aria-invalid={!!errors.email} />
{errors.email && <span role="alert">{errors.email.message}</span>}
```

## El schema único cliente↔servidor
La validación de cliente es **UX**, no seguridad. El servidor **re-valida siempre** con el mismo schema.
En Next con Server Actions, `schema.safeParse(formData)` antes de tocar la DB.

```jsx
'use server'
export async function createOrder(_, formData: FormData) {
  const parsed = schema.safeParse(Object.fromEntries(formData))
  if (!parsed.success) return { errors: parsed.error.flatten().fieldErrors } // mismo shape al cliente
  await db.orders.insert(parsed.data)
  return { ok: true }
}
```
En cliente, `useActionState(createOrder, init)` lee ese retorno y `useFormStatus` da `pending` sin estado manual.

## Validación async y server-truth (email único, cupón)
No metas reglas de DB en el schema de cliente. Valida con un fetch debounced y refleja el resultado:
```jsx
setError('coupon', { message: 'Cupón vencido' })   // error imperativo desde la respuesta del server
```

## UX de errores (lo que separa amateur de pro)
| Decisión | Recomendado | Por qué |
|---|---|---|
| Cuándo mostrar | `onTouched`/`onBlur`, no `onChange` | no gritar mientras escribe |
| Tras submit fallido | revalidar `onChange` | feedback inmediato al corregir |
| Foco | mover foco al 1er campo inválido | accesibilidad + velocidad |
| Anuncio | `role="alert"` + `aria-invalid` | screen readers leen el error |
| Submit | deshabilitar con `isSubmitting`, no ocultar | evita doble envío sin esconder acción |

## Campos complejos
- Inputs controlados de 3os (selects custom, date pickers): envuélvelos en `<Controller>`.
- Arrays dinámicos (líneas de pedido): `useFieldArray` — keys estables, no el índice.
- Multi-step wizard: un schema por paso + merge final; persiste estado en `useRef`/store, no remontes.

## Gotchas
1. Sin `z.coerce`, todo input numérico llega como `string` → `min()` falla silencioso.
2. `mode:'onChange'` en form grande reintroduce el re-render-por-tecla que RHF evita.
3. `setError` con `{ type:'server' }` lo borra el próximo submit; para persistente usa `shouldUnregister:false`.
4. Confiar solo en validación de cliente = bypass trivial con curl. Server re-valida o no validaste.
5. `Object.fromEntries(formData)` pierde checkboxes múltiples y files → usa `getAll` para esos.

Cruza con [[277-component-architecture-patterns]], [[91-nextjs-react-a-fondo-2026]] y [[280-data-fetching-caching-frontend]].
