def char_histogram(string):
    result = {}

    for char in string:
        if char in result:
            result[char] = result.get(char) + 1
            continue
        
        result[char] = 1

    return result
