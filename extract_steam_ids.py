#!/usr/bin/env python3
"""
Steam ID Extractor

Extracts SteamID64 (17-digit) from any text containing inventory URLs.

Example:
    python extract_steam_ids.py < urls.txt
    
"""

import re
import sys
from typing import Set

# SteamID64: 17 digits
STEAM_ID_PATTERN = re.compile(r'\d{17}')


def extract_steam_ids_from_text(text: str) -> Set[str]:
    """
    Extracts unique SteamID64 from arbitrary text.
    Returns a set of Steam IDs (strings).
    """
    steam_ids = set()
    for match in STEAM_ID_PATTERN.finditer(text):
        steam_id = match.group()
        steam_ids.add(steam_id)
    return steam_ids


def read_text_from_file(filepath: str) -> str:
    """Reads file contents and returns as string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    if len(sys.argv) > 1:
        # Read from provided file
        input_path = sys.argv[1]
        text = read_text_from_file(input_path)
    else:
        # Read from stdin (e.g. cat urls.txt | python extract_steam_ids.py)
        text = sys.stdin.read()

    steam_ids = extract_steam_ids_from_text(text)

    # Print unique IDs, sorted for consistency
    for steam_id in sorted(steam_ids):
        print(steam_id)


if __name__ == '__main__':
    main()