# 28 · Equipo y multi-sede

> Fuentes: `src/lib/delegacion.ts` (extraer + procesar delegación, plantilla `avis_saludo`), `supabase/migration-02-equipo.sql` (tablas `puntos` + `miembros`) y `migration-03-traspaso.sql` (info vive en el punto). Atribución multi-admin: ver `04-facturas-dian-cruce.md`; planes: `03-producto-avispao.md`.

Un negocio no es una sola persona. El dueño abre, pero quien manda las facturas del día a día suele ser el administrador de cada local. AVIS está hecho para eso: **la información vive en el PUNTO (la sede), no en la persona**. Así, si cambia el administrador, no se pierde nada.

## El modelo: puntos + miembros
- **`puntos`** = las sedes/locales de un comercio (`nombre`, `direccion`, `ciudad`). Un comercio tiene uno o varios.
- **`miembros`** = las personas que le escriben a AVIS por WhatsApp (distinto del login web). Cada miembro tiene `whatsapp_phone`, `rol`, `estado` y un `punto_id` que lo ata a su sede.
- **Documentos, obligaciones y el `proceso_state`** cuelgan del `punto_id` (migración 03) → el local es el dueño de la información.

## Roles
| Rol | Quién es | Qué puede |
|---|---|---|
| **dueño** | abre la cuenta | ve todas las sedes, delega administradores, recibe reportes globales |
| **administrador** | encargado de un punto | manda facturas y papeles de SU sede; AVIS le reporta solo lo suyo |
| **empleado** | apoyo en un punto | atado a un `punto_id`, según se configure |

`estado`: **invitado** (le llegó la invitación, aún no escribe) → **activo** (ya respondió) → **inactivo**.

## Delegar un punto a un administrador
El dueño le escribe a AVIS en lenguaje natural: *"mi admin de Chapinero es Juan, 320 866 5248"*. El flujo (`delegacion.ts`):
1. **`pareceDelegacion`** — filtro barato: detecta intención (*deleg/asign/encarg/mi admin…*) + algo que parece teléfono.
2. **`extraerDelegacion`** — Gemini saca `adminNombre`, `adminTelefono` y `puntoNombre` (nunca inventa; deja `null` lo que no diga).
3. **`normalizarTelefono`** — móvil colombiano a `57XXXXXXXXXX` (asume `57` si falta indicativo).
4. **`procesarDelegacion`** — busca/crea el `punto`, hace `upsert` del `miembro` (`rol: administrador`, `estado: invitado`, `onConflict: comercio_id,whatsapp_phone`) y le manda al admin la plantilla aprobada **`avis_saludo`** con `[nombre, "Negocio Sede"]`.

Si falta el número, AVIS no inventa:
> *"Casi — me falta el número de **Juan** con indicativo (ej. +57 320 866 5248). ¿Me lo pasas?"*

Confirmación al dueño cuando sale la invitación:
> *"Listo ✅ Le escribí a **Juan** para el punto **Chapinero**. Apenas responda 'Hola', arranco a acompañarlo."*

Y si la plantilla aún no está aprobada por Meta, queda anotado igual y se envía solo:
> *"Anoté a **Juan** como encargado de **Chapinero** 📝. En cuanto Meta apruebe la plantilla de invitación, le llega el mensaje automáticamente."*

## Cada admin manda facturas → se atribuyen a su sede
Cuando un administrador le escribe a AVIS, su `whatsapp_phone` lo identifica como `miembro` y su `punto_id` dice a qué sede pertenece. Las facturas que sube se guardan con ese `punto_id`, así que **cada gasto cae en el local correcto** sin que nadie tenga que aclararlo. El dueño ve el consolidado; el admin ve solo lo suyo. (El cruce sin doble conteo es el mismo de `04-facturas-dian-cruce.md`.)

## Traspaso de un punto (cambia de administrador)
La migración 03 garantiza una **transición suave**: como documentos, obligaciones y `proceso_state` viven en el punto, el nuevo administrador **hereda todo** apenas entra. Se registra en la tabla **`traspasos`** (`admin_saliente`, `admin_entrante`, `resumen`) para auditoría y contexto. AVIS le da la bienvenida al nuevo encargado con el estado al día —en qué va cada papel, qué falta— en vez de empezar de cero.

