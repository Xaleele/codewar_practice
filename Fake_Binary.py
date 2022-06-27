def fake_bin(x):
    elist = []
    for i in range(len(x)):
        if int(x[i]) < 5:
            elist.append("0")
        else:
            elist.append("1")
    xstrng = "".join(elist)
    return xstrng
