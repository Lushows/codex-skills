# 139 — Calidad de datos y governance

La **calidad de datos y su governance** (gobierno de datos: las reglas para mantenerlos limpios, únicos y vigentes) es lo que evita que tu warehouse de leads (`138`) se pudra hasta volverse inservible. Los datos B2B **se degradan solos**: la gente cambia de trabajo, las empresas quiebran, los emails mueren, los duplicados se acumulan. Sin governance, en 12 meses tu base preciosa es un cementerio que rebota, te manda a spam (`45`) y te hace escribirle tres veces a la misma persona. Este módulo son las **reglas y rutinas** para mantener el activo vivo. Es primo de la verificación de listas (`28`) y de la higiene del CRM (`77`), pero mira el **panorama completo y continuo**, no una limpieza puntual.

## El principio: los datos B2B se degradan ~2–3 % al mes

El número que debes interiorizar: la data de contactos B2B **decae 20–30 % al año** (algunas fuentes citan hasta 30 %+). Eso es ~2–2,5 % **cada mes** que se vuelve incorrecto: la persona se fue (job change, `133`), el email dejó de existir, el cargo cambió, la empresa cerró. La consecuencia es directa y cara:

- **Rebotes ↑ → deliverability ↓.** Mandar a emails muertos dispara tu bounce rate y te tumba la reputación de envío (`46`); pasas a spam para **todos**, no solo para los muertos.
- **Duplicados → contactas 3 veces a la misma persona**, quedas como spammer (`07`).
- **Score mentiroso** (`137`): decides sobre datos falsos.
- **SDRs frustrados** llamando a números y cargos que ya no existen.

Governance no es limpieza de una vez; es un **proceso continuo** que compensa ese decaimiento constante.

## Los cuatro frentes de la calidad de datos

| Frente | Problema que ataca | Rutina |
|---|---|---|
| **Vigencia (freshness)** | El dato caduca (job change, empresa cerró) | Re-verificar y re-enriquecer por lotes cada 3–6 meses |
| **Deduplicación** | El mismo contacto/cuenta repetido | Dedup automático por email/dominio + fuzzy match |
| **Normalización** | "Bogota" vs "Bogotá" vs "BOG"; "CEO" vs "Director General" | Reglas de formato estándar al ingresar |
| **Cumplimiento (compliance)** | Datos que no puedes/debes tener (GDPR, opt-outs) | Respetar bajas, base legal, borrado a pedido (`07`) |

### Vigencia — el frente que más gente ignora
Un email verificado hoy no es verificado para siempre. Re-verifica tu base activa **antes de cada campaña grande** y haz un barrido completo cada 3–6 meses (NeverBounce/ZeroBounce, `28`). Señal barata de decaimiento: **un email que empieza a rebotar suele significar que la persona se fue** — eso es un job change gratis, busca dónde está ahora (`133`).

### Deduplicación — la disciplina invisible
Los duplicados entran por todos lados: compras la misma cuenta en dos fuentes, el mismo contacto con dos emails, "Restaurante El Sol S.A.S" vs "El Sol". Reglas:
- **Clave única** por email (contactos) y por dominio (cuentas).
- **Fuzzy match** para nombres casi iguales (mayúsculas, espacios, tildes, sufijos legales).
- **Dedup ANTES de enriquecer** (`138`): no gastes créditos en alguien que ya tienes.
- Al fusionar, **conserva la mejor versión de cada campo** sin perder historia (la actividad de ambos registros se une, no se borra).

> Lección real de campo (proyecto AVISPA'O): deduplicar por match **exacto** (sensible a mayúsculas/espacios) deja pasar duplicados; hay que normalizar **antes** de comparar (minúsculas, sin tildes, sin espacios sobrantes). Y al borrar/fusionar por API, **revisa el error que devuelve** antes de asumir que funcionó.

### Normalización — para que segmentar y el score funcionen
Si "Bogotá" está escrito de seis formas, tu filtro por ciudad falla y tu score (`137`) también. Estandariza al ingresar: país/ciudad con lista fija, cargos mapeados a categorías (`22`), nombres de empresa sin sufijos legales para comparar.

### Cumplimiento — la línea que no se cruza
Respeta **siempre** las bajas (opt-out): quien pidió no ser contactado sale y no vuelve (`45`, `07`). Ten base legal para los datos que guardas (interés legítimo B2B en muchos marcos, consentimiento donde aplique), y capacidad de **borrar a pedido** (GDPR/derechos del titular). En LatAm aplica la ley de datos local. Esto no es opcional: es riesgo legal y de reputación.

## La rutina de governance (cadencia sugerida)

```
CONTINUO (automático):
  - Dedup al ingresar cualquier dato nuevo (clave única + fuzzy).
  - Normalización al ingresar (ciudad, cargo, empresa).
  - Registrar opt-outs y excluirlos de todo envío al instante.
  - Sacar de la cola cualquier email que rebote (hard bounce).

MENSUAL:
  - Revisar bounce rate y sender reputation (`46`).
  - Marcar "sospechosos de job change" (emails que empiezan a fallar) → `133`.

CADA 3–6 MESES:
  - Re-verificar la base activa por lotes (`28`).
  - Re-enriquecer datos clave que caducan (cargo, tamaño, technographics `134`).
  - Archivar cuentas "muertas" (cerraron, nunca responden) para no ensuciar métricas.
```

Un **dueño** claro de la calidad de datos (aunque seas tú solo) evita el "todos y nadie". Define quién es responsable de que la base esté limpia.

## Errores comunes

- **Comprar más datos sin limpiar los que tienes** → apilas basura sobre basura; el volumen no arregla la calidad.
- **Verificar una vez y creer que es para siempre** → el dato decae 2–3 %/mes; re-verifica.
- **Dedup por match exacto** → deja pasar duplicados; normaliza antes de comparar.
- **Ignorar los opt-outs** → riesgo legal + reputación destruida (`07`).
- **No sacar los hard bounces de inmediato** → cada reenvío a un muerto te hunde la deliverability (`45`, `46`).
- **Sin dueño de la calidad** → nadie limpia, la base se pudre en silencio.

## Frontera y siguiente paso

La governance mantiene el **activo** (`138`) vivo para que la máquina de outbound funcione; **convencer y cerrar** con esos datos limpios es `ventas_lushows`. Empieza por lo continuo: activa dedup + normalización al ingresar y saca los opt-outs y hard bounces al instante. Agenda una re-verificación por lotes (`28`) cada trimestre. Para la limpieza puntual de una lista antes de enviarla → `28`; para la higiene y disposición dentro del CRM día a día → `77`; para el marco ético/legal completo → `07`. Con esto cierras el Bloque 13: datos con cobertura (`130`), intent (`131`, `132`), señales (`133`–`136`), un score que prioriza (`137`), una base que los acumula (`138`) y limpia (`139`).
