import pytest
from unittest.mock import MagicMock
from specflow_ai.core.persistence_service import PersistenceService

def test_persistence_service_saves_spec():
    # Arrange
    fs_adapter = MagicMock()
    service = PersistenceService(fs_adapter=fs_adapter)
    feature_name = "login_feature"
    content = "# Spec content"
    
    # Act
    service.save_spec(feature_name, content)
    
    # Assert
    expected_path = f"specs/{feature_name}/spec.md"
    fs_adapter.create_file.assert_called_once_with(expected_path, content)
