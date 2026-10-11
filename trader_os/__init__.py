import json
from pathlib import Path
from tkinter import ttk, Tk, StringVar, messagebox

from trader_os.analytics import calculate_summary
from trader_os.journal import load_trades, save_trade


class TraderOSApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Trader OS v2")
        self.geometry("820x520")
        self.minsize(760, 480)
        self.configure(bg="#101820")

        self.data_path = Path("data/trades.json")
        self.data_path.parent.mkdir(exist_ok=True, parents=True)

        self.symbol_var = StringVar(value="NVDA")
        self.side_var = StringVar(value="Long")
        self.result_r_var = StringVar(value="0.75")
        self.pnl_var = StringVar(value="150")
        self.setup_var = StringVar(value="Breakout")
        self.strategy_var = StringVar(value="Momentum-Continuation")
        self.notes_var = StringVar(value="Clean continuation trade")

        self._build_ui()
        self.refresh_summary()

    def _build_ui(self):
        main = ttk.Frame(self, padding=16)
        main.pack(fill="both", expand=True)

        left = ttk.Frame(main)
        left.pack(side="left", fill="y", padx=(0, 16))

        ttk.Label(left, text="Symbol").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(left, textvariable=self.symbol_var).grid(row=0, column=1, padx=6, pady=4)

        ttk.Label(left, text="Side").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Combobox(left, textvariable=self.side_var, values=["Long", "Short"], state="readonly").grid(row=1, column=1, padx=6, pady=4)

        ttk.Label(left, text="R Result").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Entry(left, textvariable=self.result_r_var).grid(row=2, column=1, padx=6, pady=4)

        ttk.Label(left, text="P&L").grid(row=3, column=0, sticky="w", pady=4)
        ttk.Entry(left, textvariable=self.pnl_var).grid(row=3, column=1, padx=6, pady=4)

        ttk.Label(left, text="Setup").grid(row=4, column=0, sticky="w", pady=4)
        ttk.Entry(left, textvariable=self.setup_var).grid(row=4, column=1, padx=6, pady=4)

        ttk.Label(left, text="Strategy").grid(row=5, column=0, sticky="w", pady=4)
        ttk.Entry(left, textvariable=self.strategy_var).grid(row=5, column=1, padx=6, pady=4)

        ttk.Label(left, text="Notes").grid(row=6, column=0, sticky="w", pady=4)
        ttk.Entry(left, textvariable=self.notes_var, width=28).grid(row=6, column=1, padx=6, pady=4)

        ttk.Button(left, text="Add Trade", command=self.add_trade).grid(row=7, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        right = ttk.Frame(main)
        right.pack(side="right", fill="both", expand=True)

        ttk.Label(right, text="Performance Summary", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 8))

        self.summary_labels = {
            "net_r": ttk.Label(right, text="Net R: 0.00"),
            "avg_r": ttk.Label(right, text="Avg R: 0.00"),
            "win_rate": ttk.Label(right, text="Win Rate: 0.00%"),
            "trades": ttk.Label(right, text="Trades: 0"),
            "wins": ttk.Label(right, text="Wins: 0"),
            "losses": ttk.Label(right, text="Losses: 0"),
        }

        for widget in self.summary_labels.values():
            widget.pack(anchor="w", pady=2)

    def refresh_summary(self):
        trades = load_trades(self.data_path)
        summary = calculate_summary(trades)
        self.summary_labels["net_r"]["text"] = f"Net R: {summary['net_r']:.2f}"
        self.summary_labels["avg_r"]["text"] = f"Avg R: {summary['avg_r']:.2f}"
        self.summary_labels["win_rate"]["text"] = f"Win Rate: {summary['win_rate']:.2f}%"
        self.summary_labels["trades"]["text"] = f"Trades: {summary['total']}"
        self.summary_labels["wins"]["text"] = f"Wins: {summary['wins']}"
        self.summary_labels["losses"]["text"] = f"Losses: {summary['losses']}"

    def add_trade(self):
        trade = {
            "symbol": self.symbol_var.get().strip(),
            "side": self.side_var.get(),
            "result_r": float(self.result_r_var.get()),
            "pnl": float(self.pnl_var.get()),
            "setup": self.setup_var.get().strip(),
            "strategy": self.strategy_var.get().strip(),
            "notes": self.notes_var.get().strip(),
        }
        if not trade["symbol"]:
            messagebox.showerror("Validation Error", "Symbol cannot be empty.")
            return

        save_trade(self.data_path, trade)
        self.refresh_summary()
        messagebox.showinfo("Trade Added", f"{trade['symbol']} saved successfully.")


if __name__ == "__main__":
    app = TraderOSApp()
    app.mainloop()
