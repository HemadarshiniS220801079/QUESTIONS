def transform_numbers(numbers):
    result = []
    
    for num in numbers:
        if num % 2 == 0:
            result.append(num ** 2)   
        else:
            result.append(num ** 3)   
    
    return result


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    
    transformed = transform_numbers(numbers)
    
    print(*transformed)
