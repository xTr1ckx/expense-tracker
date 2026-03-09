# Izdevumu izsekotājs

Šī ir vienkārša komandrindas Python programma personīgo izdevumu uzskaitei.
Lietotājs var pievienot, apskatīt, filtrēt, rediģēt un analizēt savus izdevumus.
Programma arī ļauj eksportēt datus CSV failā.

## Uzstādīšana

git clone https://github.com/xTr1ckx/final-project.git
cd expense_tracker
python app.py

Nav nepieciešamas papildus bibliotēkas - tikai Python 3.10+

## Lietošana

Programma darbojās interaktīvā režīmā ar izvēlni:

1) Pievienot izdevumu                   - Ļauj lietotājam pievienot jaunu izdevumu. Izdevuma struktūra - Datums, Summa, Kategorija, Apraksts
2) Parādīt izdevumus                    - Parāda visus ievadītos izdevumus
3) Filtrēt pēc mēneša                   - Ļauj lietotājam ērti skatīt izdevumus pēc gada un mēneša
4) Kopsavilkums pa kategorijām          - Parāda kopējo cenu summu pa kategorijām
5) Statistika                           - Parāda vidējo izdevumu dienā, dārgāko kategoriju un izdevumu skaitu pa dienām
6) Meklēšana                            - Meklē izdevumus pēc apraksta
5) Rediģēt izdevumu                     - Ļauj lietotājam rediģēt jebkuru elementu jebkuram izdevumam, bez nepieciešamības dzēst to ārā
6) Dzēst izdevumu                       - Izdzēš jebkuru izdevumu no saraksta
7) Eksportēt CSV                        - Eksportē visu izdevumus CSV failā
8) Iziet                                - Apstādina programmu

Visi ievadītie dati tiks saglabāti expenses.json failā, kurš tiks automātiski izveidots ievadot pirmos izdevuma datus programmā.

## Autors

Edgars Slīpais - Programmēšanas pamati un algoritmizācija, 2026