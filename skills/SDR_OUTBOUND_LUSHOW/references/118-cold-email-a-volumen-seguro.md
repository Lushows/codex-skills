# 118 — Cold email a volumen seguro

Este módulo junta todo el Bloque 11 en la pregunta que importa a escala: **¿cómo mando miles de correos fríos al día sin morir?** La respuesta no es un truco, es una **matemática de buzones** más disciplina de operación. Todo lo anterior —flota multi-dominio (ver `110`), DMARC estricto (ver `111`), warmup en oleadas (ver `112`), monitoreo (ver `113`)— existe para sostener volumen sin quemarte. Aquí lo integramos en un sistema con números concretos, para que sepas exactamente cuántos buzones necesitas, qué volumen puede aguantar cada uno, y cuáles son las líneas rojas que nunca cruzas. **El volumen seguro es un resultado del diseño, no de la suerte:** se construye hacia atrás desde tu meta, con margen de seguridad incorporado.

## El principio inamovible: el volumen vive en los buzones, no en el envío

Repetido porque es la ley que más se rompe (ver `44`): **no subes el volumen subiendo el límite por buzón; lo subes agregando buzones.** Un buzón caliente y sano aguanta ~30–40 correos fríos/día. Para mandar 2.000/día no configuras 20 buzones a 100 (suicidio) — montas ~60 buzones a 33. La fórmula que gobierna todo:

```
Correos/día seguros = número de buzones sanos × límite por buzón (25-40)
Buzones necesarios  = correos/día objetivo ÷ límite por buzón
Dominios necesarios = buzones ÷ 2-3 (máx 3 buzones por dominio; ver 110)
```

**Usa el límite BAJO del rango (25–33) a gran volumen.** El margen de seguridad es lo que te salva cuando un lote de lista sale peor de lo esperado. Para los cálculos exactos a tu meta, apóyate en `Matematicas_lushows`.

## La tabla de dimensionamiento (a 33/buzón, 3 buzones/dominio)

| Correos/día | Buzones | Dominios | Prospectos/mes (~22 días) | Costo infra aprox./mes |
|---|---|---|---|---|
| 300 | 9 | 3 | ~6.600 | ~$70–120 |
| 600 | 18 | 6 | ~13.200 | ~$140–240 |
| 1.000 | 30 | 10 | ~22.000 | ~$230–400 |
| 2.000 | 60 | 20 | ~44.000 | ~$450–800 |
| 5.000 | 150 | 50 | ~110.000 | ~$1.100–2.000 |

Costo incluye dominios (~$10–15/año c/u) + buzones (~$1.5–7/buzón/mes según proveedor/revendedor; ver `110`) + plataforma de envío (Instantly/Smartlead ~$37–97/mes escalando por buzones). Para el retorno (cuántas reuniones y ventas sale de eso) cruza con la ecuación de pipeline `05` y con `economist_lushows` para el CAC.

## La secuencia de un correo frío seguro (integrando el bloque)

Cada correo que mandas a volumen debe pasar por esta cadena; saltarte un eslabón quema la flota:

```
1. DESTINATARIO califica (ICP; ver 10, 16) — la mejor deliverability es un buen ICP
2. CORREO verificado y limpio (NeverBounce/ZeroBounce/MillionVerifier; ver 28)
      → bounce esperado < 2%. Si la lista da > 3% en muestra, NO la mandes
3. BUZÓN caliente (warmup ok, health > 90%; ver 112) y dentro de su límite diario
4. DOMINIO autenticado (SPF/DKIM/DMARC; ver 42, 111) y con reputación sana (ver 113)
5. MENSAJE texto plano, corto, 1 link máx, cero palabras spam (ver 45), placement ok (ver 116)
6. ENVÍO con rotación entre buzones, delay 60-180s, ventana horaria laboral (ver 44)
7. MONITOREO diario: bounce, spam rate, blacklist, reply (ver 113, 114)
```

## Las líneas rojas (nunca las cruces, a ningún volumen)

| Métrica | Línea roja | Acción inmediata |
|---|---|---|
| **Bounce rate** | > 4% | Detén la campaña, limpia toda la lista (ver `28`) |
| **Spam complaint rate** | > 0.3% | Baja volumen, aprieta ICP y copy |
| **Correos/buzón/día** | > 50 | Reparte en más buzones, no subas el límite |
| **Buzones por dominio** | > 3–4 | Concentras riesgo; abre más dominios (ver `110`) |
| **Domain Reputation (Postmaster)** | Baja/Mala | Frena, diagnostica (ver `113`, `117`) |
| **Volumen de buzón nuevo día 1** | > 5–10 real | Warmup primero (ver `112`) |

## Disciplina operativa a volumen (lo que separa al pro)

- **Limpia SIEMPRE antes de enviar.** A volumen, una lista con 8% de correos muertos rebota cientos de una y quema dominios en un día. Verificar es innegociable (ver `28`).
- **Fragmenta las cargas.** No subas 20.000 contactos a una campaña y le des play. Divide en lotes por día/segmento; si un lote sale mal, contuviste el daño.
- **Prueba lista nueva en pequeño.** Antes de mandar una base grande y desconocida, envía a una muestra de 100–200 y mira bounce/placement. Si la muestra rebota mucho, la base entera está sucia.
- **Colchón de buzones siempre caliente** (~15–20%; ver `112`) para reemplazar caídos sin bajar capacidad.
- **Un buzón/dominio degradado se aísla de inmediato**, no "a ver si mejora". Pausa, diagnostica, jubila si hace falta (ver `117`).
- **Segmenta por proveedor a gran escala** (Gmail vs Outlook; ver `115`) para que un problema en Microsoft no frene todo.

## La frontera importante

Este módulo es la **máquina de entrega a escala** (buzones, volumen, matemática, seguridad). Que ese volumen se convierta en reuniones y ventas depende de: la **relevancia del mensaje y la conversación** (copy `45`, `52`; y el cierre humano → `ventas_lushows`), del **ICP y la lista** (ver `10`, `20`), y de la **economía** (¿el CAC de mandar 60 buzones cierra? → `economist_lushows`). Volumen sin relevancia solo es spam más rápido. La escala amplifica lo que ya tienes: si tu oferta y lista son buenas, escala; si no, arréglalas antes de subir volumen (no mandes basura más rápido).

## Errores comunes (qué NO hacer)

- Subir el límite por buzón en vez de agregar buzones. El error que más quema operaciones.
- Mandar a volumen sin verificar la lista. Bounce alto = reputación destruida en un día.
- Cargar toda la base en una campaña gigante sin fragmentar ni probar en muestra.
- Escalar el envío sin escalar warmup, colchón y monitoreo (ver `112`, `113`).
- Creer que "más volumen = más reuniones" con oferta/lista malas. Escalas el fracaso.
- No calcular el costo real de la flota vs el retorno (cruza con `05`, `economist_lushows`).

## Siguiente paso

Cerraste el email a escala. El outbound serio en LatAm es multicanal: revisa `119` (no quemar números en WhatsApp/SMS — la misma disciplina de "no quemar" aplicada a mensajería). Para la arquitectura de flota que sostiene este volumen, `110`. Para el warmup en oleadas, `112`. Para los números exactos de buzones y costo a tu meta, `Matematicas_lushows`; para el CAC, `economist_lushows`; para el cierre de las reuniones que genere, `ventas_lushows`.
