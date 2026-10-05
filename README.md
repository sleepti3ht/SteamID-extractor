
<div align="center">

# Steam id extractor

[![python](https://img.shields.io/badge/python-3.6+-black?style=flat&logo=python&color=18181b)](https://python.org)
[![deps](https://img.shields.io/badge/dependencies-zero-black?style=flat&color=18181b)]()
[![io](https://img.shields.io/badge/io-streaming-black?style=flat&color=18181b)]()
[![status](https://img.shields.io/badge/status-private-black?style=flat&color=18181b)]()

</div>

> ⚡ Extract and deduplicate SteamID64s from raw text and inventory URLs with zero dependencies.

Handles `/id/username` and `/profiles/` formats.
Upstream text dumps build the foundation; `steam-id-extractor` adds strict validation and O(1) memory processing.

## Get started

```bash
python extract_steamids.py
```

> Ensure your raw data is placed in `urls.txt` before execution. Output is automatically written to `steamids.txt`.

## After extraction

```bash
cat steamids.txt
```

- clean output: one 17-digit ID per line
- deduplicated: `set()` ensures zero duplicates
- sorted: deterministic output for easy diffing
- malformed lines ignored silently
- tweak regex patterns in `extract_steamids.py` if custom formats appear

## ⚙️ Engineering Details

**🧠 Core Logic**

- pre-compiled regex (`re.compile`) for minimal overhead
- strict 17-digit validation (`^7656\d{14}$`)
- handles fragmented or broken URL strings

**💾 Memory Management**

- streaming I/O (`for line in file`) instead of `.read()`
- O(1) memory footprint regardless of input file size
- prevents OOM (Out of Memory) crashes on large dumps

**🛡️ Edge Cases**

- ignores false positives (non-Steam 17-digit numbers)
- safely handles missing `urls.txt` with graceful exit
- UTF-8 encoding enforced for cross-platform compatibility

## Why steam-id-extractor

A quick bash grep or naive Python script feels like a toy. Memory spikes, regex compilation overhead, and false positives: chores you hit when scaling data extraction.

`steam-id-extractor` handles them by default and stays close to Python's standard library. No pip installs, no virtual environments, no drift.

**🦾 Better for automation:** predictable standard I/O, built for cron jobs and systemd timers without external wrappers.

## How it works

```text
read urls.txt (stream)
  → compile regex pattern
  → iterate lines (O(1) memory)
  → extract & validate 17-digit IDs
  → deduplicate via hash set
  → write sorted output to steamids.txt
```

No external APIs. Just a small, highly optimized regex surface on top of local file streams.

## ⚠️ Private Use Notice

- This tool is for private infrastructure and local data processing.
- Not intended for public distribution or commercial SaaS.
- No license is granted. Use at your own risk.

---

📖 Need network resolution for `/id/` aliases? Implement exponential backoff and caching to avoid Steam API HTTP 429 rate limits.

