from .log import Log;

class LibraryLog:
    
    def __init__(self, id:int, path:str, name:str, list_logs:list[Log]|list = []):
        self.__id = id;
        self._list_logs = list_logs;
        self._path = path;
        self._name = name;
        
        self.validate();
        
    # Getters 
    # Only the id is private, the rest of the attributes are protected
    @property
    def id(self) -> int:
        return self.__id;

    @property
    def list_logs(self) -> list[Log]|list:
        return self._list_logs;
    
    @property
    def path(self) -> str:
        return self._path;
    
    @property
    def name(self) -> str:
        return self._name;

    # Verified if the list logs is valid, if not it will raise an exception
    def validate_list_logs(self):
        if not self._list_logs or not isinstance(self._list_logs, list):
            raise ValueError("List logs cannot be empty.")
        return True
    
    # Verified if the path is valid, if not it will raise an exception
    def validate_path(self):
        if not self._path or not self._path.strip():
            raise ValueError("Path cannot be empty.")
        return True
    
    # Verified if the name is valid, if not it will raise an exception
    def validate_name(self):
        if not self._name or not self._name.strip():
            raise ValueError("Name cannot be empty.")
        return True

    # Validate the log by checking all the attributes
    def validate(self) -> bool:
        return (
            self.validate_list_logs() and 
            self.validate_path() and 
            self.validate_name()
        )