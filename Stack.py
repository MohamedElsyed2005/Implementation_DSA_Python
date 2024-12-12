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
    # create operation 
    def __init__(self, size):
        self.size = size
        self.S = [None] * size # [None, None, None ,None]
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

import matplotlib.pyplot as plt
import networkx as nx

# Create the game tree as a graph
game_tree = nx.DiGraph()

# Add nodes (state) and terminal states with values
# Format: (Player A position, Player B position)
game_tree.add_node("Start", label="(1, 4)")

# Level 1: Player A's moves
game_tree.add_node("A: (2, 4)", label="(2, 4)")
game_tree.add_edge("Start", "A: (2, 4)")

# Level 2: Player B's response
game_tree.add_node("B: (2, 3)", label="(2, 3)")
game_tree.add_edge("A: (2, 4)", "B: (2, 3)")

# Level 3: Player A moves again
game_tree.add_node("A: (3, 3)", label="(3, 3)")
game_tree.add_edge("B: (2, 3)", "A: (3, 3)")

# Terminal State: A wins
game_tree.add_node("A Wins", label="Terminal (+1)")
game_tree.add_edge("A: (3, 3)", "A Wins")

# More branches can be added for full exploration

# Draw the game tree
pos = nx.spring_layout(game_tree)  # Layout for visualization
labels = nx.get_node_attributes(game_tree, 'label')
plt.figure(figsize=(10, 6))
nx.draw(game_tree, pos, with_labels=False, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
nx.draw_networkx_labels(game_tree, pos, labels, font_size=10)
plt.title("Partial Game Tree for Two-Player Game")
plt.show()
