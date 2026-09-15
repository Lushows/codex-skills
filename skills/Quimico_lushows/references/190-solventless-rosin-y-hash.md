# 190 — Solventless: hash de agua y rosin (calidad premium sin un solo solvente)

Solventless es la única ruta donde el único "solvente" es **agua, hielo y presión**. No hay etanol, no hay
butano, no hay CO₂ — y por lo tanto **no hay ensayo de solventes residuales que reprobar**. Por eso el
rosin de hash es el segmento de mayor precio por gramo en los mercados legales maduros y, al mismo tiempo,
el proceso más accesible para alguien pequeño: puedes empezar con baldes, bolsas de malla y una prensa de
mesa. Su límite es que **no purifica nada**: si la planta traía pesticidas o metales, ahí siguen. Este
módulo te da la mecánica, los rendimientos reportados y el criterio de calidad.

Términos:
- **tricoma (trichome)** = la glándula resinosa de la flor; su cabeza es donde vive casi todo el cannabinoide.
- **hash de agua / bubble hash (ice water hash)** = tricomas separados mecánicamente en agua helada y
  clasificados por tamaño de malla.
- **micras (microns)** = luz de malla de las bolsas de filtrado; se habla de "73–120 µ" como el rango
  premium porque ahí caen las cabezas de tricoma maduras.
- **rosin** = extracto obtenido aplicando calor y presión, sin solvente.
- **rosin de flor (flower rosin)** vs. **rosin de hash (hash rosin)** = prensar flor seca vs. prensar hash.
- **fresh frozen** = planta congelada al cosechar, sin secar; da el mejor hash porque el tricoma no se
  degradó ni se pegó.

## Los dos procesos

### Hash de agua

El agua helada vuelve quebradiza la unión entre el tricoma y la planta. La agitación suave los desprende, y
una torre de bolsas de distintas micras los clasifica por tamaño.

```
Fresh frozen (o flor seca) + agua a 0–4 °C + hielo
   ↓ agitación suave (3–15 min por lavado)
Suspensión → torre de bolsas: 220 µ (planta) → 160 → 120 → 90 → 73 → 45 → 25 µ
   ↓ recolección por bolsa, prensado del agua, congelado
Liofilización (freeze dryer) — 24–48 h — o secado al aire frío
   ↓
Hash seco, clasificado por fracción
```

La **liofilización (freeze drying)** es el salto de calidad: secar al aire tarda días, calienta el material y
degrada terpenos; liofilizar tarda horas y conserva el perfil. Es la inversión que separa el hash artesanal
del hash comercial.

### Rosin

Calor moderado + presión hacen que la resina fluya y salga de la bolsa de filtrado.

| Variable | Rango de trabajo | Efecto |
|---|---|---|
| Temperatura de placas | 70–90 °C (flor); 55–75 °C (hash) | Más frío = más terpeno y consistencia "cold cure"; más caliente = más rendimiento y menos aroma |
| Presión | Fuerza controlada, no "a fondo" | Exceso revienta la bolsa y arrastra material vegetal |
| Tiempo | 45 s – 3 min | Prensadas largas queman terpenos |
| Micraje de la bolsa | 25–90 µ (hash); 90–160 µ (flor) | Malla fina = producto más limpio, menos rendimiento |
| Humedad de la flor | 58–62 % HR equivalente | Flor muy seca no fluye; muy húmeda emulsiona |

## Rendimientos reportados

Cifras que circulan en la industria y en guías de fabricantes de prensas — **rango de referencia, no
promesa**: verifica con tu material.

| Material de partida | Rendimiento de rosin reportado | Fuente del rango |
|---|---|---|
| Flor seca → rosin de flor | 15–25 % (algunas fuentes 15–30 %) | Guías de fabricantes de prensa (The Press Club, Green Thumb Depot) |
| Flor → hash de agua | 10–20 % | Mismas guías |
| Hash de agua → rosin de hash | 50–80 % (frecuente 60–70 %) | Mismas guías |
| Flor → rosin de hash (ruta completa) | Comparable a la ruta directa de flor | Producto de las dos etapas anteriores |

La explicación química del salto es simple: cuando prensas flor estás apretando quizá 5–15 % de cabezas de
tricoma contra 85–95 % de fibra vegetal; cuando prensas hash aprietas 60–90 % de cabezas contra casi nada.

Y la conclusión de negocio, que casi nadie hace explícita: **el rendimiento total desde flor es parecido por
las dos rutas** (porque el lavado ya te costó rendimiento), pero **la calidad y el precio por gramo no lo
son**. Haz esa cuenta con tus propios números y en código —`lab-tools/rendimiento_extraccion.py` o
`Matematicas_lushows`— antes de decidir la ruta.

## Qué NO hace el solventless

Aquí está el error de posicionamiento más caro del segmento. Solventless significa "sin solvente añadido".
**No significa "puro", "limpio" ni "libre de contaminantes":**

- Los **pesticidas** que estaban en la planta se concentran igual que los cannabinoides (`200`).
- Los **metales pesados** que la raíz absorbió siguen ahí, y se concentran (`202`).
- La **carga microbiana** puede empeorar: agua tibia, material húmedo y secado lento son un caldo de cultivo.
  El hash mal secado es un problema de microbiología, no de estética (`203`).
- El **agua** que uses entra a tu producto. Agua de acueducto con cloro o con hierro deja marca (`106`).

Por eso el solventless exige el mismo panel de contaminantes que cualquier otro extracto. Ahorras el ensayo
de solventes residuales; no ahorras ninguno de los demás.

## Cómo se mide / cómo se comprueba

