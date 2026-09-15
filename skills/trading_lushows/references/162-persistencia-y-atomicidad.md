# 162 — Persistencia y atomicidad: que un reinicio no corrompa nada

## El problema real

El bot guarda su estado (portafolio, trades, memoria, análisis) en archivos JSON. El peligro:
si el proceso **muere a mitad de una escritura** (Render redeploya, se acaba la memoria, crash),
el archivo queda escrito por la mitad → JSON inválido → al reiniciar, `JSON.parse` explota y el
bot amanece sin memoria o directamente no arranca. En un sistema de trading eso puede significar
"olvidé que tenía una posición abierta". Inaceptable.

## La solución: write-temp-rename (escritura atómica)

"Atómico" significa **todo o nada**: la operación ocurre completa o no ocurre, sin estados
intermedios visibles. La receta de 3 pasos:

1. Escribir el contenido nuevo en un archivo temporal (`portfolio.json.tmp`).
2. (Idealmente) hacer `fsync` — pedirle al sistema operativo que baje los datos al disco físico.
3. **Renombrar** el temporal sobre el archivo real (`rename tmp → portfolio.json`).

La magia está en el paso 3: en los sistemas de archivos habituales, `rename` sobre el mismo disco
es atómico. O el archivo viejo sigue intacto, o el nuevo está completo. **Nunca hay medio archivo.**

| Momento del crash | Qué queda en disco |
|---|---|
| Durante la escritura del `.tmp` | Archivo real intacto; el `.tmp` basura se ignora/borra al arrancar |
| Justo antes del rename | Archivo real intacto (versión anterior) |
| Después del rename | Archivo nuevo completo |

Lo que NUNCA se debe hacer: `fs.writeFile('portfolio.json', ...)` directo sobre el archivo real.
Ese es el bug que produce JSONs corruptos "misteriosos".

## FIFO de históricos: no crecer para siempre

Los archivos de histórico (análisis, meta-análisis, equity) crecerían sin límite si nadie los
poda. El bot usa **FIFO** (First In, First Out: entra el nuevo, sale el más viejo): por ejemplo,
los meta-análisis se limitan a las últimas 52 semanas. Beneficios: el archivo se mantiene chico
(lectura/escritura rápidas), el disco de Render no se llena, y lo relevante para decidir es lo
reciente. Los datos podados no son "pérdida": si algún día se quiere archivo histórico completo,
esa es una feature aparte (exportar antes de podar), no una razón para dejar crecer todo.

## Reglas complementarias

- **Un escritor por archivo.** El diseño evita que dos partes del código escriban el mismo JSON
  a la vez (una escritura atómica no protege contra dos escritores pisándose lógicamente).
- **Validar al leer:** si al arrancar un JSON no parsea, mejor fallar ruidosamente (log + alerta)
  que arrancar con estado vacío en silencio fingiendo que no pasó nada.
- **El disco de Render es persistente pero no es backup** (ver módulo 169).

## Cómo aplica al AGENTE TRADING

Todos los stores de `src/persistence/` (`candlesStore`, `portfolioStore`, `traderMemoryStore`,
`analysesStore`, `metaAnalysesStore` con FIFO 52 semanas, `equityStore`, `alertsStore`) escriben
con write-temp-rename. Es la razón de que 44 días de uptime, con sus redeploys de por medio,
no hayan corrompido ni un archivo. Para live la regla se vuelve sagrada: el portafolio en disco
es la memoria de qué posiciones existen; corromperlo con dinero real no tiene deshacer.
