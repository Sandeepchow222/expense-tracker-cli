# 💸 Expense Tracker CLI

A simple, Python-based CLI tool to track and export personal expenses. Built with [Typer](https://github.com/tiangolo/typer) and fully testable.

---

## 📦 Features

- Add expenses with category and note
- List all saved expenses
- Export all expenses to a CSV report
- Simple CLI interface using Typer
- Easy to extend and test

---

## 🚀 Getting Started

```bash
git clone https://github.com/Sandeepchow222/expense-tracker-cli.git
cd expense-tracker-cli
pip install -r requirements.txt
# Add an expense
python app.py add 100 food --note "Lunch"

# List all expenses
python app.py list-all

# Export to CSV
python app.py export --file report.csv
 Run Tests
bash
Copy
Edit
