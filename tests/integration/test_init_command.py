import os
import pytest
from pathlib import Path
from specflow_ai.cli import main

def test_init_command_integration(tmp_path):
    # Change current working directory to tmp_path for the test
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    
    try:
        # Act
        # Run the CLI 'init' command
        main(["init"])
        
        # Assert
        # Verify directories exist
        assert (tmp_path / "prompts").exists()
        assert (tmp_path / "prompts").is_dir()
        assert (tmp_path / "skills").exists()
        assert (tmp_path / "skills").is_dir()
        
        # Verify files exist and have content
        agents_file = tmp_path / "AGENTS.md"
        assert agents_file.exists()
        assert "# AGENTS.md" in agents_file.read_text()
        
        project_context_file = tmp_path / "PROJECT_CONTEXT.md"
        assert project_context_file.exists()
        assert "# PROJECT_CONTEXT.md" in project_context_file.read_text()
        
    finally:
        # Change back to original CWD
        os.chdir(original_cwd)
