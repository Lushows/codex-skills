# 34 · Movimiento que narra

**Qué resuelve:** el movimiento por defecto —empujar siempre, porque hay que mover algo—
es decoración. El movimiento tiene significado y el espectador lo lee aunque no lo
piense. Si contradice lo que dice la voz, resta; si lo acompaña, el plano vale el doble
sin material extra.

---

## El diccionario

| Intención de la frase | Movimiento | Parámetro |
|---|---|---|
| Entrar en la historia, en la cara, en la culpa | Empuje lento al punto de interés | 8-11%, easeOut |
| Revelar el contexto, la consecuencia, la soledad | Alejamiento | 10-14%, empezando en 1,14 |
| Algo no cuadra, inquietud, sospecha | Deriva diagonal + péndulo | 8-10%, 10-14 px/s |
| La ambición, la cifra que crece | Escala creciente + contador | 12-16%, easeIn |
| La caída, la pérdida, el final | Deriva hacia abajo + alejamiento | 10%, dy 8-12 px/s |
| El tiempo que corre, la persecución | Travelling lateral | 14-16%, 60-90 px/s |
| La revelación, el dato que cambia todo | **Freno**: el gesto se detiene sobre la palabra | easeOut fuerte, `pow(...,5)` |
| La rutina, el trámite, lo burocrático | Estático con capas: la cámara no se mueve, entran documentos | 0% de fondo |

**La regla que ordena todo:** el gesto **resuelve sobre la palabra clave**. No termina
antes (el plano se queda muerto esperando el corte) ni sigue después (la palabra pasa
mientras la cámara todavía viaja y se pierde el acento).

---

## El freno narrativo

Es el gesto más útil del canal y el que menos se usa. La cámara empuja y va frenando
hasta detenerse justo cuando la voz dice la palabra que importa. El movimiento
**subraya** sin que nada aparezca en pantalla.

```bash
# La palabra clave suena en el segundo 3,40 del plano.
# El empuje de 13% frena a cero exactamente ahí.
[0:v]scale=4320:-2,
     zoompan=z='1+0.13*(1-pow(1-clip((on/25)/3.4,0,1),5))':d=1:
             x='(iw-iw/zoom)*0.58':y='(ih-ih/zoom)*0.34':
             s=1920x1080:fps=25
```

Con exponente 5, el 80% del recorrido se gasta en el primer 30% del tiempo: el último
segundo casi no se mueve y la detención se siente. Con exponente 3 la frenada es más
suave y sirve para frases largas.

## El empuje que acelera

Lo contrario: el gesto se acelera hacia el corte. Sirve para tensión y para entregar el
plano siguiente con energía.

```
z='1+0.14*pow(clip((on/25)/3.0,0,1),2)'
```

Se **corta en pleno movimiento**, nunca cuando ya paró. Un plano que se detiene antes
del corte deja un agujero de medio segundo (ver `38`).

## La velocidad es tono

El mismo gesto dice cosas distintas según el recorrido:

| Recorrido | Lectura |
|---|---|
| 6-8% | Calma, respeto, distancia. Un retrato de archivo, una fecha |
| 9-12% | Ritmo de crucero. El desarrollo del episodio |
| 13-16% | Tensión, urgencia. El gancho y el remate |
| más de 18% | Solo travelling intencionado. Fuera de eso, se lee como error |

## El movimiento contradictorio

Es el error caro, porque el plano parece correcto y el episodio se siente mal:

| La voz dice | Y la cámara | Resultado |
|---|---|---|
| Algo íntimo, personal | Se aleja | El espectador se desconecta justo donde debía acercarse |
| Que todo se derrumbó | Empuja hacia dentro | Suena a triunfo |
| Una cifra enorme | Deriva lenta y suave | La cifra pierde peso |
| Una lista de trámites | Travelling dramático | El plano promete algo que la frase no da |

## Verificación

En la tabla de eventos, cada plano lleva su columna `mov` **y su motivo**:

```python
{"plano": 7, "mov": "freno", "r": 0.13, "motivo": "cierra sobre 'nunca devolvió'"},
{"plano": 8, "mov": "alejar", "r": 0.11, "motivo": "aparece el barrio entero"},
{"plano": 9, "mov": "deriva", "r": 0.09, "motivo": "transición, no hay dato nuevo"},
```

**Si el motivo es "para que se mueva", el plano está sin dirigir.** No siempre hay que
cambiarlo —los planos de apoyo existen— pero hay que saber cuáles son y que no sean más
de un tercio del episodio.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Empujar en todos los planos | El episodio tiene una sola emoción: avanzar |
| El gesto termina antes que la frase | Medio segundo de plano congelado antes del corte |
| El gesto sigue después de la palabra clave | La palabra pasa desapercibida |
| Movimiento fuerte en un plano de trámite | Promete un giro que no llega |
| Alejarse en el momento íntimo | Contradicción; el espectador se despega y no sabe por qué |
| Deriva en el remate | El remate necesita freno, no vagabundeo |

## Relacionado

`15` rampa de ritmo · `30` catálogo de movimientos · `31` curvas de aceleración ·
`38` ritmo del movimiento · `39` sincronizar gesto y palabra
