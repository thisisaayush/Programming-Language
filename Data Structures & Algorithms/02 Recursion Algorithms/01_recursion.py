'''
-   Recursion is a fundamental concept in computer science and programming that involves solving problems by breaking
    them down into smaller, similar subproblems. It's a process where a function calls itself to solve a problem.

-   Recursion typically consists of two parts:
    a. Base Case: The base case is the condition under which the recursive function terminates. The base case is
       essential to prevent infinite recursion.

    b. Recursive Case: In the recursive case, the function breaks the problem down into smaller instances of the same
       problem and makes one or more recursive calls to solve those smaller instances. The function then combines the
       results from these smaller instances to solve the original problem.
'''

'''Simple recursive function- recursive factorial function'''
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)

'''Here, the time complexity of the recursive function is O(n).'''


'''
Notes:
a. Recursion uses a call stack: 
   - Each recursive function call is added to the call stack, and the computer keeps track of these calls in memory. 
     When the base case is reached, the function calls are resolved in reverse order, effectively "unwinding" the stack.
     However, each recursive call consumes memory, and too many recursive calls can lead to a stack overflow.
     It's especially useful for solving problems that have a recursive structure, such as those involving tree and graph 
     data structures.
'''