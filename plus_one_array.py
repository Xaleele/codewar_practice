def up_array(arr):
    empty_list = []
    if len(arr) <1:
        return None
    for num in range(len(arr)):
        if arr[num] >= 0 and arr[num] <= 9:
            str_num = str(arr[num])
            empty_list.append(str_num)
        else:
            return None
    sum_list = ''.join(empty_list)
    intsum = int(sum_list)
    intsum += 1
    strsum = str(intsum)
    sum_map = map(int, strsum)
    str_list = list(sum_map)
    return str_list