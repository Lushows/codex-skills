# Índice de módulos · canales_lushows

Plan de expansión de la skill. Cada módulo es un archivo de `references/` que se carga
bajo demanda. Marcados: ✅ escrito · 🔨 en construcción · ⬜ pendiente.

**Estado: los 90 módulos están escritos.** Se escribieron en paralelo, un agente por
bloque, y cada uno verificó su propio código contra el proyecto real: los CSS se
renderizaron con Chrome, los filtros se ejecutaron con ffmpeg 8.1 y los scripts de
Python se corrieron sobre `piloto/`. Lo que salió mal en esa verificación está
documentado dentro de cada módulo, no escondido.

---

## 🎞️ Bloque 1 — Densidad, ritmo y arquitectura del plano (10–19)

| # | Módulo | Qué resuelve |
|---|---|---|
| 10 ✅ | `densidad-de-eventos.md` | Cuántos eventos por minuto, cómo se cuentan, el objetivo 44-48 y por qué no más. La diferencia entre *más cortos* y *más simultáneos* |
| 11 ✅ | `el-hueco-prohibido.md` | Ningún tramo sin elemento. Detector automático de huecos y las 6 maneras de rellenarlos sin ruido |
| 12 ✅ | `capas-simultaneas.md` | 2-4 elementos vivos a la vez: reparto de peso, quién manda, quién acompaña |
| 13 ✅ | `ciclo-de-vida-del-elemento.md` | Entrada, gesto, salida. Duraciones por tipo (dato, retrato, documento, objeto) |
| 14 ✅ | `encadenar-elementos.md` | Que uno salga empujando al siguiente: relevo, solape, sustitución |
| 15 ✅ | `rampa-de-ritmo.md` | Acelerar hacia el remate y frenar en la revelación |
| 16 ✅ | `el-plano-de-descanso.md` | Cuándo SÍ vale un plano limpio (y son pocos) |
| 17 ✅ | `medir-el-montaje.md` | Script de auditoría: eventos/min, huecos, duración media, simultaneidad |
| 18 ✅ | `densidad-por-tipo-de-bloque.md` | El gancho pide más densidad que el desarrollo; el remate, menos |
| 19 ✅ | `errores-de-ritmo.md` | Los 8 síntomas de un montaje flojo y su causa |

## 🧩 Bloque 2 — Composición del collage (20–29)

| # | Módulo | Qué resuelve |
|---|---|---|
| 20 ✅ | `reticula-del-collage.md` | Las 9 posiciones canónicas y por qué no se colocan elementos a ojo |
| 21 ✅ | `peso-visual-y-jerarquia.md` | Tamaño, contraste y posición: quién se ve primero |
| 22 ✅ | `profundidad-por-capas.md` | Fondo, medio, frente. Escala y desenfoque para dar aire |
| 23 ✅ | `empatar-recorte-y-fondo.md` | Luz, ángulo, grano y color: cuándo un recorte NO pega |
| 24 ✅ | `agrupar-y-separar.md` | Gestalt aplicado: qué se lee como conjunto |
| 25 ✅ | `el-borde-de-papel.md` | Anatomía del recorte: margen, sombra, rasgado, cinta, grapa |
| 26 ✅ | `superposicion-y-oclusion.md` | Qué tapa a qué y por qué eso cuenta una historia |
| 27 ✅ | `composicion-de-datos.md` | Cifra + comparación + fuente en el mismo cuadro |
| 28 ✅ | `respiracion-del-cuadro.md` | Márgenes, zona segura y el vacío como material |
| 29 ✅ | `plantillas-de-escena.md` | 12 disposiciones probadas listas para reutilizar |

## 🎥 Bloque 3 — Movimiento (30–39)

| # | Módulo | Qué resuelve |
|---|---|---|
| 30 ✅ | `catalogo-de-movimientos.md` | Empuje, alejamiento, deriva, parallax, golpe, péndulo, latido |
| 31 ✅ | `curvas-de-aceleracion.md` | Por qué el lineal se ve barato; ease-in/out en `zoompan` y `overlay` |
| 32 ✅ | `entradas-y-salidas.md` | Las 8 familias, cuándo cada una, duraciones exactas |
| 33 ✅ | `parallax-real.md` | Separar figura y fondo en capas con velocidades distintas |
| 34 ✅ | `movimiento-que-narra.md` | Avanzar = entrar en la historia; alejarse = revelar contexto |
| 35 ✅ | `animar-una-foto-fija.md` | De lámina muerta a plano vivo (recorte + capas + micro-movimiento) |
| 36 ✅ | `contadores-y-cifras-animadas.md` | Números que suben, barras que crecen, mapas que se dibujan |
| 37 ✅ | `movimiento-de-camara-simulado.md` | Travelling, panorámica y grúa sobre material estático |
| 38 ✅ | `ritmo-del-movimiento.md` | Cambiar de dirección entre planos; el patrón que aburre |
| 39 ✅ | `sincronizar-gesto-y-palabra.md` | El adelanto de 0,1-0,2 s y por qué el ojo lo exige |

