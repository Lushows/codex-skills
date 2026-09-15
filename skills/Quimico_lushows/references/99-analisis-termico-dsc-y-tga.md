# 99 — Análisis térmico: DSC y TGA (qué le pasa a tu producto cuando sube la temperatura)

DSC y TGA responden preguntas que ninguna cromatografía contesta: ¿a qué temperatura se derrite mi aislado?
¿mi extracto es cristalino o amorfo? ¿cuánta agua y cuánto volátil pierde al calentarse, y a qué temperatura
empieza a descomponerse? Sirven para decidir temperaturas de secado, de encapsulado y de almacenamiento, para
detectar adulterantes que se derriten donde no deben, y para entender por qué un aislado de CBD se vuelve
melcocha en el clima de Bogotá o de Cartagena. Se hacen con miligramos y en menos de una hora.

Términos: **DSC (Differential Scanning Calorimetry)** = mide el flujo de calor de la muestra frente a una
referencia mientras sube la temperatura; ve fusiones, cristalizaciones y transiciones. **TGA
(Thermogravimetric Analysis)** = mide la **masa** mientras sube la temperatura; ve pérdida de agua,
volátiles y descomposición. **Tg (glass transition)** = temperatura a la que un sólido amorfo pasa de
vidrioso a gomoso. **Tm (melting point)** = temperatura de fusión. **endotérmico / exotérmico** = absorbe /
libera calor.

## Qué ve cada técnica

| Evento | DSC | TGA |
|---|---|---|
| Pérdida de agua o solvente | Endoterma ancha | **Escalón de masa** (lo cuantifica) |
| Fusión (Tm) | Endoterma aguda | No |
| Cristalización | Exoterma | No |
| **Transición vítrea (Tg)** | Escalón en la línea base | No |
| Descomposición | Exoterma o endoterma grande | **Pérdida de masa** irreversible |
| Ceniza / residuo inorgánico | No | Masa remanente a 600–800 °C |
| Polimorfos | Sí, Tm distintos | No |

Se corren juntas: TGA te dice **cuánto** se pierde y DSC te dice **qué tipo de evento** es.

## Para qué lo vas a usar de verdad

- **Tg de un extracto en polvo.** Los extractos de hongo y de planta secados por aspersión son sólidos
  amorfos, ricos en azúcares. Si la Tg está por debajo de la temperatura de bodega, el polvo se apelmaza y se
  vuelve caramelo. Subir la Tg es la razón por la que se usan portadores como maltodextrina de alto DE
  equivalente o goma arábiga (ver `150-secado-por-aspersion-y-liofilizacion.md`). La Tg **baja con la
  humedad**: agua = plastificante.
- **Punto de fusión y pureza aparente de un aislado.** Un cristal puro funde estrecho; una impureza baja y
  ensancha la fusión. DSC da una estimación de pureza por depresión del punto de fusión (van 't Hoff), útil
  como tamiz — no sustituye a qNMR ni a HPLC (ver `95`, `80`).
- **Temperatura máxima de proceso.** El TGA te dice a qué temperatura tu material empieza a perder masa por
  descomposición. Ese dato fija el techo del secado y de la descarboxilación.
- **Contenido de humedad y volátiles** como método complementario a Karl Fischer (ver `98`).
- **Ceniza total** por TGA en atmósfera de aire, comparable con el método gravimétrico de farmacopea.
- **Detección de adulterantes**: maltodextrina, lactosa o sacarosa añadidas dan eventos térmicos propios.

## Cómo se corre

```
TGA tipico:
  Masa de muestra   : 5-20 mg
  Atmosfera         : N2 (inerte) para descomposicion; aire para ceniza
  Rampa             : 10 C/min de 25 a 600 C (o 800 C si buscas ceniza)
  Se reporta        : % de masa perdida por escalon y temperatura de inicio (onset)

DSC tipico:
  Masa de muestra   : 2-10 mg en crisol de aluminio sellado o con perforacion
  Atmosfera         : N2, 50 mL/min
  Programa          : ciclo calentar-enfriar-calentar (el 2do calentamiento borra la historia termica)
  Se reporta        : Tg (punto medio), Tm (onset y pico), entalpia (J/g)
```

El **segundo calentamiento** es clave: el primero refleja cómo quedó el material después de fabricarlo; el
segundo refleja el material en sí. Ambos son informativos, pero hay que decir cuál se está reportando.

## Cómo se comprueba

- **Calibración con metales puros** de punto de fusión conocido: indio (156,6 °C), estaño (231,9 °C), zinc
  (419,5 °C). Se verifica temperatura y entalpía.
- **Crisol vacío como línea base** en cada serie.
- **Velocidad de rampa declarada.** Los eventos térmicos se corren con la velocidad; comparar 5 °C/min con
  20 °C/min no tiene sentido.
- **Atmósfera declarada.** En aire hay oxidación; en N₂ no. El mismo material da termogramas distintos.
- **Duplicados**, porque 5 mg de un polvo heterogéneo no representan un bulto (ver `66`, `67`).

## Ejemplo aplicado (ILUSTRATIVO)

Extracto de reishi secado por aspersión, con 20 % de maltodextrina como portador, lote GL-2608.

```
TGA (N2, 10 C/min)
  25-120 C   : -6,3 % de masa   -> agua y volatiles (concordante con KF: 6,2 %, ver 98)
  120-190 C  : estable          -> ventana segura de proceso
  onset 197 C: inicio de descomposicion  -> techo de secado muy por debajo de este valor
  residuo 600 C (aire): 2,1 %   -> ceniza total

DSC (2do calentamiento, N2)
  Tg = 48 C (punto medio)
  Sin endoterma de fusion  -> material amorfo, como se esperaba

Decision de negocio:
  Tg 48 C con humedad 6,2 %. En bodega sin clima en Barranquilla (32-36 C) el margen es de
  ~12-16 C y BAJA si el polvo gana humedad. Riesgo real de apelmazado.
  Acciones: bajar humedad objetivo a <= 4,5 %, envase con barrera y desecante (163),
  o subir el portador. Verificar con estudio de estabilidad (164).
```

(Cifras ilustrativas; hay que medirlas en tu lote.)

## Errores comunes

- **Reportar Tg sin decir humedad.** La Tg de un amorfo higroscópico depende del agua; sin humedad el dato
  no significa nada.
- **Usar el primer calentamiento** para caracterizar el material sin aclararlo.
- **Comparar termogramas con rampas o atmósferas distintas.**
- **Concluir pureza solo por DSC.** Es un tamiz; la pureza másica la da qNMR (`95`).
- **Crisol mal sellado** en muestras volátiles: se pierde señal y la entalpía sale baja.
- **Extrapolar del laboratorio a la planta.** 5 mg calientan distinto que 200 kg; el escalado térmico es otro
  problema (ver `166-escalado-de-lote.md`).

## Conexión con otros módulos

→ `98-karl-fischer-y-humedad.md` — el método específico para agua, que TGA no distingue de otros volátiles.
→ `18-estados-de-la-materia-y-transiciones.md` — la física detrás de Tg y Tm.
→ `150-secado-por-aspersion-y-liofilizacion.md` — donde la Tg decide el diseño del proceso.
→ `164-estabilidad-ich-q1-y-vida-util.md` — cómo se traduce todo esto a vida útil.
→ `174-descarboxilacion-cinetica-y-calculo.md` — la ventana térmica en cannabis.
→ `163-envase-primario-y-compatibilidad.md` — barrera de humedad y desecantes.