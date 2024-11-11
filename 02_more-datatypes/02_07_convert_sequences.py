# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
tup = tuple(string)
tuple_to_list = list(tup)
tuple_to_list[0] = "k"
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)
print(tuple_to_list)
print(tup)
# print(string)

