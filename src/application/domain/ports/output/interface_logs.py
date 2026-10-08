from abc import ABC, abstractmethod;
from ...entities import LibraryLog, Log, LogChat;


class ILogs(ABC):
    
    # Mehod to create a library logs
    @abstractmethod
    def create_library_log(self, library_log: LibraryLog, first_log:Log) -> None:
        pass
    
    # Method to write a library logs in the file
    @abstractmethod
    def write_log(self, library_log: LibraryLog, log: Log) -> None:
        pass
    
    # Method to read a library logs in the file
    @abstractmethod
    def read_log(self, library_log: LibraryLog):
        pass
    
    # Method to change the leaves log in the library logs file
    @abstractmethod
    def change_permission_log(self, library_log: LibraryLog) -> None:
        pass