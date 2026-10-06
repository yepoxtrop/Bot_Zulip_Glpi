import datetime;

class Message:
    
    def __init__(self, id:int, content:str, author:str, date:datetime.datetime):
        
        self.__id = id; 
        self._content = content;
        self._author = author;
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
    def author(self) -> str:
        return self._author;

    @property
    def date(self) -> datetime.datetime:
        return self._date;
    
    # Verified if the user is valid, if not it will raise an exception
    def validate_content(self) -> str:
        if not self._content or not self._content.strip():
            raise ValueError("Content cannot be empty.")
        return True
    
    # Verified if the origin is valid, if not it will raise an exception
    def validate_author(self) -> str:
        if not self._author or not self._author.strip():
            raise ValueError("Author cannot be empty.")
        return True
    
    # Verified if the identity is valid, if not it will raise an exception
    def validate_date(self) -> datetime.datetime:
        if not self._date:
            raise ValueError("Date cannot be empty.")
        return True

    # Validate the user by checking all the attributes
    def validate(self) -> bool:
        return (
            self.validate_content() and 
            self.validate_author() and 
            self.validate_date()
        )