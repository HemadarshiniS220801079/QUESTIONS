def pair_elements(lst):
    result = []
    
    for i in range(0, len(lst) - 1, 2):
        result.append((lst[i], lst[i + 1]))
    
    return result


if __name__ == "__main__":
    lst = input().split()
    print(pair_elements(lst))
