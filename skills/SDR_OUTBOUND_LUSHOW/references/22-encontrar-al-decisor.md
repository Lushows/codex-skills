# 22 — Encontrar al decisor

Ya tienes la lista de empresas (`21`). Ahora hay que dar con **la persona correcta dentro de cada cuenta**: no "alguien de la empresa", sino quien siente el dolor que resuelves y tiene poder o influencia para comprar. Escribirle al perfil equivocado es el desperdicio más común del outbound: quemas el toque, quemas la cuenta y a veces ni te reenvían. Este módulo es cómo identificar por **cargo y función** a quién contactar, en empresas grandes y en PYMES.

## El principio: función > título

Los títulos mienten y cambian por país e industria. Lo que no cambia es la **función**: ¿quién sufre el problema que resuelves y quién firma? Mapea a la persona por lo que **hace**, no por cómo se llama el cargo. En una empresa grande hay un **comité de compra** (ver `11`): decisor económico (firma), champion (empuja internamente), usuario (sufre el dolor), influenciador y bloqueador. Tú apuntas primero al que **más siente el dolor y tiene voz** — normalmente un manager o director del área afectada, no el CEO (que delega).

Regla de tamaño de empresa:
- **PYME (1–50 empleados):** el decisor suele ser el **dueño/fundador/gerente general**. Una sola persona. Fácil de identificar, difícil de alcanzar (está ocupado).
- **Mediana (50–500):** el **director/jefe del área** (Head of, Gerente de X) es el champion; su VP o el gerente general aprueba.
- **Grande (500+):** multi-threading (ver `162`) — contactas 2–3 personas: el usuario-líder + su director. El VP/C-level entra tarde.

## Cómo mapear el cargo objetivo (paso a paso)

1. **Traduce tu solución a un dolor de un área.** ¿A quién le explota el problema? Si vendes software de costos de restaurante → dolor del **dueño / gerente de operaciones / chef administrativo**. Si vendes reclutamiento → **Head of Talent / Gerente de RRHH**. Escribe el/los cargos objetivo antes de buscar.
2. **Arma la lista de títulos equivalentes** (varían por idioma/país). Ej. para "compras": *Gerente de Compras, Jefe de Abastecimiento, Purchasing Manager, Procurement, Head of Supply.* La usarás como filtro booleano (ver `26`).
3. **Busca a la persona** en la cuenta (métodos abajo).
4. **Valida el fit del contacto:** ¿el cargo real coincide? ¿sigue en la empresa? (LinkedIn "activo", `133` job change).

## Dónde encontrar a la persona — por método

| Método | Cómo | Mejor para |
|---|---|---|
| **LinkedIn Sales Navigator** | Filtro por empresa + *Función* + *Seniority* + título booleano (ver `26`) | B2B, medianas y grandes |
| **Apollo / ZoomInfo** (ver `25`) | Buscas la empresa → te lista sus empleados por cargo, con email | Volumen, ya trae el correo |
| **LinkedIn gratis** | Entra a la página de la empresa → pestaña *Personas* → filtra por cargo | Sin presupuesto, pocas cuentas |
| **La web de la empresa** | Páginas "Equipo/Nosotros/Contacto"; PYMES ponen al dueño | PYMES y locales |
| **Google** | `site:linkedin.com/in "Gerente de Compras" "Empresa X"` | Encontrar el nombre exacto |
| **Instagram/Facebook** | En PYMES LatAm el dueño aparece en la bio o etiquetado | Negocios locales (ver `24`) |

**Filtros clave en Sales Navigator/Apollo:** *Function* (Operations, Finance, Marketing, HR, IT, Sales), *Seniority level* (Owner, CXO, VP, Director, Manager) y *Job title* con booleano. Combinar Función + Seniority es más robusto que solo el título (que la gente escribe de mil formas).

## Ejemplo real: decisor en un restaurante (PYME) vs. en una cadena

```
CASO A — Restaurante independiente (PYME):
  Decisor = dueño o gerente general (una persona, todo pasa por él/ella).
  Búsqueda: LinkedIn/IG → "propietario / gerente / administrador" del negocio.
  Muchas veces el nombre sale en Google Maps (respuestas a reseñas) o IG.

CASO B — Cadena de restaurantes (mediana):
  Champion/usuario = Gerente de Operaciones o Director de Costos/Compras.
  Aprobador = Gerente General / Director Financiero.
  Sales Nav: Company = "Cadena X" AND Function = Operations OR Finance
             AND Seniority = Director OR Manager.
  Multi-threading: contacta al de Operaciones (dolor) y avisa al de Finanzas.
```

Filtro booleano de título para Sales Nav (compras/costos, ES+EN):
```
("gerente de compras" OR "jefe de compras" OR "director de operaciones"
 OR "purchasing manager" OR "procurement" OR "head of operations"
 OR "gerente de costos" OR "administrador")
```

## Cuántos contactos por cuenta

- PYME: **1** (el dueño). No hay comité.
- Mediana: **1–2** (champion + su jefe).
- Grande/enterprise: **2–4** (multi-threading, ver `162`). Más de una puerta a la misma cuenta sube mucho la tasa de reunión, pero coordina el mensaje para no parecer spam interno (`127`).

## Errores comunes (qué NO hacer)

- **Apuntar siempre al CEO.** En medianas/grandes delega y no te lee; y si te reenvía, llegas sin contexto. Ve al que siente el dolor.
- **Filtrar solo por título exacto.** Pierdes a la mitad (los escriben distinto). Usa Función + Seniority + booleano amplio.
- **No validar que siga en la empresa.** Un contacto que se fue = rebote seguro. Cruza con LinkedIn actual (`133`).
- **Contactar 6 personas de la misma PYME.** En una empresa chica eso es acoso; una puerta basta.

## Frontera

Identificar y llegar al decisor correcto = esta skill. **Convencerlo, manejar sus objeciones a fondo y cerrar** = `ventas_lushows`. Si en una empresa grande hay que "vender internamente" navegando el comité (MEDDIC, champion, poder), esa conversación de venta compleja vive en `ventas_lushows`; aquí solo lo identificas y agendas.

## Siguiente paso

Con el nombre + apellido + empresa + `linkedin_url` de cada decisor, pasa a `23` para conseguir su correo (patrón + herramienta + verificación) y a `24` para teléfono/WhatsApp.
