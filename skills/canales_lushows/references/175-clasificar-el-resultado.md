# 175 · Clasificar: historia, contexto y ruido

**Qué resuelve:** repartir el resultado del sondeo en tres montones antes de decidir
nada, porque un total alto puede esconder un episodio imposible.

---

## Los tres montones

| Montón | Qué es | Ejemplo del sondeo de Enron |
|---|---|---|
| **De la historia** | La persona, el edificio, el documento, el objeto **de este caso** | `File:Enron Complex.jpg`, `File:Enron Code of Ethics cover.jpg` |
| **Contexto** | Verdadero y de la época, pero de cualquier caso parecido | `Downtown Houston` (87 piezas), `Accounting` (43), `Bankruptcy` (29) |
| **Ruido** | Homónimos y falsos positivos | `Hans Christian Andersen by Arthur Rackham`, `Hebe subalpina (Cockayne) Andersen` |

El montón que decide si hay episodio es el primero. Los otros dos **rellenan**, y un
documental que solo tiene relleno es un vídeo de stock con voz encima.

## Cómo se clasifica

No hay automatismo que lo haga bien: el ruido se cuela por el título y el contexto se
parece a la historia. Lo que sí funciona es un pre-recuento automático —cuántas piezas
nombran el caso— y después **mirar esa lista corta una a una**, que son minutos.

```python
import json, io, re, collections

d = json.load(io.open("ep01-enron/sondeo.json", encoding="utf-8"))
CLAVE = re.compile(r"enron|lay|skilling|fastow|andersen|sarbanes", re.I)

nombran = [x for x in d if CLAVE.search(x["titulo"])]
print(f"total sondeado : {len(d)}")
print(f"nombran el caso: {len(nombran)}")
for x in nombran:
    print(f"  {x['px']:<12} {x['titulo'][5:72]}")

print("\ncontexto: las búsquedas que más aportan")
for k, v in collections.Counter(x["busqueda"] for x in d).most_common(6):
    print(f"  {v:4d}  {k}")
```

**Salida real (11-sep-2026), recortada:**

```
total sondeado : 379
nombran el caso: 31
  3987x2848    December 2017- Enron Code of Ethics.jpg
  3888x2592    Enron Complex.jpg
  1024x1024    Enron Email Network.jpg
  2272x1704    Immeuble Andersen.jpg
  4096x2730    Enron Corporation Dassault Falcon 900 (N5733-39).jpg
  1024x768     Gas pipeline laying, Omagh - geograph.org.uk - 8178509.jpg
  2265x1500    US Navy 081120-N-5758H-379 Sailors lay out mooring lines.jpg
  5291x7544    Hebe subalpina (Cockayne) Andersen (AM AK8013).jpg
  4590x6810    Hans Andersen's fairy tales, illustrated ... by Arthur Rackham
  724x876      JoleneAndersen.jpg
  ...

contexto: las búsquedas que más aportan
    87  Downtown Houston
    43  Accounting
    35  electricity transmission tower
    34  ledger accounting book
    29  Bankruptcy
    24  United States congressional hearing
```

## El recuento que importa

```
total sondeado ................ 379
nombran el caso ................ 31   (8 %)
son de verdad del caso ......... 11   (3 %)
resto (contexto y ruido) ...... 348
```

Las veinte restantes de esas 31 son homónimos puros: los cuentos de Hans Christian
Andersen, una planta neozelandesa, una luchadora apellidada Andersen, tuberías que se
estaban *laying* en Omagh, un asfaltado en Portrush y marineros recogiendo amarras. (La
primera pasada del sondeo dio la misma forma con otros números: 276 útiles y 14 del caso.)

**Un caso con cientos de piezas de contexto y once de la historia no es un caso con
archivo.**
Es un caso que hay que contar de otra manera, o dejar.

## Qué hacer con cada montón

- **De la historia (11):** se reservan para los momentos que las necesitan de verdad —el
  primer plano del protagonista, el documento que prueba la cifra, el edificio en el
  gancho—. No se gastan en transiciones.
- **Contexto (276):** se selecciona por escenario con cupo (`191`), no por orden de
  aparición. Un rascacielos de Houston sirve para decir «Houston», no para decir «Enron».
  Y se rotula con cuidado: si en pantalla se ve una torre cualquiera mientras la voz dice
  «la sede de Enron», eso es una afirmación falsa (`198`).
- **Ruido:** fuera del `sondeo.json`, no «por si acaso». Una pieza de ruido guardada
  acaba en el montaje un martes a las once de la noche.

## Cuando el montón de historia está vacío: las tres salidas

1. **Contar por documento.** Si no hay caras pero sí actas, acusaciones e informes —y en
   Enron las hay: las audiencias del Congreso están escaneadas y son dominio público— el
   episodio se construye sobre el papel. Es una forma, no un parche (`48`, `91`).
2. **Contar por reconstrucción gráfica.** Silueta, mapa, diagrama de flujo del dinero,
   cifra animada. Nunca un retrato inventado: **caras generadas con IA están prohibidas**.
3. **Cambiar de caso.** Es la salida honesta cuando las dos anteriores no dan (`176`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Contar el total y declarar el caso viable | 379 piezas, once de la historia |
| Confiar el recuento al filtro de título | 31 nombran el caso y 20 son homónimos |
| Usar contexto como si fuera historia | Se afirma en imagen algo que no es verdad |
| Guardar el ruido «por si acaso» | Aparece en el montaje |
| Clasificar después de escribir el guion | El guion pide planos que no existen |

## Relacionado

`173` · `174` · `176` · `191` · `198`
