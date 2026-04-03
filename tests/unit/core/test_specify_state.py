import pytest
from specflow_ai.core.specify_state import SpecifyState

def test_specify_state_initialization():
    state = SpecifyState()
    assert state.question_count == 0
    assert state.gathered_data == {}
    assert state.is_ready_to_generate is False

def test_specify_state_add_data():
    state = SpecifyState()
    state.add_response("target_users", "Developers")
    assert state.question_count == 1
    assert state.gathered_data["target_users"] == "Developers"

def test_specify_state_ready_to_generate():
    state = SpecifyState()
    state.add_response("q1", "a1")
    state.add_response("q2", "a2")
    assert state.is_ready_to_generate is False
    state.add_response("q3", "a3")
    assert state.is_ready_to_generate is True
