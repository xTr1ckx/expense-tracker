from storage import load_expenses, save_expenses
from logic import sum_total
from datetime import date, datetime

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"]

# Kolonnu platumi (simbolu skaitā)
DATE_W = 12
AMOUNT_W = 8
CATEGORY_W = 20
DESC_W = 25

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
    return text[:max_len - 3] + "..."

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
    
    print(f"{'Datums':<{DATE_W}}" f"{'Summa':>{AMOUNT_W}}" f"{'Kategorija':<{CATEGORY_W}}" f"{'Apraksts':<{DESC_W}}")
    print("-" * (DATE_W + AMOUNT_W + CATEGORY_W + DESC_W + 10)) #printē noteiktu skaitu domu zīmju

    for exp in expenses:
        description = truncate(exp["description"])
        print(
            f"{exp['date']:<{DATE_W}}  "
            f"{exp['amount']:>{AMOUNT_W}.2f} EUR  " #Python f-string formatēšana. 8 apzīmē simbolu platuma minimumu un 2 nozīmē divi skaitļi pēc komata (kā tiek apzīmētas cenas dzīvajā).
            f"{exp['category']:<{CATEGORY_W}}  " #20 apzīmē simbolu platumu
            f"{description:<{DESC_W}}"
        )

    total = sum_total(expenses)

    print("-" * (DATE_W + AMOUNT_W + CATEGORY_W + DESC_W + 10))
    print(f"Kopā: {total:.2f} EUR ({len(expenses)} ieraksti)")

def main():
    """Galvenais programmas cikls."""

    expenses = load_expenses()

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            list_expenses(expenses)

        #elif choice == "3":

        #elif choice == "4":

        #elif choice == "5":

        #elif choice == "6":

        #elif choice == "7":

        elif choice == "8":
            print("Uz redzēšanos!")
            break
        else:
            print("Nepareiza izvēle. Izvēlaties no 1-8.")

if __name__ == "__main__":
    main()                    

