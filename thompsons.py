# Thompsons Construction
# James Mullarkey

def shunt(infix):
    """The Shunting Yard Algorithm for converting infix regular expressions 
    to postfix."""

    # special characters for regular expressions and their precidence
    specials = {'*': 50, '.': 40, '|': 30}

    # will eventually be the output
    pofix = ""
    # operator stack
    stack = ""

    # loop throuh the string a character at a time
    for c in infix:
        # If an open bracket, push to the stack
        if c== '(':
            stack = stack + c
        # If a closing bracket, pop from the stack, push to output until open bracket
        elif c == ')':
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
        # Regular characters are pushed immediately to the output
        else:
            pofix = pofix + c
    # Pop all remaining operators from the stack to output
    while stack:
        pofix  = pofix + stack[-1]
        stack = stack[:-1]

    return pofix

print(shunt("(a.b)|(c*.d)"))

# Represents a state with two arrows labelles by label
# Use None for a label represenring "e" arrows
class state:
    label = None
    edge1 = None
    edge2 = None

# An NFA is a represented by its initial and accept states
class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept 

def compile(profix):
    nfastack = []

    for c in profix:
        if c == '.':
            # pop two NFA's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Connect first NFA's accept state to the second's initial.
            nfa1.accept.edge1 = nfa2.initial
            # Push NFA to the stack
            nfastack.append(nfa(nfa1.initial, nfa2.accept))
        elif c == '|':
            # pop two NFA's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Create a new initial state, connect it to initial states
            # of the two NFA's popped from the stack.
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            # Create a new accept state, connecting the new accept states
            # of the thwo NFA's popped from the stack, to the new state.
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            # Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '*':
            # Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # Creat new initial and accept states
            initial = state()
            accept = state()
            # Join the new initial state to nfa1's
            # initial state and the new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # Join the old accept state to the new accept
            # state and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        else: 
            # Create new initial and accept states
            accept  = state()
            initial = state()
            # Join the initial state and the accept state
            # using an arrow labelled c.
            initial.label = c
            initial.edge1 = accept
            #Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

    # nfastack should only have a single nfa on it at this point
    return nfastack.pop()

print(compile("ab.cd.|"))
print(compile("aa.*"))