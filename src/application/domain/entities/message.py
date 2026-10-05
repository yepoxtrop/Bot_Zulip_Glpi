import datetime;

class Message:
    
    
    def __init__(self, id:int,  content:str, author:str, date:datetime.datetime = datetime.datetime.now()):
        
        self.id = id; 
        self.content = content;
        self.author = author;
        self.date = date;