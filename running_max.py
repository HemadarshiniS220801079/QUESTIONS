def running_max_reset(nums):
    result = []
    current_max = 0

    for num in nums:
        if num <= 0:
            current_max = 0
        else:
            if num > current_max:
                current_max = num
        
        result.append(current_max)

    return result

nums = list(map(int, input().split()))
print(running_max_reset(nums))
