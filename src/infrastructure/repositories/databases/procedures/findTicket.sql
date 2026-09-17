DROP PROCEDURE IF EXISTS findTicket;

DELIMITER $$
CREATE PROCEDURE findTicket(
	IN id_ticket_consultar INT,
	IN nombre_usuario VARCHAR(100)
)
BEGIN
	
	DECLARE id_ticket_tecnicos VARCHAR(20);
	DECLARE nombre_ticket_tecnicos TEXT;
	DECLARE v_id INT;
	DECLARE v_id_t INT;
    DECLARE v_content TEXT;
	DECLARE v_fin INT DEFAULT 0;
	
	/* Cursor de la consulta  */
	DECLARE cursor_tecnicos CURSOR FOR
		SELECT glpi_itilfollowups.items_id, glpi_itilfollowups.users_id,
		glpi_itilfollowups.content
		FROM glpi_itilfollowups
		INNER JOIN glpi_tickets ON glpi_itilfollowups.items_id = glpi_tickets.id
		WHERE glpi_itilfollowups.items_id = 2885 AND glpi_itilfollowups.users_id IN(
			SELECT glpi_users.id 
    		FROM glpi_users 
    		INNER JOIN glpi_tickets_users on glpi_users.id = glpi_tickets_users.users_id AND glpi_tickets_users.`type` = 2
    		WHERE glpi_tickets_users.tickets_id = 2885
		) ORDER BY glpi_itilfollowups.`date`;
	
	/* Handler para cuando el cursor se quede sin registros */
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_fin = 1;
	
	DROP TABLE IF EXISTS tmp_seguimientos;
	
	CREATE TEMPORARY TABLE tmp_seguimientos (
		ticket_id INT,
		usuario_id INT,
		comentario TEXT
	);
	
	/* Abrir cursor */
	OPEN cursor_tecnicos;
	
	/* Ciclo */
	bucle: WHILE v_fin = 0 DO
	
		FETCH cursor_tecnicos INTO v_id_t, v_id, v_content;
		
		IF v_fin THEN
            LEAVE bucle;
        END IF;
		
		INSERT INTO tmp_seguimientos(
			ticket_id,
			usuario_id,
			comentario
		)VALUES(
			v_id_t, v_id, v_content
		);
		
	END WHILE bucle;
	
	CLOSE cursor_tecnicos;

	SELECT concat(comentario) FROM tmp_seguimientos GROUP BY ticket_id;
	/*
	SELECT GROUP_CONCAT(glpi_users.id) INTO id_ticket_tecnicos
    FROM glpi_users 
    INNER JOIN glpi_tickets_users on glpi_users.id = glpi_tickets_users.users_id AND glpi_tickets_users.`type` = 2
    WHERE glpi_tickets_users.tickets_id = id_ticket_consultar;
	
	SELECT GROUP_CONCAT(glpi_users.firstname, " ", glpi_users.realname) INTO nombre_ticket_tecnicos
	FROM glpi_users 
    INNER JOIN glpi_tickets_users on glpi_users.id = glpi_tickets_users.users_id AND glpi_tickets_users.`type` = 2
    WHERE glpi_tickets_users.tickets_id = id_ticket_consultar;
	
	SELECT glpi_tickets.id,
	glpi_tickets.name AS `titulo`, 
	glpi_tickets.urgency AS `urgencia`,		
    glpi_tickets.impact AS `impacto`,
	glpi_tickets.priority AS `prioridad`, 
    glpi_entities.name AS `entidad`,
    glpi_tickets.status AS `estado`,
	CONCAT(glpi_users.firstname, " ", glpi_users.realname) AS `autor` ,
    glpi_itilcategories.name AS `ctegoria`,
    id_ticket_tecnicos AS `id_tecnicos`,
    nombre_ticket_tecnicos AS `tecnicos`
    FROM glpi_tickets
    INNER JOIN glpi_entities ON glpi_tickets.entities_id = glpi_entities.id
    INNER JOIN glpi_users ON glpi_tickets.users_id_recipient = glpi_users.id
    INNER JOIN glpi_itilcategories ON glpi_tickets.itilcategories_id  = glpi_itilcategories.id 
    WHERE glpi_tickets.id = id_ticket_consultar
    ORDER BY glpi_tickets.id DESC;	*/
END $$
DELIMITER ;

CALL findTicket(3333, 'LUIS');


SELECT GROUP_CONCAT(comentario, '¥'), GROUP_CONCAT(usuario_id, '¥')  FROM tmp_seguimientos ;