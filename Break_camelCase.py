def solution(s):
    nlist = []
    for i in range(len(s)):
        if s[i].isupper() == False:
            nlist.append(s[i])
        else:
            nlist.append(' ' + s[i])

    strng = ''.join(nlist)
    return strng