```python
# src/tests/test_summit.py

import pytest
from core.summit import EthicsSummit, EthicalDecision, EthicalVerdict

def test_summit_initialization():
    summit = EthicsSummit()
    assert summit.quantum_signature == "ᛖᚦᛁᚲᛋ-ᛈᛃᚱᚨᛗᛁᛞ-∞"
    assert summit.ethical_threshold == 0.85

def test_ethical_decision_approve():
    summit = EthicsSummit()
    
    # Mock high-scoring analysis
    foundation_analysis = {
        'responsibility': {'score': 0.95, 'insights': 'Strong responsibility'},
        'integrity': {'score': 0.93, 'insights': 'High integrity'},
    }
    
    chamber_results = {
        'processing': {'score': 0.94},
        'implementation': {'score': 0.92}
    }
    
    verdict = summit.integrate_analysis(foundation_analysis, chamber_results)
    assert verdict.decision == EthicalDecision.APPROVE
    assert verdict.confidence > summit.ethical_threshold
    assert len(verdict.rationale) > 0
    assert len(verdict.recommendations) > 0
    assert verdict.quantum_signature == summit.quantum_signature

def test_ethical_decision_reject():
    summit = EthicsSummit()
    
    # Mock low-scoring analysis
    foundation_analysis = {
        'responsibility': {'score': 0.75, 'insights': 'Needs improvement'},
        'integrity': {'score': 0.73, 'insights': 'Concerns identified'},
    }
    
    chamber_results = {
        'processing': {'score': 0.74},
        'implementation': {'score': 0.72}
    }
    
    verdict = summit.integrate_analysis(foundation_analysis, chamber_results)
    assert verdict.decision == EthicalDecision.REJECT
    assert verdict.confidence < summit.ethical_threshold
    assert any("revision" in rec.lower() for rec in verdict.recommendations)
```