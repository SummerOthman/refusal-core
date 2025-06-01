"""
Logging system for ethical decisions and refusals.
"""
import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Union, Dict, Any

from loguru import logger

# Configure logging
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Configure loguru logger
logger.add(
    LOG_DIR / "refusal_log.txt",
    rotation="500 MB",
    retention="30 days",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO"
)

class DecisionLogger:
    """Logger for ethical decisions and refusals."""
    
    @staticmethod
    def log_decision(
        decision: bool,
        reason: str,
        context: Dict[str, Any],
        additional_info: Optional[str] = None
    ) -> None:
        """
        Log a decision with its context and reasoning.
        
        Args:
            decision: True if action approved, False if refused
            reason: Explanation for the decision
            context: Decision context dictionary
            additional_info: Optional additional information
        """
        status = "APPROVED" if decision else "REFUSED"
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "status": status,
            "reason": reason,
            "context": context,
            "additional_info": additional_info
        }
        
        # Log with appropriate level and formatting
        log_level = "INFO" if decision else "WARNING"
        logger.log(
            log_level,
            "\n{}\nStatus: {}\nReason: {}\nContext: {}\nAdditional Info: {}\n{}\n",
            "="*50,
            status,
            reason,
            context,
            additional_info or "None",
            "="*50
        )

    @staticmethod
    def log_error(error: Union[str, Exception], context: Optional[Dict[str, Any]] = None) -> None:
        """Log an error that occurred during decision processing."""
        logger.error(
            "\nERROR\nMessage: {}\nContext: {}\n",
            str(error),
            context or "No context provided"
        )

    @staticmethod
    def get_recent_decisions(n: int = 10) -> list:
        """Retrieve the n most recent decisions from the log."""
        # This is a placeholder - in a real implementation, you would parse the log file
        # and return the actual recent decisions
        return []  # TODO: Implement log parsing

# Global logger instance
decision_logger = DecisionLogger() 