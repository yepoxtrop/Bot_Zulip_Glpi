import sys
import os

# Importacion para test
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from database.connector import connector_db;
from database.query_error import QueryError; # Clase de error personalizado

# Funciones para consulta e insercion en la base de datos del glpi
def find_ticket(id_ticket:int)->str:
    try:
        if not connector_db.is_connected():
            raise QueryError("Conexion no establecida", 500);
        

        cursor = connector_db.cursor();
        cursor.execute(f"""
            SELECT  glpi_tickets.id,
    		glpi_tickets.name AS `titulo`, 
	    	glpi_tickets.urgency AS `urgencia`,		
    		glpi_tickets.impact AS `impacto`,
	    	glpi_tickets.priority AS `prioridad`, 
    		glpi_entities.name AS `entidad`,
	    	CONCAT(glpi_users.firstname, " ", glpi_users.realname) AS `autor`,
    		glpi_itilcategories.name AS `categoria`,
    		(SELECT GROUP_CONCAT(glpi_users.id)
    		 FROM glpi_users 
    		 INNER JOIN glpi_tickets_users on glpi_users.id = glpi_tickets_users.users_id AND glpi_tickets_users.`type` = 2
    		 WHERE glpi_tickets_users.tickets_id = '{id_ticket}' ) AS `id_tecnicos`,
    		(SELECT GROUP_CONCAT(glpi_users.firstname, " ", glpi_users.realname)
	     	 FROM glpi_users 
     		 INNER JOIN glpi_tickets_users on glpi_users.id = glpi_tickets_users.users_id AND glpi_tickets_users.`type` = 2
    		 WHERE glpi_tickets_users.tickets_id = '{id_ticket}' ) AS `tecnicos`
            FROM glpi_tickets
            INNER JOIN glpi_entities ON glpi_tickets.entities_id = glpi_entities.id
            INNER JOIN glpi_users ON glpi_tickets.users_id_recipient = glpi_users.id
            INNER JOIN glpi_itilcategories ON glpi_tickets.itilcategories_id  = glpi_itilcategories.id 
            WHERE glpi_tickets.id = '{id_ticket}'
            ORDER BY glpi_tickets.id DESC;)
        """);
        print(cursor.fetchall());
        cursor.close();
    except QueryError as e:
        return e.message;

numero = int(input("Ingrese el id:"))
find_ticket(numero);
