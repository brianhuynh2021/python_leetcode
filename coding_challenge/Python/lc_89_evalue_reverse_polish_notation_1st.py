"""
✅ Problem Statement
Given a list of tokens representing an arithmetic expression in 
Reverse Polish Notation, evaluate the expression.
Example input:
    tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
Output: 14
📘 Principle: How to Read RPN (Reverse Polish Notation)

🧠 General Rule:

Read tokens from left to right.
If it’s a number, push it onto the stack.
If it’s an operator (+, -, *, /),
→ pop the top two numbers, apply the operator,
→ then push the result back onto the stack.
"""

def evaluate_reverse_polish_notation(tokens: list[str])->int:
    if not tokens:
        raise ValueError("Invalid RPN: empty input")
    n = len(tokens)
    if n == 1:
        if tokens[0].lstrip("-").isdigit(): # syntax that lstrip("-") remove the sign - in the string if exist
            return int(tokens[0])           # then that string is digit
        else:
            raise ValueError("Invalid RPN: not enough operands")
    
    stack = []
    for c in tokens:
        if c in "*/+-":
            if len(stack) < 2:
                raise ValueError("Invalid RPN: not enough operands")
            b = stack.pop()
            a = stack.pop()
            if c == '*':
                result = a * b
            elif c == '/':
                result = int(a / b)
            elif c == "+":
                result = a + b
            elif c == "-":
                result = a - b
            # We can use lambda more pythonic
            '''
            ops = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a -b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: int(a / b)
            }
            
            result = ops[c](a, b)
            '''
            stack.append(result)
        else:
            if c.lstrip("-").isdigit():
                stack.append(int(c))
            else:
                raise ValueError(f'Invalid token {c}')
        
    if len(stack) != 1:
        raise ValueError('Invalid RPN: leftover items in stack')
    return stack[0]