# Algorithm Problems Practical Documentation & Reflection

## Instructions
For this practical, we were required to:

- Implement solutions to seven fundamental algorithm problems covering arrays, strings, and hash-based operations
- Apply efficient algorithmic patterns including two pointers, sliding window, and hash map optimizations
- Handle edge cases and optimize for time and space complexity in each solution
- Write and test code to verify the correctness of each implementation
- Demonstrate understanding of when to use different data structures and algorithms based on problem constraints

## Reflection

### What I Learned
- Gained practical experience solving common algorithm problems that frequently appear in technical interviews
- Learned to apply hash maps and sets for O(1) lookups to optimize solutions from O(n²) to O(n) time complexity
- Improved my understanding of the two-pointer technique for problems involving sorted arrays and string manipulation
- Developed skills in implementing sliding window algorithms for substring and subarray problems
- Understood the importance of sorting as a preprocessing step to enable more efficient algorithms
- Enhanced my ability to analyze time and space complexity trade-offs between different approaches

### Challenges Faced and How I Overcame Them

**Duplicate Handling in 3Sum:**
Managing duplicate triplets without using extra storage was challenging. I overcame this by carefully analyzing the sorted array and implementing conditional checks to skip identical elements during iteration.

**Sliding Window Boundaries:**
Maintaining correct window start and end positions in the longest substring problem was difficult. I solved this by visualizing the window movement and implementing proper index updates when encountering duplicate characters.

**Space-Time Complexity Decisions:**
Choosing between character frequency arrays and hash maps required careful consideration. I addressed this by analyzing problem constraints and selecting arrays for limited character sets and hash maps for larger ranges.

**Two Pointer Synchronization:**
Coordinating pointer movements in palindrome checking, especially when skipping non-alphanumeric characters, presented challenges. I resolved this by implementing careful while loop conditions and boundary checks.

**Optimization from Brute Force:**
Identifying optimization opportunities in problems like stock buying required pattern recognition practice. I improved by learning to track minimum/maximum values during single passes rather than nested iterations.

This practical significantly strengthened my problem-solving skills and algorithmic thinking. The process of implementing, testing, and optimizing these common problems has enhanced my ability to recognize patterns and apply appropriate data structures. Working through edge cases and efficiency considerations has prepared me for more complex algorithmic challenges and technical interviews.