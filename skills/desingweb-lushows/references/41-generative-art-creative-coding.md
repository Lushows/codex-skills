# 41 — Arte generativo & creative coding (la capa atmosférica)

La capa generativa separa un sitio "bonito" de uno que *respira*. No es decoración, es atmósfera — pero el 95% de las demos son ruido sin intención. **Léelo cuando quieras visuales artísticos/generativos** (partículas, flow fields, fondos vivos). Pareja de 07, 08, 38, 39. Código vanilla canvas/p5/shaders.

## 1. Particle systems (canvas 2D)

Patrón: clase `Particle` + array que el loop actualiza/dibuja. Reglas de perf: cap de partículas, **object pooling** (recicla con `reset()`, no crees/destruyas), **sprite cache del glow** (evita `shadowBlur` por partícula), trail con `fillRect` semi-transparente (no `clearRect`+globalAlpha).
```js
class Particle{
  constructor(){this.reset(true)}
  reset(init){this.x=Math.random()*W;this.y=init?Math.random()*H:-10;this.vx=0;this.vy=0;this.r=Math.random()*1.8+.4}
  update(){
    this.vx+=0.002; this.vy+=0.004;                 // wind + gravity
    if(mouse.active){const dx=this.x-mouse.x,dy=this.y-mouse.y,d2=dx*dx+dy*dy;
      if(d2<14000){const f=(14000-d2)/14000*.6,d=Math.sqrt(d2)||1;this.vx+=dx/d*f;this.vy+=dy/d*f;}} // repulsión (resta=atraer)
    this.vx*=.96;this.vy*=.96;                       // damping = sensación de fluido
    this.x+=this.vx;this.y+=this.vy;
    if(this.y>H+10||this.x>W+10||this.x<-10)this.reset(false);
  }
}
function makeGlow(size,color){const c=document.createElement('canvas');c.width=c.height=size;const g=c.getContext('2d');
  const gr=g.createRadialGradient(size/2,size/2,0,size/2,size/2,size/2);gr.addColorStop(0,color);gr.addColorStop(1,'rgba(255,255,255,0)');g.fillStyle=gr;g.fillRect(0,0,size,size);return c;}
function loop(){
  ctx.fillStyle='rgba(8,12,10,0.18)';ctx.fillRect(0,0,W,H);   // trail fade
  ctx.globalCompositeOperation='lighter';                     // glow aditivo
  for(const p of particles){p.update();ctx.drawImage(glow,p.x-p.r*8,p.y-p.r*8,p.r*16,p.r*16);}
  ctx.globalCompositeOperation='source-over';requestAnimationFrame(loop);
}
```
**Constellation** (líneas entre partículas cercanas) es O(n²) → cap 120 o spatial grid. **Dust/esporas atmosférico** (caso BIO-SETA): partículas lentas, minúsculas, deriva con seno, opacidad baja, respawn abajo (`this.y-=0.15; this.x+=Math.sin(this.y*.01+seed)*.3`).

## 2. Noise & flow fields — el corazón orgánico

**Por qué noise:** `Math.random()` salta caótico; **Perlin/Simplex** es *coherente* (puntos cercanos → valores cercanos) = lo "orgánico". Simplex > Perlin (más suave, sin artefactos). Lib `simplex-noise`: `const noise3D=createNoise3D()`.
**Flow field** (la firma Tyler Hobbs/Fidenza): cada celda guarda un ángulo del noise; las partículas siguen el ángulo de su celda → trazan ríos visuales:
```js
const SCALE=0.0016, STEP=1.2; let t=0;
class Flow{ constructor(){this.x=Math.random()*W;this.y=Math.random()*H;this.px=this.x;this.py=this.y}
  step(){ const a=noise3D(this.x*SCALE,this.y*SCALE,t)*Math.PI*2.5; this.px=this.x;this.py=this.y;
    this.x+=Math.cos(a)*STEP;this.y+=Math.sin(a)*STEP;
    if(this.x<0||this.x>W||this.y<0||this.y>H){this.x=Math.random()*W;this.y=Math.random()*H;this.px=this.x;this.py=this.y} } }
function flowLoop(){
  ctx.fillStyle='rgba(10,14,12,0.04)';ctx.fillRect(0,0,W,H);    // trail bajísimo acumula como tinta
  ctx.strokeStyle='rgba(120,200,160,0.08)';ctx.beginPath();
  for(const a of agents){a.step();ctx.moveTo(a.px,a.py);ctx.lineTo(a.x,a.y);}ctx.stroke();
  t+=0.0008;requestAnimationFrame(flowLoop);
}
```
`*2.5` = más turbulencia; `*1` = curvas suaves Fidenza. **fBm** (textura natural): suma octavas `v+=amp*noise; freq*=2; amp*=.5`. **Domain warping** (iQuilez, look líquido/marmolado): evalúa noise en `p+fbm(p)` → `fbm(x+fbm(x,y)*40, y+...)` (el truco detrás de los mesh gradients que parecen humo).

