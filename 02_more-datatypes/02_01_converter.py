# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
tup = tuple(string)
print(tup)
for x in tup:
    print(x)
for x in string:
    print(x)

# string = "codingnomads"

# tup = tuple(string)
# print(tup)

# tup1 = 1, 2, "hello"
# print(tup1)
# for element in tup1:
#     print(element)
# for user in ("David", "Alice", "Lucy"):
#     print(user)
