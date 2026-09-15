# Pasarelas en España y Europa

> Vigencia: 14-sep-2026. **Comisiones, umbrales y requisitos cambian: verificar antes de contratar.**
> IVA, IOSS y obligaciones fiscales: invoca `contador_lushows`. Régimen aduanero: `15`, `26`.

Europa es el mercado con la mejor conversión potencial de los que trata esta skill, y también el de
mayor carga regulatoria. La pasarela es la parte fácil; el IVA es la difícil.

## España: las cuatro opciones

| Pasarela | Fuerte en | Débil en |
|---|---|---|
| **Stripe** | La mejor integración técnica, SCA resuelto, multi-moneda, panel excelente | Sin marca frente al comprador final |
| **PayPal** | Confianza altísima en España, protección al comprador | Comisión alta, y su protección juega contra ti en disputas |
| **Redsys** (TPV bancario) | Es lo que el comprador español reconoce como "el banco" | Integración anticuada, alta vía banco, lenta |
| **Bizum** | Pago móvil masivo entre particulares y cada vez más en comercio | Cobertura en ecommerce todavía desigual |

### Qué debe tener un checkout español

| Método | Peso |
|---|---|
| Tarjeta (Visa/Mastercard) con SCA | Crítico |
| **PayPal** | Alto: mucha gente solo compra si está |
| **Bizum** | Medio-alto y subiendo |
| Pago aplazado (Klarna, SeQura) | Medio, sube ticket |
| Transferencia | Bajo |
| COD | Marginal. España es mercado prepago |

## Los tres impuestos que hay que entender antes de vender

### 1. IVA español: 21%
El tipo general en España es **21%**. En B2C se muestra **siempre el precio con IVA incluido**: es
obligación legal y además de conversión — un precio que sube en el checkout es la causa número uno
de abandono por costo inesperado. `190`.

Efecto en el modelo: de cada 100 € cobrados, ~17,36 € son IVA que no son tuyos. Si modelaste con
100 € de ingreso, tu margen real es 20% menor de lo que pensabas. Mete el IVA en el modelo **antes**
de fijar precio. `06`, y para la mecánica contable invoca `contador_lushows`.

### 2. IOSS (ventanilla única de importación)
Para envíos de fuera de la UE de bajo valor, el IOSS permite cobrar el IVA en la venta y que el
paquete entre sin que el cliente pague nada al recibir. Sin IOSS, el transportista le cobra al
cliente IVA más gastos de gestión en la puerta: eso genera rechazo del paquete y reseñas pésimas.

**El punto crítico:** un vendedor **no establecido en la UE** necesita un **intermediario
establecido en la UE** para usar el IOSS.

| Concepto | Rango | Nota |
|---|---|---|
| Alta con intermediario | **€99-400** una vez | Verificar con el proveedor |
| Cuota del intermediario | **€20-300 al mes** | Según volumen y proveedor |

Con capital menor a USD 500, esa cuota mensual puede ser la mitad del presupuesto de anuncios. Esto
es lo que hace que **Europa no sea el primer mercado para un operador que arranca desde LatAm sin
sociedad europea**. `15`, `26`.

### 3. Reforma aduanera de la UE
Los umbrales y el tratamiento de los envíos de bajo valor están en revisión. Cualquier modelo que
dependa de enviar desde China sin pagar IVA está construido sobre arena. `15`.

## SCA: la autenticación reforzada

En la UE, los pagos con tarjeta requieren autenticación reforzada (3-D Secure). Consecuencias
prácticas:

1. El cliente confirma con el banco. Eso **añade fricción y pierde ventas** si la pasarela lo hace
   mal.
2. Elige pasarela con buena implementación (Stripe destaca aquí).
3. Prueba el flujo completo con una tarjeta europea real antes de gastar en pauta.

## El resto de Europa: qué cambia

| País | Método que no puede faltar |
|---|---|
| Alemania | **Factura a 14 días** (Rechnungskauf) y adeudo SEPA. Sin factura, pierdes mucho mercado |
| Países Bajos | **iDEAL**. Es el método, no un método |
| Polonia | **BLIK** y Przelewy24 |
| Francia | Tarjeta (Carte Bancaire) y pago en cuotas |
| Italia | Tarjeta, PayPal, y COD todavía relevante |
| Portugal | **MB Way** y Multibanco |
| Reino Unido | Fuera de la UE: umbral propio. `19`, `27` |

Cada país tiene un método local sin el cual el checkout se siente extranjero. Y cada país tiene su
propio tipo de IVA: vender a toda la UE con un solo precio requiere el régimen OSS. Invoca
`contador_lushows`.

## Derecho de desistimiento: 14 días

En la UE, el consumidor puede devolver sin motivo en 14 días. No es una garantía que tú ofreces: es
un derecho que tienes que respetar, informar en la página, y ejecutar. Si tu política dice menos de
eso, estás incumpliendo.

Úsalo a tu favor: comunícalo como fortaleza en la página, y añade tu propia garantía por encima.
`188`, `207`.

## Veredicto honesto para un operador que arranca

| Situación | Veredicto |
|---|---|
| Capital bajo USD 500, sin sociedad en la UE, sin stock europeo | **No empieces por Europa.** El IOSS solo te come el presupuesto |
| Ya tienes sociedad o socio establecido en la UE | Europa es excelente: alta conversión, alto ticket |
| Stock en un almacén europeo | Las reglas de importación dejan de pesar; el negocio se vuelve local |
| Quieres probar Europa barato | Empieza por **un** país con proveedor local, no por "la UE" |

Para el proyecto de diciembre 2026 (México, capital bajo USD 500), **Europa queda fuera**. Se
reconsidera cuando México ya funcione y haya caja para el intermediario IOSS.

## Relacionados
`192` pasarelas México · `193` pasarelas LatAm · `15` reforma aduanera UE · `22` playbook España · `207` la tienda legal
