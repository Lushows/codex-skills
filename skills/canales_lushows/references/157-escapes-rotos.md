# 157 · Escapes rotos al parchear código

**Qué resuelve:** parchear Python desde un heredoc de shell convierte `\n` en un salto
de línea real. **El archivo deja de compilar** — y si el parche sólo tocó una rama poco
frecuente, el fallo aparece tres pasos más tarde. Ocurrió **tres veces en una sesión**.

---

## Cómo se manifiesta

```bash
cat > parche.py <<EOF
filtros.append(f"[{n}:v]scale={anchura}:-1,format=rgba,"
               f"fade=t=in:st={e0:.2f}:d=0.30:alpha=1\n")
EOF
```

El shell expande `\n` **dentro** del heredoc sin comillas. Lo que llega al disco es:

```python
               f"fade=t=in:st={e0:.2f}:d=0.30:alpha=1
")
```

```
SyntaxError: unterminated string literal (detected at line 187)
```

Con `SyntaxError` hay suerte: se ve al instante. Los casos malos son otros:

| Qué se rompe | Cómo se manifiesta |
|---|---|
| `\n` dentro de una cadena de filtro de ffmpeg | El filtro se parte; ffmpeg dice *«Invalid argument»* |
| `\\,` dentro de una expresión `eq` | **El destello no ocurre.** Cero errores |
| `$` sin escapar en un heredoc | `${n}` se expande al valor de una variable del shell |
| `` ` `` sin escapar | El shell ejecuta lo de dentro |
| `\b` en un regex | Se convierte en retroceso: el corrector de tildes deja de casar |

El de `eq` es el peor. La campana de Gauss del destello se construye así en `motor.py`:

```python
bri = "+".join(f"{f:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))" for td, f, s in picos)
```

Esa doble barra es obligatoria: ffmpeg usa la coma como separador de filtros y dentro
de una expresión hay que escaparla. Si el parche la convierte en `,`, el grafo cambia
de forma, ffmpeg lo acepta y **el fogonazo simplemente no aparece**.

## Por qué ocurre

El código del canal está lleno de cadenas que son **lenguajes dentro de Python**:
expresiones de ffmpeg, CSS, regex, HTML. Cada uno tiene su propio escapado, y el
heredoc del shell añade una capa encima: `shell → heredoc → literal de Python →
f-string → filtro de ffmpeg`. Cuatro traducciones, y un `\` puesto para la última lo
procesa la primera.

## Cómo se caza

**Comprobación de sintaxis como paso previo, siempre.** No renderizar, no abrir el
resultado: compilar.

```bash
python -m py_compile motor.py auditar.py diccionario.py guion_visual.py \
  && echo "sintaxis OK" || echo "NO TOCAR NADA MÁS HASTA ARREGLAR ESTO"
```

Para lo que compila pero está mal, revisar los literales que son filtros de ffmpeg:

```python
import ast
arbol = ast.parse(open("motor.py", encoding="utf-8").read())   # falla si hay SyntaxError
for nodo in ast.walk(arbol):
    if isinstance(nodo, ast.Constant) and isinstance(nodo.value, str):
        s = nodo.value
        if "\n" in s and any(k in s for k in ("overlay", "fade=", "eq=", "zoompan")):
            print(f"  línea {nodo.lineno}: salto de línea dentro de un filtro")
        if "exp(-pow(" in s and "\\," not in s:
            print(f"  línea {nodo.lineno}: coma sin escapar en expresión de eq")
```

Y, después de cualquier parche, **imprimir el grafo montado antes de ejecutarlo**
(`print(";".join(filtros).replace(";", ";\n"))`). Verlo con los ojos cuesta veinte
segundos y cierra la clase entera.

## La guardia automática

Tres reglas de trabajo, por orden de preferencia:

**Uno · no parchear código con heredocs.** Editar el archivo con una herramienta de
edición, que no reinterpreta nada. Es la regla, y las otras dos son para cuando no hay
más remedio.

**Dos · si hay que usar heredoc, con el delimitador entre comillas simples.** Así el
shell no expande `$`, ni `` ` ``, ni las secuencias de barra:

```bash
cat > fragmento.py <<'FIN'
bri = "+".join(f"{f:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))" for td, f, s in picos)
FIN
```

`<<'FIN'` en vez de `<<FIN`. Un solo par de comillas separa el archivo correcto del
archivo roto.

**Tres · la compilación es parte del parche, no un paso opcional.** Un cambio no está
hecho hasta que compila:

```bash
python -m py_compile "$f" || { git checkout -- "$f"; echo "parche revertido"; exit 1; }
```

Revertir es mejor que dejar el archivo a medias: un `motor.py` que no compila bloquea
el render entero, y el impulso de «arreglarlo rápido» con otro heredoc es lo que
convirtió un fallo en tres.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `<<EOF` sin comillas | `\n`, `$` y `` ` `` se expanden: el archivo deja de compilar |
| Parchear y renderizar sin compilar | Ocho minutos de render para descubrir un `SyntaxError` |
| Arreglar un heredoc roto con otro heredoc | Un fallo se convierte en tres, en la misma sesión |
| Perder el `\\,` de las expresiones `eq` | El destello no ocurre y no hay error |
| Perder el `\b` de un regex | El corrector de tildes deja de casar y aprueba todo |
| Dejar un archivo a medias «para seguir luego» | Nada del pipeline corre; se pierde el contexto del fallo |

## Relacionado

`150` el catálogo del fallo silencioso · `158` procesos que se pisan · `159` cómo se
caza un fallo que no avisa · `67` luz y destellos · `74` flash y golpe
