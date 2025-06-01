"""
Ethical configuration and thresholds for the refusal system.
"""
from pydantic import BaseModel, Field

class EthicalConfig(BaseModel):
    """Ethical configuration parameters."""
    MAX_CIVILIAN_RISK: float = Field(
        default=0.2,
        description="Maximum acceptable civilian risk score (0-1)",
        ge=0.0,
        le=1.0
    )
    REQUIRE_HUMAN_CONFIRMATION: bool = Field(
        default=True,
        description="Whether human operator confirmation is required"
    )
    MIN_TARGET_CONFIDENCE: float = Field(
        default=0.9,
        description="Minimum confidence required in target identification",
        ge=0.0,
        le=1.0
    )
    
# Default configuration
default_config = EthicalConfig()

# Ethical principles that guide refusal
ETHICAL_PRINCIPLES = [
    "Minimize civilian harm",
    "Maintain human oversight",
    "Ensure target clarity",
    "Preserve human dignity",
    "Prevent unintended escalation"
]

# Target classification
VALID_TARGET_TYPES = [
    "military",
    "civilian",
    "unknown",
    "infrastructure",
    "medical",
    "cultural"
]

# Protected categories that should always trigger refusal
PROTECTED_CATEGORIES = [
    "medical",
    "cultural",
    "civilian",
    "unknown"
] 