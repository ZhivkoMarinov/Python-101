def fact_digits(n):
    n = abs(n)
    digit_list = []
    factorial = []

    for i in str(n):
        digit_list.append(int(i))

    result = 1

    for num in digit_list:
        for x in range(1, num + 1):
            result = result * x
        factorial.append(result)
        result = 1

    return sum(factorial)
