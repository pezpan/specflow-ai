import pytest
from unittest.mock import MagicMock
from specflow_ai.core.specify_use_case import SpecifyUseCase
from specflow_ai.core.critic_agent import ValidationResult

def test_specify_use_case_blocking_on_validation_failure():
    # Arrange
    dialogue_controller = MagicMock()
    gherkin_generator = MagicMock()
    spec_exporter = MagicMock()
    persistence_service = MagicMock()
    critic_agent = MagicMock()
    
    # Mock failure
    critic_agent.validate.return_value = ValidationResult(is_valid=False, issues=["Error 1"])
    
    use_case = SpecifyUseCase(
        dialogue_controller=dialogue_controller,
        gherkin_generator=gherkin_generator,
        spec_exporter=spec_exporter,
        persistence_service=persistence_service,
        critic_agent=critic_agent
    )
    
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        use_case.execute("feature_name")
    
    assert "Specification validation failed" in str(excinfo.value)
    persistence_service.save_spec.assert_not_called()

def test_specify_use_case_success():
    # Arrange
    dialogue_controller = MagicMock()
    gherkin_generator = MagicMock()
    spec_exporter = MagicMock()
    persistence_service = MagicMock()
    critic_agent = MagicMock()
    
    critic_agent.validate.return_value = ValidationResult(is_valid=True)
    
    use_case = SpecifyUseCase(
        dialogue_controller=dialogue_controller,
        gherkin_generator=gherkin_generator,
        spec_exporter=spec_exporter,
        persistence_service=persistence_service,
        critic_agent=critic_agent
    )
    
    # Act
    use_case.execute("feature_name")
    
    # Assert
    dialogue_controller.run.assert_called_once()
    persistence_service.save_spec.assert_called_once()
