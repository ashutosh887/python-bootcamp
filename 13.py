# Functions

'''
print("Enter your Name: ", end="")
name = input()
print("Enter your Age: ", end="")
age = input()

print("Calling the function: ")
myFirstFunction(name, age)
'''

def myFirstFunction(name, age):
    print(("Hello {}!").format(name))
    print(("We got to know that your age is {}").format(age))

print("\nUsing our function for a Dictionary...")
data = {
    "A":1,
    "B":2,
    "C":0
}

for key,value in data.items():
    print(myFirstFunction(key, value))

