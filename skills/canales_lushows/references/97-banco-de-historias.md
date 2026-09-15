# 97 · Banco de historias

**Qué resuelve:** de qué se hace el próximo episodio. Elegir mal el caso cuesta una
semana de trabajo que no se puede salvar con montaje. El banco es una cola con
criterios, no una lluvia de ideas.

---

## Los cinco criterios de entrada

Un caso entra a la cola sólo si cumple los cinco. No hay cuatro de cinco.

| # | Criterio | Cómo se comprueba |
|---|---|---|
| 1 | **Hay documentos públicos** | Existe al menos una fuente de nivel 1 o 2 (§ `90`) y está descargada |
| 2 | **Hay una cifra imaginable** | Se puede hacer un cálculo propio que quepa en la cabeza (§ `92`) |
| 3 | **El arco tiene caída** | Construyó algo real → cruzó la raya → se derrumbó. Con final documentado |
| 4 | **El archivo es libre** | Hay imágenes de dominio público o propias suficientes para 10 min |
| 5 | **Monetiza** | El foco es dinero e ingeniería; se puede contar sin violencia ni drogas en primer plano |
| 6 | **Alguien la está buscando** | ≥ 20.000 visitas/mes en Wikipedia EN y ≥ 2.000 en ES (§ `404`) |

**El criterio 6 se añadió después del episodio 1**, y es el que lo habría cambiado: Lustig tiene 6.193 visitas/mes frente a las 109.694 de Madoff o las 44.143 de Enron. Los cinco primeros comprueban que el caso SE PUEDE CONTAR; ninguno comprobaba que alguien lo estuviera buscando (§ `404`).

Y el criterio 4 pide ahora un orden de magnitud más de lo que pedía: un episodio de diez minutos consume unas 160 piezas distintas en pantalla, no 40 (§ `403`).

**El criterio 4 es el que más casos elimina** y el que menos se comprueba a tiempo. Se
verifica ANTES de escribir: media hora buscando archivo evita tres días de trabajo con
un episodio que no se puede ilustrar.

## La ficha de puntuación

Cada candidato se puntúa de 0 a 5 en seis ejes. La cola se ordena por total.

```
DOCUMENTACIÓN ....... 0-5   cuántos documentos de nivel 1-2 hay y qué detalle traen
CIFRA ............... 0-5   ¿hay una magnitud que se pueda convertir en imagen?
ARCO ................ 0-5   ¿construcción, raya, grieta y caída, todas documentadas?
ARCHIVO ............. 0-5   material libre disponible (0 si sólo hay fotos de agencia)
RAREZA .............. 0-5   ¿el mecanismo sorprende? Un fraude más no sorprende
SEGURIDAD ........... 0-5   riesgo de icono amarillo, personas vivas, reclamaciones
                     ----
TOTAL                 /30   se produce a partir de 22; por debajo, se aparca
```

**Regla de personas vivas:** con alguien vivo y no condenado, el episodio se ciñe a lo
documentado y a las fórmulas de atribución de § `91`. Si no se puede contar así, se cae.

## Cómo se encola

1. **Captura** — el caso se anota con una línea y de dónde salió la pista.
2. **Sondeo de 30 minutos** — buscar el documento principal y el archivo visual. La
   mayoría de los candidatos muere aquí, que es justo lo que se busca.
3. **Ficha de puntuación** — con los enlaces reales ya encontrados.
4. **Cola** — ordenada por total, con la fecha de sondeo.
5. **Producción** — se abre carpeta y empieza el orden de trabajo de SKILL.md.

### El formato del banco (`archivo/banco.json`)

```json
{
  "id": "caso-xxx",
  "titulo_provisional": "",
  "una_linea": "qué construyó y cómo cayó",
  "documentos": [{"organismo": "", "tipo": "", "url": "", "descargado": false}],
  "archivo_visual": {"fuente": "", "piezas_libres": 0, "suficiente": false},
  "cifra_ancla": {"valor": "", "que_mide": "", "fuente": ""},
  "puntuacion": {"documentacion":0,"cifra":0,"arco":0,"archivo":0,"rareza":0,"seguridad":0},
  "estado": "captura | sondeado | en cola | producido | descartado",
  "motivo_descarte": ""
}
```

> **Sin URL real y comprobada, un caso no pasa de "captura".** Este módulo no trae
> enlaces a propósito: una URL inventada contamina el archivo y hace inservible el
> banco entero.

## Familias de historias que funcionan en este canal

