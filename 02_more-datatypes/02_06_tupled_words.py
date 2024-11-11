# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

# user_string = input("What are some things unique about fall?: ")
# words = user_string.split()
# print(words)

# result_list = []
# for word in words:
#     result_list.append(tuple(word))
# print(result_list)

user_string = input("What are some things unique about fall?: ")
fall = user_string.split()
print(fall)
result_list = [tuple(fall) for word in fall]
print(result_list)

