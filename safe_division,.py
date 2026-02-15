def safe_division(numerator, denominator):
    if denominator == 0:
        return "NaN"
    return numerator / denominator


if __name__ == "__main__":
    numerator = float(input().strip())
    denominator = float(input().strip())
    
    result = safe_division(numerator, denominator)
    print(result)
