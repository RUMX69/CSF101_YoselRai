Practical 3 Documentation & Reflection
a) Documentation
Main Concepts Applied
Queue Data Structure:
Implemented a queue using a Python class with a list as the underlying storage. Practiced the core queue operations: enqueue (adding to the rear), dequeue (removing from the front), checking if the queue is empty, accessing the front element, and determining the size of the queue.

Object-Oriented Programming:
Used class definitions, constructors (__init__), and instance methods to encapsulate queue behavior and data.

Error Handling:
Added error handling for cases where dequeue or front operations are attempted on an empty queue, raising an IndexError with a descriptive message.

Testing and Output:
Wrote test code to enqueue and dequeue elements, print the front element, and display the size of the queue to verify correct implementation.

b) Reflection
What I Learned
Gained a clear understanding of how queues work and how to implement them from scratch in Python.
Practiced using object-oriented programming principles to organize code and encapsulate data and behavior.
Learned the importance of handling edge cases, such as attempting to dequeue from an empty queue, to make code more robust and user-friendly.
Challenges Faced and How I Overcame Them
Handling Empty Queue Operations:
Initially, I did not handle the case where dequeue or front was called on an empty queue, which caused errors. I resolved this by adding checks and raising appropriate exceptions.
Testing All Methods:
Ensured that all queue methods worked as expected by writing and running test cases for each operation.
Understanding List Performance:
Noticed that using pop(0) on a list is not the most efficient for large queues, as it has O(n) time complexity. Researched alternatives like collections.deque for more efficient queue operations, but kept the list implementation for learning purposes.
This practical improved my understanding of data structures, object-oriented programming, and robust error handling in Python. The process of testing and refining the implementation helped reinforce these concepts and prepared me for more complex data structure challenges.