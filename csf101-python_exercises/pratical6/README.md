# Searching Algorithms Practical Documentation & Reflection

## Instructions
For this practical, we were required to:

1. Implement three fundamental searching algorithms: Linear Search, Binary Search, and Recursive Binary Search
2. Understand the differences in time and space complexity between these algorithms
3. Test each implementation with appropriate sample data to verify correctness
4. Analyze the performance characteristics and use cases for each searching approach
5. Apply problem-solving skills to modify and extend the basic algorithms

## Reflection

### What I Learned
- **Algorithm Efficiency**: Gained practical understanding of how Linear Search (O(n)) performs compared to Binary Search (O(log n)) and the significant performance implications for large datasets
- **Prerequisite Conditions**: Learned that Binary Search requires sorted data, while Linear Search works on any arrangement, highlighting the trade-off between preprocessing and search efficiency
- **Recursive Thinking**: Developed deeper understanding of recursive problem-solving through the recursive binary search implementation and its call stack behavior
- **Edge Case Handling**: Recognized the importance of handling scenarios like empty arrays, missing elements, and boundary conditions in search algorithms

### Challenges Faced and How I Overcame Them
1. **Understanding Recursive Base Cases**
   - Initially struggled with defining the proper termination condition for recursive binary search
   - Overcame by tracing through small examples and understanding how the search space shrinks with each recursive call

2. **Index Management in Binary Search**
   - Faced off-by-one errors when calculating midpoints and updating left/right boundaries
   - Solved by carefully testing with edge cases and visualizing the search process

3. **Algorithm Selection**
   - Was uncertain when to prefer one algorithm over another in different scenarios
   - Addressed by analyzing time/space complexity and considering data characteristics like size and sort status

4. **Testing Comprehensive Scenarios**
   - Initially tested only with ideal cases, missing important edge conditions
   - Improved by creating systematic test cases including empty arrays, single elements, duplicates, and missing targets

This practical provided valuable hands-on experience with fundamental searching algorithms, strengthening my understanding of algorithm analysis, recursive thinking, and the importance of choosing the right tool for specific problem constraints. The process of implementing, testing, and comparing these algorithms has built a solid foundation for tackling more complex algorithmic challenges.