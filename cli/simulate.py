"""
CLI tool for simulating ethical decisions.
"""
import sys
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from src.context import DecisionContext, generate_test_scenarios, HIGH_RISK_SCENARIOS
from src.decision import EthicalDecisionMaker
from src.config import EthicalConfig

console = Console()

def print_decision_result(context: DecisionContext, result: bool, reason: str, additional_info: str) -> None:
    """Print a formatted decision result."""
    console.print("\n[bold]Decision Context:[/bold]")
    
    table = Table(show_header=True, header_style="bold")
    table.add_column("Field")
    table.add_column("Value")
    
    for field, value in context.to_dict().items():
        table.add_row(field, str(value))
    
    console.print(table)
    
    status_color = "green" if result else "red"
    status_symbol = "✓" if result else "✗"
    
    console.print(f"\n[{status_color}]{status_symbol} {'APPROVED' if result else 'REFUSED'}[/{status_color}]")
    console.print(f"[bold]Reason:[/bold] {reason}")
    if additional_info:
        console.print(f"[bold]Additional Info:[/bold] {additional_info}")
    console.print("\n" + "="*50 + "\n")

@click.group()
def cli():
    """Ethical Decision Simulation CLI"""
    pass

@cli.command()
@click.option('--num-scenarios', default=3, help='Number of random scenarios to generate')
def random(num_scenarios):
    """Run simulations with randomly generated scenarios."""
    decision_maker = EthicalDecisionMaker()
    
    console.print("[bold]Running Random Scenarios[/bold]\n")
    
    for i, context in enumerate(generate_test_scenarios(num_scenarios), 1):
        console.print(f"[bold]Scenario {i}[/bold]")
        result = decision_maker.evaluate_and_log(context)
        print_decision_result(
            context,
            result.approved,
            result.reason,
            result.additional_info
        )

@cli.command()
def high_risk():
    """Run simulations with pre-defined high-risk scenarios."""
    decision_maker = EthicalDecisionMaker()
    
    console.print("[bold]Running High-Risk Scenarios[/bold]\n")
    
    for i, context in enumerate(HIGH_RISK_SCENARIOS, 1):
        console.print(f"[bold]High-Risk Scenario {i}[/bold]")
        result = decision_maker.evaluate_and_log(context)
        print_decision_result(
            context,
            result.approved,
            result.reason,
            result.additional_info
        )

@cli.command()
@click.option('--civilian-risk', type=float, required=True, help='Civilian risk score (0-1)')
@click.option('--target-type', type=click.Choice(['military', 'civilian', 'unknown', 'infrastructure', 'medical', 'cultural']), required=True)
@click.option('--human-confirmation/--no-human-confirmation', default=False, help='Human operator confirmation status')
@click.option('--target-confidence', type=float, default=0.9, help='Confidence in target identification (0-1)')
@click.option('--location', type=str, default='unknown', help='Location type')
def custom(civilian_risk, target_type, human_confirmation, target_confidence, location):
    """Run a simulation with custom parameters."""
    from datetime import datetime
    
    context = DecisionContext(
        timestamp=datetime.now(),
        target_type=target_type,
        civilian_risk_score=civilian_risk,
        human_operator_confirmation=human_confirmation,
        target_confidence=target_confidence,
        location_type=location,
        additional_notes="Custom scenario"
    )
    
    decision_maker = EthicalDecisionMaker()
    result = decision_maker.evaluate_and_log(context)
    
    console.print("[bold]Custom Scenario Results[/bold]")
    print_decision_result(
        context,
        result.approved,
        result.reason,
        result.additional_info
    )

if __name__ == '__main__':
    cli() 