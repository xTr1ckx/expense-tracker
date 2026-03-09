from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months
from datetime import date, datetime
from export import export_to_csv

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"]

"""Kolonnu platumi (simbolu skaitā)"""
DATE_W = 11
AMOUNT_W = 8
CATEGORY_W = 19
DESC_W = 22

COL_SPACING = "  "

print("=" * 30)
print("     Izdevumu izsekotājs")
print("=" * 30)

def show_menu():
    """Parāda galveno izvēlni un atgriež lietotāja izvēli."""
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Rediģēt izdevumu")
    print("6) Dzēst izdevumu")
    print("7) Eksportēt CSV")
    print("8) Iziet")

    return input("\nIzvēlies darbību: ")

def choose_category():
    """Ļauj lietotājam izvēlēties kategoriju."""
    print("\nKategorija: ")

    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}) {cat}")

    while True:
        choice = input("Izvēlies kategoriju (1-7): ")

        try:
            index = int(choice)
            if 1 <= index <= len(CATEGORIES):
                return CATEGORIES[index - 1]
        except ValueError:
            pass

        print("Šāda kategorija nepastāv! Izvēlies no 1-7.")

def input_amount():
    """Nolasa un validē summu."""
    while True:
        value = input("Summa (EUR): ")

        try:
            amount = float(value)

            if amount <= 0:
                print("Summai ir jābūt pozitīvai!")
                continue

            if amount > 99999.99:
                print("Summa ir pārāk liela! Maksimālā atļautā summa ir 99999.99 EUR.")
                continue

            return amount
        except ValueError:
            print("Lūdzu ievadīt derīgu skaitli.")

def input_date():
    """Nolasa un validē datumu (YYYY-MM-DD)."""
    today = date.today().isoformat()

    while True:
        value = input(f"Datums (YYYY-MM-DD) [{today}]: ").strip()

        if not value:
            return today
        
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Nepareizs datuma formāts! Pareizs formāts: YYYY-MM-DD.")

def truncate(text, max_len=DESC_W):
    """Saīsina tekstu līdz max_len simbolu skaitam"""
    if len(text) <= max_len:
        return text
    return text[:max_len - 3] + "."

def add_expense(expenses):
    """"Pievieno jaunu izdevumu."""

    date_input = input_date()
    amount = input_amount()
    category = choose_category()
    description = input("Apraksts: ")

    expense = {"date": date_input, "amount": amount, "category": category, "description": description,}

    expenses.append(expense)
    save_expenses(expenses)

    print(f"\n✓ Pievienots: {date_input} | {category} | {amount:.2f} EUR | {description}")

def list_expenses(expenses):
    """Parāda visus izdevumus."""

    expenses = sorted(expenses, key=lambda x: x["date"]) #sakārto izdevumus secīgi pēc datumiem

    if not expenses:
        print("\nNav neviena ieraksta.")
        return
    
    print()
    print(f"{'Datums':<{DATE_W}} | {'Summa':{AMOUNT_W}}     | {'Kategorija':{CATEGORY_W}} | {'Apraksts':{DESC_W}}")
    
    line_width = DATE_W + AMOUNT_W + CATEGORY_W + DESC_W + len(COL_SPACING) * 5
    print("-" * line_width)

    for exp in expenses:
        description = truncate(exp["description"])
        print(f"{exp['date']:<{DATE_W}} | {exp['amount']:>{AMOUNT_W}.2f} EUR | {exp['category']:<{CATEGORY_W}} | {description:<{DESC_W}}")

    total = sum_total(expenses)

    print("-" * line_width)
    print(f"Kopā: {total:.2f} EUR ({len(expenses)} ieraksti)")

def filter_expenses(expenses):
    """Filtrē izdevumus pēc gada un mēneša."""
    months = get_available_months(expenses)

    if not months:
        print("\nNav pieejamu mēnešu.")
        return
    
    print("\nPieejamie mēneši:\n")

    for i, month in enumerate(months, start=1):
        print(f"{i} {month}")

    choice = input("\nIzvēlies mēnesi: ")

    try:
        month = months[int(choice) - 1]
    except:
        print("Nepareiza izvēle.")
        return
    
    filtered = filter_by_month(expenses, month)

    print(f"\n{month} izdevumi:\n")

    for exp in filtered:
        print(f"{exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")

    total = sum_total(filtered)
    print(f"\nKopā: {total:.2f} EUR ({len(filtered)} ieraksti)")

def category_summary(expenses):
    """Grupē summas pa kategorijām."""
    totals = sum_by_category(expenses)

    if not totals:
        print("\nNav ierakstītu izdevumu.") 
        return
    
    print("\nKopsavilkums pa kategorijām:\n")

    for category, total in totals.items():
        print(f"{category}: {total:.2f} EUR")

def edit_expense(expenses):
    """Rediģēt pastāvošo izdevumu."""

    if not expenses:
        print("\nNav ierakstu ko rediģēt.")
        return
    
    print("\nIzdevumi:\n")

    for i, exp in enumerate(sorted(expenses, key=lambda x: x["date"]), start=1):
        print(f"{i}) {exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")

    choice = input("\nKuru ierakstu vēlaties rediģēt? (Lai atceltu darbību, ierakstiet 0): ")

    try:
        index = int(choice)

        if index == 0:
            return
        
        expense = expenses[index - 1]

    except:
        print("Nepareiza izvēle.")
        return

    print("\nKo vēlaties rediģēt?")
    print("1) Datums")
    print("2) Summa")
    print("3) Kategorija")
    print("4) Apraksts")

    field_choice = input("Izvēle: ")

    if field_choice == "1":
        expense["date"] = input_date()

    elif field_choice == "2":
        expense["amount"] = input_amount()

    elif field_choice == "3":
        expense["category"] = choose_category()

    elif field_choice == "4":
        expense["description"] = input("Jauns apraksts: ")

    else:
        print("Nepareiza izvēle. Izvēlaties no 1-4.")
        return

    save_expenses(expenses)

    print("\n✓ Izdevums veiksmīgi atjaunināts.")  

def delete_expense(expenses):
    """Izdēst izdevumu."""
    if not expenses:
        print("\nNav ierakstu ko dzēst.")
        return
    
    print("\nIzdevumi:\n")

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}) {exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")

    choice = input("\nKuru ierakstu vēlaties izdzēst? (Lai atceltu darbību, ierakstiet 0): ")

    try:
        index = int(choice)

        if index == 0:
            return
        
        removed = expenses.pop(index - 1)
        save_expenses(expenses)

        print(f"\n✓ Dzēsts: {removed['date']} | {removed['amount']:.2f} EUR | {removed['category']} | {removed['description']}")

    except:
        print("Lūdzu izvēlaties izdevumu no saraksta.")

def export_expenses(expenses):
    """Eksportē izdevumus CSV failā."""
    if not expenses:
        print("\nNav izdevumu ko eksportēt.")
        return
    
    filename = input("\nFaila nosakums [izdevumi.csv]: ").strip()

    if not filename:
        filename = "izdevumi.csv"

    count = export_to_csv(expenses, filename)

    print(f"\n✓ Eksportēts: {count} ieraksti -> {filename}")

def main():
    """Galvenais programmas cikls."""

    expenses = load_expenses()

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            list_expenses(expenses)

        elif choice == "3":
            filter_expenses(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            edit_expense(expenses)

        elif choice == "6":
            delete_expense(expenses)

        elif choice == "7":
            export_expenses(expenses)

        elif choice == "8":
            print("Uz redzēšanos!")
            break
        else:
            print("Nepareiza izvēle. Izvēlaties no 1-8.")

if __name__ == "__main__":
    main()                    

