from ....application.domain.ports import IOwnDatabase;
from ....application.domain.entities import User, Message;
from mysql.connector import MySQLConnection;

class MYSQL_ADAPTER(IOwnDatabase):
    def __init__(self, database_connector:MySQLConnection):
        self._database_connector = database_connector;
        
    def _try_connection(self):
        try:
            self._database_connector.ping(reconnect=True, attempts=3, delay=5);
        except Exception as e:
            raise Exception(f"Failed to connect to GLPI database: {e}");

    def insert_message(self, message: Message):
        self._try_connection();
        pass;

    def query_message(self):
        self._try_connection();
        pass;

    def insert_user(self, user:User):
        self._try_connection();
        pass;

    def abstractmethod(self):
        self._try_connection();
        pass;