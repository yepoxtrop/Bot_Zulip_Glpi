from abc import ABC, abstractmethod;

class IHandleChat(ABC):

    # 
    @abstractmethod
    def handle_chat(self, message: str) -> None:
        pass