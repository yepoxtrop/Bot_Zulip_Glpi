import datetime;
from .log import Log;
from ..models.chats import Chats;
class LogChat(Log):
    
    def __init__(self, id:int,  content:str, object:str, date:datetime.datetime, action:Chats):
        super().__init__(id, content, date);
        self._action = action;
        
    @property
    def action(self) -> Chats:
        return self._action;
    
    def validate_action(self) -> Chats:
        if not self._action:
            raise ValueError("Action cannot be empty.");
        return True;
    
    def validate(self) -> bool:
        return (
            super().validate() and 
            self.validate_action()
        )