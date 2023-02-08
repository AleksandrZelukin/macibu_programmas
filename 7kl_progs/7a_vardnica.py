phonebook = {}

# # def book(vards,tlr_num):
#     vards = input("Vārds: ")
#     tlr_num = input("Tālrunis: ")
#     phonebook[vards]=tlr_num
#     print(phonebook)

while True:
    vards = input("Vārds: ")
    tlr_num = input("Tālrunis: ")
    phonebook[vards]=tlr_num
    if vards == 'none' and tlr_num == 'none':
        break
    print(phonebook)

