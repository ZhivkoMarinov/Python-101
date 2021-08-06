import copy

Pretensions = {
    'A': [-1, 0],
    'B': [1, 0],
    'R': [0, 1],
    'L': [0, -1],

}


def outside_of_matrix(layout, coordinates):
    x, y = coordinates

    min_x = 0
    max_x = len(layout) - 1

    min_y = 0
    max_y = len(layout[0]) - 1

    return x < min_x or x > max_x or y < min_y or y > max_y


def construct_seat_matrix(friends_configurations):

    seat_matrix = {}

    for friend in friends_configurations:

        if len(friend) == 1:
            seat_matrix[friend] = [0, 0]
            continue

        if friend[2] in seat_matrix:
            start_x, start_y = seat_matrix[friend[2]]
            seat_matrix[friend[0]] = [start_x + Pretensions[friend[1]][0],
                                      start_y + Pretensions[friend[1]][1]]

    return seat_matrix


def find_places(layout, seat_matrix, layout_matrix):

    result = []
    temp = {}
    counter = 0

    for seat in layout_matrix:
        x, y = seat[0], seat[1]

        for key, value in seat_matrix.items():
            if outside_of_matrix(layout, (x + value[0], y + value[1])) or \
                    layout[x + value[0]][y + value[1]] == '*':
                temp = {}
                counter = 0
                break

            temp[key] = [x + value[0], y + value[1]]
            counter += 1

            if counter == len(seat_matrix):
                result.append(temp)
                temp = {}
                counter = 0

    return result


def print_solutions(cinema_layout, all_possibilities):
    result = []
    counter = 0

    for order in all_possibilities:
        result.append(copy.deepcopy(cinema_layout))

        for key, value in order.items():
            x, y = value

            temp_string = list(result[counter][x])
            temp_string[y] = key
            result[counter][x] = ''.join(temp_string)

        for answer in result[counter]:
            print(answer)
        print('\n')
        counter += 1


def stranger_forms(cinema_layout, friends_configuration):
    matrix = []

    for row in range(len(cinema_layout)):
        for col in range(len(cinema_layout[row])):
            matrix.append([row, col])

    all_possibilities = find_places(cinema_layout, construct_seat_matrix(friends_configuration), matrix)

    return print_solutions(cinema_layout, all_possibilities)


stranger_forms(
    ['..*...*.**',
     '.....**...',
     '*.*...*..*',
     '.**....*.*',
     '...*..*.*.',
     '.***...*..',
     '*......*.*',
     '.....**..*',
     '..*.*.*..*',
     '***.*.**..'
     ], ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]
)
