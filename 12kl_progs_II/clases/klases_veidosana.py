'''
Saliec pareizi klases “Laiks" kodu, ar atribūtiem stundas, minutes, sekundes. 
Konstruktorā inicializē atribūtu sākumvērtības. 
Laiku uzrādi stundas:minūtes:sekundes, piemēram, 01:01:01. 
_______
Ja laika izveides metodē nepadod argumentus, tas sākumvērtības pēc noklusējuma uzstāda uz 0, 
piemēram, 00:00:00, ja nepadod ne stundas, ne minūtes, ne sekundes.
________

Uzliec, lai, ja laiku ievada ar vienu ciparu, 
to pārveido par virkni ar 0 priekšā izmantojot funkciju 
zfill("cik nulles pielikt brīvajās vietās, bet, ja ir skaitlis minētajos desmitos, 
nulli nelikt"). Piemēram, zfill(2) -> skatās, ja dots skaitlis 1 -> 01, ja dots 0 -> 00, 
ja dots 10, nekas nemainās, jo nav brīvās vietas divos desmitos.
_________
Jārealizē sekojošas metodes (tādā pašā secībā kā zemāk minēts): 

1. Konstruktors #konstruktors ar parametru stundas, minutes, sekundes
2. uzstadit_laiku (stundas, minutes, sekundes)  #nomaina laiku uz jaunu laiku
3. izvadit_laiku () #izvada laiku
4. nakama_stunda () #pievieno laikam vienu stundu

Rezultātā redz:

Laiks ir:  23 : 30 : 49
Laiks ir:  00 : 30 : 49
Laiks ir:  03 : 03 : 03

Pirmo laiku, uzstāda veidojot objektu, 
otro laiku iegūst nomainot uz nākamo stundu, 
trešo laiku iegūst liekot vērtības stundas ir 3, minutes ir 3, sekundes ir 3.

'''
# Veido klasi, sakārtojot zemāk dotās daļas pareizā secībā!

class Laiks:
    def __init__(self, stundas=0, minutes=0, sekundes=0):
        self.stundas = stundas
        self.minutes = minutes
        self.sekundes = sekundes


        #pieliek nulles cipara prieksa,
        #ja laiks ir aprakstits tikai ar vienu ciparu
        if(stundas>=0 and stundas <=9):
            self.stundas = str(stundas).zfill(2)
        if(minutes>=0 and minutes <=9):
            self.minutes = str(minutes).zfill(2)
        if(sekundes>=0 and sekundes <=9):
            self.sekundes = str(sekundes).zfill(2)

    def uzstadit_laiku(self, stundas, minutes, sekundes):
        self.stundas = stundas
        self.minutes = minutes
        self.sekundes = sekundes

        #pieliek nulles cipara prieksa,
        #ja laiks ir aprakstits tikai ar vienu ciparu
        if(stundas>=0 and stundas <=9):
            self.stundas = str(stundas).zfill(2)
        if(minutes>=0 and minutes <=9):
            self.minutes = str(minutes).zfill(2)
        if(sekundes>=0 and sekundes <=9):
            self.sekundes = str(sekundes).zfill(2)


    def izvadi_laiku(self):
        print("Laiks ir: ", self.stundas, ":", self.minutes, ":", self.sekundes)


    def nakama_stunda(self):
        if(self.stundas == 23):
            self.stundas = 0
            self.stundas = str(self.stundas).zfill(2)
        else:
            self.stunda = self.stunda + 1


laiks1 = Laiks(23, 30, 49)
laiks1.izvadi_laiku()

laiks1.nakama_stunda()
laiks1.izvadi_laiku()

laiks1.uzstadit_laiku(3, 3, 3)
laiks1.izvadi_laiku()
    

        