# Lanzar la tienda: lista de verificación

> Vigencia: 14-sep-2026. Recórrela completa **antes de gastar el primer peso en anuncios**. Si algo
> falla, no enciendas: cada día de pauta sobre una tienda rota es dinero quemado y datos envenenados.

## A. Dominio, correo y marca (5)

1. [ ] Dominio propio comprado, de **marca** y no de producto. `179`
2. [ ] HTTPS activo y el candado se ve en móvil.
3. [ ] Buzón `hola@tudominio.com` creado y funcionando.
4. [ ] **SPF, DKIM y DMARC** configurados en el DNS. `179`
5. [ ] Nombre y logo (aunque sea el nombre en texto) consistentes en la tienda.

## B. Producto y oferta (6)

6. [ ] La página de producto tiene las 13 secciones en orden. `180`
7. [ ] El encabezado tiene los 7 elementos obligatorios. `181`
8. [ ] El texto está escrito desde el dolor, no desde las características. `183`, `184`
9. [ ] El **bundle** existe, está preseleccionado y cruza el umbral de MSI (1.099 MXN). `195`
10. [ ] Inventario real cargado, con el número correcto de unidades.
11. [ ] La tabla comparativa contra la alternativa está y es honesta. `180`

## C. Imágenes y video (5)

12. [ ] La primera foto muestra el producto **en uso**, sin fondo blanco, sin marca de agua. `182`
13. [ ] 8 imágenes en la secuencia argumental, todas con la misma proporción. `182`
14. [ ] Ninguna imagen pesa más de 200 KB.
15. [ ] Video de demostración con **toma continua** del uso completo, subtitulado, sin autoplay con
    sonido. `186`
16. [ ] La foto del contenido de la caja coincide exactamente con lo que incluye el bundle.

## D. Confianza (6)

17. [ ] Reseñas reales publicadas, con foto, nombre y ciudad. Ninguna inventada. `185`
18. [ ] FAQ con 8-12 preguntas reales, la primera abierta. `187`
19. [ ] Garantía escrita con **plazo, procedimiento y plazo de reembolso**. `188`
20. [ ] Pie con razón social, domicilio, correo del dominio y WhatsApp con horario. `197`
21. [ ] Tira de confianza bajo el botón, con cuatro elementos verdaderos. `197`
22. [ ] Ningún contador falso, ninguna escasez inventada, ningún precio tachado irreal. `189`

## E. Pagos (6)

23. [ ] Pasarela dada de alta y **aprobada**, no en trámite. `192`
24. [ ] Métodos activos: crédito, débito, OXXO/efectivo, SPEI/transferencia. `192`
25. [ ] **MSI activos**, con el mínimo por debajo de tu bundle. `195`
26. [ ] La mensualidad de MSI aparece **junto al precio en la página de producto**, no solo al pagar.
27. [ ] Moneda de cobro = moneda local (MXN). `206`
28. [ ] Segunda pasarela dada de alta y probada, como respaldo. `192`

## F. Envíos (4)

29. [ ] Zonas y tarifas configuradas, con plazos **reales más colchón**. `178`
30. [ ] El plazo de entrega se ve en el encabezado, no solo en el checkout. ~18% abandona por
    entrega lenta (Baymard). `181`
31. [ ] Si hay envío gratis, el umbral está claro y es coherente en toda la página.
32. [ ] Confirmaste los plazos con la transportadora, por escrito. `205`

## G. Checkout (6)

33. [ ] Compra como **invitado**, sin obligar a crear cuenta. `190`
34. [ ] Campos mínimos; ningún campo de empresa ni de RFC en el flujo principal. `190`
35. [ ] El total no cambia entre la página y el pago.
36. [ ] Garantía y plazo de entrega repetidos junto al botón de pago.
37. [ ] Sin menú, sin pop-ups, sin campo de cupón grande. `190`
38. [ ] El botón dice el monto: `Pagar $1,099`.

## H. Legal (5)

39. [ ] Los cinco documentos publicados, completos, sin marcadores sin llenar. `207`
40. [ ] Enlazados desde el pie en todas las páginas, incluido el checkout.
41. [ ] La política de devoluciones **coincide** con lo que promete la página y la FAQ.
42. [ ] Aviso de privacidad accesible desde donde se recogen datos.
43. [ ] Si vendes en la UE: banner de cookies con rechazo tan fácil como aceptar. `194`

## I. Medición (5)

44. [ ] Un solo píxel instalado, vía integración oficial. `200`
45. [ ] **API de conversiones activa y deduplicada.** `200`
46. [ ] Los cinco eventos disparan una sola vez cada uno. `201`
47. [ ] `Purchase` con valor, moneda y `order_id` correctos.
48. [ ] GA4 instalado y la hoja diaria de gasto/pedidos/CAC creada. `199`

## J. Velocidad y móvil (4)

49. [ ] Probaste la página en **tu celular con datos móviles**, no wifi. `196`
50. [ ] El botón de compra se ve sin bajar.
51. [ ] Nada salta mientras carga.
52. [ ] Menos de 6 apps instaladas; ninguna sin justificación de venta. `196`

## K. La prueba final (5)

53. [ ] **Compra real** con tarjeta propia, desde el celular, de punta a punta. `190`
54. [ ] Cronometraste el checkout: menos de 90 segundos.
55. [ ] Llegó el correo de confirmación y **no** cayó en spam.
56. [ ] El evento de compra apareció completo y se concilia con el pedido del panel. `201`
57. [ ] Hiciste el reembolso y funcionó.

## L. Recuperación y post-venta (3)

58. [ ] Secuencia de carrito abandonado de 3 correos activa, con descuento solo en el tercero. `198`
59. [ ] Correos transaccionales configurados: confirmación, enviado, entregado. `190`
60. [ ] Correo de solicitud de reseña a los 7 días de entregado. `185`

---

## Las 8 que no puedes saltarte bajo ninguna circunstancia

Si tienes que lanzar mañana y solo alcanzas a verificar ocho:

| # | Punto |
|---|---|
| 53 | Compra real de punta a punta |
| 25 | MSI activos (México) |
| 45 | API de conversiones deduplicada |
| 30 | Plazo de entrega visible en el encabezado |
| 39 | Documentos legales completos |
| 19 | Garantía escrita con procedimiento |
| 50 | Botón visible sin bajar en móvil |
| 4 | SPF/DKIM/DMARC del correo |

## Después de encender

| Cuándo | Qué revisar |
|---|---|
| Primera hora | Que entren sesiones y que los eventos disparen |
| Primeras 24 h | Que no haya errores de checkout; revisa 10 grabaciones de sesión |
| Primeras 300 sesiones | Si hay 0 ventas, ve directo a `204` |
| Primera semana | Embudo completo, CAC, utilidad por sesión. `199` |

## Relacionados
`178` montar en un día · `190` checkout · `201` eventos · `204` diagnóstico · `209` errores que matan ventas
