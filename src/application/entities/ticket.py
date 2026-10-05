import datetime;

class Ticket:
    
    
    def __init__(self, id:int,  
                 entities_id:int, 
                 title_ticket:str, 
                 request_types:int, 
                 content:str, 
                 urgency:int, 
                 priority:int, 
                 impact:int, 
                 categories_id:int, 
                 type:int, 
                 slas_id_ttr:int, 
                 slas_id_tto:int, 
                 time_to_resolve:datetime.datetime, 
                 time_to_own:datetime.datetime, 
                 name_user:str,
                 date_ticket:datetime.datetime = datetime.datetime.now()):
        
        self.id = id;
        self.entities_id = entities_id;
        self.title_ticket = title_ticket;
        self.date_ticket = date_ticket;
        self.request_types = request_types;
        self.content = content;
        self.urgency = urgency;
        self.impact = impact;
        self.priority = priority;
        self.categories_id = categories_id;
        self.type = type;
        self.slas_id_ttr = slas_id_ttr;
        self.slas_id_tto = slas_id_tto;
        self.time_to_resolve = time_to_resolve;
        self.time_to_own = time_to_own;
        self.name_user = name_user;