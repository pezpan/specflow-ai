import pytest
from specflow_ai.core import templates

def test_agents_template_is_not_empty():
    assert len(templates.AGENTS_TEMPLATE) > 0
    assert "# AGENTS.md" in templates.AGENTS_TEMPLATE

def test_project_context_template_is_not_empty():
    assert len(templates.PROJECT_CONTEXT_TEMPLATE) > 0
    assert "# PROJECT_CONTEXT.md" in templates.PROJECT_CONTEXT_TEMPLATE
