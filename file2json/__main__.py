#!/usr/bin/env python3
"""
Command-line interface for File2JSON converter.
"""

import sys
import argparse
from pathlib import Path

from file2json.converter import read_file, convert_to_json


def main():
    """Main entry point for the file2json command."""
    parser = argparse.ArgumentParser(
        description='Convert various file formats to JSON'
    )
    parser.add_argument('file_path', help='Path to the input file')
    parser.add_argument(
        '-o', '--output', 
        help='Output JSON file path (defaults to input filename with .json extension)'
    )
    parser.add_argument(
        '-t', '--type', 
        choices=['excel', 'csv', 'tsv', 'json', 'text'],
        help='Force file type instead of auto-detection'
    )
    
    args = parser.parse_args()
    
    try:
        # Read the file
        data = read_file(args.file_path, args.type)
        
        # Set default output path if not specified
        if not args.output:
            input_path = Path(args.file_path)
            args.output = str(input_path.with_suffix('.json'))
        
        # Convert and save
        result = convert_to_json(data, args.output)
        print(result)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())