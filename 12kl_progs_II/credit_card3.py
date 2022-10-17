#https://allwin-raju-12.medium.com/credit-card-number-validation-using-luhns-algorithm-in-python-c0ed2fac6234
def digits_of(n):
        return [int(d) for d in str(n)]
digits = digits_of("4532015112830366")  #Get the card number as a list of numbers.

odd_digits = digits[-1::-2]
even_digits = digits[-2::-2]  # Get a list of odd and even digits starting from the rightmost or last digit.

checksum = 0
for d in even_digits:
    checksum += sum(digits_of(d*2)) 
    
    # Multiply each value from the even_digits by 2. 
    #If any number is greater than 9, sum its digits to convert it into a single-digit number. 
    #Here we are converting all the numbers to a list of individual digits and summing it up.

checksum += sum(odd_digits) # Sum all the odd numbers along with this checksum.

# If the modulus of the checksum is 0, then the number is valid.

if checksum%90==0:
    print("valid") 
else:
     print("Invalid") 