# 143 · Una comprobación que grita en falso se ignora

**Qué resuelve:** avisos que saltan cuando no pasa nada. Acaban apagándose mentalmente,
y entonces también se ignora el aviso bueno: es peor que no tener la comprobación.

---

## El caso del corrector de tildes

Un canal en español con `ANOS` o `DEFUNCION` en pantalla se descalifica solo, y lo ve
cualquier hispanohablante en el primer segundo. En la prueba del Chapo, **14 de 26
piezas de texto no llevaban una sola tilde**.

La comprobación es simple: se lee el **HTML fuente** de cada pieza (ahí está la palabra
tal y como se escribió, no el PNG) y se busca una lista de palabras que en español
llevan tilde y aparecen sin ella.

La primera versión buscaba **subcadena**. Resultado, sobre texto perfectamente correcto:

| Palabra buscada | Salta dentro de | ¿Hay falta? |
|---|---|---|
| `segun` | SEGUNDA | no |
| `aqui` | CHECOSLOVAQUIA | no |
| `como` | COMODIN | no |
| `numero` | NUMEROSOS | no |
| `fabrica` | FABRICABA | no |
| `maquina` | MAQUINARIA | no |
| `ultimo` | ULTIMOS | no |
| `anos` | HERMANOS, PLANOS | no |

Doce falsos positivos en la primera pasada. A la tercera vez que el informe marca un
titular impecable, nadie vuelve a leer esa sección — y ahí es donde se cuela el
`DEFUNCION` de verdad.

## La corrección: palabra entera

```python
SIN_TILDE = re.compile(
    r"\b(defuncion|informacion|resolucion|duracion|numero|segun|aqui|mexico|"
    r"debito|metodos|fabrica|maquina|calculo|montana|ningun|como|contesto|"
    r"sostenia|joaquin|guzman|compania|anos|traficos|deposito|credito|"
    r"telefono|ultimo|proximo|analisis|decada)\b", re.I)
```

Y se limpia el HTML antes de buscar, para no leer CSS ni etiquetas:

```python
cuerpo = re.sub(r"<style.*?</style>", " ", src, flags=re.S)
cuerpo = re.sub(r"<[^>]+>", " ", cuerpo)
cuerpo = re.sub(r"&[A-Za-z]+;", "X", cuerpo)   # las entidades ya llevan la tilde
```

**Medido hoy sobre las 17 piezas de texto de `ep01-lustig`:**

| Versión | Piezas marcadas | Faltas reales |
|---|---|---|
| Subcadena | 2 (`_d_1890`, `_f_certificado` → *Checoslovaquia*) | 0 |
| Palabra entera | 0 | 0 |

Dos de cada diecisiete piezas gritaban por la misma palabra de un topónimo.

## Las tres causas de una alarma en falso

| Causa | Ejemplo del canal | Arreglo |
|---|---|---|
| **Coincidencia parcial** | subcadena en vez de palabra entera | `\b…\b` |
| **Excepción legítima no declarada** | el logotipo cuenta como repetición | lista `MOTIVOS` (`142`) |
| **Contexto que la regla no ve** | `como` sin tilde es correcto como conjunción | ver abajo |

El tercero no tiene arreglo limpio y hay que asumirlo: `\bcomo\b` marcará *"COMO SE
HIZO"*, que está bien escrito, igual que marcaría *"COMO LO HIZO"* en una pregunta,
que está mal. La regla no distingue interrogativo de conjunción. Se deja en la lista
**sabiendo** que produce revisión manual ocasional, porque el fallo que evita es caro;
si empezara a saltar en cada episodio, se saca de la lista (`147`).

## Cómo se valida una comprobación antes de confiar en ella

Ninguna comprobación entra al auditor sin **dos listas de prueba**:

```python
DEBE_SALTAR   = ["DEFUNCION", "ANOS 20", "DURACION REAL", "DEPOSITO", "CONTESTO A"]
NO_DEBE       = ["SEGUNDA GUERRA", "CHECOSLOVAQUIA", "COMODIN", "NUMEROSOS",
                 "FABRICABA", "MAQUINARIA", "ULTIMOS DIAS", "HERMANOS"]

for t in DEBE_SALTAR:
    assert SIN_TILDE.search(t), f"no detecta: {t}"
for t in NO_DEBE:
    assert not SIN_TILDE.search(t), f"falso positivo: {t}"
```

Ocho líneas. Se corren en un segundo y son la diferencia entre una comprobación que se
lee y una que se salta.

## El criterio para dejarla dentro

Una comprobación se queda si cumple las tres:

1. **Cero falsos positivos** sobre el material que ya existe.
2. **Salta** en al menos un fallo real reproducible.
3. **Dice dónde**: nombre de la pieza y palabra encontrada, no "hay errores".

Formato del aviso, con las dos cosas:

```
  --- piezas de texto SIN TILDE (2) ---
   d_defuncion        defuncion, anos
   f_metodo           calculo
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Buscar subcadena en texto natural | Doce avisos falsos y la sección entera se ignora |
| Poner el aviso sin probarlo contra texto correcto | Se descubre el ruido con el informe ya en uso |
| Avisar sin decir dónde | Nadie lo arregla: hay que buscarlo a mano |
| Dejar una regla que salta cada episodio | Deja de ser una alarma y pasa a ser decorado |
| Tolerar "un par de falsos, no pasa nada" | El aviso bueno viaja escondido entre los falsos |

## Relacionado

`96` verificación de datos · `42` tipografía del canal · `142` la medida que miente ·
`147` cuándo una métrica deja de servir · `148` el cuadro de mando
