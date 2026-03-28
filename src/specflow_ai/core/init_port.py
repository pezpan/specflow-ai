from abc import ABC, abstractmethod

class InitPort(ABC):
    @abstractmethod
    def execute(self) -> None:
        """
        Executes the initialization process.
        """
        pass
