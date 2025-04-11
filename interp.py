######################################
#  Interpreter for the B++ language  #
######################################

import sys
class Ev:
    def ev(self, s):
        lines = [x for x in s.split("\n") if x.strip() != ""] # Split into new lines and throw away empty lines
        for line in lines:
            print(self.ev_expr(line)) # Evaluate each line
    def ev_expr(self, s): # Single expression evaluator function
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
        return stack[0] # Return result
Ev().ev(open(sys.argv[1]).read())
