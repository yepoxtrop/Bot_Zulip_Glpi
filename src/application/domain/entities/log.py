import datetime;

class Log:
    
    def __init__(self, id:int,  content:str, date:datetime.datetime):
        self.__id = id; 
        self._content = content;
        self._date = date;
        
        self.validate();
        
    # Getters 
    # Only the id is private, the rest of the attributes are protected
    @property
    def id(self) -> int:
        return self.__id;

    @property
    def content(self) -> str:
        return self._content;

    @property
    def date(self) -> datetime.datetime:
        return self._date;
    
    # Verified if the content is valid, if not it will raise an exception
    def validate_content(self):
        if not self._content or not self._content.strip():
            raise ValueError("Content cannot be empty.")
        return True
    
    # Verified if the date is valid, if not it will raise an exception
    def validate_date(self):
        if not self._date:
            raise ValueError("Date cannot be empty.")
        return True

    # Validate the log by checking all the attributes
    def validate(self) -> bool:
        return (
            self.validate_content() and 
            self.validate_date()
        )