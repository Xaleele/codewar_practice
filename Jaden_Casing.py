def to_jaden_case(string):
    jlist = []
    x = string.split()
    for word in x:
        firstw = word[0].capitalize()
        last = word[1:].lower()
        jaden = firstw + last
        jlist.append(jaden)
    j_case = ' '.join(jlist)
    return j_case
to_jaden_case("Welcome to the jungle")


