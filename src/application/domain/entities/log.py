import datetime;

class Log:
    
    
    def __init__(self, id:int,  content:str, date:datetime.datetime = datetime.datetime.now()):
        
        self.id = id; 
        self.content = content;
        self.date = date;