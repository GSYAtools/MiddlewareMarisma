-- ar_marisma.acl_class definition

CREATE TABLE `acl_class` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `class` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_iy7ua5fso3il3u3ymoc4uf35w` (`class`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


-- ar_marisma.acl_sid definition

CREATE TABLE `acl_sid` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sid` varchar(255) NOT NULL,
  `principal` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK1781b9a084dff171b580608b3640` (`sid`,`principal`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


-- ar_marisma.audit_log definition

CREATE TABLE `audit_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `persisted_object_id` varchar(255) DEFAULT NULL,
  `property_name` varchar(255) DEFAULT NULL,
  `date_created` datetime NOT NULL,
  `last_updated` datetime NOT NULL,
  `event_name` varchar(255) DEFAULT NULL,
  `actor` varchar(255) DEFAULT NULL,
  `new_value` varchar(255) DEFAULT NULL,
  `class_name` varchar(255) DEFAULT NULL,
  `old_value` varchar(255) DEFAULT NULL,
  `persisted_object_version` bigint(20) DEFAULT NULL,
  `uri` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4710 DEFAULT CHARSET=utf8;


-- ar_marisma.capec definition

CREATE TABLE `capec` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `related_weakness` text,
  `mitigations` text,
  `typical_severity` varchar(255) DEFAULT NULL,
  `code` int(11) DEFAULT NULL,
  `consequences` text,
  `taxonomy_mappings` text,
  `prerequisites` text,
  `notes` text,
  `execution_flow` text,
  `skill_required` text,
  `example_instances` text,
  `resources_required` text,
  `abstraction` varchar(255) DEFAULT NULL,
  `likelihood_of_attack` varchar(255) DEFAULT NULL,
  `alternate_terms` text,
  `name` varchar(255) DEFAULT NULL,
  `indicators` text,
  `status` varchar(255) DEFAULT NULL,
  `related_attack_patterns` text,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.cnae definition

CREATE TABLE `cnae` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `codigo` varchar(255) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1011 DEFAULT CHARSET=utf8;


-- ar_marisma.configuracion definition

