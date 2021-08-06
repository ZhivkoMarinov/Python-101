def reduce_file_path(path):
    result = []

    for i in path.split('/'):

        if i == '.' or i == '':
            continue

        if i == '..':
            if len(result) > 0:
                result.pop()
            continue

        result.append('/' + i)

    if len(result) < 1:
        result.append('/')

    return ''.join(result)
