# 191 — Winterización y desceramiento (quitar las ceras sin botar el activo)

La winterización es el paso donde el crudo turbio y opaco se vuelve un aceite claro que sí se puede
destilar. Se basa en algo simple: **las ceras y los lípidos de la planta son mucho menos solubles en frío
que los cannabinoides**. Disuelves el crudo en etanol, lo congelas, y las ceras precipitan; filtras y las
botas. Suena elemental y es donde más gente pierde producto sin darse cuenta, porque la torta de filtro se
lleva cannabinoides atrapados y nadie la analiza. Este módulo te da los parámetros, el criterio de filtrado
y cómo cuantificar lo que se te está yendo.

Términos:
- **winterización (winterization)** = precipitación en frío de ceras y lípidos disueltos en etanol.
- **desceramiento (dewaxing)** = el mismo objetivo pero hecho **dentro** del proceso de extracción (columna
  fría en hidrocarburo), sin paso aparte.
- **ceras (waxes)** = ésteres de ácidos grasos de cadena larga, más ceras cuticulares de la planta.
- **torta / pastel de filtro (filter cake)** = el sólido que queda retenido en el filtro.
- **tierra de diatomeas / celite (diatomaceous earth)** = ayuda-filtro que evita que la torta se compacte y
  ciegue el medio.

## Por qué hay que hacerlo

| Problema que causan las ceras | Consecuencia |
|---|---|
| Espuman y arrastran en la destilación | Distillate turbio, "bumping", pérdida de vacío (ver `192`) |
| Enturbian el aceite del cartucho de vapeo | Producto que se ve mal y se separa en el frasco |
| Aportan sabor a "quemado" al vaporizar | Rechazo del consumidor |
| Ensucian la película del wiped film | Paradas de limpieza, menos productividad |

Cuál ruta de extracción las trae y cuánta:

| Ruta de origen | Carga de ceras en el crudo | ¿Necesita winterización? |
|---|---|---|
| Etanol caliente / reflujo | Alta | Sí, obligatorio |
| Etanol a temperatura ambiente | Media-alta | Sí |
| Etanol a −40 °C | Baja | A veces no |
| Hidrocarburo con columna fría (dewaxed) | Baja | Frecuentemente no |
| CO₂ supercrítico | Media | Normalmente sí |
| Solventless (rosin, hash) | — | **No** — no se winteriza, se perdería el perfil (ver `190`) |

## Parámetros de trabajo

Rangos que la práctica industrial usa como punto de partida. Ajusta con tu material.

| Variable | Rango habitual | Qué pasa si te quedas corto |
|---|---|---|
| Relación etanol : crudo | 5:1 a 15:1 (v/p); ratios altos evitan que el cannabinoide coprecipite | Con poco etanol la solución es viscosa y el activo precipita con la cera |
| Temperatura | −20 a −40 °C típico; −60 a −80 °C si buscas máxima remoción | Por encima de −20 °C la precipitación es pobre |
| Tiempo | 12–48 h | Cristales finos que atraviesan el filtro |
| Disolución previa | Disolver **caliente/templado** hasta homogéneo antes de enfriar | Grumos que atrapan activo y nunca se disuelven |
| Filtración | Dos etapas: 25–40 µm de desbaste → 5 µm de pulido, con capa de diatomeas | El medio se ciega y la torta se lleva el producto |
| Recuperación de etanol | Evaporador de película o rotavapor, al vacío | Sobrecalentar el aceite y degradarlo (`204`) |

Dos reglas que resumen la operación:

1. **Disuelve caliente, enfría lento, filtra frío.** Si filtras a temperatura ambiente, las ceras se
   redisuelven y pasan al filtrado: acabas de hacer nada.
2. **La torta verde no se bota, se lava.** Si el pastel de filtro sale verde/dorado en vez de blanco-crema,
   tiene cannabinoides atrapados. Se lava con etanol frío y ese lavado se une al filtrado.

La pérdida de masa por winterización suele ser **de unos pocos puntos porcentuales del crudo** en forma de
grasas y ceras. Si tu proceso te está quitando 15 % o 20 %, no estás quitando cera: estás botando activo.

## Alternativas y complementos

- **Desceramiento en línea (inline dewaxing):** en hidrocarburo, mantener la columna a −20 °C o menos hace
  que las ceras nunca se disuelvan. Es más elegante que winterizar después, y ahorra un paso completo.
- **Filtración con adsorbentes:** carbón activado, tierras activadas o sílice para **decolorar**. Ojo: la
  sílice ácida puede isomerizar CBD hacia Δ8/Δ9-THC con calor (ver `180`, `193`). Decolorar no es winterizar.
- **Centrifugación en frío:** separa sin filtro, útil a gran escala.
- **Winterización con el mismo hidrocarburo:** posible, pero mueve el paso a un área clasificada (`188`).

## Cómo se mide / cómo se comprueba

Winterizar "hasta que se vea claro" no es un control de proceso. Lo que se mide:

