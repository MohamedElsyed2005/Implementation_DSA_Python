from Data_structure.Linear_list.Stack import Stack

def invert_string(input_string):
    stack = Stack(80)
    print("Pushing characters onto the stack...")
    # Push all characters onto the stack
    for char in input_string:
        stack.push(char)
        print(f"Pushed: {char}")
    
    # Pop characters from the stack to form the inverted string
    print("Popping characters from the stack...")
    inverted_string = ""
    while not stack.isEmpty():
        popped_char = stack.pop()
        inverted_string += popped_char
        print(f"Popped: {popped_char}")
    
    return inverted_string

if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter a string or number to invert: ")
    print("Input String is:", user_input)
    print("Inverted String is:", invert_string(user_input))