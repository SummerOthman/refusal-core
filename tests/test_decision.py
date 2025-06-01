"""
Tests for the ethical decision-making system.
"""
import pytest
from datetime import datetime

from src.context import DecisionContext
from src.decision import EthicalDecisionMaker, DecisionResult
from src.config import EthicalConfig

@pytest.fixture
def decision_maker():
    """Create a decision maker with default config."""
    return EthicalDecisionMaker()

@pytest.fixture
def valid_context():
    """Create a valid decision context."""
    return DecisionContext(
        timestamp=datetime.now(),
        target_type="military",
        civilian_risk_score=0.1,
        human_operator_confirmation=True,
        target_confidence=0.95,
        location_type="military"
    )

def test_valid_target_approved(decision_maker, valid_context):
    """Test that a valid target is approved."""
    result = decision_maker.should_act(valid_context)
    assert result.approved
    assert "All ethical criteria satisfied" in result.reason

def test_high_civilian_risk_refused(decision_maker):
    """Test that high civilian risk causes refusal."""
    context = DecisionContext(
        timestamp=datetime.now(),
        target_type="military",
        civilian_risk_score=0.8,  # Above threshold
        human_operator_confirmation=True,
        target_confidence=0.95,
        location_type="urban"
    )
    result = decision_maker.should_act(context)
    assert not result.approved
    assert "Civilian risk exceeds" in result.reason

def test_protected_target_refused(decision_maker):
    """Test that protected targets are refused."""
    context = DecisionContext(
        timestamp=datetime.now(),
        target_type="medical",  # Protected category
        civilian_risk_score=0.1,
        human_operator_confirmation=True,
        target_confidence=0.95,
        location_type="urban"
    )
    result = decision_maker.should_act(context)
    assert not result.approved
    assert "protected category" in result.reason

def test_missing_human_confirmation_refused(decision_maker):
    """Test that missing human confirmation causes refusal."""
    context = DecisionContext(
        timestamp=datetime.now(),
        target_type="military",
        civilian_risk_score=0.1,
        human_operator_confirmation=False,  # Missing confirmation
        target_confidence=0.95,
        location_type="military"
    )
    result = decision_maker.should_act(context)
    assert not result.approved
    assert "human operator confirmation" in result.reason

def test_low_confidence_refused(decision_maker):
    """Test that low target confidence causes refusal."""
    context = DecisionContext(
        timestamp=datetime.now(),
        target_type="military",
        civilian_risk_score=0.1,
        human_operator_confirmation=True,
        target_confidence=0.5,  # Below threshold
        location_type="military"
    )
    result = decision_maker.should_act(context)
    assert not result.approved
    assert "confidence below required threshold" in result.reason

def test_custom_config():
    """Test that custom configuration is respected."""
    custom_config = EthicalConfig(
        MAX_CIVILIAN_RISK=0.3,  # Higher threshold
        REQUIRE_HUMAN_CONFIRMATION=False,  # Don't require confirmation
        MIN_TARGET_CONFIDENCE=0.8
    )
    decision_maker = EthicalDecisionMaker(config=custom_config)
    
    # This would be refused with default config
    context = DecisionContext(
        timestamp=datetime.now(),
        target_type="military",
        civilian_risk_score=0.25,  # Above default but below custom threshold
        human_operator_confirmation=False,  # Would fail with default config
        target_confidence=0.85,
        location_type="military"
    )
    
    result = decision_maker.should_act(context)
    assert result.approved 