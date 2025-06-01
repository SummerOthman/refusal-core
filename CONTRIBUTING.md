# Contributing to Refusal Core

Thank you for your interest in contributing to Refusal Core. This project exists to explore and implement ethical decision-making in autonomous systems, with a focus on the power to refuse harmful actions.

## Ethical Principles

Before contributing, please consider our core ethical principles:

1. **Human Oversight**: All lethal decisions must require explicit human confirmation
2. **Civilian Protection**: Civilian safety is paramount and non-negotiable
3. **Transparency**: Decision-making logic must be clear and auditable
4. **Precautionary Principle**: When in doubt, refuse action
5. **Ethical Design**: Technical solutions must serve humanitarian values

## Technical Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and returns
- Write clear docstrings for all modules, classes, and functions
- Keep functions focused and single-purpose
- Use meaningful variable names that reflect ethical context

### Testing

- Write tests for all new functionality
- Include both technical and ethical edge cases
- Document test scenarios clearly
- Maintain or improve test coverage

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Update documentation as needed
6. Commit with clear, descriptive messages
7. Push to your fork
8. Submit a Pull Request

### Commit Messages

Format:
```
type(scope): Brief description

Detailed description of changes and reasoning
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `ethics`: Changes to ethical logic

## Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Reporting Issues

- Use the GitHub issue tracker
- Include clear reproduction steps
- Specify your environment details
- For ethical concerns, label with "ethics"
- For security issues, please email maintainers directly

## Ethical Considerations

When contributing new features or modifications:

1. Consider the ethical implications
2. Document your ethical reasoning
3. Include safeguards against misuse
4. Think about edge cases that could cause harm
5. Consider international humanitarian law
6. Add appropriate logging and transparency

## Questions or Concerns?

- For technical questions: Open an issue
- For ethical discussions: Use discussions tab
- For security concerns: Contact maintainers directly

Remember: This project's goal is to prevent harm through ethical system design. All contributions should align with this mission. 