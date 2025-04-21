# File2JSON

A versatile Python utility that converts various file formats (Excel, CSV, TSV, etc.) to JSON.

## Features

- Automatic file type detection based on extension or content
- Support for multiple file formats:
  - Excel (.xlsx, .xls, .xlsm, .xlsb, .odf, .ods, .odt)
  - CSV (.csv)
  - TSV (.tsv)
  - JSON (.json)
  - Text (.txt, .text)
- Multiple sheet support for Excel files
- Command-line interface
- Configurable output path

## Project Structure
```
file2json/
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── pyproject.toml
├── file2json/
│   ├── __init__.py
│   ├── __main__.py
│   └── converter.py
└── tests/
    ├── __init__.py
    ├── test_converter.py
    └── test_data/
        ├── sample.csv
        ├── sample.tsv
        ├── sample.xlsx
        └── sample.txt
```

## Installation

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) for virtual environment and package management

### Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/file2json.git
cd file2json
```

Set up a virtual environment and install dependencies:

```bash
# Using Make (recommended)
make setup

# Or manually with uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

## Usage

### Command Line

```bash
# Basic usage
file2json sample.csv

# Specify output file
file2json sample.xlsx -o output.json

# Force file type
file2json ambiguous_file -t csv

# Get help
file2json --help
```

### As a Python Module

```python
from file2json.converter import read_file, convert_to_json

# Read a file
data = read_file('sample.xlsx')

# Convert to JSON string
json_str = convert_to_json(data)

# Or save directly to a file
convert_to_json(data, 'output.json')
```

## Development

Run tests:

```bash
make test
```

Run linting:

```bash
make lint
```

Format code:

```bash
make format
```

## License

MIT License - See LICENSE file for details.