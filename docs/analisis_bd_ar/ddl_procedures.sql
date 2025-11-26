CREATE DEFINER=`ar_marisma`@`%` PROCEDURE `ar_marisma`.`actualizarExitoControles`( idSubproyecto INT )
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE idControl INT;
	DECLARE vExito float;
	DECLARE mediaAuditoria float;
	DECLARE mediaRama FLOAT;
	DECLARE padreRama INT;
    DECLARE existePadre INT;
    DECLARE porcentajeTotal FLOAT;
    declare porcentajeHoja FLOAT;
	DECLARE idObjetivo INT;
	DECLARE idDominio INT;
	DECLARE recorre CURSOR FOR 
      SELECT control_instanciado_id from control_auditoria ca left join agrupacion_checklist ag on ca.agrupacion_checklist_id = ag.id where ag.subproyecto_id = idSubproyecto ;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
   SET max_sp_recursion_depth=255;
   OPEN recorre;
   loop_recorre: LOOP  
	FETCH recorre INTO idControl;
    	select func_calculoControles(idSubproyecto, idControl) INTO vExito;

   		UPDATE control_auditoria ca, agrupacion_checklist ag
   		SET ca.exito = vExito
   		where ca.agrupacion_checklist_id = ag.id and ag.subproyecto_id = idSubproyecto and control_instanciado_id = idControl;

		select oa.objetivo_instanciado_id into idObjetivo 
		from control_auditoria ca, agrupacion_checklist ag, objetivo_auditoria oa
		where ca.agrupacion_checklist_id = idAgrupacion and ca.deleted=0 and ag.deleted=0 and ca.agrupacion_checklist_id = ag.id 
		and ag.subproyecto_id = idSubproyecto and ca.control_instanciado_id = idControl
		and oa.agrupacion_checklist_id = ag.id and oa.agrupacion_checklist_id = idAgrupacion and oa.agrupacion_checklist_id = ca.agrupacion_checklist_id
		and oa.deleted = 0 and oa.id = ca.objetivo_auditoria_id;

		update objetivo_auditoria oa
		inner join (
			select c.objetivoId, sum(c.exito)/count(c.id) as exi, sum(c.cobertura)/count(c.id) as cober from (
				SELECT ca.id as id, oi.id as objetivoId, ca.exito as exito, ca.cobertura as cobertura
				from control_auditoria ca
				inner join agrupacion_checklist agc on ca.agrupacion_checklist_id = agc.id and agc.subproyecto_id = idSubproyecto
				inner join control_instanciado ci on ci.id = ca.control_instanciado_id
				inner join objetivo_instanciado oi on oi.id = ci.objetivo_instanciado_id
				inner join dominio_instanciado di on di.id = oi.dominio_instanciado_id
				inner join respuesta re on agc.id = re.agrupacion_checklist_id
				inner join checklist_instanciado chk on chk.id = re.checklist_instanciado_id and chk.control_instanciado_id = ci.id
				where ca.agrupacion_checklist_id = idAgrupacion and re.aplica = 'SI' and ca.deleted=0 and ci.deleted=0 and oi.deleted=0 and di.deleted=0 
				and agc.deleted=0 and re.deleted=0 and chk.deleted=0
				group by ca.id
			) c where c.objetivoId = idObjetivo group by c.objetivoId
		) b on b.objetivoId = oa.objetivo_instanciado_id
		set oa.cobertura = b.cober, oa.exito = b.exi
		where oa.objetivo_instanciado_id = idObjetivo and oa.deleted = 0 and oa.agrupacion_checklist_id = idAgrupacion;

		select da.dominio_instanciado_id into idDominio 
		from objetivo_auditoria oa, dominio_auditoria da 
		where oa.objetivo_instanciado_id = idObjetivo and oa.deleted = 0 and oa.agrupacion_checklist_id = idAgrupacion
		and da.id = oa.dominio_auditoria_id and da.deleted = 0 and da.agrupacion_checklist_id = idAgrupacion and da.agrupacion_checklist_id = oa.agrupacion_checklist_id;

		update dominio_auditoria da
		inner join (
			select avg(b.ex) as exi, avg(b.ceb) as cober, b.dominioId from (
				select c.dominioId, c.objetivoId, sum(c.exito)/count(c.id) as ex, sum(c.cobertura)/count(c.id) as ceb from (
					SELECT ca.id as id, oi.id as objetivoId, di.id as dominioId, ca.exito as exito, ca.cobertura as cobertura
					from control_auditoria ca
					inner join agrupacion_checklist agc on ca.agrupacion_checklist_id = agc.id and agc.subproyecto_id = idSubproyecto
					inner join control_instanciado ci on ci.id = ca.control_instanciado_id
					inner join objetivo_instanciado oi on oi.id = ci.objetivo_instanciado_id
					inner join dominio_instanciado di on di.id = oi.dominio_instanciado_id
					inner join respuesta re on agc.id = re.agrupacion_checklist_id
					inner join checklist_instanciado chk on chk.id = re.checklist_instanciado_id and chk.control_instanciado_id = ci.id
					where ca.agrupacion_checklist_id = idAgrupacion and re.aplica = 'SI' and ca.deleted=0 and ci.deleted=0 and oi.deleted=0 and di.deleted=0 
					and agc.deleted=0 and re.deleted=0 and chk.deleted=0
					group by ca.id
				) c group by c.objetivoId
			) b where b.dominioId = idDominio group by b.dominioId
		) e on e.dominioId = da.dominio_instanciado_id
		set da.cobertura = e.cober, da.exito = e.exi
		where da.dominio_instanciado_id = idDominio and da.deleted = 0 and da.agrupacion_checklist_id = idAgrupacion;

		update agrupacion_checklist ag
		inner join (
			select avg(x.ex) as exi, avg(x.cob) as cober, x.agId from (
				select avg(b.exb) as ex, avg(b.ceb) as cob, b.dominioId, b.agId from (
					select c.dominioId, c.objetivoId, sum(c.exito)/count(c.id) as exb, sum(c.cobertura)/count(c.id) as ceb, c.agId from (
						SELECT ca.id as id, ca.agrupacion_checklist_id as agId, oi.id as objetivoId, di.id as dominioId, ca.exito as exito, ca.cobertura as cobertura
						from control_auditoria ca
						inner join agrupacion_checklist agc on ca.agrupacion_checklist_id = agc.id and agc.subproyecto_id = idSubproyecto
						inner join control_instanciado ci on ci.id = ca.control_instanciado_id
						inner join objetivo_instanciado oi on oi.id = ci.objetivo_instanciado_id
						inner join dominio_instanciado di on di.id = oi.dominio_instanciado_id
						inner join respuesta re on agc.id = re.agrupacion_checklist_id
						inner join checklist_instanciado chk on chk.id = re.checklist_instanciado_id and chk.control_instanciado_id = ci.id
						where ca.agrupacion_checklist_id = idAgrupacion and re.aplica = 'SI' and ca.deleted=0 and ci.deleted=0 and oi.deleted=0 and di.deleted=0 
						and agc.deleted=0 and re.deleted=0 and chk.deleted=0
						group by ca.id
					) c group by c.objetivoId
				) b group by b.dominioId
			) x group by x.agId
		) v on v.agId = ag.id
		set ag.cobertura = v.cober, ag.exito = v.exi
		where ag.subproyecto_id = idSubproyecto and ag.id = idAgrupacion and ag.deleted = 0;
       IF done THEN 
   LEAVE loop_recorre;
   END IF;
   END LOOP;
