# 41 — Fibonacci: retrocesos y extensiones

Los **retrocesos de Fibonacci** son niveles porcentuales que se trazan sobre un movimiento:
tomado un impulso de mínimo a máximo, se marcan el 38.2%, 50% y 61.8% de la vuelta atrás.
La idea: los retrocesos suelen frenar cerca de esos niveles antes de que la tendencia continúe.

## Cómo se usan

- **Retrocesos**: en tendencia alcista, se traza del mínimo del impulso al máximo. Los niveles
  38.2/50/61.8% marcan zonas candidatas donde el retroceso podría terminar (dónde buscar el
  HL de `32`). Retroceso poco profundo (38.2%) = tendencia fuerte; más allá del 61.8% la
  continuación pierde probabilidad.
- **Extensiones**: proyectan targets más allá del máximo previo (127.2%, 161.8%) cuando el
  precio entra en territorio sin referencias históricas.

## La parte honesta: por qué "funciona"

- Los números vienen de la secuencia de Fibonacci y la proporción áurea, que aparece en girasoles
  y caracolas. **No hay ningún mecanismo por el cual una caracola gobierne el precio de BTC.**
- La explicación realista es la **profecía autocumplida**: millones de traders miran los mismos
  niveles, ponen órdenes de compra en el 61.8% y stops debajo — y esa coordinación crea la
  reacción que "confirma" el nivel. Funciona porque muchos creen que funciona.
- Los estudios estadísticos no encuentran que los niveles Fibonacci frenen el precio más que
  niveles porcentuales cualesquiera. Un retroceso "respetó el 61.8%" muchas veces solo porque
  cerca había un soporte real (`31`) que era la verdadera razón.
- Además hay grados de libertad de sobra: ¿desde qué mínimo? ¿hasta qué máximo? ¿con mechas o
  cuerpos? Dos traders trazan el mismo impulso distinto — y ambos encuentran "su" nivel respetado.

## Uso prudente (si se usa)

1. Solo como **mapa de zonas candidatas** para retrocesos en tendencia — nunca como señal.
2. Exigir **confluencia**: un 61.8% que coincide con un soporte previo y con la SMA20 es
   interesante; un 61.8% solo, en el vacío, es numerología.
3. No discutir con el precio: si el nivel se pierde con decisión, no era "el nivel".

## Cómo aplica al AGENTE TRADING

- El bot no usa Fibonacci y **no lo necesita**: sus soportes/resistencias (`31`) y la SMA20
  como zona de retroceso (`33`) cubren la misma función — "¿dónde podría terminar el
  retroceso?" — con niveles que tienen una justificación mecánica (memoria del mercado) en vez
  de una mística.
- Si Claude menciona Fibonacci al analizar, el marco correcto es: "el retroceso está en la zona
  del 50-61.8% del impulso" como descripción de PROFUNDIDAD del retroceso (¿leve o profundo?),
  que sí es información útil — no como "el 61.8 va a aguantar", que es predicción disfrazada.
