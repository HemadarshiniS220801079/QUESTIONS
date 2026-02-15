def replace_digits(text):
    result = ""
    
    for ch in text:
        if ch.isdigit():
            result += "#"
        else:
            result += ch
    
    return result


if __name__ == "__main__":
    text = input().strip()
    print(replace_digits(text))