CREATE TABLE `configuracion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `valor` varchar(4000) DEFAULT NULL,
  `clave` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;


-- ar_marisma.cvss_metricv20 definition

CREATE TABLE `cvss_metricv20` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `availability_impact` varchar(255) NOT NULL,
  `access_complexity` varchar(255) NOT NULL,
  `obtain_user_privilege` bit(1) NOT NULL,
  `authentication` varchar(255) NOT NULL,
  `exploitability_score` float NOT NULL,
  `confidentiality_impact` varchar(255) NOT NULL,
  `ac_insuf_info` bit(1) NOT NULL,
  `base_score` float NOT NULL,
  `integrity_impact` varchar(255) NOT NULL,
  `source` varchar(255) NOT NULL,
  `obtain_other_privilege` bit(1) NOT NULL,
  `impact_score` float NOT NULL,
  `access_vector` varchar(255) NOT NULL,
  `user_interaction_required` bit(1) NOT NULL,
  `type` varchar(255) NOT NULL,
  `base_severity` varchar(255) NOT NULL,
  `vector_string` varchar(255) NOT NULL,
  `obtain_all_privilege` bit(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.cvss_metricv30 definition

CREATE TABLE `cvss_metricv30` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `availability_impact` varchar(255) NOT NULL,
  `user_interaction` varchar(255) NOT NULL,
  `exploitability_score` float NOT NULL,
  `confidentiality_impact` varchar(255) NOT NULL,
  `privileges_required` varchar(255) NOT NULL,
  `base_score` float NOT NULL,
  `integrity_impact` varchar(255) NOT NULL,
  `source` varchar(255) NOT NULL,
  `attack_complexity` varchar(255) NOT NULL,
  `attack_vector` varchar(255) NOT NULL,
  `impact_score` float NOT NULL,
  `scope` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `base_severity` varchar(255) NOT NULL,
  `vector_string` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.cvss_metricv31 definition

CREATE TABLE `cvss_metricv31` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `availability_impact` varchar(255) NOT NULL,
  `user_interaction` varchar(255) NOT NULL,
  `exploitability_score` float NOT NULL,
  `confidentiality_impact` varchar(255) NOT NULL,
  `privileges_required` varchar(255) NOT NULL,
  `base_score` float NOT NULL,
  `integrity_impact` varchar(255) NOT NULL,
  `source` varchar(255) NOT NULL,
  `attack_complexity` varchar(255) NOT NULL,
  `attack_vector` varchar(255) NOT NULL,
  `impact_score` float NOT NULL,
  `scope` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `base_severity` varchar(255) NOT NULL,
  `vector_string` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.esquema_disponible definition

CREATE TABLE `esquema_disponible` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `codigo` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `id_esquema` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_pion2nlds3xmn97l8vlmk0qmm` (`id_esquema`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;


-- ar_marisma.esquema_instanciado definition

CREATE TABLE `esquema_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `esquema_instanciado` bigint(20) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `codigo_padre` varchar(255) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `tipo` varchar(255) NOT NULL,
  `codigo` varchar(255) NOT NULL,
  `nombre_padre` varchar(255) DEFAULT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


-- ar_marisma.historico_activo_amenaza definition

CREATE TABLE `historico_activo_amenaza` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `id_activo_amenaza` bigint(20) DEFAULT NULL,
  `nombre_tipo_activo` varchar(255) DEFAULT NULL,
  `id_subproyecto` bigint(20) DEFAULT NULL,
  `id_tipo_activo` bigint(20) DEFAULT NULL,
  `nombre_amenaza` varchar(255) DEFAULT NULL,
  `codigo_amenaza` varchar(255) DEFAULT NULL,
  `codigo_tipo_activo` varchar(255) DEFAULT NULL,
  `id_amenaza` bigint(20) DEFAULT NULL,
  `id_activo` bigint(20) DEFAULT NULL,
  `valor` decimal(19,2) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `id_sugerencia` bigint(20) DEFAULT NULL,
  `descripcion_activo` varchar(255) DEFAULT NULL,
  `nombre_activo` varchar(255) DEFAULT NULL,
  `editado` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;


-- ar_marisma.historico_activo_amenaza_dimension definition

CREATE TABLE `historico_activo_amenaza_dimension` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `id_activo_amenaza` bigint(20) DEFAULT NULL,
  `valor` int(11) DEFAULT NULL,
  `id_dimension_instanciada` bigint(20) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `nombre_dimension_instanciada` varchar(255) DEFAULT NULL,
  `id_sugerencia` bigint(20) DEFAULT NULL,
  `codigo_dimension_instanciada` varchar(255) DEFAULT NULL,
  `editado` bit(1) DEFAULT NULL,
  `id_activo_amenaza_dimension` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;


-- ar_marisma.historico_con_aud definition

CREATE TABLE `historico_con_aud` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `fecha` datetime NOT NULL,
  `cobertura` float NOT NULL,
  `control_auditoria` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8;


-- ar_marisma.historico_pdt definition

CREATE TABLE `historico_pdt` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `plan` text,
  `analisis_riesgo_id` bigint(20) DEFAULT NULL,
  `control_instanciado_nombre` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `control_instanciado_codigo` varchar(255) DEFAULT NULL,
  `riesgo_inherentearfin` float DEFAULT NULL,
  `riesgo_inherente_ini` float DEFAULT NULL,
  `fecha_fin_prev` datetime DEFAULT NULL,
  `riesgo_inherentearini` float DEFAULT NULL,
  `control_instanciado_id` bigint(20) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `valor_riesgo` float DEFAULT NULL,
  `subproyecto_nombre` varchar(255) DEFAULT NULL,
  `agrupacion_checklist_nombre` varchar(255) DEFAULT NULL,
  `fecha_ejec` datetime DEFAULT NULL,
  `riesgo_inherente_fin` float DEFAULT NULL,
  `agrupacion_checklist_id` bigint(20) DEFAULT NULL,
  `resultado` text,
  `fecha_prev` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.log_sugerencias definition

CREATE TABLE `log_sugerencias` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `id_probabilidad_ocurrencia_sugerida` bigint(20) DEFAULT NULL,
  `datos_conservados` varchar(255) DEFAULT NULL,
  `id_probabilidad_ocurrencia_anterior` bigint(20) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `nombre_probabilidad_ocurrencia_anterior` varchar(255) DEFAULT NULL,
  `nombre_amenaza` varchar(255) DEFAULT NULL,
  `conservar_datos` varchar(255) DEFAULT NULL,
  `fecha_validacion` datetime DEFAULT NULL,
  `aplicara` varchar(255) DEFAULT NULL,
  `id_amenaza` bigint(20) DEFAULT NULL,
  `ids_activos_amenaza_aplicados` varchar(255) DEFAULT NULL,
  `ids_activos_implicados` varchar(255) DEFAULT NULL,
  `codigo_evento` varchar(255) DEFAULT NULL,
  `id_sugerencia` bigint(20) DEFAULT NULL,
  `nombre_activos_implicados` varchar(255) DEFAULT NULL,
  `nombre_probabilidad_ocurrencia_sugerida` varchar(255) DEFAULT NULL,
  `id_incidencia` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.nombre_activo_instanciado definition

CREATE TABLE `nombre_activo_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `nombre_pt` varchar(255) DEFAULT NULL,
  `nombre_en` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.novedad definition

CREATE TABLE `novedad` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime NOT NULL,
  `texto` longtext NOT NULL,
  `deleted` bit(1) NOT NULL,
  `fecha_implementacion` datetime DEFAULT NULL,
  `titulo` varchar(255) NOT NULL,
  `version_implementacion` varchar(255) DEFAULT NULL,
  `show_modal` bit(1) NOT NULL,
  `image` longtext,
  `show_time_line` bit(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.pais definition

CREATE TABLE `pais` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.`role` definition

CREATE TABLE `role` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `authority` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_irsamgnera6angm0prq1kemt2` (`authority`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;


-- ar_marisma.security_event definition

CREATE TABLE `security_event` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `remote_address` varchar(255) DEFAULT NULL,
  `session_id` varchar(255) DEFAULT NULL,
  `event` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=198 DEFAULT CHARSET=utf8;


-- ar_marisma.tutorial_youtube definition

CREATE TABLE `tutorial_youtube` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `show_video` bit(1) NOT NULL,
  `video_url` varchar(255) DEFAULT NULL,
  `video_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.user_import_log definition

CREATE TABLE `user_import_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `cliente_id` bigint(20) DEFAULT NULL,
  `estado_sub` varchar(255) DEFAULT NULL,
  `error_pro` longtext,
  `consultor_id` bigint(20) DEFAULT NULL,
  `fecha_importacion` datetime DEFAULT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  `estado_pro` varchar(255) DEFAULT NULL,
  `codigo_cnae` varchar(255) DEFAULT NULL,
  `estado_us` varchar(255) DEFAULT NULL,
  `nombre_subproyecto` varchar(255) DEFAULT NULL,
  `cnae_id` bigint(20) DEFAULT NULL,
  `nombre_cnae` varchar(255) DEFAULT NULL,
  `cliente_username` varchar(255) DEFAULT NULL,
  `proyecto_id` bigint(20) DEFAULT NULL,
  `consultor_username` varchar(255) DEFAULT NULL,
  `nombre_proyecto` varchar(255) DEFAULT NULL,
  `esquema_disponible_id` bigint(20) DEFAULT NULL,
  `nombre_esquema_disponible` varchar(255) DEFAULT NULL,
  `telefono` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `error_sub` longtext,
  `prefijo` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `error_us` longtext,
  `codigo_esquema_disponible` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.user_token definition

CREATE TABLE `user_token` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `username` varchar(255) NOT NULL,
  `refresh_token` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- ar_marisma.acl_object_identity definition

CREATE TABLE `acl_object_identity` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `object_id_identity` bigint(20) NOT NULL,
  `entries_inheriting` bit(1) NOT NULL,
  `object_id_class` bigint(20) NOT NULL,
  `owner_sid` bigint(20) DEFAULT NULL,
  `parent_object` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK56103a82abb455394f8c97a95587` (`object_id_class`,`object_id_identity`),
  KEY `FKikrbtok3aqlrp9wbq6slh9mcw` (`owner_sid`),
  KEY `FK4soxn7uid8qxltqps8kewftx7` (`parent_object`),
  CONSTRAINT `FK4soxn7uid8qxltqps8kewftx7` FOREIGN KEY (`parent_object`) REFERENCES `acl_object_identity` (`id`),
  CONSTRAINT `FKc06nv93ck19el45a3g1p0e58w` FOREIGN KEY (`object_id_class`) REFERENCES `acl_class` (`id`),
  CONSTRAINT `FKikrbtok3aqlrp9wbq6slh9mcw` FOREIGN KEY (`owner_sid`) REFERENCES `acl_sid` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;


-- ar_marisma.cve_record definition

CREATE TABLE `cve_record` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `modified` datetime DEFAULT NULL,
  `code` varchar(255) NOT NULL,
  `published` datetime DEFAULT NULL,
  `cvss_metricv31_id` bigint(20) DEFAULT NULL,
  `summary` longtext,
  `cvss_metricv20_id` bigint(20) DEFAULT NULL,
  `last_modified` datetime DEFAULT NULL,
  `cvss_metricv30_id` bigint(20) DEFAULT NULL,
  `ref` longtext,
  `assigner` varchar(255) DEFAULT NULL,
  `cwe` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKnnynccgb0k9liscafieghus1o` (`cvss_metricv31_id`),
  KEY `FK9ktgykxiputs3o2a6jhlrjr3a` (`cvss_metricv20_id`),
  KEY `FKmgvnkq83ndk8l0uje03vohse5` (`cvss_metricv30_id`),
  CONSTRAINT `FK9ktgykxiputs3o2a6jhlrjr3a` FOREIGN KEY (`cvss_metricv20_id`) REFERENCES `cvss_metricv20` (`id`),
  CONSTRAINT `FKmgvnkq83ndk8l0uje03vohse5` FOREIGN KEY (`cvss_metricv30_id`) REFERENCES `cvss_metricv30` (`id`),
  CONSTRAINT `FKnnynccgb0k9liscafieghus1o` FOREIGN KEY (`cvss_metricv31_id`) REFERENCES `cvss_metricv31` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.cve_record_capecs definition

CREATE TABLE `cve_record_capecs` (
  `cve_record_id` bigint(20) NOT NULL,
  `capec_id` bigint(20) NOT NULL,
  PRIMARY KEY (`cve_record_id`,`capec_id`),
  KEY `FKq5y2uroa5ovulkj0mf6jr9iyt` (`capec_id`),
  CONSTRAINT `FK5os24geilcdyst15r76ansnc1` FOREIGN KEY (`cve_record_id`) REFERENCES `cve_record` (`id`),
  CONSTRAINT `FKq5y2uroa5ovulkj0mf6jr9iyt` FOREIGN KEY (`capec_id`) REFERENCES `capec` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.dimension_instanciada definition

CREATE TABLE `dimension_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKg7dk7yqbko0s1kxlumpp6sob6` (`esquema_instanciado_id`),
  CONSTRAINT `FKg7dk7yqbko0s1kxlumpp6sob6` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;


-- ar_marisma.esquema_instanciado_esquema_instanciado definition

CREATE TABLE `esquema_instanciado_esquema_instanciado` (
  `esquema_instanciado_hijos_id` bigint(20) NOT NULL,
  `esquema_instanciado_id` bigint(20) DEFAULT NULL,
  KEY `FKb8ogdnpe5vh1mgujxc3k98ct` (`esquema_instanciado_id`),
  KEY `FKor17hes3wh2p81u4sxp5p8q9r` (`esquema_instanciado_hijos_id`),
  CONSTRAINT `FKb8ogdnpe5vh1mgujxc3k98ct` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`),
  CONSTRAINT `FKor17hes3wh2p81u4sxp5p8q9r` FOREIGN KEY (`esquema_instanciado_hijos_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.porcentaje_degradacion_instanciado definition

CREATE TABLE `porcentaje_degradacion_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `rango_minimo` double NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `rango_maximo` double NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `color` varchar(255) NOT NULL,
  `etiqueta` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK2bin96bot7oadp812nsts5mnv` (`esquema_instanciado_id`),
  CONSTRAINT `FK2bin96bot7oadp812nsts5mnv` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;


-- ar_marisma.provincia definition

CREATE TABLE `provincia` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `pais_id` bigint(20) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKm4s599988w0v1q1nw6dyo5t2m` (`pais_id`),
  CONSTRAINT `FKm4s599988w0v1q1nw6dyo5t2m` FOREIGN KEY (`pais_id`) REFERENCES `pais` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.proyecto definition

CREATE TABLE `proyecto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `last_updated_by` varchar(255) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `alcance` varchar(4000) DEFAULT NULL,
  `esquema_disponible_id` bigint(20) NOT NULL,
  `cnae_id` bigint(20) NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKcgidxprqssvwr5us0mx1f6cn` (`esquema_disponible_id`),
  KEY `FKtj0kxk5ifeh3xo6bcr7m6gw7g` (`cnae_id`),
  CONSTRAINT `FKcgidxprqssvwr5us0mx1f6cn` FOREIGN KEY (`esquema_disponible_id`) REFERENCES `esquema_disponible` (`id`),
  CONSTRAINT `FKtj0kxk5ifeh3xo6bcr7m6gw7g` FOREIGN KEY (`cnae_id`) REFERENCES `cnae` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


-- ar_marisma.rango_instanciado definition

CREATE TABLE `rango_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `rango_final` int(11) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `rango_inicial` int(11) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `color` varchar(255) NOT NULL,
  `etiqueta` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK6t19appx3w33malse6ry70o0e` (`esquema_instanciado_id`),
  CONSTRAINT `FK6t19appx3w33malse6ry70o0e` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;


-- ar_marisma.temporalidad_instanciada definition

CREATE TABLE `temporalidad_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `valor` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `etiqueta` varchar(255) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK6fc1ge43jkno82ew087typxbb` (`esquema_instanciado_id`),
  CONSTRAINT `FK6fc1ge43jkno82ew087typxbb` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;


-- ar_marisma.tipo_activo_disponible definition

CREATE TABLE `tipo_activo_disponible` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `formulas` longtext,
  `esquema_disponible_id` bigint(20) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `tipo_raiz_id` bigint(20) DEFAULT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  `proyecto_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK6vi1mwyyg5a3s18qgljb44tv1` (`esquema_disponible_id`),
  KEY `FKb34pl6ya5sfiq04en1ei9w5un` (`tipo_raiz_id`),
  KEY `FKhgh52kp61132mmch0cq2lchav` (`proyecto_id`),
  CONSTRAINT `FK6vi1mwyyg5a3s18qgljb44tv1` FOREIGN KEY (`esquema_disponible_id`) REFERENCES `esquema_disponible` (`id`),
  CONSTRAINT `FKb34pl6ya5sfiq04en1ei9w5un` FOREIGN KEY (`tipo_raiz_id`) REFERENCES `tipo_activo_disponible` (`id`),
  CONSTRAINT `FKhgh52kp61132mmch0cq2lchav` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;


-- ar_marisma.tipo_activo_instanciado definition

CREATE TABLE `tipo_activo_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `formulas` longtext,
  `origen` bigint(20) DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `tipo_raiz_id` bigint(20) DEFAULT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKh3xw8xwbjkt47jd5l5mh3iame` (`esquema_instanciado_id`),
  KEY `FKdcbs3gdbgyt18bqop7ht34plo` (`tipo_raiz_id`),
  CONSTRAINT `FKdcbs3gdbgyt18bqop7ht34plo` FOREIGN KEY (`tipo_raiz_id`) REFERENCES `tipo_activo_instanciado` (`id`),
  CONSTRAINT `FKh3xw8xwbjkt47jd5l5mh3iame` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;


-- ar_marisma.tipo_amenaza_instanciada definition

CREATE TABLE `tipo_amenaza_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKoh3vien2vkl3a3yjkcxwwpri` (`esquema_instanciado_id`),
  CONSTRAINT `FKoh3vien2vkl3a3yjkcxwwpri` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;


-- ar_marisma.tipo_caracteristica_control_instanciada definition

CREATE TABLE `tipo_caracteristica_control_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKk2si6admjejo5fkivo4eksnr4` (`esquema_instanciado_id`),
  CONSTRAINT `FKk2si6admjejo5fkivo4eksnr4` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.`user` definition

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `nombre_comercial` varchar(255) DEFAULT NULL,
  `last_updated_by` varchar(255) DEFAULT NULL,
  `status_account` int(11) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `password_expired` bit(1) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `max_clientes` int(11) DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `activation_token` varchar(255) DEFAULT NULL,
  `account_expired` bit(1) NOT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `contacto` varchar(255) DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `account_locked` bit(1) NOT NULL,
  `cnae_id` bigint(20) DEFAULT NULL,
  `telefono` varchar(255) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `importado` bit(1) NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  `enabled` bit(1) NOT NULL,
  `num_clientes` int(11) DEFAULT NULL,
  `last_access` varchar(100) DEFAULT NULL,
  `status_acccount` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_sb8bbouer5wak8vyiiy4pf2bx` (`username`),
  KEY `FKn33if1c7h5uaf52071fqi1qde` (`cnae_id`),
  CONSTRAINT `FKn33if1c7h5uaf52071fqi1qde` FOREIGN KEY (`cnae_id`) REFERENCES `cnae` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


-- ar_marisma.user_consent definition

CREATE TABLE `user_consent` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `info_terceros` bit(1) NOT NULL,
  `info_marisma` bit(1) NOT NULL,
  `privacidad` bit(1) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `fecha_aceptacion` datetime NOT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  `perfilado` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKejyqlj281wi1ttn7fqrvcxkw2` (`user_id`),
  CONSTRAINT `FKejyqlj281wi1ttn7fqrvcxkw2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;


-- ar_marisma.user_esquemas_asignados definition

CREATE TABLE `user_esquemas_asignados` (
  `user_id` bigint(20) NOT NULL,
  `esquema_disponible_id` bigint(20) NOT NULL,
  PRIMARY KEY (`user_id`,`esquema_disponible_id`),
  KEY `FKi07mcyr5lbweltue898it3x4t` (`esquema_disponible_id`),
  CONSTRAINT `FK6arg153huncr4s7rnbvi65lys` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKi07mcyr5lbweltue898it3x4t` FOREIGN KEY (`esquema_disponible_id`) REFERENCES `esquema_disponible` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.user_image definition

CREATE TABLE `user_image` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `directory` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK5m3lhx7tcj9h9ju10xo4ruqcn` (`user_id`),
  CONSTRAINT `FK5m3lhx7tcj9h9ju10xo4ruqcn` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


-- ar_marisma.user_modulos definition

CREATE TABLE `user_modulos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `responsables_controles` bit(1) NOT NULL,
  `gestor_documental` bit(1) NOT NULL,
  `jerarquia` bit(1) NOT NULL,
  `incidentes` bit(1) NOT NULL,
  `cuadro_mando` bit(1) NOT NULL,
  `no_conformidades` bit(1) NOT NULL,
  `amenazas_riesgos` bit(1) NOT NULL,
  `activos_riesgos` bit(1) NOT NULL,
  `mensajes` bit(1) NOT NULL,
  `agrupaciones_checklist` bit(1) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `auditorias` bit(1) NOT NULL,
  `analisis_riesgos` bit(1) NOT NULL,
  `empresas` bit(1) NOT NULL,
  `plan_tratamiento` bit(1) NOT NULL,
  `gestion_amenazas` bit(1) NOT NULL,
  `informes` bit(1) NOT NULL,
  `nmap` bit(1) NOT NULL,
  `sugerencias` bit(1) NOT NULL,
  `sugerencias_mejoras` bit(1) NOT NULL,
  `mapa_riesgos` bit(1) NOT NULL,
  `activos_predefinidos` bit(1) NOT NULL,
  `subproyectos` bit(1) NOT NULL,
  `atributtes` bit(1) NOT NULL,
  `heatmap` bit(1) NOT NULL,
  `activos_amenazas` bit(1) NOT NULL,
  `soa` bit(1) NOT NULL,
  `kiviats` bit(1) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `indicadores` bit(1) NOT NULL,
  `activos` bit(1) NOT NULL,
  `revision_control` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKl1twgr2ahaqrcyakema6qwxjm` (`user_id`),
  CONSTRAINT `FKl1twgr2ahaqrcyakema6qwxjm` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


-- ar_marisma.user_proyectos definition

CREATE TABLE `user_proyectos` (
  `proyecto_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`user_id`,`proyecto_id`),
  KEY `FKb0fs9s8pbtblnyxxausrjmoew` (`proyecto_id`),
  CONSTRAINT `FK7bsnvc8uvglefepfy5unhpfux` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKb0fs9s8pbtblnyxxausrjmoew` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.user_role definition

CREATE TABLE `user_role` (
  `user_id` bigint(20) NOT NULL,
  `role_id` bigint(20) NOT NULL,
  PRIMARY KEY (`user_id`,`role_id`),
  KEY `FKa68196081fvovjhkek5m97n3y` (`role_id`),
  CONSTRAINT `FK859n2jvi8ivhui0rl0esws6o` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKa68196081fvovjhkek5m97n3y` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.acl_entry definition

CREATE TABLE `acl_entry` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sid` bigint(20) NOT NULL,
  `audit_failure` bit(1) NOT NULL,
  `granting` bit(1) NOT NULL,
  `acl_object_identity` bigint(20) NOT NULL,
  `audit_success` bit(1) NOT NULL,
  `ace_order` int(11) NOT NULL,
  `mask` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UKce200ed06800e5a163c6ab6c0c85` (`acl_object_identity`,`ace_order`),
  KEY `FK9r4mj8ewa904g3wivff0tb5b0` (`sid`),
  CONSTRAINT `FK9r4mj8ewa904g3wivff0tb5b0` FOREIGN KEY (`sid`) REFERENCES `acl_sid` (`id`),
  CONSTRAINT `FKl39t1oqikardwghegxe0wdcpt` FOREIGN KEY (`acl_object_identity`) REFERENCES `acl_object_identity` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;


-- ar_marisma.activo definition

CREATE TABLE `activo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `descripcion2` varchar(255) DEFAULT NULL,
  `last_updated_by` varchar(255) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `valor_estrategico` int(11) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `observaciones` varchar(4000) DEFAULT NULL,
  `tipo_activo_instanciado_id` bigint(20) DEFAULT NULL,
  `marca` varchar(255) DEFAULT NULL,
  `soporte` bit(1) DEFAULT NULL,
  `activo_raiz_id` bigint(20) DEFAULT NULL,
  `coste` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `tipo_activo_instanciado2_id` bigint(20) DEFAULT NULL,
  `n_serie` varchar(255) DEFAULT NULL,
  `codigo` varchar(255) DEFAULT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `propietario` varchar(255) DEFAULT NULL,
  `codigo2` varchar(255) DEFAULT NULL,
  `tipo_activo_instanciado3_id` bigint(20) DEFAULT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKnpgslow5yh5sxa6jlqh7j7mxh` (`tipo_activo_instanciado_id`),
  KEY `FKeeovs46gy3h03rvjynj2ocqkk` (`activo_raiz_id`),
  KEY `FKmuaw8d5yvmxydf3arpfylidmy` (`tipo_activo_instanciado2_id`),
  KEY `FK6s32j7ksys62flw1ur5mxks01` (`user_id`),
  KEY `FK44nhy53gs1x7g66mlpjxd6eiy` (`tipo_activo_instanciado3_id`),
  CONSTRAINT `FK44nhy53gs1x7g66mlpjxd6eiy` FOREIGN KEY (`tipo_activo_instanciado3_id`) REFERENCES `tipo_activo_instanciado` (`id`),
  CONSTRAINT `FK6s32j7ksys62flw1ur5mxks01` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKeeovs46gy3h03rvjynj2ocqkk` FOREIGN KEY (`activo_raiz_id`) REFERENCES `activo` (`id`),
  CONSTRAINT `FKmuaw8d5yvmxydf3arpfylidmy` FOREIGN KEY (`tipo_activo_instanciado2_id`) REFERENCES `tipo_activo_instanciado` (`id`),
  CONSTRAINT `FKnpgslow5yh5sxa6jlqh7j7mxh` FOREIGN KEY (`tipo_activo_instanciado_id`) REFERENCES `tipo_activo_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


-- ar_marisma.activo_compartido definition

CREATE TABLE `activo_compartido` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `user_destino_id` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `user_propietario_id` bigint(20) NOT NULL,
  `activo_id` bigint(20) NOT NULL,
  `aceptado` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK3remtrr9qpte50dvsopqw4run` (`user_destino_id`),
  KEY `FKar7860qk0acd6b44oafp5q8cj` (`user_propietario_id`),
  KEY `FK3fpk091y81afci5vfeilcn1vy` (`activo_id`),
  CONSTRAINT `FK3fpk091y81afci5vfeilcn1vy` FOREIGN KEY (`activo_id`) REFERENCES `activo` (`id`),
  CONSTRAINT `FK3remtrr9qpte50dvsopqw4run` FOREIGN KEY (`user_destino_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKar7860qk0acd6b44oafp5q8cj` FOREIGN KEY (`user_propietario_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.activo_predefinido definition

CREATE TABLE `activo_predefinido` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `last_updated_by` varchar(255) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `valor_estrategico` int(11) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `tipo_activo_disponible_id` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `observaciones` varchar(4000) DEFAULT NULL,
  `activo_raiz_id` bigint(20) DEFAULT NULL,
  `coste` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `propietario` varchar(255) DEFAULT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  `proyecto_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKgiaq0yxbagfgfi1mece07evor` (`tipo_activo_disponible_id`),
  KEY `FK1lb6ykgsprbl0340j0judmpjn` (`activo_raiz_id`),
  KEY `FK5byc1y9jpny1ym4qy7hxl43y5` (`user_id`),
  KEY `FK7hg6eht3k458gpfjqc6wdtqok` (`proyecto_id`),
  CONSTRAINT `FK1lb6ykgsprbl0340j0judmpjn` FOREIGN KEY (`activo_raiz_id`) REFERENCES `activo_predefinido` (`id`),
  CONSTRAINT `FK5byc1y9jpny1ym4qy7hxl43y5` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FK7hg6eht3k458gpfjqc6wdtqok` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`id`),
  CONSTRAINT `FKgiaq0yxbagfgfi1mece07evor` FOREIGN KEY (`tipo_activo_disponible_id`) REFERENCES `tipo_activo_disponible` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_proyecto definition

CREATE TABLE `archivo_proyecto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `proyecto_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKe3m8fs51apntq2jmcamseex13` (`user_id`),
  KEY `FKch5da06lycyp70y4fm6d41k7` (`proyecto_id`),
  CONSTRAINT `FKch5da06lycyp70y4fm6d41k7` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`id`),
  CONSTRAINT `FKe3m8fs51apntq2jmcamseex13` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.caracteristica_control_instanciada definition

