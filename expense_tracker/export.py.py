import csv

def export_to_csv(expenses, filename="izdevumi.csv"):
    """Eksportē izdevumus CSV failā."""
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])

        for exp in expenses:
            writer.writerow([exp["date"], f"{exp['amount']:.2f}", exp["category"], exp["description"]])

    return len(expenses)