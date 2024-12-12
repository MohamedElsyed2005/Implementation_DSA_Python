"""
Queue:
       	FIFO (First in first out) or FCFS (First come first served).
       	Insert is called enqueue.
       	Delete is called dequeue.
       	All this manipulation with two pointers called rear(last) and front (first).
       	Rear to insert and front to delete.

Implementation of Sequential Queue

Basic operation on stack:
       o	Create: create an empty queue.
       o	enqueue: insert an element at rear of queue.
       o	dequeue: retrieve and remove the element at front of queue.
       o	Empty: test whether queue is empty.
       o	Full: test whether queue is full.

Two types of errors are possible:
       o	Overflow: an enqueue operation was applied to a full queue.
       o	Underflow: a dequeue operation was applied to an empty queue.

Operations:
       o	  An array Q of elements and size is max.
       o	  An index F (one element before the current first element) and R (at rear of queue).

Initially, F = 0 and R = 0
"""

class Queue:

    def __init__(self,size):
        self.size = size
        self.Q = [None] * size 
        self.R , self.F = -1 , -1

    def enqueue(self,element):
        
        if self.R == self.size + 1 :
            print("Queue overflow: Cannot enqueue, the queue is full.")
            return
        self.R += 1
        self.Q[self.R] = element

    def dequeue(self):

        if self.R == self.F == -1 :
            print("Queue underflow: Cannot enqueue, the queue is empty.")
            return
        self.F += 1
        element = self.Q[self.F]
        self.Q[self.F] = None
        if self.R == self.F != -1:
            self.R , self.F = -1 , -1 
        return element
    
    def Display(self):

        print("Queue contents:", self.Q)

if __name__ == "__main__":

    qu =  Queue(4)
    qu.enqueue(4)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.dequeue()
    qu.dequeue()
    qu.enqueue(3)
    qu.enqueue(3) # here there error so we gonna use circular queue
    qu.Display()