CLOSE recorre;  
	SET done = FALSE;
	SELECT FLOOR(AVG(exito)) INTO mediaAuditoria from control_auditoria ca left join agrupacion_checklist ag on ca.agrupacion_checklist_id = ag.id where ag.subproyecto_id = idSubproyecto and ca.agrupacion_checklist_id is not null;
        UPDATE nodo_arbol na, subproyecto sub
        SET na.porcentaje = mediaAuditoria
        WHERE na.id = sub.nodo_arbol_id and sub.id = idSubproyecto;
        
        COMMIT;
        
	SELECT padre INTO padreRama from nodo_arbol na left join subproyecto sub on na.id = sub.nodo_arbol_id where sub.id = idSubproyecto;
        
    set porcentajeHoja = ( SELECT porcentaje from (
		SELECT count(id), FLOOR(AVG(porcentaje)) as porcentaje ,padre from nodo_arbol where padre is not null and padre != 0 and padre = padreRama group by padre) c );
        
        UPDATE nodo_arbol
        SET porcentaje = porcentajeHoja
        WHERE id = padreRama;
        
        if padreRama in (select id from nodo_arbol WHERE padre != 0)
        THEN 
        loop_arbol: LOOP
        
        SELECT padre INTO existePadre from nodo_arbol where id = padreRama LIMIT 1;
        
        
         set porcentajeTotal = ( SELECT porcentaje from (
		SELECT count(id), FLOOR(AVG(porcentaje)) as porcentaje ,padre from nodo_arbol where padre is not null and padre != 0 and padre = existePadre group by padre) c );
        
        UPDATE nodo_arbol
        SET porcentaje = porcentajeTotal
        WHERE id = existePadre;

       	SET padreRama = existePadre;
       
       	IF done THEN 
		   LEAVE loop_arbol;
		END IF;
        
        END LOOP;
        END IF;
END;

