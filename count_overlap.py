def count_overlapping_substring(text, pattern):
    if pattern == "":
        return 0
    
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    
    return count


if __name__ == "__main__":
    text = input().strip()
    pattern = input().strip()
    
    result = count_overlapping_substring(text, pattern)
    print(result)
