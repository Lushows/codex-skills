# 168 — Gestión de capacidad y demanda

Cómo hacer que tu capacidad (mesas, sillas, horas, máquinas, stock, gente) y tu demanda (clientes que llegan) coincidan en el tiempo. El objetivo: no perder ventas por estar lleno ni pagar capacidad ociosa por estar vacío. Es de los problemas que más plata silenciosa cuesta y casi nadie mide.

## El problema en una frase
La demanda casi nunca es plana: llega en **picos** (sábado 8pm, diciembre, lunes a la hora del almuerzo) y **valles** (martes 3pm, enero). La capacidad, en cambio, suele ser fija (pagas el arriendo y la nómina llegue o no llegue gente). Cuando demanda > capacidad → **pierdes ventas** y quemas reputación. Cuando capacidad > demanda → **pagas por aire** (ociosidad). Gestionar esto = ganar dinero sin vender más caro ni gastar más.

## Términos en cristiano
- **Capacidad**: cuánto puedes atender/producir por unidad de tiempo sin reventar la calidad (ej. 40 cubiertos/hora, 8 cortes de pelo/día, 200 pedidos/día).
- **Cuello de botella**: el recurso MÁS lento de tu cadena; él fija tu capacidad real, no el más rápido (ver 161 sobre cuello de botella).
- **Utilización**: % de capacidad que sí usas. 100% suena ideal pero genera colas eternas; lo sano suele ser 70–85%.
- **Demanda perdida (balking/lost sales)**: el cliente que se fue porque estaba lleno o la espera era larga. NO aparece en tus ventas → invisible si no la cuentas.
- **Tarifa dinámica**: cambiar el precio según qué tan llena está tu capacidad (más caro en pico, más barato en valle).

## Marco práctico: el ciclo de 4 pasos
1. **Mide tu capacidad real** (la del cuello de botella, no la teórica).
2. **Mide la demanda real por franja** (hora del día, día de la semana, mes). Incluye la demanda perdida.
3. **Decide la palanca**: ¿muevo la demanda hacia los valles, o muevo la capacidad hacia los picos? (casi siempre las dos).
4. **Ajusta y vuelve a medir.** Esto es continuo, no un proyecto de una vez.

## Cómo medir la capacidad real (el cuello de botella manda)
Lista los pasos de tu operación y mira cuál es el más lento por hora.

> **Ejemplo (cifras ilustrativas).** Un restaurante: cocina produce 50 platos/hora, hay 12 mesas que rotan cada 75 min (≈ 4 personas × 12 mesas / 1,25 h ≈ 38 cubiertos/hora), y 1 cajero cobra 30 cuentas/hora.
> El cuello de botella son **las mesas: ~38 cubiertos/hora**. Comprar otra estufa NO sube tus ventas; poner 3 mesas más, sí. Atacar el recurso equivocado es el error #1 (ver 161 sobre cuello de botella).

## Cómo medir la demanda perdida (la venta invisible)
Lo que no se cuenta, no se gestiona. Formas baratas de capturarla:
- Una rayita en un papel cada vez que alguien se va por la fila / cuelga / pregunta y no compra por falta de cupo.
- En digital: "agotado", "sin cupo", clics en horarios no disponibles, carritos abandonados por stock 0.
- Lista de espera: cuánta gente quiso y no pudo.

| Franja | Capacidad | Demanda real | Ventas | Perdida |
|---|---|---|---|---|
| Sáb 8–10pm | 76 cub. | 110 | 76 | **34** |
| Mar 3–5pm | 76 cub. | 18 | 18 | 0 (sobra 58) |

*(Cifras ilustrativas.)* Aquí ves el doble problema: pierdes 34 el sábado y desperdicias 58 el martes. Casi siempre **no necesitas más capacidad total**: necesitas mover demanda del pico al valle.

## Palanca A — Mover la demanda (aplanar la curva)
Más barato que crecer capacidad. Tácticas:
- **Tarifa dinámica / precios por franja**: descuento en valle (happy hour 3–6pm), recargo o precio premium en pico. Aerolíneas, hoteles y Uber viven de esto.
- **Reservas y citas**: convierten una demanda caótica en una agenda predecible. Reducen ociosidad y colas a la vez.
- **Depósito / seña anti-no-show**: el cliente que no paga nada no respeta la reserva. Un depósito reembolsable baja los plantones (ver más abajo).
- **Promos solo en valle** (martes 2x1, combo de almuerzo entre semana).
- **Pre-orden / lista de espera** para correr demanda a otro momento sin perderla.