CREATE DEFINER=`ar_marisma`@`%` FUNCTION `ar_marisma`.`func_calculoControles`(idSubproyecto INT, idControl INT, idAgrupacion INT) RETURNS float
BEGIN
	DECLARE vExito float;

	SELECT (exito) INTO vExito FROM (
		select 
			ag.subproyecto_id as subproyecto_id, ca.control_instanciado_id = control_instanciado_id, 
			@varCoberCheck := obtenerControlAuditoriaExito(ag.subproyecto_id, ca.control_instanciado_id, idAgrupacion) as coberCheck,
		 	if (
		 		if (
		 			(select @varAuxiliar := COUNT(id) FROM (
		 				select ch.id as id, ch.control_instanciado_id 
		 				from checklist_instanciado ch 
						inner join respuesta res on ch.id = res.checklist_instanciado_id
						where res.aplica = 'SI' and res.deleted=0 and ch.deleted=0 
						and res.agrupacion_checklist_id = idAgrupacion
						group by ch.id, ch.control_instanciado_id
					) a
					where control_instanciado_id = ca.control_instanciado_id) 
					= 
					(select COUNT(res.id) as auxiliar from respuesta res
						 inner join checklist_instanciado ch on ch.id = res.checklist_instanciado_id
						 where ch.control_instanciado_id = ca.control_instanciado_id and res.deleted=0 and ch.deleted=0
						 group by ch.control_instanciado_id), true, false) = true,
		 		if (ca.cobertura is not null, ca.cobertura *100.0, 0*100),
		 		if (@varCoberCheck is not null, 0, null)
		 	) as exitocero,
		 	@varAuxiliar as auxiliar,
		 	@checksTotal := (select count(ch1.id) from checklist_instanciado ch1 where ch1.control_instanciado_id = ca.control_instanciado_id and ch1.deleted=0) as totalChecks,
		 	@varAplica := if (@varAxuliar = 0.0, false, true) as aplica,
			(@varCoberCheck / (NULLIF(@varAuxiliar,0) * 2)) * 100.0 as exitoTotal,
			@varCobertura := SUM(ca.cobertura) *100.0 as cobertura,
			@totalControles := (
				select count(ca1.id) 
				from control_auditoria ca1 
				left join agrupacion_checklist ag1 on ca1.agrupacion_checklist_id = ag1.id 
				where ca1.deleted=0 and ag1.deleted=0 and ag1.subproyecto_id = ag.subproyecto_id and ca1.control_instanciado_id = ca.control_instanciado_id and ca1.agrupacion_checklist_id is not null and ca1.agrupacion_checklist_id = idAgrupacion
			) as totalControles,
			ctrl.codigo,
			ctrl.nombre,
			ca.control_instanciado_id,
			@calculo := if (@checksTotal = @varAuxiliar, SUM(ca.cobertura) *100.0 / NULLIF(@totalControles,0) , if(@varAuxiliar != 0.0, if (@varCoberCheck != 0.0, (@varCoberCheck /(NULLIF(@varAuxiliar,0) * 2.0)) , 0.0) * 100.0, 0.0 )) as exito
		from control_auditoria ca
		left join agrupacion_checklist ag on ca.agrupacion_checklist_id = ag.id
		inner join control_instanciado ctrl on ctrl.id = ca.control_instanciado_id
		where ag.subproyecto_id = idSubproyecto and ca.agrupacion_checklist_id = idAgrupacion and ca.control_instanciado_id = idControl 
		and ca.agrupacion_checklist_id is not null and ca.deleted=0 and ctrl.deleted=0 and ag.deleted=0 limit 1 
	) b; 

	return vExito;
END;

CREATE DEFINER=`ar_marisma`@`%` FUNCTION `ar_marisma`.`obtenerControlAuditoriaExito`(idSubproyecto int, idControl int, idAgrupacion int) RETURNS float
BEGIN  
   DECLARE exito FLOAT;
	       SET exito = (
	       		select sum(case when res.nivel_cobertura='SI' then 1 else 0 end) * 2 +
	       			   sum(case when res.nivel_cobertura='PARCIAL' then 1 else 0 end)
		       	from checklist_instanciado ch 
						inner join respuesta res on ch.id = res.checklist_instanciado_id
						inner join agrupacion_checklist agck on res.agrupacion_checklist_id = agck.id
					where res.aplica = 'SI' and res.nivel_cobertura IN ('SI','PARCIAL') and ch.deleted = 0 and res.deleted = 0 and agck.deleted=0 
				and agck.subproyecto_id = idSubproyecto and checklist_instanciado_id in (select chl.id from checklist_instanciado chl where chl.control_instanciado_id = idControl and chl.deleted=0) 
				and agrupacion_checklist_id = idAgrupacion
			);
   return exito;
END;

CREATE DEFINER=`ar_marisma`@`%` FUNCTION `ar_marisma`.`obtenerControlAuditoriaExito1`(idSubproyecto int, idControl int, idAgrupacion int) RETURNS float
BEGIN  
   DECLARE exito FLOAT;
	       SET exito = (
	       		select sum(case when res.nivel_cobertura='SI' then 1 else 0 end) * 2 +
	       			   sum(case when res.nivel_cobertura='PARCIAL' then 1 else 0 end)
		       	from checklist_instanciado ch 
						inner join respuesta res on ch.id = res.checklist_instanciado_id
						inner join agrupacion_checklist agck on res.agrupacion_checklist_id = agck.id
					where res.aplica = 'SI' and res.nivel_cobertura IN ('SI','PARCIAL') and ch.deleted = 0 and res.deleted = 0 and agck.deleted=0 
				and agck.subproyecto_id = idSubproyecto and checklist_instanciado_id in (select chl.id from checklist_instanciado chl where chl.control_instanciado_id = idControl and chl.deleted=0) 
				and agrupacion_checklist_id = idAgrupacion
			);
   return exito;
END;

