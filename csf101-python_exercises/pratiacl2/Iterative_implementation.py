def iterative(n): # Function to calculate Fibonacci number using iteration
    if n == 0: # Base case for iteration
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1 # Initial values for Fibonacci sequence
    for i in range(2, n + 1): # Iterate from 2 to n
        a, b = b, a + b # Update values for next Fibonacci number
    return b # Return the nth Fibonacci number

print(iterative(int(input("Enter a number: ")))) # Input a number to get its Fibonacci value
