# Migration to Python 3.12+ and pyproject.toml

This project has been updated to use modern Python packaging standards and requires Python 3.12 or later.

## What Changed

1. **Python Version**: Now requires Python 3.12+ (previously no specific requirement)
2. **Packaging**: Moved from `requirements.txt` to `pyproject.toml`
3. **Dependencies**: Updated all dependencies to their latest compatible versions
4. **Installation**: Now supports proper pip installation with `pip install .`

## Migration Steps

### If you were using requirements.txt:

1. **Update Python**: Ensure you have Python 3.12 or later
   ```bash
   python3 --version  # Should show 3.12.0 or higher
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install using the new method**:
   ```bash
   pip install .
   ```

4. **For development**:
   ```bash
   pip install -e ".[dev]"
   ```

### Legacy Support

If you need to continue using `requirements.txt` for some reason, it's still present in the repository, but we recommend migrating to the new pyproject.toml approach.

## New Features

- **Entry point script**: You can now run `trailblazer` directly after installation
- **Development tools**: Includes pytest, black, flake8, and mypy for development
- **Modern packaging**: Follows PEP 621 standards for Python packaging

## Dependency Updates

| Package | Old Version | New Version |
|---------|-------------|-------------|
| click | 7.1.2 | ≥8.1.7 |
| Flask | 1.1.2 | ≥3.0.0 |
| gunicorn | 20.0.4 | ≥21.2.0 |
| itsdangerous | 1.1.0 | ≥2.1.2 |
| Jinja2 | 2.11.3 | ≥3.1.2 |
| MarkupSafe | 1.1.1 | ≥2.1.3 |
| redis | 3.5.3 | ≥5.0.1 |
| Werkzeug | 1.0.1 | ≥3.0.1 |

All dependencies have been updated to their latest stable versions that are compatible with Python 3.12+.
