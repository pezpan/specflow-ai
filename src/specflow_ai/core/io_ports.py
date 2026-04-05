from abc import ABC, abstractmethod

class InputPort(ABC):
    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass

class OutputPort(ABC):
    @abstractmethod
    def show_message(self, message: str) -> None:
        pass

    @abstractmethod
    def show_error(self, message: str, details: list[str] | None = None) -> None:
        pass