CREATE DEFINER=`ar_marisma`@`%` PROCEDURE `ar_marisma`.`sp_actualizarExitoArbol`( idSubproyecto INT )
BEGIN
   DECLARE done INT DEFAULT FALSE;
   DECLARE mediaRama FLOAT;
   DECLARE padreRama INT;
   DECLARE existePadre INT;
   DECLARE entraifid INT;
   DECLARE porcentajeTotal FLOAT;

   DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
   SET max_sp_recursion_depth=255;
   
   SELECT padre INTO padreRama from nodo_arbol na left join subproyecto sub on na.id = sub.nodo_arbol_id where sub.id = idSubproyecto and sub.deleted=0 and na.deleted=0;
		
		        SELECT porcentaje INTO mediaRama from (
				SELECT (sum(n.porcentaje)/count(n.id)) as porcentaje from nodo_arbol n where n.padre is not null and n.padre != 0 and n.padre = padreRama and n.deleted=0) c;
		
		        UPDATE nodo_arbol
		        SET porcentaje = if(mediaRama is null, 0, mediaRama)
		        WHERE id = padreRama and deleted=0;
		
				set entraifid := (select nar.id from nodo_arbol nar WHERE nar.id = padreRama and nar.padre != 0 and nar.deleted=0);
		       
				if (entraifid is not null)
		        THEN
			        loop_arbol: LOOP
				        SELECT ao.padre INTO existePadre from nodo_arbol ao where ao.id = padreRama and ao.deleted=0 LIMIT 1;
				
						SET porcentajeTotal := ( SELECT FLOOR(avg(al.porcentaje)) from nodo_arbol al where al.padre is not null and al.padre != 0 and al.padre = padreRama and al.deleted=0 );
				
				        UPDATE nodo_arbol
				        SET porcentaje = if(porcentajeTotal is null, 0, porcentajeTotal)
				        WHERE id = padreRama and deleted=0;
				
				        SET padreRama = existePadre;
				
				        IF done THEN
						   LEAVE loop_arbol;
						END IF;
		        	END LOOP;
		        END IF;
END;

