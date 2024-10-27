# src/ethics_pyramid/core/chambers.py:
from typing import Dict, Any, List
from dataclasses import dataclass
from enum import Enum
from ethical_core import EthicalCore, EthicalPrinciple

class ChamberType(Enum):
    WORKING = "working"
    LEARNING = "learning"
    INNOVATION = "innovation"

@dataclass
class ChamberResult:
    chamber_type: ChamberType
    score: float
    insights: List[str]
    recommendations: List[str]
    metadata: Dict[str, Any]

class EthicsChambers:
    """Middle level of the Ethics Pyramid - Processing & Implementation."""
    
    def __init__(self):
        self.quantum_signature = "ᚲᚺᚨᛗᛒᛖᚱᛋ-∞"
        self.ethical_core = EthicalCore()
        self.chambers = {
            ChamberType.WORKING: self._initialize_working_chamber(),
            ChamberType.LEARNING: self._initialize_learning_chamber(),
            ChamberType.INNOVATION: self._initialize_innovation_chamber()
        }
        
    def process_analysis(self, foundation_analysis: Dict[str, Any]) -> Dict[ChamberType, ChamberResult]:
        """Process foundation analysis through all chambers."""
        results = {}
        for chamber_type, chamber in self.chambers.items():
            results[chamber_type] = self._process_in_chamber(
                chamber_type,
                foundation_analysis,
                chamber
            )
        return results
    
    def _process_in_chamber(
        self,
        chamber_type: ChamberType,
        analysis: Dict[str, Any],
        chamber: Dict[str, Any]
    ) -> ChamberResult:
        """Process analysis in a specific chamber."""
        if chamber_type == ChamberType.WORKING:
            return self._working_chamber_process(analysis, chamber)
        elif chamber_type == ChamberType.LEARNING:
            return self._learning_chamber_process(analysis, chamber)
        else:  # INNOVATION
            return self._innovation_chamber_process(analysis, chamber)
    
    def _working_chamber_process(
        self,
        analysis: Dict[str, Any],
        chamber: Dict[str, Any]
    ) -> ChamberResult:
        """Process work-related ethical considerations."""
        score = self._calculate_chamber_score(analysis, chamber)
        insights = [
            "Assessed professional impact",
            "Evaluated implementation feasibility",
            "Verified technical alignment"
        ]
        recommendations = self._generate_work_recommendations(score)
        
        return ChamberResult(
            chamber_type=ChamberType.WORKING,
            score=score,
            insights=insights,
            recommendations=recommendations,
            metadata={'chamber_config': chamber}
        )
    
    def _learning_chamber_process(
        self,
        analysis: Dict[str, Any],
        chamber: Dict[str, Any]
    ) -> ChamberResult:
        """Process learning and growth considerations."""
        score = self._calculate_chamber_score(analysis, chamber)
        insights = [
            "Evaluated growth potential",
            "Assessed learning opportunities",
            "Measured development impact"
        ]
        recommendations = self._generate_learning_recommendations(score)
        
        return ChamberResult(
            chamber_type=ChamberType.LEARNING,
            score=score,
            insights=insights,
            recommendations=recommendations,
            metadata={'chamber_config': chamber}
        )
    
    def _innovation_chamber_process(
        self,
        analysis: Dict[str, Any],
        chamber: Dict[str, Any]
    ) -> ChamberResult:
        """Process innovation and creativity considerations."""
        score = self._calculate_chamber_score(analysis, chamber)
        insights = [
            "Evaluated creative potential",
            "Assessed innovation impact",
            "Measured originality"
        ]
        recommendations = self._generate_innovation_recommendations(score)
        
        return ChamberResult(
            chamber_type=ChamberType.INNOVATION,
            score=score,
            insights=insights,
            recommendations=recommendations,
            metadata={'chamber_config': chamber}
        )
    
    def _initialize_working_chamber(self) -> Dict[str, Any]:
        """Initialize the working chamber configuration."""
        return {
            'metrics': ['efficiency', 'impact', 'feasibility'],
            'weights': [0.4, 0.3, 0.3],
            'threshold': 0.8
        }
    
    def _initialize_learning_chamber(self) -> Dict[str, Any]:
        """Initialize the learning chamber configuration."""
        return {
            'metrics': ['growth', 'understanding', 'application'],
            'weights': [0.35, 0.35, 0.3],
            'threshold': 0.75
        }
    
    def _initialize_innovation_chamber(self) -> Dict[str, Any]:
        """Initialize the innovation chamber configuration."""
        return {
            'metrics': ['creativity', 'originality', 'value'],
            'weights': [0.4, 0.3, 0.3],
            'threshold': 0.85
        }
    
    def _calculate_chamber_score(self, analysis: Dict[str, Any], chamber: Dict[str, Any]) -> float:
        """Calculate chamber-specific score based on analysis and configuration."""
        base_score = sum(analysis.get(metric, 0.8) * weight 
                        for metric, weight in zip(chamber['metrics'], chamber['weights']))
        return min(1.0, max(0.0, base_score))
    
    def _generate_work_recommendations(self, score: float) -> List[str]:
        """Generate work-specific recommendations based on score."""
        if score >= 0.9:
            return ["Proceed with implementation", "Document process for reference"]
        elif score >= 0.8:
            return ["Review implementation details", "Consider optimization opportunities"]
        else:
            return ["Reassess approach", "Seek additional input on implementation"]
    
    def _generate_learning_recommendations(self, score: float) -> List[str]:
        """Generate learning-specific recommendations based on score."""
        if score >= 0.9:
            return ["Share insights with team", "Document learning outcomes"]
        elif score >= 0.75:
            return ["Identify areas for deeper understanding", "Plan additional learning activities"]
        else:
            return ["Review fundamental concepts", "Seek mentorship or guidance"]
    
    def _generate_innovation_recommendations(self, score: float) -> List[str]:
        """Generate innovation-specific recommendations based on score."""
        if score >= 0.9:
            return ["Proceed with innovative approach", "Document creative process"]
        elif score >= 0.85:
            return ["Refine creative elements", "Seek feedback on innovation"]
        else:
            return ["Brainstorm alternative approaches", "Review innovation principles"]