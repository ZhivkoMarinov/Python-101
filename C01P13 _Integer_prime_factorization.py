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


def prime_factorization(n):
    p = eratosthenes(n)
    index = 2
    result = []

    while n > 1:
        a = 0
        while p[index] and n % index == 0:
            n = n // index
            a += 1

        if a > 0:
            result.append((index, a))

        index += 1

    return result
