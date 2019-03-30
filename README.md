# Grapth Theory Project #

"# ThompsonsPython" 

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
