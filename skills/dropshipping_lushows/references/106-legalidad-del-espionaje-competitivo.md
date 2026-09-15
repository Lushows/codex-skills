# Legalidad del espionaje competitivo

> Vigencia: 14-sep-2026. No es asesoría legal. Es la línea operativa de un negocio que quiere durar.
> Para un caso concreto, abogado.

## Por qué la Biblioteca de Anuncios es pública

No es una filtración ni un agujero. Meta publica todos los anuncios **por obligación de
transparencia**: nació de la presión regulatoria sobre publicidad electoral (elecciones de 2016-2018)
y se extendió a toda la publicidad comercial. La Unión Europea lo refuerza con el Reglamento de
Servicios Digitales, que obliga a las plataformas grandes a mantener repositorios públicos de
anuncios.

Consecuencia directa: **mirar la biblioteca es exactamente el uso previsto de la herramienta.** No
estás burlando nada. No hay "hackeo", no hay acceso no autorizado, no hay violación de términos.

Lo mismo aplica a:

| Recurso | Por qué es legítimo consultarlo |
|---|---|
| Biblioteca de Anuncios de Meta | Publicada por obligación de transparencia |
| TikTok Creative Center | Publicado por TikTok como herramienta de marketing |
| Landing pages públicas | Están en internet abierto, sin contraseña |
| `/products.json` y sitemaps de Shopify | Rutas públicas diseñadas para buscadores y apps |
| Reseñas y comentarios públicos | Publicados por sus autores en abierto |
| Precios públicos en marketplaces | Publicados para el consumidor |

## El semáforo

| 🟢 Legítimo | 🟡 Cuidado | 🔴 Nunca |
|---|---|---|
| Consultar bibliotecas de anuncios | Scraping de volumen alto a un sitio ajeno | Acceder a paneles o cuentas ajenas |
| Navegar tiendas públicas | Descargar videos ajenos para "estudio" | Usar credenciales que no son tuyas |
| Leer `/products.json` una vez | Crear cuentas falsas para acceder a contenido | Suplantar identidad para sacar información |
| Comprar como cliente (compra-espía) | Simular ser proveedor o socio | Sobornar a un empleado del competidor |
| Leer comentarios públicos | Guardar datos personales de comentaristas | Armar base de datos con esos contactos |
| Analizar estructura y ángulo | Parafrasear muy cerca del original | Copiar creativos, fotos o textos |
| Comparar precios | | Usar la marca ajena en tus anuncios |
| Documentar todo en tu archivo | | Publicidad engañosa comparativa |

## Los cuatro cuerpos legales que importan

### 1. Derecho de autor
Protege la **expresión**: el video, la foto, el texto, la música. No protege la idea ni el ángulo.
En México, Ley Federal del Derecho de Autor; en Colombia, Ley 23 de 1982 y decisiones andinas; en
EE.UU., Copyright Act. La regla es la misma en todos: no copies la obra. Ver `105`.

### 2. Derecho marcario
Protege el **nombre, logo y signos distintivos**. No uses la marca del competidor en tus anuncios,
tu dominio, tus etiquetas ni tus palabras clave de forma que confunda. En México, IMPI.

### 3. Competencia desleal
Prohíbe actos que induzcan a confusión, denigren al competidor o exploten su reputación. Ejemplos de
lo que cae aquí:

| Acto | Problema |
|---|---|
| Dominio casi idéntico al del competidor | Confusión |
| Decir "somos los originales" sin serlo | Engaño |
| Afirmar que el competidor estafa sin prueba | Denigración |
| Usar su marca como palabra clave con copy confuso | Aprovechamiento de reputación |

Comparar honestamente ("entregamos en 48 h desde México, no en 25 días") **sí** se puede, si es
verificable y no denigra.

### 4. Datos personales
Los comentarios son públicos, pero los **datos de las personas que comentan no son tuyos**. En
México aplica la LFPDPPP; en Colombia, la Ley 1581 de 2012; en la UE, el RGPD. Recolectar perfiles,
correos o teléfonos de comentaristas para contactarlos es tratamiento sin base legal. No lo hagas.
Ver `07`.

## Scraping: dónde está la frontera

| Práctica | Lectura |
|---|---|
| Abrir `/products.json` de 5 competidores una vez al mes | Sin problema |
| Script con pausa de 1-2 s que recorre esas 5 tiendas | Aceptable |
| Miles de peticiones por minuto a un sitio ajeno | Puede constituir abuso; te bloquean y puede haber responsabilidad |
| Saltarse bloqueos técnicos (CAPTCHA, rate limit, login) | 🔴 Cruzaste la línea |
| Ignorar `robots.txt` deliberadamente a escala | 🟡-🔴 Mala práctica, agrava cualquier reclamación |

Principio simple: **si tienes que burlar una protección, ya no estás mirando algo público.** Ver
`108`.

## Términos de servicio vs ley

Son cosas distintas. Violar los términos de servicio de Meta o Shopify no suele ser un delito, pero:

- Te pueden cerrar la cuenta sin previo aviso y sin devolverte nada.
- Con una operación de temporada (Buen Fin + diciembre) eso equivale a perder el año.

O sea: **el riesgo de plataforma es más inmediato y más caro que el riesgo legal.** Gestiónalo con la
misma seriedad.

## Qué hacer si TE copian a ti

| Paso | Acción |
|---|---|
| 1 | Documenta: capturas con fecha, ID del anuncio, URL |
| 2 | Verifica qué copiaron: ¿ángulo (nada que hacer) o creativo/texto (sí hay caso)? |
| 3 | Si es creativo/texto: reporta por el formulario de derechos de autor de la plataforma |
| 4 | Si es marca: reclamación marcaria en la plataforma y, si escala, ante la autoridad (IMPI en MX) |
| 5 | No respondas atacándolo en público. No sube ventas y te expone a denigración |
| 6 | Acelera tu rotación de creativos: el que copia siempre va detrás |

Que te copien el ángulo es señal de que funciona. Que te copien el video es reportable. Distingue.

## Relacionados
`105` qué copiar y qué nunca · `07` ética y reputación · `81` la biblioteca · `92` espiar tiendas · `108` automatizar · `95` comentarios
