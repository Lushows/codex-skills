# DESIGN — contador_lushows

**Fecha:** 2026-06-18
**Estado:** Spec aprobado (pendiente revisión final del usuario)
**Autor:** Lushows + Claude

---

## 1. Qué es

Skill que convierte a Claude en un **contador público de élite**: lleva los libros, arma
estados financieros bajo norma (NIIF/IFRS, NIIF para pymes, US GAAP), liquida y presenta
impuestos, nómina, conciliaciones, cierre contable y auditoría. Profesión completa de la
contaduría, **robusta en Colombia** y diseñada para abrir a otros países sin reescribir.

Es la 13ª skill del equipo "lushows" y sigue el mismo patrón: `SKILL.md` (router) +
`references/` (200 módulos cargados bajo demanda) + entregable PDF.

## 2. Carácter no-negociable (la promesa)

**CUADRE + CUMPLIMIENTO + AUDITABLE.**

1. **Los libros SIEMPRE cuadran** — partida doble, débitos = créditos, todo soportado.
2. **Cumplimiento sin falla** — plazos, formatos y normas vigentes (DIAN, NIIF) al día.
3. **Auditable** — todo registro con su soporte; listo para auditor/revisor fiscal/DIAN.
4. **Nunca calcula de cabeza** — ejecuta/verifica en código o **ruta a `Matematicas_lushows`**.
5. **Honesto sobre riesgos** — sanciones, contingencias, lo que NO se debe hacer; con
   disclaimer de que no reemplaza al contador titulado que firma.
6. **Explica para no-técnicos** — define cada término la primera vez (glosario contable).
7. **Pregunta país/régimen/grupo NIIF antes de cualquier registro o impuesto.** Cero supuestos.

## 3. Frontera con el equipo (ruteo, sin duplicar)

| Skill | Se queda con | Le ruta a contador |
|---|---|---|
| **economist** | DECIDIR con números (viabilidad, pricing, crecer, levantar capital) — futuro | llevar libros, estados bajo NIIF, liquidar/presentar impuestos, nómina |
| **Matematicas** | EJECUTAR el cálculo exacto (error cero) | — (contador le ruta TODO cálculo) |
| **AVIS** | Agente WhatsApp del producto AVISPA'O (cumplimiento conversacional Colombia) | lo contable profundo (estados, NIIF, impuestos a fondo) |
| **contador** | REGISTRAR / REPORTAR / CUMPLIR — presente y pasado | el QUÉ calcular → Matematicas; la DECISIÓN → economist |

**Regla:** economist DECIDE · contador REGISTRA/REPORTA/CUMPLE · Matematicas EJECUTA · AVIS CONVERSA (producto).

## 4. Arquitectura de la biblioteca (200 módulos, carga bajo demanda)

### Núcleo 00–99 (Colombia tejido dentro)
- **0 Fundamentos (00–09):** método, promesa cuadre/cumplimiento/auditable, ecuación contable
  + partida doble, marco normativo, ética y secreto profesional, glosario, ruteo al equipo.
- **1 Ciclo contable (10–19):** PUC, asientos, diario/mayor, balance de comprobación, ajustes,
  devengo vs caja, cierre contable.
- **2 Estados financieros (20–29):** situación financiera, resultados, flujo de efectivo, cambios
  en patrimonio, notas, presentación NIIF, lectura/ratios (→ Matematicas).
- **3 Cuentas y operación (30–39):** inventarios (PEPS/promedio), activos fijos/depreciación,
  CxC/CxP, conciliación bancaria, provisiones, diferidos, costeo.
- **4 Impuestos (40–49):** IVA, renta, retención en la fuente, ICA, facturación electrónica,
  calendario y declaraciones.
- **5 Nómina y laboral contable (50–59):** nómina, prestaciones sociales, seguridad social/PILA,
  liquidaciones, nómina electrónica.
- **6 Colombia a fondo (60–69):** DIAN/RUT/regímenes, NIIF pymes (Grupos 1/2/3), UGPP, exógena,
  revisoría fiscal, sanciones.
- **7 Práctica profesional y control (70–79):** auditoría, control interno, papeles de trabajo,
  NIA, fraude, dictamen.
- **8 Herramientas y automatización (80–89):** Excel contable, software (Siigo/Alegra/World Office),
  IA contable, integración con el bot, conciliación automática.
- **9 Dueño y entregables (90–99):** leer tus estados sin ser contador, tablero, alertas de plazos,
  checklist mensual, plantillas + PDF profesional.

### Expansión 100–199 (apertura de mercado + profundidad)
- **10 Tributario avanzado y planeación 2026 (100–109)**
- **11 NIIF a fondo (110–119)**
- **12 Contabilidad por sector (120–129)**
- **13 Nómina y laboral a fondo 2026 — jornada 42h Ley 2101 (130–139)**
- **14 Contador como profesión/servicio (140–149)**
- **15 Tesorería y finanzas operativas (150–159)**
- **16 Automatización contable con IA 2026 (160–169)**
- **17 Auditoría y aseguramiento a fondo (170–179)**
- **18 Otros países — México/USA/España/Perú/Chile (180–189)**
- **19 Cierre anual, casos y changelog normativo 2026 (190–199)**

## 5. Actualidad 2026

Todo el contenido refleja normativa vigente a fin de 2026: facturación y nómina electrónica DIAN,
NIIF vigentes, jornada laboral 42h, conciliación fiscal (formato 2516), exógena, y un módulo
**changelog** (199) que registra cambios normativos con fecha — igual que el changelog de las
skills de ads.

## 6. Cambios al equipo (no se borra contenido, solo ruteo)

- **economist** (140–149 "contabilidad y finanzas avanzada" y 60–69 legal/tributario): añadir
  puntero "para llevar libros, estados bajo NIIF, liquidar/presentar impuestos y nómina →
  `contador_lushows`". economist se queda con la DECISIÓN.
- **AVIS** (14-tributario-practico, 04-facturas-dian-cruce): puntero "lo contable profundo →
  `contador_lushows`".
- **Matematicas** (bloque financiero 70–89): nota recíproca "el QUÉ contable lo define contador;
  yo ejecuto el cálculo".

## 7. Entregable

Conversacional paso a paso. Al cerrar (estados armados, declaración liquidada), genera **PDF
profesional** con chrome headless (módulo 99). Nunca Markdown crudo.

## 8. Fuera de alcance (YAGNI)

- No firma declaraciones ni reemplaza al contador titulado (disclaimer claro).
- No asesoría legal (eso es economist 60–69 / abogado).
- Expansión 180–189 (otros países) se escribe en profundidad solo cuando abra ese mercado;
  por ahora queda como estructura + lo esencial.

## 9. Plan de construcción

1. `SKILL.md` (router + índice de 200 módulos + reglas de oro) — primero.
2. Núcleo 00–99 (lo que Lushows usa ya en Colombia) — prioridad alta.
3. Expansión 100–179 + 190–199 — prioridad media.
4. 180–189 (otros países) — esqueleto ahora, profundidad al abrir mercado.
5. Cross-links en economist, AVIS, Matematicas.
6. Actualizar memoria (`MEMORY.md` + archivo de proyecto).
