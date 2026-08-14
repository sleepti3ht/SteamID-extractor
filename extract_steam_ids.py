#!/usr/bin/env python3
"""
Steam ID Extractor (private use)

Extracts SteamID64 (17-digit) from inventory URLs.

Auto mode:
   Place URLs in urls.txt → run script → get steamids.txt
Manual mode:
   cat urls.txt | python extract_steam_ids.py

Public domain (no license).
"""

import re
import os
import sys
from typing import Set

# Match exactly 17 digits (SteamID64)
STEAM_ID_PATTERN = re.compile(r'\d{17}')


def extract_steam_ids_from_text(text: str) -> Set[str]:
    """
    Extracts unique SteamID64 from arbitrary text.
    Returns a set of Steam IDs (strings).
    """
    return set(STEAM_ID_PATTERN.findall(text))
def read_text_from_file(filepath: str) -> str:
    """Reads file contents and returns as string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    input_file = 'urls.txt'
    output_file = 'steamids.txt'

    if os.path.exists(input_file):
        print(f"[.] Reading from {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        ids = extract_steam_ids_from_text(content)

        if ids:
            with open(output_file, 'w') as f:
                for steam_id in sorted(ids):
                    f.write(steam_id + '\n')
            print(f"[+] Saved {len(ids)} unique IDs to {output_file}")
        else:
            print("[-] No SteamID64 found in input.")

    elif not sys.stdin.isatty():
        content = sys.stdin.read()
        ids = extract_steam_ids_from_text(content)
        for steam_id in sorted(ids):
            print(steam_id)
    else:
        print("Usage:")
        print(f"   Place links in {input_file} and run this script")
        print("   Or pipe data: cat urls.txt | python extract_steam_ids.py")


if __name__ == '__main__':
    main()
