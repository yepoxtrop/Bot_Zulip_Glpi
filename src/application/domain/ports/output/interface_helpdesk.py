from abc import ABC, abstractmethod;
from ...entities import Ticket, User;

class IHelpDesk(ABC):
    
    @abstractmethod
    def create_connection(self)-> None:
        pass
    
    @abstractmethod
    def create_ticket(self, ticket:Ticket)-> int:
        pass
        
    @abstractmethod
    def get_ticket(self, ticket_id:int, user:User):
        pass;

    @abstractmethod
    def update_ticket(self, ticket_id:int, ticket_data:dict):
        pass;
    
    @abstractmethod
    def close_ticket(self, ticket_id:int, calification:int, comment:list[str]):
        pass;