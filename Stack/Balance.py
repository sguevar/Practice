from Stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:  # for(int i = 0; i < paren_string.length() && is_balanced; i++);
        paren = paren_string[index]
        if paren in "([{":  # If index is one of three opening brackets, push it to stack
            s.push(paren)
        else:
            if s.is_empty():  # If Stack is empty, then it is not balanced
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False




print(is_paren_balanced("())"))
print(is_paren_balanced("()"))
