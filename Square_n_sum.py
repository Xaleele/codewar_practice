def square_sum(numbers):
    empty_list = []
    for num in range(len(numbers)):
        numsq = numbers[num]**2
        empty_list.append(numsq)
    return sum(empty_list)