# https://codereview.stackexchange.com/questions/267932/simple-credit-card-validation-with-luhns-algorithm

def main():
    # Prompts user for card number
    nums = int(input("Number: "))
    if len(str(nums)) > 16 or len(str(nums)) < 12:
        print("INVALID")
    else:
        card_classify(card_luhn(nums), nums)

# Luhn's Algorithm
def card_luhn(nums):

    tmp = str(nums)
    digit_sum = 0
        
    # Loops through the digits that needs to be multiplied by 2
    for i in range(2, len(tmp) + 1, 2):
        digits = 2 * int(tmp[-i])

        # Condition if resulting product has 2 digits
        if_sum = 0
        if len(str(digits)) == 2:
            for digit in str(digits):
                if_sum += int(digit)
                digits = 0

        if_sum += digits
        digit_sum += if_sum

    # Loops through the digits that does not need to be multiplied by 2
    for i in range(1, len(tmp) + 1, 2):
        digits = int(tmp[-i])
        digit_sum += digits

    if digit_sum % 10 == 0:
        return 0
    else:
        return 1


# Classifies the card whether AMEX, VISA, or MASTERCARD
def card_classify(check, nums):

    num = int(str(nums)[:2])

    if check != 0:
        print("INVALID")

    # AMEX condition (first two digits from left are either 37 or 34)
    elif num == 37 or num == 34:
        print("AMEX")

    # VISA condition (first digit from left is 4)
    elif str(num)[:1] == "4":
        print("VISA")

    # MASTERCARD condition (first two digits from left are between 50 and 56)
    elif num > 50 and num < 56:
        print("MASTERCARD")

    else:
        print("INVALID")

if __name__ == "__main__":
    main()