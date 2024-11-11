# Sentence Analysis Tool
# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

# # Note: ignore all spaces.
count_dict = {"lowercase_letters": 0, "uppercase_letters": 0, "punctuation_characters": 0, "total_characters": 0}
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~."
total_characters = {}
advice = input("Please tell me your favorite travel destination and why: ")
for char in advice:
    if char in lowercase_letters:
        count_dict["lowercase_letters"] += 1
    if char in uppercase_letters:
        count_dict["uppercase_letters"] += 1
    if char in punctuation_characters:
        count_dict["punctuation_characters"] += 1
    if char != " ":
        count_dict["total_characters"] += 1
print(count_dict)
