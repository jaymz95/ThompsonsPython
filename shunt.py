# James Mullarkey
# Shunting Yard Algorithm
# http://www.oxfordmathcenter.com/drupal7/node/628

def shunt(infix):
    """The Shunting Yard Algorithm for converting infix regular expressions to postfix."""
    # special characters for regular expressions and their precidence
    specials = {'?': 50,'+': 50,'*': 50, '.': 40, '|': 30}

    # pofix will eventually be the output and operator stack
    pofix, stack = "", ""

    # loop throuh the string a character at a time
    for c in infix:
        if c== '(': # If an open bracket, push to the stack
            stack = stack + c
        elif c == ')': # If a closing bracket, pop from the stack, push to output until open bracket
            while stack[-1] != '(':
                pofix  = pofix + stack[-1]
                stack = stack[:-1]
            stack = stack[:-1]
        # If it's an operator, push to the stack after popping lower or equal precedence
        # operators from top of stack into output
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix  = pofix + stack[-1]
                stack = stack[:-1]
            stack = stack + c
        else: # Regular characters are pushed immediately to the output
            pofix = pofix + c
    while stack: # Pop all remaining operators from the stack to output
        pofix  = pofix + stack[-1]
        stack = stack[:-1]
    
    # Return postfix regex
    return pofix