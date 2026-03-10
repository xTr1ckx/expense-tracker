import csv

def export_to_csv(expenses, filename="izdevumi.csv"):
    """
    Eksportē izdevumus CSV failā.
    
    Args:
        expenses: Izdevumu saraksts
        filename: Faila nosaukums 
    
    Returns:
        Izdevumu saraksts    
    """
    if not filename.lower().endswith('.csv'):
        filename += '.csv' #ja fails nebeidzas ar .csv, tad pieliek .csv
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['Datums', 'Summa', 'Kategorija', 'Apraksts']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for expense in expenses:
                writer.writerow({
                    'Datums': expense['date'],
                    'Summa': f"{expense['amount']:.2f}",
                    'Kategorija': expense['category'],
                    'Apraksts': expense['description']
                })
        
        return len(expenses)
    
    except Exception as e:
        print(f"Kļūda eksportējot: {e}")
        return 0

if __name__ == "__main__":
    test_expenses = [
        {"date": "2026-03-10", "amount": 15.50, "category": "Ēdiens", "description": "Pusdienas"},
        {"date": "2026-03-10", "amount": 2.00, "category": "Transports", "description": "Autobuss"}
    ]
    count = export_to_csv(test_expenses, "test")
    print(f"Eksportēts: {count} ieraksti -> test.csv")