CREATE DEFINER=`ar_marisma`@`%` PROCEDURE `ar_marisma`.`sp_actualizarExitoControl`( idSubproyecto INT, idControl INT, idAgrupacion INT, deleted INT )
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE mediaAuditoria FLOAT;
    DECLARE mediaRama FLOAT;
    DECLARE vExito FLOAT;
    DECLARE padreRama INT;
    DECLARE entraifid INT;
    DECLARE entraifpadre INT;
    DECLARE existePadre INT;
    DECLARE porcentajeTotal FLOAT;
    DECLARE porcentajeHoja FLOAT;
	DECLARE idObjetivo INT;
	DECLARE idDominio INT;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    SET max_sp_recursion_depth=255;

	if deleted = 0 then
		select func_calculoControles(idSubproyecto, idControl, idAgrupacion) into vExito;

		UPDATE control_auditoria ca, agrupacion_checklist ag
   		SET ca.exito = vExito
   		where ca.agrupacion_checklist_id = idAgrupacion and ca.deleted=0 and ag.deleted=0 and ca.agrupacion_checklist_id = ag.id and ag.subproyecto_id = idSubproyecto and ca.control_instanciado_id = idControl;
	
		select oa.objetivo_instanciado_id into idObjetivo 
		from control_auditoria ca, agrupacion_checklist ag, objetivo_auditoria oa
		where ca.agrupacion_checklist_id = idAgrupacion and ca.deleted=0 and ag.deleted=0 and ca.agrupacion_checklist_id = ag.id 
		and ag.subproyecto_id = idSubproyecto and ca.control_instanciado_id = idControl
		and oa.agrupacion_checklist_id = ag.id and oa.agrupacion_checklist_id = idAgrupacion and oa.agrupacion_checklist_id = ca.agrupacion_checklist_id
		and oa.deleted = 0 and oa.id = ca.objetivo_auditoria_id;

		update objetivo_auditoria oa
		inner join (
			select c.objetivoId, sum(c.exito)/count(c.id) as exi, sum(c.cobertura)/count(c.id) as cober from (
				SELECT ca.id as id, oi.id as objetivoId, ca.exito as exito, ca.cobertura as cobertura
				from control_auditoria ca
				inner join agrupacion_checklist agc on ca.agrupacion_checklist_id = agc.id and agc.subproyecto_id = idSubproyecto
				inner join control_instanciado ci on ci.id = ca.control_instanciado_id
				inner join objetivo_instanciado oi on oi.id = ci.objetivo_instanciado_id
				inner join dominio_instanciado di on di.id = oi.dominio_instanciado_id
				inner join respuesta re on agc.id = re.agrupacion_checklist_id
				inner join checklist_instanciado chk on chk.id = re.checklist_instanciado_id and chk.control_instanciado_id = ci.id
				where ca.agrupacion_checklist_id = idAgrupacion and re.aplica = 'SI' and ca.deleted=0 and ci.deleted=0 and oi.deleted=0 and di.deleted=0 
				and agc.deleted=0 and re.deleted=0 and chk.deleted=0
				group by ca.id
			) c where c.objetivoId = idObjetivo group by c.objetivoId
		) b on b.objetivoId = oa.objetivo_instanciado_id
		set oa.cobertura = b.cober, oa.exito = b.exi
		where oa.objetivo_instanciado_id = idObjetivo and oa.deleted = 0 and oa.agrupacion_checklist_id = idAgrupacion;

		select da.dominio_instanciado_id into idDominio 
		from objetivo_auditoria oa, dominio_auditoria da 
		where oa.objetivo_instanciado_id = idObjetivo and oa.deleted = 0 and oa.agrupacion_checklist_id = idAgrupacion
		and da.id = oa.dominio_auditoria_id and da.deleted = 0 and da.agrupacion_checklist_id = idAgrupacion and da.agrupacion_checklist_id = oa.agrupacion_checklist_id;

		update dominio_auditoria da
		inner join (
			select avg(b.ex) as exi, avg(b.ceb) as cober, b.dominioId from (
				select c.dominioId, c.objetivoId, sum(c.exito)/count(c.id) as ex, sum(c.cobertura)/count(c.id) as ceb from (
					SELECT ca.id as id, oi.id as objetivoId, di.id as dominioId, ca.exito as exito, ca.cobertura as cobertura
					from control_auditoria ca
					inner join agrupacion_checklist agc on ca.agrupacion_checklist_id = agc.id and agc.subproyecto_id = idSubproyecto
					inner join control_instanciado ci on ci.id = ca.control_instanciado_id
					inner join objetivo_instanciado oi on oi.id = ci.objetivo_instanciado_id
					inner join dominio_instanciado di on di.id = oi.dominio_instanciado_id
					inner join respuesta re on agc.id = re.agrupacion_checklist_id
					inner join checklist_instanciado chk on chk.id = re.checklist_instanciado_id and chk.control_instanciado_id = ci.id
					where ca.agrupacion_checklist_id = idAgrupacion and re.aplica = 'SI' and ca.deleted=0 and ci.deleted=0 and oi.deleted=0 and di.deleted=0 
					and agc.deleted=0 and re.deleted=0 and chk.deleted=0
					group by ca.id
				) c group by c.objetivoId
			) b where b.dominioId = idDominio group by b.dominioId
		) e on e.dominioId = da.dominio_instanciado_id
		set da.cobertura = e.cober, da.exito = e.exi
		where da.dominio_instanciado_id = idDominio and da.deleted = 0 and da.agrupacion_checklist_id = idAgrupacion;

		update agrupacion_checklist ag
		inner join (
			select avg(x.ex) as exi, avg(x.cob) as cober, x.agId from (
				select avg(b.exb) as ex, avg(b.ceb) as cob, b.dominioId, b.agId from (
					select c.dominioId, c.objetivoId, sum(c.exito)/count(c.id) as exb, sum(c.cobertura)/count(c.id) as ceb, c.agId from (
						SELECT ca.id as id, ca.agrupacion_checklist_id as agId, oi.id as objetivoId, di.id as dominioId, ca.exito as exito, ca.cobertura as cobertura
						from control_auditoria ca
						inner join agrupacion_checklist agc on ca.agrupacion_checklist_id = agc.id and agc.subproyecto_id = idSubproyecto
						inner join control_instanciado ci on ci.id = ca.control_instanciado_id
						inner join objetivo_instanciado oi on oi.id = ci.objetivo_instanciado_id
						inner join dominio_instanciado di on di.id = oi.dominio_instanciado_id
						inner join respuesta re on agc.id = re.agrupacion_checklist_id
						inner join checklist_instanciado chk on chk.id = re.checklist_instanciado_id and chk.control_instanciado_id = ci.id
						where ca.agrupacion_checklist_id = idAgrupacion and re.aplica = 'SI' and ca.deleted=0 and ci.deleted=0 and oi.deleted=0 and di.deleted=0 
						and agc.deleted=0 and re.deleted=0 and chk.deleted=0
						group by ca.id
					) c group by c.objetivoId
				) b group by b.dominioId
			) x group by x.agId
		) v on v.agId = ag.id
		set ag.cobertura = v.cober, ag.exito = v.exi
		where ag.subproyecto_id = idSubproyecto and ag.id = idAgrupacion and ag.deleted = 0;
	end if;

	select floor(avg(y.exitoDom)) into mediaAuditoria from (
		select floor(sum(x.exitoOB)/count(x.codigoId)) as exitoDom from (
			select g.codigo, g.codigoId, avg(g.exitoCon) as exitoOB, g.agrupacionId from (
				select b.codigo, b.codigoId, count(b.objetivoId) as cuentaOb, count(b.codigoId), avg(b.ce) as exitoCon, b.agrupacionId from (
					select count(c.id) as cuentaId, sum(c.exito) as exito, c.codigo, c.codigoId, c.objetivoId, sum(c.exito)/count(c.id) as ce, c.agrupacionId from (
						SELECT ca.id as id, oi.id as objetivoId, ca.exito as exito, di.id as codigoId, di.codigo as codigo, agc.nombre, agc.id as agrupacionId
						from control_auditoria ca
						inner join agrupacion_checklist agc on ca.agrupacion_checklist_id = agc.id and agc.subproyecto_id = idSubproyecto
						inner join control_instanciado ci on ci.id = ca.control_instanciado_id
						inner join objetivo_instanciado oi on oi.id = ci.objetivo_instanciado_id
						inner join dominio_instanciado di on di.id = oi.dominio_instanciado_id
						inner join respuesta re on agc.id = re.agrupacion_checklist_id
						inner join checklist_instanciado chk on chk.id = re.checklist_instanciado_id and chk.control_instanciado_id = ci.id
						where ca.agrupacion_checklist_id is not null and re.aplica = 'SI' and ca.deleted=0 and ci.deleted=0 and oi.deleted=0 and di.deleted=0 
						and agc.deleted=0 and re.deleted=0 and chk.deleted=0
						group by ca.id, agc.id
					) c group by c.agrupacionId, c.objetivoId  order by c.agrupacionId
				) b group by b.agrupacionId, b.codigoId order by b.agrupacionId
			) g group by g.agrupacionId
		) x group by x.agrupacionId
	) y;

    UPDATE nodo_arbol na, subproyecto sub
    SET na.porcentaje = if(mediaAuditoria is null, 0, mediaAuditoria)
    WHERE na.id = sub.nodo_arbol_id and sub.id = idSubproyecto and na.deleted=0 and sub.deleted=0;

    SELECT padre INTO padreRama from nodo_arbol na left join subproyecto sub on na.id = sub.nodo_arbol_id where sub.id = idSubproyecto and sub.deleted=0 and na.deleted=0;

    SELECT porcentaje INTO mediaRama from (SELECT floor(sum(porcentaje)/count(id)) as porcentaje from nodo_arbol where padre is not null and padre != 0 and padre = padreRama) c;

    UPDATE nodo_arbol
    SET porcentaje = if(mediaRama is null, 0, mediaRama)
    WHERE id = padreRama and deleted=0;

	set entraifid := (select nar.id from nodo_arbol nar WHERE nar.id = padreRama and nar.padre != 0 and nar.deleted=0);
   
	if (entraifid is not null)
    THEN
        loop_arbol: LOOP
	        SELECT ao.padre INTO existePadre from nodo_arbol ao where ao.id = padreRama and ao.deleted=0 LIMIT 1;

			SET porcentajeTotal := ( SELECT floor(sum(al.porcentaje)/count(al.id)) from nodo_arbol al where al.padre is not null and al.padre != 0 and al.padre = padreRama and al.deleted=0 );
	
	        UPDATE nodo_arbol
	        SET porcentaje = if(porcentajeTotal is null, 0, porcentajeTotal)
	        WHERE id = padreRama and deleted=0;
	
	        SET padreRama = existePadre;
	
	        IF done THEN
			   LEAVE loop_arbol;
			END IF;
    	END LOOP;
    END IF;
