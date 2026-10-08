from abc import ABC, abstractmethod;
from ...entities import User, Message;



class IOwnDatabase(ABC):
    
    @abstractmethod
    def insert_message(self, message: Message):
        pass
    
    @abstractmethod
    def query_message(self):
        pass
    
    @abstractmethod
    def insert_user(self, user:User):
        pass
    
    @abstractmethod
    def query_user(self):
        pass