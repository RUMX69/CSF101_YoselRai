Practical 2 Reflection
Instructions
For this practical, we were required to:

Implement the Fibonacci sequence using both recursive and iterative approaches in Python.
Accept user input to specify which Fibonacci number to compute.
Compare the recursive and iterative solutions in terms of logic, efficiency, and implementation.
Reflect on the challenges faced and what was learned during the process.
Solutions
Recursive Implementation

def recursive(n): # Function to calculate Fibonacci number using recursion    if n <= 1: # Base case for recursion        return n # If n is 0 or 1, return n    else:        return recursive(n-1) + recursive(n-2) # Recursive case to calculate Fibonacci numberprint(recursive(int(input("Enter a number: ")))) # Input a number to get its Fibonacci value
Iterative Implementation

def iterative(n): # Function to calculate Fibonacci number using iteration    if n == 0: # Base case for iteration        return 0    elif n == 1:        return 1    a, b = 0, 1 # Initial values for Fibonacci sequence    for i in range(2, n + 1): # Iterate from 2 to n        a, b = b, a + b # Update values for next Fibonacci number    return b # Return the nth Fibonacci numberprint(iterative(int(input("Enter a number: ")))) # Input a number to get its Fibonacci value
Reflection
What I Learned
Understood the difference between recursive and iterative approaches for solving the same problem.
Learned that recursion closely matches the mathematical definition but can be inefficient for large inputs due to repeated calculations and stack overflow.
Saw that iteration is more efficient for the Fibonacci sequence, as it avoids redundant calculations and is faster for large inputs.
Improved my ability to write modular code using functions and handle user input/output in Python.
Challenges Faced and How I Overcame Them
Stack Overflow in Recursion:
When using large input values with the recursive function, I encountered a maximum recursion depth error. I learned to use smaller inputs for recursion and understood the need for optimization (like memoization) for larger values.
Efficiency Issues:
The recursive approach was much slower for large numbers. This highlighted the importance of analyzing algorithm efficiency.
Input Validation:
Initially, the code did not handle invalid or negative inputs. I realized the importance of validating user input for robustness.
Debugging:
Faced off-by-one errors in the iterative solution. Careful tracing and testing helped me fix these issues.
This practical enhanced my understanding of recursion and iteration, and gave me practical experience in comparing different algorithmic approaches to the same problem. The challenges I faced taught me valuable lessons in debugging, efficiency, and writing user-friendly code.