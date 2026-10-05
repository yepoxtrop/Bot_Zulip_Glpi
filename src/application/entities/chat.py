import datetime;

class Chat:
    
    
    def __init__(self, id:int,  serial:str, user, date_satart:datetime.datetime = None):
        Chat.id += 1;
        
        self.id = id; 
        self.serial = serial;
        self.status = True;
        self.date_start = date_satart;
        self.date_end = None;
        self.messages = None;
        self.process = None;
        self.users = [user];
        self.steps = None;