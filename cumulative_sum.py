def cumulative_sum_until_negative(lst):
    total = 0
    
    for num in lst:
        if num < 0:  
            break
        total += num
    
    return total


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(cumulative_sum_until_negative(lst))
