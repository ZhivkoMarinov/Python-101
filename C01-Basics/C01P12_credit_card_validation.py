def calculations(data):
    data = list_builder(data)[::-1]
    result = 0
    double = False

    for i in range(len(data)):
        multiplier = 1

        if double:
            multiplier = 2

        result += sum(list_builder(data[i] * multiplier))

        double = not double

    return result


def list_builder(number):
    ready_list = []

    for i in str(number):
        ready_list.append(int(i))

    return ready_list


def is_credit_card_valid(number):

    return calculations(number) % 10 == 0
