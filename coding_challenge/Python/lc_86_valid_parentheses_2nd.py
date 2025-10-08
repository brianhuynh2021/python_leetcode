def valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in "({[":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                top = stack.pop()
                if mapping[c] != top:
                    return False
    return not stack


assert valid_parentheses("()") == True
assert valid_parentheses("()[]{}") == True
assert valid_parentheses("([)]") == False
assert valid_parentheses("{[]}") == True
assert valid_parentheses("") == True
assert valid_parentheses("(") == False
assert valid_parentheses("]") == False
print("✅ All test cases passed!")
