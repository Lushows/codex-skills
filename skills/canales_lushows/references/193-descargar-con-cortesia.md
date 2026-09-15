# 193 · Descargar sin castigar el servicio

**Qué resuelve:** el archivo del canal sale de servicios gratuitos que nadie está
obligado a mantener. Bajar 700 MB de Wikimedia a toda velocidad, sin decir quién eres y
repitiendo la descarga cada vez que se relanza el script, es la forma más rápida de que
te bloqueen la IP y de quedarte sin archivo a mitad de episodio.

---

## Lo que cuesta un episodio

Medido en el episodio 01: **80 ficheros, 702 MB**, media 8,8 MB por pieza, el mayor
82,9 MB (un plano del metro de París de 300 Mpx). Con las pausas, unos 12 minutos.
Bajar el sondeo entero (988 piezas) serían ~8,7 GB y más de dos horas — ver `190`.

## Regla 1 · El `User-Agent` que dice quién eres

No es cortesía simbólica: **Wikimedia rechaza el agente por defecto de Python**.
Comprobado hoy contra `upload.wikimedia.org`:

```
UA='PaperEmpires-archivo/1.0 (documental; contacto: ...)'  -> 200 · 1.081.644 bytes · 0,88 s
UA='Python-urllib/3.11'                                    -> 403 Forbidden · 0,29 s
```

El `403` llega en 0,29 s y no dice por qué. Sin `User-Agent` propio el script no falla
«a veces»: falla siempre, y parece un problema de red.

```python
UA = ("PaperEmpires-archivo/1.0 "
      "(documental; contacto: acountempirepaper@gmail.com)")
req = urllib.request.Request(url, headers={"User-Agent": UA})
```

Nombre, versión y **un correo que alguien lee**: es lo que permite que te escriban antes
de bloquearte.

## Regla 2 · Pausa entre peticiones

`time.sleep(0.25)` — cuatro peticiones por segundo como techo. Con ficheros de 8,8 MB la
descarga ya dura más que la pausa (el ritmo real es una pieza cada 2-9 s); la pausa
protege el caso contrario, el de los ficheros pequeños en ráfaga. **La pausa va después
de una descarga efectiva**, no después de un fichero que ya estaba: saltársela cuando no
hubo petición es lo que hace que reanudar sea instantáneo.

## Regla 3 · Reanudar sin volver a bajar

```python
out = os.path.join(carp, nombre)
if not os.path.exists(out):
    ...descargar...
    time.sleep(0.25)
fuentes.append({...})     # la ficha se escribe siempre
```

Tiene una trampa grave: un fichero **a medias** (corte de red, Ctrl+C en mitad de los
82 MB) existe, así que nunca se vuelve a bajar y queda corrupto para siempre. La forma
correcta es descargar a un temporal y renombrar al final, que es atómico:

```python
def bajar(url, destino, ua=UA, reintentos=3):
    if os.path.exists(destino) and os.path.getsize(destino) > 0:
        return "ya estaba"
    tmp = destino + ".parcial"
    for intento in range(1, reintentos + 1):
        try:
            cab = {"User-Agent": ua}
            if os.path.exists(tmp):                      # continuar donde se cortó
                cab["Range"] = f"bytes={os.path.getsize(tmp)}-"
            req = urllib.request.Request(url, headers=cab)
            with urllib.request.urlopen(req, timeout=120) as f, open(tmp, "ab") as g:
                esperado = f.headers.get("Content-Length")
                while True:
                    trozo = f.read(1 << 16)
                    if not trozo:
                        break
                    g.write(trozo)
            if esperado and os.path.getsize(tmp) < int(esperado):
                raise IOError("descarga incompleta")
            os.replace(tmp, destino)                     # atómico: o está entero, o no está
            time.sleep(0.25)
            return "bajado"
        except Exception as e:
            espera = 2 ** intento                        # 2 s, 4 s, 8 s
            print(f"  ! {os.path.basename(destino)}: {e} · reintento en {espera}s")
            time.sleep(espera)
    return "falló"
```

`Range` funciona: comprobado contra Wikimedia, `Range: bytes=0-199999` devuelve **206** y
exactamente 200.000 bytes. Con eso, cortar y retomar una descarga de 82 MB cuesta lo que
falte, no 82 MB otra vez.

## Regla 4 · Reintento con espera creciente, no bucle

`2 s, 4 s, 8 s` y se rinde. Un bucle de reintento sin espera contra un servicio que ya
devuelve error es indistinguible de un ataque, y es lo que dispara el bloqueo. Si fallan
los tres intentos se anota la pieza y se sigue: un episodio no se para por una foto.

## Regla 5 · Sin paralelismo

Nada de hilos ni de `asyncio`. Una descarga a la vez. El cuello de botella del canal no
es la red: son los 5 s por imagen de `rembg` (`195`) y los minutos de render. Paralelizar
ahorra minutos y arriesga el acceso a la única fuente de archivo del canal.

## Lo que se registra

```
descargando en ep01-lustig/archivo ...
  ! paris_chemins_de_fer_metropolitain.jpg: timeout · reintento en 2s
80 piezas · 702 MB · fuentes.json escrito
```

Si la línea final dice menos piezas que el cupo, hay huecos que decidir (`191`): no se
sigue al recorte con un archivo incompleto.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| No poner `User-Agent` propio | 403 en todas las peticiones; parece un fallo de red |
| Escribir directo sobre el fichero final | Un corte deja un JPEG truncado que ya nunca se vuelve a bajar |
| Reintentar en bucle sin espera | Bloqueo de IP; se pierde el acceso al archivo |
| Descargar en paralelo con hilos | Riesgo alto para ahorrar minutos en lo que no es el cuello de botella |
| `time.sleep` también cuando el fichero ya estaba | Reanudar 80 piezas tarda 20 s de más por nada |
| Bajar el sondeo entero «por si acaso» | 8,7 GB para usar el 7% |

## Relacionado

`171` · `190` · `192` · `199` · `378`
