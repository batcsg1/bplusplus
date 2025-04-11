######################################
#  Interpreter for the B++ language  #
######################################

import sys
def ev(s): # Evaluation function
    toks = s.split() # Split a line into tokens
    print(toks) # Print tokens
ev(open(sys.argv[1]).read())
