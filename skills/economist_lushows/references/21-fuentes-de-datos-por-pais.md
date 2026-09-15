# 21 — Fuentes de datos por país

Este módulo es tu **antídoto contra inventar números**. Te enseña dónde buscar datos REALES de mercado en cualquier país, cómo cruzarlos para confiar en ellos (triangulación) y cómo estimar de forma honesta cuando el dato no existe. Si en algún momento de un análisis pones una cifra sin fuente, vuelve aquí.

## Regla cero: pregunta el país y la ciudad PRIMERO

Antes de buscar un solo dato, fija el **dónde**: país, región/departamento, ciudad. Un "tamaño de mercado de hongos funcionales" no significa nada sin geografía. Toda fuente de abajo cambia según el país. Si no sabes el país del usuario, pregúntalo antes de continuar.

## El mapa de fuentes (de más confiable a menos)

| Nivel | Fuente | Qué te da | Costo |
|---|---|---|---|
| 1. Oficial | Oficina nacional de estadística | Población, ingresos, inflación, censos económicos | Gratis |
| 1. Oficial | Portales de datos abiertos del gobierno | Registros de empresas, comercio exterior, licencias | Gratis |
| 2. Gremial | Cámaras de comercio y asociaciones del sector | Nº de empresas, ventas del sector, tendencias | Gratis / socio |
| 3. Señal de demanda | Google Trends, autocompletar de buscadores | Interés relativo en el tiempo, estacionalidad | Gratis |
| 3. Señal de demanda | Marketplaces (Amazon, ML, etc.) | Precios reales, nº de reseñas (proxy de ventas), competencia | Gratis |
| 4. Pagos | Informes de consultoras (Euromonitor, Statista, Nielsen) | Tamaño de mercado estimado, participación | Caro |
| 5. Tu propio dato | Encuestas, entrevistas, ventas piloto | Lo que NADIE más tiene de tu nicho | Tu tiempo |

### Oficinas nacionales de estadística (el primer lugar SIEMPRE)
Son gratis, públicas y serias. Por país (lista orientativa, verifica el nombre actual):
- **Colombia:** DANE
- **México:** INEGI
- **España:** INE
- **Perú:** INEI · **Chile:** INE Chile · **Argentina:** INDEC · **Ecuador:** INEC
- **EE. UU.:** Census Bureau / BLS · **Global:** Banco Mundial, CEPAL, Eurostat

Qué sacar de ahí: población por ciudad y edad, ingreso promedio del hogar, gasto por categoría (encuestas de hogares), número de establecimientos por actividad económica (censos económicos). Es la base para calcular tu TAM/SAM/SOM (ver 20).

### Gremios y cámaras de comercio
Casi todo sector tiene una asociación (de panaderos, de software, de turismo). Publican informes anuales con número de empresas y ventas del sector. La **cámara de comercio** local suele tener el registro de empresas activas por actividad: te dice cuántos competidores hay de verdad. A menudo basta con escribir o llamar y pedir el dato.

### Google Trends y marketplaces (demanda barata y rápida)
- **Google Trends:** no da números absolutos, da interés RELATIVO. Sirve para ver si algo crece o cae, comparar dos ideas y detectar estacionalidad (ej.: "regalos" sube en diciembre). Filtra por país y ciudad.
- **Marketplaces:** abre Amazon / Mercado Libre / la tienda dominante de tu país. Los **precios** son reales. El **número de reseñas** es un proxy de cuántas unidades se han vendido (regla cruda: las ventas reales suelen ser varias veces las reseñas). Cuenta competidores y mira sus rangos de precio.

### Informes pagos
Statista, Euromonitor, Nielsen, IBISWorld dan tamaños de mercado ya calculados, pero son caros (cientos a miles de USD). Trucos legítimos: busca el **resumen gratuito** del informe, notas de prensa que citan la cifra, o tesis y papers universitarios que ya pagaron el acceso y publican el número con su fuente.

