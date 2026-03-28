import pytest
from unittest.mock import MagicMock, ANY
from specflow_ai.core.init_use_case import InitUseCase

def test_init_use_case_executes_successfully():
    # Arrange
    fs_adapter = MagicMock()
    use_case = InitUseCase(fs_adapter=fs_adapter)
    
    # Act
    use_case.execute()
    
    # Assert
    # Verify created directories
    fs_adapter.create_directory.assert_any_call("prompts")
    fs_adapter.create_directory.assert_any_call("skills")
    
    # Verify created files
    fs_adapter.create_file.assert_any_call("AGENTS.md", ANY)
    fs_adapter.create_file.assert_any_call("PROJECT_CONTEXT.md", ANY)
