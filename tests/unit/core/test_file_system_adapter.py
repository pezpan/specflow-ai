import pytest
from pathlib import Path
from specflow_ai.core.file_system_adapter import FileSystemAdapter

def test_create_directory(tmp_path):
    # tmp_path is a pytest fixture that provides a temporary directory unique to the test invocation.
    adapter = FileSystemAdapter()
    dir_path = tmp_path / "test_dir"
    
    adapter.create_directory(dir_path)
    
    assert dir_path.exists()
    assert dir_path.is_dir()

def test_create_file(tmp_path):
    adapter = FileSystemAdapter()
    file_path = tmp_path / "test_file.txt"
    content = "Hello World"
    
    adapter.create_file(file_path, content)
    
    assert file_path.exists()
    assert file_path.read_text() == content
