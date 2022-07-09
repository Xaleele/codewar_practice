def get_sum(a, b):
    elist = []
    if a == b:
        return a
    elif a < b:
        for num in range(a,b+1,1):
            elist.append(num)
    elif a > b:
        for num in range(b,a+1,1):
            elist.append(num)

    return sum(elist)