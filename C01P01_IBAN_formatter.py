def iban_formatter(iban):
    result = []
    counter = 0
    
    for char in iban:
        if char == ' ':
            continue
        else:
            result.append(char)
            counter += 1
            if counter == 4:
                result.append(' ')
                counter = 0

    return ''.join(result)
