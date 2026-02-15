def rotate_right(lst, k):
    n = len(lst)
    
    if n == 0:
        return lst
    k = k % n 
    for _ in range(k):
        last = lst.pop()     
        lst.insert(0, last)  
    
    return lst


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    k = int(input().strip())
    
    result = rotate_right(lst, k)
    print(*result)
