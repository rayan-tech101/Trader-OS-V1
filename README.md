# Trader OS v2

Trader OS v2 is a clean, lightweight trading journal designed for Windows 10+ and built for disciplined traders who want structure, accountability, and measurable performance.

It combines:
- Obsidian-based note journaling
- structured trade logging
- session reviews
- strategy tracking
- psychology and risk checks
- performance metrics such as R, win rate, drawdown, and streaks
- optional Python analytics and reports

## Features

- Trade log with entry, exit, P&L, R multiple, risk, and notes
- Session review notes for market quality and execution quality
- Strategy templates for repeatable systems
- Psychology tracker for emotional state and discipline
- Daily dashboard for quick review
- Optional analytics export and chart generation
- Works as a local markdown vault and as a Python desktop tool

## Recommended stack

- Windows 10 or newer
- Python 3.10+
- Obsidian
- Dataview plugin (recommended)
- Optional: Python packages from `requirements.txt`

## Install

### Python desktop app

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Optional Python analytics

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r Python-Analytics/requirements.txt
python Python-Analytics/analytics.py
```

## Repo layout

```text
Trader-OS-V1/
├── README.md
├── app.py
├── requirements.txt
├── .gitignore
├── .obsidian/
├── Dashboard/
├── Journal/
├── Strategies/
├── Psychology/
├── Templates/
├── Python-Analytics/
├── trader_os/
├── data/
├── tests/
└── LICENSE
```

## Quick start

1. Open the repo in Obsidian as a vault or use the folder as a local trading journal.
2. Use the templates in `Templates/`.
3. Log each trade in `Journal/`.
4. Review your dashboard in `Dashboard/`.
5. Run the desktop app to add trades and inspect summary metrics.

## Example trade note

```md
---
type: trade
date: 2026-10-11
time: 09:42
market: NASDAQ
symbol: NVDA
setup: breakout
strategy: Momentum-Continuation
session: 2026-10-11
trade_id: T-2026-10-11-001
status: closed
---

# Trade Log: NVDA

- Long / Short: Long
- Entry: 126.40
- Exit: 127.15
- Size: 2
- Result: +0.75R
- Net P&L: $150.00
```

## Notes

This project is intentionally lightweight, easy to maintain, and suitable for personal trading review without heavy infrastructure.

## License

MIT
