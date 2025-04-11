######################################
#  Interpreter for the B++ language  #
######################################

import sys
class Ev:
    def ev(s): # Single expression evaluator function
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
            elif tok in ops:
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(ops[tok](lhs, rhs))
        print(stack[0]) # Print the result
        #print(toks) # Print tokens
Ev.ev(open(sys.argv[1]).read())
