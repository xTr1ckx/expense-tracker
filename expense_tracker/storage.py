import json
import os

EXPENSES_FILE = "expenses.json"

def load_expenses():
    """Nolasa expenses.json failu. Ja fails neeksistē, atgriež [], kas pasaka programmai, ka saraksts pašalik ir tukšs"""
    if not os.path.exists(EXPENSES_FILE):
        return []
    
    with open(EXPENSES_FILE, "r", encoding="utf-8-sig") as f:
        return json.load(f)
    
def save_expenses(expenses):
    """Saglabā izdevumu sarakstu JSON failā."""
    with open(EXPENSES_FILE, "w", encoding="utf-8-sig") as f:
        json.dump(expenses, f, indent=2, ensure_ascii=False)