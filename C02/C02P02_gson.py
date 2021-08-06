import json
import sys


def get_attribute_index(attribute):

    key = ''
    temp_list = []
    keys_list = []

    for char in attribute:

        if char == '[' or char == ']':
            if key != '':
                temp_list.append(key)
                key = ''
            continue

        key += char

    for k in temp_list:
        if k.isdigit():
            keys_list.append(int(k))
            continue
        if k.startswith('-') and k[1:].isdigit():
            keys_list.append(-int(k[1:]))
            continue
        keys_list.append(k)

    return keys_list


def path_constructor(path):

    attributes = path.split('.')
    keys_list = []

    for a in attributes:

        if a.endswith(']'):
            keys_list += get_attribute_index(a)
            continue

        keys_list.append(a)

    return keys_list


def gson(json_file, path):

    keys = path_constructor(path)

    try:
        file = open(json_file)
        data = json.load(file)
    except:
        sys.stderr.write('Error: JSON file not found\n')
        sys.exit(1)

    try:
        for k in keys:
            data = data[k]
        sys.stdout.write(str(data) + '\n')
    except:
        sys.stderr.write('Error: Property not found\n')
        sys.exit(1)


gson(sys.argv[1], sys.argv[2])
import re


def parse_path_to_list(args):

    params = re.findall('[a-zA-Z]+|[0-9]+', args)
    return params
