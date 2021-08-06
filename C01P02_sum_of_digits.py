def sum_of_digits(n):
    digit_list = []
    n = abs(n)

    for i in str(n):
        digit_list.append(int(i))

    return sum(digit_list)
