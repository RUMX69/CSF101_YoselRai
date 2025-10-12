Practical 5 Documentation & Reflection
a) Documentation
Main Concepts Applied
Binary Search Tree (BST) Implementation:
Built a BST from scratch using Python classes. Implemented core operations: insertion, searching, deletion, and three types of traversals (in-order, pre-order, post-order). Used recursion for most operations to simplify logic and maintain code clarity.

BST Deletion Algorithm:
Carefully handled all deletion cases: removing a leaf node, a node with one child, and a node with two children (by replacing with the minimum value from the right subtree).

Graph Implementation (Adjacency List):
Created an undirected graph using a dictionary to represent adjacency lists. Supported adding vertices and edges dynamically.

Graph Traversals:
Implemented Depth-First Search (DFS) using recursion and Breadth-First Search (BFS) using a queue (collections.deque). Used a visited set to avoid revisiting nodes.

Object-Oriented Programming:
Encapsulated tree and graph behaviors in classes, using methods to organize and modularize code.

Testing and Output:
Wrote test code to insert, search, delete, and traverse the BST, as well as to build and traverse the graph, printing results to verify correctness.

b) Reflection
What I Learned
Gained practical experience implementing both trees and graphs from scratch, reinforcing my understanding of these fundamental data structures.
Learned how to perform and implement tree traversals (in-order, pre-order, post-order) and graph traversals (DFS and BFS), and when to use each.
Improved my object-oriented programming skills by designing and organizing code using classes and methods.
Understood the importance of handling edge cases, such as deleting nodes with two children in BSTs and ensuring all nodes are visited in graph traversals.
Challenges Faced and How I Overcame Them
BST Deletion Logic:
Handling deletion of nodes with two children was tricky. I reviewed the algorithm, used helper functions to find the minimum value in the right subtree, and tested thoroughly to ensure correctness.

Graph Traversal Bugs:
Initially, my DFS and BFS implementations revisited nodes or missed some. I fixed this by carefully managing the visited set and testing with different graph structures.

Testing and Debugging:
Some methods did not work as expected on the first try. I used print statements and step-by-step tracing to verify the correctness of insertions, deletions, and traversals.

This practical strengthened my understanding of tree and graph data structures, traversal algorithms, and object-oriented programming in Python. The process of implementing, testing, and debugging these structures has prepared me for more advanced algorithmic challenges.