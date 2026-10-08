from abc import ABC, abstractmethod;

class IHandlerPlatformChat(ABC):

    # 
    @abstractmethod
    def handle_platform_chat(self, message: str) -> None:
        pass