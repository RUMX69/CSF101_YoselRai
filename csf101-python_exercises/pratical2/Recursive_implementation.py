def recursive(n): # Function to calculate Fibonacci number using recursion
    if n <= 1: # Base case for recursion
        return n # If n is 0 or 1, return n
    else:
        return recursive(n-1) + recursive(n-2) # Recursive case to calculate Fibonacci number

print(recursive(int(input("Enter a number: ")))) # Input a number to get its Fibonacci value