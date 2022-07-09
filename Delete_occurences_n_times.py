def delete_nth(order, max_e):
    elist = []
    for num in order:
        if elist.count(num) < max_e:
            elist.append(num)
        else:
            continue
    print(elist)


delete_nth([20,37,20,21], 1)

# nlist = [20,37,20,21]
#
# ncount = nlist.count(20)
#
# print(ncount)