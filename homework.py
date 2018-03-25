import re


def list_reverse(arr):
    return arr[::-1]


def string_filter(line, min_letter_count=1):
    filtered_string = ''
    for letter in set(line):
        if line.count(letter) > min_letter_count:
            filtered_string = filtered_string + letter
    return filtered_string


# I'm a little bit confusing about immutable data. I didn't understand what you certainly mean.
# That's why I used tuple instead list. I have no idea how immutable dict should look
def update(id, state):
    array = (
        {'id': 1, 'state': True},
        {'id': 2, 'state': True},
        {'id': 8, 'state': False}
    )
    new_arr = ()
    for elem in array:
        if elem['id'] is id:
            new_elem = dict((('id', id), ('state', state)))
        else:
            new_elem = dict((('id', elem['id']), ('state', elem['state'])))
        new_arr = new_arr + (new_elem,)
    return new_arr


def normalize(line):
    result = re.sub("[!\"$%&\'*+,-./:;<=?[\\]^`{|}~\t\n\\x0b\x0c\r\s]", '', line)
    result = result.strip('> ')
    result = result.replace('>', ' > ')
    return result


