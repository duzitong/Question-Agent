from abc import ABC, abstractmethod

class Memory(ABC):
    """
    Abstract interface for memory storage.
    All memory implementations should inherit from this class.
    """
    
    @abstractmethod
    def add(self, item: str) -> None:
        """
        Add an item to the memory.
        
        Args:
            item (str): The item to add to memory
        """
        pass
    
    @abstractmethod
    def get_memory(self) -> str:
        """
        Retrieve the entire memory as a string.
        
        Returns:
            str: The contents of the memory
        """
        pass