"""
 and prints a greeting with user's name
"""
def greet(name):
    print("hello " + name)
"""
requests user to enter and name and returns it
"""
def name_input():
    name = input("Enter a name\n")
    return name

h = 1

greet(name_input())


