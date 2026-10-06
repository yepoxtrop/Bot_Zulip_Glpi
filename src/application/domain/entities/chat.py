import datetime;
from .message import Message;
from .library_logs import LibraryLog;
from .ticket import Ticket;
from ..models.chats import Chats;
from .user import User;

class Chat:
    def __init__(
        self,
        id:int,
        serial:str,
        user:User,
        date_satart:datetime.datetime,
        logs_chat:LibraryLog
    ):
        self.__id = id; 
        self._serial:str = serial;
        self._status:bool = True;
        self._date_start = date_satart;
        self._date_end:datetime.datetime|None = None;
        self._messages:list[Message]|None = None;
        self._tickets:list[Ticket] = [];
        self._logs_chat = logs_chat;
        self._process:list[Chats]|None = None;
        self._steps:list[Chats]|None = None;
        self._users:list[User] = [user];
        
        self.validate();
        
    @property
    def id(self) -> int:
        return self.__id;
    
    @property
    def serial(self) -> str:
        return self._serial;
    
    @property
    def status(self) -> bool:
        return self._status;
    
    @property
    def date_start(self) -> datetime.datetime:
        return self._date_start;
    
    @property
    def date_end(self) -> datetime.datetime|None:
        return self._date_end;
    
    @property
    def messages(self) -> list[Message]|None:
        return self._messages;

    @property
    def tickets(self) -> list[Ticket]:
        return self._tickets;

    @property
    def logs_chat(self) -> LibraryLog:
        return self._logs_chat;
    
    @property
    def process(self) -> list[Chats]|None:
        return self._process;
    
    @property
    def steps(self) -> list[Chats]|None:
        return self._steps;
    
    @property
    def users(self) -> list[User]:
        return self._users;
    
    def validate_serial(self):
        if not self._serial or not self._serial.strip():
            raise ValueError("Serial cannot be empty.");
        return True
    
    def validate_status(self):
        if not isinstance(self._status, bool):
            raise ValueError("Status must be a boolean.");
        return True;
    
    def validate_date_start(self):
        if not self._date_start:
            raise ValueError("Date start cannot be empty.");
        return True;
    
    def validate_users(self):
        if not self._users or not isinstance(self._users, list) or len(self._users) == 0:
            raise ValueError("Users cannot be empty.");
        return True;

    def validate_logs_chat(self):
        if not isinstance(self._logs_chat, LibraryLog):
            raise ValueError("Chat logs must be an instance of LibraryLog.");
        return True;

    def validate_tickets(self):
        if not isinstance(self._tickets, list):
            raise ValueError("Tickets must be a list.");
        if any(not isinstance(ticket, Ticket) for ticket in self._tickets):
            raise ValueError("Tickets must contain Ticket instances.");
        return True;
    
    def update_date_end(self, date_end:datetime.datetime):
        if not date_end:
            raise ValueError("Date end cannot be empty.");
        elif date_end < self._date_start:
            raise ValueError("Date end cannot be earlier than date start.");
        else:
            self._date_end = date_end;
    
    def add_message(self, message:Message):
        if not message:
            raise ValueError("Message cannot be empty.");
        elif not isinstance(message, Message):
            raise ValueError("Message must be an instance of Message.");
        else:
            if self._messages is None:
                self._messages = [];
            self._messages.append(message);   
            
    def add_process(self, process:Chats):
        if not process:
            raise ValueError("Process cannot be empty.");
        elif not isinstance(process, Chats):
            raise ValueError("Process must be an instance of Chats.");
        else:
            if self._process is None:
                self._process = [];
            self._process.append(process);
            
    def add_step(self, step:Chats):
        if not step:
            raise ValueError("Process cannot be empty.");
        elif not isinstance(step, Chats):
            raise ValueError("Process must be an instance of Chats.");
        else:
            if self._steps is None:
                self._steps = [];
            self._steps.append(step);
            
    def add_users(self, user:User):
        if not user:
            raise ValueError("Process cannot be empty.");
        elif not isinstance(user, User):
            raise ValueError("Process must be an instance of Chats.");
        else:
            self._users.append(user);
    
    def validate(self) -> bool:
        return (
            self.validate_serial() and 
            self.validate_status() and 
            self.validate_date_start() and 
            self.validate_users() and
            self.validate_logs_chat() and
            self.validate_tickets()
        );