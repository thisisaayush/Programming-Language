'''
1. Stack: A stack is a fundamental data structure in computer science that follows the Last-In-First-Out (LIFO) principle.
       In a stack, the most recently added item is the first to be removed. Think of a stack like a stack of plates:
       you add or remove plates from the top of the stack, not the middle or the bottom.

2. A stack has three primary operations:
   a. Push: This operation adds an element to the top of the stack. It's equivalent to placing a plate on top of the stack
      of plates.
   b. Pop: This operation removes the element from the top of the stack. It's equivalent to taking the top plate off the
      stack.
   c. Peek or Top: This operation allows you to look at the top element of the stack without removing it.

3. Common use of Stack:
   a. Function Call Management: Stacks are used in programming languages to keep track of function calls. When a function
      is called, its local variables and execution context are pushed onto the stack, and when the function returns,
      it is popped off the stack.

   b. Expression Evaluation: Stacks are used in evaluating arithmetic expressions, like converting infix expressions
      (e.g., 2 + 3) to postfix (2 3 +) and then evaluating them.

   c. Undo/Redo Functionality: Many applications use stacks to implement undo and redo features. Each action is pushed
      onto the stack, and undo/redo operations pop from or push to the stack.

   d. Backtracking Algorithms: Stacks are used in backtracking algorithms, like depth-first search in graphs or solving
   puzzles like the Tower of Hanoi.
'''