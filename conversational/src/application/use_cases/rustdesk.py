from .command import Command;

class Rustdesk(Command):
    
    def __init__(self, initial_message:str):
        super.__init__(); 
        self._initial_message = initial_message;
        self.inputs = initial_message.lower();
        
    