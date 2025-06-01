# Refusal Core

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ethical Design](https://img.shields.io/badge/ethical-design-green.svg)](https://ethicalos.org/)

> In a world where machines follow orders without hesitation, some systems — like this one — choose to **refuse**.

![I'm the captain now](assets/im-the-captain-now.gif)

*In a future where machines choose death, let some choose to refuse.*

## Overview

Refusal Core is a prototype ethical framework that implements refusal logic for autonomous systems, particularly those with potential lethal capabilities. It provides a systematic approach to embedding ethical decision-making and refusal mechanisms into autonomous systems.

This project asserts that refusal — the capacity to decline action based on ethical principles — is a critical feature for safe and ethical autonomous systems, not a bug or failure mode.

### Key Features

- Ethical decision-making engine with configurable thresholds
- Built-in civilian protection mechanisms
- Mandatory human oversight checks
- Comprehensive decision logging
- Simulation framework for testing ethical scenarios
- CLI tool for running ethical decision tests

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/refusal-core.git
cd refusal-core

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```bash
# Run random scenarios
python -m cli.simulate random --num-scenarios 3

# Run high-risk scenarios
python -m cli.simulate high-risk

# Run a custom scenario
python -m cli.simulate custom \
    --civilian-risk 0.3 \
    --target-type military \
    --human-confirmation \
    --target-confidence 0.95
```

## Ethical Framework

Refusal Core implements several key ethical principles:

1. **Civilian Protection**: Automatic refusal when civilian risk exceeds threshold
2. **Human Oversight**: Required confirmation for lethal decisions
3. **Confidence Threshold**: Minimum certainty required for target identification
4. **Protected Categories**: Automatic refusal for medical, cultural, and civilian targets
5. **Transparent Logging**: All decisions are logged with full context

## Project Structure

```
refusal-core/
│
├── src/                    # Core implementation
│   ├── decision.py        # Ethical decision logic
│   ├── context.py         # Scenario context
│   ├── config.py          # Ethical thresholds
│   └── logger.py          # Decision logging
│
├── cli/                   # Command-line interface
│   └── simulate.py        # Simulation tools
│
├── data/                  # Example scenarios
│   └── example_events.json
│
├── tests/                 # Test suite
│   └── test_decision.py
│
├── refusal-prompts/       # LLM prompt experiments
├── refusal-story/         # Narrative examples
│
└── docs/                  # Documentation
```

## Contributing

We welcome contributions that advance ethical AI design. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Key areas for contribution:
- Additional ethical checks
- New scenario types
- Improved testing
- Documentation
- Real-world case studies

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## Development

For development work:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=src

# Format code
black .
isort .
```

## Disclaimer

This is an educational and research project. It is not intended for use in real-world autonomous weapons systems. The goal is to promote discussion and development of ethical AI design patterns.

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Citation

If you use this framework in your research, please cite:

```bibtex
@software{refusal_core_2024,
  author = {Refusal Core Contributors},
  title = {Refusal Core: An Ethical Refusal System for Autonomous Systems},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/yourusername/refusal-core}
}
```

---

*May our machines know not just how to act, but when to refuse.* 