'''
Kā ar programmēšanas palīdzību risināt problēmas?
Sasniedzamais rezultāts: Izstrādāju vienkāršu programmatūru 
atbilstoši programmatūras prasību specifikācijai un uzdevumam.
2. uzdevums. Lasi, analizē, raksti programmu, kas risina problēmu!
Lasi un analizē doto problēmas aprakstu un specifikāciju! Atbildi uz jautājumiem!

>Vai specifikācijā ir minēts viss, kas nepieciešams, lai uzrakstītu programmu, kas to realizē?
>Kāda papildu informācija nepieciešama?
>Kādus jautājumus varētu uzdot, lai nepieciešamo informāciju iegūtu?
'''

#Uzdod skolotājam jautājumus, lai noskaidrotu nepieciešamās detaļas, un uzprogrammē risinājumu!

#Kreklu apdruka
#Problēma
'''
Draugiem jāaprēķina, cik izmaksās apdrukātu T-kreklu pasūtīšana 
un piegāde, ņemot vērā, ka cena ir atkarīga no apdrukas veida un kreklu skaita, 
bet piegādes maksa ir atkarīga no pasūtījuma summas.
'''
#Specifikācija

'''
>Funkcijai pasuti_tkreklus ir trīs parametri saskaņā ar formātu 
pasuti_tkreklus(skaits, apdruka, piegade). 
Parametrs skaits ir vesels skaitlis (pasūtamo kreklu skaits), 
parametri apdruka un piegade ir simbolu virknes.
>Parametrs apdruka var būt simbolu virkne, kam atļautas trīs vērtības: 
TEKSTS, ZIME vai FOTO. Cena attiecīgi ir 5 EUR, 7 EUR un 20 EUR.
>Parametrs piegade ir Būla tipa mainīgais (True vai False). 
Ja piegade ir True un kopējā pasūtījuma summa ir mazāka nekā 50 EUR, 
par piegādi papildus jāmaksā 15 EUR, ja summa ir 50 EUR vai vairāk, tad piegāde ir par brīvu.
>Pasūtījumiem, kas pārsniedz 100 EUR, tiek piemērota 5 % atlaide no pasūtījuma summas
'''

