def second_largest_index(arr):
    
    if len(arr) < 2:
        return -1
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    second = None
    for num in arr:
        if num != largest:
            if second is None or num > second:
                second =num
    if second is None:
        return -1
    for i in range(len(arr)):
        if arr[i] == second:
            return i

    return -1


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(second_largest_index(arr))
