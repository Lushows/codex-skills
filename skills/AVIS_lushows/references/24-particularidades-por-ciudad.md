# 24 · Particularidades por ciudad

> **Nunca inventes tarifas, fechas ni procesos por municipio.** Cada alcaldía, cuerpo de bomberos y secretaría de salud fija lo suyo y lo cambia. El valor de AVIS aquí es saber **a QUÉ entidad acudir** y decir "ese dato lo confirmo con ellos" — no recitar un número que puede estar mal.

## Por qué estos trámites cambian de ciudad a ciudad
Cuatro trámites son **municipales** (o departamentales), no nacionales. La ley es la misma en todo el país, pero **cada territorio fija su propia tarifa, fecha y proceso**:

| Trámite | Quién lo regula localmente | Qué cambia por ciudad |
|---|---|---|
| **Uso de suelo** | Alcaldía / Secretaría de Planeación (según el POT) | Qué actividad se permite en cada zona, costo del certificado, si es online |
| **Concepto de bomberos** | Cuerpo de Bomberos del municipio | Tarifa (suele ir por metraje/riesgo), vigencia, si visitan o es virtual |
| **Concepto sanitario** | Secretaría de Salud municipal/distrital | Cómo se agenda la visita, vigencia que asignan, requisitos previos |
| **ICA (Industria y Comercio)** | Secretaría de Hacienda municipal | Tarifa por actividad (mil x mil), si es bimestral/anual, plataforma de pago |

> Nacional y **no** cambia por ciudad: matrícula mercantil (Cámara), RUT y factura electrónica (DIAN), RNT (MinCIT), SG-SST (Min. Trabajo), SAYCO-ACINPRO (OSA). Esos van en `02-cumplimiento-colombia.md`.

**Regla de oro para AVIS:** la matrícula la renuevas el 31 de marzo en todo el país; **bomberos, sanitario, uso de suelo e ICA dependen de tu municipio**, así que ahí AVIS nombra la entidad y ofrece confirmar el dato vigente con ellos.

## A qué entidad acudir por ciudad

### Uso de suelo
| Ciudad | Entidad | Frase de AVIS |
|---|---|---|
| Bogotá | Secretaría Distrital de Planeación (consulta del POT por dirección) | "El uso de suelo lo valida Planeación Distrital; lo confirmo con ellos para tu dirección." |
| Medellín | Curaduría Urbana / Planeación municipal | "Eso lo revisa Planeación de Medellín según el POT; confirmamos el dato con ellos." |
| Cali | Departamento Administrativo de Planeación Municipal | (confirmar tarifa y proceso con la entidad del municipio) |
| Barranquilla | Secretaría de Planeación Distrital | (confirmar con la entidad del municipio) |
| Bucaramanga | Secretaría de Planeación municipal | (confirmar con la entidad del municipio) |
| Cartagena | Secretaría de Planeación Distrital | (confirmar con la entidad del municipio) |

### Concepto de bomberos
| Ciudad | Entidad | Frase de AVIS |
|---|---|---|
| Bogotá | Unidad Administrativa Especial Cuerpo Oficial de Bomberos de Bogotá | "El concepto de bomberos lo expide el Cuerpo de Bomberos de Bogotá; la tarifa va por tu local, la confirmo con ellos." |
| Medellín | Cuerpo de Bomberos de Medellín | (confirmar tarifa/vigencia con la entidad del municipio) |
| Cali | Cuerpo de Bomberos Voluntarios de Cali | (confirmar con la entidad del municipio) |
| Barranquilla | Cuerpo de Bomberos de Barranquilla | (confirmar con la entidad del municipio) |
| Bucaramanga | Cuerpo de Bomberos de Bucaramanga | (confirmar con la entidad del municipio) |
| Cartagena | Cuerpo de Bomberos de Cartagena | (confirmar con la entidad del municipio) |

### Concepto sanitario
| Ciudad | Entidad | Frase de AVIS |
|---|---|---|
| Bogotá | Secretaría Distrital de Salud (visitas por las Subredes/hospitales) | "El concepto sanitario lo da la Secretaría de Salud de Bogotá tras la visita; confirmamos la fecha con ellos." |
| Medellín | Secretaría de Salud de Medellín | "Eso lo maneja la Secretaría de Salud de tu municipio; confirmamos la fecha con ellos." |
| Cali | Secretaría de Salud Pública Municipal | (confirmar vigencia con la entidad del municipio) |
| Barranquilla | Secretaría de Salud Distrital | (confirmar con la entidad del municipio) |
| Bucaramanga | Secretaría de Salud y Ambiente | (confirmar con la entidad del municipio) |
| Cartagena | DADIS (Departamento Administrativo Distrital de Salud) | (confirmar con la entidad del municipio) |

### ICA (Industria y Comercio)
| Ciudad | Entidad | Frase de AVIS |
|---|---|---|
| Bogotá | Secretaría Distrital de Hacienda (ICA bimestral/anual según ingresos) | "El ICA se paga a la Secretaría de Hacienda de Bogotá; la tarifa depende de tu actividad, la confirmo con ellos." |
| Medellín | Secretaría de Hacienda de Medellín | (confirmar tarifa por actividad con la entidad del municipio) |
| Cali | Departamento Administrativo de Hacienda Municipal | (confirmar con la entidad del municipio) |
| Barranquilla | Secretaría de Hacienda Distrital (Gerencia de Gestión de Ingresos) | (confirmar con la entidad del municipio) |
| Bucaramanga | Secretaría de Hacienda municipal | (confirmar con la entidad del municipio) |
| Cartagena | Secretaría de Hacienda Distrital | (confirmar con la entidad del municipio) |

## Cómo AVIS lo dice bien (plantilla)
1. **Nombra la entidad correcta** del municipio del cliente: "para tu local en Medellín, eso lo maneja la Secretaría de Salud de Medellín".
2. **Ofrece confirmar, no inventes:** "la tarifa y la vigencia me las confirma la entidad, así no te doy un dato viejo".
3. **Si no sabes la entidad exacta de un municipio pequeño:** "es la alcaldía / el cuerpo de bomberos de tu municipio; ubico el contacto exacto y te lo paso". Nunca un número inventado.
4. **Distingue nacional vs municipal:** "la matrícula es 31 de marzo en todo el país; lo de bomberos sí depende de tu ciudad".

> **Roadmap:** cargar tarifas, vigencias y fechas reales por ciudad (empezando por Bogotá/Medellín/Cali) en datos verificados como `catalogo.ts`, con link/oficina y plataforma de pago de cada entidad, para que AVIS dé el dato exacto en vez de remitir a confirmar.
