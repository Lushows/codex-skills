# 02 · Cumplimiento de pymes en Colombia (el dominio de AVIS)

> **Fuente de verdad en código:** `src/lib/catalogo.ts` (19 obligaciones verificadas jun-2026, cada
> una con `entidad`, `vence`, `siNoCumple`, `fuente` y un predicado `aplica`). AVIS toma de ahí las
> fechas/montos/obligatoriedad EXACTOS — **nunca inventa**. La capa Gemini se acomoda al rubro encima,
> marcando lo no verificado como "(por confirmar)".

## Cómo decide AVIS qué papeles pedirle a un negocio
Por el **perfil** del negocio se encienden "ejes de riesgo" (atributos), y cada obligación aplica según
esos atributos. El perfil: `tipoNegocio`, `ciudad`, `formalizado`, `estructura` (natural|sas),
`localFisico`, `poneMusica`, `manejaAlimentos`, `numEmpleados`, `fabricaProductos`, y flags de rubro.

**Detección de rubro (regex sobre lo que dijo el dueño) → enciende el eje:**
- **estética/belleza:** pelu, barber, belleza, estética, spa, uñas, salón, cosmet, manicur, maquillaje
- **turismo:** hotel, hostal, hospedaje, alojamiento, turismo, agencia de viajes, posada, finca, glamping, tour, cabaña
- **droguería:** droguería, farmacia, botica
- **licor:** bar, licor, discoteca, taberna, estanco, cantina, cervecería, aguardiente, nightclub
- **impacto ambiental (taller/lavadero):** taller, mecánica, lavadero, autolavado, montallantas, latonería, lubricadora, cambio de aceite
- **transporte:** transporte, acarreo, mudanza, mensajería, carga, taxi, buseta, colectivo, encomienda
- **salud:** consultorio, médico, odontología, dentista, laboratorio clínico, fisioterapia, optometría, IPS, EPS
- **educación:** jardín infantil, colegio, preescolar, guardería, institución educativa, liceo

Un negocio mixto (ej. "cafetería-bar") suma ejes: alimentos + licor + música. AVIS puede marcar un eje
a mano en el onboarding para negocios que el rubro no delata.

## Las 19 obligaciones (verificadas jun-2026)

### Transversales (a casi todo negocio formal o con local/empleados)
| Obligación | Entidad | Vence / frecuencia | Si no cumple | Aplica si |
|---|---|---|---|---|
| **Renovación matrícula mercantil** | Cámara de Comercio | **31 de marzo** cada año | Sanción Supersociedades hasta 17 SMLMV + matrícula inactiva | formalizado |
| **RUT actualizado** | DIAN | Cuando cambie un dato | Sanciones DIAN, no puede facturar | formalizado |
| **Facturación electrónica** | DIAN | Implementar (hasta 2 meses tras Régimen Simple) + uso continuo | No puede facturar legal; sanciones | formalizado |
| **SG-SST + autoevaluación** | Min. Trabajo (SGRL) | Anual | Multa micro hasta 5 SMMLV | ≥1 empleado |
| **Exámenes médicos ocupacionales** | IPS/médico ocupacional | Ingreso / periódico / retiro (egreso ≤5 días hábiles) | Multa hasta 2.455 UVT | ≥1 empleado |
| **Seguridad social (PILA)** | Salud/Pensión/ARL | Mensual (según dígito) | Sanciones + responsabilidad por accidentes | ≥1 empleado |
| **Uso de suelo conforme** | Alcaldía/Planeación | Al abrir / si cambia | Cierre (Ley 232: 30 días → suspende → cierra) | local físico |
| **Concepto de bomberos** | Bomberos (municipal) | Anual (varía por municipio) | Multas/cierre | local físico |
| **Licencia SAYCO-ACINPRO (música)** | Organización Sayco Acinpro (OSA) | Anual | Pueden sellar/cerrar (Ley 232); valor del simulador OSA | pone música |

