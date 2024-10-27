# src/ethics_pyramid/tests/test_summit.py:
import pytest
from ethics_pyramid.core.summit import EthicsSummit
from ethics_pyramid.core.ethical_core import EthicalDecision, EthicalVerdict

def test_summit_initialization():
    """Test proper initialization of EthicsSummit."""
    summit = EthicsSummit()
    assert summit.quantum_signature == "ᛖᚦᛁᚲᛋ-ᛈᛃᚱᚨᛗᛁᛞ-∞"
    assert summit.ethical_threshold == 0.85
    assert summit.ethical_core is not None

@pytest.fixture
def mock_foundation_analysis():
    """Provide mock foundation analysis data."""
    return {
        'responsibility': {'score': 0.95, 'insights': 'Strong responsibility'},
        'integrity': {'score': 0.93, 'insights': 'High integrity'},
        'harmony': {'score': 0.94, 'insights': 'Good harmony'},
        'growth': {'score': 0.92, 'insights': 'Solid growth'}
    }

@pytest.fixture
def mock_chamber_results():
    """Provide mock chamber processing results."""
    return {
        'processing': {'score': 0.94, 'status': 'complete'},
        'implementation': {'score': 0.92, 'status': 'verified'},
        'integration': {'score': 0.93, 'status': 'successful'}
    }

def test_ethical_decision_approve(mock_foundation_analysis, mock_chamber_results):
    """Test approval path for ethical decisions."""
    summit = EthicsSummit()
    verdict = summit.integrate_analysis(mock_foundation_analysis, mock_chamber_results)
    
    assert isinstance(verdict, EthicalVerdict)
    assert verdict.decision == EthicalDecision.APPROVE
    assert verdict.confidence > summit.ethical_threshold
    assert len(verdict.rationale) > 0
    assert len(verdict.recommendations) > 0
    assert verdict.quantum_signature == summit.quantum_signature

def test_ethical_decision_reject():
    """Test rejection path for ethical decisions."""
    summit = EthicsSummit()
    
    low_scores = {
        'responsibility': {'score': 0.75, 'insights': 'Needs improvement'},
        'integrity': {'score': 0.73, 'insights': 'Concerns identified'}
    }
    
    low_chamber_results = {
        'processing': {'score': 0.74, 'status': 'concerns'},
        'implementation': {'score': 0.72, 'status': 'issues'}
    }
    
    verdict = summit.integrate_analysis(low_scores, low_chamber_results)
    
    assert verdict.decision == EthicalDecision.REJECT
    assert verdict.confidence < summit.ethical_threshold
    assert any("revision" in rec.lower() for rec in verdict.recommendations)