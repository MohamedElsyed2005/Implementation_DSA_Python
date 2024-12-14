"""
Stack:
     	LIFO (last in first out) or FILO (first in last out)
     	Access, delete and insert are made at one end of the list called the top of the stack.
     	Insert called push or stacking.
     	Delete is called pop or unstacking.
     	All this manipulation with one pointer called stack pointer. Which points to the top element.

Basic operation on stack:
       o	Create: create an empty stack.
       o	Push: insert an element on top of the stack.
       o	Pop: retrieve and remove the element on top of the stack.
       o	isEmpty: test whether stack is empty.
       o	isFull: test whether stack is full.

Two types of errors are possible:
       o	Overflow: a push operation was applied to a full stack.
       o	Underflow: a pop operation was applied to an empty stack.

Operations:
       o	An array S of elements and size is max.
       o	An index top to element at top of stack.

"""

class Stack:
    """Implementation of a fixed-size stack."""
    # constructor __name__ magic method
    def __init__(self, size):
        """Create an empty stack with a fixed size."""
        self.size = size
        self.S = [None] * size # if size = 4 [None, None, None, None] ==> Initialize the stack with a fixed size
        self.top = -1  # Initialize the stack pointer to -1

    def push(self, element):
        """Insert an element on top of the stack."""
        if self.isFull():
            print("Stack overflow: Cannot push, the stack is full.")
            return
        self.top += 1
        self.S[self.top] = element

    def pop(self):
        """Retrieve and remove the top element of the stack."""
        if self.isEmpty():
            print("Stack underflow: Cannot pop, the stack is empty.")
            return None
        element = self.S[self.top]
        self.S[self.top] = None
        self.top -= 1
        return element

    def isEmpty(self):
        """Check if the stack is empty."""
        return self.top == -1

    def isFull(self):
        """Check if the stack is full."""
        return self.top + 1 == self.size

    def get_top(self):
        """Return the top element without removing it."""
        if self.isEmpty():
            print("Stack is empty: Nothing to peek.")
            return None
        return self.S[self.top]

    def Display(self):
        """Display the current stack contents."""
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack contents:", self.S[:self.top + 1]) 


# Example usage
if __name__ == "__main__":
    stack = Stack(5)  # Create a stack with size 5
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.Display()  # Output: [10, 20, 30]
    print("Top element:", stack.get_top())
    stack.pop()
    stack.Display()  # Output: [10, 20]
