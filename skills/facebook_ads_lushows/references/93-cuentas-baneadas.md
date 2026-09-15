# 93 — Cuentas baneadas: prevención y rescate

La cuenta publicitaria es el activo más frágil de toda la operación: se construye en meses y se pierde en un clic de un sistema automatizado. Lee este módulo ANTES de tener problemas (el 90% es prevención) o cuando ya te restringieron/inhabilitaron algo y necesitas apelar bien. Vocabulario: **restricción** (no puedes pautar con esa cuenta/página/perfil), **inhabilitación** (ban del activo), **verificación de negocio** (business verification: Meta confirma que tu empresa es real con documentos — cada vez más obligatoria para pautar en 2026), **Account Quality** (el panel de Meta donde vive todo esto: business.facebook.com/accountquality).

## Los triggers reales de baneo

1. **Violaciones de policy repetidas**: ads rechazados una y otra vez, claims prohibidos, categorías restringidas mal manejadas (ver 08/44). Cada rechazo suma; el patrón mata.
2. **Actividad inusual**: login desde IP/dispositivo raro, cambio súbito de método de pago, gasto que explota de la nada. Una cuenta nueva que pasa de $0 a $5M COP/día en 3 días le grita "fraude" al sistema — el historial de gasto se construye GRADUAL.
3. **Negocio no verificado**: en 2026 Meta empuja la **verificación de negocio** como requisito para muchas funciones; BM sin verificar, admin con perfil personal flojo (cuenta nueva, sin historial), datos de negocio inconsistentes con tus documentos = bandera.
4. **Deuda de pago**: tarjeta rechazada con saldo pendiente. Paga deudas el mismo día, siempre.
5. **Feedback negativo masivo de usuarios**: el Page Feedback Score baja cuando la gente reporta "no recibí el producto" / "no era lo prometido". No es policy: es tu operación (entregas, calidad, promesas del ad vs realidad, ver 48).
6. **Circumvention** (evasión): cualquier intento de trampear la revisión — cloaking, cuentas espejo tras un ban, editar el ad post-aprobación para cambiar el mensaje. Es la violación que entierra TODO el Business Manager, no solo una cuenta.

## Verificación de negocio: hazla ANTES de necesitarla (jun-2026)

Meta apretó la verificación en 2026. Hacerla con calma hoy te evita una restricción en el peor momento (a mitad de una campaña que vende). Pasos:

1. Business Settings → **Security Center** o **Centro de verificación** → iniciar verificación de negocio.
2. Datos del negocio que **coincidan exactamente** con tus documentos: razón social, dirección, teléfono, sitio web.
3. Documento: en Colombia, RUT o cámara de comercio (ver 04). El nombre del documento debe calzar con el del BM — la inconsistencia es la causa #1 de rechazo de verificación.
4. Verificación de dominio en Brand Safety (meta tag, DNS o archivo) — separada pero igual de importante.
5. Espera horas a días. Una vez verde, baja drásticamente tu probabilidad de restricción automática.

## El setup blindado (hazlo hoy, no después del susto)

- [ ] **Business Manager verificado** con documentos reales del negocio (RUT/cámara de comercio, ver 04) — ver sección anterior.
- [ ] **2FA activado en TODOS los admins** — un admin hackeado pauta porno con tu tarjeta y el ban es tuyo.
- [ ] Dominio verificado en Brand Safety.
- [ ] Método de pago estable (la misma tarjeta meses; ideal saldo prepago o tarjeta empresarial).
- [ ] Mínimo 2 admins de confianza (si banean el perfil de uno, el otro mantiene acceso).
- [ ] Historial de gasto gradual: escala ≤20-30% cada pocos días (ver 72), nunca saltos de 10×.
- [ ] Página de Facebook con contenido real y datos de contacto: las páginas cascarón pesan en contra.

## Higiene operativa semanal

- Revisa **Account Quality** cada semana (5 min): rechazos, restricciones, feedback score, estado de verificación.
- Ad rechazado → **edítalo de verdad** (cambia lo señalado) y solicita revisión. Re-subir el mismo ad idéntico una y otra vez = patrón de circumvention.
- No pautes "en el borde" de la policy por deporte: cada ad al límite es un boleto de rifa que no quieres ganar.
- Promesas del ad alineadas con lo que el cliente recibe: el feedback score se cuida en la operación, no en Ads Manager.

## Apelación paso a paso

