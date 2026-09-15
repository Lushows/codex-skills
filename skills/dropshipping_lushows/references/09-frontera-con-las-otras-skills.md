# Frontera con las otras skills

## Por qué esto importa

Las skills de Lushows se rutean, no se duplican. Cuando dos skills cubren el mismo tema con criterios
distintos, el resultado es peor que si solo existiera una: Claude improvisa una mezcla. Este módulo
define quién manda en cada frontera.

## El mapa completo

| Tema | Skill dueña | Qué aporta `dropshipping_lushows` |
|---|---|---|
| Mecánica de Meta: pujas, píxel, CAPI, estructura, cuentas baneadas | `facebook_ads_lushows` | **Qué** anunciar; cómo leer la biblioteca para hallar producto |
| TikTok Ads, Spark Ads, TikTok Shop | `tiktok_ads_lushows` | Qué producto y qué ángulo llevar ahí |
| Google Ads, Shopping, búsqueda, SEO de pago | `google_ads_lushows` | Qué producto tiene demanda de búsqueda |
| Vender de humano a humano, cerrar por chat, objeciones en vivo | `ventas_lushows` | Vender **sin humano**: página, oferta, bundle |
| Viabilidad del negocio, formalizar, TAM, levantar capital | `economist_lushows` | Viabilidad de **este producto, esta semana** |
| Diseño visual de la página, animación, UI, componentes | `desingweb-lushows` | Qué debe **decir** la página para convertir |
| Logo, identidad, empaque, fotografía de producto | `directorcreativo_lushows` | El **producto**, no la marca |
| Editar el video: cortes, subtítulos, color, ffmpeg | `editpro_lushows` | El **guion** y el ángulo del anuncio |
| Cálculos que deben ser exactos | `Matematicas_lushows` | El modelo; los números se verifican allá |
| Impuestos, libros, facturar, declarar | `contador_lushows` | Qué impuesto dispara cada modelo logístico |
| Prospección B2B, correo en frío, agendar reuniones | `SDR_OUTBOUND_LUSHOW` | Nada: esto es B2C |
| Reducir costo de tokens de un bot | `optimizer_tokens_lushows` | Nada |

## Las cuatro fronteras que más se confunden

### 1. Contra las skills de anuncios

**La pregunta que decide:** *"¿La duda es sobre QUÉ vender o sobre CÓMO comprar el clic?"*

| Es de dropshipping | Es de la skill de ads |
|---|---|
| "¿Qué producto testeo?" | "¿Cómo estructuro la campaña?" |
| "¿Qué ángulo uso?" | "¿CBO o ABO?" |
| "¿Cómo encuentro ganadores en la biblioteca?" | "¿Por qué no sale del aprendizaje?" |
| "¿Cuál es mi ROAS de equilibrio?" | "¿Por qué subió mi CPM?" |
| "Este creativo, ¿qué dolor ataca?" | "Me bloquearon la cuenta" |

**Caso mixto frecuente:** "mi campaña no vende". Empieza aquí (`267`) para descartar que el problema
sea producto, oferta o página —que es lo más común— y **entonces** invoca la skill de ads.

### 2. Contra `economist_lushows`

Economist responde **¿debo montar este negocio?**. Dropshipping responde **¿debo vender este
producto?**. Economist piensa en trimestres y en estructura; dropshipping piensa en semanas y en
unidades.

Si el usuario pregunta "¿me conviene dedicarme al dropshipping?", eso es de economist con apoyo de
esta skill para los números del modelo.

### 3. Contra `desingweb-lushows`

Desingweb es dueña de **cómo se ve**. Esta skill es dueña de **qué dice y en qué orden**.

En la práctica: esta skill entrega la estructura y los textos de la página de producto (`180`-`189`);
desingweb la convierte en una página que se ve cara. Cuando el usuario pide "hazme la página", se
usan las dos: primero el contenido, después la forma.

### 4. Contra `ventas_lushows`

Ventas es dueña de la conversación. Esta skill es dueña de la conversión sin conversación.

El punto de contacto real es la **atención al cliente** y la **confirmación de pedidos**: ahí sí se
vende hablando, y ahí `ventas_lushows` aporta el manejo de objeciones. Ver `277`, `160`.

## Reglas de ruteo

1. **Nunca dupliques el contenido de otra skill.** Si necesitas su conocimiento, invócala.
2. **Cuando la pregunta cruce la frontera a la mitad, dilo.** "La parte del producto la resuelvo yo;
   para la estructura de campaña voy a cargar `facebook_ads_lushows`."
3. **Los números siempre se pueden verificar en `Matematicas_lushows`.** Esta skill trae los modelos;
   si el usuario necesita certeza absoluta sobre una cifra, esa es la ruta.
4. **Si dos skills se contradicen, gana la dueña del tema.** Y hay que corregir el módulo de la que
   se salió de su carril.

## Lo que esta skill NO debe crecer hacia

Para que la frontera se mantenga limpia con el tiempo, estos temas **no** se documentan aquí aunque
parezcan relacionados:

- Configuración detallada de campañas en cualquier plataforma
- Teoría de diseño, tipografía o color
- Contabilidad, declaración de impuestos, nómina
- Técnicas de edición de video
- Construcción de marca a largo plazo
- Venta consultiva o B2B

## Relacionados
`01` cómo usar esta skill · `267` diagnosticar campaña que no vende · `180` estructura de página · `228` modelo financiero