END;

CREATE DEFINER=`ar_marisma`@`%` PROCEDURE `ar_marisma`.`sp_analisisRiesgo`(in sub INT(4))
BEGIN
	SELECT a.subproyecto_id as subproyecto, a.activo_amenaza_id, max(a.activo_id) as activo_id, max(a.amenaza_instanciada_id) as amenaza_instanciada_id, 
	   	   max(a.agrupacion_checklist_id) as agrupacion_checklist_id, sum(a.cobertura)/count(*) as cobertura, sum(a.porcentaje)/count(*) as porcentaje
	FROM (
	    SELECT ack.subproyecto_id, am.id as activo_amenaza_id, am.activo_id, am.amenaza_instanciada_id, aaud.agrupacion_checklist_id, ob.porcentaje,
			ctl.id as control_instanciado_id, max(ctlAud.cobertura) as cobertura, sum(CASE WHEN res.aplica='SI' THEN 1 ELSE 0 END) as aplica
		FROM activo_amenaza am inner join amenaza_instanciada ama on am.amenaza_instanciada_id = ama.id and ama.subproyecto_id = sub
			inner join activo_auditoria aaud on am.activo_id = aaud.activo_id and aaud.subproyecto_id = sub   
			inner join agrupacion_checklist ack on aaud.agrupacion_checklist_id = ack.id
			inner join control_amenaza_instanciado ob on am.amenaza_instanciada_id = ob.amenaza_instanciada_id
			inner join control_instanciado ctl on ob.control_instanciado_id = ctl.id
			inner join control_auditoria ctlAud on ctl.id = ctlAud.control_instanciado_id and ctlAud.agrupacion_checklist_id = ack.id
			inner join checklist_instanciado chk on chk.control_instanciado_id = ctl.id
			inner join respuesta res on res.checklist_instanciado_id = chk.id and res.agrupacion_checklist_id = ack.id   
		WHERE am.deleted = 0 and ama.deleted = 0 and aaud.deleted = 0 and ack.deleted = 0 and ob.deleted = 0 and ctl.deleted = 0 and ctlAud.deleted = 0 and chk.deleted = 0 
		and res.deleted = 0
		GROUP BY ack.subproyecto_id, am.id, am.activo_id, am.amenaza_instanciada_id, aaud.agrupacion_checklist_id, ob.porcentaje, ctl.id
	) a
	WHERE aplica >= 1 and a.subproyecto_id=sub
	group by
       a.subproyecto_id ,
       a.activo_amenaza_id;
END;