## Cómo reporta AVIS por sede
- Al **administrador**: solo su punto (sus papeles, sus vencimientos, sus gastos).
- Al **dueño**: la foto completa, sede por sede, con el consolidado del negocio.

## En qué plan vive
**Multi-sede, multi-usuario y delegación al equipo son del plan Empresarial** ($49.900/mes). En Básico/Avispa'o el negocio es de una sola persona. (Ver `03-producto-avispao.md`.)

---

## 🔄 FLUJO CANÓNICO end-to-end (fuente de verdad — establecido 23-jun-2026 con Luis)

> Principio rector: **la información vive en el PUNTO (la sede), no en la persona.** El **dueño supervisa**; el **personal opera**. La labor del día a día del local (papeles + facturas de la sede) es **casi neta del personal** que interactúa con AVIS por WhatsApp.

### 1. Identidad (quién escribe)
`whatsapp_phone` resuelve el rol (`procesarConversacion` → `resolverComercioPorTelefono`):
- existe en `comercios` → **DUEÑO** (respeta su espacio activo Personal↔empresa).
- existe en `miembros` (estado `activo`) → **PERSONAL** (admin de sede), atado a su `punto_id`.
- ninguno → prospecto nuevo.

### 2. Recibir facturas
- **Personal:** SOLO por **foto** (WhatsApp). Se atribuye a su sede automáticamente: `guardarFactura` estampa `datos.punto_id` del miembro. El personal **NO conecta correo** — es un perfil de un 3ro (lo paga la empresa); si lo intenta, AVIS le aclara que **eso lo hace el dueño** y que con foto basta. (Regla de oro 8.)
- **Dueño (empresa):** conecta su correo UNA vez (Gmail/Outlook/cualquiera) y las facturas entran solas; también puede mandar foto. El correo es **a nivel de comercio**, no por sede.

### 3. Generar documentos del local (saneamiento, capacitación, SG-SST, bioseguridad)
- **El personal SÍ los genera** para SU sede (es la labor del local). En `flujoMiembro`, "genérame el [doc]" → `generarDocumento(db, comercio_id, tipo, punto_id)` → se guarda **atado al punto** (migración 11: `documentos_generados.punto_id`).
- El miembro recibe el borrador con un **enlace de documento puntual** (`urlDoc`, token propósito `doc`) que abre SOLO ese documento — **NUNCA** el panel del dueño (confidencialidad / regla 11). El dueño y el equipo sí lo ven con sesión.
- **AVIS le avisa al dueño** (best-effort, dentro de su ventana de 24h): "*[nombre]* (*sede*) generó el borrador de *X*". ⚠️ *Limitación actual:* fuera de la ventana de 24h ese aviso no llega (haría falta una plantilla de Meta) — el documento igual queda en el panel del dueño.
- El gate por perfil (`aplica`) NO bloquea una generación pedida explícitamente (ver `23-plantillas-de-documentos.md`).

### 4. Guardar y fluir al reporte del dueño
- Facturas → `documentos` con `datos.punto_id`. Documentos generados → `documentos_generados` con `punto_id`. Obligaciones/proceso → cuelgan del punto (migración 03).
- **Reporte del personal:** acotado a SU punto (`cargarReporteFacturas(comercio_id, punto_id)`).
- **Reporte del dueño:** consolidado del negocio **sede por sede** (`sedesDesglose`). El dueño no maneja los papeles de cada local; los **ve** consolidados.

