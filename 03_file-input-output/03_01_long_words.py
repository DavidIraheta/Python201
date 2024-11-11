# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
# with open("/Users/davidiraheta/Documents/CodingNomads/Projects/python-201-main/03_file-input-output/words.txt", "r") as file:
#     long_words = file.read().split()
#     for word in long_words:
#         if len(word) > 20:
#             print(word)
# def greet (greeting, name):
#     sentence = f"{greeting} {name}! How it be?"
#     return sentence
# print(greet("Hello", "David"))

import os

cwd = os.getcwd()
print(cwd)