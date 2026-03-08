Izdevumu izsekotājs

A. Programmas apraksts
	Izdevuma izsekotājs ļauj lietotājam ievadīt savus ikmēneša izdevumus, sadalīt tos pa kategorijām, rādīt atsevišķu izdevumu vai izdevumu grupējuma kopsummas, kā arī eksportētus datus CSV failā, kas ļaus tos apskatīt Excelī. Īsāk 	sakot, tā ir vienkārša grāmatvedības programma, ko var izmantot kā palīgu savā ikdienā.

B. Datu struktūra
	Datums, laiks, summa, kategorija, apraksts

 	Piemērs: 06.03.2026. | 12:23 | 0,90€ | Ēdiens | Jūras kāposti brokastīm

	Šāda struktūra tika izvēlēta, jo līdzīga struktūra bija piedāvāta projekta apraksta failā, kura likās visai sakarīga. Kaut arī pašam būtu vēlme aprakstu izvadīt kā pirmo lietu ko lietotājs redz, pats saprotu, ka tas bojātu 	caurskatāmību visai struktūrai, par cik teksts var būt dažāda garuma, kas nozīmē, ka katrs jauns ieraksts "bīdītu" apkārt visus pārējos datus kas iet pēc apraksta.

C. Moduļu plāns
	app.py - Galvenā programma, kura apkopos citus moduļus un ļaus lietotājam mijiedarboties ar to

 	storage.py - JSON failu operācijas
 	logic.py - Biznesa loģika (filtrēšana, grupēšana, summas)
 	export.py - CSV eksports
 	expenses.json - Saglabās lietotāja ievadītos datus 

 	DEVLOG.md - Programmas izstrādes žurnāls
 	plan.md - Sākotnējais plāns par programmas darbību

 	README.md - Projekta dokumentācija

D. Lietotāja scenāriji

	1. Lietotājs nepareizi ieraksta summu un vēlas to rediģēt - ar speciālu funkciju programma ļauj nomainīt veco cenu uz jauno neizdzēšot pārējos datus par konkrēto izdevumu.
	2. Lietotājs neieraksta izdevuma kategoriju - programma atgriež kļūdu un ļauj lietotājam ievadīt izdevumu vēlreiz.
	3. Lietotājs neizmanto pareizo formātu - programma salīdzina ar pareizo formatējumu un atgriež kļūdu, sakot, ka lietotājs ir izmantojis nepareizu formatējumu un ļauj ievest izdevumu pa jaunam.

E. Robežgadījumi

	- Ja expenses.json neeksistē tad izdevumu saraksts rādīsies tukšs. Ja programmas kods ir pareizi uzrakstīts, tad expenses.json failam ir jāparādās ar pirmo lietotāja ievadīto izdevumu.
	- Ja lietotājs ievada negatīvu summu, tukšu aprakstu vai nepareizu datumu, tad programma atgriež kļūdu, sakot, ka lietotājs ir nepareizi formatējis izdevumu un ļauj ievest izdevumu pa jaunam.
	- Ja saraksts ir tukšs un lietotājs izvēlas "Parādīt", tad programma atgriež paziņojumu, ka saraksts ir tukšs.