## 3. Fondos & patterns generativos

**Mesh gradient animado** (barato y elegante): blobs radiales moviéndose con noise + `filter:blur(60px)` en CSS → look Stripe/Linear.
**Blobs orgánicos** (Catmull-Rom/quadratic entre puntos perturbados por noise): radio `r*(1+noise*0.35)` por ángulo, dibuja con `quadraticCurveTo`.
**Seeded randomness** ("cada reload distinto pero reproducible") — `Math.random` no acepta seed, usa **mulberry32**:
```js
function mulberry32(s){return function(){s|=0;s=s+0x6D2B79F5|0;let t=Math.imul(s^s>>>15,1|s);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;}}
const rng=mulberry32(seed);  // guarda el seed en ?seed= → versión compartible/colectible
```
**Palette discipline** (no random RGB): hue base + relaciones armónicas (análogos ±30°, complementario +180°), saturación/luz acotadas en HSL.

## 4. p5.js para diseñadores

**p5 vs raw canvas:** p5 para prototipar rápido / API rica (vectors, noise, WebGL fácil); raw canvas para producción (cero dependencias, control de perf). En un hero, **instance mode** (no contamina global):
```js
new p5(p=>{ let agents=[];
  p.setup=()=>{const c=p.createCanvas(p.windowWidth,p.windowHeight);c.parent('hero-bg');c.style('position','fixed');c.style('inset','0');c.style('z-index','-1');
    for(let i=0;i<1200;i++)agents.push(p.createVector(p.random(p.width),p.random(p.height)));};
  p.draw=()=>{ if(matchMedia('(prefers-reduced-motion: reduce)').matches){p.noLoop();return;}
    p.background(10,14,12,10);p.stroke(120,200,160,18);
    for(const v of agents){const a=p.noise(v.x*.002,v.y*.002,p.frameCount*.002)*p.TWO_PI*2;
      const nx=v.x+p.cos(a)*1.4,ny=v.y+p.sin(a)*1.4;p.line(v.x,v.y,nx,ny);v.set(nx,ny);
      if(nx<0||nx>p.width||ny<0||ny>p.height)v.set(p.random(p.width),p.random(p.height));} };
  p.windowResized=()=>p.resizeCanvas(p.windowWidth,p.windowHeight);
});
```
**Perf p5:** `pixelDensity(1)` en fondos, `noLoop()` si estático, `frameRate(30)` para atmósfera.

## 5. Tipografía generativa & SVG

**Kinetic type** ("el texto se deshace y reforma"): renderiza el texto en canvas offscreen, lee `getImageData`, por cada píxel opaco crea una partícula que vuelve a su posición (spring) tras ser perturbada por el mouse.
**SVG goo/metaballs** (filtro nativo, casi gratis en GPU) — fusiona divs/blobs como metaballs reales:
```html
<filter id="goo"><feGaussianBlur stdDeviation="8" result="b"/><feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -10"/></filter>
```
**Displacement líquido** en texto/SVG: `<feTurbulence>`+`<feDisplacementMap>`. **Generative line art** (look topográfico): líneas paralelas con cada punto desplazado por noise.

## 6. Art direction & taste (la línea entre arte y gimmick)

Lo que hace lo generativo **intencional, no "demo de ruido":**
- **Disciplina de paleta:** 2-4 colores de marca, no arcoíris; bajísima saturación para atmósfera (el generativo de élite es casi monocromo + 1 acento).
- **Composición & restraint:** deja espacio negativo; densidad variable > uniforme; un punto focal, no textura de borde a borde.
- **Relación con la marca:** para BIO-SETA → esporas a la deriva, micelio (flow field ramificado), verdes tierra. La forma debe *significar* algo del producto.
- **Movimiento lento** (`t+=0.0008`); rápido grita "demo". Atmósfera casi imperceptible.
- **Enriquece** en heroes/transiciones/loading; **distrae** detrás de párrafos/formularios/tablas.

### Generative anti-slop
ruido sin intención (random sobre random, screensaver 2003) · perf hogs (`shadowBlur` por partícula, miles sin cap, constellation O(n²) sin grid, DPR sin cap) · **ilegibilidad detrás de texto** (la causa #1 de amateur — si hay texto encima: opacidad ≤15%, blur o backdrop) · ignorar `prefers-reduced-motion` (frame estático) · no pausar en tab oculto (`document.hidden`) ni fuera de viewport (IntersectionObserver) · WebGL/Three (600kb) para 200 partículas (canvas 2D hasta ~3k; WebGL para decenas de miles o domain warping en tiempo real).
**Regla final:** el generativo premium se siente como atmósfera que casi no notas, pero que harías falta si la quitaran. Sutil, lento, de marca, performante, accesible. Si grita "mira mi efecto", es gimmick.
