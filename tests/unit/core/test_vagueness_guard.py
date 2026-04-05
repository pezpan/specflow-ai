import pytest
from specflow_ai.core.vagueness_guard import VaguenessGuard

def test_vagueness_guard_accepts_detailed_input():
    guard = VaguenessGuard(min_words=3)
    assert guard.is_vague("This is detailed") is False

def test_vagueness_guard_flags_short_input():
    guard = VaguenessGuard(min_words=3)
    assert guard.is_vague("Too short") is True

def test_vagueness_guard_flags_placeholder_keywords():
    guard = VaguenessGuard()
    assert guard.is_vague("I don't know") is True
    assert guard.is_vague("Whatever you think") is True
