def recursive(n):
    if n <= 1:
        return n
    else:
        return recursive(n-1) + recursive(n-2)

print(recursive(int(input("Enter a number: "))))