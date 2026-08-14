# Steam ID Extractor (Private Use)

Extract SteamID64 (17-digit numbers) from any text, especially from Steam inventory URLs.

## Features

- Works with both `/id/username/inventory` and `/profiles/12345678901234567/inventory` URLs
- Handles fragmented or malformed lines
- Outputs clean list of unique IDs
- No external dependencies
- Private — no license

## Quick Start

1. Put your inventory URLs into `urls.txt` (one per line or all in one line)
2. Run:
   ```bash
   python extract_steamids.py
   ```
3. Get your list in `steamids.txt`

## Example

Input in `urls.txt`:
```
https://steamcommunity.com/profiles/76561199516149257/inventory#570_2_29100785753
https://steamcommunity.com/id/SomeUser/inventory
https://steamcommunity.com/profiles/76561198000000000/inventory
```

Output in `steamids.txt`:
```
76561198000000000
76561199516149257
```

## Requirements

- Python 3.6+

## Notes

- This tool is for private use.
- Not intended for public distribution.
- No license is granted.
