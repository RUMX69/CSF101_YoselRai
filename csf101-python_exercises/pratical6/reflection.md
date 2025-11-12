# Searching Algorithms Practical Documentation & Reflection

## a) Documentation

### Main Concepts Applied

**Linear Search Implementation:**
Implemented a straightforward sequential search algorithm that checks each element one by one until the target is found or the end of the array is reached. This approach works on both sorted and unsorted data and returns the first occurrence of the target element.

**Binary Search Algorithm:**
Implemented the iterative version of binary search that efficiently finds elements in sorted arrays by repeatedly dividing the search space in half. Used careful index management with left and right pointers to ensure correct boundary conditions.

**Recursive Binary Search:**
Applied divide-and-conquer principles to create a recursive version of binary search. Used proper base case termination (when left > right) and recursive calls that progressively narrow the search space by adjusting the left and right boundaries.

**Algorithm Analysis:**
Compared time and space complexity between algorithms: Linear Search (O(n) time, O(1) space), Binary Search (O(log n) time, O(1) space), and Recursive Binary Search (O(log n) time, O(log n) space due to recursion stack).

**Testing and Verification:**
Created comprehensive test cases including edge scenarios like empty arrays, single elements, duplicate values, and missing targets to ensure algorithm robustness and correctness.

## b) Reflection

### What I Learned
- Gained practical understanding of the fundamental differences between linear and binary search algorithms and their respective time complexities
- Learned that Binary Search requires sorted data as a prerequisite, highlighting the trade-off between preprocessing overhead and search efficiency
- Developed deeper insight into recursive problem-solving through implementing recursive binary search and understanding its call stack behavior
- Improved my ability to analyze algorithm performance characteristics and select the appropriate search method based on data size and structure
- Understood the importance of handling edge cases and boundary conditions in search algorithms to ensure robustness

### Challenges Faced and How I Overcame Them

**Recursive Base Case Definition:**
Initially struggled with defining the proper termination condition for recursive binary search. I overcame this by tracing through small examples step by step and visualizing how the search space shrinks with each recursive call.

**Index Management in Binary Search:**
Faced off-by-one errors when calculating midpoints and updating left/right boundaries. Solved this by carefully testing with edge cases and creating visual diagrams of the search process to verify index calculations.

**Understanding Space Complexity Differences:**
Was initially confused about why recursive binary search had higher space complexity. I addressed this by analyzing the recursion call stack and understanding how each recursive call consumes additional memory.

**Algorithm Selection Decisions:**
Found it challenging to determine when to prefer one algorithm over another in different scenarios. I resolved this by creating comparison tables of time/space complexity and considering real-world use cases for each approach.

This practical provided valuable hands-on experience with fundamental searching algorithms, strengthening my understanding of algorithm analysis, recursive thinking, and the importance of choosing the right tool for specific problem constraints. The process of implementing, testing, and comparing these algorithms has built a solid foundation for tackling more complex algorithmic challenges in future programming tasks.