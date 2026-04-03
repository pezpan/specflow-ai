from typing import Any

class SpecifyState:
    """
    Manages the state of the /sdd.specify dialogue process.
    """
    def __init__(self, min_questions: int = 3):
        self.question_count = 0
        self.gathered_data: dict[str, Any] = {}
        self.min_questions = min_questions

    def add_response(self, key: str, value: Any) -> None:
        """
        Adds a user response to the state.
        """
        self.gathered_data[key] = value
        self.question_count += 1

    @property
    def is_ready_to_generate(self) -> bool:
        """
        Checks if the state has met the minimum question threshold.
        """
        return self.question_count >= self.min_questions
