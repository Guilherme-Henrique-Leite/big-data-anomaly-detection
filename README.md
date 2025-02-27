# Shape MLE Challenge

Project to refactor the code to solve the Shape MLE Challenge.

## Current Setup

- Python environment configured with Poetry
- Python version: 3.13
- Key dependencies:
  - scikit-learn 1.6.1
  - Development tools: ruff

## Development Environment

- VS Code devcontainer configured

## Running the code

```
# Open the devcontainer
poetry env activate
source .venv/bin/activate
poetry install
poetry run ruff check .
```