CREATE DEFINER=`ar_marisma`@`%` PROCEDURE `ar_marisma`.`sp_calcularExitoProyecto`(idProyecto INT)
BEGIN
   DECLARE done INT DEFAULT FALSE;
   DECLARE mediaRama FLOAT;
   DECLARE padreRama INT;
   DECLARE existePadre INT;
   DECLARE entraifid INT;
   DECLARE porcentajeTotal FLOAT;
   DECLARE idSubproyecto INT;
   DECLARE recorre CURSOR FOR 
	  select sub.id from subproyecto sub inner join nodo_arbol na on sub.nodo_arbol_id = na.id left join proyecto p on na.proyecto_id = p.id 
	  where p.id = idProyecto and p.deleted = 0 and sub.deleted = 0 and na.deleted = 0; 

   DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
   SET max_sp_recursion_depth=255;
	 		
	OPEN recorre;
   		set idSubproyecto = 0;
	    loop_recorre: LOOP   
	       FETCH recorre INTO idSubproyecto;		
				
		        SELECT padre INTO padreRama from nodo_arbol na left join subproyecto sub on na.id = sub.nodo_arbol_id where sub.id = idSubproyecto and sub.deleted=0 and na.deleted=0;
		
		        SELECT porcentaje INTO mediaRama from (
				SELECT (sum(porcentaje)/count(id)) as porcentaje from nodo_arbol where padre is not null and padre != 0 and padre = padreRama) c;
		
		        UPDATE nodo_arbol
		        SET porcentaje = if(mediaRama is null, 0, mediaRama)
		        WHERE id = padreRama and deleted=0;
		
				set entraifid := (select nar.id from nodo_arbol nar WHERE nar.id = padreRama and nar.padre != 0 and nar.deleted=0);
		       
				if (entraifid is not null)
		        THEN
			        loop_arbol: LOOP
				        SELECT ao.padre INTO existePadre from nodo_arbol ao where ao.id = padreRama and ao.deleted=0 LIMIT 1;
				
						SET porcentajeTotal := ( SELECT FLOOR(avg(al.porcentaje)) from nodo_arbol al where al.padre is not null and al.padre != 0 and al.padre = padreRama and al.deleted=0 );
				
				        UPDATE nodo_arbol
				        SET porcentaje = if(porcentajeTotal is null, 0, porcentajeTotal)
				        WHERE id = padreRama and deleted=0;
				
				        SET padreRama = existePadre;
				
				        IF done THEN
						   LEAVE loop_arbol;
						END IF;
		        	END LOOP;
		        END IF;
			
			IF done THEN 
				LEAVE loop_recorre;
    		END IF;
	       		    
	   	END LOOP;
   CLOSE recorre; 
END;

