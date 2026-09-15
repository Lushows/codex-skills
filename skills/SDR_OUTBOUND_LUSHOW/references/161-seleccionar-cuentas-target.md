# 161 — Seleccionar cuentas target (el ICP de CUENTA, no de contacto)

En ABM la lista NO es una lista de personas: es una lista de **empresas**. Antes de buscar a nadie, tienes que decidir **cuáles 30–150 cuentas** merecen tu artillería pesada. Este módulo es sobre construir esa lista: definir el **ICP de cuenta** (el perfil de la empresa ideal, distinto del buyer persona `11`), armar el universo, puntuarlo y cortarlo en tiers. Si eliges mal las cuentas, todo lo demás —el research, el multi-threading, el play coordinado— se desperdicia en empresas que nunca iban a comprar. **La selección de cuentas es la decisión más apalancada de todo el programa.**

## El principio: ICP de cuenta ≠ ICP de contacto

Son dos cosas distintas y en ABM necesitas las dos:

- **ICP de cuenta** = qué empresa encaja: sector, tamaño, geografía, tecnología que usa, modelo de negocio, señal activa (ver firmographics/technographics en `15`). Responde *"¿a qué empresas les vendo?"*.
- **Buyer persona / comité** = qué personas dentro decides tocar (`11`, `165`). Responde *"¿a quién le escribo dentro de esa empresa?"*.

En volumen a veces colapsas las dos. En ABM las separas: primero eliges la **empresa** (esto), luego mapeas el **comité** dentro de ella (`165`).

## Construir el universo de cuentas (de dónde salen)

Tu lista objetivo se arma cruzando fuentes hasta tener el conjunto real de empresas que caben en tu ICP de cuenta:

| Fuente | Qué aporta | Herramienta |
|---|---|---|
| Filtro firmográfico | Sector + tamaño + país, base del universo | Sales Navigator (`26`), Apollo, ZoomInfo |
| Technographics | Empresas que usan/no usan X tecnología | BuiltWith, Clay (`31`), ZoomInfo |
| Intent data | Cuentas investigando tu categoría ahora | Bombora, G2 intent, 6sense (`36`) |
| Listas públicas | Rankings, ferias, gremios, cámaras (LatAm) | Web, directorios sectoriales |
| Tu CRM | Clientes actuales parecidos, deals perdidos revivibles | HubSpot/CRM (`32`) |
| Look-alike | "Empresas como mi mejor cliente" | Clay, ZoomInfo similar-companies |

**En LatAm** el dato firmográfico es más pobre que en EE.UU.: complementa con cámaras de comercio, gremios sectoriales, rankings locales (ej. "500 empresas más grandes de X") y scraping ético de directorios (ver `27`). Enriquece con Clay (`31`, `29`).

## Puntuar y cortar en tiers (el fit score de cuenta)

No todas las cuentas del universo valen igual. Aplica el **ICP fit score** (método completo en `16`): 4–6 criterios con peso, puntúas cada cuenta 0–100, cortas en A/B/C.

```
Criterio (peso)                    Cuenta A     Cuenta B
Sector exacto (25)                   25           25
Tamaño ideal 200–800 empl. (20)      20            8   (B tiene 3.000)
País/región objetivo (15)            15           15
Usa tecnología-señal (15)            15            0
Tengo caso en su nicho (15)          15           15
Intent activo / trigger (10)         10            0
------------------------------------------------------
FIT SCORE                           100           63
TIER                                  A            B
```

- **Tier A (10–30 cuentas):** encaje perfecto + señal + ticket top. ABM 1:1, research a mano, multi-threading completo, el AE metido desde el inicio (`163`).
- **Tier B (30–100):** buen encaje, sin señal fuerte. ABM 1:few por cluster de sector/caso de uso.
- **Tier C:** o van a la máquina de volumen (`93`) o a ABM programático con ads/intent (`160`).

⚠️ Si armas el modelo de scoring con muchos criterios y pesos y quieres que los umbrales y ponderaciones sean **exactos**, ejecútalo/verifícalo con **`Matematicas_lushows`**. Aquí va el método; el número fino se calcula.

## Cuántas cuentas por SDR (números realistas 2026)

El error clásico es una lista demasiado grande para hacer ABM de verdad. Referencias por SDR/trimestre:

| Sabor | Cuentas activas | Contactos/cuenta | Toques por contacto |
|---|---|---|---|
| ABM 1:1 | 20–40 | 5–10 | Multicanal, semanas |
| ABM 1:few | 50–150 | 3–6 | Semi-personalizado por cluster |

Si tienes 500 cuentas "prioritarias", no tienes prioridades: tienes una lista de volumen mal etiquetada. Corta. **Menos cuentas bien trabajadas > muchas mal tocadas.** Valida el tamaño contra tu capacidad real de toques en `17` y `44` (deliverability es recurso escaso).

## Ejemplo: filtro de universo (Sales Navigator, cuenta B2B LatAm)

```
Sales Navigator → Account filters:
  Industry: Food & Beverages, Restaurants, Hospitality
  Headcount: 201–1000
  Headquarters: Colombia, México, Chile
  + señal: "Company headcount growth > 10%" (contratando)
→ Guardar como Account List "ABM Q3 – Retail Alimentos"
→ Exportar a Clay (31) → enriquecer con tecnología + web + noticias
→ Fit score en Clay → cortar A/B/C
```

Luego, POR cada cuenta, entras a mapear el comité (`165`) y a buscar contactos (`22`, `23`).

## Errores comunes

- **Elegir cuentas por tamaño/logo, no por encaje.** Una empresa gigante que no tiene tu problema no es Tier A, es pérdida de tiempo.
- **Lista estática.** El fit score es dinámico: una cuenta B con señal nueva sube a A esa ventana (`14`, `37`). Re-prioriza cada mes.
- **Confundir ICP de cuenta con persona:** eliges la empresa aquí; a la persona en `165`.
- **Universo sin fuente de intent:** trabajas cuentas dormidas mientras las que buscan tu categoría hoy se te escapan (`36`).

## Siguiente paso

Arma tu universo con las fuentes de arriba, aplica el fit score (`16`), corta en A/B/C y quédate con un número de cuentas que de verdad puedas trabajar (`17`). Con la lista de cuentas Tier A lista, pasa a mapear el comité de cada una en `165`, y a montar el multi-threading en `162`.
