# Grapth Theory Project #

## User Guide ##
Command to run Program(Go to the project folder "Thompsons"):
    Python regex.py

* You will then be propted to enter an option from the menu
    * "Press 1 to run an array of infix expressions with strings
    * Press 2 to enter a Regular Expression and String to test it:"

* If 1 is entered a list of regular expressions and strings will be displayed and 
wheather or not the string can pass through the expression (e.g. True a.b? ab).
* If 2 is entered, the user will be promped to enter a regular expression and 
a string to pass through it. If it is True or False will be output to the user.


## Explaining The Operators in the Code: ##

### Shunting Yard Algorithm code explanation ###
The Shunting Yard Algorithm is for converting infix regular expressions to postfix.
An infix expressiona and a string to test it with are parameters for the fucntion. 
It has a dictionary of special characters for regular expressions and their precidence. 
A postfix expression will eventually be the output of the function. 
Loop throuh the string, a character at a time. 
using an if elif check for brackets and change the expression appropriatly. 
If the character is an operator, it is put in the correct place in the statement using a while loop checking for precedence. 
When regular characters are encountered they are pushed immediately onto the postfix expression. 
Pop all remaining operators from the stack to the postfix expression. 
Return Postfix Regular Expression. 

### Matching and following 'E' arrows code explanation ###
The main fucntion of the "folloes()" function is to Return the set of states that can be 
reached from state following e arrow and test expression against strings. 
The followes() function is useed to find all the states where the 'E' arrows point. 
It check if state has arrows labelled e from it and if there is an edge1, follow it
and or if there's an edge2, follow it . 
Return the set of states where the 'E' arrows point.

The 'match()' function matches string to infix regular expression with case insensitive matching. 
It sends the infix expression to the Shunt.py file and the postfix regex to the Thompsons.py file, 
which returns an nfa. 
'match()' then gets the current set of states and the next set of states. 
Then each character on the string is looped through the expression. 
If the current set of states is in the accept state of the nfa then it returns "true".
Input menu with user options 

### Thompsons Algorithm code explanation ###
__Dot__
When The "."(dot) character is encountered in an infix Regular Expression it pops 
the last two NFA's from the stack, NFA2 and NFA1. They are then joined by an 'E' 
arrow from NFA1's accept state to NFA2's initial state (NFA1,.accept.edge1=NFA2.initial)
![Imgur](https://i.imgur.com/1CbJa9I.jpg)

__Verticle Bar__
When The "|"(verticle bar) character is encountered in an infix Regular Expression it pops 
the last two NFA's from the stack, NFA2 and NFA1. A new initial state and a new accept 
state is created. The new intial state is joined by 'E' arrows to both the initial states 
of NFA1 and NFA2. The accept states of NFA1 and NFA2 are joined by 'E' arrows to the new 
accept state.  (NFA1,.accept.edge1=accept)
![Imgur](https://i.imgur.com/83P2N6u.jpg)

__Star__
When The "*"(star) character is encountered in an infix Regular Expression it pops 
the last NFA from the stack, NFA1. A new initial state and a new accept state is created. 
The new intial state is joined by 'E' arrows to both the initial state of NFA1 and 
the new accept state. Then NFA1's accept state joins by 'E' arrows to both NFA1's initial 
state and the new accept state (NFA1,.accept.edge1=NFA1.initial)
![Imgur](https://i.imgur.com/22vaqGr.jpg)

__Plus__
When The "+"(plus) character is encountered in an infix Regular Expression it pops 
the last NFA from the stack, NFA1. A new initial state and a new accept state is 
created. The new intial state is joined by an 'E' arrow to the initial state of NFA1. 
Then NFA1's accept state joins by 'E' arrows to both NFA1's initial state and the new 
accept state (NFA1,.accept.edge1=NFA1.initial)
![Imgur](https://i.imgur.com/LBfmxtJ.jpg)

__Question Mark__
When The "?"(question mark) character is encountered in an infix Regular Expression it pops 
the last NFA from the stack, NFA1. A new initial state and a new accept state is created. 
The new intial state is joined by 'E' arrows to both the initial state of NFA1 and the new 
accept state. Then NFA1's accept state joins by an 'E' arrow to the new accept state 
(NFA1,.accept.edge1=accept)
![Imgur](https://i.imgur.com/TE5FNza.jpg)
