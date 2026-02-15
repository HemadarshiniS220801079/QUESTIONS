def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    n = len(orderNumbers)
    present = [False] * (n + 1)
    for num in orderNumbers:
        if 1 <= num <= n:
            present[num] = True
    for i in range(1, n + 1):
        if not present[i]:
            return i
    return n + 1

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
