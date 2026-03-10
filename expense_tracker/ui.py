from datetime import date, datetime

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"]

"""Kolonnu platumi (simbolu skaitā)"""
DATE_W = 11
AMOUNT_W = 8
CATEGORY_W = 19
DESC_W = 22

def show_menu():
    """Parāda galveno izvēlni un atgriež lietotāja izvēli."""
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Statistika")
    print("6) Meklēšana")
    print("7) Rediģēt izdevumu")
    print("8) Dzēst izdevumu")
    print("9) Eksportēt CSV")
    print("10) Iziet")

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

def show_header():
    """Programmas nosaukums"""
    print("=" * 30)
    print("     Izdevumu izsekotājs")
    print("=" * 30)

def list_expenses_display(expenses, total):
    """Parāda visus izdevumus."""

    expenses = sorted(expenses, key=lambda x: x["date"]) #sakārto izdevumus secīgi pēc datumiem

    if not expenses:
        print("\nNav neviena ieraksta.")
        return
    
    print()
    print(f"{'Datums':<{DATE_W}} | {'Summa':{AMOUNT_W}}     | {'Kategorija':{CATEGORY_W}} | {'Apraksts':{DESC_W}}")
    print("-" * 70)

    for exp in expenses:
        description = truncate(exp["description"])
        print(f"{exp['date']:<{DATE_W}} | {exp['amount']:>{AMOUNT_W}.2f} EUR | {exp['category']:<{CATEGORY_W}} | {description:<{DESC_W}}")
    print("-" * 70)
    print(f"Kopā: {total:.2f} EUR ({len(expenses)} ieraksti)")

def show_available_months(months):
    """Parāda pieejamos mēnešus."""
    print("\nPieejamie mēneši:\n")
    for i, month in enumerate(months, start=1):
        print(f"{i} {month}")

def show_filtered_expenses(filtered, month, total):
    """Parāda filtrētos izdevumus"""
    print(f"\n{month} izdevumi:\n")

    for exp in filtered:
        print(f"{exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")
    print(f"\nKopā: {total:.2f} EUR ({len(filtered)} ieraksti)")

def show_category_summary(totals):
    """Parāda kopsavilkumu pa kategorijām."""
    if not totals:
        print("\nNav ierakstītu izdevumu.") 
        return
    
    print("\nKopsavilkums pa kategorijām:\n")
    for category, total in totals.items():
        print(f"{category}: {total:.2f} EUR")

def show_statistics_ui(total, avg_per_day, max_category, category_totals, per_day):
    """Parāda statistiku par izdevumiem."""
    print("\nStatistika:\n")
    print(f"Kopējie izdevumi: {total:.2f} EUR")
    print(f"Vidēji dienā: {avg_per_day:.2f} EUR")
    print(f"Dārgākā kategorija: {max_category} ({category_totals[max_category]:.2f} EUR)")

    print("\nIzdevumu skaits pa dienām:")
    for day, count in sorted(per_day.items()):
        print(f"{day}: {count}")

def show_search_results(results):
    """Meklē izdevumus pēc apraksta"""
    print(f"\nAtrasti {len(results)} rezultāti:\n")
    for exp in results:
        print(f"{exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")

if __name__ == "__main__":
    show_header()
    print(choose_category())
    print(input_amount())
    print(input_date())