CREATE DEFINER=`ar_marisma`@`%` PROCEDURE `ar_marisma`.`sp_createExitoControl`( idSubproyecto INT, idAgrupacion INT, idEsquema INT)
BEGIN
   DECLARE done INT DEFAULT FALSE;
   DECLARE mediaAuditoria FLOAT;
   DECLARE mediaRama FLOAT;
   DECLARE padreRama INT;
   DECLARE existePadre INT;
   DECLARE entraifid INT;
   DECLARE porcentajeTotal FLOAT;
   DECLARE porcentajeHoja FLOAT;
   DECLARE idControl INT;
   DECLARE recorre CURSOR FOR 
	  select ci.id 
	  from control_instanciado ci, objetivo_instanciado oi, dominio_instanciado di, esquema_instanciado ei 
	  where ci.deleted =0 and ci.objetivo_instanciado_id = oi.id and oi.deleted = 0 and oi.dominio_instanciado_id = di.id and di.deleted = 0 
	  and di.esquema_instanciado_id = ei.id and ei.deleted = 0 and ei.id = idEsquema;

   DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
   SET max_sp_recursion_depth=255;
	 		
	OPEN recorre;
   		set idControl = 0;
	    loop_recorre: LOOP   
	       FETCH recorre INTO idControl;		
					select floor(avg(y.exitoDom)) into mediaAuditoria from (
						select floor(sum(x.exitoOB)/count(x.codigoId)) as exitoDom from (
							select g.codigo, g.codigoId, avg(g.exitoCon) as exitoOB, g.agrupacionId from (
								select b.codigo, b.codigoId, count(b.objetivoId) as cuentaOb, count(b.codigoId), avg(b.ce) as exitoCon, b.agrupacionId from (
									select count(c.id) as cuentaId, sum(c.exito) as exito, c.codigo, c.codigoId, c.objetivoId, sum(c.exito)/count(c.id) as ce, c.agrupacionId from (
										SELECT ca.id as id, oi.id as objetivoId, ca.exito as exito, di.id as codigoId, di.codigo as codigo, agc.nombre, agc.id as agrupacionId
										from control_auditoria ca
										inner join agrupacion_checklist agc on ca.agrupacion_checklist_id = agc.id and agc.subproyecto_id = idSubproyecto
										inner join control_instanciado ci on ci.id = ca.control_instanciado_id
										inner join objetivo_instanciado oi on oi.id = ci.objetivo_instanciado_id
										inner join dominio_instanciado di on di.id = oi.dominio_instanciado_id
										inner join respuesta re on agc.id = re.agrupacion_checklist_id
										inner join checklist_instanciado chk on chk.id = re.checklist_instanciado_id and chk.control_instanciado_id = ci.id
										where ca.agrupacion_checklist_id is not null and re.aplica = 'SI' and ca.deleted=0 and ci.deleted=0 and oi.deleted=0 and di.deleted=0 
										and agc.deleted=0 and re.deleted=0 and chk.deleted=0
										group by ca.id, agc.id
									) c group by c.agrupacionId, c.objetivoId  order by c.agrupacionId
								) b group by b.agrupacionId, b.codigoId order by b.agrupacionId
							) g group by g.agrupacionId
						) x group by x.agrupacionId
					) y;
			
		        UPDATE nodo_arbol na, subproyecto sub
        		SET na.porcentaje = if(mediaAuditoria is null, 0, mediaAuditoria)
        		WHERE na.id = sub.nodo_arbol_id and sub.id = idSubproyecto and na.deleted=0 and sub.deleted=0;

		        SELECT padre INTO padreRama from nodo_arbol na left join subproyecto sub on na.id = sub.nodo_arbol_id where sub.id = idSubproyecto and sub.deleted=0 and na.deleted=0;
		
		        SELECT porcentaje INTO mediaRama from (
				SELECT (sum(porcentaje)/count(id)) as porcentaje from nodo_arbol where padre is not null and padre != 0 and padre = padreRama) c;
		
		        UPDATE nodo_arbol
		        SET porcentaje = if(mediaRama is null, 0, mediaRama)
		        WHERE id = padreRama and deleted=0;
		
				set entraifid := (select nar.id from nodo_arbol nar WHERE nar.id = padreRama and nar.padre != 0 and nar.deleted=0);
		       
				if (entraifid is not null)
		        THEN
			        loop_arbol: LOOP
				        SELECT ao.padre INTO existePadre from nodo_arbol ao where ao.id = padreRama and ao.deleted=0 LIMIT 1;
				
						SET porcentajeTotal := ( SELECT FLOOR(avg(al.porcentaje)) from nodo_arbol al where al.padre is not null and al.padre != 0 and al.padre = padreRama and al.deleted=0 );
				
				        UPDATE nodo_arbol
				        SET porcentaje = if(porcentajeTotal is null, 0, porcentajeTotal)
				        WHERE id = padreRama and deleted=0;
				
				        SET padreRama = existePadre;
				
				        IF done THEN
						   LEAVE loop_arbol;
						END IF;
		        	END LOOP;
		        END IF;
			
			IF done THEN 
				LEAVE loop_recorre;
    		END IF;
	       		    
	   	END LOOP;
   CLOSE recorre; 
END;

CREATE DEFINER=`ar_marisma`@`%` PROCEDURE `ar_marisma`.`sp_planTratamiento`(in sub INT(4))
BEGIN
	SELECT a.subproyecto_id as subproyecto, a.activo_amenaza_id, max(a.activo_id) as activo_id, max(a.amenaza_instanciada_id) as amenaza_instanciada_id, 
		   max(a.agrupacion_checklist_id) as agrupacion_checklist_id, a.porcentaje, a.control_instanciado_id, sum(a.cobertura)/count(*) as cobertura
	FROM (
		SELECT ack.subproyecto_id, am.id as activo_amenaza_id, am.activo_id, am.amenaza_instanciada_id, aaud.agrupacion_checklist_id, ob.porcentaje,
			ctl.id as control_instanciado_id, max(ctlAud.cobertura) as cobertura, sum(CASE WHEN res.aplica = 'SI' THEN 1 ELSE 0 END) as aplica
		FROM activo_amenaza am inner join amenaza_instanciada ama on am.amenaza_instanciada_id = ama.id and ama.subproyecto_id = sub
			inner join activo_auditoria aaud on am.activo_id = aaud.activo_id and aaud.subproyecto_id = sub
			inner join agrupacion_checklist ack on aaud.agrupacion_checklist_id = ack.id
			inner join control_amenaza_instanciado ob on am.amenaza_instanciada_id = ob.amenaza_instanciada_id
			inner join control_instanciado ctl on ob.control_instanciado_id = ctl.id
			inner join control_auditoria ctlAud on ctl.id = ctlAud.control_instanciado_id and ctlAud.agrupacion_checklist_id = ack.id
			inner join checklist_instanciado chk on chk.control_instanciado_id = ctl.id
			inner join respuesta res on res.checklist_instanciado_id = chk.id and res.agrupacion_checklist_id = ack.id
		WHERE am.deleted = 0 and ama.deleted = 0 and aaud.deleted = 0 and ack.deleted = 0 and ob.deleted = 0 and ctl.deleted = 0 and ctlAud.deleted = 0 and chk.deleted = 0
		and res.deleted = 0
		GROUP BY ack.subproyecto_id, am.id, am.activo_id, am.amenaza_instanciada_id, aaud.agrupacion_checklist_id, ob.porcentaje, ctl.id
	) a
	WHERE aplica >= 1 AND a.subproyecto_id = sub
	GROUP BY a.subproyecto_id, a.activo_amenaza_id, a.porcentaje, a.control_instanciado_id
	ORDER BY a.cobertura ASC;
END;