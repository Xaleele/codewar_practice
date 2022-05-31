def get_middle(s):
    empty_list = []

    for letter in s:
        empty_list.append(letter)
    if len(empty_list) == 1:
        return (empty_list[0])

    elif len(empty_list) % 2 != 0:
        return (str(empty_list[int(len(empty_list) / 2)]))
    else:
        return (str(empty_list[int(len(empty_list) / 2) - 1]) + str(empty_list[int(len(empty_list) / 2)]))
