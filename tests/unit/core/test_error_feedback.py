import pytest
from specflow_ai.core.io_adapters import ConsoleOutputAdapter
import io
from contextlib import redirect_stdout

def test_console_output_adapter_formats_errors():
    adapter = ConsoleOutputAdapter()
    f = io.StringIO()
    with redirect_stdout(f):
        adapter.show_error("Validation failed", ["Missing keyword", "Redundancy"])
    
    output = f.getvalue()
    assert "ERROR: Validation failed" in output
    assert "- Missing keyword" in output
    assert "- Redundancy" in output
