# 177 — Acceso de emergencia y herencia: si Luis no está

## El problema que nadie quiere pensar

La cripto no tiene sucursal donde la familia pueda ir con el certificado de defunción. Si el
único que conoce las claves falta (muerte, accidente, incapacidad), el dinero **existe pero es
inalcanzable** — para siempre. Se estima que una fracción enorme de todo el bitcoin está
perdida así. Un sistema serio planifica esto igual que planifica los stops.

También aplica a escenarios menores: hospitalización, viaje sin acceso, pérdida de memoria de
una clave. "Acceso de emergencia" no es solo herencia.

## La tensión a resolver

- Si NADIE más puede acceder → el dinero muere contigo.
- Si alguien más puede acceder HOY → creaste un riesgo en vida (robo, presión, error).

La solución es acceso **documentado pero sellado**: la información existe, completa, pero
nadie puede usarla mientras estés bien.

## El paquete de emergencia (qué documentar)

| Elemento | Ejemplo |
|---|---|
| Inventario de cuentas | Exchange X, banco Y, hardware wallet Z — SIN claves aún, solo qué existe |
| Frase semilla | En papel/metal, en sobre sellado, ubicación segura |
| Instrucciones | "Paso 1: contactar a [contador/persona de confianza]. Paso 2: ..." en lenguaje simple |
| Accesos digitales | Gestor de contraseñas: clave maestra en el sobre, o función de "acceso de emergencia" del gestor |
| Contexto | Qué es el bot, dónde corre, que se puede simplemente APAGAR y retirar los fondos |

**Regla de oro:** la familia no necesita entender trading. Necesita UNA instrucción: "apaga
esto, retira todo a pesos, con ayuda de [persona/contador de confianza]".

## Cómo separar acceso de conocimiento (opciones de menor a mayor)

1. **Sobre sellado** en lugar seguro (caja fuerte, caja de seguridad) + decirle a UNA persona
   de confianza que existe y dónde está — no qué contiene.
2. **Dividir la información**: la semilla en un lugar, la instrucción de dónde está en otro.
3. **Gestores de contraseñas con acceso de emergencia**: un contacto puede solicitar acceso y
   tú tienes días para negarlo — si no respondes (porque no estás), entra.
4. Formalizar con testamento la existencia de estos activos — punto legal colombiano:
   **verificar con contador_lushows / abogado**, sin improvisar figuras de memoria.

Lo que NUNCA: semilla en una foto del celular, en Drive/correo sin cifrar, o repartida en
un chat familiar "por si acaso".

## Mantenimiento

Revisar el paquete cada vez que cambie algo grande (nuevo exchange, nueva wallet, cambio de
banco) y mínimo una vez al año. Un paquete desactualizado da falsa tranquilidad.

## Cómo aplica al AGENTE TRADING

- Hoy (paper) el paquete es corto: accesos a GitHub, Render, correo y este manual. Armarlo
  ya, que el hábito quede antes de que haya dinero real.
- Al go-live se agregan: exchange, banco asociado, hardware wallet. La instrucción para la
  familia es una sola línea: "apagar el bot y retirar — no intenten operar".
