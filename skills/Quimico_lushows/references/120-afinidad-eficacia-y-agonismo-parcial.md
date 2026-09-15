# 120 — Afinidad, eficacia y agonismo parcial (por qué dos moléculas del mismo receptor no hacen lo mismo)

Este módulo resuelve una de las confusiones más costosas del oficio: creer que si dos moléculas se unen al
mismo receptor, hacen lo mismo. No. Una puede activarlo a fondo, otra a medias, otra bloquearlo, y otra
apagarlo por debajo de su nivel basal. Entender agonista pleno, parcial, antagonista, agonista inverso y
modulador alostérico es lo que te permite leer con criterio la farmacología del CBD, del THC y de la
psilocina, y detectar cuándo un dossier está inflando un dato de unión. El error caro: comprar un
ingrediente por su "afinidad al receptor X" sin saber si es agonista o si simplemente lo tapona.

Términos: **afinidad (affinity)** = qué tan fuerte se une el ligando, se cuantifica con Kd o Ki (nM; menor
= más fuerte). **Eficacia intrínseca (intrinsic efficacy)** = cuánto activa el receptor una vez unido.
**Agonista (agonist)** = se une y activa. **Antagonista (antagonist)** = se une y no activa; estorba al
agonista. **Agonista inverso (inverse agonist)** = reduce la actividad basal del receptor por debajo de
cero-estímulo. **Modulador alostérico (allosteric modulator)** = se une en otro sitio y cambia la respuesta
al ligando natural, sin activar por sí mismo.

## El espectro completo

```
Actividad del receptor
  100% ┤ ████ agonista pleno (full agonist)
   60% ┤ ███  agonista parcial (partial agonist)
   basal┤ ██   antagonista neutro (no cambia el basal)
    0% ┤ █    agonista inverso (inverse agonist)
```

| Tipo | Se une | Activa | Ejemplo relevante |
|---|---|---|---|
| Agonista pleno | Sí | 100 % del Emáx del sistema | Anandamida en algunos ensayos de CB1 |
| Agonista parcial | Sí | Fracción del Emáx | **Δ9-THC en CB1** — es agonista parcial, dato clave |
| Antagonista | Sí | No | Naloxona en receptores opioides |
| Agonista inverso | Sí | Baja el basal | Rimonabant en CB1 (retirado del mercado) |
| Modulador alostérico positivo (PAM) | En otro sitio | Amplifica al ligando natural | Benzodiacepinas en GABA-A |
| Modulador alostérico negativo (NAM) | En otro sitio | Atenúa | **CBD se ha descrito como NAM de CB1** `[in vitro]` |

Dos datos que aclaran discusiones enteras:

- **El THC es agonista parcial de CB1** `[in vitro]`, y ese es parte del motivo de que su perfil sea
  distinto al de los cannabinoides sintéticos, que son agonistas plenos y mucho más peligrosos (`205`).
- **La psilocina es agonista de 5-HT2A**, y su perfil de agonismo (incluyendo el sesgo hacia rutas
  específicas) es materia de investigación activa `[in vitro]` / `[clínico fase 2]` (ver `128`, `257`).

## Agonista parcial: agonista y antagonista a la vez

Lo contraintuitivo y muy útil: un agonista parcial, **en presencia de un agonista pleno**, se comporta como
antagonista, porque ocupa receptores y entrega menos activación de la que entregaría el pleno. Por eso el
mismo compuesto puede subir o bajar la señal según el tono endógeno del sistema. Cualquier afirmación del
tipo "regula el sistema" debe poder explicarse así o es palabrería.

## Kd, Ki, EC50: no son lo mismo

```
Kd   ← afinidad, de un ensayo de unión directa
Ki   ← afinidad, de un ensayo de competencia (corregida por Cheng-Prusoff, ver 116)
EC50 ← potencia funcional, de un ensayo de efecto
```

