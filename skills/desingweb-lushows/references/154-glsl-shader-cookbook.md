# 154 — GLSL shader cookbook (recetas con nombre)

**CRAFT, code-heavy.** Recetario copy-paste de efectos GLSL. Pareja de 08/38 (WebGL/R3F), 143 (image fx), 41 (generative), 148 (gradients). Regla de oro: **donde pondrías un `if`, usa `step`/`smoothstep`/`mix`; normaliza siempre `gl_FragCoord`; anima moviendo un uniform con GSAP, no recompilando el shader.** Convención de uniforms: `uTime`, `uResolution` (vec2 px), `uMouse` (vec2 px).

## 1. Fundamentals quick-ref

Pipeline: vertex (posiciona) → rasterizado → fragment (corre por píxel). Para efectos full-screen renderizas un quad/triángulo y la magia vive en el fragment.
```glsl
vec2 uv = gl_FragCoord.xy / uResolution.xy;                       // UV [0,1] para texturas
vec2 p = (gl_FragCoord.xy*2.0 - uResolution.xy) / uResolution.y;  // centrado aspect-correct [-1,1]
```
**Las 6 funciones clave:** `mix(a,b,t)` interpola, `step(edge,x)` 0/1 borde duro, `smoothstep(e0,e1,x)` transición suave (AA gratis), `fract(x)` repetición/tiling, `mod(x,n)` rejillas, `clamp(x,0,1)`. **Setup OGL (~10kb, recomendado):** `Renderer` + `Triangle` + `Program` con uniforms, loop que sube `uTime`. **Three:** `ShaderMaterial` con uniforms en `PlaneGeometry(2,2)` + cámara ortográfica.

## 2. Noise toolbox (el backbone orgánico)

```glsl
float random(vec2 st){ return fract(sin(dot(st.xy, vec2(12.9898,78.233)))*43758.5453123); }
float noise(vec2 st){ vec2 i=floor(st),f=fract(st); vec2 u=f*f*(3.0-2.0*f);
  float a=random(i),b=random(i+vec2(1,0)),c=random(i+vec2(0,1)),d=random(i+vec2(1,1));
  return mix(a,b,u.x)+(c-a)*u.y*(1.0-u.x)+(d-b)*u.x*u.y; }
// Simplex (Ashima snoise) para calidad — pegar la implementación canónica de github.com/ashima/webgl-noise
float fbm(vec2 st){ float v=0.0,a=0.5; mat2 rot=mat2(1.6,1.2,-1.2,1.6); // rota cada octava: rompe la rejilla
  for(int i=0;i<5;i++){ v+=a*noise(st); st=rot*st; a*=0.5; } return v; }
```
**Domain warping (IQ)** — alimenta fBm con fBm (nubes, mármol, humo, auroras): `vec2 q=vec2(fbm(p),fbm(p+vec2(5.2,1.3))); return fbm(p+4.0*q);`.

## 3. Surface effects

```glsl
float fresnel = pow(1.0 - max(dot(normalize(vNormal), normalize(vViewDir)), 0.0), 3.0); // rim light
vec3 palette(float t){ return 0.5+0.5*cos(6.28318*(vec3(1.0)*t+vec3(0.0,0.33,0.67))); }  // IQ cosine palette
float vig = smoothstep(0.9, 0.3, length(uv-0.5)); col *= vig;                            // vignette
// CHROMATIC ABERRATION: muestrea R/G/B en UVs desplazados radialmente
vec3 post = floor(col*5.0)/5.0;   // POSTERIZE (sin if)
col -= sin(uv.y*uResolution.y*1.5)*0.08;  // SCANLINES/CRT
```

## 4. Transitions & reveals (`mix(texA, texB, mask)` con `mask∈{0,1}`)

```glsl
// DISSOLVE (umbral sobre noise — burn/desintegración)
float mask = smoothstep(uProgress-0.05, uProgress+0.05, noise(uv*8.0));
// WIPE direccional: smoothstep(uProgress-0.1, uProgress, uv.x)
// IRIS desde centro: smoothstep(uProgress, uProgress-0.02, length((uv-0.5)*vec2(aspect,1.0)))
// PIXELATE transition: float px=mix(2.0,200.0,abs(uProgress-0.5)*2.0); vec2 puv=floor(uv*px)/px;
// DISPLACEMENT crossfade: warp UV con un map antes de mezclar (el de Codrops)
```

## 5. Patterns

```glsl
float voronoi(vec2 st){ vec2 i=floor(st),f=fract(st); float md=1.0;
  for(int y=-1;y<=1;y++) for(int x=-1;x<=1;x++){ vec2 g=vec2(float(x),float(y));
    vec2 o=vec2(random(i+g),random(i+g+vec2(31.0))); md=min(md,length(g+o-f)); } return md; }
// GRID: step(0.95, max(fract(uv*10.0).x, fract(uv*10.0).y))
// RIPPLE: sin(length(p)*20.0 - uTime*4.0)*0.5+0.5
// PLASMA: sin(p.x*10.+uTime)+sin(p.y*10.+uTime)+sin(length(p)*12.-uTime) → palette(plasma*0.1)
```

## 6. Performance & integración

`precision highp float;` (primera línea; `mediump` en móvil cuando el banding sea tolerable). **Sin branches** (la GPU ejecuta ambas ramas de un `if` divergente → usa `mix`/`step`). **`for` con límite constante** en WebGL1 (`i<5`, nunca `i<uOctaves`). Texture lookups son caros; no leas dentro de loops grandes; un `texture2D` dependiente cuesta más que uno directo. **Móvil:** reduce octavas de fBm (3 no 6), capa `dpr` a `min(devicePixelRatio,2)`, evita `pow`/`atan` en hot path (lentos en Mali/Adreno; `length()` usa sqrt → si solo comparas distancias usa `dot(v,v)`). **Uniforms desde GSAP:** `gsap.to(program.uniforms.uProgress, {value:1, duration:1.2, ease:'power2.inOut'})`. **¿Shader o CSS?** Si `filter`/`conic-gradient`/`mix-blend-mode`/`mask` lo resuelve → usa CSS (compositor, gratis, accesible); shader solo para noise procedural animado, distorsión de textura por píxel, transiciones con displacement, o partículas masivas.

## Shader anti-patterns — blacklist
**`if` con ramas divergentes** en el hot path (usa `step`/`mix`) · **`for` con límite dinámico** (`i<uCount`) en WebGL1 · **no normalizar `gl_FragCoord`** (se rompe en cada resolución/aspect) · **`pow`/`sin`/`atan`/`length` dentro de loops** sin necesidad · **dpr sin capar** (×3 en móvil quema GPU; `min(dpr,2)`) · **`texture2D` dependiente dentro de loop** (thrash de caché) · **fBm con 8+ octavas en móvil** (3-5 basta) · **borde duro con `step` donde se ve el aliasing** (usa `smoothstep`) · **olvidar `precision`** (comportamiento indefinido entre GPUs) · **reasignar el shader/material por frame** en vez de mover un uniform (recompila, stalls) · **WebGL solo para un gradiente estático** (CSS lo hace sin contexto GL).