| Familia | Por qué funciona | Dónde suele estar documentada |
|---|---|---|
| **Ponzi y pirámides** | El mecanismo se explica en 40 s y todo el mundo lo entiende | Demanda del regulador de valores, acusación penal, informes del síndico o del administrador judicial |
| **Fraude contable de cotizada** | Está la mentira firmada en sus propias cuentas | Presentaciones en EDGAR + acción del regulador |
| **Tapadera industrial** | Un negocio real que servía para otra cosa: el arquetipo del canal | Acusación penal y demandas civiles de decomiso |
| **Fondos y bancos que reventaron** | Cifras enormes y una grieta técnica concreta | Informes de examinador, comisiones parlamentarias, reguladores |
| **Cripto** | Reciente, muy buscado, con expediente ya público | Acciones de reguladores + expediente de la quiebra |
| **Producto que no existía** | Una promesa técnica imposible vendida como empresa | Acusación penal + demanda del regulador |
| **Saqueo de fondos públicos** | Explica un país con una sola cifra | Demandas civiles de decomiso, informes de fiscalización, comisiones |
| **Quiebras históricas** | Archivo antiguo, a menudo libre; menos competencia | Informes oficiales de la época y archivos nacionales |

## Candidatos (sin enlaces: hay que localizarlos antes de encolar)

Cada uno se sondea antes de puntuar. La columna dice **qué tipo de fuente** buscar, no
una URL.

| Caso | Familia | Dónde buscar el documento |
|---|---|---|
| Bernie Madoff | Ponzi | Demanda de la SEC, acusación penal federal, informes del síndico |
| Allen Stanford | Ponzi | Demanda de la SEC, acusación penal, informes del administrador judicial |
| Enron | Fraude contable | Acciones de la SEC, causas penales, informe del examinador de la quiebra, informes del Congreso |
| WorldCom | Fraude contable | Acción de la SEC e informe del examinador de la quiebra |
| Tyco (Kozlowski) | Fraude contable | Acción de la SEC y proceso penal estatal |
| Adelphia (familia Rigas) | Fraude contable | Acción de la SEC y causa penal federal |
| HealthSouth | Fraude contable | Acción de la SEC y causas penales |
| Theranos | Producto que no existía | Acusación penal federal y demanda de la SEC |
| Nikola (Trevor Milton) | Producto que no existía | Acusación penal federal y demanda de la SEC |
| FTX | Cripto | Acusación penal federal y expediente de la quiebra con sus informes |
| Celsius | Cripto | Acusación penal federal y acciones de reguladores |
| BitConnect | Cripto | Acción de la SEC y causa penal federal |
| OneCoin | Cripto | Acusación penal federal y material del FBI |
| Archegos | Fondos | Acusación penal federal y demanda de la SEC |
| MF Global | Fondos | Acción del regulador de derivados e informes del síndico |
| Barings (Nick Leeson) | Fondos | Informe oficial de la supervisión bancaria británica |
| BCCI | Bancos | Informe de investigación del Senado de EE.UU. |
| 1MDB | Saqueo público | Demandas civiles de decomiso del DOJ y acuerdos con bancos |
| Wirecard | Fraude contable | Regulador alemán, comisión parlamentaria de investigación y proceso penal |
| Bre-X | Materias primas | Actuaciones del regulador de valores canadiense y causas judiciales |
| Fyre Festival | Producto que no existía | Acusación penal federal y sentencia |
| Charles Ponzi | Histórico | Archivos judiciales y prensa de época (⚠️ verificar derechos de cada imagen) |

⚠️ Los casos con **opioides, armas o violencia** en el centro —aunque sean historias de
dinero— van al final de la cola: el icono amarillo hunde el CPM del nicho.

**Producido:** episodio 01 — el negocio de exportación como tapadera, contado desde el
dinero y no desde la violencia.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Elegir el caso por lo famoso que es | Sin archivo libre no hay episodio, por famoso que sea |
| Escribir el guion antes de sondear el archivo | Tres días de trabajo para un vídeo que no se puede ilustrar |
| Encolar un caso sin desenlace documentado | El remate se inventa o se queda cojo |
| Un caso sin cifra clara | No hay cálculo propio, y sin él el episodio es un resumen |
| Repetir familia dos episodios seguidos | El canal se vuelve monótono; alternar familia y época |
| No anotar el motivo de descarte | Se vuelve a sondear el mismo caso dentro de dos meses |

## Relacionado

`90` fuentes primarias · `92` el aporte original · `93` estructura de episodio ·
`96` verificación de datos · `99` título, miniatura y descripción
