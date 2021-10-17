# Doc String
# Used to add implementation or pass important messages along with the function

def function_for_sum(a, b):
    """This is a function to return the sum and average of two numbers"""
    print("SUM : ",(a+b))
    print("Average: ",(a+b)/2)

print("Read this,\nThe Doc String of the above function ", end="--> ")
print(function_for_sum.__doc__)
function_for_sum(1,3)
