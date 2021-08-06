phone_keys = {
        0: " ",
        1: '1',
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
    }

def convert_to_message(number):

    message_ready = []

    for index in number:
        key = index[0]
        letter = len(index)
        counter = 0

        if letter > len(phone_keys[key]):

            for i in range(letter):
                counter += 1

                if counter > len(phone_keys[key]):
                    counter = 1

                letter = counter

        message_ready.append(phone_keys[key][letter - 1])

    for i, v in enumerate(message_ready):
        if v == '1':
            message_ready[i + 1] = message_ready[i + 1].upper()
            message_ready.pop(i)

    return ''.join(message_ready)


def numbers_to_message(pressed_sequence):
    sequence_list = []

    num = 0

    while num < len(pressed_sequence):
        item = pressed_sequence[num]
        temp = [item]
        next_num = num + 1

        while next_num < len(pressed_sequence) and item == pressed_sequence[next_num]:

            temp.append(pressed_sequence[next_num])
            next_num += 1

        sequence_list.append(temp)
        num = next_num

    cleared_sequence = []
    for i in range(len(sequence_list)):
        if -1 not in sequence_list[i]:
            cleared_sequence.append(sequence_list[i])

    return convert_to_message(cleared_sequence)


def presses_count(key, char_list, char):

    result = []
    for count in range(len(char_list)):
        if result and int(result[-1]) == key:
            result.append('-1')

        if char_list[count] == char:
            result.append(str(key) * (count + 1))

    return result


def presses_count(key, char_list, char):

    result = ''
    if char.isupper():
        result += '1'

    for count in range(len(char_list)):

        if char_list[count] == char.lower():
            result += str(key) * (count + 1)

    return result


def message_to_numbers(message):

    temp = ''
    for char in message:
        for item in phone_keys.items():
            if char.lower() in item[1]:
                result = presses_count(item[0], item[1], char)

                if temp and temp[-1] == result[-1]:
                    temp += '-1'
                temp += result

    answer = []
    for x in range(len(temp)):
        if temp[x] == '-':
            answer.append(int('-' + temp[x + 1]))
            continue

        if temp[x-1] and temp[x-1] == '-':
            continue
        answer.append(int(temp[x]))

    return answer
