def isAlphabeticPalindrome(code):
    # Write your code here
    filtered = ""
    for ch in code:
        if ch.isalpha():
            filtered += ch.lower()
    return filtered == filtered[::-1]

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
