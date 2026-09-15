# 172 — Biosíntesis de cannabinoides: la ruta que explica por qué tu COA se ve así

Entender la ruta biosintética no es lujo académico: es lo que te permite leer un COA y saber si tiene
sentido. Si un certificado te dice "CBD 15 %, CBG 0,0 %, CBC 0,0 %, THC 0,0 %", desconfía — la ruta
biológica casi nunca produce un solo compuesto puro en la planta. Este módulo te da el mapa: de dónde salen
los cannabinoides, por qué siempre aparecen en **forma ácida**, y por qué el CBGA es la materia prima de
todo el negocio de cannabinoides menores.

Términos:
- **precursor (precursor)** = molécula de partida que la planta transforma.
- **prenilación (prenylation)** = pegar una cadena isoprenoide a un anillo aromático; el paso que crea el
  esqueleto cannabinoide.
- **sintasa (synthase)** = enzima que cierra el anillo y define cuál cannabinoide sale.
- **CBGA (cannabigerolic acid)** = el precursor común de THCA, CBDA y CBCA.
- **forma ácida (acidic form)** = el cannabinoide tal como la planta lo hace, con un grupo carboxilo
  (–COOH). Ver `173`.

## Las dos ramas que se juntan

El esqueleto cannabinoide nace de la unión de dos rutas del metabolismo secundario (ver `58` y `59`):

```
Ruta de policétidos (poliketide)          Ruta MEP / plastídica
  hexanoil-CoA + 3 × malonil-CoA            GPP (geranil difosfato, C10)
            ↓ (OLS/OAC)                              ↓
   ÁCIDO OLIVETÓLICO (olivetolic acid)                │
            └──────────────┬───────────────────────────┘
                           ↓  prenilación por CBGA sintasa (aromatic prenyltransferase, CsPT4)
                    CBGA (ácido cannabigerólico)
```

El ácido olivetólico lleva la cadena **pentilo** (5 carbonos) que hereda el THC y el CBD. Si en vez de
hexanoil-CoA la planta usa butanoil-CoA (C4), sale **ácido divarínico** y de ahí la serie **varínica**
(THCVA, CBDVA, ver `178`). Si usa cadenas más largas, salen los homólogos raros como el THCPA (ver `179`).

## El punto de bifurcación: CBGA

CBGA es el nodo. Tres sintasas compiten por él:

| Enzima | Producto | Nota |
|---|---|---|
| THCA sintasa (THCAS) | **THCA** | Oxidociclasa dependiente de FAD; libera H₂O₂ |
| CBDA sintasa (CBDAS) | **CBDA** | Misma familia, distinto cierre de anillo |
| CBCA sintasa (CBCAS) | **CBCA** | Menos estudiada; explica el CBC de fondo |
| (ninguna) | CBGA remanente | Los quimiotipos IV acumulan CBGA porque la conversión es baja |

Esto explica de un golpe tres cosas que ves en COA reales:

1. **Siempre hay algo del otro.** Un tipo III con CBDAS dominante casi siempre muestra THCA en trazas — no
   es contaminación, es la ruta.
2. **El CBG del mercado casi nunca es "natural abundante".** Se obtiene de quimiotipos IV seleccionados,
   de cosecha temprana, o por síntesis/aislamiento (ver `177`, `193`).
3. **El CBN no está en la ruta.** El CBN es producto de **degradación oxidativa** del THC, no de biosíntesis
   (ver `177` y `204`). Un COA de flor fresca con CBN alto te está diciendo que el material es viejo o que
   se manejó mal.

## Lo que la planta NO hace

- La planta **no fabrica Δ8-THC en cantidad relevante**. El Δ8-THC de los productos comerciales es, en la
  práctica, producto de isomerización química del CBD (ver `180`).
- La planta **no fabrica HHC, THC-O ni H4CBD**. Todos son semisintéticos (ver `181`).
- La planta **no fabrica THC neutro en cantidad**: fabrica THCA. El THC neutro aparece por
  descarboxilación con tiempo, luz y calor (ver `174`).

Esta lista es una herramienta de auditoría: si un proveedor te dice que su Δ8 es "natural, extraído de la
planta", o miente o está describiendo una isomerización que no quiere nombrar.

## Cómo se mide / cómo se comprueba

- **Perfil completo por HPLC-DAD** con estándares de CBGA, CBG, THCA, Δ9-THC, CBDA, CBD, CBCA, CBC, CBN
  (`% p/p base seca`). Es el único modo de ver la ruta reflejada en el lote (`198`).
- **Coherencia interna del COA:** revisa que la suma de cannabinoides sea plausible (típicamente 15–30 %
  `% p/p base seca` en flor de alta potencia; reportado en literatura, verifica tu lote) y que aparezcan
  los menores esperados. Un COA con ceros perfectos en todos los menores es sospechoso (`111`).
- **Confirmación de identidad de compuestos poco comunes:** HRMS (QTOF/Orbitrap) para fórmula elemental,
  y RMN si hay que distinguir isómeros de posición (`84`, `94`).
- **Ausencia de compuestos no biosintéticos:** buscar Δ8-THC, HHC, ésteres acetilados por LC-MS/MS. Su
  presencia indica intervención química, no planta (`180`, `181`).

## Ejemplo aplicado

COA de flor tipo III, HPLC-DAD, `% p/p base seca` (ILUSTRATIVO):

| Analito | Valor | Lectura |
|---|---|---|
| CBDA | 13,1 % | Rama CBDAS dominante, coherente |
| CBD | 0,7 % | Descarboxilación parcial normal por secado |
| CBGA | 0,45 % | Precursor remanente, coherente |
| CBG | 0,05 % | Trazas |
| THCA | 0,54 % | Fuga esperada de la ruta |
| Δ9-THC | 0,04 % | Coherente |
| CBCA + CBC | 0,22 % | Rama CBCAS, coherente |
| CBN | < LOQ | Material fresco, bien manejado |
| Δ8-THC | No detectado | Bien: sin intervención química |

Este COA "se ve como una planta". Un COA que reportara `CBD 15,0 %` y todo lo demás en cero no se ve como
una planta: se ve como un aislado mezclado con biomasa, o como un reporte que solo midió un analito.

## Errores comunes

- Pedir solo "CBD y THC" al laboratorio y quedarte sin la información que te permite auditar el lote.
- Creer que "CBG natural" y "CBG aislado" son lo mismo en costo y en trazabilidad (`177`, `193`).
- Interpretar CBN alto como una virtud del producto en vez de como un indicador de envejecimiento (`204`).
- Aceptar la explicación "es natural" para Δ8, HHC o acetatos. No lo es (`180`, `181`).
- Comparar sumatorias de cannabinoides entre COA con bases distintas (húmeda vs seca) — ver `07`.
- Olvidar que la ruta produce H₂O₂ como subproducto: los tejidos con alta actividad THCAS se oxidan más
  rápido, lo que refuerza la importancia del secado y el envase (`186`, `163`).

## Conexión con otros módulos

→ `58-rutas-biosinteticas-mevalonato-y-mep.md` — de dónde sale el GPP.
→ `59-ruta-del-shikimato-y-policetidos.md` — de dónde sale el ácido olivetólico.
→ `173-formas-acidas-thca-y-cbda.md` — por qué todo sale con –COOH.
→ `177-cbg-cbc-y-cbn.md` — los tres que esta ruta explica (y el que no).
→ `179-thcp-cbdp-y-homologos.md` — qué pasa cuando la cadena alquílica cambia.
→ `198-analisis-de-potencia-metodo.md` — cómo se ve todo esto en el cromatograma.