## 🔠 Bloque 4 — Texto en pantalla (40–49) ← **el más urgente tras el ritmo**

| # | Módulo | Qué resuelve |
|---|---|---|
| 40 ✅ | `el-texto-como-canal-principal.md` | La mayoría ve sin sonido: qué información NO puede vivir solo en el audio |
| 41 ✅ | `maquina-de-escribir.md` | **Efecto teletipo**: texto que se escribe letra a letra, con cursor y sonido. Implementación exacta en ffmpeg |
| 42 ✅ | `tipografia-del-canal.md` | Las 3 familias: titular (Archivo), dato (monoespaciada), documento (serif) |
| 43 ✅ | `rotulos-y-etiquetas.md` | Cómo se explica un objeto en pantalla sin estorbar |
| 44 ✅ | `la-cifra-en-pantalla.md` | Números: tamaño, color, unidad, fuente y el gesto de entrada |
| 45 ✅ | `subtitulos-y-destacados.md` | Cuándo transcribir y cuándo resaltar solo la palabra clave |
| 46 ✅ | `texto-sobre-collage.md` | Legibilidad sobre fotos: contorno, sombra, caja, tachado |
| 47 ✅ | `tipografia-cinetica.md` | Texto que reacciona: golpe, cascada, revelado por máscara |
| 48 ✅ | `citas-y-documentos.md` | Reproducir una frase textual del expediente con su formato |
| 49 ✅ | `zona-segura-y-tamanos.md` | Mínimos legibles por plataforma; qué se corta en móvil |

## 🎨 Bloque 5 — Fondos (50–59)

| # | Módulo | Qué resuelve |
|---|---|---|
| 50 ✅ | `sistema-de-fondos.md` | Un fondo por escena, construido por código: la regla y el porqué |
| 51 ✅ | `paleta-por-escena.md` | Temperatura y recorrido de color a lo largo del episodio |
| 52 ✅ | `texturas-de-fondo.md` | Papel, guilloché, rejilla técnica, tela, hormigón, metal |
| 53 ✅ | `luz-y-viñeta.md` | Dónde poner el punto de luz para guiar la mirada |
| 54 ✅ | `fondos-de-datos.md` | Rejillas, planos, mapas y tableros de investigación |
| 55 ✅ | `fondos-atmosfericos.md` | Humo, polvo, partículas, profundidad de campo simulada |
| 56 ✅ | `fondos-animados.md` | Fondos que se mueven solos sin robar atención |
| 57 ✅ | `transicion-de-fondo.md` | Cómo se pasa de una escena a otra sin corte brusco |
| 58 ✅ | `coherencia-entre-fondos.md` | Que los seis se vean del mismo episodio |
| 59 ✅ | `biblioteca-de-fondos.md` | Catálogo reutilizable con su código |

## ✨ Bloque 6 — Efectos visuales (60–69)

| # | Módulo | Qué resuelve |
|---|---|---|
| 60 ✅ | `catalogo-de-efectos.md` | Inventario: qué tenemos y qué falta |
| 61 ✅ | `efectos-de-dinero.md` | Fajos, lluvia de billetes, contadores, gráficas, balanzas |
| 62 ✅ | `efectos-de-documento.md` | Sellos, tachados, subrayados, anotaciones, firmas |
| 63 ✅ | `comparaciones-visuales.md` | Cómo se hace entender una cifra: escala humana, objetos conocidos |
| 64 ✅ | `mapas-y-rutas.md` | Trazados animados, puntos que laten, fronteras |
| 65 ✅ | `diagramas-de-flujo.md` | Cadenas de pasos que se construyen ante la cámara |
| 66 ✅ | `grano-y-textura.md` | Película, VHS, fotocopia, escaneo: cuál para qué |
| 67 ✅ | `luz-y-destellos.md` | Flash de archivo, foco, halo, proyector |
| 68 ✅ | `efectos-que-se-ven-baratos.md` | La lista negra y sus sustitutos |
| 69 ✅ | `construir-un-efecto-nuevo.md` | Método: de la idea al PNG animable |

