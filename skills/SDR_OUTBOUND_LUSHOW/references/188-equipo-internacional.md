# 188 — Equipo internacional de SDRs

Cuando tu outbound crece más allá de lo que tú solo puedes ejecutar, o cuando operas cross-border (ver `187`), necesitas gente — y esa gente suele estar en varios países. Contratar, pagar y coordinar SDRs distribuidos internacionalmente tiene reglas que no aparecen cuando contratas al vecino: cómo pagarle legalmente a alguien en otro país, en qué moneda, cómo estructurar el equipo por huso, y cómo mantener calidad y cultura sin oficina física. Este módulo complementa la contratación general (ver `85`) y el onboarding (ver `86`) con la capa internacional. Es cómo construyes una máquina humana que corre en varias zonas horarias.

## El principio: LatAm es el mejor lugar del mundo para contratar SDRs remotos

El talento SDR latinoamericano es una de las mejores relaciones calidad/costo del planeta para outbound en inglés y español: bilingües, en husos alineados con USA, cultura de trabajo fuerte, y costo muy inferior al SDR gringo. Por eso tantas empresas de USA arman sus equipos de SDR en Colombia, México y Argentina. Del lado de Lushows, esto corta en dos: puedes **contratar SDRs latinos para tu operación** y puedes **ser el proveedor** que le arma equipos a otros (ver `95`). En ambos casos, saber montar y pagar un equipo internacional es la competencia central.

## Dónde contratar (por perfil)

| Región | Fortaleza | Nota |
|---|---|---|
| **Colombia** | Bilingüe, huso USA Este, cultura de servicio fuerte | Medellín y Bogotá, hubs de BPO/ventas |
| **México** | Bilingüe, cercanía y huso USA, gran volumen de talento | Guadalajara, CDMX, Monterrey |
| **Argentina** | Inglés muy bueno, costo atractivo (peso débil) | Fuerte en SaaS/tech |
| **Filipinas** | Inglés nativo-nivel, costo bajo, cultura BPO madura | Huso opuesto a USA (bueno para cobertura 24h, malo para tiempo real) |
| **Europa del Este** | Inglés bueno, para vender a Europa | Costo mayor que LatAm |

Para outbound hacia USA desde el mundo hispano, **LatAm gana** por la combinación idioma + huso + cultura + costo.

## Cómo pagarle legalmente a alguien en otro país

Este es el punto que traba a los no expertos. No puedes simplemente "meterlo a nómina" si está en otro país; hay tres caminos:

1. **Contratista independiente (freelance).** El SDR factura como contratista; le pagas por transferencia/plataforma. Simple y común para empezar, pero cuidado con la "clasificación errónea" (misclassification): si lo tratas como empleado (horario fijo, exclusividad, supervisión total) algunos países lo consideran relación laboral encubierta y hay riesgo legal/tributario. Bien para arranque y volumen bajo.
2. **EOR (Employer of Record).** Empresas como **Deel, Remote.com, Ontop, Oyster** contratan legalmente al SDR en su país por ti — se encargan de nómina, impuestos, prestaciones y cumplimiento local. Tú les pagas una tarifa mensual por empleado (~$50–600 USD/mes según proveedor y país). Es la forma limpia de tener "empleados" internacionales sin abrir empresa en cada país. El estándar cuando quieres relación estable y sin riesgo.
3. **Entidad local propia.** Abrir empresa en el país del equipo. Solo tiene sentido a escala grande (muchos empleados en un país); costoso y lento para empezar.

Herramientas de pago a contratistas/equipos: **Deel, Payoneer, Wise, Ontop, Mercury** para mover dinero cross-border con bajo costo de cambio. La estructura fiscal y contable de contratar/pagar internacionalmente (retenciones, facturación, en qué país tributa qué) es tema de **`contador_lushows`**; la constitución de empresa o entidad, de las skills legales/de negocio (`economist_lushows` para el modelo, contador/abogado para lo formal). No improvises la parte legal-tributaria.

## Cómo estructurar el equipo por huso

- **Cobertura de ventana del prospecto, no de la tuya** (ver `186`). Si vendes a USA, tu equipo debe estar despierto en horario USA — LatAm lo cubre naturalmente.
- **"Follow the sun" para cobertura amplia**: si vendes a USA y Europa, un SDR en LatAm cubre América y uno en Europa del Este o Filipinas cubre Europa/Asia. Entre ambos, cobertura casi 24h.
- **Especializa por mercado/idioma** cuando puedas: el SDR nativo o más fluido en el idioma del segmento lo trabaja (ver `185`).
- **Un líder por turno/región** a medida que creces, para coaching y QA en cada huso (ver `87`).

## Mantener calidad y cultura sin oficina

- **Playbook escrito y único** (ver `90`, `98`): el equipo distribuido necesita la fuente de verdad documentada, no transmisión oral.
- **Onboarding y ramp estructurado** (ver `86`): mismo estándar para todos, sin importar el país.
- **QA y coaching remoto** (ver `87`): revisa llamadas grabadas, correos enviados, actividad en CRM. La distancia no exime de control de calidad.
- **Métricas visibles y compartidas** (ver `80`, `83`): el dashboard de actividad y resultados alinea a todos sin necesidad de mirar por encima del hombro.
- **Ritmo de comunicación**: daily o weekly sync por video, canal de chat siempre activo, cultura de reconocimiento. El equipo remoto se desmotiva en silencio si no lo cuidas (ver `04`).

## Ejemplo: primer equipo internacional de Lushows

```
Operación: outbound a USA (SaaS) desde LatAm
- 2 SDRs en Medellín/Bogotá (bilingües, huso USA Este) — contratados vía Deel (EOR)
- Pago: salario base en USD + bono por reunión calificada (ver 84)
- Herramientas: mismas licencias (Apollo, Instantly) compartidas
- Playbook: documentado (ver 90), onboarding de 2 semanas (ver 86)
- QA: review semanal de correos + llamadas grabadas (ver 87)
- Sync: daily de 15 min por video, canal de Slack activo
- Cumplimiento fiscal/laboral: resuelto por el EOR + contador (ver contador_lushows)
```

## Errores comunes (qué NO hacer)

- Tratar a un contratista como empleado (horario, exclusividad, control total): riesgo de misclassification en su país.
- Improvisar la parte legal/tributaria del pago internacional: usa EOR o consulta a `contador_lushows`.
- Contratar por huso equivocado: un equipo que duerme cuando el prospecto trabaja no sirve (ver `186`).
- Escalar sin playbook documentado: el equipo distribuido se desalinea sin fuente de verdad (ver `90`).
- Descuidar cultura y coaching remoto: la rotación se dispara y quemas la inversión de ramp (ver `85`, `86`).

## Siguiente paso

Define tu primer rol (mercado, idioma, huso), decide la vía de pago (contratista para probar, EOR tipo Deel/Ontop para estable), y documenta el playbook antes de contratar (ver `90`, `98`). La contratación y el perfil del SDR en `85`, el onboarding en `86`, la compensación en `84`, el coaching en `87`. Para la estructura fiscal/legal del pago internacional → `contador_lushows`; para el modelo de negocio → `economist_lushows`. Si armas equipos para otros como servicio, ver `95` y `187`.
