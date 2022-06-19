def increment_string(strng):
    n_list = []
    s_list = []
    if strng.isalpha():
        strng = strng + "1"
        return strng
    else:
        for i in range(len(strng)):
            if strng[i].isnumeric():
                n_list.append(strng[i])
            else:
                s_list.append(strng[i])
        n_list = ''.join(n_list)
        s_list = ''.join(s_list)
        i_list = int(n_list) + 1
        strng = s_list + str(i_list)
        return strng
