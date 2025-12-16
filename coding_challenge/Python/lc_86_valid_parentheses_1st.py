"""
✅ Problem Definition

Given a string s containing only the characters ()[]{}, determine if the input string is valid.

👉 A string is valid if:
	1.	Open brackets are closed by the same type of brackets.
	2.	Open brackets are closed in the correct order.
	3.	Every closing bracket has a corresponding opening bracket.

📥 Input
	•	s: a string containing only these 6 characters: '(', ')', '{', '}', '[', ']'

⸻

📤 Output
	•	True if the parentheses are valid
	•	False otherwise
"""


def valid_parentheses_optimized(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}  # 🔁 match closing to opening
    for c in s:
        if c in "({[":
            stack.append(c)
        else:
            if not stack:
                return False
            top = stack.pop()
            if mapping[c] != top:
                return False
    return not stack


assert valid_parentheses_optimized("()") == True
assert valid_parentheses_optimized("({[]})") == True
assert valid_parentheses_optimized("([)]") == False
assert valid_parentheses_optimized("{[}") == False



def valid_parentheses_replace(s: str) -> bool:
    prev = None
    while s != prev:
        prev = s
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return not s


def is_valid(s: str) -> bool:
    if not s:
        return True
    for i in range(1, len(s), 2):
        if (s[0], s[i]) in [("(", ")"), ("[", "]"), ("{", "}")]:
            if is_valid(s[1:i]) and is_valid(s[i + 1 :]):
                return True
    return False


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

def valid_parentheses_2(s: str) -> bool:
    if not s:
        return True
    for i in range(1, len(s), 2):
        if (s[0], s[i]) in [("(", ")"), ("[", "]"), ("{", "}")]:
            if valid_parentheses_2(s[1:i]) and valid_parentheses_2(s[i + 1 :]):
                return True
    return False

def valid_parentheses_3(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    prev = None
    while s != prev:
        prev = s
        s = (s.replace("[]", "")
             .replace("{}", "")
             .replace("()", ""))
    return s == ""