| Ensayo | Técnica | Unidad | Nota específica del solventless |
|---|---|---|---|
| Potencia y perfil | HPLC-DAD (`198`) | % p/p | El rosin de hash bien hecho suele mantener THCA alto: prensado frío no descarboxila mucho |
| Terpenos | GC-MS / GC-FID headspace (`199`) | mg/g | Es el argumento de valor del producto; mídelo o no lo cobres |
| Solventes residuales | GC-MS headspace (`201`) | ppm | **Debe salir no detectado**: es tu prueba documental del claim "solventless" |
| Metales pesados | ICP-MS (`202`) | µg/kg | No perdona: nada en el proceso los quita |
| Pesticidas | LC-MS/MS y GC-MS/MS (`200`) | µg/kg | Se concentran; el ensayo es sobre el extracto, no sobre la flor |
| Microbiología y micotoxinas | Cultivo/qPCR, LC-MS/MS (`203`) | UFC/g, µg/kg | El riesgo propio de este proceso |
| Actividad de agua del hash | Medidor aw (`35`) | adimensional | Control de secado: hash mal liofilizado = moho |

Consejo de auditoría: pide siempre el COA con **solventes residuales aunque no uses solventes**. Un "no
detectado" documentado es lo que convierte tu claim de marketing en un dato defendible (`293`).

## Ejemplo aplicado (ILUSTRATIVO)

10,0 kg de *fresh frozen* (≈ 2,7 kg de sólidos secos equivalentes), lavado en tres pases, torre 160/120/90/73/45 µ,
liofilizado 30 h, y prensado a 68 °C. Cifras **(ILUSTRATIVO)**:

| Fracción | Masa seca | Cannabinoides totales | Terpenos | Uso |
|---|---|---|---|---|
| 160–120 µ | 62 g | 51 % p/p | 2,9 % | Prensar a rosin de segunda |
| 120–73 µ ("full melt") | 148 g | 74 % p/p | 5,4 % | Rosin premium |
| 73–45 µ | 71 g | 66 % p/p | 4,1 % | Rosin premium |
| < 45 µ y bolsas de trabajo | 39 g | 38 % p/p | 1,6 % | Comestibles / reproceso |

Total de hash seco: 320 g = **3,2 % sobre material fresco** o **11,9 % sobre base seca**. Prensando las dos
fracciones premium (219 g) a un 65 % de rendimiento salen ≈ 142 g de rosin de hash.

La lección del ejemplo no son los gramos: es que **el mismo lote tiene cuatro precios distintos**. La
fracción de 120–73 µ vale varias veces lo que la de menos de 45 µ, y quien no separa por bolsa está
regalando el margen. Y de nuevo: siempre di sobre qué base reportas (ver `07`).

## Equipo modesto vs. maquila

| Actividad | Con equipo modesto | Exige maquila / equipo mayor |
|---|---|---|
| Lavado de hash (1–5 kg fresco) | **Sí**: baldes, bolsas, hielo, agitador manual | — |
| Congelado del material | Sí: congelador −20 °C o menos | — |
| Liofilización | Liofilizador de mesa (inversión media, USD 3–6 mil) | Para volumen, servicio o equipo industrial |
| Prensado de rosin | **Sí**: prensa de 5–20 t con control de temperatura | Prensas neumáticas para volumen |
| "Cold cure" y consistencias | Sí: horno de precisión a baja temperatura | — |
| Potencia, terpenos, contaminantes | No | **Sí** — laboratorio acreditado (`107`, `108`) |
| Producción a escala de toneladas | No | Sí — planta con lavadoras y liofilizadores industriales |

Este es, con diferencia, **el proceso de cannabis con la barrera de entrada técnica más baja y el producto
final de mayor precio unitario**. Si alguien pequeño va a entrar al negocio de extractos, esta es la puerta
racional; hidrocarburo (`188`) no lo es.

## Errores comunes

- **Vender "solventless" como sinónimo de "limpio".** Los contaminantes de la planta pasan enteros.
- **Agua tibia o agitación violenta.** Rompe las cabezas de tricoma, emulsiona y arrastra clorofila.
- **Secar el hash al aire porque el liofilizador es caro.** Se paga en terpenos perdidos y en riesgo de moho.
- **Mezclar todas las bolsas en un solo producto.** Estás promediando tu mejor fracción con la peor.
- **Prensar caliente para subir el rendimiento.** Ganas gramos y pierdes exactamente lo que el cliente
  compraba (`199`).
- **No medir la actividad de agua del hash.** Es el control que evita el lote perdido por microbiología.
- **Usar agua de acueducto sin analizar.** Cloro, hierro y dureza terminan en el producto (`106`).

## Conexión con otros módulos

→ `186-cosecha-secado-y-curado.md` — el *fresh frozen* nace en la decisión de cosecha.
→ `188-extraccion-con-hidrocarburos.md` — la ruta premium alternativa, con riesgo y capital enormemente mayores.
→ `199-analisis-de-perfil-de-terpenos.md` — el ensayo que sostiene el precio del rosin.
→ `201-solventes-residuales-en-cannabis.md` — el "no detectado" que documenta tu claim.
→ `200-pesticidas-en-cannabis.md` y `202-metales-pesados-en-cannabis.md` — lo que este proceso no quita.
→ `203-micotoxinas-y-microbiologia-en-cannabis.md` — el riesgo propio del agua y el secado.
→ `35-actividad-de-agua-y-humedad.md` — cómo se controla el secado del hash.
→ `150-secado-por-aspersion-y-liofilizacion.md` — la teoría de la liofilización.
