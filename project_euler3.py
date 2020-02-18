input_number = 600851475143

divisor = 2
list_numbers = []
while input_number != 1:
    if input_number % divisor == 0:
        list_numbers.append(divisor)
        input_number = input_number / divisor
        divisor += 1
    else:
        divisor += 1

print(list_numbers)
