# 248 · Aislar el worker GPU: contenedor, egress y SSRF al bajar URLs

> Tu worker recibe `image_url`/`audio_url` de internet y carga pesos no confiables. Es la superficie de
> ataque perfecta: una URL mala lee tu metadata cloud; un peso malo escapa el contenedor. Aísla por defecto.

## El modelo de amenaza del worker de inferencia
Un handler de generación visual hace tres cosas peligrosas a la vez:
1. **Baja URLs que controla el atacante** (`image_url`, `audio_url`, `ref_video`) → SSRF.
2. **Carga pesos** que pueden ejecutar código ([[247-model-supply-chain-pickle-safetensors]]) → RCE.
3. **Tiene secretos vivos**: token HF, claves R2/S3, URL del webhook firmado. Un escape = robo de todo.

Defensa = romper la cadena en cada eslabón. Asumir que el código *dentro* del contenedor puede ser hostil.

## SSRF: el bug que casi nadie cierra en workers GPU
El cliente manda `image_url`. Tu worker hace `requests.get(url)`. Si no validas, el atacante apunta a:

| Objetivo del atacante | Qué roba |
|---|---|
| `http://169.254.169.254/...` | Credenciales IAM/metadata de la nube (clásico SSRF→cloud takeover). |
| `http://localhost:6379` / puertos internos | Redis, panel del orquestador, otros servicios de tu VPC. |
| `file:///etc/passwd`, `gopher://`, `dict://` | Lectura de archivos / pivot por esquemas raros. |
| Redirect 302 a IP interna | Bypass de validación que solo mira la URL inicial. |

**Mitigación SSRF (capas):**
- **Allowlist de esquemas**: solo `https://`. Rechaza `file/gopher/ftp/dict`.
- **Resuelve el DNS tú mismo** y valida que la IP **no** sea privada/loopback/link-local
  (`10/8`, `172.16/12`, `192.168/16`, `127/8`, `169.254/16`, `::1`, IPv4-mapped). Hazlo **después** de seguir redirects, o desactiva redirects.
- **DNS rebinding**: valida la IP y **conéctate a esa misma IP** (pin), no re-resuelvas. Un dominio puede
  responder IP pública en la validación y privada en la descarga.
- **Límites**: timeout, tamaño máximo (`Content-Length` + corte de stream), tipo MIME esperado.
- Idealmente, **el orquestador descarga y valida** el archivo y le pasa al worker un blob ya saneado, no una URL.

## Egress: el worker no debería poder llamar a internet
Una vez cargado el modelo, el worker **solo** necesita: leer del Network Volume y subir el resultado a tu
bucket (o devolver al webhook). Nada más.
- **Bloquea egress por defecto**; allowlist el endpoint de R2/S3 y el del webhook. Sin egress libre, un peso
  troyanizado no puede exfiltrar ni hacer callback a C2.
- RunPod serverless no da firewall fino → al menos **no inyectes secretos que no uses**, y rota tokens con scope mínimo.
- Bloquea explícitamente `169.254.169.254` a nivel de red si la plataforma lo permite.

## Endurecer el contenedor
- **Rootless / `USER` no-root** en el Dockerfile. Dropea capabilities (`--cap-drop=ALL`, añade solo lo
  imprescindible). Nada de `--privileged`.
- **Seccomp + AppArmor/SELinux**: perfil que bloquee syscalls que no usas. Reduce mucho la superficie de escape.
- **Read-only rootfs** + `tmpfs` para scratch; el modelo no escribe el sistema.
- **GPU passthrough con NVIDIA Container Toolkit**, no `--privileged`. namespaces + cgroups acotan recursos.
- **Parchea runc**: nov-2025 trajo CVE-2025-31133/52565/52881 (escape vía mounts en creación). Mantén runtime al día;
  imágenes/Dockerfiles no confiables son justamente el vector.

## Checklist de despliegue
1. `USER` no-root + `cap-drop=ALL` + seccomp. 2. rootfs read-only. 3. Egress allowlist (bucket+webhook). 4.
Bloqueo de IPs internas/metadata. 5. Validación SSRF con pin de IP. 6. Secretos con scope mínimo y rotables.
7. Pesos verificados ([[247-model-supply-chain-pickle-safetensors]]) antes de cargar.

Cruza con [[27-seguridad-apps-owasp]] y [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]].
