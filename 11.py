# Conditional Statements

# Two numbers example
"""
print("Enter two numbers:")
print("Enter a : ")
a = int(input())
print("Enter b : ")
b = int(input())

if a>b:
    print("a is greater")
elif a == b:
    print("Numbers are Equal")
else:
    print("b is Greater")
"""

# Admin Example
user = "Admin"
logged_in = "true"
if user == "Admin" and logged_in:
    print(("Welcome to {} Dashboard").format(user))
else:
    print("Sign up for a new Account")

if not logged_in:
    print("Please log in to continue")
else:
    print("Welcome")
