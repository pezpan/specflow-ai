from specflow_ai.core.io_ports import InputPort, OutputPort

class ConsoleInputAdapter(InputPort):
    """
    Standard console input implementation.
    """
    def get_input(self, prompt: str) -> str:
        return input(prompt)

class ConsoleOutputAdapter(OutputPort):
    """
    Standard console output implementation with structured error feedback.
    """
    def show_message(self, message: str) -> None:
        print(message)

    def show_error(self, message: str, details: list[str] | None = None) -> None:
        print(f"\nERROR: {message}")
        if details:
            for detail in details:
                print(f"  - {detail}")
        print()
