from .....application.domain.ports import IHelpDesk;
from mysql.connector import MySQLConnection;
from .....application.domain.entities import User;
from .....application.domain.entities import Ticket;

class GLPI_Adapter(IHelpDesk):
    
    
    def __init__(self, database_connector:MySQLConnection):
        self._database_connector = database_connector;
        
    def _try_connection(self):
        try:
            self._database_connector.ping(reconnect=True, attempts=3, delay=5);
        except Exception as e:
            raise Exception(f"Failed to connect to GLPI database: {e}");

    def create_ticket(self, ticket:Ticket):
        self._try_connection();
        
        pass;

    def update_ticket(self, ticket_id:int, ticket_data:dict):
        self._try_connection();
        pass;

    def get_ticket(self, ticket_id:int, user:User):
        self._try_connection();
        pass;

    def delete_ticket(self, ticket_id:int):
        self._try_connection();
        pass;