# 15 · Playbooks por rubro

> **Fuentes:** los papeles exactos salen de `src/lib/catalogo.ts` (predicados `aplica` y ejes de riesgo,
> verificado jun-2026) y de la referencia `02-cumplimiento-colombia.md`; los rangos de plata (food cost,
> arriendo, margen, rotación) son ORIENTATIVOS de `economist_lushows` (playbooks 100/104/105/103) —
> cambian por ciudad. AVIS **no inventa**: fechas/montos legales del catálogo; lo municipal se confirma
> con la entidad; los % financieros son referencia para conversar, no verdad fiscal.

## Cómo leer esto
A casi todo negocio formal con local y empleados le aplican los **transversales** (no se repiten por rubro):
matrícula mercantil (vence **31 de marzo**), RUT, facturación electrónica DIAN, SG-SST + exámenes + PILA
(si ≥1 empleado), uso de suelo y bomberos (si local), y **SAYCO-ACINPRO si pone música**. Abajo va lo
**extra** que enciende cada rubro y dónde se le va la plata.

## Tabla maestra por rubro

| Rubro | Papeles EXTRA clave (sobre los transversales) | Dónde se va la plata (referencia) |
|---|---|---|
| **Restaurante / cafetería** | Concepto sanitario · Plan de saneamiento* · Plan de capacitación* · Manipulación de alimentos (1 año/persona) · SAYCO si música | Food cost 28–35% · nómina 25–35% (**Prime Cost ≤65%**) · arriendo ≤8–10% · comisión apps 20–35% |
| **Tienda / minimercado** | (transversales) · SAYCO si música · *licor → ver bar* | Margen bruto 25–50% · arriendo 5–12% · rotación inventario · inventario muerto 20–40% |
| **Peluquería / barbería / estética** | Manual de bioseguridad + concepto sanitario* (Res. 2827/2006) | Arriendo · silla productiva (ocupación) · insumos · % comisión a estilistas |
| **Ferretería** | (transversales) · uso de suelo y bomberos pesan (inflamables/bodega) | Margen bajo-medio · capital atrapado en stock lento · rotación · robo/merma |
| **Droguería / farmacia** | Director técnico (regente/QF con tarjeta) + concepto sanitario (Dec. 2200/2005) | Margen regulado bajo en medicamentos · rotación · vencimientos · sueldo del regente |
| **Bar / licorera / discoteca** | Licor legal con estampilla + impuesto al consumo** (Ley 1816/2016) · SAYCO casi seguro · sanitario si vende comida | Costo de bebida · arriendo · licencias/seguridad · contrabando = decomiso |
| **Taller / lavadero** | Permiso de vertimientos + aceites usados/RESPEL (Dec. 1076/2015) · bomberos | Repuestos · mano de obra · disposición de residuos · garantías mal cobradas |
| **Hotel / hostal** | Renovación RNT (**1-ene a 31-mar**, gratis) · sanitario si da alimentos · SAYCO zonas comunes | Ocupación % (RevPAR) · nómina · arriendo/inmueble · OTAs comisión 15–20% |
| **Panadería** | Igual a alimentos: sanitario · saneamiento* · capacitación* · manipulación · INVIMA si marca propia*** | Food cost (harina/levadura/huevo volátil) · merma de producto fresco · energía (hornos) |
| **Papelería / misceláneo** | (transversales) · SAYCO si música · INVIMA si fabrica/empaca marca propia*** | Margen bajo y muchos SKUs · rotación dispar · inventario muerto · temporada escolar |

\* *Lo genera AVISPA'O.* \** *Lo tramita el cliente, AVIS guía.* \*** *Solo si fabrica/vende con marca propia (NSO INVIMA).*

## Notas por rubro

**Restaurante / cafetería.** El eje es `manejaAlimentos` → enciende los 4 papeles sanitarios. La trampa #1
no es legal, es el **arriendo caro + food cost descuidado**: con prime cost sobre 70% no queda para nada. *"Parce, su sanitario y la manipulación de alimentos los tengo en la mira — pero ojo: si el arriendo le
pasa del 10% de lo que vende, ese local se lo está comiendo. Súbame el certificado y le aviso cuando renueve."*

**Tienda / minimercado.** Casi puro transversal. Si vende cerveza/licor, AVIS marca `vendeLicor` y suma el
licor legal. Vive de **rotación**, no de margen. *"Su tienda solo necesita los papeles básicos al día. La
plata se le escapa en lo que no rota: mándeme su lista y miramos qué liquidar antes de que envejezca."*

**Peluquería / barbería / estética.** `esEstetica` enciende el manual de bioseguridad (lo armo yo) + visita
sanitaria. *"El manual de bioseguridad se lo dejo listo para la visita. Y cuide la silla vacía: cada hora
sin cliente es plata quieta — armemos agenda."*

**Ferretería.** Sin papel especial, pero **bomberos y uso de suelo pesan** por inflamables y bodega. *"Lo suyo es tener bomberos y uso de suelo impecables. Y revise el stock dormido: tornillo que no rota es
plata clavada en el estante."*

**Droguería / farmacia.** `esDrogueria` exige **director técnico** (regente o químico farmacéutico con
tarjeta) permanente, o la sellan. *"Sin director técnico vigente la Secretaría se la cierra — ¿lo tiene?
Le ayudo a tener concepto y regente en regla, y vigilamos vencimientos para que no pierda inventario."*

**Bar / licorera / discoteca.** `vendeLicor` + casi siempre `poneMusica`. El **licor con estampilla** es
sagrado: contrabando = decomiso + sanción hasta 10× el impuesto. *"Venda solo licor con estampilla, esa no
se la perdonan. Y SAYCO va sí o sí por la música — le saco el valor del simulador de la OSA."*

**Taller / lavadero.** `impactoAmbiental` enciende **vertimientos + aceites usados (RESPEL)**: verter aceite
al suelo o al agua está prohibido. *"Necesita trampa de grasas, permiso de vertimientos y entregar el
aceite usado a un gestor autorizado. Yo le gestiono el permiso; usted no bote nada al desagüe."*

**Hotel / hostal.** `esTurismo` + formalizado → **RNT** que se renueva entre el **1 de enero y el 31 de
marzo**; el 1 de abril se suspende solo. *"Renueve el RNT antes del 31 de marzo o no puede operar legal
desde abril. Es gratis y virtual — yo se lo gestiono y le pongo el recordatorio."*

**Panadería.** Igual a alimentos. Si saca marca propia empacada, suma **INVIMA**. La plata se va en **merma
de producto fresco** y energía de hornos. *"Manejamos los mismos papeles de alimentos. Si va a vender su
pan empacado con marca, toca notificación INVIMA — yo se la gestiono cuando llegue ese momento."*

**Papelería / misceláneo.** Transversales + INVIMA solo si fabrica/empaca con marca propia. Muchos SKUs, margen
flaco. *"Sus papeles son los básicos. El reto es el surtido: tanta referencia que no rota es plata dormida —
le ayudo a ver cuáles mueven y cuáles no."*

> **Roadmap:** valores en pesos de cada sanción por año vigente · particularidades por ciudad
> (Bogotá/Medellín/Cali/Barranquilla) · más rubros (fruver, restaurante-bar mixto, dark kitchen, gimnasio) ·
> plantilla de P&L por rubro que AVIS arme con los números reales del dueño · cruce de cada papel con su
> recordatorio automático de renovación.
