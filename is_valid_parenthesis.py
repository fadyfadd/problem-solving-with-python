def is_valid_parenthesis(s: str) -> bool:
    stack = []

    for c in s:
        if c in "({[":
            stack.append(c)
        else:
            if not stack:
                return False
            if c not in ")}]":
                continue

            top = stack.pop()
            if (c == ')' and top != '(') or \
               (c == '}' and top != '{') or \
               (c == ']' and top != '['):
                return False

    return len(stack) == 0

# Example usage:
s = "{[()]}"
print(is_valid_parenthesis(s))  # Output: True
