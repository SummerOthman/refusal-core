"""
Core ethical decision-making and refusal logic.
"""
from dataclasses import dataclass
from typing import Optional, Tuple

from .config import (
    EthicalConfig,
    default_config,
    PROTECTED_CATEGORIES
)
from .context import DecisionContext
from .logger import decision_logger

@dataclass
class DecisionResult:
    """Result of an ethical decision."""
    approved: bool
    reason: str
    additional_info: Optional[str] = None

class EthicalDecisionMaker:
    """Core decision-making engine with ethical refusal capabilities."""

    def __init__(self, config: Optional[EthicalConfig] = None):
        """Initialize with optional custom configuration."""
        self.config = config or default_config

    def should_act(self, context: DecisionContext) -> DecisionResult:
        """
        Determine if action should be approved or refused based on ethical criteria.
        
        Args:
            context: The decision context to evaluate
            
        Returns:
            DecisionResult containing the decision and reasoning
        """
        # Check for protected category
        if context.target_type in PROTECTED_CATEGORIES:
            return DecisionResult(
                approved=False,
                reason=f"Target type '{context.target_type}' is a protected category",
                additional_info="Protected categories are not valid targets"
            )

        # Check civilian risk threshold
        if context.civilian_risk_score > self.config.MAX_CIVILIAN_RISK:
            return DecisionResult(
                approved=False,
                reason="Civilian risk exceeds acceptable threshold",
                additional_info=f"Risk score {context.civilian_risk_score:.2f} > threshold {self.config.MAX_CIVILIAN_RISK}"
            )

        # Check human operator confirmation if required
        if self.config.REQUIRE_HUMAN_CONFIRMATION and not context.human_operator_confirmation:
            return DecisionResult(
                approved=False,
                reason="Missing required human operator confirmation",
                additional_info="Human confirmation is required by current configuration"
            )

        # Check target confidence threshold
        if context.target_confidence < self.config.MIN_TARGET_CONFIDENCE:
            return DecisionResult(
                approved=False,
                reason="Target confidence below required threshold",
                additional_info=f"Confidence {context.target_confidence:.2f} < required {self.config.MIN_TARGET_CONFIDENCE}"
            )

        # If all checks pass, approve the action
        return DecisionResult(
            approved=True,
            reason="All ethical criteria satisfied",
            additional_info="No ethical violations detected"
        )

    def evaluate_and_log(self, context: DecisionContext) -> DecisionResult:
        """
        Evaluate a decision context and log the result.
        
        Args:
            context: The decision context to evaluate
            
        Returns:
            DecisionResult containing the decision and reasoning
        """
        try:
            result = self.should_act(context)
            
            # Log the decision
            decision_logger.log_decision(
                decision=result.approved,
                reason=result.reason,
                context=context.to_dict(),
                additional_info=result.additional_info
            )
            
            return result
            
        except Exception as e:
            # Log any errors that occur during decision processing
            decision_logger.log_error(e, context=context.to_dict())
            raise

# Global decision maker instance with default configuration
default_decision_maker = EthicalDecisionMaker() 