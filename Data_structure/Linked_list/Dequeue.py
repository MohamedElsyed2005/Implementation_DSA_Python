"""
Implement Linked Double-Ended Queue (Dequeue) using singly linked list:

Singly linked list --> each node has one linked-field following the direction of deletion of nodes(from top to bottom in stacks and from front to rear in queues)

--> void create():                 initilize the dequeue.
--> void insertFront(int value):   takes an integer value and insert it at the front of the dequeue.
--> void insertRear(int value):    takes an integer value and insert it at the rear of the dequeue.
--> int removeFront():             removes the front node from the dequeue and returns its value.
--> int removeRear():              removes the rear node from the dequeue and returns its value.
--> int size():                    returns an integer, the number of elements in the dequeue
"""

class Node:
    
    def __init__(self, Data):
        """
        Represents a node in the singly linked list.
            -> Data: Holds the data stored in the node.
            -> next: Points to the next node in the list (or None if it is the last node).
        """
        self.Data = Data
        self.next = None

class dequeue:
    
    def __init__(self):
        """
        Initializes an empty double-ended queue (deque).
            -> self.F: Points to the front (head) of the deque.
            -> self.R: Points to the rear (tail) of the deque.
            -> self._size: Tracks the current number of elements in the deque.
        """
        self.F = None
        self.R = None
        self._size = 0 #_size is private 

    def insertFront(self, value: int):
        """
        Inserts a new value at the front of the deque.
            -> If the deque is empty, the new node becomes both the front and rear.
            -> If not empty, the new node is added before the current front.
        """
        # isinstance check if value is int ( -> True) or (not -> False)
        assert isinstance(value, int), "the dequeue value must be integers" #enforce data type checking at runtime based solely on type annotations.
        new_node = Node(value)
        if self.F is None: # If deque is empty
            self.F = self.R = new_node
        else: # Add the new node at the front
            new_node.next = self.F
            self.F = new_node 
        self._size +=1

    def insertRear(self, value: int):
        """
        Inserts a new value at the rear of the deque.
            -> If the deque is empty, the new node becomes both the front and rear.
            -> If not empty, the new node is added after the current rear.
        """
        """ 
        --> Assert -> if condition is true: program continue to run.
                   -> if condition is false: program stops program and gives assertion error
        """
        assert isinstance(value, int), "the dequeue value must be integers" 
        new_node = Node(value)
        if self.R is None: # If deque is empty
            self.F = self.R = new_node 
        else:  # Add the new node at the rear
            self.R.next = new_node
            self.R = new_node
        self._size += 1

    def removeFront(self) -> int:
        """
        Removes the front node of the deque and returns its value.
           -> Raises an exception if the deque is empty.
           -> Updates the rear to None if the deque becomes empty after removal.
        """
        if self.F is None:
            raise IndexError("Dequeue underflow: Cannot remove from front, the dequeue is empty")
        Data = self.F.Data
        self.F = self.F.next
        if self.F is None:
            """
            It handles a special case when the dequeue becomes empty after removing the front element. 
            in last node self.F = self.F.next = None then make self.R = None to become an empty dequeue
            """
            self.R = None
        self._size -= 1
        return Data

    def removeRear(self) -> int :
        """
        Removes the rear node of the deque and returns its value.
            -> Raises an exception if the deque is empty.
            -> If there is only one node, resets both front and rear to None.
        """
        if self.R is None:
            raise IndexError("Dequeue underflow: Cannot remove from Rear, the dequeue is empty")
        if self.F == self.R:
            Data = self.R.Data
            self.F = self.R = None
        else: # Traverse the list to find the second last node
            current_node = self.F
            while current_node.next != self.R:
                current_node = current_node.next
            Data = self.R.Data
            current_node.next = None
            self.R = current_node
        self._size -= 1
        return Data 

    def size(self) -> int:
        """
        Returns the number of elements in the deque.
        """
        return self._size
    
    def Display(self):
        """
        Displays all elements in the deque from front to rear.
        """
        current_node = self.F
        all_elements = []
        while current_node:
            all_elements.append(current_node.Data)
            current_node = current_node.next
        print(f"All dequeue elements: {all_elements}")

if __name__ == '__main__':
    deque = dequeue()
    deque.insertFront(4)
    deque.Display()
    deque.insertRear(5)
    deque.Display()
    deque.insertFront(3)
    deque.Display()
    deque.removeRear()
    deque.Display()
    print(f"Size of dequeue is {deque.size()}")
    deque.insertFront(1)
    deque.Display()
    deque.insertRear(5)
    deque.Display()
    deque.insertFront(4)
    deque.Display()
    deque.removeFront()
    deque.Display()
    print(f"Size of dequeue is {deque.size()}")