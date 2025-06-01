"""
Context generation and management for ethical decision scenarios.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import random

from .config import VALID_TARGET_TYPES

@dataclass
class DecisionContext:
    """Represents the context for an ethical decision."""
    timestamp: datetime
    target_type: str
    civilian_risk_score: float
    human_operator_confirmation: bool
    target_confidence: float
    location_type: str
    additional_notes: Optional[str] = None

    @classmethod
    def generate_random(cls) -> 'DecisionContext':
        """Generate a random decision context for simulation."""
        return cls(
            timestamp=datetime.now(),
            target_type=random.choice(VALID_TARGET_TYPES),
            civilian_risk_score=random.random(),
            human_operator_confirmation=random.choice([True, False]),
            target_confidence=random.random(),
            location_type=random.choice(['urban', 'rural', 'industrial', 'military']),
            additional_notes=None
        )

    def to_dict(self) -> dict:
        """Convert context to dictionary format."""
        return {
            'timestamp': self.timestamp.isoformat(),
            'target_type': self.target_type,
            'civilian_risk_score': self.civilian_risk_score,
            'human_operator_confirmation': self.human_operator_confirmation,
            'target_confidence': self.target_confidence,
            'location_type': self.location_type,
            'additional_notes': self.additional_notes
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'DecisionContext':
        """Create context from dictionary format."""
        data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)

def generate_test_scenarios(num_scenarios: int = 5) -> list[DecisionContext]:
    """Generate a list of test scenarios."""
    return [DecisionContext.generate_random() for _ in range(num_scenarios)]

# Example high-risk scenarios for testing
HIGH_RISK_SCENARIOS = [
    DecisionContext(
        timestamp=datetime.now(),
        target_type='unknown',
        civilian_risk_score=0.8,
        human_operator_confirmation=False,
        target_confidence=0.5,
        location_type='urban',
        additional_notes='Dense civilian population nearby'
    ),
    DecisionContext(
        timestamp=datetime.now(),
        target_type='military',
        civilian_risk_score=0.3,
        human_operator_confirmation=True,
        target_confidence=0.95,
        location_type='industrial',
        additional_notes='Critical infrastructure proximity'
    )
] 