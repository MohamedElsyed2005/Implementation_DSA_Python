from Data_structure.Linear_list.Stack import Stack

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
                return "Not Balanced"  # Unbalanced if stack is empty
            if char == '}' and stack.get_top() == '{':
                stack.pop()
            elif char == ']' and stack.get_top() == '[':
                stack.pop()
            elif char == ')' and stack.get_top() == '(':
                stack.pop()
            else:
                return "Not Balanced"  # Mismatch case
        elif char in {'(', '[', '{'}:
            stack.push(char)
        else:
            return "illegal char in input"
    
    if not stack.isEmpty():
        return "Not Balanced"
    else:
        return "properly Nested stucture"  # Balanced if stack is empty

if __name__ == '__main__':
    s = input("Enter your text: ")
    print(isValid(s))
