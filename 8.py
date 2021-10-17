# Dictionary
# Collection of key value pairs
# Keys must be Immutable

print("Example of a Dictionary")
a = {
    "name": "Ashutosh",
    "role": {
        "first": "student",
        "second": "programmer",
        "third": "artist"
    },
    "qualification": "null"
}

print(a)
print("Name: ", a["name"])
print("Roles...")
print(a["role"]["first"])
print(a["role"]["second"])
print(a["role"]["third"])
print("Qualification: ", a["qualification"])

# Key can be a String or a Number
print("\nCreating a new Dictionary")
d = {"my": "second dictionary"}
d[1] = "Okay"
d["Google"] = "Google"

print(d)

# Deleting value from Dictionary

print("\nDeleting from the Dictionary")
del d["my"]
print(d)
del d[1]
print(d)


"""
d2 = d
This will create a reference of the list d and operations performed on d2 will be reverted to d also

To avoid this conflict, we should use
d2 = d.copy()
"""

print("Some dictionary functions: ")
    # .get()
    # .update()  or dict["key:] = "new value"
    # .keys() = Prints all the keys
    # .items() = Prints key value pairs
    # dictionary-name.values()
    # for key, value in student.items():
    #     print(key, value)

    # .get("key-name", "default value")     Returns the default-value if the key is not found...