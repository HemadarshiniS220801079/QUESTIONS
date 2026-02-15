def square_even_numbers(lst):
    result = []
    
    for num in lst:
        if num % 2 == 0:  
            result.append(num * num)
    
    return result


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(*square_even_numbers(lst))
