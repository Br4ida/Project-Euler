
def even_fib_sum():
    fib_list = [1, 2]
    total_sum = 0
    while (fib_list[-1] + fib_list[-2]) < 4_000_000:
        fib_list.append(fib_list[-1] + fib_list[-2])
    for each_num in fib_list:
        if each_num % 2 == 0:
            total_sum += each_num

    return total_sum


print('Even sum of numbers below 4.000.000:', even_fib_sum())
