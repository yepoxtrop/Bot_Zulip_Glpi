/* ===================================================================
 * PROCEDURE: 	FindTicket
 * AUTHOR:		Luis Sarmiento
 * DESCRIPTION:	Get info about one ticket
 * 
 * INPUTS:		-id_ticket_to_find 	-> Id to find
 * 				-name_user			-> Possible user
 * 
 * OUTPUTS:		-Case_00 -> Code 0 mean error, don't acces to ticket
 * 				-Case_01 -> Query.
 * =================================================================== */

DROP PROCEDURE IF EXISTS FindTicket;

DELIMITER $$
CREATE PROCEDURE FindTicket(
	IN id_ticket_to_find INT,
	IN name_user VARCHAR(100)
)
BEGIN
	
	/* Variables */
	DECLARE id_ticket_tech VARCHAR(20);
	DECLARE name_ticket_tech TEXT;
	DECLARE recipient_user_id INT;
	
	/* Check variables */
	DECLARE check_ticket INT;
	DECLARE check_followups TEXT;
	DECLARE check_followups_techs TEXT;
	
	/* Query to find user recipient id into the database*/
	SELECT glpi_tickets.id INTO check_ticket
	/* FROM glpi_users WHERE name = name_user  -- If works with ldaps domain */
	FROM glpi_users
	INNER JOIN glpi_tickets
	ON glpi_users.id = glpi_tickets.users_id_recipient
	WHERE (CONCAT(glpi_users.firstname, ' ' ,glpi_users.realname) = name_user
	OR glpi_tickets.content LIKE CONCAT('%', name_user, '%'))
	AND glpi_tickets.id = id_ticket_to_find;  
	
	
	IF check_ticket IS NULL THEN
		/* User does not have acces to ticket */
		SELECT False as `Resultado`; 
	ELSE
	
		/* Find id user */
		SELECT id INTO recipient_user_id
		FROM glpi_users
		/* WHERE WHERE name = name_user -- If works with ldaps domain */
		WHERE CONCAT(firstname, ' ' ,realname) = name_user; -- If works with complete name
		
		/* Create temporary table with query */
		DROP TABLE IF EXISTS tmp_followups;
		CREATE TEMPORARY TABLE tmp_followups AS
		SELECT id_ticket_to_find as `ticket`
			,recipient_user_id as `id_recipient`
			,name_user as `name_recipient`
			,glpi_itilfollowups.users_id as `id_followup`
			,CONCAT(glpi_users.firstname, ' ', glpi_users.realname) as `tech_name` 
			,glpi_itilfollowups.content as `followup`
		FROM glpi_itilfollowups
		INNER JOIN glpi_tickets ON glpi_itilfollowups.items_id = glpi_tickets.id
		INNER JOIN glpi_users ON glpi_users.id = glpi_itilfollowups.users_id 
		WHERE glpi_itilfollowups.items_id = id_ticket_to_find AND glpi_itilfollowups.users_id IN(
			/* Find id techs from the ticket id*/
			SELECT glpi_users.id 
    		FROM glpi_users 
	    	INNER JOIN glpi_tickets_users on glpi_users.id = glpi_tickets_users.users_id AND glpi_tickets_users.`type` = 2
    		WHERE glpi_tickets_users.tickets_id = id_ticket_to_find
		) ORDER BY glpi_itilfollowups.`date`;
	
		SELECT IFNULL(GROUP_CONCAT(followup SEPARATOR '¥'), False) AS 'FOLLOWUPS' , 
		IFNULL(GROUP_CONCAT(tech_name SEPARATOR '¥'), False) AS 'TECH' INTO check_followups, check_followups_techs
		FROM tmp_followups;
		
		SELECT glpi_tickets.id
    		,glpi_tickets.name AS `titulo`
	    	,glpi_tickets.urgency AS `urgencia`		
    		,glpi_tickets.impact AS `impacto`
	    	,glpi_tickets.priority AS `prioridad` 
    		,glpi_entities.name AS `entidad`
    		,glpi_tickets.status AS `estado`
	    	,CONCAT(glpi_users.firstname, " ", glpi_users.realname) AS `autor`
    		,glpi_itilcategories.name AS `categoria`
    		,(SELECT GROUP_CONCAT(glpi_users.id)
    		FROM glpi_users 
    		INNER JOIN glpi_tickets_users on glpi_users.id = glpi_tickets_users.users_id AND glpi_tickets_users.`type` = 2
    		WHERE glpi_tickets_users.tickets_id = check_ticket ) AS `id_tecnicos`
    		,(SELECT GROUP_CONCAT(glpi_users.firstname, " ", glpi_users.realname)
	     	FROM glpi_users 
     		INNER JOIN glpi_tickets_users on glpi_users.id = glpi_tickets_users.users_id AND glpi_tickets_users.`type` = 2
    		WHERE glpi_tickets_users.tickets_id = check_ticket ) AS `tecnicos`
    		,check_followups
    		,check_followups_techs
            FROM glpi_tickets
            INNER JOIN glpi_entities ON glpi_tickets.entities_id = glpi_entities.id
            INNER JOIN glpi_users ON glpi_tickets.users_id_recipient = glpi_users.id
            INNER JOIN glpi_itilcategories ON glpi_tickets.itilcategories_id  = glpi_itilcategories.id 
            WHERE glpi_tickets.id = check_ticket
            ORDER BY glpi_tickets.id DESC;
		
		-- SELECT 'TIENE ACCESO AL CASO';	
	END IF;

END $$
DELIMITER ;

/* TRY SP */
-- CALL findTicket(2614, 'Maria Daniela Zapata Londoño');