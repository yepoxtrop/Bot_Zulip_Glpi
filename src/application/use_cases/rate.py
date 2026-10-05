from .command import Command;

class Rate(Command):
    
    def __init__(self, id:int,  initial_message:str):
        super.__init__(); 
        self._initial_message = initial_message;
        self.inputs = initial_message.lower();
        
    