#Lai izveidotu programmu ar datubāzi, kurā ir divas saistītas tabulas, 
#varat izmantot ārējo atslēgu (FOREIGN KEY), lai definētu saistību starp tām.
#Tālāk ir dots Python programmas piemērs, kurā izmantotas SQLite tabulas `Person`
#un `Auto`, un tās ir savstarpēji saistītas:
import sqlite3

# Savienošanās ar datubāzi (vai jaunas datubāzes izveide, ja tādas nav).
conn = sqlite3.connect('autoservis_DB.db')
cursor = conn.cursor()

# Создание таблицы Person
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Person (
        person_id INTEGER PRIMARY KEY,
        vards TEXT,
        uzvards TEXT,
        phone TEXT
    )
''')

# Tabulas Auto izveide ar svešatslēgu, kas to saista ar tabulu Persona
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Auto (
        v_numurs_id TEXT PRIMARY KEY,
        modelis TEXT,
        marka TEXT,
        person_id INTEGER,
        FOREIGN KEY (person_id) REFERENCES Person(person_id)
    )
''')

# Datu ievietošana tabulā Person
vards = input("Vārds: ")
uzvards = input("Uzvārds: ")
phone = input("Tālrunis: ")

person = (vards, uzvards, phone)

cursor.execute('INSERT INTO Person (vards, uzvards, phone) VALUES (?, ?, ?)',person)

# Datu ievietošana tabulā Auto ar person_id, kas to saista ar tabulu Person
vn = input("Valsts reģistrācijas numurs: ")
mod = input("Modelis: ")
mar = input("Marka: ")
pers = input("Īpašnieka ID: ")

automobils = (vn, mod, mar, pers)

cursor.execute('INSERT INTO Auto (v_numurs_id, modelis, marka, person_id) VALUES (?, ?, ?, ?)', automobils)

# Izmaiņu saglabāšana
conn.commit()

# Abu tabulu izejas datu izvadīšana
cursor.execute('''
    SELECT Person.person_id, Person.vards, Person.uzvards, Auto.modelis, Auto.marka
    FROM Person
    JOIN Auto ON Person.person_id = Auto.person_id WHERE Person.person_id = Person.person_id
''')

print("Person and Auto:")
for row in cursor.fetchall():
  print(row)

# Datu bāzes savienojuma slēgšana
conn.close()

#Šajā piemērā tabulas `Person` un `Auto` ir saistītas ar lauku `person_id`.
#Tabulas `Auto` dati satur ārējo atslēgu `person_id`, kas atsaucas uz tabulas
#`Person` primāro atslēgu. Tas nodrošina saikni starp abām tabulām. 
#Programma izvada datus no abām tabulām, izmantojot operatoru `JOIN`, 
#kas savieno rindas no abām tabulām, kuras atbilst 
#atslēgas atbilstības nosacījumam.