## 🌀 Bloque 7 — Transiciones (70–79) ✅ **completo**

| # | Módulo | Qué resuelve |
|---|---|---|
| 70 ✅ | `cuando-usar-transicion.md` | El 90% van duras; las 4 respuestas válidas |
| 71 ✅ | `transiciones-de-collage.md` | Barrido con papel, pase de página, apilado |
| 72 ✅ | `match-cut-de-forma.md` | Cortar de un círculo a otro círculo: la forma como puente |
| 73 ✅ | `transicion-por-elemento.md` | Un recorte que cruza el cuadro y arrastra el cambio |
| 74 ✅ | `flash-y-golpe.md` | Los tres recursos que dan sensación de comercial |
| 75 ✅ | `transicion-sonora.md` | El sonido que cruza el corte (J-cut visual) |
| 76 ✅ | `entrar-y-salir-de-escena.md` | Cómo abre y cómo cierra cada bloque |
| 77 ✅ | `transiciones-de-marca.md` | El tachado rojo de Paper Empires como transición |
| 78 ✅ | `ritmo-de-transiciones.md` | No repetir la misma dos veces seguidas |
| 79 ✅ | `xfade-a-fondo.md` | Las que sirven de las 58 de ffmpeg y sus parámetros |

## 🔊 Bloque 8 — Sonido (80–89)

| # | Módulo | Qué resuelve |
|---|---|---|
| 80 ✅ | `arquitectura-de-la-mezcla.md` | Las 4 capas: voz, colchón, objetos, picos |
| 81 ✅ | `sintetizar-efectos.md` | Método para crear cualquier sonido con ffmpeg |
| 82 ✅ | `musica-por-codigo.md` | Progresiones, tensión armónica, temas por escena |
| 83 ✅ | `sonido-diegetico.md` | Lo que suena en pantalla y por qué ancla la imagen |
| 84 ✅ | `picos-dramaticos.md` | Riser, impacto, silencio: la arquitectura de un golpe |
| 85 ✅ | `ducking-y-espacio.md` | Que la voz mande sin aplastar el resto |
| 86 ✅ | `medir-el-audio.md` | LUFS, saltos por minuto, recorrido dinámico |
| 87 ✅ | `voz-a-fondo.md` | Cadena completa, ritmo, pausas, elección de voz |
| 88 ✅ | `sonido-por-idioma.md` | Cuadrar las 6 pistas sin rehacer la mezcla |
| 89 ✅ | `biblioteca-de-sonido.md` | Catálogo, nomenclatura y niveles calibrados |

## 📚 Bloque 9 — Investigación y guion (90–99)

| # | Módulo | Qué resuelve |
|---|---|---|
| 90 ✅ | `fuentes-primarias.md` | DOJ, FBI Vault, SEC, PACER, Treasury/OFAC: dónde y cómo buscar |
| 91 ✅ | `leer-un-expediente.md` | Qué mirar en una acusación o una sentencia |
| 92 ✅ | `el-aporte-original.md` | Convertir un dato en algo imaginable (el cálculo propio) |
| 93 ✅ | `estructura-de-episodio.md` | Gancho, bucle, desarrollo, remate: el reparto por minutos |
| 94 ✅ | `el-gancho-de-dinero.md` | Los 10 arranques que funcionan en este nicho |
| 95 ✅ | `escribir-para-el-oido.md` | Frases que se puedan decir; el ritmo del lenguaje |
| 96 ✅ | `verificacion-de-datos.md` | Nada en pantalla sin fuente; qué hacer con lo dudoso |
| 97 ✅ | `banco-de-historias.md` | Cómo se elige y se encola el siguiente caso |
| 98 ✅ | `episodios-largos.md` | Cómo se planifican 12 minutos por tramos |
| 99 ✅ | `titulo-miniatura-descripcion.md` | Lo que decide si le dan al play |

---

## Total: 90 módulos

**Lo que se escribe primero, porque es lo que hoy falla:**
`10` densidad · `11` el hueco prohibido · `12` capas simultáneas ·
`41` máquina de escribir · `40` el texto como canal principal · `17` medir el montaje
