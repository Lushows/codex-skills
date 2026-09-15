# 479 — Manifiesto de la contención

Esta es la última página del bloque 470–479. Lo anterior son procedimientos; esto es lo que queda
cuando los procedimientos se olvidan.

Empieza por lo único que hay que entender:

> **La contención no es pobreza. Es lo que hace que el efecto que sí está signifique algo.**
> Un vídeo con un destello tiene un destello. Un vídeo con veinte no tiene ninguno: tiene textura.

---

## I. La cuenta

**1. El presupuesto es una tasa, no un total.**
«Ocho efectos» no dice nada. Ocho en cuarenta segundos es una discoteca; ocho en doce minutos es un
documental sobrio. Lo que se decide es cuántos por minuto, y se decide antes.

**2. Uno de cada diez momentos puede llevar efecto.**
El episodio medido del piloto: 66 eventos, 5 efectos. **7,6 %.** Y el módulo `29`, llegando desde el
ritmo por otro camino, dice menos del 10 % de los cortes con transición. Dos cocinas, el mismo número.
Cuando dos métodos independientes coinciden, deja de ser una opinión.

**3. La energía no la dan los efectos.**
62,4 eventos por minuto con 4,7 efectos por minuto. El vídeo que se percibe cargadísimo lo está de
cosas que pasan, no de cosas procesadas. Si tu montaje se siente flojo, te faltan eventos; los efectos
son mucho más caros y no arreglan eso.

**4. Ánclalo a la estructura, no al reloj.**
«Uno por bloque» sobrevive a cualquier duración. «Cinco efectos» se rompe el día que el vídeo dura otra
cosa. Los dos episodios del piloto, de 63 y 80 segundos, acabaron en 4,7 y 4,5 efectos por minuto sin
que nadie calculara nada.

**5. El sexto efecto no pregunta si queda bien. Pregunta a cuál de los cinco sustituye.**
Esa pregunta mata sola al noventa por ciento de los candidatos, y al que sobrevive lo convierte en una
mejora en vez de una suma.

---

## II. El sitio

**6. Un efecto se paga donde se decide la atención, no donde ya la tienes.**
El piloto no pone un solo efecto en los primeros **6,88 segundos**. Ahí la atención te la están dando
gratis; gastarla en un fogonazo es pagar por algo que ya era tuyo.

**7. La fuerza sigue a la importancia de la frase, no a la duración del plano.**
El efecto más fuerte del episodio (0,22) está en el bloque **más corto** (6,73 s), que es el golpe de la
promesa. El más débil (0,14), en el bloque más largo de los flojos.

**8. El tramo aburrido no se tapa con un efecto.**
Se comprobó solo: el episodio peor montado de los dos —el que falla la simultaneidad y tiene cinco
huecos— es el que lleva **más** efectos. Un bloque flojo con un fogonazo encima sigue siendo un bloque
flojo, y ahora además tiene un fogonazo que no viene a cuento.

**9. Marca el final.**
El último efecto del piloto cae a 0,52 s del final. Un vídeo que se apaga sin subrayar su última frase
desaprovecha el único trozo que el espectador se lleva entero.

---

## III. La medida

**10. Mídelo en el archivo antes de molestar a un espectador.**
Dos minutos, gratis, sin varianza de plataforma. La viñeta cambia muchísimo la imagen (PSNR 20,6 dB) y
cuesta **+0 % de peso**. El grano apenas la cambia (43,6 dB) y cuesta **+55 % de peso y +152 % de
render**. Eso se sabe antes de publicar, y saberlo cierra la discusión.

**11. Lo que no llega, no existe.**
Un efecto de luminancia a gran escala atraviesa una recompresión a 400 kbps sin despeinarse. Uno de
detalle fino llega convertido en lo que el códec decidió. Si tu efecto vive en la alta frecuencia, no es
tuyo: es del compresor.

**12. No vas a poder medir el efecto de un efecto.**
Ocupa el **1,6 %** del metraje. La variación normal entre dos vídeos iguales ronda los ±10 puntos. Deja
de intentar demostrarlo: decídelo por criterio y gasta tu capacidad de experimentar en lo que sí mueve
diez puntos.

**13. El tiempo de render es la medida más ruidosa que tienes.**
La misma orden, sin efecto, tardó 25, 36, 42 y 51 segundos en cuatro pasadas de la misma máquina. Si tu
decisión depende de esa columna, no tienes una decisión: tienes un ruido con formato de tabla.

---

## IV. El sistema

**14. Lo que se vuelve marca no es el efecto: son sus números.**
Un destello lo tiene cualquiera. El de 0,075 s de medio ancho, campana de Gauss, contraste al 1,4 del
brillo y 40 ms de adelanto, repetido cien veces, es tuyo.

**15. Deja una sola perilla.**
Si varían tres parámetros, ninguno significa nada. En el piloto solo varía la fuerza, y por eso la
fuerza dice algo.

**16. La deriva empieza en cinco milésimas de segundo.**
El parámetro declarado como fijo ya tiene dos valores entre dos episodios: 0,09 y 0,095. Nadie lo
decidió, nadie lo va a ver, y así es como se muere un sistema. Con dos episodios se arregla en treinta
segundos; con veinte, no hay nada que reconstruir.

