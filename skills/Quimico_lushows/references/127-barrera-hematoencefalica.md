# 127 — Barrera hematoencefálica (el filtro que descarta la mitad de los claims "para el cerebro")

Cualquier producto que se venda "para la mente", "para la memoria" o "para el enfoque" tiene que responder
una pregunta que casi nunca responde: **¿la molécula llega al cerebro?** La barrera hematoencefálica es un
filtro físico y activo que deja pasar muy poco. Este módulo te da los criterios fisicoquímicos y los métodos
para comprobarlo, y te permite descartar en cinco minutos afirmaciones nootrópicas que no tienen forma de
ser ciertas. El error caro que evita: construir una línea "cognitiva" sobre una molécula que no atraviesa.

Términos: **barrera hematoencefálica (blood-brain barrier, BBB)** = red de capilares cerebrales con uniones
estrechas entre células endoteliales, sin las fenestraciones que tienen otros capilares. **Uniones estrechas
(tight junctions)** = sellos entre células que impiden el paso entre ellas. **Transportador de eflujo
(efflux transporter)** = bomba que devuelve activamente a la sangre lo que logró entrar; P-gp y BCRP son las
principales. **Kp,uu** = cociente de concentración libre en cerebro sobre libre en plasma; es el mejor
indicador de penetración real.

## Por qué es tan restrictiva

```
Capilar normal          Capilar cerebral
─────────────           ────────────────
células con huecos      uniones estrechas continuas
poca cobertura          pericitos + pies astrocitarios
difusión libre          transporte selectivo + bombas de eflujo (P-gp, BCRP)
```

Resultado: el paso ocurre por tres rutas y ninguna es gratis.

| Ruta | Qué la usa | Requisitos |
|---|---|---|
| Difusión pasiva transcelular | Moléculas pequeñas y lipofílicas | < ~400–500 Da, logP ~2–3, pocos H-bond, no sustrato de P-gp |
| Transporte mediado por transportador | Glucosa (GLUT1), aminoácidos (LAT1), colina | Debe parecerse al sustrato natural |
| Transcitosis mediada por receptor | Transferrina, insulina | Vía usada por biotecnología, no por suplementos |

Y hay una cuarta que importa mucho al hablar de eje intestino-cerebro: la señalización **indirecta** — vía
nervio vago, metabolitos microbianos (ácidos grasos de cadena corta), citoquinas. Una molécula puede
influir en el cerebro **sin entrar**, pero entonces el mecanismo que se propone es otro y hay que decirlo
así (ver `131`).

## Reglas de dedo para saber si algo entra

Criterios orientativos (no leyes):

- Peso molecular < 400–500 Da.
- logP entre aproximadamente 1,5 y 3 (muy polar no cruza; demasiado lipofílico se queda en membranas).
- Menos de ~8 enlaces de hidrógeno totales.
- Sin carga permanente al pH fisiológico.
- **No ser sustrato de P-gp** — este es el que más candidatos tumba.

Aplicación inmediata:

| Molécula | ¿Cruza? | Por qué |
|---|---|---|
| Psilocina (~204 Da) | Sí `[clínico]` | Pequeña, lipofilia adecuada; la psilocibina es el profármaco que se desfosforila (`258`) |
| Δ9-THC (~314 Da) | Sí `[clínico]` | Muy lipofílica |
| Cafeína (~194 Da) | Sí `[clínico]` | Pequeña y suficientemente lipofílica |
| Erinacina A (~430 Da, diterpenoide) | Se ha propuesto que sí `[animal]` | Datos preclínicos; sin PK humana publicada robusta |
| Hericenonas (mayores, muy lipofílicas) | No demostrado en humanos | Falta dato |
| β-glucano (kDa a cientos de kDa) | No | Polímero enorme y polar (`130`) |
| Ergotioneína | Entra por transportador OCTN1 `[animal]` / `[in vitro]` | Vía activa, no pasiva (`235`) |

