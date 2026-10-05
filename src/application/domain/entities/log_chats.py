import datetime;

class LogChat:
    
    
    def __init__(self, id:int,  content:str, object:str, date:datetime.datetime = datetime.datetime.now()):
        
        self.id = id; 
        self.content = content;
        self.date = date;
        self.object = object;