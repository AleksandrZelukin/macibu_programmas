def valid(input):
    input = input[::-1]
    
    input = [int(x) for x in input]
    
    for i in range(1, len(input), 2):
        input[i] *= 2

        if input[i] > 9 :
            input[i] = input[i] % 10 + 1
            
    kopa = sum(input)
    
    return kopa % 10 == 0

print(valid("3804382672939623"))

