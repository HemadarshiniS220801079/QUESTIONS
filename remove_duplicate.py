def remove_duplicates_keep_last(lst):
    result = []
    n = len(lst)
    
    for i in range(n):
        if lst[i] not in lst[i+1:]:
            result.append(lst[i])
    
    return result


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    result = remove_duplicates_keep_last(lst)
    print(*result)
