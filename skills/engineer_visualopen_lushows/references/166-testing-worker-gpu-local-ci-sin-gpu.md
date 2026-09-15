# 166 · Testear el worker GPU (smoke local + lógica en CI sin GPU)

> El bug que costó horas NO estaba en el modelo: estaba en `num_segments`, en la normalización del audio
> y en el handler reusando el input anterior. Esa lógica se testea SIN GPU, rápido y en CI. El modelo
> pesado se mockea. La GPU solo entra en un smoke ocasional, no en cada push.

## La pirámide para un worker GPU
```
        ╱ smoke real en GPU (1 input mínimo→MP4) · manual / nightly · caro
      ╱   integración del handler (payload real, modelo MOCKEADO) · CI sin GPU
    ╱     unit de la lógica pura (num_segments, normalización, IO) · CI sin GPU · milisegundos
```
El 80% de los bugs de [[111-longcat-avatar-runpod-produccion]] vivían en la base de la pirámide. Cruza con [[26-testing-a-fondo-python]].

## Separar lógica de GPU (la decisión de diseño que habilita todo)
Si el cómputo del modelo está enredado con el parsing del input y el cálculo de segmentos, no puedes testear nada sin GPU. Extrae funciones **puras**:
```python
def compute_num_segments(audio_seconds: float, sec_per_seg: float = 3.0) -> int:
    return max(1, math.ceil(audio_seconds / sec_per_seg))

def normalize_audio(src: Path, dst: Path) -> None:        # ffmpeg → WAV 16k mono
    run(["ffmpeg","-y","-i",str(src),"-ar","16000","-ac","1",str(dst)])
```
Estas se testean sin tocar la GPU. El bug del "mp3 renombrado .wav → num_segments=1 → video de 3s con audio de 13s" ([[114-video-segmentado-largo-clip]]) es UN test:
```python
def test_segments_audio_largo():
    assert compute_num_segments(13.0) == 5      # no 1
def test_segments_minimo_uno():
    assert compute_num_segments(0.4) == 1
```

## Mockear el modelo pesado
El handler no debe importar torch a nivel de módulo si quieres que CI sin GPU lo cargue. Inyecta el inferidor o mockéalo:
```python
def test_handler_payload_real(monkeypatch, tmp_path):
    monkeypatch.setattr(infer, "run_model",
        lambda **kw: write_dummy_mp4(tmp_path/"out.mp4"))   # no GPU
    out = handler({"input": {"input_image_url": IMG, "input_audio_url": AUD,
                             "prompt": "static camera"}})
    assert out["output_video_url"].endswith(".mp4")
```
Esto prueba TODO el flujo del handler —descarga de inputs, normalización, armado de `{prompt, cond_image, cond_audio:{person1:aud}}`, subida a R2, formato de respuesta— sin un solo FLOP de GPU.

## Tests de los bugs reales que ya pagamos (regresión)
- **Worker caliente reusa input previo:** test que llama el handler 2 veces con imágenes distintas y verifica que el 2º output corresponde a la 2ª imagen (mock que devuelve hash del input). Atrapa el `if os.path.exists(f): return f`.
- **Limpieza IN/OUT por job:** test que verifica `shutil.rmtree` de los dirs antes/después.
- **Audio no-wav:** test con un .mp3 renombrado .wav → debe normalizar o fallar ruidoso, nunca producir 1 segmento silencioso.
- **Respuesta de error:** input inválido → el handler devuelve `{error}` estructurado, no crashea el worker.

## Fixtures: imagen y audio mínimos en el repo
Commitea assets diminutos (no 44GB de pesos):
```python
@pytest.fixture
def tiny_png(tmp_path):          # PIL 64×64, ~1KB
    p = tmp_path/"f.png"; Image.new("RGB",(64,64),"gray").save(p); return p
@pytest.fixture
def tiny_wav(tmp_path):          # 1s silencio 16k mono, ~32KB
    p = tmp_path/"a.wav"; sf.write(p, np.zeros(16000), 16000); return p
```
Sírvelos por HTTP local (`pytest-httpserver`) para ejercitar la ruta de descarga del handler sin red externa.

## CI sin GPU (GitHub Actions, runner normal)
```yaml
- run: pip install -r requirements-test.txt   # SIN torch+cuda; usa torch CPU o mock
- run: pytest tests/ -m "not gpu"             # lógica + handler mockeado
```
Marca el smoke real con `@pytest.mark.gpu` y déjalo fuera de PR; córrelo nightly en un Pod RunPod o manual. **Importa lazy** torch/el modelo dentro de la función, no en el top del módulo, para que el import de CI no falle por falta de CUDA.

## Smoke real en GPU (antes de release)
Un input mínimo (tiny_png + 2s de audio real) → render completo → asserts: el MP4 existe, duración ≈ audio, >0 bytes, abre con ffprobe, ≥1 frame con cara (face-detect). Es el último gate de [[118-checklist-pre-lanzamiento-render-gpu]]: si el smoke pasa y el golden-set de [[164-evals-calidad-avatar-video]] no regresa → release.

## Gotchas
1. `import torch` en el top del handler → CI sin GPU revienta al colectar. Lazy import.
2. Mock que devuelve siempre el mismo MP4 → no atrapa el bug de "reusa input". Haz que el mock dependa del input.
3. Smoke en GPU en cada PR = caro y lento; déjalo nightly/manual.
4. Fixtures pesados (imágenes grandes, wavs largos) inflan el repo y ralentizan CI — usa los más pequeños que ejerciten el código.
5. No testear la **ruta de error** → un input malo tumba el worker en producción en vez de devolver `{error}`.

**Fuentes:** docs.pytest.org · github.com/csernazs/pytest-httpserver · ffmpeg.org/ffmpeg.html (normalización audio).
