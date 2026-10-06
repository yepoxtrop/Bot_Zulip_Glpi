from ..models.platforms import Platforms;

class User:
    # Constructor
    def __init__(self, id:int,  name:str, identity:str, origin:Platforms):
        self.__id = id; 
        self._name = name;
        self._identity = identity;
        self._origin = origin;
        
        self.validate(); # Validate the user when it is created
    
    # Getters 
    # Only the id is private, the rest of the attributes are protected
    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self._name

    @property
    def identity(self) -> str:
        return self._identity

    @property
    def origin(self) -> Platforms:
        return self._origin
    
    # Verified if the user is valid, if not it will raise an exception
    def validate_username(self) -> bool:
        if not self._name or not self._name.strip():
            raise ValueError("Username cannot be empty.")
        return True
    
    # Verified if the origin is valid, if not it will raise an exception
    def validate_identity(self) -> bool:
        if not self._identity or not self._identity.strip():
            raise ValueError("Identity cannot be empty.")
        return True
    
    # Verified if the identity is valid, if not it will raise an exception
    def validate_origin(self) -> bool:
        if not self._origin:
            raise ValueError("Origin cannot be empty.")
        return True

    # Validate the user by checking all the attributes
    def validate(self) -> bool:
        return (
            self.validate_username() and 
            self.validate_identity() and 
            self.validate_origin()
        ) 