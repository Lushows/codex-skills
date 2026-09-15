# 139 · La lista de lo que nunca entra

**Qué resuelve:** cerrar la discusión. Los módulos anteriores explican el porqué; este es
la lista, corta y tajante, de lo que no se pone en un episodio de Paper Empires bajo
ninguna circunstancia, ni «solo tres segundos», ni «es para el gancho», ni «nadie se va a
dar cuenta».

> ⚖️ **Esto no es asesoría legal.** Es una política interna deliberadamente **más
> estricta que la ley**, porque el coste de equivocarse (perder el canal) es mucho mayor
> que el coste de renunciar a un audio.

---

## La regla de la línea

> **Si no puedes escribir la procedencia de un audio en UNA línea —qué es, de dónde
> salió, con qué licencia y con qué fecha— no entra.**

No «no entra todavía». No entra. Se sustituye por algo sintetizado (§ 135) y se sigue
trabajando. La duda no se investiga a mitad de montaje: se resuelve cambiando el audio.

## La lista

| Nunca entra | Por qué | Qué se hace en su lugar |
|---|---|---|
| **Música comercial**, aunque sean 3 segundos | Content ID detecta fragmentos cortos (§ 132) | tema propio sintetizado (§ 82) |
| **Grabaciones de sello de obras de dominio público** | la obra es libre, el fonograma no (§ 130) | tocar/sintetizar la pieza nosotros |
| **Audio de películas, series, documentales o tráileres** | fonograma, obra y producción, todo ajeno | efecto propio + rótulo que lo explique |
| **Sintonías, jingles y cabeceras reconocibles** | son marca además de obra | motivo propio del canal (§ 126) |
| **Sonidos de videojuegos** | licencia del estudio; muchos están en Content ID | síntesis (§ 81) |
| **Samples de packs de origen dudoso** (foros, descargas, «encontrado en Google») | sin cadena de derechos: respondes tú | osciladores y ruido propios |
| **Audio extraído de un vídeo de YouTube** | sin licencia y sin fuente citable | ir al archivo institucional (§ 137) o sintetizar |
| **Grabaciones de conciertos o de radio** | fonograma + intérpretes + emisora | descartar |
| **Podcasts y entrevistas ajenas** | obra y fonograma del productor | citar el contenido en voz del canal (§ 48) |
| **«Sonido de TikTok» / audios virales** | licencia de plataforma, no exportable | síntesis |
| **Pistas «sin copyright» sin página de licencia** | la etiqueta no es una licencia (§ 134) | descartar |
| **Piezas con licencia NC o ND** | NC choca con la monetización; ND, con el montaje | descartar |
| **Remasterizaciones de grabaciones antiguas** | pueden generar fonograma nuevo ⚠️ discutido (§ 137) | tratarlas como protegidas: descartar |
| **Voz clonada de una persona real** | derecho sobre la semejanza + credibilidad del canal (§ 136) | voz del canal, rotulada como lectura |
| **Rostro generado de una persona real** | detección de semejanza de YouTube (§ 136) | recorte de archivo o reconstrucción etiquetada |

## La zona gris, que también se evita

No son ilegales necesariamente. Se evitan porque **cuestan más gestión de la que
aportan**:

- **Bancos «libres de derechos», gratuitos o de pago.** Añaden un contrato que
  administrar y un reclamante permanente (§ 134).
- **Bibliotecas de audio con subidas de usuarios.** El banco no verifica la cadena; tú
  respondes por el robo de otro.
- **Música generada por modelos de IA.** Términos de uso variables, dudas abiertas sobre
  entrenamiento y titularidad. ⚠️ **No lo doy por resuelto**; el canal no lo usa.
- **Audio de archivo cuyo `titular_fonograma` queda en `desconocido`.** La compuerta de
  § 138 lo rechaza automáticamente.

## Lo que sí entra

Para que la lista no parezca solo prohibiciones:

1. **Todo lo sintetizado por nosotros** con su script y su entrada en `pistas.json`
   (§ 135, § 138).
2. **La voz del canal**, con los términos del motor leídos y guardados (§ 136, con la
   deuda abierta de `edge-tts` que ese módulo documenta).
3. **Archivo sonoro que pasa el filtro completo de § 137**, con los dos titulares
   identificados y la ficha descargada.

Nada más. La lista de lo que entra cabe en tres puntos, y esa es exactamente la
intención.

## Lo que está en juego

| Si entra algo de la lista | Consecuencia realista |
|---|---|
| Reclamación de Content ID | los ingresos de ese vídeo van a otro |
| Bloqueo por territorio | el episodio deja de verse donde más CPM tiene |
| Retirada por derechos de autor | **falta**; varias cierran el canal |
| Disputa perdida tras apelar | camino directo de la reclamación a la falta (§ 133) |
| Voz o cara falsificada descubierta | se rompe lo único que vende un canal de documentales |

El único renglón realmente irreversible es el último: una reclamación se resuelve, un
canal cerrado se pierde, pero la credibilidad rota no se recupera con una rectificación.

## La comprobación antes de publicar

```
por cada archivo de audio del render:
    ¿tiene entrada en audio/pistas.json?          → si no, PARAR
    ¿su origen es "sintetizado"?
        SÍ  → adelante
        NO  → ¿hay PDF de licencia o ficha de archivo
               con titular del FONOGRAMA?          → si no, PARAR
    ¿alguna pista imita una melodía reconocible?  → si sí, PARAR (§ 135)
    ¿alguna voz o rostro imita a una persona real? → si sí, PARAR (§ 136)
```

Son cuatro preguntas. Cuestan un minuto y son lo único que separa este canal de la causa
número uno de muerte de los canales de archivo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| «Son solo tres segundos» | Content ID detecta fragmentos de segundos |
| «Lo pongo bajito debajo de la voz» | la huella se detecta igual con voz encima |
| «Le cambio el tono y la velocidad» | el sistema está hecho justo para eso |
| «Es un canal pequeño, nadie lo va a mirar» | la detección es automática, no depende del tamaño |
| «Lo cito en la descripción» | citar no es licenciar |
| «Lo saco si me reclaman» | para entonces ya perdiste ingresos y sumaste historial |
| Hacer una excepción «solo en este episodio» | la lista deja de ser una lista y vuelve la discusión |

## Relacionado

`130` la obra y la grabación · `132` Content ID · `133` reclamaciones ·
`134` bancos de música · `135` sintetizar es la garantía · `136` voz generada ·
`137` el sonido de archivo · `138` registrar lo propio
