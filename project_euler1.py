
def return_sum(num_max):
    aux_list = []
    num = 1
    while num != num_max:
        if (num % 3 == 0) or (num % 5 == 0):
            aux_list.append(num)
        num += 1
    return sum(aux_list)


print('Sum of multiples of 3 and 5 below 1000:', return_sum(1000))
