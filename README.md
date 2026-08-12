# Steam ID Extractor

Extract SteamID64 from a list of URLs (e.g. `inventory` pages).

## Features

- Extracts all SteamID64 (17-digit) from any text.
- Handles both user URLs (`/id/.../inventory`) and profile URLs (`/profiles/.../inventory`).
- Returns unique IDs only.
- Simple CLI, no external dependencies.

## Installation

No installation required. Requires Python 3.6+.

```bash
# Clone or download the script
git clone <repo-url>
cd extract_steam_ids
```

## Usage

### From a file

```bash
python extract_steam_ids.py < urls.txt
```

### From stdin

```bash
cat urls.txt | python extract_steam_ids.py
```

### From a string (Python)

```python
from extract_steam_ids import extract_steam_ids_from_text

text = """
https://steamcommunity.com/id/ExampleUser/inventory
https://steamcommunity.com/profiles/76561198000000000/inventory
https://steamcommunity.com/id/AnotherUser/inventory
"""

steam_ids = extract_steam_ids_from_text(text)
print("\n".join(sorted(steam_ids)))
```

## Output format

One SteamID64 per line, sorted ascending:

```
76561198000000000
76561198111111111
76561198922222222
```

