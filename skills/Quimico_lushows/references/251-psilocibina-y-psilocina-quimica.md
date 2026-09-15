# 251 — Psilocibina y psilocina: la química (qué son exactamente estas dos moléculas)

Casi todo lo que confunde a la gente sobre psilocibina se explica con una diferencia química mínima: un
grupo fosfato. La psilocibina es un **profármaco** — no es la molécula activa; es una forma estable y
soluble en agua que el cuerpo convierte en psilocina, que sí es la activa. Entender ese detalle explica la
estabilidad, la farmacocinética, el análisis y hasta por qué los hongos se ponen azules al cortarlos.

**Alcance de este módulo (línea roja de la skill):** esto es química estructural, analítica y de estabilidad.
**No se dan rutas de síntesis, condiciones de reacción, precursores ni protocolos de producción o
extracción.** El manejo de estas sustancias está controlado en casi todo el mundo (`263`); lo que aquí se
cubre es lo necesario para entender, analizar e investigar en un marco legal.

Términos: **profármaco (prodrug)** = compuesto inactivo que el organismo transforma en el activo.
**triptamina (tryptamine)** = esqueleto químico derivado del indol, base de la serotonina y de estas
moléculas. **zwitterión (zwitterion)** = molécula con carga positiva y negativa a la vez, muy polar.
**fosfatasa alcalina (alkaline phosphatase)** = enzima que corta el grupo fosfato.

## Las dos moléculas, lado a lado

| Propiedad | Psilocibina | Psilocina |
|---|---|---|
| Nombre químico | 4-fosforiloxi-N,N-dimetiltriptamina | 4-hidroxi-N,N-dimetiltriptamina |
| Abreviatura frecuente | 4-PO-DMT | 4-HO-DMT |
| Fórmula molecular | C₁₂H₁₇N₂O₄P | C₁₂H₁₆N₂O |
| Masa molar | 284,25 g/mol | 204,27 g/mol |
| CAS | 520-52-5 | 520-53-6 |
| Estado | Sólido cristalino | Sólido, se oxida rápido |
| Carácter | Zwitteriónico, muy polar | Fenol, más lipofílico |
| Solubilidad en agua | Alta | Moderada |
| Estabilidad | Relativamente estable en seco y oscuro | Baja: se oxida al aire y a la luz |
| Actividad en receptor | Prácticamente nula | Agonista 5-HT2A (`257`) |
| Color al degradarse | — | Azul (quinoide) |

La relación de masas molares es lo que permite convertir entre las dos:

```
Factor de conversión psilocibina → psilocina (equivalente molar):
  204,27 / 284,25 = 0,7186

Es decir: 1,00 mg de psilocibina equivale, en moles, a 0,719 mg de psilocina.
Es el mismo tipo de factor que el 0,877 del THC total en cannabis (175).
Ejecuta la cuenta en código, no de memoria (Matematicas_lushows).
```

Ese factor sirve para expresar el contenido total de un material como "psilocibina equivalente", que es la
forma correcta de sumar psilocibina y psilocina en un mismo número:

```
Psilocibina equivalente (mg/g) = [psilocibina] + [psilocina] / 0,7186
o, si prefieres expresar todo como psilocina:
Psilocina equivalente (mg/g) = [psilocina] + [psilocibina] × 0,7186
Declara SIEMPRE cuál de las dos convenciones usaste. No son intercambiables.
```

## Por qué el fosfato lo cambia todo

El grupo fosforiloxi en la posición 4 hace tres cosas:

1. **Estabiliza.** El fenol de la psilocina es un blanco fácil para el oxígeno; esterificado como fosfato,
   está protegido. Por eso el hongo seco conserva psilocibina y no psilocina (`255`).
2. **Solubiliza.** El zwitterión es muy soluble en agua y muy poco en solventes orgánicos apolares, lo que
   condiciona todo el análisis (`256`).
3. **Desactiva temporalmente.** La psilocibina prácticamente no se une al receptor 5-HT2A; hace falta
   quitarle el fosfato para que aparezca la actividad. Esa hidrólisis la hacen fosfatasas del organismo
   (`258`).

## El azul: una reacción química, no un indicador de potencia

Cuando se magulla un hongo psilocibio aparece un color azul. Químicamente es la oxidación de la psilocina a
especies quinoides que oligomerizan; la reacción está catalizada por enzimas fúngicas tipo lacasa/fenoloxidasa.
Consecuencia práctica: **el azul indica psilocina que ya se degradó**, no potencia. Un material muy azul es
un material que perdió activo. Ojo con quien vende el azul como sello de calidad.

## Cómo se mide / cómo se comprueba

Ambas moléculas se cuantifican por cromatografía líquida; el detalle completo del método está en `256`.
Resumen de lo que hace falta para que un número signifique algo:

| Elemento | Requisito |
|---|---|
| Patrón de referencia | Psilocibina y psilocina certificados, con licencia para sustancias controladas |
| Estándar interno | Isotopólogos deuterados (psilocibina-d₄, psilocina-d₁₀) |
| Técnica | HPLC-DAD (UV ~267 nm) para material rico; LC-MS/MS para trazas |
| Unidad | mg/g base seca, o % p/p base seca |
| Base | Siempre declarada; los hongos frescos tienen ~90 % de agua |
| Convención | "psilocibina equivalente" o valores separados; nunca mezclar |

Detalle instrumental que se paga caro por ignorar: la psilocibina es **tan polar que casi no retiene en C18**
en fase móvil convencional. Se resuelve con alto contenido acuoso, columnas polar-embedded o HILIC (`256`).

## Ejemplo aplicado (ILUSTRATIVO) — reporte analítico bien escrito

```
Muestra: material vegetal fúngico seco, homogeneizado, lote de investigación PSY-2026-003
Método: HPLC-DAD 267 nm, columna C18 polar-embedded, estándar interno deuterado
Base: seca (humedad 6,2 % por pérdida a 105 °C)

  Psilocibina    7,42 mg/g b.s.   (RSD 3,1 %, n = 3)
  Psilocina      0,88 mg/g b.s.   (RSD 5,4 %, n = 3)
  Psilocibina equivalente = 7,42 + 0,88 / 0,7186 = 8,64 mg/g b.s.
  = 0,86 % p/p base seca
```

Ese reporte se puede auditar. Un "0,9 % de psilocibina" sin método, sin base y sin convención, no.

## Errores comunes

- **Sumar psilocibina y psilocina directo.** Son masas molares distintas; hay que convertir (0,7186).
- **Reportar en base húmeda.** Un hongo fresco con 90 % de agua da un número 10 veces menor y no comparable.
- **Creer que el azul mide potencia.** Mide degradación.
- **Llamar "psilocibina" a la molécula activa.** La activa es la psilocina; la psilocibina es el profármaco.
- **Usar un método de C18 estándar sin ajustar.** La psilocibina sale en el volumen muerto y se subestima.
- **Manejar patrones sin licencia.** Es un problema legal serio, incluso para un laboratorio (`263`).

## Conexión con otros módulos

→ `50-alcaloides.md` y `128-serotonina-y-receptor-5ht2a.md` — familia química y diana.
→ `252-baeocistina-y-otros-alcaloides-relacionados.md` — los demás alcaloides del mismo grupo.
→ `253-biosintesis-de-psilocibina.md` — cómo la fabrica el hongo (a nivel conceptual).
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — el fosfato como escudo.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — el método completo.
→ `263-estado-clinico-y-regulatorio-2026.md` — bajo qué marco se puede tocar todo esto.