## Triangulación: la regla de las 2-3 fuentes

**Nunca confíes en un solo número.** Triangular = estimar lo mismo por 2-3 caminos distintos y ver si concuerdan. Si dan parecido, confías. Si dan muy distinto, encontraste un error o un supuesto malo.

**Ejemplo numérico ilustrativo (cifras inventadas, solo para mostrar el método):**
Quieres el mercado anual de café de especialidad en una ciudad de 1.000.000 habitantes.

- **Vía A (top-down):** Informe gremial dice que el café de especialidad es el 5 % del consumo de café. Si el gasto en café de la ciudad es ~10.000.000 USD/año → especialidad ≈ **500.000 USD/año**.
- **Vía B (bottom-up por consumidor):** ~50.000 personas toman café de especialidad, gastan ~12 USD/mes → 50.000 × 12 × 12 = **7.200.000 USD/año**. (¡Muy distinto! Revisa supuestos: ¿son 50.000 o 5.000? ¿12 USD/mes es realista?)
- **Vía C (oferta):** Hay ~40 cafeterías de especialidad facturando ~150.000 USD/año cada una → **6.000.000 USD/año**.

B y C concuerdan (~6-7 M); A se quedó corta porque el "5 %" del informe era de otro país. **Conclusión honesta:** el mercado está en el rango **6-7 M USD/año**, no en 500 mil. Sin triangular, habrías usado la cifra equivocada. (Conecta con 20 para TAM/SAM/SOM y con 29 para evaluar si el sector vale la pena.)

## Cómo estimar cuando NO hay dato (sin inventar)

A veces no existe la cifra. Estimar honestamente es válido **si dejas ver tus supuestos**. Métodos:

1. **Fermi (de arriba hacia abajo):** descompón en factores que sí conoces. "Clientes/mes = población × % objetivo × % que compra × frecuencia". Cada factor con su fuente o supuesto explícito.
2. **Proxy / analogía:** usa un dato de un país o sector parecido y ajústalo (por población, por poder adquisitivo). Marca que es una aproximación.
3. **Rango, no punto:** di "entre 400 y 600 clientes/mes", no "500". Un rango honesto vale más que un número falso preciso.
4. **Etiqueta SIEMPRE:** marca cada cifra como `[dato: DANE 2023]`, `[estimación: Fermi, supuestos X]` o `[rango orientativo, verificar]`. El usuario debe saber qué es roca y qué es arena.

## Checklist de calidad de un dato

- [ ] ¿Tiene fuente con nombre y año? (un dato sin fuente no existe)
- [ ] ¿Es del país/ciudad correctos, o lo estoy importando de otro lado?
- [ ] ¿Está actualizado? (datos de hace 6+ años pueden estar obsoletos)
- [ ] ¿Lo confirmé con una segunda fuente (triangulación)?
- [ ] Si es estimación, ¿dejé visibles los supuestos y di un rango?

## Errores comunes

- **Citar de memoria.** "El mercado es de 500 millones" sin fuente = inventado. Búscalo o etiquétalo como estimación.
- **Importar cifras de otro país** sin ajustar (un % de consumo de EE. UU. no aplica a Bolivia).
- **Confundir interés con ventas.** Google Trends sube ≠ la gente compra. Es señal, no demanda confirmada.
- **Falsa precisión.** "47.382 clientes" cuando estimaste a ojo. Redondea y da rango.
- **Una sola fuente.** Sin triangular, un error de la fuente se vuelve tu error.
- **Olvidar el país.** Dar datos legales, fiscales o de costos sin preguntar país/ciudad primero (ver módulos legales).

## Siguiente paso típico

Define país y ciudad, abre la oficina de estadística nacional y un marketplace, saca 2-3 cifras para triangular, y etiqueta cada una con fuente o supuesto. Con eso ya puedes calcular tu mercado con rigor en el módulo 20 y convertirlo en decisión de entrar o no en el 29.
