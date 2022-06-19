def increment_string(strng):
    new_i = ''
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
        n = ''.join(n_list)
        s = ''.join(s_list)
        iw = int(n) + 1
        #print(iw)
        zero_lead = ("0" * (len(n) - len(str(iw)))) + str(iw)
        return s + zero_lead




increment_string('')

