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

class SequentialStack:
    # create operation 
    def __init__(self, size):
        self.size = size
        self.S = [None] * size 
        self.top = -1

    def push(self, element):

        if self.isFull():
            print("Stack overflow: Cannot push, the stack is full.")
            return
        self.top += 1
        self.S [self.top] = element
    
    def pop(self):

        if self.isEmpty():
            print("Stack underflow: Cannot pop, the stack is empty.")
            return
        element = self.S[self.top]
        self.S[self.top] = None
        self.top -=1
        return element
    
    def isEmpty(self):

        if self.top == -1:
            return True
        else: return False
    
    def isFull(self):
        
        if (self.top + 1) == self.size :
            return True
        else: return False

    def Display(self):

        print("Stack contents:", self.S)

if __name__ == "__main__":

    stack = SequentialStack(4)
    stack.push(2)
    stack.pop()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(50)
    stack.push(70)
    stack.Display()