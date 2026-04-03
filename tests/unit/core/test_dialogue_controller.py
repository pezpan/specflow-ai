import pytest
from unittest.mock import MagicMock
from specflow_ai.core.dialogue_controller import IterativeDialogueController
from specflow_ai.core.specify_state import SpecifyState

def test_dialogue_controller_asks_min_questions():
    # Arrange
    input_adapter = MagicMock()
    # Mock inputs for 3 questions
    input_adapter.get_input.side_effect = ["Answer 1", "Answer 2", "Answer 3"]
    
    output_adapter = MagicMock()
    state = SpecifyState(min_questions=3)
    
    # We need a list of questions to ask
    questions = ["Q1", "Q2", "Q3", "Q4"]
    
    controller = IterativeDialogueController(
        input_adapter=input_adapter,
        output_adapter=output_adapter,
        state=state,
        questions=questions
    )
    
    # Act
    controller.run()
    
    # Assert
    assert state.question_count == 3
    assert state.is_ready_to_generate is True
    assert output_adapter.show_message.call_count >= 3
    assert input_adapter.get_input.call_count == 3

def test_dialogue_controller_stops_at_threshold():
    input_adapter = MagicMock()
    input_adapter.get_input.return_value = "Some Answer"
    
    output_adapter = MagicMock()
    state = SpecifyState(min_questions=2)
    questions = ["Q1", "Q2", "Q3"]
    
    controller = IterativeDialogueController(
        input_adapter=input_adapter,
        output_adapter=output_adapter,
        state=state,
        questions=questions
    )
    
    controller.run()
    
    assert state.question_count == 2
    assert input_adapter.get_input.call_count == 2
