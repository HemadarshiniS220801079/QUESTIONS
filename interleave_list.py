def interleave_lists(list1, list2):
    result = []
    
    length = min(len(list1), len(list2))
    
    for i in range(length):
        result.append(list1[i])
        result.append(list2[i])
    
    return result


if __name__ == "__main__":
    list1 = input().split()
    list2 = input().split()
    
    result = interleave_lists(list1, list2)
    print(*result)
