
<div align="center">

# Steam ID Extractor

[![python](https://img.shields.io/badge/python-3.6+-black?style=flat&logo=python&color=18181b)](https://python.org)
[![steam](https://img.shields.io/badge/steam-id64-black?style=flat&logo=steam&color=18181b)](https://steamcommunity.com)
[![status](https://img.shields.io/badge/status-private-black?style=flat&color=18181b)](#)
[![deps](https://img.shields.io/badge/deps-zero-black?style=flat&color=18181b)](#)
[![license](https://img.shields.io/badge/license-none-black?style=flat&color=18181b)](#)

</div>

> ⚡ Extract and deduplicate SteamID64 (17-digit) from any text, especially Steam inventory URLs.

Works with both `/id/username/inventory` and `/profiles/12345678901234567/inventory` formats.
Handles fragmented or malformed lines with zero external dependencies.

## Get started

```bash
python extract_steamids.py
```

> Put your inventory URLs into `urls.txt` (one per line or all in one line) and run the script. A clean list of unique IDs will be saved to `steamids.txt`.

## After extraction

```bash
cat steamids.txt
```

- input file: `urls.txt` (supports mixed formats and broken lines)
- output file: `steamids.txt` (sorted, unique 17-digit IDs)
- no config files required
- no API keys or network access needed

## 🔋 Batteries Included

**👩‍💻 Parser defaults**

- dual format support (`/id/` and `/profiles/`)
- handles fragmented or malformed lines gracefully
- strict 17-digit SteamID64 regex validation (`^7656\d{14}$`)
- O(1) memory footprint via streaming I/O
- deterministic sorted output

**➕ Architecture details**

- pre-compiled regex for minimal loop overhead
- set-based deduplication
- zero external dependencies (stdlib only)
- private use — no telemetry, no license

**🛠 Edge Cases Handled**

- ignores non-Steam 17-digit numbers
- skips broken URLs without crashing
- safely handles empty files or missing input

## Why Steam ID Extractor

Parsing Steam URLs manually is tedious. Regular expressions often fail on malformed lines, and loading huge text files into memory causes OOM errors on low-end VPS.

`Steam ID Extractor` handles this by default. Streaming I/O ensures it runs on a 512MB RAM droplet without swapping. Strict regex ensures you only get valid SteamID64s.

**🦾 Better for automation:** predictable output, zero side effects, easy to chain with `xargs` or bash scripts.

## How it works

```
read urls.txt line by line (streaming)
  → apply compiled SteamID64 regex
  → add matches to hash set (deduplication)
  → sort results
  → write to steamids.txt
```

No full file buffering. Just a small memory footprint and fast execution.

## Example

Input in `urls.txt`:
```text
https://steamcommunity.com/profiles/76561199516149257/inventory#570_2_29100785753
https://steamcommunity.com/id/SomeUser/inventory
broken_line_https://steamcommunity.com/profiles/76561198000000000/inventory
76561199516149257 # duplicate
```

Output in `steamids.txt`:
```text
76561198000000000
76561199516149257
```

> _Need to resolve `/id/username` to actual SteamID64? You will need to implement Steam Web API calls with exponential backoff to avoid HTTP 429 rate limits._

---

📖 Private infrastructure tool. No public distribution intended.

## License

MIT

