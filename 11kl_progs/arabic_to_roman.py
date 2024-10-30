#A user selects the type of conversion and types 1 or 2 into the IDLE Shell
answer = input("""Convert:
                  1. Arabic Number to Roman Numeral
                  2. Roman Numeral to Arabic Number
                  Please enter 1 or 2 : """)


if answer == "1":    
    #A user will need to write down an arabic number into the IDLE Shell
    convert = input("Please enter an arabic number between 0 and 3999: ")

elif answer == "2":  
    #A user will need to write down roman numerals into the IDLE Shell
    convert = input("Please enter roman numerals between 0 and 3999: ")

else:     
    #A user need to type either 1 or 2 
    print("Please type 1 or 2 only")


#Creating a function that converts arabic number to roman numerals
def arabictoroman(convert):
    roman_thousands = [" ","M","MM","MMM"]
    roman_hundreds  = [" ","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    roman_tens      = [" ","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    roman_ones      = [" ","I","II","III","IV","V","VI","VII","VIII","IX"]

    output = [] #The roman numerals will be stored here

    #The program runs when the arabic number is between 0 and 4000
    if int(convert) < 4000 and int(convert) > 0:

        thousands = int(int(convert)/1000)            #Finds the digit of thousand's place
        output.append(roman_thousands[(thousands)])   #Adds the corresponding roman numerals into 'output'

        hundreds = int(int(convert)/100 % 10)         #Finds the digit of hundred's place
        output.append(roman_hundreds[(hundreds)])     #Adds the corresponding roman numerals into 'output'

        tens = int(int(convert)/10 % 10)              #Finds the digit of ten's place
        output.append(roman_tens[(tens)])             #Adds the corresponding roman numerals into 'output'

        ones = int(int(convert) % 10)                 #Finds the digit of one's place
        output.append(roman_ones[(ones)])             #Adds the corresponding roman numerals into 'output'

    #Joining all roman numerals in the 'output' list and store it in 'whole'
    output = [str(i) for i in output]
    whole = str(''.join(output))
    return whole


#Creating a function that converts roman numerals to arabic number
def romantoarabic(convert):

    subtract = []     #The numbers to be subtracted are stored here
    new_output = []   #Finalized list of numbers

    #A dictionary with roman numerals corresponding to arabic numbers
    arabic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    output = list(convert)  #Converts the roman numerals entered into a list
    n = len(str(convert))   #Calculates the number of letters entered

    #Taking two letters each time to compare the values
    for i in range(n-1):
        first = str(convert[i])          #First letter taken is converted into a corresponding number
        first_key = int(arabic[first])
        second = str(convert[i+1])       #Second letter taken is converted into a corresponding number
        second_key = int(arabic[second])
        
        #If the first number is smaller than the second number
        #then the negative of the first is added to 'subtract' list and removed from the 'output' list
        if first_key < second_key : 
            first_key = -first_key
            subtract.append(first_key)
            output.remove(first)
            
    #For the remaining elements in the 'output' list, find the corresponding arabic number from 'arabic' dictionary
    for i in range(len(output)):
        k = output[i]
        for roman, numbers in arabic.items():
            if str(k) == roman:
                new_k = int(numbers)
        new_output.append(new_k)    #The arabic number is added to the 'new_output' list 

    sum_of_output = sum(new_output)            #Takes the sum of the 'new_output' list
    sum_of_subtract = sum(subtract)            #Takes the sum of the 'subtract' list
    arabics = sum_of_output + sum_of_subtract  #Takes the sum of the above 2 lists 

    return arabics #Returns the final answer 


#If the user want to convert arabic numbers to roman numerals, return roman numerals 
if answer == "1":
    print("It is " + str(arabictoroman(convert)))

#If the user want to convert roman numerals to arabic numbers, return arabic numbers
elif answer == "2":
    print("It is " + str(romantoarabic(convert)))