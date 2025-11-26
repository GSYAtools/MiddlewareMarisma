{ CALL ar_marisma.actualizarExitoControles(:idSubproyecto) }

SELECT ar_marisma.func_calculoControles(:idSubproyecto, :idControl, :idAgrupacion);

SELECT ar_marisma.obtenerControlAuditoriaExito(:idSubproyecto, :idControl, :idAgrupacion);

SELECT ar_marisma.obtenerControlAuditoriaExito1(:idSubproyecto, :idControl, :idAgrupacion);

{ CALL ar_marisma.sp_actualizarExitoArbol(:idSubproyecto) }

{ CALL ar_marisma.sp_actualizarExitoControl(:idSubproyecto, :idControl, :idAgrupacion, :deleted) }

{ CALL ar_marisma.sp_analisisRiesgo(:sub) }

{ CALL ar_marisma.sp_calcularExitoProyecto(:idProyecto) }

{ CALL ar_marisma.sp_createExitoControl(:idSubproyecto, :idAgrupacion, :idEsquema) }

{ CALL ar_marisma.sp_planTratamiento(:sub) }