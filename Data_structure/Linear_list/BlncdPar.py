from Stack import Stack

"""
Check for balancing of parentheses, brackets, and braces.
Valid input characters: (, ), {, }, [, ]
"""

def isValid(s):
    size = len(s)
    stack = Stack(size)  # Initialize stack with given size

    for char in s:
        if char in {')', ']', '}'}:
            if stack.isEmpty():
                return False  # Unbalanced if stack is empty
            if char == '}' and stack.get_top() == '{':
                stack.pop()
            elif char == ']' and stack.get_top() == '[':
                stack.pop()
            elif char == ')' and stack.get_top() == '(':
                stack.pop()
            else:
                return False  # Mismatch case
        else:
            stack.push(char)
    
    stack.Display()
    return stack.isEmpty()  # Balanced if stack is empty

if __name__ == '__main__':
    s = input("Enter your text: ")
    if isValid(s):
        print("Balanced")
    else:
        print("Not Balanced")
