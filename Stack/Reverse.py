from Stack import Stack

def reverse_string(string):
    """
    This method also works but not as practical as the one below
    s = Stack()
    reversed_string = ""
    for i in range(len(string)):
        s.push(string[i])
    for j in range(len(string)):
        reversed_string += s.pop()
    return reversed_string
    """
    for i in range(len(string)):
        stack.push(string[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


stack = Stack()
print(reverse_string("Strike"))