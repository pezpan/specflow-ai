import pytest
from unittest.mock import MagicMock, patch
from specflow_ai.cli import main

def test_cli_init_command_calls_use_case():
    with patch("specflow_ai.cli.InitUseCase") as MockUseCase:
        mock_use_case_instance = MockUseCase.return_value
        
        # Simulate running: python -m specflow_ai.cli init
        main(["init"])
        
        MockUseCase.assert_called_once()
        mock_use_case_instance.execute.assert_called_once()
