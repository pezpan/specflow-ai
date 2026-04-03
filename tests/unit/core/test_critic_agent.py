import pytest
from specflow_ai.core.critic_agent import CriticAgent

def test_critic_agent_validation_success():
    agent = CriticAgent()
    content = "Característica: Test\n  Escenario: Valid\n    Dado a\n    Cuando b\n    Entonces c"
    result = agent.validate(content)
    assert result.is_valid is True
    assert not result.issues

def test_critic_agent_validation_failure_missing_gherkin():
    agent = CriticAgent()
    content = "This is not gherkin"
    result = agent.validate(content)
    assert result.is_valid is False
    assert "Missing Gherkin keywords (Característica, Escenario, Dado, Cuando, Entonces)" in result.issues

def test_critic_agent_consistency_check_redundancy():
    agent = CriticAgent()
    # Given and Then are identical
    content = "Característica: Test\n  Escenario: Redundant\n    Dado same state\n    Cuando action\n    Entonces same state"
    result = agent.validate(content)
    assert result.is_valid is False
    assert "Redundancy detected: Given and Then conditions are identical" in result.issues
