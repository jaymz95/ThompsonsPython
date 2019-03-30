# James Mullarkey
# Shunting Yard Algorithm
# http://www.oxfordmathcenter.com/drupal7/node/628

def toPostfix(infix):
    """The Shunting Yard Algorithm for converting infix regular expressions to postfix."""
    # special characters for regular expressions and their precidence
    specials = {'?': 50,'+': 50,'*': 50, '.': 40, '|': 30} # dictionary

    # postfix will eventually be the output and operator stack
    postfix, stack = "", ""

    # loop throuh the string a character at a time
    for c in infix:
        if c== '(': # If an open bracket, push to the stack
            stack = stack + c
        elif c == ')': # If a closing bracket, pop from the stack, push to output until open bracket
            while stack[-1] != '(': # checks if the last char in the stack is '('
                postfix = postfix + stack[-1]
                stack = stack[:-1] # taking the last char in the stack off the stack
            stack = stack[:-1] # removes the '(' from the stack
        # If it's an operator, push to the stack after popping lower or equal precedence
        # operators from top of stack into output
        elif c in specials:
            # checks stack is not null and if the special character in c is lessthan 
            # or equal to the char at the top off the stack
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0): 
                # takes char off the stack and puts it on the postfix regex
                postfix  = postfix + stack[-1]
                stack = stack[:-1]
            stack = stack + c
        else: # Regular characters are pushed immediately to the output
            postfix = postfix + c
    while stack: # Pop all remaining operators from the stack to output
        postfix  = postfix + stack[-1]
        stack = stack[:-1]
    
    # Return postfix regex
    return postfix