# 176 — Seguridad personal del trader: el eslabón débil eres tú

## La verdad incómoda

A la mayoría de la gente no le hackean el exchange: **la engañan a ella**. Los ataques más
efectivos no rompen computadores, rompen personas. Y el dueño de un bot de trading es un
objetivo más jugoso que el usuario promedio: se asume que tiene capital y acceso a APIs.

## Los 3 ataques que debes conocer por nombre

### 1. SIM swapping (robo de tu número)
El atacante convence al operador celular (o soborna a un empleado) de pasar TU número a SU
sim. Desde ese momento recibe tus SMS — incluidos los códigos de verificación — y resetea tus
cuentas. **Defensa:** nunca usar SMS como segundo factor en cuentas de dinero; usar app
autenticadora (Google Authenticator, Authy) o llave física; poner clave/pin de portabilidad
con el operador celular.

### 2. Phishing (la imitación)
Correo o página idéntica a Binance/tu banco pidiendo "verificar tu cuenta". Escribes tu clave
en la copia y se la regalaste al ladrón. **Defensa:** jamás entrar por links de correos o
mensajes; escribir la URL a mano o usar marcador guardado; desconfiar de toda urgencia
("tu cuenta será suspendida en 24 horas" = casi seguro estafa).

### 3. Ingeniería social (el cuento)
El "soporte de Binance" que te escribe por WhatsApp/Telegram, el "asesor" que te ayuda a
"recuperar fondos", la "chica" que te enseña su plataforma de inversión (pig butchering).
**Defensa:** ningún exchange te escribe primero por chat. Nadie legítimo te pide tu frase
semilla, tu clave o instalar un programa de acceso remoto. NUNCA.

## Higiene digital del dueño de un bot (checklist)

- **2FA con app** (no SMS) en: exchange, correo, GitHub, Render, y el correo de recuperación.
- **El correo es la llave maestra**: quien controla tu email resetea todo lo demás. Protegerlo primero.
- Claves únicas por servicio, en un gestor de contraseñas. No la misma clave del 2015 en todo.
- **API keys del bot con permisos mínimos**: solo trading, retiros DESACTIVADOS, restricción
  por IP si el exchange lo permite. Si roban la key, que no puedan sacar fondos.
- Secrets fuera del código: .env local y variables de Render, jamás commiteados a GitHub.
- Equipo del bot limpio: no instalar software pirata/cracks en la máquina que toca las keys.

## No presumir ganancias en redes

Publicar pantallazos de ganancias te convierte en objetivo — de estafadores digitales y, en
Colombia, de riesgos muy físicos. El trader silencioso vive más tranquilo. Ni el monto del
capital, ni el exchange que usas, ni pantallazos del dashboard en redes públicas.

## Cómo aplica al AGENTE TRADING

- Implementar YA (aunque sea paper): 2FA app en correo y GitHub, gestor de contraseñas,
  pin de portabilidad con el operador.
- Al crear las API keys reales: retiros deshabilitados + IP restringida. Es la diferencia
  entre "me robaron la key" (susto) y "me vaciaron la cuenta" (tragedia).
