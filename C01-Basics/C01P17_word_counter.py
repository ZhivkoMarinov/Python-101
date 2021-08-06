import enum

class Directions(enum.Enum):

    HORIZONTAL_RIGHT = 'HORIZONTAL_RIGHT'
    HORIZONTAL_LEFT = 'HORIZONTAL_LEFT'

    VERTICAL_UP = 'VERTICAL_UP'
    VERTICAL_DOWN = 'VERTICAL_DOWN'

    DIAGONAL_UP_RIGHT = 'DIAGONAL_UP_RIGHT'
    DIAGONAL_UP_LEFT = 'DIAGONAL_UP_LEFT'

    DIAGONAL_DOWN_RIGHT = 'DIAGONAL_DOWN_RIGHT'
    DIAGONAL_DOWN_LEFT = 'DIAGONAL_DOWN_LEFT'


def word_finder(length, coordinates, direction, matrix):

    x, y = coordinates
    end_x = len(matrix) - 1
    end_y = len(matrix[0]) - 1
    temp = []

    if direction == Directions.HORIZONTAL_RIGHT:
        while y <= end_y:
            temp.append(matrix[x][y])
            y += 1
            if len(temp) == length:
                return ''.join(temp)

    if direction == Directions.HORIZONTAL_LEFT:
        while end_y >= y >= 0:
            temp.append(matrix[x][y])
            y = y - 1
            if len(temp) == length:
                return ''.join(temp)

    if direction == Directions.VERTICAL_UP:
        while end_x >= x >= 0:
            temp.append(matrix[x][y])
            x -= 1
            if len(temp) == length:
                return ''.join(temp)

    if direction == Directions.VERTICAL_DOWN:
        while x <= end_x:
            temp.append(matrix[x][y])
            x += 1
            if len(temp) == length:
                return ''.join(temp)

    if direction == Directions.DIAGONAL_UP_RIGHT:
        while end_x >= x >= 0 and y <= end_y:
            temp.append(matrix[x][y])
            x -= 1
            y += 1
            if len(temp) == length:
                return ''.join(temp)

    if direction == Directions.DIAGONAL_UP_LEFT:
        while end_x >= x >= 0 and end_y >= y >= 0:
            temp.append(matrix[x][y])
            x -= 1
            y -= 1
            if len(temp) == length:
                return ''.join(temp)

    if direction == Directions.DIAGONAL_DOWN_RIGHT:
        while x <= end_x and y <= end_y:
            temp.append(matrix[x][y])
            x += 1
            y += 1
            if len(temp) == length:
                return ''.join(temp)

    if direction == Directions.DIAGONAL_DOWN_LEFT:
        while x <= end_x and end_y >= y >= 0:
            temp.append(matrix[x][y])
            x += 1
            y -= 1
            if len(temp) == length:
                return ''.join(temp)


def word_counter(matrix, word):

    result = 0
    word_length = len(word)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for direction in Directions:
                if word_finder(word_length, (row, col), direction, matrix) == word:
                    result += 1

    if word == ''.join(reversed(word)):
        result = result // 2

    return result


print(word_counter(
    [
        ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],
        ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],
        ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],
        ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],
        ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],
        ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],
        ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],
        ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]
    ], 'actually'))