Ese contraste hericenonas vs erinacinas es una discusión seria en melena de león: se ha planteado que las
erinacinas, más pequeñas, serían las candidatas plausibles a penetración cerebral, mientras que las
hericenonas serían menos probables. A agosto de 2026 sigue sin haber farmacocinética humana publicada
sólida de ninguna de las dos. Eso se dice tal cual (ver `226`).

## Cómo se mide

| Nivel | Método | Qué da | Limitación |
|---|---|---|---|
| Predicción | Modelos in silico (reglas de BBB, QSAR) | Probabilidad | Orientativo, se equivoca |
| `[in vitro]` | PAMPA-BBB; monocapa de células endoteliales cerebrales | Papp (cm/s) | No reproduce el eflujo real completo |
| `[in vitro]` | Ensayo de sustrato de P-gp (Caco-2 bidireccional) | Ratio de eflujo | Un ratio > 2 es señal de alerta |
| `[animal]` | Cociente cerebro/plasma; microdiálisis cerebral | Kp, Kp,uu | Diferencias de especie en P-gp |
| `[clínico]` | PET con radiotrazador; LCR (líquido cefalorraquídeo) | % ocupación, ng/mL en LCR | Caro, requiere trazador |

**Kp,uu ≈ 1** significa buena penetración libre; **Kp,uu << 1** significa que hay eflujo activo aunque el
cociente total parezca alto (porque el compuesto se pegó a lípidos cerebrales sin estar disponible).

## Ejemplo aplicado — auditar un claim nootrópico

Producto **(ILUSTRATIVO)**: "Cápsula de melena de león — apoya la claridad mental." El proveedor cita un
estudio en roedores donde erinacina A incrementó marcadores de NGF en hipocampo `[animal]`.

Lo que se revisa:

1. ¿El producto **contiene** erinacina A? Las erinacinas se producen principalmente en cultivo de micelio,
   no en el cuerpo fructífero. Si el producto es cuerpo fructífero, el estudio citado no aplica al material.
2. ¿Cuánta erinacina A hay? Casi ningún COA comercial la cuantifica. Sin ese número no hay dosis
   comparable (ver `226`).
3. ¿Hay dato de paso de BBB en humanos? No publicado a agosto de 2026.
4. ¿Qué queda en pie? Ensayos clínicos pequeños con desenlaces cognitivos autorreportados, heterogéneos,
   con material poco caracterizado → `[clínico fase 2]` de baja calidad (ver `248`).
5. Lenguaje sostenible: describir el material, su contenido medido y el estado de la evidencia. Sin nombrar
   ninguna enfermedad neurológica ni cognitiva; eso es claim prohibido en Colombia (ver `268`).

## Errores comunes

- Vender "para el cerebro" sin haber preguntado si la molécula atraviesa la barrera.
- Extrapolar de roedor a humano sin considerar diferencias de P-gp entre especies.
- Usar el cociente cerebro/plasma total (Kp) en vez del libre (Kp,uu) y sobrestimar la penetración.
- Citar estudios de micelio (erinacinas) para vender cuerpo fructífero, o al revés (`217`, `226`).
- Suponer que "cruza la barrera" implica que llega a concentración activa. Son dos preguntas distintas.
- Confundir efecto central directo con señalización indirecta vía intestino (`131`). Ambas pueden existir,
  pero el mecanismo que se afirma debe corresponder a la evidencia que se tiene.

## Conexión con otros módulos

→ `121-farmacocinetica-adme.md` — distribución, de la que la BBB es un caso especial.
→ `131-eje-intestino-cerebro-y-microbiota.md` — cómo influir sin entrar.
→ `128-serotonina-y-receptor-5ht2a.md` — un caso donde sí entra y se conoce el receptor.
→ `226-hericenonas-y-erinacinas-analisis.md` — cómo se cuantifican estas moléculas.
→ `225-melena-de-leon-hericium-quimica.md` — la química de la materia prima.