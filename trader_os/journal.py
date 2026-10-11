import csv
from pathlib import Path
from typing import Iterable, List, Dict, Any


def load_trade_csv(csv_path: str | Path) -> List[Dict[str, Any]]:
    """Load trades from a CSV file."""
    records: List[Dict[str, Any]] = []
    path = Path(csv_path)
    if not path.exists():
        return records

    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                trade = {
                    "symbol": row.get("symbol", ""),
                    "side": row.get("side", "Long"),
                    "result_r": float(row.get("result_r", 0) or 0),
                    "pnl": float(row.get("pnl", 0) or 0),
                    "setup": row.get("setup", ""),
                    "strategy": row.get("strategy", ""),
                    "notes": row.get("notes", ""),
                }
            except (TypeError, ValueError):
                continue
            records.append(trade)
    return records


def calculate_summary(trades: Iterable[Dict[str, Any]]) -> Dict[str, float | int]:
    """Return summary metrics for a set of trades."""
    trade_list = list(trades)
    total = len(trade_list)
    wins = sum(1 for trade in trade_list if float(trade.get("result_r", 0) or 0) > 0)
    losses = sum(1 for trade in trade_list if float(trade.get("result_r", 0) or 0) < 0)
    net_r = sum(float(trade.get("result_r", 0) or 0) for trade in trade_list)
    avg_r = net_r / total if total else 0.0
    win_rate = (wins / total * 100) if total else 0.0

    running = 0.0
    max_drawdown = 0.0
    for trade in trade_list:
        running += float(trade.get("result_r", 0) or 0)
        max_drawdown = min(max_drawdown, running)

    return {
        "total": total,
        "wins": wins,
        "losses": losses,
        "net_r": net_r,
        "avg_r": avg_r,
        "win_rate": win_rate,
        "max_drawdown": abs(max_drawdown) if max_drawdown < 0 else 0.0,
    }


def equity_curve(trades: Iterable[Dict[str, Any]]) -> List[float]:
    """Compute cumulative equity in R terms."""
    running_total = 0.0
    curve: List[float] = []
    for trade in trades:
        running_total += float(trade.get("result_r", 0) or 0)
        curve.append(running_total)
    return curve
