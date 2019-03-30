# Thompsons Construction
# James Mullarkey

# Represents a state with two arrows labelles by label
# Use None for a label represenring "e" arrows
class state:
    label, edge1, edge2 = None, None, None

# An NFA is a represented by its initial and accept states
class nfa:
    initial, accept = None, None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept 

def compile(postfix):
    """Compiles a postfix regular expression into a NFA"""

    nfastack = []

    for c in postfix:
        if c == '.':
            # pop two NFA's off the stack
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Connect first NFA's accept state to the second's initial.
            nfa1.accept.edge1 = nfa2.initial
            # Push NFA to the stack
            nfastack.append(nfa(nfa1.initial, nfa2.accept))
        elif c == '|':
            # pop two NFA's off the stack
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Creat new initial and accept states
            # Connect it to initial states of the two NFA's popped from the stack.
            accept, initial  = state(), state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            # Create a new accept state, connecting the new accept states
            # of the thwo NFA's popped from the stack, to the new state.
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            # Push new NFA to the stack
            nfastack.append(nfa(initial, accept))
        elif c == '*':
            # Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # Creat new initial and accept states
            accept, initial  = state(), state()
            # Join the new initial state to nfa1's initial state and the new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # Join the old accept state to the new accept state and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # Push new NFA to the stack
            nfastack.append(nfa(initial, accept))
        elif c == '+':
            # Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # Creat new initial and accept states
            accept, initial  = state(), state()
            # Join the new initial state to nfa1's initial state 
            initial.edge1 = nfa1.initial
            # Join the old accept state to the new accept state and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # Push new NFA to the stack
            nfastack.append(nfa(initial, accept))
        elif c == '?':
            # Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # Creat new initial and accept states
            accept, initial  = state(), state()
            # Join the new initial state to nfa1's initial state 
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # Join the old accept state to the new accept state
            nfa1.accept.edge1 = accept
            # Push new NFA to the stack
            nfastack.append(nfa(initial, accept))
        else: 
            # Create new initial and accept states
            accept, initial  = state(), state()
            # Join the initial state and the accept state using an arrow labelled c.
            initial.label = c
            initial.edge1 = accept
            #Push new NFA to the stack
            nfastack.append(nfa(initial, accept))

    # nfastack should only have a single nfa on it at this point
    return nfastack.pop()