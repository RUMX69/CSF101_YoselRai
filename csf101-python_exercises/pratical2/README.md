# Practical 2 Documentation & Reflection

## a) Documentation

### Main Concepts Applied

#### Recursion
Implemented the Fibonacci sequence using a recursive function. The recursive approach involves a function calling itself with smaller arguments until it reaches a base case. This demonstrates the concept of breaking a problem into smaller subproblems and solving them recursively.

#### Iteration
Developed an iterative solution for the Fibonacci sequence. The iterative approach uses a loop to build up the solution step by step, updating variables to keep track of the current and previous Fibonacci numbers. This method is generally more efficient in terms of time and memory usage compared to recursion for this problem.

#### Input/Output Handling
Used the `input()` function to receive user input and `print()` to display the result. This allowed for interactive testing of both implementations.

#### Function Definition and Return Values
Defined functions that take parameters and return computed values, reinforcing the concept of modular programming and code reuse.

## b) Reflection

### What I Learned
- Gained a deeper understanding of the differences between recursive and iterative approaches to problem-solving.
- Learned how recursion can be elegant and closely match the mathematical definition of a problem, but may be less efficient due to repeated calculations and stack usage.
- Saw that iteration is often more efficient for problems like Fibonacci, as it avoids redundant calculations and stack overflow issues.
- Improved my skills in writing clean, modular functions and handling user input/output in Python.

### Challenges Faced and How I Overcame Them

#### Efficiency Comparison
Noticed that the recursive approach was much slower for larger numbers compared to the iterative approach. This helped me appreciate the importance of analyzing the time and space complexity of different algorithms.

#### Input Validation
Initially, the code did not handle invalid inputs (like negative numbers or non-integers). I realized the importance of validating user input to make the program more robust.

#### Debugging Logic Errors
Faced minor issues with off-by-one errors in the iterative implementation. Careful tracing of variable values and step-by-step debugging helped me fix these issues.

This practical enhanced my understanding of recursion and iteration, and gave me practical experience in comparing different algorithmic approaches to the same problem. The challenges I faced taught me valuable lessons in debugging, efficiency, and writing user-friendly code.