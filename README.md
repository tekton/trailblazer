# trailblazer
Python URL Shortening

Mostly just because I can and it sounded like fun!

## Requirements

- Python 3.12+
- Redis server

## Installation

### Using pip (recommended)

```bash
pip install .
```

### Development installation

```bash
pip install -e ".[dev]"
```

### Legacy installation (if you still have requirements.txt)

```bash
pip install -r requirements.txt
```

## Usage

### Running the application

```bash
# If installed via pip
trailblazer

# Or run directly
python trailblazer.py
```

### API Examples

Create a shortened URL:
```bash
curl -v "localhost:5000/trail" -X POST -d '{"url":"http://pyroturtle.com"}' -H "Content-Type: application/json"
```

Access a shortened URL:
```bash
curl -v "localhost:5000/u/<blur_hash>"
```

## Configuration

Edit `config.json` to configure Redis connection settings:

```json
{
  "root": "trailblazer",
  "redis": {
    "host": "localhost",
    "port": 6379,
    "db": 0
  }
}
```

## Development

This project uses modern Python packaging with `pyproject.toml`. Development dependencies include:

- pytest for testing
- black for code formatting
- flake8 for linting
- mypy for type checking

Install development dependencies:
```bash
pip install -e ".[dev]"
```
