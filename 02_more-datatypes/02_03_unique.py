# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]
list1 = [1, 32, "halloween", 32, 42, 99, 24, "happy", 13, "happy", 1]
unique_list = [word for word in list1 if list1.count(word) == 1]
print(unique_list)

