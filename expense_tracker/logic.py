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

def calculate_statistics(expenses):
    """Aprēķina statistikas datus."""
    total = sum_total(expenses)

    """Vidējais dienas patēriņš"""
    dates = {exp["date"] for exp in expenses}
    avg_per_day = total / len(dates)

    """Dārgākā kategorija"""
    category_totals = sum_by_category(expenses)
    max_category = max(category_totals, key=category_totals.get)

    """Dienas izmaksas"""
    per_day = {}
    for exp in expenses:
        day = exp["date"]
        per_day[day] = per_day.get(day, 0) + 1

        return{'total': total, 'avg_per_day': round(avg_per_day, 2), 'max_category': max_category, 'category_totals': category_totals, 'per_day': per_day}
    
def search_expenses_logic(expenses, query):
    """Meklē izdevumus pēc apraksta."""
    results = []
    for exp in expenses:
        if query in exp["description"].lower():
            results.append(exp)
    return results
