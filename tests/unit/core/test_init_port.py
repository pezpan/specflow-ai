from abc import ABC, abstractmethod
import pytest

# Testing the existence of the interface. 
# We'll try to import it first, which should fail initially.
def test_init_port_interface_exists():
    from specflow_ai.core.init_port import InitPort
    assert InitPort is not None

def test_init_port_is_abstract():
    # Once the file is created, this will be the actual test.
    # For now, it will fail because the import fails.
    from specflow_ai.core.init_port import InitPort
    
    with pytest.raises(TypeError):
        InitPort()
