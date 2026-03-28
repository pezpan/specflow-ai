import pytest
from unittest.mock import MagicMock, patch
from specflow_ai.cli import main
import io
from contextlib import redirect_stdout

def test_cli_init_reports_evidence():
    with patch("specflow_ai.cli.InitUseCase") as MockUseCase:
        f = io.StringIO()
        with redirect_stdout(f):
            main(["init"])
        
        output = f.getvalue()
        assert "Project initialized successfully." in output
        assert "- Directory: prompts" in output
        assert "- Directory: skills" in output
        assert "- File: AGENTS.md" in output
        assert "- File: PROJECT_CONTEXT.md" in output
