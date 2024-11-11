# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}
user_string = input("What is your favorite word?: ")
char_count_dict = {char: user_string.count(char) for char in user_string}
print(char_count_dict)