CREATE TABLE `caracteristica_control_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `tipo_caracteristica_control_instanciada_id` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK2dgwig7arin0y140r8jkapkge` (`tipo_caracteristica_control_instanciada_id`),
  KEY `FKls3t54hu8lgv5dgybq1jiraqj` (`esquema_instanciado_id`),
  CONSTRAINT `FK2dgwig7arin0y140r8jkapkge` FOREIGN KEY (`tipo_caracteristica_control_instanciada_id`) REFERENCES `tipo_caracteristica_control_instanciada` (`id`),
  CONSTRAINT `FKls3t54hu8lgv5dgybq1jiraqj` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.consultores_clientes definition

CREATE TABLE `consultores_clientes` (
  `consultor_id` bigint(20) NOT NULL,
  `cliente_id` bigint(20) DEFAULT NULL,
  KEY `FKqgblsd0ss2derklxwelwwjecw` (`cliente_id`),
  KEY `FKvsppk546ne90q4anjp7r3gti` (`consultor_id`),
  CONSTRAINT `FKqgblsd0ss2derklxwelwwjecw` FOREIGN KEY (`cliente_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKvsppk546ne90q4anjp7r3gti` FOREIGN KEY (`consultor_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.history_user_consent definition

CREATE TABLE `history_user_consent` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `info_terceros` bit(1) NOT NULL,
  `info_marisma` bit(1) NOT NULL,
  `privacidad` bit(1) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `fecha_aceptacion` datetime NOT NULL,
  `perfilado` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKm99dcxbfb1lmrniy19offik94` (`user_id`),
  CONSTRAINT `FKm99dcxbfb1lmrniy19offik94` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.municipio definition

CREATE TABLE `municipio` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `provincia_id` bigint(20) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK4ud8nsel0i9ti2kr3hboxrosg` (`provincia_id`),
  CONSTRAINT `FK4ud8nsel0i9ti2kr3hboxrosg` FOREIGN KEY (`provincia_id`) REFERENCES `provincia` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.nodo_arbol definition

CREATE TABLE `nodo_arbol` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `nivel` varchar(255) DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `porcentaje` bigint(20) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `proyecto_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKd0t3q8mac62ll0kea5sk1ybwh` (`proyecto_id`),
  CONSTRAINT `FKd0t3q8mac62ll0kea5sk1ybwh` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


-- ar_marisma.notificacion definition

CREATE TABLE `notificacion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `leido` bit(1) NOT NULL,
  `asunto` varchar(255) DEFAULT NULL,
  `usuario_origen_id` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `activo_id` bigint(20) DEFAULT NULL,
  `tipo` varchar(255) NOT NULL,
  `mensaje` text,
  `usuario_destino_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKcgyu7aygn49x83alt1qhjyh6k` (`usuario_origen_id`),
  KEY `FKd5p4fy5tsfsu2htccy3q0gv3s` (`activo_id`),
  KEY `FK69pu9tnc5rq51imekrkylqt0j` (`usuario_destino_id`),
  CONSTRAINT `FK69pu9tnc5rq51imekrkylqt0j` FOREIGN KEY (`usuario_destino_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKcgyu7aygn49x83alt1qhjyh6k` FOREIGN KEY (`usuario_origen_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKd5p4fy5tsfsu2htccy3q0gv3s` FOREIGN KEY (`activo_id`) REFERENCES `activo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.novedad_usuarios definition

CREATE TABLE `novedad_usuarios` (
  `novedad_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`novedad_id`,`user_id`),
  KEY `FKgbsrv3sqkve5lmyqsxllrtsui` (`user_id`),
  CONSTRAINT `FK10omd06bc5xk9nivs83gtyie9` FOREIGN KEY (`novedad_id`) REFERENCES `novedad` (`id`),
  CONSTRAINT `FKgbsrv3sqkve5lmyqsxllrtsui` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.probabilidad_ocurrencia_instanciada definition

CREATE TABLE `probabilidad_ocurrencia_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `rango_minimo` double NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `temporalidad_instanciada_id` bigint(20) NOT NULL,
  `rango_maximo` double NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `color` varchar(255) NOT NULL,
  `etiqueta` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKev0l6jl7ain9s9hmh8pu6swrw` (`esquema_instanciado_id`),
  KEY `FKot8hrnf57mouae3trxvyg4xcg` (`temporalidad_instanciada_id`),
  CONSTRAINT `FKev0l6jl7ain9s9hmh8pu6swrw` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`),
  CONSTRAINT `FKot8hrnf57mouae3trxvyg4xcg` FOREIGN KEY (`temporalidad_instanciada_id`) REFERENCES `temporalidad_instanciada` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;


-- ar_marisma.solicitud_estudiante definition

CREATE TABLE `solicitud_estudiante` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `rechazado` bit(1) NOT NULL,
  `aprobado` bit(1) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `fecha_validacion` datetime DEFAULT NULL,
  `ampliacion` bit(1) NOT NULL,
  `correo_justificacion` bit(1) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `meses` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKp4ghue7u9bqtno610y7md3onh` (`user_id`),
  CONSTRAINT `FKp4ghue7u9bqtno610y7md3onh` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.subproyecto definition

CREATE TABLE `subproyecto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `full_path` varchar(255) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `estado_calculo` varchar(255) DEFAULT NULL,
  `responsable` varchar(255) NOT NULL,
  `alcance` varchar(4000) DEFAULT NULL,
  `recomendacion` varchar(4000) DEFAULT NULL,
  `nodo_arbol_id` bigint(20) DEFAULT NULL,
  `auto_import` bit(1) NOT NULL,
  `observacion` varchar(4000) DEFAULT NULL,
  `destinatario` varchar(255) NOT NULL,
  `autoria_institucional` varchar(255) NOT NULL,
  `codigo` varchar(255) NOT NULL,
  `cnae_id` bigint(20) NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKr0sk4j3w8w94tjc31botgmxby` (`esquema_instanciado_id`),
  KEY `FKcug963vxfwn8jd5owjjda9pb8` (`nodo_arbol_id`),
  KEY `FK7wn8ukfx2dya071y7hqy89kqw` (`cnae_id`),
  CONSTRAINT `FK7wn8ukfx2dya071y7hqy89kqw` FOREIGN KEY (`cnae_id`) REFERENCES `cnae` (`id`),
  CONSTRAINT `FKcug963vxfwn8jd5owjjda9pb8` FOREIGN KEY (`nodo_arbol_id`) REFERENCES `nodo_arbol` (`id`),
  CONSTRAINT `FKr0sk4j3w8w94tjc31botgmxby` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- ar_marisma.user_nodos_arbol definition

CREATE TABLE `user_nodos_arbol` (
  `nodo_arbol_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`user_id`,`nodo_arbol_id`),
  KEY `FKo2bse6hflf26c0qq1qy67flnm` (`nodo_arbol_id`),
  CONSTRAINT `FKc6v0n16bj9pt9w3tulhyvxb7j` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKo2bse6hflf26c0qq1qy67flnm` FOREIGN KEY (`nodo_arbol_id`) REFERENCES `nodo_arbol` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.user_subproyectos definition

CREATE TABLE `user_subproyectos` (
  `subproyecto_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`user_id`,`subproyecto_id`),
  KEY `FKq69wqny8p32yn3ki4ov8qtqkw` (`subproyecto_id`),
  CONSTRAINT `FKm79nf5svkgtmew4bb6vbvdobo` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKq69wqny8p32yn3ki4ov8qtqkw` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.user_subscription definition

CREATE TABLE `user_subscription` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `processing` bit(1) NOT NULL,
  `pais_id` bigint(20) DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `current_period_end` datetime DEFAULT NULL,
  `plan_elegido` bit(1) NOT NULL,
  `plan_id` varchar(255) DEFAULT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  `show_modal` bit(1) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `provincia_id` bigint(20) DEFAULT NULL,
  `canceled` bit(1) NOT NULL,
  `customer_id` varchar(255) DEFAULT NULL,
  `cantidad_contratada` int(11) NOT NULL,
  `municipio_id` bigint(20) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `unpaid` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKgpbjo758shii3ame6xokpc14p` (`pais_id`),
  KEY `FKpsiiu2nyr0cbxeluuouw474s9` (`user_id`),
  KEY `FKifavlwnx5oiw7s0lsmr9tsj4j` (`provincia_id`),
  KEY `FKls4it9i6jt9pt6m1axbkxjmyk` (`municipio_id`),
  CONSTRAINT `FKgpbjo758shii3ame6xokpc14p` FOREIGN KEY (`pais_id`) REFERENCES `pais` (`id`),
  CONSTRAINT `FKifavlwnx5oiw7s0lsmr9tsj4j` FOREIGN KEY (`provincia_id`) REFERENCES `provincia` (`id`),
  CONSTRAINT `FKls4it9i6jt9pt6m1axbkxjmyk` FOREIGN KEY (`municipio_id`) REFERENCES `municipio` (`id`),
  CONSTRAINT `FKpsiiu2nyr0cbxeluuouw474s9` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.agrupacion_checklist definition

CREATE TABLE `agrupacion_checklist` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `estado` varchar(255) NOT NULL DEFAULT 'vacio',
  `cobertura` float NOT NULL,
  `deleted` bit(1) NOT NULL,
  `exito` float DEFAULT NULL,
  `nombre_grupo_activos` varchar(255) DEFAULT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKqas2xk3ee3dg4stg4vcujccd1` (`subproyecto_id`),
  CONSTRAINT `FKqas2xk3ee3dg4stg4vcujccd1` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- ar_marisma.amenaza_instanciada definition

CREATE TABLE `amenaza_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  `porcentaje_degradacion_instanciado_id` bigint(20) DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `probabilidad_ocurrencia_instanciada_id` bigint(20) DEFAULT NULL,
  `tipo_amenaza_instanciada_id` bigint(20) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKc6rtvowutwucedg3r3r5wh77` (`subproyecto_id`),
  KEY `FK15vkc6hiwkn4yruji0im0faft` (`porcentaje_degradacion_instanciado_id`),
  KEY `FK1bu77iil7w9cqw0v2e0utbllh` (`probabilidad_ocurrencia_instanciada_id`),
  KEY `FKnwm9f36klv6acmqc0757j0r5l` (`tipo_amenaza_instanciada_id`),
  CONSTRAINT `FK15vkc6hiwkn4yruji0im0faft` FOREIGN KEY (`porcentaje_degradacion_instanciado_id`) REFERENCES `porcentaje_degradacion_instanciado` (`id`),
  CONSTRAINT `FK1bu77iil7w9cqw0v2e0utbllh` FOREIGN KEY (`probabilidad_ocurrencia_instanciada_id`) REFERENCES `probabilidad_ocurrencia_instanciada` (`id`),
  CONSTRAINT `FKc6rtvowutwucedg3r3r5wh77` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKnwm9f36klv6acmqc0757j0r5l` FOREIGN KEY (`tipo_amenaza_instanciada_id`) REFERENCES `tipo_amenaza_instanciada` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=281 DEFAULT CHARSET=utf8;


-- ar_marisma.analisis_riesgo_lanzamientos definition

CREATE TABLE `analisis_riesgo_lanzamientos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `fecha_lanzamiento` datetime NOT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKscubgnthhwiiqq8ad9d6l4if3` (`subproyecto_id`),
  CONSTRAINT `FKscubgnthhwiiqq8ad9d6l4if3` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;


-- ar_marisma.analisisnmap definition

CREATE TABLE `analisisnmap` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `fecha_ejecucion` datetime NOT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `activo_id` bigint(20) NOT NULL,
  `objetivo` varchar(255) NOT NULL,
  `estado_resultado` varchar(255) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `resultado` longtext,
  PRIMARY KEY (`id`),
  KEY `FKkipldes6tljc0ansv9t0255u0` (`subproyecto_id`),
  KEY `FKe7jf87fae941emvohw77966cx` (`activo_id`),
  KEY `FK9e3ojxyqgm9jsf195hf3tq0du` (`user_id`),
  CONSTRAINT `FK9e3ojxyqgm9jsf195hf3tq0du` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKe7jf87fae941emvohw77966cx` FOREIGN KEY (`activo_id`) REFERENCES `activo` (`id`),
  CONSTRAINT `FKkipldes6tljc0ansv9t0255u0` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.analisisowasp definition

CREATE TABLE `analisisowasp` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `activo_id` bigint(20) NOT NULL,
  `estado_resultado` varchar(255) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `fecha_ejecucion` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK622q3c1itosu9eheu9cij9cj7` (`subproyecto_id`),
  KEY `FKipogksad52nunu2scah5novwr` (`activo_id`),
  KEY `FKnjg5g6jqgisvccjlmk2dwv7pu` (`user_id`),
  CONSTRAINT `FK622q3c1itosu9eheu9cij9cj7` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKipogksad52nunu2scah5novwr` FOREIGN KEY (`activo_id`) REFERENCES `activo` (`id`),
  CONSTRAINT `FKnjg5g6jqgisvccjlmk2dwv7pu` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo definition

CREATE TABLE `archivo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `vinculado` bit(1) NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `proyecto_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKajnd1qjngsxce1fp5xnnvacse` (`subproyecto_id`),
  KEY `FKfar4ijj9ykj20abfat026us2q` (`user_id`),
  KEY `FKdtddnpcviptyntj5tr6hkgpe0` (`proyecto_id`),
  CONSTRAINT `FKajnd1qjngsxce1fp5xnnvacse` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKdtddnpcviptyntj5tr6hkgpe0` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`id`),
  CONSTRAINT `FKfar4ijj9ykj20abfat026us2q` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.auditoria definition

CREATE TABLE `auditoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_updated` datetime NOT NULL,
  `date_created` datetime NOT NULL,
  `period_beginning` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `responsable` varchar(255) NOT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `tipo` varchar(255) NOT NULL,
  `period_ending` datetime DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKgb32neb8suchxo30ldc0502r2` (`subproyecto_id`),
  CONSTRAINT `FKgb32neb8suchxo30ldc0502r2` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.chat definition

CREATE TABLE `chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `leido` bit(1) NOT NULL,
  `date_created` datetime NOT NULL,
  `emisor_id` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  `destinatario_id` bigint(20) DEFAULT NULL,
  `mensaje` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKmynxqflkotqdwav2dbugv6dxj` (`emisor_id`),
  KEY `FK75uod3t20tnr6riwfia299jrm` (`subproyecto_id`),
  KEY `FKduvcty62fn20jhcwrx05yv98u` (`destinatario_id`),
  CONSTRAINT `FK75uod3t20tnr6riwfia299jrm` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKduvcty62fn20jhcwrx05yv98u` FOREIGN KEY (`destinatario_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKmynxqflkotqdwav2dbugv6dxj` FOREIGN KEY (`emisor_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.dimension_tipo_activo_amenaza_instanciado definition

CREATE TABLE `dimension_tipo_activo_amenaza_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `amenaza_instanciada_id` bigint(20) NOT NULL,
  `tipo_activo_instanciado_id` bigint(20) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `dimension_instanciada_id` bigint(20) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKigo70byjsmvbvt3vhcryjxmq0` (`esquema_instanciado_id`),
  KEY `FKs5mg24in70kx2pqk3d6o05hds` (`amenaza_instanciada_id`),
  KEY `FKr4k2swsfnoou5e0q689stqwqk` (`tipo_activo_instanciado_id`),
  KEY `FK95it4c1h411k9vs33k2xrxns6` (`dimension_instanciada_id`),
  CONSTRAINT `FK95it4c1h411k9vs33k2xrxns6` FOREIGN KEY (`dimension_instanciada_id`) REFERENCES `dimension_instanciada` (`id`),
  CONSTRAINT `FKigo70byjsmvbvt3vhcryjxmq0` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`),
  CONSTRAINT `FKr4k2swsfnoou5e0q689stqwqk` FOREIGN KEY (`tipo_activo_instanciado_id`) REFERENCES `tipo_activo_instanciado` (`id`),
  CONSTRAINT `FKs5mg24in70kx2pqk3d6o05hds` FOREIGN KEY (`amenaza_instanciada_id`) REFERENCES `amenaza_instanciada` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=575 DEFAULT CHARSET=utf8;


-- ar_marisma.dominio_instanciado definition

CREATE TABLE `dominio_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `conclusion` varchar(4000) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK5xn41mpss6ms7e43hjbw4kpuw` (`esquema_instanciado_id`),
  KEY `FKg0cu9s2m3mqx9rvd61n9vbrm5` (`subproyecto_id`),
  CONSTRAINT `FK5xn41mpss6ms7e43hjbw4kpuw` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`),
  CONSTRAINT `FKg0cu9s2m3mqx9rvd61n9vbrm5` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;


-- ar_marisma.evento definition

CREATE TABLE `evento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `fecha_verificacion` datetime DEFAULT NULL,
  `valido` bit(1) DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `verificado` bit(1) DEFAULT NULL,
  `responsable` varchar(255) NOT NULL,
  `conclusion` varchar(4000) DEFAULT NULL,
  `solucion` varchar(4000) DEFAULT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `fecha_cierre` datetime DEFAULT NULL,
  `fecha_estimada_solucion` datetime DEFAULT NULL,
  `usuario_id` bigint(20) DEFAULT NULL,
  `coste` varchar(255) DEFAULT NULL,
  `codigo` varchar(255) DEFAULT NULL,
  `causa` varchar(4000) NOT NULL,
  `descripcion` varchar(4000) NOT NULL,
  `cerrado` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKhowuytmm1k8cw74in536iiiuw` (`subproyecto_id`),
  KEY `FKj5b30hh6y693xsugfdqyvewud` (`usuario_id`),
  CONSTRAINT `FKhowuytmm1k8cw74in536iiiuw` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKj5b30hh6y693xsugfdqyvewud` FOREIGN KEY (`usuario_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;


-- ar_marisma.objetivo_instanciado definition

CREATE TABLE `objetivo_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `dominio_instanciado_id` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKf4ck6mlhvhbtb8f0tf5eq0he2` (`dominio_instanciado_id`),
  CONSTRAINT `FKf4ck6mlhvhbtb8f0tf5eq0he2` FOREIGN KEY (`dominio_instanciado_id`) REFERENCES `dominio_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;


-- ar_marisma.plan_tratamientolanzamientos definition

CREATE TABLE `plan_tratamientolanzamientos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `fecha_fin_lanzamiento` datetime DEFAULT NULL,
  `fecha_lanzamiento` datetime NOT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `nivelvr` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKao4fpa3hdt10hq968cy61miu` (`subproyecto_id`),
  CONSTRAINT `FKao4fpa3hdt10hq968cy61miu` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


-- ar_marisma.porcentaje_ajuste definition

CREATE TABLE `porcentaje_ajuste` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `ajuste` decimal(19,2) NOT NULL,
  `signo` int(11) NOT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `tipo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKqpy5lf58a5qwyd1l5703i5go7` (`subproyecto_id`),
  CONSTRAINT `FKqpy5lf58a5qwyd1l5703i5go7` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;


-- ar_marisma.resultado_puerto definition

CREATE TABLE `resultado_puerto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `version_servicio` varchar(255) DEFAULT NULL,
  `informacion` varchar(255) DEFAULT NULL,
  `puerto` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `servicio` varchar(255) DEFAULT NULL,
  `analisisnmap_id` bigint(20) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK2s0tybosltxrdg8l0uew6fof9` (`analisisnmap_id`),
  CONSTRAINT `FK2s0tybosltxrdg8l0uew6fof9` FOREIGN KEY (`analisisnmap_id`) REFERENCES `analisisnmap` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.activo_amenaza definition

CREATE TABLE `activo_amenaza` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `amenaza_instanciada_id` bigint(20) NOT NULL,
  `valor` decimal(19,2) DEFAULT NULL,
  `activo_id` bigint(20) NOT NULL,
  `editado` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK3gte8a7t7819nbxfx5mu16xlh` (`amenaza_instanciada_id`),
  KEY `FKqfrtsr2t9e5yui4qwdwqpbe0x` (`activo_id`),
  CONSTRAINT `FK3gte8a7t7819nbxfx5mu16xlh` FOREIGN KEY (`amenaza_instanciada_id`) REFERENCES `amenaza_instanciada` (`id`),
  CONSTRAINT `FKqfrtsr2t9e5yui4qwdwqpbe0x` FOREIGN KEY (`activo_id`) REFERENCES `activo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;


-- ar_marisma.activo_amenaza_dimension definition

CREATE TABLE `activo_amenaza_dimension` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `valor` int(11) NOT NULL,
  `dimension_instanciada_id` bigint(20) DEFAULT NULL,
  `editado` bit(1) NOT NULL,
  `activo_amenaza_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKordx8byjmqfrpd06509ne6ot1` (`dimension_instanciada_id`),
  KEY `FKo6j6ah1xxwfi3rldkjsblqtlq` (`activo_amenaza_id`),
  CONSTRAINT `FKo6j6ah1xxwfi3rldkjsblqtlq` FOREIGN KEY (`activo_amenaza_id`) REFERENCES `activo_amenaza` (`id`),
  CONSTRAINT `FKordx8byjmqfrpd06509ne6ot1` FOREIGN KEY (`dimension_instanciada_id`) REFERENCES `dimension_instanciada` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;


-- ar_marisma.activo_auditoria definition

CREATE TABLE `activo_auditoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `tipo_activo_instanciado_id` bigint(20) NOT NULL,
  `agrupado` bit(1) NOT NULL,
  `activo_auditoria_raiz_id` bigint(20) DEFAULT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `activo_id` bigint(20) NOT NULL,
  `agrupacion_checklist_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK6e3b12e4c526bc59c0600fa9a1ee` (`subproyecto_id`,`activo_id`),
  KEY `FKebuoxoq9ryuhbixaq4sn75ich` (`tipo_activo_instanciado_id`),
  KEY `FKfpjbtmilgestwky57cg1l0pk1` (`activo_auditoria_raiz_id`),
  KEY `FKtqfntw9prkje2bsx3tup1vct2` (`activo_id`),
  KEY `FKp977o0yhk5y7r4pytmwqpk5sk` (`agrupacion_checklist_id`),
  CONSTRAINT `FKebuoxoq9ryuhbixaq4sn75ich` FOREIGN KEY (`tipo_activo_instanciado_id`) REFERENCES `tipo_activo_instanciado` (`id`),
  CONSTRAINT `FKfpjbtmilgestwky57cg1l0pk1` FOREIGN KEY (`activo_auditoria_raiz_id`) REFERENCES `activo_auditoria` (`id`),
  CONSTRAINT `FKp977o0yhk5y7r4pytmwqpk5sk` FOREIGN KEY (`agrupacion_checklist_id`) REFERENCES `agrupacion_checklist` (`id`),
  CONSTRAINT `FKr2t2sayu5afogixd9q9dax2ju` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKtqfntw9prkje2bsx3tup1vct2` FOREIGN KEY (`activo_id`) REFERENCES `activo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- ar_marisma.analisis_riesgo definition

CREATE TABLE `analisis_riesgo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `vulnerabilidad` float NOT NULL,
  `riesgo_inherente` float NOT NULL,
  `impacto_total` float NOT NULL,
  `deleted` bit(1) NOT NULL,
  `riesgo` float NOT NULL,
  `valor_riesgo` float NOT NULL,
  `impacto` float NOT NULL,
  `activo_amenaza_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK1e0mvx7p020lhastucuxg86jo` (`activo_amenaza_id`),
  CONSTRAINT `FK1e0mvx7p020lhastucuxg86jo` FOREIGN KEY (`activo_amenaza_id`) REFERENCES `activo_amenaza` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_auditoria definition

CREATE TABLE `archivo_auditoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `vinculado` bit(1) NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `auditoria_id` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKl6r3qb245mctw6e0qd5cy8uo6` (`auditoria_id`),
  KEY `FKwxwdqpa7myy7qo5mxvoob2y7` (`subproyecto_id`),
  KEY `FKow4cit36jn1g2dtqlcyjetdal` (`user_id`),
  CONSTRAINT `FKl6r3qb245mctw6e0qd5cy8uo6` FOREIGN KEY (`auditoria_id`) REFERENCES `auditoria` (`id`),
  CONSTRAINT `FKow4cit36jn1g2dtqlcyjetdal` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKwxwdqpa7myy7qo5mxvoob2y7` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_evento definition

CREATE TABLE `archivo_evento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `vinculado` bit(1) NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `evento_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKfowk4tvu09o7ryn27mnn1xrie` (`user_id`),
  KEY `FKhap42uj765habmhu2ahrx406r` (`evento_id`),
  CONSTRAINT `FKfowk4tvu09o7ryn27mnn1xrie` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKhap42uj765habmhu2ahrx406r` FOREIGN KEY (`evento_id`) REFERENCES `evento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.control_instanciado definition

CREATE TABLE `control_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `objetivo_instanciado_id` bigint(20) NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK59dvq92cw629vhr3s1lju972l` (`objetivo_instanciado_id`),
  CONSTRAINT `FK59dvq92cw629vhr3s1lju972l` FOREIGN KEY (`objetivo_instanciado_id`) REFERENCES `objetivo_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;


-- ar_marisma.cve definition

CREATE TABLE `cve` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `resultado_puerto_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK1ykubv37svny86hes810ow38w` (`resultado_puerto_id`),
  CONSTRAINT `FK1ykubv37svny86hes810ow38w` FOREIGN KEY (`resultado_puerto_id`) REFERENCES `resultado_puerto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.dominio_auditoria definition

CREATE TABLE `dominio_auditoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `dominio_instanciado_id` bigint(20) NOT NULL,
  `cobertura` float NOT NULL,
  `deleted` bit(1) NOT NULL,
  `exito` float DEFAULT NULL,
  `agrupacion_checklist_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKkvg8bp1dco2f0k7ao6n0jd5q6` (`dominio_instanciado_id`),
  KEY `FKut4bjyb2dw0h2d4v48e2fokm` (`agrupacion_checklist_id`),
  CONSTRAINT `FKkvg8bp1dco2f0k7ao6n0jd5q6` FOREIGN KEY (`dominio_instanciado_id`) REFERENCES `dominio_instanciado` (`id`),
  CONSTRAINT `FKut4bjyb2dw0h2d4v48e2fokm` FOREIGN KEY (`agrupacion_checklist_id`) REFERENCES `agrupacion_checklist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;


-- ar_marisma.incidente definition

CREATE TABLE `incidente` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `porcentaje_ajuste_id` bigint(20) DEFAULT NULL,
  `amenaza_instanciada_id` bigint(20) DEFAULT NULL,
  `gravedad` varchar(255) NOT NULL,
  `evento_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK8y9n3rn3a2aej1e74dwl6jm8c` (`porcentaje_ajuste_id`),
  KEY `FKg5eh36dl6pxtuo3gy2321x8f2` (`amenaza_instanciada_id`),
  KEY `FKmvpiqi7j0d1fyi46m50k357fi` (`evento_id`),
  CONSTRAINT `FK8y9n3rn3a2aej1e74dwl6jm8c` FOREIGN KEY (`porcentaje_ajuste_id`) REFERENCES `porcentaje_ajuste` (`id`),
  CONSTRAINT `FKg5eh36dl6pxtuo3gy2321x8f2` FOREIGN KEY (`amenaza_instanciada_id`) REFERENCES `amenaza_instanciada` (`id`),
  CONSTRAINT `FKmvpiqi7j0d1fyi46m50k357fi` FOREIGN KEY (`evento_id`) REFERENCES `evento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;


-- ar_marisma.incidente_activo definition

CREATE TABLE `incidente_activo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `activo_id` bigint(20) NOT NULL,
  `agrupacion_checklist_id` bigint(20) DEFAULT NULL,
  `incidente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKbnfhdce0j1hewly8fsqr3whha` (`activo_id`),
  KEY `FK1nuod4e3i9f1q4oann6al5q9d` (`agrupacion_checklist_id`),
  KEY `FK746dxyf0xk1v3iy54xgtrrblr` (`incidente_id`),
  CONSTRAINT `FK1nuod4e3i9f1q4oann6al5q9d` FOREIGN KEY (`agrupacion_checklist_id`) REFERENCES `agrupacion_checklist` (`id`),
  CONSTRAINT `FK746dxyf0xk1v3iy54xgtrrblr` FOREIGN KEY (`incidente_id`) REFERENCES `incidente` (`id`),
  CONSTRAINT `FKbnfhdce0j1hewly8fsqr3whha` FOREIGN KEY (`activo_id`) REFERENCES `activo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;


-- ar_marisma.incidente_activo_dimension definition

CREATE TABLE `incidente_activo_dimension` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `porcentaje_degradacion` int(11) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `porcentaje_degradacion_instanciado_id` bigint(20) DEFAULT NULL,
  `incidente_activo_id` bigint(20) NOT NULL,
  `dimension_instanciada_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKqi3foq9p0i63s7s01v47jtg6r` (`porcentaje_degradacion_instanciado_id`),
  KEY `FKmrt34qx9pk3es0dgr3w185nsn` (`incidente_activo_id`),
  KEY `FKbcyshpyxn1u21k48q0rau3a02` (`dimension_instanciada_id`),
  CONSTRAINT `FKbcyshpyxn1u21k48q0rau3a02` FOREIGN KEY (`dimension_instanciada_id`) REFERENCES `dimension_instanciada` (`id`),
  CONSTRAINT `FKmrt34qx9pk3es0dgr3w185nsn` FOREIGN KEY (`incidente_activo_id`) REFERENCES `incidente_activo` (`id`),
  CONSTRAINT `FKqi3foq9p0i63s7s01v47jtg6r` FOREIGN KEY (`porcentaje_degradacion_instanciado_id`) REFERENCES `porcentaje_degradacion_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;


-- ar_marisma.no_conformidad definition

CREATE TABLE `no_conformidad` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `last_updated_by` varchar(255) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `acciones_correctivas` text,
  `fecha_implantacion` datetime DEFAULT NULL,
  `requierepac` bit(1) NOT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `analisis` text,
  `accion_inmediata` text,
  `codigo` varchar(255) NOT NULL,
  `control_instanciado_id` bigint(20) NOT NULL,
  `descripcion` text,
  `created_by` varchar(255) DEFAULT NULL,
  `requiere_evidencias` bit(1) NOT NULL,
  `responsable_implantacion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKno564dbe4ke3xhko9qxpiern7` (`subproyecto_id`),
  KEY `FKk6p1hsvdeawmtm6x94s0oyrgt` (`control_instanciado_id`),
  CONSTRAINT `FKk6p1hsvdeawmtm6x94s0oyrgt` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKno564dbe4ke3xhko9qxpiern7` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.objetivo_amenaza_instanciado definition

CREATE TABLE `objetivo_amenaza_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `objetivo_instanciado_id` bigint(20) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `porcentaje` int(11) DEFAULT NULL,
  `amenaza_instanciada_id` bigint(20) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK899sptb8brn4f46m5qt0l0f17` (`esquema_instanciado_id`),
  KEY `FK51q60y24txge29px9dutb2oqx` (`objetivo_instanciado_id`),
  KEY `FKcx7v7y92kciagx44ny10hv07m` (`amenaza_instanciada_id`),
  CONSTRAINT `FK51q60y24txge29px9dutb2oqx` FOREIGN KEY (`objetivo_instanciado_id`) REFERENCES `objetivo_instanciado` (`id`),
  CONSTRAINT `FK899sptb8brn4f46m5qt0l0f17` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`),
  CONSTRAINT `FKcx7v7y92kciagx44ny10hv07m` FOREIGN KEY (`amenaza_instanciada_id`) REFERENCES `amenaza_instanciada` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.objetivo_auditoria definition

CREATE TABLE `objetivo_auditoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `cobertura` float NOT NULL,
  `deleted` bit(1) NOT NULL,
  `exito` float DEFAULT NULL,
  `dominio_auditoria_id` bigint(20) DEFAULT NULL,
  `objetivo_instanciado_id` bigint(20) NOT NULL,
  `agrupacion_checklist_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKs7ilkoggbr5tso1a67ts5o3u1` (`dominio_auditoria_id`),
  KEY `FKk71mor9d8dq7vxu33w05ccba4` (`objetivo_instanciado_id`),
  KEY `FKb0jodya02qqldquux2gvgtdr5` (`agrupacion_checklist_id`),
  CONSTRAINT `FKb0jodya02qqldquux2gvgtdr5` FOREIGN KEY (`agrupacion_checklist_id`) REFERENCES `agrupacion_checklist` (`id`),
  CONSTRAINT `FKk71mor9d8dq7vxu33w05ccba4` FOREIGN KEY (`objetivo_instanciado_id`) REFERENCES `objetivo_instanciado` (`id`),
  CONSTRAINT `FKs7ilkoggbr5tso1a67ts5o3u1` FOREIGN KEY (`dominio_auditoria_id`) REFERENCES `dominio_auditoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;


-- ar_marisma.recomendacion_instanciada definition

CREATE TABLE `recomendacion_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `rango_instanciado_id` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `control_instanciado_id` bigint(20) NOT NULL,
  `recomendacion` varchar(4000) DEFAULT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKrp8btr70lpbb8oaj2cqc9sedu` (`rango_instanciado_id`),
  KEY `FKria12nramxosbr2hkse8pexba` (`control_instanciado_id`),
  CONSTRAINT `FKria12nramxosbr2hkse8pexba` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKrp8btr70lpbb8oaj2cqc9sedu` FOREIGN KEY (`rango_instanciado_id`) REFERENCES `rango_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8;


-- ar_marisma.soa definition

CREATE TABLE `soa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `control_instanciado_id` bigint(20) NOT NULL,
  `implementacion` varchar(255) DEFAULT NULL,
  `aplica` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKhqneoc9twnxmmp2eyjn09i995` (`subproyecto_id`),
  KEY `FKkqrh9qvdbpc4ord2b055kswkv` (`control_instanciado_id`),
  CONSTRAINT `FKhqneoc9twnxmmp2eyjn09i995` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKkqrh9qvdbpc4ord2b055kswkv` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;


-- ar_marisma.sugerencia definition

CREATE TABLE `sugerencia` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `probabilidad_ocurrencia_anterior_id` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `probabilidad_ocurrencia_sugerida_id` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `estado` varchar(255) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `incidente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FKfikma6oj2xnbwvoo2pkw3devr` (`probabilidad_ocurrencia_anterior_id`),
  KEY `FKjdowin5wxfte732ddxlm6qsf6` (`probabilidad_ocurrencia_sugerida_id`),
  KEY `FKr9lsendf6m0mmwianrgskfkty` (`incidente_id`),
  CONSTRAINT `FKfikma6oj2xnbwvoo2pkw3devr` FOREIGN KEY (`probabilidad_ocurrencia_anterior_id`) REFERENCES `probabilidad_ocurrencia_instanciada` (`id`),
  CONSTRAINT `FKjdowin5wxfte732ddxlm6qsf6` FOREIGN KEY (`probabilidad_ocurrencia_sugerida_id`) REFERENCES `probabilidad_ocurrencia_instanciada` (`id`),
  CONSTRAINT `FKr9lsendf6m0mmwianrgskfkty` FOREIGN KEY (`incidente_id`) REFERENCES `incidente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;


-- ar_marisma.sugerencia_mejoras definition

CREATE TABLE `sugerencia_mejoras` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `resultados` text,
  `last_updated_by` varchar(255) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `fecha_implantacion` datetime DEFAULT NULL,
  `requierepac` bit(1) NOT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `codigo` varchar(4000) DEFAULT NULL,
  `control_instanciado_id` bigint(20) NOT NULL,
  `acciones_previstas` text,
  `descripcion` text,
  `created_by` varchar(255) DEFAULT NULL,
  `requiere_evidencias` bit(1) NOT NULL,
  `responsable_implantacion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK5fxknypaomgcruptjtsdcnjoq` (`subproyecto_id`),
  KEY `FKtr87wem1d2esd6358pc2o6tuf` (`control_instanciado_id`),
  CONSTRAINT `FK5fxknypaomgcruptjtsdcnjoq` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKtr87wem1d2esd6358pc2o6tuf` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_control_instanciado definition

CREATE TABLE `archivo_control_instanciado` (
  `archivo_controles_vinculados_id` bigint(20) NOT NULL,
  `control_instanciado_id` bigint(20) DEFAULT NULL,
  KEY `FKn6wkflan6prxusvfu4yceo2g6` (`control_instanciado_id`),
  KEY `FKk94ttkvbr8regv9d4g9cfhp1l` (`archivo_controles_vinculados_id`),
  CONSTRAINT `FKk94ttkvbr8regv9d4g9cfhp1l` FOREIGN KEY (`archivo_controles_vinculados_id`) REFERENCES `archivo` (`id`),
  CONSTRAINT `FKn6wkflan6prxusvfu4yceo2g6` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_evento_control_instanciado definition

CREATE TABLE `archivo_evento_control_instanciado` (
  `archivo_evento_controles_vinculados_id` bigint(20) NOT NULL,
  `control_instanciado_id` bigint(20) DEFAULT NULL,
  KEY `FKseygkqrbkkx6lc9pou8xx7xlb` (`control_instanciado_id`),
  KEY `FKacew7ebkdj28lh7qv0yu43stx` (`archivo_evento_controles_vinculados_id`),
  CONSTRAINT `FKacew7ebkdj28lh7qv0yu43stx` FOREIGN KEY (`archivo_evento_controles_vinculados_id`) REFERENCES `archivo_evento` (`id`),
  CONSTRAINT `FKseygkqrbkkx6lc9pou8xx7xlb` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_no_conformidad definition

CREATE TABLE `archivo_no_conformidad` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `vinculado` bit(1) NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `no_conformidad_id` bigint(20) DEFAULT NULL,
  `file_name` varchar(255) NOT NULL,
  `evidencia_reparadora` bit(1) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `evidencia_correctiva` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK7v8hu6qsqy14m06llq1j6goqx` (`no_conformidad_id`),
  KEY `FKrmymoyrxcjkreslyv7jo50ewt` (`user_id`),
  CONSTRAINT `FK7v8hu6qsqy14m06llq1j6goqx` FOREIGN KEY (`no_conformidad_id`) REFERENCES `no_conformidad` (`id`),
  CONSTRAINT `FKrmymoyrxcjkreslyv7jo50ewt` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_no_conformidad_control_instanciado definition

CREATE TABLE `archivo_no_conformidad_control_instanciado` (
  `archivo_no_conformidad_controles_vinculados_id` bigint(20) NOT NULL,
  `control_instanciado_id` bigint(20) DEFAULT NULL,
  KEY `FKb2b31h74tiuueaxjo4k3li3cm` (`control_instanciado_id`),
  KEY `FKbb8e8gmgjgdb9e2d2s7kqky4a` (`archivo_no_conformidad_controles_vinculados_id`),
  CONSTRAINT `FKb2b31h74tiuueaxjo4k3li3cm` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKbb8e8gmgjgdb9e2d2s7kqky4a` FOREIGN KEY (`archivo_no_conformidad_controles_vinculados_id`) REFERENCES `archivo_no_conformidad` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_sugerencia_mejoras definition

CREATE TABLE `archivo_sugerencia_mejoras` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `sugerencia_mejoras_id` bigint(20) DEFAULT NULL,
  `vinculado` bit(1) NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKi14n8yckwiasldav5kduqq1r1` (`sugerencia_mejoras_id`),
  KEY `FKqys7rd1g2hmdimt058juwews5` (`user_id`),
  CONSTRAINT `FKi14n8yckwiasldav5kduqq1r1` FOREIGN KEY (`sugerencia_mejoras_id`) REFERENCES `sugerencia_mejoras` (`id`),
  CONSTRAINT `FKqys7rd1g2hmdimt058juwews5` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_sugerencia_mejoras_control_instanciado definition

CREATE TABLE `archivo_sugerencia_mejoras_control_instanciado` (
  `archivo_sugerencia_mejoras_controles_vinculados_id` bigint(20) NOT NULL,
  `control_instanciado_id` bigint(20) DEFAULT NULL,
  KEY `FK2yv7qj9tt9n5ax8oekb4mmbas` (`control_instanciado_id`),
  KEY `FKp5lhoqxe7reeef4o71j4xadck` (`archivo_sugerencia_mejoras_controles_vinculados_id`),
  CONSTRAINT `FK2yv7qj9tt9n5ax8oekb4mmbas` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKp5lhoqxe7reeef4o71j4xadck` FOREIGN KEY (`archivo_sugerencia_mejoras_controles_vinculados_id`) REFERENCES `archivo_sugerencia_mejoras` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.checklist_instanciado definition

CREATE TABLE `checklist_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `codigo` varchar(255) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `control_instanciado_id` bigint(20) NOT NULL,
  `descripcion` varchar(4000) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKsfy9o6ctexodtp0ylx84bhps5` (`control_instanciado_id`),
  CONSTRAINT `FKsfy9o6ctexodtp0ylx84bhps5` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8;


-- ar_marisma.control_amenaza_instanciado definition

CREATE TABLE `control_amenaza_instanciado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `control_instanciado_id` bigint(20) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `porcentaje` int(11) DEFAULT NULL,
  `amenaza_instanciada_id` bigint(20) NOT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK41w0vrs2p796r8n4rvtjn7o02` (`esquema_instanciado_id`),
  KEY `FK4s2mnmutebgrjafkyn6xuwvu7` (`control_instanciado_id`),
  KEY `FKai74mpk99i7b5wc1rn15l994o` (`amenaza_instanciada_id`),
  CONSTRAINT `FK41w0vrs2p796r8n4rvtjn7o02` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`),
  CONSTRAINT `FK4s2mnmutebgrjafkyn6xuwvu7` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKai74mpk99i7b5wc1rn15l994o` FOREIGN KEY (`amenaza_instanciada_id`) REFERENCES `amenaza_instanciada` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8;


-- ar_marisma.control_auditoria definition

CREATE TABLE `control_auditoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `cobertura` float NOT NULL,
  `deleted` bit(1) NOT NULL,
  `exito` float DEFAULT NULL,
  `control_instanciado_id` bigint(20) NOT NULL,
  `agrupacion_checklist_id` bigint(20) DEFAULT NULL,
  `objetivo_auditoria_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK7ri4g4ihssxr11y9r2a5ssdfk` (`control_instanciado_id`),
  KEY `FK34m9ch1nq0nktifw5yx584y3h` (`agrupacion_checklist_id`),
  KEY `FKtn0impuu7hsu9dd11b0gyytbt` (`objetivo_auditoria_id`),
  CONSTRAINT `FK34m9ch1nq0nktifw5yx584y3h` FOREIGN KEY (`agrupacion_checklist_id`) REFERENCES `agrupacion_checklist` (`id`),
  CONSTRAINT `FK7ri4g4ihssxr11y9r2a5ssdfk` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKtn0impuu7hsu9dd11b0gyytbt` FOREIGN KEY (`objetivo_auditoria_id`) REFERENCES `objetivo_auditoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;


-- ar_marisma.control_caracteristica_control_instanciada definition

CREATE TABLE `control_caracteristica_control_instanciada` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `esquema_instanciado_id` bigint(20) NOT NULL,
  `padre` bigint(20) DEFAULT NULL,
  `control_instanciado_id` bigint(20) NOT NULL,
  `caracteristica_control_instanciada_id` bigint(20) NOT NULL,
  `heredado` varchar(255) DEFAULT NULL,
  `origen` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK1c2br2741r98eo0otsjswgptl` (`esquema_instanciado_id`),
  KEY `FKghojx0qc2eygdcih3b1lkv0x7` (`control_instanciado_id`),
  KEY `FK3wg5rgxsit5m9phq3dyj4yyu5` (`caracteristica_control_instanciada_id`),
  CONSTRAINT `FK1c2br2741r98eo0otsjswgptl` FOREIGN KEY (`esquema_instanciado_id`) REFERENCES `esquema_instanciado` (`id`),
  CONSTRAINT `FK3wg5rgxsit5m9phq3dyj4yyu5` FOREIGN KEY (`caracteristica_control_instanciada_id`) REFERENCES `caracteristica_control_instanciada` (`id`),
  CONSTRAINT `FKghojx0qc2eygdcih3b1lkv0x7` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.control_instanciado_incidentes definition

CREATE TABLE `control_instanciado_incidentes` (
  `control_instanciado_id` bigint(20) NOT NULL,
  `incidente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`control_instanciado_id`,`incidente_id`),
  KEY `FKapf3is1gkjh6fg4xkbdrobaw9` (`incidente_id`),
  CONSTRAINT `FKa5v2k6a75cvtdygk17c04luhj` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKapf3is1gkjh6fg4xkbdrobaw9` FOREIGN KEY (`incidente_id`) REFERENCES `incidente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.plan_tratamiento definition

CREATE TABLE `plan_tratamiento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `plan` text,
  `analisis_riesgo_id` bigint(20) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `control_auditoria_id` bigint(20) DEFAULT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `riesgo_inherentearfin` float DEFAULT NULL,
  `riesgo_inherente_ini` float DEFAULT NULL,
  `orden` int(11) DEFAULT NULL,
  `fecha_fin_prev` datetime DEFAULT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `riesgo_inherentearini` float DEFAULT NULL,
  `valor_riesgo` float DEFAULT NULL,
  `agrupacion_checklist_id` bigint(20) DEFAULT NULL,
  `fecha_ejec` datetime DEFAULT NULL,
  `riesgo_inherente_fin` float DEFAULT NULL,
  `resultado` text,
  `nombre` varchar(255) NOT NULL,
  `fecha_prev` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKrjx7o5er6y8yfhvn3qgs5ogso` (`analisis_riesgo_id`),
  KEY `FK2662vniuyirnaxm49qba1ctvh` (`control_auditoria_id`),
  KEY `FKrga4kuth8r3542cn9kh3kvpqq` (`subproyecto_id`),
  KEY `FKppvl1bhly6988j1ua6yy0omie` (`agrupacion_checklist_id`),
  CONSTRAINT `FK2662vniuyirnaxm49qba1ctvh` FOREIGN KEY (`control_auditoria_id`) REFERENCES `control_auditoria` (`id`),
  CONSTRAINT `FKppvl1bhly6988j1ua6yy0omie` FOREIGN KEY (`agrupacion_checklist_id`) REFERENCES `agrupacion_checklist` (`id`),
  CONSTRAINT `FKrga4kuth8r3542cn9kh3kvpqq` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKrjx7o5er6y8yfhvn3qgs5ogso` FOREIGN KEY (`analisis_riesgo_id`) REFERENCES `analisis_riesgo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.respuesta definition

CREATE TABLE `respuesta` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `checklist_instanciado_id` bigint(20) DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `nivel_cobertura` varchar(255) DEFAULT NULL,
  `observaciones` varchar(255) DEFAULT NULL,
  `nota_final` float DEFAULT NULL,
  `comentario` varchar(4000) DEFAULT NULL,
  `agrupacion_checklist_id` bigint(20) DEFAULT NULL,
  `aplica` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK1gxvsik7aa2l2eiejxc46fwd9` (`checklist_instanciado_id`),
  KEY `FK1n0oyf7p9nu8ap25w3hc6p7n2` (`agrupacion_checklist_id`),
  CONSTRAINT `FK1gxvsik7aa2l2eiejxc46fwd9` FOREIGN KEY (`checklist_instanciado_id`) REFERENCES `checklist_instanciado` (`id`),
  CONSTRAINT `FK1n0oyf7p9nu8ap25w3hc6p7n2` FOREIGN KEY (`agrupacion_checklist_id`) REFERENCES `agrupacion_checklist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=143 DEFAULT CHARSET=utf8;


-- ar_marisma.revision_control definition

CREATE TABLE `revision_control` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `control_auditoria_id` bigint(20) NOT NULL,
  `cobertura_actual` float DEFAULT NULL,
  `fecha_revision` datetime DEFAULT NULL,
  `justificacion` varchar(4000) DEFAULT NULL,
  `subproyecto_id` bigint(20) NOT NULL,
  `aplica_anterior` varchar(255) DEFAULT NULL,
  `cobertura_anterior` float DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `aplica_actual` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKtna8fmnixawjyhgkhn10drw6f` (`control_auditoria_id`),
  KEY `FKr7pfhnde8xw54dr52rrr0wrr5` (`subproyecto_id`),
  KEY `FKg7jicb3psok6td0xqyu3ar762` (`user_id`),
  CONSTRAINT `FKg7jicb3psok6td0xqyu3ar762` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKr7pfhnde8xw54dr52rrr0wrr5` FOREIGN KEY (`subproyecto_id`) REFERENCES `subproyecto` (`id`),
  CONSTRAINT `FKtna8fmnixawjyhgkhn10drw6f` FOREIGN KEY (`control_auditoria_id`) REFERENCES `control_auditoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_control_auditoria definition

CREATE TABLE `archivo_control_auditoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `vinculado` bit(1) NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `control_auditoria_id` bigint(20) DEFAULT NULL,
  `file_name` varchar(255) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKjgyvs6dlm6wxmb2ue0o30hdi9` (`control_auditoria_id`),
  KEY `FKtpbg2el0ecx64jnhr7teppyd7` (`user_id`),
  CONSTRAINT `FKjgyvs6dlm6wxmb2ue0o30hdi9` FOREIGN KEY (`control_auditoria_id`) REFERENCES `control_auditoria` (`id`),
  CONSTRAINT `FKtpbg2el0ecx64jnhr7teppyd7` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_control_auditoria_control_instanciado definition

CREATE TABLE `archivo_control_auditoria_control_instanciado` (
  `archivo_control_auditoria_controles_vinculados_id` bigint(20) NOT NULL,
  `control_instanciado_id` bigint(20) DEFAULT NULL,
  KEY `FK3qjkinfjqcqhd14quf37calhr` (`control_instanciado_id`),
  KEY `FKh021qlpt28ngoahr2clio693n` (`archivo_control_auditoria_controles_vinculados_id`),
  CONSTRAINT `FK3qjkinfjqcqhd14quf37calhr` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKh021qlpt28ngoahr2clio693n` FOREIGN KEY (`archivo_control_auditoria_controles_vinculados_id`) REFERENCES `archivo_control_auditoria` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_revision_control definition

CREATE TABLE `archivo_revision_control` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `vinculado` bit(1) NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `deleted` bit(1) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `revision_control_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKdtn6r9o5tv9a1sdq6yidigbt1` (`user_id`),
  KEY `FKdi5xdjn2xqbe7mi2mx2xrua0k` (`revision_control_id`),
  CONSTRAINT `FKdi5xdjn2xqbe7mi2mx2xrua0k` FOREIGN KEY (`revision_control_id`) REFERENCES `revision_control` (`id`),
  CONSTRAINT `FKdtn6r9o5tv9a1sdq6yidigbt1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ar_marisma.archivo_revision_control_control_instanciado definition

CREATE TABLE `archivo_revision_control_control_instanciado` (
  `archivo_revision_control_controles_vinculados_id` bigint(20) NOT NULL,
  `control_instanciado_id` bigint(20) DEFAULT NULL,
  KEY `FK6clljvsjb9qyc61lqfyi9i3qn` (`control_instanciado_id`),
  KEY `FKgxdpiq0aqubvcnduou2jfc2ow` (`archivo_revision_control_controles_vinculados_id`),
  CONSTRAINT `FK6clljvsjb9qyc61lqfyi9i3qn` FOREIGN KEY (`control_instanciado_id`) REFERENCES `control_instanciado` (`id`),
  CONSTRAINT `FKgxdpiq0aqubvcnduou2jfc2ow` FOREIGN KEY (`archivo_revision_control_controles_vinculados_id`) REFERENCES `archivo_revision_control` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;