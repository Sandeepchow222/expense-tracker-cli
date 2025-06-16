import typer
import csv
from tracker.expense_manager import ExpenseManager

app = typer.Typer()
manager = ExpenseManager("data/expenses.json")

@app.command()
def add(amount: float, category: str, note: str = ""):
    """Add a new expense."""
    manager.add_expense(amount, category, note)
    typer.echo("✅ Expense added!")

@app.command()
def list_all():
    """List all saved expenses."""
    expenses = manager.get_expenses()
    for e in expenses:
        typer.echo(e)

@app.command()
def export(file: str = "report.csv"):
    """Export all expenses to a CSV file."""
    expenses = manager.get_expenses()
    with open(file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "category", "note", "date"])
        writer.writeheader()
        for row in expenses:
            writer.writerow(row)
    typer.echo(f"✅ Exported {len(expenses)} expenses to {file}")

if __name__ == "__main__":
    app()