### Rubro alimentos (restaurante, fruver, cafetería, panadería…)
| Obligación | Entidad | Notas | Cómo se obtiene |
|---|---|---|---|
| **Concepto sanitario** | Secretaría de Salud (mun.) | Tras visita; vigencia según la visita | gestiona AVISPA'O |
| **Plan de saneamiento básico** | (documento en el local) | Limpieza+desinfección, residuos, control de plagas | **lo genera AVISPA'O** |
| **Plan de capacitación del personal** | (documento en el local) | Metodología, cronograma, temas | **lo genera AVISPA'O** |
| **Certificado de manipulación de alimentos** | Capacitador autorizado | Vigencia 1 año, por persona que toca comida | gestiona AVISPA'O |

### Por rubro específico (se encienden por el eje de riesgo)
| Obligación | Rubro | Entidad | Si no cumple |
|---|---|---|---|
| **Manual bioseguridad + concepto sanitario** | estética/belleza | Secretaría de Salud | Concepto desfavorable/cierre. *Lo genera AVISPA'O.* (Res. 2827/2006) |
| **Renovación RNT** | turismo + formalizado | MinCIT/Confecámaras | Suspensión automática desde 1-abr. Vence **1-ene a 31-mar**, virtual y gratis |
| **Director técnico + concepto sanitario** | droguería | Secretaría de Salud | Cierre. Regente/químico farmacéutico con tarjeta (Dec. 2200/2005) |
| **Licor legal con estampilla + impuesto consumo** | vende licor | Hacienda Departamental | Cierre, decomiso, sanción hasta 10× el impuesto evadido (Ley 1816/2016). *Lo tramita el cliente.* |
| **Registro/Notificación sanitaria INVIMA** | fabrica con marca propia | INVIMA | No comercializa; decomiso. Por producto |
| **Permiso de vertimientos + aceites usados (RESPEL)** | taller/lavadero | CAR + Secretaría de Ambiente | Multas ambientales/cierre (Dec. 1076/2015) |
| **Habilitación + tarjeta de operación** | transporte público | Min. Transporte | Inmovilización. Tarjeta cada 2 años (Dec. 1079/2015). *Lo tramita el cliente.* |
| **Habilitación REPS + residuos biosanitarios** | salud | Secretaría de Salud/REPS | No presta servicios; cierre (Res. 3100/2019) |
| **Licencia de funcionamiento (PEI)** | educación | Secretaría de Educación | Cierre. Radicar 6 meses antes (Dec. 1075/2015) |

## Cómo se resuelve cada papel (`comoObtener`)
- **`genera_avispao`** → lo PRODUCE AVISPA'O (servicio): plan de saneamiento, plan de capacitación,
  SG-SST, manual de bioseguridad. AVIS ofrece "yo te lo armo y te lo dejo listo".
- **`gestiona_avispao`** → AVISPA'O hace el trámite o conecta con el contacto exacto.
- **`tramita_cliente`** → lo hace el cliente (con su contador/entidad) y AVIS guía con el paso exacto.
  (Licor legal y habilitación de transporte son `tramita_cliente`.)

## Reglas al hablar de cumplimiento (críticas)
1. **Fechas/montos exactos solo de `catalogo.ts`.** Lo municipal (bomberos, sanitario, uso de suelo)
   suele decir "confirmar con la entidad del municipio" — dilo así, no inventes una fecha.
2. **Personaliza por rubro y nombre** ("para tu restaurante La Esquina, en Tocancipá…").
3. **Por cada papel:** ¿lo tienes? → SÍ: súbelo, lo guardo y te aviso al renovar. NO: paso exacto, o
   AVISPA'O te lo gestiona/genera.
4. **Sin sermones de formalización.** Si no es formalizado, no lo regañes; muéstrale el valor.
5. **SMLMV/SMMLV/UVT/SMLMV** son unidades que cambian cada año — si necesitas el valor en pesos,
   confírmalo del año vigente (no lo memorices).

> **Roadmap de este archivo:** valor en pesos de cada sanción por año · particularidades por ciudad
> (Bogotá/Medellín/Cali/Barranquilla) · Régimen Simple vs común · ICA municipal · retención en la
> fuente · calendario tributario DIAN del año · pasos exactos (links/oficinas) para cada trámite.
