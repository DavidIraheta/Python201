# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here
# r = randlist
# r.sort()
# sorted_list = []
# for i in range(0, len(r), 2):
#     if i == len(r) - 1:
#         print((r[i], 0))
#     else:
#      sorted_list.append((r[i], r[i+1]))
# for i in sorted_list:
#     print(i)
r = randlist
r.sort()
if len(r) % 2 != 0:
    r.append(0)
r = [(r[i], r[i+1]) for i in range(0, len(r), 2)]
for i in r:
    print(i)
    





# r = [(r[i], r[i+1]) for i in range(0, len(r), 2)]
# for i in r:
#     print(r)