| Ensayo | Técnica | Unidad | Para qué |
|---|---|---|---|
| Potencia antes y después | HPLC-DAD (`198`) | % p/p | Calcular la recuperación real del paso |
| **Potencia de la torta de filtro** | HPLC-DAD (`198`) | % p/p | El número que nadie mide y que dice cuánto botaste |
| Terpenos antes/después | GC-MS headspace (`199`) | mg/g | La winterización y su evaporación se llevan volátiles |
| Solventes residuales | GC-MS headspace (`201`) | ppm | El etanol añadido hay que quitarlo otra vez |
| Metales pesados | ICP-MS (`202`) | µg/kg | Se concentran al perder masa |
| Contenido de grasas/ceras | Gravimetría o pérdida de masa del paso | % p/p | Control del proceso lote a lote |
| Turbidez / claridad | Visual o turbidímetro | NTU | Control rápido en línea, nunca como liberación |

```
Recuperación del paso (%) = (masa aceite winterizado × %cannabinoides después)
                          / (masa crudo × %cannabinoides antes) × 100
```

Ejecuta esa cuenta en `lab-tools/rendimiento_extraccion.py`; en un proceso sano debería quedar **por encima
de 90 %**. Si baja de ahí, la torta es el sospechoso número uno.

## Ejemplo aplicado (ILUSTRATIVO)

5,00 kg de crudo de etanol con 68,0 % p/p de cannabinoides totales (HPLC-DAD). Etanol absoluto 8:1,
disolución a 40 °C, 24 h a −40 °C, filtración 25 µm + 5 µm con capa de diatomeas. Cifras **(ILUSTRATIVO)**:

| Corriente | Masa | Cannabinoides | Cannabinoides absolutos |
|---|---|---|---|
| Crudo de entrada | 5,00 kg | 68,0 % | 3,400 kg |
| Aceite winterizado | 4,52 kg | 72,6 % | 3,282 kg |
| Torta de filtro (seca) | 0,41 kg | 24,0 % | 0,098 kg |
| Balance no contabilizado | — | — | 0,020 kg |

Recuperación = 3,282 / 3,400 = **96,5 %**. La torta se llevó 98 g de cannabinoides — casi 3 % del total. Un
lavado con etanol frío del pastel habría rescatado buena parte de eso. Y fíjate en el otro efecto: la
concentración **subió** de 68,0 % a 72,6 % sin haber "purificado" nada químicamente; simplemente quitaste
masa inerte. Ese es todo el truco de la winterización.

## Equipo modesto vs. maquila

| Actividad | Con equipo modesto | Exige maquila / planta |
|---|---|---|
| Winterizar 100 g – 5 kg de crudo | **Sí**: congelador −40 °C, embudo Büchner, bomba de vacío, filtros | — |
| Recuperar el etanol | Rotavapor hasta ~20 L/día | Falling film para volumen real |
| Winterizar decenas de kg por día | No | Sí: tanques encamisados, filtro prensa, centrífuga |
| Decoloración con adsorbentes | Sí, a pequeña escala y con control de temperatura | — |
| Potencia, terpenos, solventes, metales | No | **Sí** — laboratorio acreditado (`107`, `108`) |
| Análisis de la torta de filtro | No | Sí — y es el que más plata devuelve |

Es, junto con el solventless, uno de los pocos pasos del cannabis que **sí se puede hacer bien con
presupuesto modesto**. El cuello de botella real no es la winterización: es la evaporación del etanol.

## Errores comunes

- **No lavar la torta de filtro.** Es la fuga de activo más común y más fácil de tapar.
- **Filtrar tibio.** Las ceras se redisuelven y el paso no sirvió de nada.
- **Ratio de etanol bajo.** La solución queda viscosa y el cannabinoide coprecipita con la cera.
- **Confundir decoloración con winterización.** Quitar color no quita ceras, y quitar ceras no aclara el color.
- **Winterizar rosin o hash de agua.** Destruyes exactamente el perfil por el que ese producto vale más (`190`).
- **Sobrecalentar en la recuperación de etanol.** El aceite se oxida y aparece CBN (`204`).
- **No volver a medir solventes residuales después del paso.** Metiste etanol nuevo: hay que volver a
  demostrar que salió (`201`).
- **No pesar y analizar cada corriente.** Sin balance de masa (ver `06`) no sabes dónde se fue el producto.

## Conexión con otros módulos

→ `19-soluciones-y-solubilidad.md` — por qué el frío precipita la cera y no el cannabinoide.
→ `187-extraccion-con-etanol.md` — el crudo que casi siempre alimenta este paso.
→ `188-extraccion-con-hidrocarburos.md` — el desceramiento en línea que evita este paso.
→ `189-extraccion-co2-en-cannabis.md` — las ceras del corte S1/S2.
→ `192-destilacion-de-cannabinoides.md` — el paso siguiente, que exige aceite winterizado.
→ `149-concentracion-y-evaporacion.md` — cómo se recupera el etanol sin quemar el aceite.
→ `06-estequiometria-y-balance-de-masa.md` — el balance que delata la fuga.
→ `201-solventes-residuales-en-cannabis.md` — el ensayo que hay que repetir tras este paso.
