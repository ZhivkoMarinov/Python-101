def eratosthenes(n):
    prime_list = [i for i in range(n + 1)]

    for i in range(len(prime_list)):
        prime_list[i] = True

    prime_list[0] = prime_list[1] = False

    for i in range(2, len(prime_list)):
        if prime_list[i]:
            j = i + i
            while j <= n:
                prime_list[j] = False
                j += i

    return prime_list


def goldbach(n):

    if n <= 2 or n % 2 != 0:
        return

    p = eratosthenes(n)
    result = []
    temp = []

    for index1 in range(len(p)):
        for index2 in range(len(p)):
            if p[index1] and p[index2] and index1 + index2 == n:
                temp.append((index1, index2))

    for i in range(len(temp)):
        if list(temp[i]) == sorted(temp[i]):
            result.append(temp[i])

    return result
