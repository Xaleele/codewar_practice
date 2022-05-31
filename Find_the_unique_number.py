def find_uniq(arr):
    for n in range(len(arr)):
        if arr[n] == arr[n+1]:
            continue
        elif arr[n] != arr[n+1] and arr[n] == arr[n-1]:
            return(arr[n+1])
            break





