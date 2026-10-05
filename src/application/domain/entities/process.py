class Process:
    
    
    def __init__(self, id:int,  name:str, steps:list = []):
        
        self.id = id;
        self.name = name;
        self.steps = steps;