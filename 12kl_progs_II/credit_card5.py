#A.Zelukin


from string import digits
card=input("card number= ")
card_lenght = len(list(card))
card_digits = int(str(card)[:2])

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

if luhn_checksum(card)==0:
    if card_lenght==15 and card_digits == 37 or card_digits == 34:
        print("AMEX")
    if card_lenght==16:
        if str(card_digits)[:1] == "4":
            print("VISA")
        if card_digits > 50 and card_digits < 56:
            print("MASTERCARD")
    if card_lenght==13 and str(card_digits)[:1] == "4":
        print("VISA")
else:
    print("NOT VALID CARD")