**17. Te vas a aburrir de tu efecto antes que nadie.**
Tú lo has visto cuatrocientas veces. El espectador, dos. Aburrirte no es una razón para cambiarlo: es la
prueba de que está funcionando.

---

## V. La escala

**18. Nada escala multiplicando. Nada.**
De un minuto a doce: de 61 elementos a **700**; de catorce minutos de render a **dos horas y media**; de
2,5 ventanas antirrepetición a **28,8**. Y el presupuesto de efectos, que parecía la excepción, tampoco:
por encima de los tres minutos el cupo de un mismo recurso **baja**, porque el espectador ya lo aprendió.

**19. A doce minutos hace falta material, no reglas más laxas.**
Hacen falta 560 recursos distintos. En disco hay 416 y el vocabulario conoce 56. Bajar la ventana de
25 s a 10 s no resuelve la sequía: la hace visible.

**20. Lo que no escala es lo que decide si el episodio es bueno.**
Elegir el material, escuchar el corte entero, decidir dónde va cada efecto. Ninguna de las tres se
automatiza, y las tres son las que importan.

---

## VI. El final

**21. Un efecto puede no estar aunque el render sea perfecto.**
Sin `eval=frame` el destello no ocurre, el archivo sale sano y `ffprobe` está encantado. Búscalo en el
fichero renderizado: los cinco del piloto aparecen con un salto de luz de +17 a +32, y todo lo demás se
queda en +8,5. No hay que afinar nada: o está o no está.

**22. Si no cabe la razón en una frase, sale.**
No «queda bien». Una frase que diga qué hace. Es la regla del `29` y a estas alturas ya sabes que es la
que más cosas quita.

**23. Escríbelo o lo volverás a inventar.**
Y la reinvención sale distinta cada vez. A los seis episodios no tienes un efecto: tienes cinco primos
parecidos.

**24. Documenta también los noes.**
Lo que vuelve cada tres meses no son los efectos que funcionan: son los que parecen buena idea y no lo
son. Cuatro líneas con un número al lado acaban con esa conversación para siempre.

---

## Errores frecuentes

Las once excusas con las que se rompe todo lo anterior, por orden de frecuencia:

1. «Es solo uno más.» Nunca es uno más: es el que rompe la proporción.
2. «Este tramo está flojo, le meto algo.» Le falta contenido, no procesado.
3. «Se ve mejor así hoy.» Ese es el mecanismo literal de la deriva.
4. «Ya lo verifico luego.» Luego el render son dos horas y media.
5. «Me acuerdo de los números.» Te acuerdas del efecto. Los números no.
6. «Subo un poco la fuerza a ver.» Si suben todos, el contraste vuelve a cero.
7. «Bajo el umbral y ya no avisa.» El aviso se va; el martillo sigue saliendo tres veces.
8. «Lo pruebo publicándolo.» No hay muestra para medir un 1,6 % del metraje.
9. «Es que este efecto me gusta.» El gusto no es una frase que diga qué hace.
10. «Con doce minutos hacemos lo mismo pero más largo.» Tres de los cuatro muros no son lineales.
11. «El render no dio error.» Nunca lo da. Ese es exactamente el problema.

---

## Checklist de conciencia

No es de ejecución. Se contesta una vez cada tanto, no en cada proyecto.

- [ ] ¿Puedo decir en una frase qué hace cada efecto de mi último vídeo?
- [ ] ¿Escribí el techo **antes** de montar, o lo conté después?
- [ ] ¿Mi efecto de marca tiene los mismos números que hace seis episodios? ¿Lo he comprobado?
- [ ] ¿Cuántos efectos he metido este mes para tapar un tramo que estaba flojo?
- [ ] ¿He medido alguna vez lo que me cuesta un efecto, o lo estimo?
- [ ] ¿Tengo escrito algún **no**? ¿O discuto la misma idea cada tres meses?
- [ ] La última vez que quité un efecto, ¿el vídeo empeoró de verdad?
- [ ] ¿Me he aburrido de algo mío y lo he cambiado sin que nadie me lo pidiera?
- [ ] ¿Estoy decidiendo con criterio o esperando que los datos decidan por mí algo que no pueden?

---

## Relacionado

- `470` a `478` — el bloque entero, del que esto es el resumen.
- `199` — manifiesto del editor: la página equivalente para el oficio completo.
- `269` — el presupuesto del esfuerzo; `209` — cuándo el motion sobra. Los dos módulos honestos de los
  que este desciende.
- `29` — el corte final: cuándo parar.
- `429` — cuándo quitar un efecto; `423` — el efecto que no se ve. Los dos módulos que convierten esta
  disciplina en umbrales duros.
- `420` — un efecto es una hipótesis: la frase con la que empieza todo este oficio.
- `canales/199-el-manifiesto-del-material` — el equivalente para el archivo y su licencia.
- `directorcreativo_lushows/225-restricciones-como-motor` — por qué la restricción produce más que la
  libertad, dicho desde la dirección creativa.
