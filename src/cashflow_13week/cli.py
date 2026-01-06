from __future__ import annotations

from pathlib import Path
import pandas as pd
import typer
from rich import print

app = typer.Typer(add_completion=False)

@app.command()
def hello():
    """Sanity check: confirm CLI is installed and runnable."""
    print("[bold green]cashflow-13week is installed and ready.[/bold green]")

@app.command()
def run(
    week_start: str = typer.Option(..., help="Week 1 start date (YYYY-MM-DD). Example: 2026-01-06"),
    raw_dir: Path = typer.Option(Path("data/raw"), help="Input folder"),
    out_dir: Path = typer.Option(Path("data/curated"), help="Output folder"),
):
    """
    Placeholder. Next steps will load raw cashflow inputs and generate a 13-week forecast.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    # tiny proof-of-life artifact so we know the pipeline writes somewhere
    df = pd.DataFrame([{"week_start": week_start, "message": "placeholder"}])
    out = out_dir / "forecast_placeholder.csv"
    df.to_csv(out, index=False)
    print(f"[bold]Wrote:[/bold] {out}")

if __name__ == "__main__":
    app()