### 5. Empleado → INDEPENDIENTE (nuevo, 23-jun-2026)
Cuando un miembro cuenta que se independizó o montó su propio negocio (`pareceIndependizacion`: "me independicé", "monté mi negocio/local", "ahora soy mi propio jefe", "trabajo por mi cuenta"):
- AVIS lo **reconoce por el número y recuerda su nombre**, lo **felicita con humor** ("¿o sea que ahora el jefe eres TÚ?"), como un **amigo que vuelve**.
- Le **abre su PROPIA cuenta** (`crearOTraerComercio` con su teléfono) y lo **suelta del punto** del antiguo empleador (`miembros.estado = inactivo`). La data del local se queda en el punto (no se pierde nada para el ex-empleador).
- Es **cliente nuevo**: a partir de ahí entra al flujo de dueño → onboarding de SU negocio → compra del plan **según su necesidad** (la suscripción que le sirva). AVIS arranca preguntándole qué negocio montó y en qué ciudad.

## Roles que SÍ / NO hace cada quien
| | Dueño | Personal (admin de sede) |
|---|---|---|
| Conectar correo | ✅ | ❌ (solo foto) |
| Mandar facturas | ✅ (todas las sedes/su espacio) | ✅ (solo su sede, por foto) |
| Generar docs del local | ✅ | ✅ (de su sede; avisa al dueño) |
| Ver reporte | ✅ consolidado por sede | ✅ solo su sede |
| Papeles generales (Cámara, RUT, renta) | ✅ los lleva él | ❌ "eso lo lleva el dueño" |
| Delegar / pagar / vender | ✅ | ❌ |

## 🗂️ Mapa de flujos con IDs (claridad — 23-jun-2026)
Cada paso tiene un ID para hablar de los flujos sin ambigüedad (úsalos en comentarios/logs/diagramas).

**DUE · Dueño (el cliente):** `DUE-0` identidad por número · `DUE-1` onboarding del negocio · `DUE-2` sube factura (foto/correo) · `DUE-3` genera documentos · `DUE-4` resumen ejecutivo (ventas/compras/margen/IVA + gráfico) · `DUE-5` cumplimiento/papeles + bóveda · `DUE-6` invita administrador (delegación) · `DUE-7` invita contador (pide correo) · `DUE-8` pago/plan · `DUE-9` referido del dueño.

**PER · Personal/admin de sede (solo dentro de empresa multi-sede):** `PER-0` invitación (plantilla `avis_saludo`) · `PER-1` activación/bienvenida (pide papeles del local) · `PER-2` factura por FOTO → se atribuye a su sede (`punto_id`) · `PER-3` *lista* de sus facturas + link ver/descargar (⛔ sin cifras acumuladas) · `PER-4` papeles del local (generales → al dueño) · `PER-5` genera docs del local (avisa al dueño) · `PER-6` se independiza → cuenta nueva (salta a DUE).

**CON · Contador (perfil que habilita el dueño, SOLO LECTURA):** `CON-0` invitación por correo · `CON-1` registro web (nombre) · `CON-2` vínculo WhatsApp (código `AC-`) · `CON-3` reporte (general + por sede) · `CON-4` activar/desactivar avisos diarios · `CON-5` panel solo-lectura + reporte "no cuadra"/fugas · `CON-6` referido $200.000/cliente · `CON-7` espacio personal del contador (roadmap).

**IND · Empleado→independiente:** `IND-0` detección ("monté mi negocio") · `IND-1` felicita + abre su cuenta → entra como DUE.

## ⚠️ El CLIENTE es el DUEÑO — el personal NO es un cliente aparte
(Corrección de modelo, 23-jun-2026, confirmada por Luis. Fuente visual: `Flujo-General-de-Uso.pdf`.)

- **El cliente = el DUEÑO** (la cuenta que contrata). Hay **dos tipos de cuenta**:
  1. **Individual** — un negocio o persona, **SIN personal**, plan gratis o pago. El dueño hace todo (foto/correo → su reporte).
  2. **Empresa multi-sede** (plan Empresarial) — el dueño tiene varias sedes y **despliega administradores**. **Este es el ÚNICO contexto donde existe "personal".**
