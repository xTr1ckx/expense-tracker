def sum_total(expenses):
    """Aprēķina kopējo izdevumu summu."""
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return round(total, 2)

def filter_by_month(expenses, year_month):
    """Filtrē izdevumus pēc gada un mēneša."""
    filtered = []

    for expense in expenses:
        if expense["date"].startswith(year_month):
            filtered.append(expense)

    return filtered

def sum_by_category(expenses):
    """Grupē summas pa kategorijām."""
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    return totals

def get_available_months(expenses):
    """Atgriež mēnešus ar izdevumiem."""
    months = set()

    for expense in expenses:
        months.add(expense["date"][:7])

    return sorted(months)