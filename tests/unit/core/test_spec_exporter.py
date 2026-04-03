import pytest
from specflow_ai.core.spec_exporter import SpecExporter
from datetime import datetime

def test_spec_exporter_metadata():
    exporter = SpecExporter()
    data = {"author": "John Doe", "version": "1.0.0"}
    output = exporter.export_metadata(data)
    
    assert "## Metadata" in output
    assert "John Doe" in output
    assert "1.0.0" in output
    assert datetime.now().strftime("%Y-%m-%d") in output

def test_spec_exporter_out_of_scope():
    exporter = SpecExporter()
    data = {"out_of_scope": ["Mobile app", "Offline mode"]}
    output = exporter.export_out_of_scope(data)
    
    assert "## Out of Scope" in output
    assert "- Mobile app" in output
    assert "- Offline mode" in output

def test_spec_exporter_history():
    exporter = SpecExporter()
    data = {
        "questions": ["Q1", "Q2"],
        "answers": ["A1", "A2"]
    }
    output = exporter.export_history(data)
    
    assert "## Dialogue History" in output
    assert "Q1" in output
    assert "A1" in output
