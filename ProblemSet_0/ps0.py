"""
Problem Set 0

Write a program that does the following in order:
    
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.

Use Spyder to create your program, and save your code in a file named ‘ps0.py’. 
An example of an interaction with your program is shown below. 
The words printed in blue are ones the computer should print, 
based on your commands, while the words in black are an example of a user's input. 
The colors are simply here to help you distinguish the two components.

Enter number x: 2
Enter number y: 3
X**y = 8
log(x) = 1
"""

import numpy as np

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

print("x**y =", x**y)
print("log(x) = ", int(np.log2(x)))
