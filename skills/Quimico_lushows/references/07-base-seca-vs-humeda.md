# 07 — Base seca vs base húmeda (el campo que más se calla y más engaña)

Un porcentaje siempre está dividido por algo. Cuando dices "28 % de β-glucano", estás diciendo 28 g por
cada 100 g de… ¿de qué? ¿De material tal como está, con su humedad? ¿De material completamente seco?
La respuesta cambia el número, cambia el precio que pagas por kilo de activo y cambia si dos COA son
comparables o no. Un hongo puede tener 8 % de humedad o 12 %, y esa diferencia sola mueve el resultado
casi un 5 % relativo. Es el campo que más se omite en los certificados comerciales, y omitirlo casi
nunca es casual: siempre se omite en la dirección que favorece a quien vende.

Términos: **base húmeda (as-is / wet basis)** = el porcentaje se calcula sobre la masa del material tal
como está, con su humedad. **base seca (dry basis, DB)** = sobre la masa del material sin agua.
**humedad (moisture content)** = agua expresada como % de la masa. **pérdida por secado (loss on
drying, LOD)** = método gravimétrico para medir humedad, típicamente a 105 °C hasta peso constante.
**actividad de agua (water activity, aw)** = agua disponible para microorganismos, distinta de la
humedad total.

## La conversión, en dos líneas

```
% base seca   = % base húmeda / (1 − humedad_fraccional)
% base húmeda = % base seca × (1 − humedad_fraccional)

Ej.: 27,0 % base húmeda con 10 % de humedad
     27,0 / (1 − 0,10) = 30,0 % base seca
```

Y para comparar dos materiales con humedades distintas, se llevan **ambos a base seca** antes de
compararlos. Nunca al revés. Ejecuta con `lab-tools/base_seca.py`.

## Cuánto mueve la aguja

| Humedad del material | Factor de conversión (÷ 1−h) | Un 25 % base húmeda equivale a |
|---|---|---|
| 3 % | 1,031 | 25,8 % base seca |
| 5 % | 1,053 | 26,3 % base seca |
| 8 % | 1,087 | 27,2 % base seca |
| 10 % | 1,111 | 27,8 % base seca |
| 12 % | 1,136 | 28,4 % base seca |
| 15 % | 1,176 | 29,4 % base seca |

Entre 3 % y 15 % de humedad hay un 14 % relativo de diferencia en el número declarado, sin que cambie
nada del material. Ahí viven muchas "mejoras" de potencia entre proveedores.

## Qué se declara en base seca y qué no

| Dato | Base habitual | Por qué |
|---|---|---|
| Activos en materia prima y extractos (β-glucano, triterpenos, cannabinoides) | Base seca | Permite comparar lotes y proveedores |
| Metales pesados, micotoxinas, pesticidas | Suele reportarse tal cual o base seca — **hay que leerlo** | El límite legal define cuál aplica |
| Contenido en producto terminado (mg por cápsula) | Tal cual, en masa absoluta | Es lo que el cliente consume |
| Humedad del propio material | No aplica | Es el dato base |
| Microbiología (UFC/g) | Tal cual | Se cuenta sobre el producto real |

Punto crítico regulatorio: **el límite de un contaminante puede estar definido sobre una base
específica**. Si el reglamento fija 2 ppm de plomo "sobre producto tal como se comercializa" y tú
comparas contra un resultado en base seca, puedes declararte incumplido sin estarlo, o al revés.
Fecha y verifica la norma aplicable (ver `265`, `272`).

## Cómo se mide la humedad

| Método | Qué mide | Cuándo usarlo | Ojo |
|---|---|---|---|
| Pérdida por secado a 105 °C | Todo lo volátil, no solo agua | Rutina, barato, en tu propia planta | Sobrestima si hay terpenos o solventes |
| Balanza de humedad por halógeno | Igual que arriba, rápido | Control de proceso en línea | Calibrar contra estufa |
| Karl Fischer | Agua específicamente | Extractos, aceites, material con volátiles | Más caro, requiere equipo (ver `98`) |
| Actividad de agua (aw) | Agua disponible | Riesgo microbiológico y vida útil | No reemplaza humedad total (ver `35`) |

En cannabis, secar a 105 °C evapora terpenos y **descarboxila** parcialmente: la "humedad" que te da
está inflada y el material queda alterado. Ahí Karl Fischer es el método correcto.

## Ejemplo aplicado (BIO-SETA)

Dos cotizaciones de extracto de reishi en polvo:

| | Proveedor A | Proveedor B |
|---|---|---|
| β-glucano declarado | 30,0 % | 27,5 % |
| Base declarada | no dice | base seca |
| Humedad | 11,5 % | 4,2 % |
| Precio | USD 62 / kg | USD 70 / kg |

Llevando A a base seca (asumiendo que su 30 % era "tal cual"): `30,0 / (1 − 0,115) = 33,9 % base seca`.
A queda arriba. Pero atención: estás pagando por agua. Costo por kg de β-glucano **(ILUSTRATIVO)**:

```
A: 1 kg de polvo -> 0,300 kg de β-glucano (tal cual)  ->  62 / 0,300 = USD 207 por kg de β-glucano
B: 1 kg de polvo -> 0,275 × (1 − 0,042) = 0,2634 kg   ->  70 / 0,2634 = USD 266 por kg de β-glucano
```

A sale más barato por kilo de activo, **si su declaración es cierta y si su método es el mismo**. Y ese
"si" es todo: antes de decidir hay que confirmar el método (Megazyme enzimático vs colorimétrico) y la
base. Con métodos distintos, esta comparación no vale nada (ver `02`, `221`).

Además, un extracto con 11,5 % de humedad es un riesgo de estabilidad y de microbiología en el clima
colombiano; el ahorro puede evaporarse en producto perdido (ver `35`, `164`).

## Errores comunes

- **Comparar dos COA sin llevarlos a la misma base.** El error más frecuente del sector.
- **Asumir que "no dice base" significa base seca.** Casi siempre significa base húmeda, que da un
  número menor y por eso conviene callarlo... salvo cuando conviene lo contrario.
- **Secar a 105 °C material con terpenos o solventes** y llamar "humedad" a lo que se fue.
- **Pagar por kilo de polvo en vez de por kilo de activo.** El precio relevante es el segundo.
- **Olvidar que la humedad cambia con el tiempo.** Un polvo higroscópico gana agua en bodega; la
  potencia por gramo baja sin que nada químico haya pasado (ver `163`).
- **Comparar un contaminante contra un límite en otra base**, y llegar a la conclusión equivocada sobre
  cumplimiento.

## Conexión con otros módulos

→ `04-unidades-concentraciones-y-conversiones.md` — la aritmética de porcentajes y ppm.
→ `06-estequiometria-y-balance-de-masa.md` — el balance solo cierra en base seca.
→ `35-actividad-de-agua-y-humedad.md` — el agua como riesgo microbiológico y de estabilidad.
→ `98-karl-fischer-y-humedad.md` — el método específico para agua.
→ `110-como-leer-un-coa.md` — dónde buscar la base en un certificado real.
→ `242-ratios-de-extraccion-y-etiquetado-honesto.md` — la base aplicada a hongos y ratios.