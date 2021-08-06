def nan_expand(times):

    answer = 'Not a '
    result = []

    if times != 0:
        result.append((answer * times) + 'NaN')
    else:
        return ''

    return ''.join(result)
