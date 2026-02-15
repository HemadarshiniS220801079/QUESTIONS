def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    if len(intervals) == 0:
        return []
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    merged.append(intervals[0])
    for i in range(1, len(intervals)):
        current = intervals[i]
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged
    

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
