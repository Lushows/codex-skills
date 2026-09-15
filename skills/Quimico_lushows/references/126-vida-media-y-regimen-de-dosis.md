# 126 — Vida media y régimen de dosis (por qué "una vez al día" puede ser una decisión equivocada)

La vida media es el parámetro que decide cada cuánto hay que tomar algo y cuánto tarda en estabilizarse la
concentración en el cuerpo. Este módulo te enseña a usarla para diseñar un régimen de dosis con criterio, y
a detectar cuándo la frecuencia de una etiqueta se eligió por conveniencia comercial y no por
farmacocinética. El error caro que evita: prometer efecto sostenido con una molécula que se elimina en dos
horas, o acumular una sustancia sin saberlo hasta llegar a concentraciones no ensayadas.

Términos: **vida media de eliminación (elimination half-life, t½)** = tiempo en que la concentración
plasmática cae a la mitad. **Estado estacionario (steady state)** = cuando lo que entra iguala a lo que
sale y la concentración media se estabiliza. **Factor de acumulación (accumulation ratio, Rac)** = cuánto
sube la concentración con dosis repetidas frente a la primera dosis. **Fluctuación (fluctuation)** = qué
tanto sube y baja entre dosis.

## Las cuentas que gobiernan todo

```
ke  = 0,693 / t½                       constante de eliminación (1/h)
t½  = 0,693 · Vd / CL                  vida media a partir de Vd y aclaramiento

Tiempo hasta estado estacionario ≈ 4–5 · t½      (independiente de la dosis)
Tras suspender, se elimina ~97 % en 5 · t½

              1
Rac  =  ─────────────────         τ = intervalo entre dosis
         1 - e^(-ke · τ)
```

Regla mental verificable: si τ = t½, Rac ≈ 2. Si τ = 2·t½, Rac ≈ 1,33. Si τ << t½, la acumulación es
grande. **Ejecuta siempre estas cuentas en código** (`Matematicas_lushows`), no de memoria.

Tabla de referencia rápida de eliminación tras suspender:

| Vidas medias transcurridas | Fracción que queda |
|---|---|
| 1 | 50 % |
| 2 | 25 % |
| 3 | 12,5 % |
| 4 | 6,25 % |
| 5 | 3,1 % |
| 7 | 0,8 % |

## Cómo se elige el intervalo

Tres criterios, en orden de importancia:

1. **Ventana terapéutica.** Si es estrecha, hay que dosificar más seguido para que Cmax no se pase y Cmin
   no se quede corto. Si es ancha, se puede espaciar.
2. **Relación efecto-concentración.** Algunas moléculas dependen del pico (Cmax); otras de la exposición
   total (AUC); otras del tiempo por encima de un umbral. Cada patrón pide un régimen distinto.
3. **Adherencia real.** Un régimen de 4 veces al día tiene adherencia peor que uno de 1 vez al día. Un
   producto perfectamente diseñado que nadie toma bien no sirve. Esa parte se conversa con `ventas_lushows`.

## La trampa de la t½ terminal

Ya se mencionó en `121` y merece su propio párrafo porque cuesta dinero: en modelos de dos compartimentos,
**la t½ terminal larga no significa efecto largo**. Los cannabinoides son el ejemplo canónico: la t½
terminal es prolongada porque salen lentamente del tejido graso, pero el efecto psicoactivo agudo del THC
inhalado dura pocas horas `[clínico]`. Confundir ambas cosas lleva a promesas de "efecto de 24 horas" que
no resisten un contraste.

Al revés también pasa: la psilocibina se convierte en psilocina, cuya t½ es de pocas horas, y aun así los
efectos subjetivos reportados en investigación clínica duran más de lo que la curva plasmática sugiere
`[clínico fase 2]` (ver `258`). Farmacocinética y farmacodinamia no siempre van de la mano — eso se llama
histéresis y hay que nombrarlo, no esconderlo.

## Dosis de carga: cuándo tiene sentido

Si t½ es larga y quieres llegar rápido al estado estacionario, se usa dosis de carga:

```
Dosis de carga  =  Cobjetivo · Vd / F
```

En suplementos naturales esto casi nunca está justificado, porque no hay una Cobjetivo definida. Cuando un
producto habla de "fase de carga" sin tener PK, generalmente es una estrategia para vender más unidades el
primer mes. Dilo así.

## Cómo se mide

| Parámetro | Cómo se obtiene | Requisito |
|---|---|---|
| t½ | Pendiente de la fase terminal en escala semilogarítmica del perfil plasmático | Al menos 3 puntos en la fase terminal y seguimiento ≥ 3 t½ |
| CL, Vd | De la curva IV; o CL/F y Vd/F si solo hay oral | Método bioanalítico validado |
| Estado estacionario | Cmin en días consecutivos hasta que no cambia | Dosis múltiple, 5+ días |
| Rac | AUC en estado estacionario / AUC de dosis única | Estudio de dosis múltiple |

Sin método bioanalítico validado (`75`) ninguno de estos números vale nada.

## Ejemplo aplicado — régimen de un extracto de hongo

Para hongos funcionales no hay t½ publicada del "extracto" porque el extracto no es una molécula. Lo
honesto es reconocerlo y razonar así:

1. Elegir un **marcador medible**. Para reishi podría ser un triterpeno específico (`224`); para cordyceps,
   cordicepina (`228`). Solo entonces existe un t½ que tenga sentido.
2. Si no vas a hacer PK propia, **replicar el régimen del estudio clínico que citas**. Si el estudio usó
   1,5 g dos veces al día, tu producto debe permitir eso, no "1 cápsula al día" porque cabe mejor en el
   frasco **(ILUSTRATIVO)**.
3. Decir con todas las letras: "régimen alineado con el usado en el estudio X", con su nivel de evidencia,
   y no "régimen optimizado", que sería una afirmación sin datos.

Cálculo ilustrativo de acumulación, suponiendo un marcador con t½ = 8 h y dosis cada 12 h:

```
ke  = 0,693 / 8 = 0,0866 1/h
Rac = 1 / (1 - e^(-0,0866 × 12)) = 1 / (1 - 0,354) = 1,55
```

Es decir, en estado estacionario la exposición sería ~1,55 veces la de la primera dosis **(ILUSTRATIVO,
verificar con `Matematicas_lushows`)**.

## Errores comunes

- Elegir "1 vez al día" por marketing cuando la t½ del marcador exige dos tomas.
- Usar la t½ terminal de un compuesto lipofílico para prometer duración de efecto.
- Hablar de t½ de un "extracto". Los extractos no tienen t½; las moléculas sí.
- Inventar una "fase de carga" sin concentración objetivo ni PK que la respalde.
- Olvidar que el estado estacionario tarda 4–5 t½: evaluar el producto a los 3 días puede ser prematuro.
- No advertir sobre acumulación cuando el intervalo es mucho menor que la vida media.

## Conexión con otros módulos

→ `121-farmacocinetica-adme.md` — de dónde salen CL, Vd y t½.
→ `119-farmacodinamia-y-dosis-respuesta.md` — la otra mitad de la decisión de dosis.
→ `161-dosis-y-tamano-de-porcion.md` — cómo se traduce a la etiqueta.
→ `249-dosificacion-de-hongos-funcionales.md` — el caso concreto de hongos.
→ `258-farmacocinetica-de-psilocibina.md` — un caso donde PK y PD no coinciden.