1. **Dónde**: Account Quality → selecciona el activo restringido → **Solicitar revisión**. Es el único canal oficial que existe para todos.
2. **Qué escribir** (cuando hay campo de texto): factual y corto. Qué pasó, qué corregiste, confirmación de que entiendes la policy. **No ruegues, no amenaces, no cuentes tu vida**: lo lee (primero) una máquina. Plantilla:

   > "El anuncio [ID] fue rechazado bajo la política de [nombre de la política]. Hemos corregido lo señalado: eliminamos el claim [X], ajustamos la landing [URL] para que cumpla con [requisito], y revisamos el resto de la cuenta para asegurar consistencia. Entendemos y cumplimos las Políticas de Publicidad de Meta. Solicitamos una nueva revisión. Gracias."

3. **Tiempos realistas**: horas a varios días; casos complejos, semanas. No envíes 5 apelaciones seguidas — no acelera y ensucia.
4. **Escalación**: si tienes acceso al chat de soporte de Meta Business (cuentas con gasto suelen tenerlo: Help Center → contactar soporte / chat en vivo), abre caso ahí citando el ID de la apelación. Existe una segunda revisión en algunos casos; agótala antes de dar nada por muerto.
5. **Cuándo está muerta de verdad**: apelación rechazada en firme + sin canal de soporte + violación grave real (circumvention, fraude de pago). Ahí el activo no vuelve; protege el resto del BM.

### Tabla de apelación por tipo de restricción

| Qué se restringió | Dónde apelar | Qué corregir antes de apelar | Probabilidad de volver |
|---|---|---|---|
| **Un anuncio** (rechazo) | Account Quality → el ad → solicitar revisión | Quita el claim/imagen señalada; edita de verdad | Alta si corriges |
| **Cuenta publicitaria** (restringida) | Account Quality → la cuenta → solicitar revisión | Autopsia de qué patrón la disparó; pausa lo que esté al borde | Media — depende del motivo |
| **Página / perfil personal** | Account Quality / Centro de cuentas | Verifica identidad si lo piden; 2FA | Media |
| **BM entero** (circumvention) | Soporte + revisión; casi siempre terminal | Nada que corregir si fue evasión real | Baja — protege otros activos |
| **Deuda de pago** | Pagar la deuda primero, luego revisión | Paga el saldo el mismo día | Alta una vez pagado |

## El día del ban: protocolo de las primeras 24 horas

1. **No entres en pánico ni crees nada nuevo**: la cuenta espejo creada a las 2 horas del ban es la confesión de circumvention que convierte una restricción recuperable en ban permanente del BM.
2. Identifica QUÉ se restringió (Account Quality): ¿la cuenta publicitaria, la página, tu perfil personal o el BM entero? Cada uno tiene su propia apelación (tabla arriba).
3. Lee el motivo citado y haz autopsia honesta: ¿qué ad, claim o comportamiento pudo dispararlo? Corrige eso ANTES de apelar (borra/edita los ads en el borde).
4. Apela una sola vez, bien (sección anterior), y anota fecha e ID del caso.
5. Mientras esperas: pausa cualquier otro activo que tenga el mismo problema (mismo claim en otra campaña) — un segundo strike durante la apelación la mata.

## Plan B legítimo (y la línea roja)

- **Legítimo**: tener una segunda cuenta publicitaria dentro del MISMO BM verificado, con campañas/píxel/activos duplicados y algo de historial de gasto. Si una cuenta cae por error del sistema, operas con la otra mientras apelas. Página de respaldo administrada y con contenido, lista.
- **Línea roja — NO hacer jamás**: comprar cuentas "agency" truchas o cuentas envejecidas, granjas de perfiles, VPN/antidetect para simular otra identidad, "recuperadores" mágicos que piden acceso total a tu BM (te roban o te queman), crear un BM nuevo con otra cédula para evadir un ban. Todo eso ES circumvention: cuando el grafo de Meta conecta los puntos (y los conecta: dispositivo, pago, dominio, IP), entierra el negocio ENTERO de forma permanente.

## Errores comunes — blacklist

- Operar meses sin verificar el BM "porque funciona": en 2026 la verificación es cada vez más requisito; funciona hasta el primer review automático.
- Datos del negocio que no coinciden con el documento al verificar: causa #1 de rechazo de verificación.
- Un solo admin, sin 2FA, con su perfil personal de toda la vida: punto único de fallo.
- Re-subir el ad rechazado idéntico "a ver si pasa": cada intento acerca el ban.
- Escalar 10× el gasto en una cuenta nueva el primer fin de semana bueno.
- Apelar con un párrafo emocional de 500 palabras sobre tu familia: el revisor necesita hechos y correcciones (usa la plantilla).
- Comprar una cuenta o alquilar un BM ajeno tras el ban: conviertes un problema recuperable en uno terminal.
- Ignorar el feedback score porque "eso es de logística": Meta banea por clientes furiosos igual que por policy.
