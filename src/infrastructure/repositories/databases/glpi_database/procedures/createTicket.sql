/*
 * ==============================================
 * 	    	MODIFICACIONES PARA LA BASE
 * ==============================================
 * 1. Crear el request_type Bot Zulip
 * 1.1. Enlazar un ticket con una entidad
 * 1.2. Enlazar un ticket con un usuario recipiente
 * 1.3. Enlazar el ticket con una categoria 
 * 
*/


/*
 * ==============================================
 * 	    CREACION DE CASOS DIRECTO POR BASE
 * ==============================================
 * 1. Crear ticket
 * 1.1. Enlazar un ticket con una entidad 'Sistemas'
 * 1.2. Enlazar un ticket con un usuario recipiente
 * 1.3. Enlazar el ticket con una categoria 
 * 1.4. Enlazar el ticket con el request_type 'Bot Zulip'
 * 
 * 2. Crear registro de usuario asignado
 * 
 * 3. Crear logs necesario para el ticket básico
*/


DROP PROCEDURE IF EXISTS CreateTicket;

DELIMITER $$
CREATE PROCEDURE CreateTicket(
	 IN entities_id INT
	,IN title_ticket VARCHAR(100)
	,IN date_ticket TIMESTAMP
	,IN request_types INT
	,IN content TEXT
	,IN urgency INT
	,IN priority INT
	,IN impact INT
	,IN categories_id INT
	,IN `type` INT
	,IN slas_id_ttr	INT
	,IN slas_id_tto INT
	,IN time_to_resolve TIMESTAMP
	,IN time_to_own	TIMESTAMP
	,IN name_user VARCHAR(100)	
)
BEGIN
	
	/* Local variables */
	DECLARE id_user INT;
	DECLARE id_ticket INT;
	DECLARE complete_user_name VARCHAR(200); -- If you use ldaps domain
	
	/* Exceptions and rollback */
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
		BEGIN
			ROLLBACK;
			SELECT FALSE AS Resultado;
		END;
	
	/* Query to find user id */
	SELECT id, (CONCAT(realname, ' ' ,firstname))
	INTO id_user, complete_user_name
	FROM glpi_users
	WHERE name = name_user -- If works with ldaps domain 
	/* WHERE CONCAT(firstname, ' ' ,realname) = name_user; -- If works with complete user name */
	ORDER BY id DESC  -- 
	LIMIT 1;  -- 
	
	/* Condition if user doesn't exists */
	IF id_user IS NULL THEN 
		/* User does not have acces to glpi or not exists */
		SELECT False as `Resultado`;
	ELSE
		/* Transaction to insert */
		START TRANSACTION;
		
		/* Create Ticket */
		INSERT INTO glpi_tickets (
	 		 entities_id 					-- defautl 'sistemas', user sets it
			,name							-- title ticket, user sets it
			,date							-- date creation, user sets it
			,date_mod						-- date creation, user sets it
			,users_id_lastupdater			-- user id customer, calc the sp 
			,users_id_recipient				-- user id customer, calc the sp
			,requesttypes_id				-- default 'Bot Zulip' or respective request type
			,content						-- description ticket, user sets it
			,urgency						-- urgency, user sets it
			,impact							-- impact, user sets it
			,priority						-- priority, user sets it
			,itilcategories_id				-- user sets it
			,type							-- user sets it (1 = Incidencia | 2 = Requerimientos)
			,slas_id_ttr					-- bot calculates it
			,slas_id_tto					-- bot calculates it
			,time_to_resolve				-- bot calculates it
			,time_to_own					-- bot calculates it
			,date_creation					-- date creation, user sets it
		) values(
	 		 entities_id
			,title_ticket
			,date_ticket
			,date_ticket
			,id_user
			,id_user
			,request_types
			,content
			,urgency
			,impact
			,priority
			,categories_id
			,`type`
			,slas_id_ttr
			,slas_id_tto
			,time_to_resolve
			,time_to_own
			,date_ticket
		);
		
		/* Fin the ticket id */
		SELECT LAST_INSERT_ID() INTO id_ticket;
		
		/* Relatiionship between user and ticket like a customer */
		INSERT INTO glpi_tickets_users (
			tickets_id
			,users_id
			/* ,type,		-- 2 o 1 (2 = technician | 1 = customer, default )*/
		) VALUES (
			 id_ticket
			,id_user
		);
		
		/* Log assign customer */
		INSERT INTO glpi_logs (
	 		 itemtype			-- Object type (Ticket is default)
			,items_id			-- Ticket id
			,itemtype_link		-- User y 0 (User = customer | 0 = technician)
			,linked_action		-- 15 y 20 (15 = customer | 20 = technician)
			,user_name			-- user name (id user)
			,date_mod			-- date modification
			,id_search_option  	-- 4 (default value)
			,new_value			-- name user
		) values (
			'Ticket'			
			,id_ticket
			,'User'
			,15
			,CONCAT(complete_user_name, ' ', '(', id_user, ')')  -- If works with ldaps domain 
			 /* ,CONCAT(firstname, ' ' ,realname), ' ', '(', id_user, ')' )  -- If works with complete name */ 
			,date_ticket
			,4
			,name_user
		);
		
		
		/* Assign Technician */
		/*INSERT INTO glpi_tickets_users (
	 		 tickets_id
			,users_id
		) VALUES (
	 		 4116
			,333
		);*/
		
		/* Log assign customer */
		/*INSERT INTO glpi_logs (
	 		itemtype			-- Tipo de objeto (Ticket, Este es el valor quemado)
			,items_id			-- numero ticket
			,itemtype_link		-- User y 0 (User = customer | 0 = technician)
			,linked_action		-- 15 y 20 (15 = customer | 20 = technician)
			,user_name			-- nombre de la persona (id_persona)
			,date_mod			-- fecha modificaion
			,id_search_option  	-- 0 (Valor quemado)
		) values (	
			'Ticket'			-- Id del ticket
			,id_ticket
			,'0'
			,20
			,CONCAT(name_user, ' ', '(', id_ticket, ')') 
			,date_ticket
			,0
		)*/
		
		COMMIT;
		ROLLBACK;
	END IF;
	
END $$
DELIMITER ;

/* TRY SP */
/* CALL CreateTicket(
 		 2
		,'Caso de prueba con sp v3'
		,'2026-09-24 12:02:57'
		,7
		,'Lorem bro'
		,1
		,1
		,1
		,1
		,1
		,100
		,100
		,'2026-09-24 12:02:57'
		,'2026-09-24 12:02:57'
		,'myriam.salinas'
   ); */