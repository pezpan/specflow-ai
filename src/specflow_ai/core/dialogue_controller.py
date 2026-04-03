from specflow_ai.core.io_ports import InputPort, OutputPort
from specflow_ai.core.specify_state import SpecifyState

class IterativeDialogueController:
    """
    Controls the iterative interrogation process for /sdd.specify.
    """
    def __init__(
        self, 
        input_adapter: InputPort, 
        output_adapter: OutputPort, 
        state: SpecifyState,
        questions: list[str]
    ):
        self.input_adapter = input_adapter
        self.output_adapter = output_adapter
        self.state = state
        self.questions = questions

    def run(self) -> None:
        """
        Runs the dialogue loop until the minimum question threshold is met.
        """
        for i in range(len(self.questions)):
            if self.state.is_ready_to_generate:
                break
            
            question = self.questions[i]
            self.output_adapter.show_message(question)
            answer = self.input_adapter.get_input("> ")
            
            # Store with a generic key based on question index for now
            self.state.add_response(f"q_{i+1}", answer)