## Palanca B — Flexibilizar la capacidad (subir en pico, bajar en valle)
- **Personal por turnos / part-time / on-call** para cubrir solo las horas pico (cuida la ley laboral del país — ver 103).
- **Capacidad bajo demanda**: alquilar en vez de comprar, tercerizar el exceso, nube en vez de servidor propio.
- **Cross-training**: un empleado que hace varias tareas cubre el cuello que esté apretado ese día.
- **Buffer de inventario** para negocios de producto (acumulas en valle para vender en pico) — solo si el producto no se vence (ver 142 sobre inventario, 143 sobre capital de trabajo).
- **Reservar capacidad para lo rentable**: en pico, prioriza al cliente/producto de mayor margen.

## Tarifa dinámica: cómo arrancar sin sobrecomplicar
No necesitas un algoritmo. Empieza con **3 niveles**:
1. Define franjas (Valle / Normal / Pico) según tus datos de demanda.
2. Pon un precio por nivel. Regla simple: que el **pico subsidie al valle**.
3. Comunícalo como beneficio ("precio especial entre semana"), no como castigo.

> **Ejemplo (ilustrativo).** Peluquería, corte base $30.000. Lun–jue 9am–4pm (valle): $24.000. Vie–sáb (pico): $36.000.
> Si eso mueve 10 cortes/semana del sábado lleno al martes vacío, llenas horas que valían $0 y liberas cupo de sábado para venderlo otra vez. Ganancia neta sin contratar a nadie.

## Reservas y no-shows: el cálculo que casi nadie hace
Un cupo reservado que no llega es **doble pérdida**: no cobras a quien faltó Y rechazaste a alguien que sí habría venido.

> **Ejemplo (ilustrativo).** 20 reservas/noche, 15% de no-show = 3 mesas vacías que rechazaron a 3 clientes. A $80.000 de ticket promedio = **$240.000/noche perdidos**, ~$6,2M/mes.
> Soluciones: depósito reembolsable, recordatorio por WhatsApp 24h y 3h antes, o **overbooking controlado** (acepta 22 reservas sabiendo que ~3 faltan). Ojo: overbooking mal calibrado = clientes furiosos; empieza conservador y mide.

## KPIs de capacidad y demanda
- **% utilización** por franja (usado / disponible). Meta sana: 70–85% sostenido.
- **Tasa de demanda perdida** (perdidos / (ventas + perdidos)).
- **Tasa de no-show** y % de reservas con depósito.
- **Ingreso por unidad de capacidad** (ej. ingreso por mesa-hora, por silla, por m², RevPAR en hotelería).
- **Ratio pico/valle** (demanda del pico ÷ demanda del valle): qué tan desbalanceada está tu curva.

## Errores comunes
- **Atacar el recurso equivocado** (gastar en lo que no es el cuello de botella).
- **No contar la demanda perdida** → crees que vendes bien cuando dejas plata en la mesa.
- **Buscar 100% de utilización** → colas, mala experiencia, equipo quemado. Deja holgura.
- **Bajar precios en el pico** (cuando ya estás lleno) o subirlos en el valle: justo al revés.
- **Tratar el no-show como inevitable** en vez de gestionarlo con depósito/recordatorio.
- **Crecer capacidad fija (arriendo, nómina) para cubrir un pico que dura 4 horas/semana** → ociosidad cara el resto del tiempo.

## Cómo arrancar mínimo viable (esta semana)
1. Una semana contando, en papel, demanda y demanda perdida por franja.
2. Identifica tu cuello de botella real.
3. Define 3 franjas (valle/normal/pico) y una sola acción para cada una (ej. promo en valle, recargo o reserva en pico).
4. Mide otra semana y compara.

## Siguiente paso típico
Cuenta UNA semana tu demanda perdida por franja y encuentra tu cuello de botella (ver 161 sobre cuello de botella). Con eso, elige la palanca más barata: casi siempre mover demanda del pico al valle con una promo o una reserva, antes que pagar más capacidad fija. Luego revísalo contra tu punto de equilibrio por franja (ver 53).
