# quantum_nexus/test_core.py

from quantum_nexus.core import QuantumCore

def test_quantum_core():
    """Simple test to verify core functionality"""
    core = QuantumCore()
    state = core.initialize_system()
    assert state['ethical_alignment'] > 0.9
    
    thread = core.add_thread('test_thread', 'development')
    assert thread['state'] == 'active'
    
    status = core.get_system_status()
    assert status['active_threads'] == 1