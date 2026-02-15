def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()  # new line after each row


if __name__ == "__main__":
    n = int(input().strip())
    multiplication_table(n)
