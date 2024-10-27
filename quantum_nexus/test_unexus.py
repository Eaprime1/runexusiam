# quantum_nexus/test_unexus.py

from quantum_nexus.unexus_integration import UNEXUSBridge
from quantum_nexus.ethics.core import EthicalCore

def test_unexus_bridge():
    """Test UNEXUS integration functionality"""
    bridge = UNEXUSBridge()
    
    # Test initialization
    connection = bridge.initialize_bridge()
    assert connection['status'] == 'active'
    assert len(connection['reality_anchors']) >= 3
    
    # Test anchor creation with ethical evaluation
    ethics = EthicalCore()
    evaluation = ethics.evaluate_action('navigation', {
        'purpose': 'anchor_creation',
        'location': 'perspective_pyramid'
    })
    
    if evaluation['approved']:
        new_anchor = bridge.create_reality_anchor('perspective_pyramid')
        assert new_anchor['state'] == 'active'
    
    # Test status reporting
    status = bridge.get_bridge_status()
    assert status['unexus_connection']['status'] == 'active'