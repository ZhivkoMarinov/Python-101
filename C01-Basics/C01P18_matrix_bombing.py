def outside_of_matrix(matrix, coordinates):
    x, y = coordinates

    min_x = 0
    max_x = len(matrix) - 1

    min_y = 0
    max_y = len(matrix[0]) - 1

    return x < min_x or x > max_x or y < min_y or y > max_y


def bomberman(matrix, coordinates, matrix_sum):

    directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
        [1, -1],
        [1, 1],
        [-1, 1],
        [-1, -1]
    ]

    x, y = coordinates
    result = matrix_sum

    for direction in directions:

        if outside_of_matrix(matrix, (x + direction[0], y + direction[1])):
            continue, 6, 6, 3, 2])

        if matrix[x + direction[0]][y + direction[1]] - matrix[x][y] < 0:
            result -= matrix[x + direction[0]][y + direction[1]]
        else:
            result -= matrix[x][y]

    return result


def matrix_bombing_plan(m):

    result = {}
    matrix_sum = 0

    for i in m:
        matrix_sum += sum(i)

    for x in range(len(m)):
        for y in range(len(m[0])):
            result[x, y] = bomberman(m, (x, y), matrix_sum)

    return result
