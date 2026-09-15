# 44 — Tipografía de marca (corporativa)

La tipografía de marca es la fuente (o sistema de fuentes) que una empresa usa SIEMPRE, en todo: web, empaque, anuncios, app, facturas. Es uno de los activos de identidad más potentes y más subestimados.

## Por qué importa tanto
- **Reconocimiento sin logo**: puedes tapar el logo de Apple y aún reconocer su comunicación por San Francisco. La fuente es marca.
- **Consistencia**: una sola fuente bien definida hace que 100 piezas hechas por 10 personas se vean de la misma empresa.
- **Tono de voz visual**: la fuente comunica personalidad antes que cualquier palabra (ver 41).
- **Diferenciación**: en un mercado donde todos usan Montserrat, una tipografía propia te separa al instante.

## Los tres niveles de "fuente de marca"

### Nivel 1 — Fuente licenciada estándar (el 90% de los casos)
Eliges una fuente comercial existente y la adoptas como oficial. Suficiente y profesional para casi cualquier pyme.
- Ej: una marca elige **Söhne** para todo, o **GT America** + **GT Sectra**.
- Costo: licencia (ver 49). Implementación: inmediata.

### Nivel 2 — Fuente licenciada + ajustes / fuente exclusiva
Licencias una fuente y, a veces, pagas por exclusividad temporal o por una variante hecha a medida sobre una base existente. Más barato que una custom desde cero.

### Nivel 3 — Fuente custom (a medida)
Una fundidora diseña una tipografía única SOLO para la marca. Es el máximo nivel: identidad imposible de copiar + ahorro a largo plazo (no pagas licencias por usuario/dispositivo).

Casos famosos:
- **Apple → San Francisco (SF)**: diseñada para sus pantallas, legible en relojes y teléfonos.
- **Netflix → Netflix Sans**: dejaron de pagar licencias de Gotham; pagó la inversión sola.
- **Airbnb → Cereal**: cálida, redonda, internacional, propia.
- **Google → Product Sans + Google Sans**: coherencia en todo el ecosistema.
- **Spotify → Spotify Circular / Mix**: voz juvenil y geométrica.
- **IBM → Plex** (que además liberaron gratis).

## ¿Licenciar o encargar una custom? Tabla de decisión

| Situación | Recomendación |
|---|---|
| Pyme / startup / presupuesto limitado | Licenciar (o usar una gratis de calidad, ver 49) |
| Marca mediana, identidad importante | Licenciar una fundidora seria + sistema bien documentado |
| Empresa grande con MUCHOS usuarios/dispositivos | Evaluar custom: el ahorro en licencias puede pagarla |
| Necesidad técnica especial (pantallas, idiomas, legibilidad) | Custom o semi-custom |
| Quieres ser legalmente imposible de copiar | Custom |

## La matemática del ahorro (por qué Netflix lo hizo)
Las fuentes comerciales cobran por uso: por usuario web mensual, por app, por dispositivo. A escala de millones, esas licencias se vuelven enormes. Una custom tiene costo alto fijo (decenas de miles de USD) pero CERO regalías después. Si tu volumen es masivo, se paga sola. Si eres una pyme, NO tiene sentido: licencia una buena fuente o usa una gratis de élite.

## Cómo definir el sistema tipográfico de marca (entregable)
Un manual de marca (ver módulos de guidelines) debe especificar:
- [ ] **Fuente(s) primaria(s)** y sus pesos permitidos.
- [ ] **Fuente de respaldo / fallback** (qué se usa cuando la oficial no está, ej. en email: Arial/Georgia).
- [ ] **Jerarquía** (tamaños, pesos, colores por nivel — ver 43, 48).
- [ ] **Usos correctos e incorrectos** (no estirar, no usar otros pesos, no cambiar tracking sin razón).
- [ ] **Acentos en español garantizados** (ver 41).
- [ ] **Licencia y alcance** (web, app, desktop, impresión — ver 49).

## Fallback: el detalle que casi todos olvidan
La fuente de marca no carga en todos lados (un correo, un Office del cliente). Define SIEMPRE una segunda línea: "si no está Söhne, usar Arial". Para web se define en CSS como `font-family: 'Söhne', Helvetica, Arial, sans-serif;`. Esto evita que la marca se vea rota en sistemas ajenos.

## Errores comunes
- No documentar la fuente y terminar con cada diseñador usando una distinta.
- Comprar licencia desktop y usarla en web/app sin la licencia correcta (ver 49).
- Encargar una custom siendo una pyme (gasto injustificado).
- Olvidar el fallback y romper la marca en email/Office.

## Siguiente paso
Para una pyme: elige una fuente de élite (gratis o licenciada) en 49, documenta el sistema con la jerarquía de 43 y la escala de 48. Si la fuente vivirá sobre todo en pantalla, revisa 47. Para integrarla al logo, ver 46.
