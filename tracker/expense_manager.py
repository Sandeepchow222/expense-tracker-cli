import json
from datetime import datetime
import os

class ExpenseManager:
    def __init__(self, filepath):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump([], f)

    def add_expense(self, amount, category, note=""):
        new_expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().isoformat()
        }
        with open(self.filepath, 'r+') as f:
            data = json.load(f)
            data.append(new_expense)
            f.seek(0)
            json.dump(data, f, indent=2)

    def get_expenses(self):
        with open(self.filepath, 'r') as f:
            return json.load(f)
