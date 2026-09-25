from .command import Command;
from ...models.messages import Welcome_Messages;
from ...settings import GLPI_KEYWORDS;

class Welcome(Command):
    
    def __init__(self, initial_message:str):
        super().__init__(); 
        self._initial_message = initial_message;
        self.inputs = initial_message.lower();
        
    def send_message(self)->str:
        message_to_send = "";
        
        if (len(self.workflow) == 0) :
            message_to_send += Welcome_Messages.WELCOME_GENERAL_MESSAGE;
            self.step = "INTRODUCTION";
            self.workflow = "INTRODUCTION";
        else:
            self.step = "OPEN_CHAT";
            self.workflow = "OPEN_CHAT";
            
        for word in GLPI_KEYWORDS:
            if word in self.inputs[-1]:
                message_to_send += Welcome_Messages.WELCOME_HELP_GENERAL_MESSAGE.value;
                
        return message_to_send;