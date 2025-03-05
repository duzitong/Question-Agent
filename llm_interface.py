from abc import ABC, abstractmethod

class LLMInterface(ABC):
    """
    Abstract interface for language model interactions.
    All LLM implementations should inherit from this class.
    """
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the language model based on the given prompt.
        
        Args:
            prompt (str): The input prompt for the language model
            
        Returns:
            str: The generated response from the language model
        """
        pass