En sistemas con reserva de receptores, **EC50 puede ser mucho menor que Kd**: basta ocupar el 10 % para
lograr el efecto máximo. Por eso comparar la EC50 de un laboratorio con la Kd de otro es un error de bulto.
Compara siempre magnitudes homólogas medidas en el mismo tipo de sistema.

## Selectividad: el número que nadie enseña

Un ligando con Ki = 20 nM en 5-HT2A y Ki = 25 nM en 5-HT2B no es selectivo: la relación es 1,25×. Y en ese
ejemplo concreto importa mucho, porque la activación crónica de 5-HT2B se asocia a efectos cardiacos
adversos documentados con otros agonistas `[clínico]`. La selectividad se reporta como cociente de Ki y se
obtiene de un panel de dianas, no de un solo ensayo.

## Cómo se mide

| Parámetro | Método | Unidad | Notas críticas |
|---|---|---|---|
| Kd / Ki | Radioligando de saturación o competencia; SPR; TR-FRET | nM | Exigir el radioligando usado y su Kd |
| Emáx y EC50 | Ensayo funcional (AMPc, GTPγS, Ca2+, β-arrestina) | % vs referencia, nM | El "100 %" debe ser un agonista de referencia declarado |
| Eficacia relativa | Comparación contra agonista pleno en el mismo sistema | fracción | Sin referencia, el % no significa nada |
| Selectividad | Panel de 40–80 receptores | cociente de Ki | Los "hits" fuera de blanco explican efectos adversos |
| Ocupación in vivo | PET con radiotrazador | % ocupación a dosis X | El puente real entre in vitro y humano |

## Ejemplo aplicado — auditar una ficha de CBD

Ficha comercial recibida **(ILUSTRATIVO)**: "CBD: alta afinidad por CB1 y CB2, modula el sistema
endocannabinoide". Lo que se responde, con la literatura en la mano:

1. **Falso de entrada**: el CBD tiene afinidad ortostérica **baja** por CB1 y CB2 comparado con el THC; lo
   que se ha descrito es modulación alostérica negativa de CB1 `[in vitro]` y actividad sobre otros blancos
   (TRPV1, GPR55, receptor 5-HT1A, inhibición de la recaptación/hidrólisis de anandamida) `[in vitro]`.
2. Pide las Ki numéricas y el sistema de ensayo. Si no las tiene, no tiene farmacología: tiene folleto.
3. Contrasta con lo que sí es sólido: la interacción del CBD con enzimas CYP (inhibición de CYP3A4 y
   CYP2C19) tiene respaldo clínico y consecuencias reales de interacción farmacológica (ver `124`, `139`).
4. Conclusión para el expediente: el mecanismo se describe como multi-diana y no bien definido, con
   evidencia mayormente `[in vitro]`; la conversación relevante para seguridad es la de interacciones.

## Errores comunes

- Decir "alta afinidad" sin dar Ki en nM ni el ensayo. Es la señal más clara de dossier vacío.
- Comparar EC50 de un laboratorio con Kd de otro y concluir potencia relativa.
- Ignorar que un agonista parcial puede reducir la señal cuando el tono endógeno es alto.
- No pedir el panel de selectividad y luego sorprenderse con efectos fuera de blanco.
- Reportar "% de activación" sin declarar cuál es el agonista de referencia al 100 %.
- Suponer que afinidad in vitro se traduce a ocupación in vivo sin datos de exposición (`121`).

## Conexión con otros módulos

→ `118-receptores-y-transduccion-de-senal.md` — qué pasa después de la unión.
→ `119-farmacodinamia-y-dosis-respuesta.md` — la curva donde se leen Emáx y potencia.
→ `128-serotonina-y-receptor-5ht2a.md` — el caso 5-HT2A.
→ `129-sistema-endocannabinoide.md` — CB1/CB2 y el papel real del CBD.
→ `206-farmacologia-del-cbd.md` — el detalle completo del CBD.