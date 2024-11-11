# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist
a = randlist
print(a)
a.sort()
print(a[-1])
# print(sum(a))
prod = 1
for x in a:
    prod *= x
print(prod)