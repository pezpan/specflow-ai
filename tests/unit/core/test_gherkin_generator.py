import pytest
from specflow_ai.core.gherkin_generator import GherkinGenerator

def test_gherkin_generator_simple_scenario():
    # Arrange
    data = {
        "feature_name": "Login",
        "scenario_name": "Successful login",
        "given": "the user is on the login page",
        "when": "the user enters valid credentials",
        "then": "the user is redirected to the dashboard"
    }
    generator = GherkinGenerator()
    
    # Act
    output = generator.generate(data)
    
    # Assert
    assert "Característica: Login" in output or "Feature: Login" in output
    assert "Escenario: Successful login" in output or "Scenario: Successful login" in output
    assert "Dado the user is on the login page" in output or "Given the user is on the login page" in output
    assert "Cuando the user enters valid credentials" in output or "When the user enters valid credentials" in output
    assert "Entonces the user is redirected to the dashboard" in output or "Then the user is redirected to the dashboard" in output

def test_gherkin_generator_handles_missing_keys():
    generator = GherkinGenerator()
    with pytest.raises(KeyError):
        generator.generate({})