- **El personal (admin/empleado) NO es un tipo de cliente.** Solo existe dentro de una empresa con sedes. Un empleado suelto, si no abre su propia cuenta, es una **cuenta normal (gratis)** — por eso el flujo *empleado→independiente* le crea SU propia cuenta.
- **Interconexión de facturas:** cada sede manda facturas por foto → cada una lleva su `punto_id` → se atribuye sola a su sede → **consolidan en el reporte del DUEÑO**, que tiene acceso a TODAS las facturas (en foto) de cada local, consolidado y sede por sede.

## 🧭 PERFILES OPERACIONALES POR ÁREA (visión 23-jun-2026, Luis — el valor premium)
La idea que sube el precio: el dueño habilita **perfiles por área**, cada uno **solo lectura** con
SU corte de los datos. **La misma data, distintos cortes → detectar fugas y comparativas.** El
contador es el PRIMER perfil ya construido; se generaliza el modelo a más áreas.

| Perfil | Qué VE (su corte) | Valor que da |
|---|---|---|
| 👑 **Dueño** | Todo: resumen ejecutivo + drill-down a la totalidad | la foto completa, decide |
| 🧮 **Contabilidad** (contador) | Facturas cruzadas, IVA, "no cuadra"/fugas, export | declaración-ready, detecta fugas |
| 🛒 **Compras** | Compras por proveedor/categoría, **alzas de precio, duplicados, sobreprecio** | fuga de sobrecostos, negociar proveedor |
| 💰 **Ventas** | Ventas, lo más vendido, ingresos, **márgenes por producto** | comparativa de qué deja más |
| 🧑‍🍳 **Personal/sede** | Solo la *lista* de sus facturas + ver/descargar (PER-3) | operación, sin cifras |

**Cruces de valor (lo que nadie más da fácil):** compras vs ventas → **margen / food cost** · fugas
(facturas sin cruce, duplicados, gastos hormiga, sobreprecio) · comparativas por **sede / periodo /
proveedor**. **Cada perfil = un filtro/vista sobre los MISMOS datos** (no silos: un solo origen).

**Implementación (a futuro):** generalizar el modelo de acceso (como `contador_acceso`) a una tabla
de **perfiles** con un campo `rol` (`dueno|contabilidad|compras|ventas`), cada rol con su vista
scopeada y su canal (web + WhatsApp). El contador ya es ese patrón → se extiende.

**Pricing:** estos perfiles operacionales son **tier alto** (Negocio/Empresa). El precio se fija con
**`economist_lushows`** (valor percibido + disposición a pagar por "ver mis fugas por área").

## 🧮 Perfil CONTADOR (diseñado 23-jun-2026 — pendiente de construir)
Un **perfil adicional que el DUEÑO habilita** para su contador. Idea de Luis; doble propósito: **valor** (el contador revisa) + **canal de REFERIDOS** (el contador trae más negocios).

- **Invitación:** el dueño le dice a AVIS que quiere dar acceso a su contador → AVIS pide *"envíame el correo de tu contador"* → **envía un correo** (Resend) que **obliga al contador a registrarse** y le abre su acceso.
- **Acceso del contador = SOLO LECTURA (visual).** Ve las **facturas cruzadas** (foto ↔ electrónica del correo, sin doble conteo) y, sobre todo, un **reporte de "no cuadra"**: lo que **no corresponde a nada** — facturas huérfanas, sin cruce, sin clasificar, sospechosas → para **revisar y analizar cada fuga** o factura que no cuadre. NO edita, NO sube, NO ve papeles de cumplimiento (eso es del dueño).
- **Referidos:** por este perfil se lanza publicidad de referido — el contador (que atiende varios negocios) trae clientes nuevos. El perfil contador lleva su **link de referido**.
- *Decisiones abiertas:* canal (panel web de solo lectura vs WhatsApp), 1 contador por comercio vs 1 contador multi-cliente (importa para el referido), y el detalle del "registro" del contador.

> **Roadmap:** perfil contador (arriba) · permisos finos por empleado · traspaso iniciado por el propio admin saliente · resumen de traspaso autogenerado por IA desde el `proceso_state` del punto · **plantilla de Meta para avisar al dueño fuera de la ventana de 24h** cuando un admin genera un documento o sube facturas.
