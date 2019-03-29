# Matching Regular Expressions with Strings using Thompsons Construction and Shunting Yard Algorithm
# James Mullarkey

# Importing function from another python file
from shunt import shunt
# Importing function from another python file
from thompsons import compile

def followes(state):
    """Return the set of states that can be reached from state following e arrows"""
    # Create a new set, with state as its only member
    states = set()
    states.add(state)

    # Check if state has arrows labelled e from it
    if state.label is None:
        # Check if edge1 is a state
        if state.edge1 is not None:
            # if theres an edge1, follow it
            states |= followes(state.edge1)
        # Check if edge2 is a state 
        if state.edge2 is not None:
            # If there's an edge2, follow it
            states |= followes(state.edge2)
    
    # Return the set of states
    return states

def match(infix, string):
    """Matches string to infix regular expression"""
    # shunt and compile the regular expression
    postfix = shunt(infix)
    nfa = compile(postfix)

    # the current set of states and the next set of states
    current = set()
    next = set()

    # Add the initial state to the current set
    current |= followes(nfa.initial)

    # loop through set of character in the string
    for s in string:
        # Loop through the current set of states
        for c in current:
            # Check if that state is labelled s
            if c.label == s:
                # Add the edge1 state to the next set
                next |= followes(c.edge1)
        # Set current to next, and clear out next
        current = next
        next  = set()

    # Check if the accept state is in the set of current states
    return (nfa.accept in current)

test, userInput = 1, 2
option = input("Press 1 to run an array of infix expressions with strings " + 
"\nPress 2 to enter a Regular Expression and String to test it: ")

# Casting option to an int
option = int(option)
if option == test:
    # A few tests
    infixes = ["a.b?","a.b.c?", "a.(b|d).c+", "(a.(b|d))*", "a.(b.b)*.c"]
    strings = ["ab", "abc", "abbc", "abcc", "abad", "abbbc"]
    for i in infixes:
        for s in strings:
         print(match(i, s), i, s)

elif option == userInput:
    infix = input("Please enter an infix Regular Expression: ")
    stri = input("Please enter a String to test your Regular Expression: ")
    print(match(infix, stri), infix, stri)