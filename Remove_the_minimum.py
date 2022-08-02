def remove_smallest(numbers):
    nlist = []
    zlist = []
    for number in numbers:
        if number == min(numbers) and number not in nlist:
            nlist.append(number)
            continue
        else:
            zlist.append(number)

    print(zlist)

remove_smallest([1,2,3,4,1,5])