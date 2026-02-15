def countResponseTimeRegressions(responseTimes):
    # Write your code here
    total = 0
    count = 0

    for i in range(len(responseTimes)):
        if i == 0:
            total += responseTimes[i]
            continue

        if responseTimes[i] * i > total:
            count += 1

        total += responseTimes[i]

    return count
         

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
