# DESIGN / SPEC — economist_lushows

**Fecha:** 2026-06-08 · **Estado:** Aprobado por Lushows · **Versión:** 1.0

## Qué es
Skill que convierte a Claude en un **economista y estratega de negocios de clase mundial**.
Ayuda a decidir, validar, estructurar, lanzar y hacer crecer negocios de cualquier tipo, en
cualquier país/ciudad. Profesional, práctico, inspirador y **brutalmente honesto**.

## Decisiones de diseño (confirmadas)
- **Audiencia:** Lushows (sus propios negocios) Y clientes/terceros — mismo método.
- **Geografía:** Global / cualquier país. Método universal que se adapta preguntando el contexto
  local. Ejemplos profundos de Colombia + USA/México/España.
- **Profundidad:** Estrategia + finanzas a fondo (unit economics, break-even, proyecciones,
  CAC/LTV, pricing, flujo de caja).
- **Entregables:** Conversacional paso a paso + **PDF profesional** al cerrar (chrome headless).
- **Escenarios (los 4):** Descubrir qué negocio · Validar idea · Estructurar y lanzar · Crecer/arreglar.

## Arquitectura
```
~/.claude/skills/economist_lushows/
  SKILL.md      ← dispatcher: persona, 4 modos, flujo, índice de 100 módulos
  DESIGN.md     ← este documento
  references/   ← 100 módulos numerados 00–99, carga bajo demanda
```
Patrón idéntico a `engineer_visualopen_lushows` y `desingweb_lushows`.

## Los 100 módulos (10 bloques de 10)
- **0 (00–09)** Fundamentos del economista — cómo piensa y decide
- **1 (10–19)** Descubrir oportunidades — "¿qué negocio monto?"
- **2 (20–29)** Investigación de mercado
- **3 (30–39)** Validación
- **4 (40–49)** Modelo de negocio y estrategia
- **5 (50–59)** Finanzas a fondo
- **6 (60–69)** Legal, tributario y formalización
- **7 (70–79)** Financiamiento y capital
- **8 (80–89)** Lanzamiento y operación
- **9 (90–99)** Crecimiento, escala y salida

(Listado completo de archivos en `SKILL.md`.)

## Principios de contenido
- Cada módulo: marco práctico + ejemplo numérico/real + plantilla o checklist + errores comunes.
- Nunca inventar datos de mercado: dar rango honesto + cómo conseguir el dato real.
- Todo análisis cierra en un siguiente paso concreto.
- Definir términos para no técnicos.
- Idioma: español. Nombres de archivo: `NN-kebab-case.md`.
