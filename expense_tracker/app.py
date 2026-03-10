from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months, calculate_statistics, search_expenses_logic
from ui import show_menu, choose_category, input_amount, input_date, show_header, list_expenses_display, show_available_months, show_filtered_expenses, show_category_summary, show_statistics_ui, show_search_results, truncate
from datetime import date, datetime
from export import export_to_csv

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
    total = sum_total(expenses)
    list_expenses_display(expenses, total)

def filter_expenses(expenses):
    """Filtrē izdevumus pēc gada un mēneša."""
    months = get_available_months(expenses)

    if not months:
        print("\nNav pieejamu mēnešu.")
        return
    show_available_months(months)
    choice = input("\nIzvēlies mēnesi: ")

    try:
        month = months[int(choice) - 1]
    except:
        print("Nepareiza izvēle.")
        return
    
    filtered = filter_by_month(expenses, month)
    total = sum_total(filtered)
    show_filtered_expenses(filtered, month, total)

def category_summary(expenses):
    """Grupē summas pa kategorijām."""
    totals = sum_by_category(expenses)
    show_category_summary(totals)

def show_statistics(expenses):
    """Parāda statistiku par izdevumiem"""
    if not expenses:
        print("\nNav izdevumu.")
        return
    
    stats = calculate_statistics(expenses)
    show_statistics_ui(**stats)

def search_expenses(expenses):
    """Meklē izdevumus pēc apraksta."""
    if not expenses:
        print("\nNav izdevumu.")
        return
    
    query = input("\nMeklēt: ").lower().strip()
    if not query:
        print("Nav ievadīts teksts.")
        return
    
    results = search_expenses_logic(expenses, query)
    if not results:
        print("\nNekas netika atrasts.")
        return
    
    show_search_results(results)

def edit_expense(expenses):
    """Rediģēt pastāvošo izdevumu."""
    if not expenses:
        print("\nNav ierakstu ko rediģēt.")
        return
    
    print("\nIzdevumi:\n")
    sorted_expenses = sorted(expenses, key=lambda x: x["date"]) #šis kods palīdzēs programmai izvēlēties pareizo izdevumu, kuru lietotājs izvēlās pēc kārtas numura, ne pēc kārtības kurā izdevums tika ievests programmā.

    for i, exp in enumerate(sorted_expenses, start=1):
        print(f"{i}) {exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")

    choice = input("\nKuru ierakstu vēlaties rediģēt? (Lai atceltu darbību, ierakstiet 0): ")

    try:
        index = int(choice)
        if index == 0:
            return
        expense = sorted_expenses[index - 1]
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
    
    filename = input("\nFaila nosaukums [izdevumi.csv]: ").strip()
    if not filename:
        filename = "izdevumi.csv"

    count = export_to_csv(expenses, filename)
    print(f"\n✓ Eksportēts: {count} ieraksti -> {filename}")

def main():
    """Galvenais programmas cikls."""
    show_header()
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
            show_statistics(expenses)
        elif choice == "6":
            search_expenses(expenses)
        elif choice == "7":
            edit_expense(expenses)
        elif choice == "8":
            delete_expense(expenses)
        elif choice == "9":
            export_expenses(expenses)
        elif choice == "10":
            print("Uz redzēšanos!")
            break
        else:
            print("Nepareiza izvēle. Izvēlaties no 1-10.")

if __name__ == "__main__":
    main()                    
