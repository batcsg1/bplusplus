######################################
#  Interpreter for the B++ language  #
######################################

import sys
def ev(s): # Evaluation function
    toks = s.split() # Split a line into tokens
    stack = [] # Create an empty stack

    # Operators
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    for tok in toks:
        if tok.isnumeric(): stack.append(int(tok)) # Append numbers to the stack
        elif tok == "+":
            rhs = stack.pop() # Remove two numbers from stack
            lhs = stack.pop()
            stack.append(lhs + rhs) # Append result to stack
    print(stack[0]) # Print value

    #print(toks) # Print tokens
ev(open(sys.argv[1]).read())
